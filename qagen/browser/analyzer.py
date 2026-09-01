"""Settle, extract, classify, verify -- one settled page becomes one PageModel.

Selector verification is the step that decides whether generated test cases are
usable. A locator that resolves to zero or many elements is downgraded through
the ladder; anything still ambiguous is flagged low-confidence. Without this,
the tool emits steps that look plausible and fail on first run -- which is worse
than emitting nothing.
"""

from __future__ import annotations

import asyncio
import logging
import time
from typing import Any, Callable

from playwright.async_api import Page

from ..config import RunConfig
from ..models import (
    Confidence,
    Element,
    ElementKind,
    FormField,
    FormSpec,
    Landmark,
    OverlaySpec,
    OverlayType,
    PageModel,
    SearchControl,
    is_actionable,
)
from .classify import classify
from .extract_js import CONSENT_JS, EXTRACT_JS, LOADER_JS, SIGNATURE_JS, TOOLTIP_JS
from .fingerprint import compute_fingerprint, normalize_url

log = logging.getLogger("qagen.analyzer")


def _consume_task_result(task: "asyncio.Task[Any]") -> None:
    """Retrieve a background task's outcome so asyncio stops warning about it.

    Deliberately not `await task`: awaiting a cancelled task raises
    CancelledError, which is a BaseException and escapes ordinary exception
    handling.
    """
    if task.cancelled():
        return
    try:
        task.exception()
    except Exception:  # pragma: no cover - defensive
        pass


class PageAnalyzer:
    def __init__(
        self,
        cfg: RunConfig,
        same_origin: Callable[[str], bool],
        destructive_match: Callable[[str], str | None],
        is_consent_text: Callable[[str], bool],
    ) -> None:
        self.cfg = cfg
        self._same_origin = same_origin
        self._destructive = destructive_match
        self._is_consent = is_consent_text

    # -- settle -----------------------------------------------------------
    async def settle(self, page: Page, quick: bool = False) -> str:
        """Wait for the page to stop changing. Returns the final signature.

        Three stages, because each one alone gets a real SPA wrong:

        1. ``domcontentloaded`` -- the shell exists.
        2. ``networkidle``, raced against a cap. A React route change resolves
           no request and fires no load event, and a polling app never goes
           idle at all, so this can only ever be a hint.
        3. **Hydration wait, then stability poll.** An app that has not
           rendered yet has a *stable empty* signature -- two consecutive empty
           reads would otherwise satisfy a naive stability check and we would
           extract an empty ``<div id="root">``. So we first wait for the page
           to have any interactive content, and only then wait for it to stop
           changing.
        """
        cap_ms = self.cfg.crawl.settle_timeout_ms
        hydrate_ms = self.cfg.crawl.hydration_timeout_ms
        if quick:
            # Restore attempts just need to see the page return to a known
            # signature; they are not capturing, so they need not wait out
            # progressive loading.
            cap_ms = min(cap_ms, 1500)
            hydrate_ms = min(hydrate_ms, 1500)

        try:
            await page.wait_for_load_state("domcontentloaded", timeout=cap_ms)
        except Exception:
            pass

        idle = asyncio.create_task(page.wait_for_load_state("networkidle", timeout=cap_ms))
        # Consume whatever the task ends up with, without awaiting it. Awaiting
        # a task we just cancelled re-raises CancelledError -- which inherits
        # from BaseException, so `suppress(Exception)` does NOT catch it and it
        # unwinds the whole crawl. A done-callback retrieves the result safely
        # and also silences "Task exception was never retrieved".
        idle.add_done_callback(_consume_task_result)
        try:
            await asyncio.wait_for(asyncio.shield(idle), timeout=cap_ms / 1000)
        except Exception:
            pass
        finally:
            if not idle.done():
                idle.cancel()

        # Stage 3a -- hydration.
        #
        # "Not empty" is not the same as "hydrated". A React shell commonly
        # renders one element (a spinner, a cookie close button) and sits there
        # for seconds while the bundle and the first API calls land. Breaking on
        # the first non-empty signature captures that shell -- and because it
        # then holds still, the stability check below happily declares it
        # settled. So wait for a non-trivial surface, not merely a non-empty one.
        hydrate_deadline = time.monotonic() + (hydrate_ms / 1000)
        minimum = self.cfg.crawl.hydration_min_elements
        current = ""
        while time.monotonic() < hydrate_deadline:
            try:
                current = await page.evaluate(SIGNATURE_JS)
            except Exception:
                return ""
            if current and len(current.split("|")) >= minimum:
                break
            await asyncio.sleep(0.2)
        else:
            log.debug(
                "page did not reach %d elements within %dms: %s",
                minimum, hydrate_ms, page.url,
            )

        # Stage 3a2 -- wait out the app's own loading indicator.
        #
        # The spinner is the app telling us when it is done, which beats any
        # timer we could pick. The grace period afterwards is charged only when
        # a loader was actually seen: paying it on every settle would add
        # seconds to each of the ~60 settles in a crawl for no reason.
        if await self._wait_for_loader(page, quick):
            grace = self.cfg.crawl.post_loader_wait_ms / 1000
            if quick:
                grace = min(grace, 1.0)
            if grace > 0:
                log.debug("loader cleared; holding %.1fs for content to land", grace)
                await asyncio.sleep(grace)
            try:
                current = await page.evaluate(SIGNATURE_JS)
            except Exception:
                return current

        # Stage 3b -- stability, measured as a sustained quiet period rather
        # than two consecutive polls. A dashboard fills its cards one API
        # response at a time; ~300ms of quiet is easily hit *between* two
        # responses, and extracting there captures a half-rendered page that
        # fingerprints differently every visit.
        quiet_ms = 150 if quick else self.cfg.crawl.stability_ms
        deadline = time.monotonic() + (cap_ms / 1000)
        # A page that is still *growing* has not settled, whatever the clock
        # says. The old loop was bounded purely by settle_timeout_ms (2s on the
        # tuned profile), so a page still drawing at 2s was extracted half-built
        # -- which is how one screen became 31 states with element counts from
        # 32 to 165. While the element count keeps rising, extend the deadline;
        # max_settle_ms is the hard stop so a polling widget cannot hang us.
        hard_stop = time.monotonic() + (
            min(cap_ms, 1500) if quick else self.cfg.crawl.max_settle_ms
        ) / 1000
        previous = current
        count = len(current.split("|")) if current else 0
        quiet_since = time.monotonic()
        while time.monotonic() < deadline and time.monotonic() < hard_stop:
            try:
                current = await page.evaluate(SIGNATURE_JS)
            except Exception:
                return previous
            now_count = len(current.split("|")) if current else 0
            if now_count > count:
                # Still rendering. Reset the quiet period and buy more time.
                count = now_count
                previous = current
                quiet_since = time.monotonic()
                deadline = max(deadline, time.monotonic() + (cap_ms / 1000))
            elif current == previous:
                if (time.monotonic() - quiet_since) * 1000 >= quiet_ms:
                    return current
            else:
                previous = current
                quiet_since = time.monotonic()
            await asyncio.sleep(0.15)
        return previous

    async def _wait_for_loader(self, page: Page, quick: bool = False) -> bool:
        """Wait for any visible loading indicator to disappear.

        Returns True if a loader was seen (and therefore a grace period is
        owed), False if the page was never busy.
        """
        cap_ms = self.cfg.crawl.loader_timeout_ms
        if cap_ms <= 0:
            return False
        if quick:
            cap_ms = min(cap_ms, 3000)

        extra = self.cfg.crawl.loader_selectors
        deadline = time.monotonic() + (cap_ms / 1000)
        seen: str | None = None

        while time.monotonic() < deadline:
            try:
                found = await page.evaluate(LOADER_JS, extra)
            except Exception:
                return seen is not None
            if not found:
                if seen:
                    log.debug("loader %r cleared", seen)
                return seen is not None
            if seen is None:
                seen = found
            await asyncio.sleep(0.2)

        if seen:
            log.debug("loader %r still visible after %dms; continuing anyway", seen, cap_ms)
        return seen is not None

    async def signature(self, page: Page) -> str:
        try:
            return await page.evaluate(SIGNATURE_JS)
        except Exception:
            return ""

    # -- consent ----------------------------------------------------------
    async def dismiss_consent(self, page: Page) -> bool:
        """Dismiss a cookie/consent banner. Safe to call after every navigation.

        A banner left standing appears in every fingerprint, obscures elements,
        and pollutes every generated test case with an irrelevant precondition.

        This runs per navigation rather than once per session: unless the app
        persists the choice, the banner comes back on every load -- including
        the reloads that ``Crawler._restore`` performs, which otherwise leaves
        the page permanently unable to match its own recorded signature.
        """
        if not self.cfg.interaction.dismiss_consent:
            return False
        vocab = [v.lower() for v in self.cfg.interaction.consent_vocab]
        try:
            found = await page.evaluate(CONSENT_JS, vocab)
        except Exception:
            return False
        if not found:
            return False

        try:
            await page.locator('[data-qagen-consent="1"]').first.click(
                timeout=self.cfg.crawl.action_timeout_ms
            )
        except Exception:
            return False

        log.debug("dismissed consent banner: %r", found)
        await self.settle(page)
        return True

    # -- extraction -------------------------------------------------------
    async def analyze(self, page: Page, depth: int, arrival: str) -> PageModel:
        status: str = "complete"
        try:
            raw: dict[str, Any] = await page.evaluate(
                EXTRACT_JS,
                {"extraClickable": self.cfg.crawl.extra_clickable_selectors},
            )
        except Exception as exc:
            log.warning("extraction failed on %s: %s", page.url, exc)
            return PageModel(
                url=page.url,
                normalized_url=normalize_url(page.url, self.cfg.target.id_collapse_exceptions),
                title="",
                depth=depth,
                arrival_action=arrival,
                capture_status="partial_error",
            )

        url = raw.get("url") or page.url

        elements = [
            classify(rec, url, self._same_origin, self._destructive)
            for rec in raw.get("elements", [])
        ]
        elements = await self._verify_selectors(page, elements)

        # Stamp each control with where a person would look for it. Done here,
        # once, because it needs the page geometry that came back with this
        # extraction -- not the geometry of whatever page we are on later.
        viewport_w = int(raw.get("viewport_width") or self.cfg.browser.viewport_width)
        doc_h = int(raw.get("document_height") or self.cfg.browser.viewport_height)
        for el in elements:
            el.location = el.describe_location(viewport_w, doc_h)
        await self._name_by_hover(page, elements)

        overlays = [
            OverlaySpec(
                overlay_type=self._overlay_type(o),
                role=o.get("role"),
                label=o.get("label"),
                selector=o.get("selector"),
                element_count=int(o.get("element_count") or 0),
            )
            for o in raw.get("overlays", [])
        ]

        forms = [self._form(f) for f in raw.get("forms", [])]
        searches = self._searches(elements, forms)

        model = PageModel(
            url=url,
            normalized_url=normalize_url(url, self.cfg.target.id_collapse_exceptions),
            title=raw.get("title", ""),
            depth=depth,
            arrival_action=arrival,
            landmarks=[
                Landmark(role=l.get("role", ""), label=l.get("label"))
                for l in raw.get("landmarks", [])
            ],
            elements=elements,
            forms=forms,
            searches=searches,
            overlays=overlays,
            console_errors=list(raw.get("js_errors", []))[:20],
            dom_nodes=int(raw.get("dom_nodes") or 0),
            viewport_width=viewport_w,
            viewport_height=int(raw.get("viewport_height") or 0),
            document_height=doc_h,
            capture_status=status,  # type: ignore[arg-type]
        )
        model.fingerprint = compute_fingerprint(
            url, elements, overlays, self.cfg.target.id_collapse_exceptions
        )
        return model

    async def _verify_selectors(self, page: Page, elements: list[Element]) -> list[Element]:
        """Prove each locator resolves to exactly one element.

        Anything ambiguous is demoted rather than silently trusted -- this is
        what makes the navigation graph a viable codegen substrate later.
        """
        # One round-trip for every CSS selector instead of one per element.
        # Per-element `locator.count()` cost ~40ms each; on a 70-element page
        # called several times per click that alone was most of the crawl's
        # wall clock.
        css = [e.selector for e in elements if e.selector and not e.selector.startswith("role=")]
        counts: dict[str, int] = {}
        if css:
            try:
                counts = await page.evaluate(
                    """(selectors) => {
                        const out = {};
                        for (const s of selectors) {
                            try { out[s] = document.querySelectorAll(s).length; }
                            catch (e) { out[s] = -1; }   // invalid selector
                        }
                        return out;
                    }""",
                    css,
                )
            except Exception as exc:
                log.debug("batched selector verification failed: %s", exc)

        verified: list[Element] = []
        for el in elements:
            if not el.selector:
                el.confidence = Confidence.LOW
                verified.append(el)
                continue

            if el.selector.startswith("role="):
                # Playwright's own engine, not CSS -- cannot be counted in
                # page context. These are re-resolved immediately before the
                # click, which is the moment correctness actually matters.
                verified.append(el)
                continue

            count = counts.get(el.selector, 0)
            if count < 0:
                el.confidence = Confidence.LOW
                verified.append(el)
                continue

            if count == 1:
                verified.append(el)
                continue

            if count > 1:
                # Unique it by position rather than throwing it away.
                el.selector = f"{el.selector} >> nth=0"
                el.selector_strategy += "+nth"
                el.confidence = Confidence.LOW
            else:
                el.confidence = Confidence.LOW
                log.debug("selector did not resolve: %s", el.selector)
            verified.append(el)
        return verified

    async def _name_by_hover(self, page: Page, elements: list[Element]) -> None:
        """Give icon-only controls a name by reading their hover tooltip.

        A "+" on a dashboard card typically has no aria-label, no title and no
        text, so the accname ladder returns "" and the control reaches the
        report as ``(unnamed)`` -- unusable in a test step. The app does label
        it, just not in the DOM: the label appears in a tooltip on hover. So we
        hover and read what appears.

        Mutates ``elements`` in place. Best-effort throughout: a page where
        hovering does nothing costs one evaluate per candidate and no names.
        """
        if not self.cfg.crawl.hover_naming or self.cfg.crawl.hover_naming_limit <= 0:
            return
        candidates = [
            el for el in elements
            if not el.name.strip() and el.enabled and is_actionable(el) and el.selector
        ][: self.cfg.crawl.hover_naming_limit]
        if not candidates:
            return

        try:
            baseline = await page.evaluate(TOOLTIP_JS, None)
        except Exception:
            return

        settle_s = self.cfg.crawl.hover_settle_ms / 1000
        named = 0
        for el in candidates:
            try:
                locator = page.locator(el.selector).first
                await locator.hover(timeout=min(self.cfg.crawl.action_timeout_ms, 2000))
                if settle_s:
                    await asyncio.sleep(settle_s)
                label = await page.evaluate(TOOLTIP_JS, el.selector)
            except Exception:
                continue
            label = (label or "").strip()
            if not label or label == baseline:
                continue
            el.name = label
            el.name_from_hover = True
            named += 1

        if named:
            log.debug("named %d icon-only element(s) by hover on %s", named, page.url)
        # Park the pointer off the content. Leaving it on the last element can
        # hold a hover menu open, which the very next extraction would then
        # record as part of the page.
        try:
            await page.mouse.move(0, 0)
        except Exception:
            pass

    def _overlay_type(self, raw: dict[str, Any]) -> OverlayType:
        declared = str(raw.get("overlay_type", "modal"))
        label = raw.get("label") or ""
        if self._is_consent(label):
            return OverlayType.CONSENT
        try:
            return OverlayType(declared)
        except ValueError:
            return OverlayType.MODAL

    def _form(self, raw: dict[str, Any]) -> FormSpec:
        fields = [
            FormField(
                name=f.get("name"),
                label=f.get("label"),
                label_source=f.get("label_source"),
                input_type=f.get("input_type", "text"),
                semantic_hint=f.get("semantic_hint"),
                required=bool(f.get("required")),
                pattern=f.get("pattern"),
                min=f.get("min"),
                max=f.get("max"),
                minlength=f.get("minlength"),
                maxlength=f.get("maxlength"),
                step=f.get("step"),
                options=f.get("options"),
                default_value=f.get("default_value"),
                readonly=bool(f.get("readonly")),
                disabled=bool(f.get("disabled")),
                validation_message=f.get("validation_message"),
                selector=f.get("selector", ""),
                confidence=Confidence(f.get("confidence", "high")),
            )
            for f in raw.get("fields", [])
        ]
        return FormSpec(
            form_id=raw.get("form_id", "F000"),
            origin=raw.get("origin", "explicit"),
            selector=raw.get("selector", ""),
            action=raw.get("action"),
            method=raw.get("method"),
            submit_selector=raw.get("submit_selector"),
            submit_label=raw.get("submit_label"),
            fields=fields,
            confidence=Confidence(raw.get("confidence", "high")),
        )

    def _searches(self, elements: list[Element], forms: list[FormSpec]) -> list[SearchControl]:
        controls: list[SearchControl] = []
        for el in elements:
            if el.kind is not ElementKind.SEARCH:
                continue
            submit = None
            method = "unknown"
            for form in forms:
                if any(f.selector == el.selector for f in form.fields):
                    submit = form.submit_selector
                    method = form.method or "unknown"
                    break
            controls.append(
                SearchControl(
                    input_selector=el.selector,
                    label=el.name or None,
                    submit_selector=submit,
                    submits_via=method if method in {"GET", "POST"} else "unknown",  # type: ignore[arg-type]
                )
            )
        return controls
