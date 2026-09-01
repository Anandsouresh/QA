"""The crawl state machine: 4A Arrive .. 4J Restore.

Termination is guaranteed two ways. The composite fingerprint stops every loop
we predicted (in-place modals, self-referential nav, templated routes); the
budgets stop the ones nobody predicted. The loop checks ``budgets.exhausted``
every iteration, so there is no path through this file that does not finish.
"""

from __future__ import annotations

import logging
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlsplit

from playwright.async_api import Page

from ..config import RunConfig
from ..graph.builder import GraphBuilder
from ..models import (
    ACTION_PRIORITY,
    CLICKABLE_KINDS,
    Element,
    ElementKind,
    NavNode,
    Observation,
    Outcome,
    PageModel,
)
from .actionlog import ActionLog
from .analyzer import PageAnalyzer
from .budgets import Budgets
from .fingerprint import anchor_set, anchor_similarity, normalize_url
from .policy import InteractionPolicy, ScopeRules
from .session import Session
from .shell import ShellDetector

log = logging.getLogger("qagen.crawler")


@dataclass
class ReplayStep:
    """One click to re-perform on arrival, to get back inside a popup."""

    selector: str
    label: str


@dataclass
class FrontierItem:
    url: str
    depth: int
    arrival_action: str
    source_fingerprint: str | None = None
    #: Clicks to re-perform after loading ``url``. A menu or modal has no URL of
    #: its own, so this is the only way to enqueue one and still explore it
    #: breadth-first: navigate, re-click the trigger, and you are back inside it.
    replay: tuple[ReplayStep, ...] = ()
    #: Element identities this item exists to exercise -- the controls the click
    #: *revealed*, not the whole page behind them. A popup carries a median of 7
    #: new controls among 49; planning against all 49 lets the per-state click
    #: budget push the real 7 out of reach, and attributes page buttons to the
    #: popup. Empty means "no restriction": plan the state normally.
    only_identities: frozenset[str] = frozenset()


@dataclass
class SkipRecord:
    url: str
    element: str
    reason: str


@dataclass
class CrawlResult:
    pages: list[PageModel] = field(default_factory=list)
    skips: list[SkipRecord] = field(default_factory=list)
    observations: list[Observation] = field(default_factory=list)
    graph: GraphBuilder | None = None
    budgets: Budgets | None = None


class Crawler:
    def __init__(self, cfg: RunConfig, session: Session) -> None:
        self.cfg = cfg
        self.session = session
        self.scope = ScopeRules(cfg.target)
        self.policy = InteractionPolicy(cfg.interaction)
        self.analyzer = PageAnalyzer(
            cfg,
            same_origin=self.scope.same_origin,
            destructive_match=self.policy.matches_destructive_text,
            is_consent_text=self.policy.is_consent_text,
        )
        self.budgets = Budgets(cfg.crawl)
        self.graph = GraphBuilder(cfg.target.url)
        self.result = CrawlResult(graph=self.graph, budgets=self.budgets)

        self._seen: dict[str, PageModel] = {}
        self._frontier: deque[FrontierItem] = deque()
        self._searched: set[str] = set()   # fingerprints already search-probed
        self._consent_done = False
        self._pending: list[str] = []
        #: fingerprint -> cheap DOM signature. Lets us detect "nothing happened"
        #: without paying for a full extraction on every click, which is the
        #: difference between a 15-second and a 90-second crawl.
        self._cheap: dict[str, str] = {}
        #: Element identity -> the state where we first exercised it. Global
        #: chrome (a floating assistant button, header nav) appears on every
        #: state; clicking it once per state burns the whole click budget on
        #: the same control and discovers nothing.
        self._exercised: dict[str, str] = {}
        #: normalised URL -> number of distinct states kept for it.
        self._per_url: dict[str, int] = {}
        #: top-level path segment -> number of distinct states kept for it.
        self._per_section: dict[str, int] = {}
        #: Fingerprints whose page model is already in result.pages.
        self._recorded: set[str] = set()
        #: Nodes whose action plan has already been run, so a repeat arrival
        #: cannot loop: each state is exercised exactly once per crawl.
        self._acted: set[str] = set()
        #: normalised URL -> [(fingerprint, anchor set)] for plain page states.
        #: Used to recognise the same screen caught at two different moments of
        #: rendering; see _canonicalise.
        self._page_anchors: dict[str, list[tuple[str, frozenset[str]]]] = {}
        #: Fingerprints already charged to the per-URL / per-section budgets.
        #:
        #: A popup is seen twice: once when a click reveals it, and again when
        #: its replay item comes off the frontier. Charging both made one popup
        #: cost two of its page's six slots, and the homepage -- base page,
        #: workspace menu, four "+" menus, notification modal -- ran out five
        #: minutes into a three-hour run. Every state pays once.
        self._charged: set[str] = set()
        #: Why states were turned away, so a silent cap cannot end a run while
        #: the summary says "completed".
        self._cap_rejections: dict[str, int] = {}
        self.shell = ShellDetector(
            declared=cfg.crawl.shell_selectors, min_urls=cfg.crawl.shell_min_urls
        )
        #: Normalised URLs ever put on the frontier, so site chrome is not
        #: queued once per state.
        self._queued: set[str] = set()
        #: Popups already queued, keyed two ways -- by the control that opens
        #: them and by the controls they reveal. See _enqueue_overlay.
        self._queued_replays: set[tuple] = set()
        #: fingerprint -> the replay path that reaches it. Lets a popup opened
        #: from inside another popup carry the whole chain.
        self._replay_by_fingerprint: dict[str, tuple] = {}
        self.log = ActionLog(cfg.output.dir, enabled=cfg.output.action_log)

    # -- main loop --------------------------------------------------------
    async def run(self) -> CrawlResult:
        assert self.session.page is not None
        self._queued.add(
            normalize_url(self.cfg.target.url, self.cfg.target.id_collapse_exceptions)
        )
        self._frontier.append(FrontierItem(self.cfg.target.url, 0, "initial navigation"))

        while self._frontier and not self.budgets.exhausted:
            item = self._frontier.popleft()
            try:
                await self._visit(item)
            except Exception as exc:  # one bad state must not kill the run
                log.warning("state failed (%s): %s", item.url, exc)
                self.result.observations.append(
                    Observation(kind="crawl_error", detail=f"{item.url}: {exc}")
                )

        self._pending = [
            i.url for i in self._frontier
        ]
        self.graph.mark_unexplored(self._pending)
        for cap, count in sorted(self._cap_rejections.items()):
            # These end runs quietly: no stop_reason, nothing in the summary,
            # just states dropped until the frontier starves.
            log.warning("%s turned away %d state(s)", cap, count)
            self.log.note("cap_summary", f"{cap} turned away {count} state(s)")
            self.result.observations.append(
                Observation(kind="budget_cap", detail=f"{cap} turned away {count} state(s)")
            )
        # Say why it ended, in terms of the work rather than the plumbing.
        # "frontier empty" told you nothing about whether the app was covered;
        # this distinguishes "everything reachable was exercised" from "there
        # is more out there and something stopped us".
        if not self.budgets.stop_reason:
            self.budgets.stop_reason = self._completion_reason()
        log.info("crawl stopped: %s", self.budgets.stop_reason)
        self.log.note("completion", self.budgets.stop_reason)
        self.log.budget(self.budgets.snapshot())
        self.log.close(self.budgets.stop_reason)
        return self.result

    # -- 4A .. 4F ---------------------------------------------------------
    async def _visit(self, item: FrontierItem) -> None:
        page = self.session.page
        assert page is not None

        # 4A Arrive
        scope = self.scope.in_scope(item.url)
        if not scope.allowed:
            self._record_boundary(item.url, scope.reason, item)
            return
        if not self.budgets.take_navigation():
            return

        self.log.navigating(item.url, item.depth)
        try:
            await page.goto(item.url, wait_until="domcontentloaded")
        except Exception as exc:
            log.warning("navigation failed %s: %s", item.url, exc)
            self.result.observations.append(
                Observation(kind="navigation_failed", detail=f"{item.url}: {exc}")
            )
            return

        # 4B Stabilize
        await self.analyzer.settle(page)
        if await self.analyzer.dismiss_consent(page):
            self._consent_done = True

        after_scope = self.scope.in_scope(page.url)
        if not after_scope.allowed:
            self._record_boundary(page.url, f"redirected: {after_scope.reason}", item)
            return

        # 4A2 Replay -- re-open the popup this item lives inside.
        if item.replay and not await self._replay(page, item):
            return

        # 4C Observe + 4D Identify
        model = await self._analyze(page, item.depth, item.arrival_action)
        if not item.replay:
            # A plain page arrival. Popups are excluded -- see _canonicalise.
            self._canonicalise(model)
        self._absorb_events(model)

        is_new = model.fingerprint not in self._seen
        self.budgets.note_state(is_new)

        source_node = (
            self.graph.node_for(item.source_fingerprint)
            if item.source_fingerprint
            else None
        )

        if not is_new and item.replay:
            # We navigated and re-clicked specifically to work through this
            # popup. Recognising the state and leaving would waste the whole
            # trip -- and it is why 49 of 101 popups in one run ended with no
            # outgoing edges: their menus were re-opened and then abandoned.
            known = self.graph.node_for(model.fingerprint)
            if known is not None and known.id not in self._acted:
                self._acted.add(known.id)
                self.log.note("replay_acting", f"{known.id} reached again; exercising it")
                if self.cfg.interaction.policy != "passive":
                    await self._act_on_state(page, model, known, item)
                return

        if not is_new:
            # The single point where every loop terminates.
            known = self.graph.node_for(model.fingerprint)
            if source_node and known:
                self.graph.add_edge(
                    source_node, known, "navigate", item.arrival_action,
                    Outcome.NAVIGATION,
                )
            self.log.state_seen(model.normalized_url, model.fingerprint)
            return

        # 4E Record node -- the page budget is charged per distinct state
        if not self._url_budget_ok(model):
            return
        if not self.budgets.take_page():
            return
        self._seen[model.fingerprint] = model
        self._cheap[model.fingerprint] = await self.analyzer.signature(page)
        self._record_page(model)
        node = self.graph.add_state(model, is_entry=not self.graph.graph.entry_node)
        await self._capture_artifacts(page, model, node.id)
        node.screenshot, node.html = model.screenshot_path, model.html_path
        if source_node:
            self.graph.add_edge(
                source_node, node, "navigate", item.arrival_action, Outcome.NAVIGATION
            )
        log.info(
            "state %s  %s  (%d elements, %d forms)",
            node.id, model.normalized_url, len(model.elements), len(model.forms),
        )
        self.log.state_found(
            node.id, model.normalized_url, len(model.elements), len(model.forms), model.depth
        )
        if len(model.elements) < self.cfg.crawl.hydration_min_elements:
            self.log.note(
                "thin_capture",
                f"{node.id} captured only {len(model.elements)} elements -- the page "
                f"probably had not finished rendering; raise hydration_timeout_ms",
            )

        # 4F Plan -- enqueue links, then act on in-page elements
        self._record_externals(model, node)
        self._log_unexercised(model)
        if item.depth < self.cfg.target.depth:
            self._enqueue_links(model, item.depth + 1)

        if self.cfg.interaction.policy != "passive":
            self._acted.add(node.id)
            await self._act_on_state(page, model, node, item)

        if self.cfg.crawl.probe_search and model.fingerprint not in self._searched:
            await self._probe_search(page, model, node)

    def _canonicalise(self, model: PageModel) -> bool:
        """Collapse a page state onto one we have already seen, if it is the same.

        A page fingerprints from its whole element list, which is only complete
        once the page has finished rendering -- and ``settle()`` cannot always
        tell. So the same screen visited twice can produce two fingerprints and
        therefore two states. Measured on a real run: ``/screen`` became 31
        states with element counts from 32 to 165, and the homepage became 17.

        Stable anchors do not have that problem. A ``data-testid`` either exists
        or it does not; it never half-renders. Two captures of the Screen page
        that fingerprinted differently had **identical** anchor sets (214 of
        214) and byte-identical screenshots.

        So: same URL plus near-identical anchors means the same screen, and the
        later capture adopts the earlier fingerprint.

        Applied to plain page states only. An overlay shares almost every anchor
        with the page behind it -- a menu adding 3 anchors to 205 would look 98%
        identical -- so collapsing those would silently erase every popup.

        Returns True when the model was collapsed onto an existing state.
        """
        threshold = self.cfg.crawl.state_anchor_threshold
        if threshold >= 1.0 and threshold != 1.0:
            return False
        anchors = anchor_set(model.elements)
        if not anchors:
            return False          # nothing stable to reason about; leave it alone

        known = self._page_anchors.setdefault(model.normalized_url, [])
        for fingerprint, seen in known:
            if fingerprint == model.fingerprint:
                return False      # already this exact state
            score = anchor_similarity(anchors, seen)
            if score >= threshold:
                self.log.note(
                    "state_merged",
                    f"{model.normalized_url} matches an earlier capture "
                    f"({score:.0%} of anchors); reusing {fingerprint[:10]} "
                    f"instead of {model.fingerprint[:10]}",
                )
                model.fingerprint = fingerprint
                return True

        known.append((model.fingerprint, anchors))
        return False

    async def _analyze(self, page: Page, depth: int, arrival: str) -> PageModel:
        """Extract, then work out which of it is the app frame.

        Every extraction goes through here so the shell detector sees every
        state -- it learns from repetition across URLs, so a state it never saw
        is a state it cannot learn from.
        """
        model = await self.analyzer.analyze(page, depth, arrival)
        self.shell.observe(model)
        self.shell.label(model)
        return model

    async def _replay(self, page: Page, item: FrontierItem) -> bool:
        """Re-perform the clicks that lead back into a popup.

        Fragile by nature -- the row you clicked may be gone, the menu may need
        different state -- so every failure is logged and ends this item rather
        than the crawl.
        """
        for step in item.replay:
            try:
                locator = page.locator(step.selector).first
                if await locator.count() == 0:
                    self.log.note(
                        "replay_failed",
                        f"{step.selector} no longer resolves on {page.url}",
                    )
                    return False
                await locator.click(
                    timeout=self.cfg.crawl.action_timeout_ms, no_wait_after=True
                )
            except Exception as exc:
                self.log.note("replay_failed", f"{step.selector}: {exc}")
                return False
            await self.analyzer.settle(page)
        self.log.note(
            "replay_ok",
            f"re-opened via {' > '.join(s.label for s in item.replay)}",
        )
        return True

    def _enqueue_overlay(
        self, base: PageModel, opened: PageModel, trigger: Element, item_depth: int
    ) -> None:
        """Queue a popup's interior for the next depth level.

        This is what keeps the crawl breadth-first. Clicking the popup's items
        the moment it opens is depth-first: it dives to the bottom of one menu
        before the rest of the page has been touched. Queuing it means the
        current page is finished first, and the popup is explored in turn.
        """
        replay = tuple(
            list(self._replay_of(base)) + [
                ReplayStep(selector=trigger.selector, label=trigger.name or trigger.role)
            ]
        )
        if len(replay) > self.cfg.crawl.max_replay_steps:
            self.log.note(
                "replay_too_deep",
                f"{opened.normalized_url} is {len(replay)} clicks deep; not queued",
            )
            return
        revealed = self._revealed(base, opened)

        # Two ways the same popup arrives twice, and both must be caught.
        #
        # by trigger -- the same button, found at a different position. A quarter
        #   of selectors here are positional (`li:nth-of-type(3)`), so keying on
        #   the selector queued one "Export" button as four popups and 21
        #   unnamed `div` triggers as 21 states.
        # by content -- two different buttons that open the same thing. The
        #   revealed controls are what the popup *is*; if we have queued that set
        #   already, queuing it again buys nothing.
        by_trigger = (opened.normalized_url, "trigger", trigger.stable_identity())
        marks = tuple(sorted(e.stable_identity() for e in revealed))
        by_content = (opened.normalized_url, "content", marks) if marks else None

        for key in (by_trigger, by_content):
            if key and key in self._queued_replays:
                self.log.note(
                    "overlay_already_queued",
                    f"{opened.normalized_url} via {trigger.name or trigger.role!r} "
                    f"matches a popup already queued; skipping",
                )
                return
        # Already explored under a different route in. Without this the same
        # menu is queued once per chain that reaches it, and each queued copy
        # costs a navigation plus a replay (~20s) only to report
        # `state_duplicate` -- the loop that stalled a live run for an hour.
        if opened.fingerprint in self._acted:
            self.log.note(
                "overlay_already_done",
                f"{opened.normalized_url} via {trigger.name or trigger.role!r} "
                f"is already exercised; not queued again",
            )
            return
        self._queued_replays.add(by_trigger)
        if by_content:
            self._queued_replays.add(by_content)
        self._replay_by_fingerprint[opened.fingerprint] = replay

        self._frontier.append(
            FrontierItem(
                url=base.url,
                depth=item_depth,
                arrival_action=f"Click '{trigger.name or trigger.role}'",
                source_fingerprint=base.fingerprint,
                replay=replay,
                only_identities=frozenset(e.identity() for e in revealed),
            )
        )

    def _replay_of(self, page: PageModel) -> tuple[ReplayStep, ...]:
        """The replay path that reaches this state, if it is itself a popup."""
        return self._replay_by_fingerprint.get(page.fingerprint, ())

    def _enqueue_links(self, model: PageModel, depth: int) -> None:
        for el in model.elements:
            if el.kind is not ElementKind.NAV_LINK or not el.href:
                continue
            decision = self.scope.in_scope(el.href)
            if not decision.allowed:
                continue

            # Dedupe against everything ever queued, not just this page. Site
            # chrome (footer legal links, header nav) appears on every state, so
            # a per-page set still queues the same URL once per state -- and
            # each of those costs a full navigation before the fingerprint can
            # tell us we have been there. On the real target that was 31
            # navigations to produce 6 states.
            key = normalize_url(el.href, self.cfg.target.id_collapse_exceptions)
            if key in self._queued:
                continue
            self._queued.add(key)

            self._frontier.append(
                FrontierItem(
                    url=el.href,
                    depth=depth,
                    arrival_action=f"Click '{el.name or el.href}'",
                    source_fingerprint=model.fingerprint,
                )
            )

    # -- 4G .. 4J ---------------------------------------------------------
    async def _act_on_state(
        self, page: Page, model: PageModel, node: NavNode, item: FrontierItem
    ) -> None:
        plan = self._plan_actions(model, only=item.only_identities)
        consecutive_failures = 0

        for index, el in enumerate(plan):
            if self.budgets.exhausted:
                return

            decision = self.policy.evaluate(el)
            if not decision.allowed:
                self._skip(model, el, decision.reason, node)
                continue

            # Global chrome: exercise each element identity once per crawl.
            identity = el.identity()
            if identity in self._exercised:
                self._skip(
                    model, el,
                    f"already exercised on {self._exercised[identity]}",
                    node, count_as_global=True,
                )
                continue

            if not self.budgets.take_click():
                return
            self._exercised[identity] = node.id

            self.log.action(node.id, el.kind.value, el.name or "(unnamed)", el.selector)
            started = time.monotonic()
            await self._perform(page, model, node, el)
            self.log.note(
                "action_done",
                f"{node.id}  {el.name or el.kind.value!r} took {time.monotonic() - started:.1f}s",
            )

            # 4J Restore
            restored = await self._restore(page, model)
            self.log.restore(node.id, restored, "escape/back/goto")
            if restored:
                consecutive_failures = 0
                continue

            # A failed restore used to end the state outright. It is the single
            # largest source of missed coverage: on one real run the entry page
            # had 46 elements, attempted 28, hit one failed restore and dropped
            # the remaining 18 -- the notification bell among them, because
            # app-frame controls are planned last and so are always in the tail
            # that gets discarded.
            #
            # Escape/back/goto failing does not mean the page is unusable. It
            # means we are somewhere unexpected. Go back deliberately and carry
            # on with the rest of the plan.
            consecutive_failures += 1
            if consecutive_failures >= self.cfg.crawl.max_restore_failures:
                self.log.note(
                    "state_abandoned",
                    f"{node.id}: {consecutive_failures} restores in a row failed; "
                    f"{len(plan) - index - 1} action(s) not attempted",
                )
                return
            if not await self._hard_reset(page, model, item):
                self.log.note(
                    "state_abandoned",
                    f"{node.id}: could not return to the state; "
                    f"{len(plan) - index - 1} action(s) not attempted",
                )
                return
            self.log.note("state_recovered", f"{node.id}: back after a failed restore")

    async def _hard_reset(
        self, page: Page, model: PageModel, item: FrontierItem
    ) -> bool:
        """Get back to a state the cheap restore could not reach.

        Reloads the page and, for a popup, replays the clicks that open it. It
        does not insist on an exact signature match the way ``_restore`` does:
        the goal is to be somewhere we can keep testing from, not to reproduce
        the state byte for byte. Insisting on the latter is what made a single
        failed restore throw away the rest of the page.
        """
        if not self.budgets.take_navigation():
            return False
        try:
            await page.goto(model.url, wait_until="domcontentloaded")
            await self.analyzer.settle(page)
            await self.analyzer.dismiss_consent(page)
        except Exception as exc:
            log.debug("hard reset failed for %s: %s", model.url, exc)
            return False

        replay = item.replay or self._replay_of(model)
        if replay:
            for step in replay:
                try:
                    locator = page.locator(step.selector).first
                    if await locator.count() == 0:
                        return False
                    await locator.click(
                        timeout=self.cfg.crawl.action_timeout_ms, no_wait_after=True
                    )
                    await self.analyzer.settle(page)
                except Exception:
                    return False
        return True

    def _skip(
        self,
        model: PageModel,
        el: Element,
        reason: str,
        node: NavNode | None = None,
        count_as_global: bool = False,
    ) -> None:
        label = f"{el.role} '{el.name}'"
        self.result.skips.append(SkipRecord(model.url, label, reason))
        self.log.skip(model.url, label, reason)
        if node is not None and not count_as_global:
            entry = f"{el.kind.value}: {el.name or '(unnamed)'} -- {reason}"
            if entry not in node.not_exercised:
                node.not_exercised.append(entry)

    def _log_unexercised(self, model: PageModel) -> None:
        """Record elements we will never click, with the reason.

        Destructive controls never enter the action plan at all, so without
        this they would be invisible everywhere -- yet a 'Delete account'
        button is one of the highest-value things a QA suite should cover.
        The summariser feeds these to the model under
        "NOT EXERCISED BY THE CRAWLER".
        """
        reasons = {
            ElementKind.DESTRUCTIVE: "destructive action, never clicked",
            ElementKind.SUBMIT: "form submit, analysed but never submitted",
            ElementKind.FILE_INPUT: "file input, chooser dismissed",
            ElementKind.EXTERNAL_LINK: "external origin, recorded as boundary",
        }
        for el in model.elements:
            reason = reasons.get(el.kind)
            if reason:
                self.result.skips.append(
                    SkipRecord(model.url, f"{el.role} '{el.name}'", reason)
                )

    def _plan_actions(
        self, model: PageModel, only: frozenset[str] = frozenset()
    ) -> list[Element]:
        """Decide the order a state is worked through, then truncate.

        Default is **reading order** -- top to bottom, left to right, the way a
        person works down a screen. Two things follow from that. The action log
        and the generated test steps track the layout, so they can be checked
        against a screenshot by eye. And a state cut short by the budget leaves
        a coherent top-slice of the page rather than a scatter of controls
        chosen by an internal ranking nobody can see.

        Content-area elements still go first (``content_before_frame``). The
        header and the left menu are identical on every state -- clicking
        "Content" from Settings teaches us nothing that clicking it from Home
        did not -- so a state is read twice: down the content, then down the
        frame. Set ``content_before_frame: false`` for strict whole-page
        reading order.
        """
        candidates = [
            el for el in model.elements
            if el.kind in CLICKABLE_KINDS and el.enabled and el.visible
        ]

        # A popup state contains the whole page behind it. Restrict to the
        # controls the click actually revealed -- a median of 7 among 49 on this
        # app. Planning against all 49 lets the per-state budget push the real
        # items out of reach, and records page buttons against the popup.
        #
        # The fallback matters: if nothing survives the filter (the diff was
        # computed against a stale parent, or the click replaced content rather
        # than adding to it) fall back to the full plan rather than silently
        # doing nothing with the state.
        if only:
            restricted = [el for el in candidates if el.identity() in only]
            if restricted:
                self.log.note(
                    "plan_restricted",
                    f"{model.normalized_url}: {len(restricted)} revealed control(s) "
                    f"of {len(candidates)} on the state",
                )
                candidates = restricted
            else:
                self.log.note(
                    "plan_restriction_empty",
                    f"{model.normalized_url}: none of the revealed controls are "
                    f"present; planning the whole state instead",
                )

        crawl = self.cfg.crawl
        band = crawl.reading_band_px

        def rank(el: Element) -> tuple:
            frame = (el.region == "shell") if crawl.content_before_frame else False
            if crawl.action_order == "reading":
                return (frame, *el.reading_key(band))
            return (frame, ACTION_PRIORITY.get(el.kind, 9), el.name.lower())

        candidates.sort(key=rank)
        plan = candidates[: crawl.max_clicks_per_state]

        # Reserve slots for controls nothing has exercised yet -- in practice
        # the app frame, which the cap above would otherwise never reach on a
        # content-heavy page. In a menu-driven SPA that is fatal: the left menu
        # is the only route to another section, and its items are divs with no
        # href, so they are never enqueued as links either. Cheap, because
        # global dedup means each of these is clicked once in the whole crawl.
        if crawl.frame_reserve:
            chosen = {id(el) for el in plan}
            extra = [
                el for el in candidates
                if el.region == "shell"
                and id(el) not in chosen
                and el.identity() not in self._exercised
            ]
            plan += extra[: crawl.frame_reserve]
        return plan

    async def _perform(
        self, page: Page, model: PageModel, node: NavNode, el: Element
    ) -> None:
        before_url = page.url
        before_fp = model.fingerprint
        self.session.sink.drain()   # start from a clean event slate

        try:
            locator = page.locator(el.selector).first
            if await locator.count() == 0:
                self.result.skips.append(
                    SkipRecord(model.url, f"{el.role} '{el.name}'", "element detached before click")
                )
                return
            await locator.click(timeout=self.cfg.crawl.action_timeout_ms, no_wait_after=True)
        except Exception as exc:
            self.result.skips.append(
                SkipRecord(model.url, f"{el.role} '{el.name}'", f"click failed: {exc}")
            )
            return

        await self.analyzer.settle(page)
        if page.url != before_url:
            # A reloaded page brings its cookie banner back; without this the
            # same URL fingerprints differently depending on how we got here,
            # and the graph grows a twin node for every page.
            await self.analyzer.dismiss_consent(page)
        events = self.session.sink.drain()

        after_url = page.url
        # Fast path: most clicks change nothing. Compare the cheap signature
        # before paying for a full extraction.
        cheap_after = await self.analyzer.signature(page)
        unchanged = (
            after_url == before_url
            and cheap_after == self._cheap.get(before_fp, cheap_after)
        )

        after: PageModel | None = None
        if unchanged:
            after_fp = before_fp
        else:
            after = await self._analyze(page, model.depth, f"Click '{el.name}'")
            after_fp = after.fingerprint
            # A client-side route change can commit *during* the extraction, so
            # the URL sampled a moment ago is stale. Trust the URL the
            # extraction actually saw: otherwise a navigation is recorded as an
            # in-page state, and we would go on to treat the next page's
            # elements as the contents of an overlay.
            after_url = after.url
            if after_url != before_url:
                # The click landed on another page; same rule as a frontier
                # arrival. In-page states deliberately skip this.
                self._canonicalise(after)
                after_fp = after.fingerprint

        outcome, annotations = self._classify_outcome(
            events, before_url, after_url, before_fp, after_fp
        )
        self.log.outcome(
            node.id, el.name or el.kind.value, outcome.value, annotations, 0.0
        )

        for obs in (*events.dialogs, *events.file_choosers, *events.downloads):
            obs.triggered_by = f"{el.role} '{el.name}'"
            self.result.observations.append(obs)
            model.observations.append(obs)
        for blocked in events.blocked:
            model.blocked_mutations.append(blocked)

        # 4I Reconcile
        target_node = node
        if outcome is Outcome.NEW_TAB and events.new_pages:
            target_node = self._handle_new_tab(events.new_pages[0], el, node, model)
        elif outcome in {Outcome.NAVIGATION, Outcome.IN_PAGE_STATE} and after is not None:
            known = self.graph.node_for(after.fingerprint)
            if after.fingerprint in self._seen and known is not None:
                target_node = known

            elif outcome is Outcome.NAVIGATION:
                # Create the node so the edge has a target, but leave the state
                # out of `_seen` so the frontier visit still explores it fully.
                target_node = self.graph.add_state(after)
                # Capture now rather than trusting the later visit to fill it
                # in. That hand-off matches on fingerprint, and when the page
                # has moved on even slightly the visit creates a *new* node --
                # leaving this one permanently without a screenshot. That is
                # why /screen and /content had none.
                if not target_node.screenshot:
                    await self._capture_artifacts(page, after, target_node.id)
                    target_node.screenshot = after.screenshot_path
                    target_node.html = after.html_path
                if model.depth + 1 <= self.cfg.target.depth:
                    self._frontier.append(
                        FrontierItem(
                            url=after_url,
                            depth=model.depth + 1,
                            arrival_action=f"Click '{el.name}'",
                            source_fingerprint=model.fingerprint,
                        )
                    )

            else:
                # An in-page state -- a modal, a drawer, or the anchored menu a
                # "+" opens. It has no URL, so it reaches the frontier as a
                # replay path instead: load the page, re-click the trigger.
                if not self._url_budget_ok(after):
                    self.graph.add_edge(
                        node, node, "click", f"Click '{el.name or el.role}'",
                        outcome, selector=el.selector, role=el.role, name=el.name,
                        annotations=annotations + ["state-cap"],
                    )
                    return
                self._cheap[after.fingerprint] = cheap_after
                # Keep the page model: it is what the generation phase reads,
                # and a popup that never reached result.pages produced no test
                # cases at all however well the crawler explored it.
                self._record_page(after)
                target_node = self.graph.add_state(after)
                # Capture while the overlay is still open -- this is the only
                # moment it exists on screen.
                await self._capture_artifacts(page, after, target_node.id)
                target_node.screenshot = after.screenshot_path
                target_node.html = after.html_path
                self._label_variant(target_node, node, model, after, el)

                # Queue its interior for the next depth rather than clicking
                # into it now. Deliberately NOT added to `_seen`: the frontier
                # visit re-opens it and works through it with the full plan,
                # exactly as it would any other state.
                revealed = self._revealed(model, after)
                target_node.not_exercised = [
                    f"{r.kind.value}: {r.name or '(unnamed)'} -- queued for depth "
                    f"{model.depth + 1}"
                    for r in revealed
                ]
                self.log.note(
                    "overlay_queued",
                    f"{target_node.id} revealed {len(revealed)} item(s) via "
                    f"{el.name or el.role!r}; queued for depth {model.depth + 1}",
                )
                if model.depth + 1 <= self.cfg.target.depth:
                    self._enqueue_overlay(model, after, el, model.depth + 1)

        self.graph.add_edge(
            node,
            target_node,
            "click",
            f"Click '{el.name or el.role}'",
            outcome,
            selector=el.selector,
            role=el.role,
            name=el.name,
            annotations=annotations,
            reversible_by=self._reversibility(outcome),
        )

    # -- same-page overlays -----------------------------------------------
    def _revealed(self, base: PageModel, opened: PageModel) -> list[Element]:
        """Elements that appeared as a result of the click, in DOM order.

        A DOM diff, deliberately, rather than the overlay detector. A dropdown
        anchored under a "+" covers a few percent of the viewport and so fails
        every size-based overlay heuristic there is -- but we know a click just
        happened, and "these elements were not here a moment ago" needs no
        heuristic at all.
        """
        known = {el.identity() for el in base.elements}
        return [el for el in opened.elements if el.identity() not in known]

    def _label_variant(
        self,
        node: NavNode,
        parent: NavNode,
        base: PageModel,
        opened: PageModel,
        trigger: Element,
    ) -> None:
        """Record a same-page overlay as a *variant* of the page it opened from.

        Otherwise the graph grows two nodes with the identical title -- the page
        and the page-with-a-menu-open -- and nothing says which is which or how
        to reach the second one.
        """
        if opened.normalized_url != base.normalized_url:
            return   # not a variant of this page at all; it is somewhere else
        node.parent_state = parent.id
        node.opened_by = f"Click '{trigger.name or trigger.role}'"

        revealed = self._revealed(base, opened)
        removed = len(base.elements) - (len(opened.elements) - len(revealed))
        if node.node_type == "page" and revealed and removed <= 0:
            # Purely additive: something opened on top. A tab switch or a
            # filtered list *replaces* content, and stays a page.
            node.node_type = "dropdown"

        label = trigger.name or trigger.role or "action"
        base_title = parent.title or base.normalized_url
        node.title = f"{base_title} — {label}"

    def _classify_outcome(
        self,
        events: Any,
        before_url: str,
        after_url: str,
        before_fp: str,
        after_fp: str,
    ) -> tuple[Outcome, list[str]]:
        """The nine things a click can actually do (CRAWLING §4H)."""
        annotations: list[str] = []
        if events.blocked:
            annotations.append("mutating")
        if events.dialogs:
            annotations.append("confirmation_required")
        if events.file_choosers:
            annotations.append("upload")
        if events.console_errors:
            annotations.append("error")

        if events.new_pages:
            return Outcome.NEW_TAB, annotations
        if events.file_choosers:
            return Outcome.FILE_CHOOSER, annotations
        if events.downloads:
            return Outcome.DOWNLOAD, annotations
        if events.dialogs:
            return Outcome.NATIVE_DIALOG, annotations

        if after_url != before_url:
            return Outcome.NAVIGATION, annotations
        if after_fp != before_fp:
            return Outcome.IN_PAGE_STATE, annotations

        # No state change. A blocked write is still the single most valuable
        # thing we can learn about an element, so it outranks "nothing happened".
        if events.blocked:
            return Outcome.BLOCKED_MUTATION, annotations
        if events.console_errors:
            return Outcome.ERROR, annotations
        annotations.append("inert")
        return Outcome.NO_CHANGE, annotations

    def _handle_new_tab(
        self, url: str, el: Element, node: NavNode, model: PageModel
    ) -> NavNode:
        decision = self.scope.in_scope(url)
        if decision.allowed:
            self._frontier.append(
                FrontierItem(
                    url=url,
                    depth=model.depth + 1,
                    arrival_action=f"Click '{el.name}' (new tab)",
                    source_fingerprint=model.fingerprint,
                )
            )
            # Provisional boundary node until the frontier resolves it.
            return self.graph.add_boundary(url, urlsplit(url).netloc, "new tab", el.name)
        return self.graph.add_boundary(
            url, urlsplit(url).netloc, decision.reason, el.name
        )

    def _reversibility(self, outcome: Outcome) -> str:
        if outcome is Outcome.IN_PAGE_STATE:
            return "escape"
        if outcome is Outcome.NAVIGATION:
            return "back"
        if outcome in {Outcome.NO_CHANGE, Outcome.BLOCKED_MUTATION}:
            return "none"
        return "goto"

    async def _restore(self, page: Page, model: PageModel) -> bool:
        """Escape -> back -> goto, cheapest first, stopping at the first that
        reproduces the target state. Failure is never fatal.

        Comparison uses the cheap signature rather than a full re-extraction:
        this runs after every single click, so a full analyze here triples the
        crawl's wall-clock for no extra information.
        """
        expected = self._cheap.get(model.fingerprint)

        for attempt in ("escape", "back", "goto"):
            try:
                if attempt == "escape":
                    await page.keyboard.press("Escape")
                elif attempt == "back":
                    if page.url == model.url:
                        continue
                    await page.go_back(wait_until="domcontentloaded")
                else:
                    await page.goto(model.url, wait_until="domcontentloaded")
            except Exception:
                continue

            await self.analyzer.settle(page, quick=True)
            if attempt == "goto":
                await self.analyzer.dismiss_consent(page)
            if page.url != model.url:
                continue
            if expected is None:
                return True
            if await self.analyzer.signature(page) == expected:
                return True
        return False

    # -- search probe -----------------------------------------------------
    async def _probe_search(self, page: Page, model: PageModel, node: NavNode) -> None:
        """Probe once per state. Results are template-collapsed by
        ``normalize_url``, so a search box cannot generate unbounded states."""
        if not model.searches:
            return
        self._searched.add(model.fingerprint)
        control = model.searches[0]
        term = self.cfg.crawl.search_probe_term

        if not self.budgets.take_click():
            return

        self.session.sink.drain()
        before_url, before_fp = page.url, model.fingerprint

        try:
            box = page.locator(control.input_selector).first
            await box.fill(term, timeout=self.cfg.crawl.action_timeout_ms)
            await self.analyzer.settle(page)
            suggestion_fp = (
                await self.analyzer.analyze(page, model.depth, "type search term")
            ).fingerprint
            control.live_suggestions = suggestion_fp != before_fp

            if control.submit_selector:
                await page.locator(control.submit_selector).first.click(
                    timeout=self.cfg.crawl.action_timeout_ms, no_wait_after=True
                )
            else:
                await box.press("Enter")
        except Exception as exc:
            self.result.skips.append(
                SkipRecord(model.url, "search box", f"probe failed: {exc}")
            )
            return

        await self.analyzer.settle(page)
        events = self.session.sink.drain()
        after = await self._analyze(page, model.depth, f"Search '{term}'")
        outcome, annotations = self._classify_outcome(
            events, before_url, page.url, before_fp, after.fingerprint
        )

        if events.blocked:
            control.submits_via = "POST"
        elif page.url != before_url:
            control.submits_via = "GET"
        elif after.fingerprint != before_fp:
            control.submits_via = "client_only"

        target = node
        if outcome in {Outcome.NAVIGATION, Outcome.IN_PAGE_STATE}:
            if after.fingerprint not in self._seen:
                self._seen[after.fingerprint] = after
                self.result.pages.append(after)
                target = self.graph.add_state(after)
            else:
                target = self.graph.node_for(after.fingerprint) or node

        self.graph.add_edge(
            node, target, "type",
            f"Search for '{term}'",
            outcome,
            selector=control.input_selector,
            input_value=term,
            annotations=annotations,
        )
        await self._restore(page, model)

    def _record_page(self, model: PageModel) -> None:
        """Keep one page model per state.

        Two paths reach the same popup -- the click that reveals it and the
        replay that returns to it -- and both need the model kept, so the
        de-duplication has to live in one place rather than at each call site.
        """
        if model.fingerprint in self._recorded:
            return
        self._recorded.add(model.fingerprint)
        self.result.pages.append(model)

    def _completion_reason(self) -> str:
        """What the crawl actually achieved, once the frontier is empty."""
        from ..models import is_actionable

        actionable = 0
        exercised = 0
        for page in self.result.pages:
            for el in page.elements:
                if not is_actionable(el):
                    continue
                actionable += 1
                if el.identity() in self._exercised:
                    exercised += 1

        unvisited = [n for n in self.graph.graph.nodes if n.id not in self._acted
                     and n.node_type not in ("boundary", "external")]
        if self._pending:
            return (
                f"stopped with {len(self._pending)} location(s) still queued "
                f"({exercised}/{actionable} actionable elements exercised)"
            )
        if unvisited:
            return (
                f"frontier empty, but {len(unvisited)} state(s) were recorded and "
                f"never exercised ({exercised}/{actionable} actionable elements "
                f"exercised)"
            )
        return (
            f"all reachable elements crawled: {exercised}/{actionable} actionable "
            f"elements exercised across {len(self.result.pages)} states"
        )

    def _section_of(self, normalized_url: str) -> str:
        """The top-level area a URL belongs to: /settings/user -> 'settings'."""
        segments = [s for s in urlsplit(normalized_url).path.split("/") if s]
        return segments[0] if segments else "/"

    def _url_budget_ok(self, model: PageModel) -> bool:
        """Two caps: per URL, so an in-page editor cannot crowd out the app, and
        per section, so one deep area cannot swallow the whole crawl.

        The section cap is not theoretical. On a real run of this app `/settings`
        produced 43 of 63 states -- eleven menu items each opening a page with
        its own sub-navigation -- while `/screen`, `/schedule` and `/channel`
        were never visited at all.
        """
        if model.fingerprint in self._charged:
            return True          # already paid for; this is the same state again

        seen = self._per_url.get(model.normalized_url, 0)
        if seen >= self.cfg.crawl.max_states_per_url:
            self._cap_rejections["max_states_per_url"] = (
                self._cap_rejections.get("max_states_per_url", 0) + 1
            )
            self.log.note(
                "url_state_cap",
                f"{model.normalized_url}  already has {seen} states; not recording more",
            )
            return False

        section = self._section_of(model.normalized_url)
        in_section = self._per_section.get(section, 0)
        if in_section >= self.cfg.crawl.max_states_per_section:
            self._cap_rejections["max_states_per_section"] = (
                self._cap_rejections.get("max_states_per_section", 0) + 1
            )
            self.log.note(
                "section_state_cap",
                f"/{section} already has {in_section} states; leaving budget for "
                f"sections not yet reached",
            )
            return False

        self._per_url[model.normalized_url] = seen + 1
        self._per_section[section] = in_section + 1
        self._charged.add(model.fingerprint)
        return True

    # -- artifacts --------------------------------------------------------
    async def _capture_artifacts(self, page: Page, model: PageModel, node_id: str) -> None:
        """One screenshot + one raw-DOM dump per discovered state.

        Worth the two extra round-trips: a blank screenshot tells you the
        settle heuristic fired before the app rendered, and the raw DOM tells
        you what the extractor was looking at when it produced a thin
        inventory. Neither is visible from the element list alone.
        """
        out = self.cfg.output
        if not (out.save_screenshots or out.save_html):
            return

        target_dir = out.dir / "artifacts"
        try:
            target_dir.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            log.debug("cannot create artifacts dir: %s", exc)
            return

        stem = f"{node_id}_{model.fingerprint[:8]}"

        if out.save_screenshots:
            shot = target_dir / f"{stem}.png"
            try:
                await page.screenshot(
                    path=str(shot),
                    full_page=out.screenshot_full_page,
                    timeout=self.cfg.crawl.action_timeout_ms,
                )
                model.screenshot_path = str(shot.relative_to(out.dir)).replace("\\", "/")
            except Exception:
                # full_page fails on pages with unbounded height (infinite
                # scroll, virtualised lists). A viewport shot is still useful.
                try:
                    await page.screenshot(path=str(shot), full_page=False, timeout=5000)
                    model.screenshot_path = str(shot.relative_to(out.dir)).replace("\\", "/")
                except Exception as exc:
                    log.debug("screenshot failed for %s: %s", node_id, exc)

        if out.save_html:
            doc = target_dir / f"{stem}.html"
            try:
                content = await page.content()
                doc.write_text(content, encoding="utf-8", errors="replace")
                model.html_path = str(doc.relative_to(out.dir)).replace("\\", "/")
            except Exception as exc:
                log.debug("html capture failed for %s: %s", node_id, exc)

    # -- bookkeeping ------------------------------------------------------
    def _absorb_events(self, model: PageModel) -> None:
        events = self.session.sink.drain()
        model.network.extend(events.network[:80])
        model.console_errors.extend(events.console_errors[:20])
        model.blocked_mutations.extend(events.blocked)
        for obs in (*events.dialogs, *events.file_choosers, *events.downloads):
            model.observations.append(obs)
            self.result.observations.append(obs)

    def _record_boundary(self, url: str, reason: str, item: FrontierItem) -> None:
        source = (
            self.graph.node_for(item.source_fingerprint)
            if item.source_fingerprint
            else None
        )
        boundary = self.graph.add_boundary(url, urlsplit(url).netloc, reason, item.arrival_action)
        if source:
            self.graph.add_edge(
                source, boundary, "navigate", item.arrival_action, Outcome.NAVIGATION,
                annotations=["boundary"],
            )
        log.debug("boundary: %s (%s)", url, reason)

    def _record_externals(self, model: PageModel, node: NavNode) -> None:
        """Record every external link as a boundary at planning time.

        These are never clicked, so recording them only on skip would mean they
        never appear at all -- and a third-party origin the app links into is
        genuine QA signal worth surfacing.
        """
        seen: set[str] = set()
        for el in model.elements:
            if el.kind is not ElementKind.EXTERNAL_LINK or not el.href:
                continue
            origin = urlsplit(el.href).netloc
            if origin in seen:
                continue
            seen.add(origin)
            boundary = self.graph.add_boundary(el.href, origin, "external origin", el.name)
            self.graph.add_edge(
                node, boundary, "click", f"Click '{el.name}'", Outcome.NEW_TAB,
                selector=el.selector, role=el.role, name=el.name,
                annotations=["boundary"],
            )
