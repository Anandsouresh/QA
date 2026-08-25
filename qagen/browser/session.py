"""Playwright lifecycle, auth loading, the network write-guard, and all six
overlay handlers.

Two of these handlers are not optional: an unhandled ``filechooser`` makes the
triggering click hang until timeout, and an unhandled ``beforeunload`` dialog
blocks navigation. Both present as unexplained crawl stalls rather than errors,
which is the worst kind of bug to chase.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from playwright.async_api import (
    Browser,
    BrowserContext,
    Dialog,
    Download,
    FileChooser,
    Page,
    Playwright,
    Request,
    Route,
    async_playwright,
)

from ..config import RunConfig
from ..models import Boundary, EndpointObservation, Observation

log = logging.getLogger("qagen.session")

MUTATING_METHODS = {"POST", "PUT", "PATCH", "DELETE"}

#: Suppress window.open so a popup cannot steal focus, while still recording
#: the URL it wanted. Also neutralises beforeunload registration noise.
INIT_SCRIPT = """
(() => {
  window.__qagen = { opened: [], errors: [] };
  const nativeOpen = window.open;
  window.open = function (url, ...rest) {
    try { window.__qagen.opened.push(String(url || '')); } catch (e) {}
    return null;   // suppressed: recorded, not rendered
  };
  window.addEventListener('error', (e) => {
    try { window.__qagen.errors.push(String(e.message)); } catch (_) {}
  });
  window.addEventListener('unhandledrejection', (e) => {
    try { window.__qagen.errors.push('unhandledrejection: ' + String(e.reason)); }
    catch (_) {}
  });
})();
"""


@dataclass
class EventSink:
    """Everything the six handlers record, drained once per action."""

    dialogs: list[Observation] = field(default_factory=list)
    file_choosers: list[Observation] = field(default_factory=list)
    downloads: list[Observation] = field(default_factory=list)
    new_pages: list[str] = field(default_factory=list)
    blocked: list[str] = field(default_factory=list)
    network: list[EndpointObservation] = field(default_factory=list)
    console_errors: list[str] = field(default_factory=list)
    boundaries: list[Boundary] = field(default_factory=list)

    def drain(self) -> "EventSink":
        """Return a copy of what has accumulated and reset the per-action fields."""
        snap = EventSink(
            dialogs=list(self.dialogs),
            file_choosers=list(self.file_choosers),
            downloads=list(self.downloads),
            new_pages=list(self.new_pages),
            blocked=list(self.blocked),
            network=list(self.network),
            console_errors=list(self.console_errors),
        )
        self.dialogs.clear()
        self.file_choosers.clear()
        self.downloads.clear()
        self.new_pages.clear()
        self.blocked.clear()
        self.network.clear()
        self.console_errors.clear()
        return snap

    @property
    def empty(self) -> bool:
        return not (
            self.dialogs
            or self.file_choosers
            or self.downloads
            or self.new_pages
            or self.blocked
        )


#: Console noise the write-guard itself produces. Filtered so an aborted
#: mutation is reported as `blocked_mutation` (useful) and not additionally as
#: an application console error (misleading).
_GUARD_NOISE = (
    "err_blocked_by_client",
    "blockedbyclient",
    "failed to fetch",
    "net::err_failed",
    "networkerror when attempting to fetch",
)


def _is_our_own_noise(text: str) -> bool:
    low = text.lower()
    return any(marker in low for marker in _GUARD_NOISE)


#: Analytics and tag-manager endpoints. These take POST beacons on essentially
#: every click, so treating them as application writes made the entire page
#: look mutating -- on one real dashboard, 46 of 46 "blocked mutations" were
#: Google Analytics and not one was the app.
_TELEMETRY_HOSTS = (
    "analytics.google.com", "google-analytics.com", "googletagmanager.com",
    "doubleclick.net", "stats.g.doubleclick.net", "google.com/g/collect",
    "segment.io", "segment.com", "amplitude.com", "mixpanel.com",
    "sentry.io", "bugsnag.com", "datadoghq.com", "newrelic.com",
    "hotjar.com", "fullstory.com", "clarity.ms", "intercom.io",
    "facebook.com/tr", "bat.bing.com", "clicky.com", "matomo.cloud",
)


def _is_telemetry(url: str) -> bool:
    low = url.lower()
    return any(marker in low for marker in _TELEMETRY_HOSTS)


class AuthError(RuntimeError):
    pass


def load_storage_state(path: Path) -> dict[str, Any]:
    """Accept Playwright ``storage_state`` JSON *or* a raw cookie-array export.

    Browser extensions (EditThisCookie and friends) export a bare array with
    ``expirationDate`` and lowercase ``sameSite``. Detect by top-level type and
    normalise, so the user never has to declare which form they have.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(raw, dict) and ("cookies" in raw or "origins" in raw):
        raw.setdefault("cookies", [])
        raw.setdefault("origins", [])
        for cookie in raw["cookies"]:
            _normalise_cookie(cookie)
        return raw

    if isinstance(raw, list):
        cookies = [_normalise_cookie(dict(c)) for c in raw]
        return {"cookies": cookies, "origins": []}

    raise AuthError(
        f"{path} is neither a Playwright storage_state object nor a cookie array"
    )


def _normalise_cookie(cookie: dict[str, Any]) -> dict[str, Any]:
    if "expirationDate" in cookie:
        cookie["expires"] = float(cookie.pop("expirationDate"))
    cookie.setdefault("expires", -1)

    same = str(cookie.get("sameSite", "Lax")).lower()
    cookie["sameSite"] = {
        "no_restriction": "None", "none": "None", "unspecified": "Lax",
        "lax": "Lax", "strict": "Strict",
    }.get(same, "Lax")

    if not cookie.get("domain") and not cookie.get("url"):
        raise AuthError(f"cookie {cookie.get('name')!r} has neither domain nor url")
    cookie.setdefault("path", "/")

    # Playwright rejects unknown keys.
    allowed = {"name", "value", "domain", "path", "expires", "httpOnly", "secure", "sameSite", "url"}
    return {k: v for k, v in cookie.items() if k in allowed}


class Session:
    """Owns the browser, the context, and every event handler."""

    def __init__(self, cfg: RunConfig) -> None:
        self.cfg = cfg
        self.sink = EventSink()
        self._pw: Playwright | None = None
        self._browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None
        #: Pages the crawler owns and must never auto-close.
        self._owned: set[Page] = set()

    async def __aenter__(self) -> "Session":
        await self.start()
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()

    # -- lifecycle --------------------------------------------------------
    async def start(self) -> None:
        self._pw = await async_playwright().start()
        self._browser = await self._pw.chromium.launch(
            headless=self.cfg.browser.headless,
            slow_mo=self.cfg.browser.slow_mo_ms or None,
        )

        storage = (
            load_storage_state(self.cfg.auth.storage_state)
            if self.cfg.auth.storage_state
            else None
        )

        self.context = await self._browser.new_context(
            storage_state=storage,
            viewport={
                "width": self.cfg.browser.viewport_width,
                "height": self.cfg.browser.viewport_height,
            },
            user_agent=self.cfg.browser.user_agent,
            permissions=[],            # handler #6: prompts can never appear
            accept_downloads=True,     # so download events fire and we can cancel
        )
        self.context.set_default_timeout(self.cfg.crawl.action_timeout_ms)
        self.context.set_default_navigation_timeout(self.cfg.crawl.nav_timeout_ms)

        await self.context.add_init_script(INIT_SCRIPT)

        if self.cfg.browser.block_mutations:
            await self.context.route("**/*", self._write_guard)

        self.context.on("response", self._on_response)

        # Create the main page BEFORE registering the popup handler. The "page"
        # event fires for every page in the context including our own, and at
        # creation time `self.page` is not yet assigned -- so a handler
        # registered first would close the very page we just opened.
        self.page = await self.context.new_page()
        self._owned.add(self.page)
        self._attach_page_handlers(self.page)

        self.context.on("page", self._on_new_page)      # handler #2

    def _attach_page_handlers(self, page: Page) -> None:
        page.on("dialog", self._on_dialog)              # handler #3
        page.on("filechooser", self._on_file_chooser)   # handler #4
        page.on("download", self._on_download)          # handler #5
        page.on("console", self._on_console)
        page.on("pageerror", lambda e: self.sink.console_errors.append(str(e)))

    async def close(self) -> None:
        try:
            if self.context:
                await self.context.close()
        finally:
            if self._browser:
                await self._browser.close()
            if self._pw:
                await self._pw.stop()

    # -- handler 1: the network write-guard -------------------------------
    async def _write_guard(self, route: Route, request: Request) -> None:
        if request.method.upper() in MUTATING_METHODS:
            if _is_telemetry(request.url):
                # Still aborted -- we are not putting crawl traffic in anyone's
                # analytics -- but NOT recorded as a mutation. A GA "button_click"
                # beacon fires on every click, so counting it made every element
                # on the page look like it wrote to the server, and any click
                # that did nothing else was reported as blocked_mutation rather
                # than the inert click it actually was.
                await route.abort("blockedbyclient")
                return
            self.sink.blocked.append(f"{request.method} {request.url}")
            self.sink.network.append(
                EndpointObservation(method=request.method, url=request.url, blocked=True)
            )
            log.debug("write-guard blocked %s %s", request.method, request.url)
            await route.abort("blockedbyclient")
            return
        await route.continue_()

    async def _on_response(self, response: Any) -> None:
        try:
            req = response.request
            if req.resource_type in {"document", "xhr", "fetch"}:
                self.sink.network.append(
                    EndpointObservation(
                        method=req.method, url=response.url, status=response.status
                    )
                )
        except Exception:  # response can be gone mid-navigation; not worth failing over
            pass

    # -- handler 2: new tab / window --------------------------------------
    async def _on_new_page(self, page: Page) -> None:
        if page is self.page or page in self._owned:
            return
        self._attach_page_handlers(page)
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=2000)
        except Exception:
            pass
        url = page.url
        self.sink.new_pages.append(url)
        log.debug("captured popup tab: %s", url)
        try:
            await page.close()
        except Exception:
            pass

    # -- handler 3: native JS dialogs -------------------------------------
    async def _on_dialog(self, dialog: Dialog) -> None:
        self.sink.dialogs.append(
            Observation(
                kind="native_dialog",
                detail=f"{dialog.type}: {dialog.message[:300]}",
            )
        )
        try:
            if dialog.type == "beforeunload":
                await dialog.accept()   # allow navigation away
            else:
                await dialog.dismiss()  # confirm/alert/prompt -> the safe branch
        except Exception:
            pass

    # -- handler 4: file chooser (the hang case) --------------------------
    async def _on_file_chooser(self, chooser: FileChooser) -> None:
        el = chooser.element
        try:
            accept = await el.get_attribute("accept")
        except Exception:
            accept = None
        self.sink.file_choosers.append(
            Observation(
                kind="file_upload",
                detail=f"accept={accept or 'any'} multiple={chooser.is_multiple()}",
            )
        )
        try:
            await chooser.set_files([])   # dismiss without uploading
        except Exception:
            pass

    # -- handler 5: downloads ---------------------------------------------
    async def _on_download(self, download: Download) -> None:
        self.sink.downloads.append(
            Observation(
                kind="download",
                detail=f"{download.suggested_filename} <- {download.url}",
            )
        )
        try:
            await download.cancel()
        except Exception:
            pass

    def _on_console(self, msg: Any) -> None:
        if msg.type not in {"error", "assert"}:
            return
        text = msg.text[:500]
        if _is_our_own_noise(text):
            # The write-guard aborting a POST makes the page log a failed
            # fetch. Reporting that as an application defect would be us
            # flagging our own safety mechanism.
            return
        self.sink.console_errors.append(text)

    # -- auth verification ------------------------------------------------
    async def verify_auth(self) -> None:
        """Fail loudly rather than crawl a login wall.

        An expired cookie silently redirects to the login page; without this
        gate the tool happily explores it and confidently emits 40 test cases
        for a login form the user never asked about.
        """
        assert self.page is not None
        page = self.page

        await page.goto(self.cfg.target.url, wait_until="domcontentloaded")

        selector = self.cfg.auth.verify_selector
        if selector:
            try:
                await page.wait_for_selector(
                    selector, timeout=self.cfg.auth.verify_timeout_ms, state="attached"
                )
                return
            except Exception as exc:
                raise AuthError(
                    f"AUTH_FAILED: verify_selector {selector!r} not found at {page.url}. "
                    "The session cookie has probably expired -- re-export "
                    "auth.storage_state and try again."
                ) from exc

        landed = page.url.lower()
        if any(marker in landed for marker in ("/login", "/signin", "/sign-in", "/auth")):
            raise AuthError(
                f"AUTH_FAILED: redirected to {page.url}, which looks like a login page. "
                "Provide auth.storage_state, or set auth.verify_selector if this is "
                "genuinely the page you meant to crawl."
            )
