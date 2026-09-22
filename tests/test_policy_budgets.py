"""Policy, scope and budget rules. Pure functions, no browser."""

from __future__ import annotations

from collections import deque
from unittest.mock import AsyncMock

import pytest

from qagen.browser.budgets import Budgets
from qagen.browser.policy import InteractionPolicy, ScopeRules
from qagen.config import CrawlConfig, InteractionConfig, TargetConfig
from qagen.models import Confidence, Element, ElementKind


def make(kind: ElementKind, name: str, selector: str = "[data-testid=x]") -> Element:
    return Element(
        ref="E1", kind=kind, role="button", name=name, tag="button",
        selector=selector, selector_strategy="data-testid", confidence=Confidence.CERTAIN,
    )


@pytest.fixture
def policy() -> InteractionPolicy:
    return InteractionPolicy(InteractionConfig())


class TestInteractionPolicy:
    def test_allows_plain_button(self, policy):
        assert policy.evaluate(make(ElementKind.GENERIC_BUTTON, "Show details")).allowed

    def test_blocks_destructive_vocabulary(self, policy):
        decision = policy.evaluate(make(ElementKind.GENERIC_BUTTON, "Delete account"))
        assert not decision.allowed
        assert "delete" in decision.reason

    def test_word_boundary_avoids_false_positives(self, policy):
        """'Reset' is denied; 'Resettings' must not be."""
        assert not policy.evaluate(make(ElementKind.GENERIC_BUTTON, "Reset password")).allowed
        assert policy.evaluate(make(ElementKind.GENERIC_BUTTON, "Resettings view")).allowed

    def test_never_submits_forms(self, policy):
        decision = policy.evaluate(make(ElementKind.SUBMIT, "Save"))
        assert not decision.allowed
        assert "never submitted" in decision.reason

    def test_file_inputs_not_exercised(self, policy):
        assert not policy.evaluate(make(ElementKind.FILE_INPUT, "Attach")).allowed

    def test_external_links_recorded_not_clicked(self, policy):
        assert not policy.evaluate(make(ElementKind.EXTERNAL_LINK, "Docs")).allowed

    def test_disabled_element_skipped(self, policy):
        el = make(ElementKind.GENERIC_BUTTON, "Continue")
        el.enabled = False
        assert not policy.evaluate(el).allowed

    def test_allow_list_overrides_deny(self):
        cfg = InteractionConfig(allow_selectors=["[data-testid=safe-delete]"])
        p = InteractionPolicy(cfg)
        el = make(ElementKind.DESTRUCTIVE, "Delete draft", "[data-testid=safe-delete]")
        assert p.evaluate(el).allowed

    def test_passive_policy_blocks_everything(self):
        p = InteractionPolicy(InteractionConfig(policy="passive"))
        assert not p.evaluate(make(ElementKind.GENERIC_BUTTON, "Show")).allowed

    def test_consent_detection(self, policy):
        assert policy.is_consent_text("Accept all")
        assert not policy.is_consent_text("Save changes")


class TestScopeRules:
    @pytest.fixture
    def scope(self) -> ScopeRules:
        return ScopeRules(
            TargetConfig(url="https://app.test/dash", exclude_paths=["/logout", "/admin/**"])
        )

    def test_same_origin_allowed(self, scope):
        assert scope.in_scope("https://app.test/settings").allowed

    def test_other_origin_blocked(self, scope):
        assert not scope.in_scope("https://other.test/x").allowed

    def test_excluded_path_blocked(self, scope):
        assert not scope.in_scope("https://app.test/logout").allowed

    def test_non_http_scheme_blocked(self, scope):
        assert not scope.in_scope("mailto:a@b.test").allowed

    def test_include_paths_restrict(self):
        scope = ScopeRules(
            TargetConfig(url="https://app.test/", include_paths=["/dashboard/**"])
        )
        assert scope.in_scope("https://app.test/dashboard/a").allowed
        assert not scope.in_scope("https://app.test/other").allowed


class TestBudgets:
    def test_page_budget_stops(self):
        b = Budgets(CrawlConfig(max_pages=2))
        assert b.take_page() and b.take_page()
        assert not b.take_page()
        assert b.stop_reason == "max_pages"
        assert b.exhausted

    def test_click_budget_stops(self):
        b = Budgets(CrawlConfig(max_clicks=1))
        assert b.take_click()
        assert not b.take_click()
        assert b.stop_reason == "max_clicks"

    def test_no_new_states_stops(self):
        """The backstop for live-updating widgets that churn the fingerprint."""
        b = Budgets(CrawlConfig(max_consecutive_no_new_states=3))
        for _ in range(3):
            b.note_state(is_new=False)
        assert b.stop_reason == "max_consecutive_no_new_states"

    def test_new_state_resets_the_counter(self):
        b = Budgets(CrawlConfig(max_consecutive_no_new_states=3))
        b.note_state(False)
        b.note_state(False)
        b.note_state(True)
        b.note_state(False)
        assert b.stop_reason is None


class TestBackgroundTaskConsumption:
    """Regression: cancelling the networkidle task used to kill the crawl.

    `asyncio.CancelledError` inherits from BaseException, so awaiting a task we
    just cancelled -- inside `contextlib.suppress(Exception)` -- let it escape
    and unwind the entire run. The done-callback must swallow every outcome.
    """

    async def test_cancelled_task_is_consumed_without_raising(self):
        import asyncio
        from qagen.browser.analyzer import _consume_task_result

        async def slow():
            await asyncio.sleep(30)

        task = asyncio.create_task(slow())
        await asyncio.sleep(0)
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        _consume_task_result(task)   # must not raise

    async def test_failed_task_is_consumed_without_raising(self):
        import asyncio
        from qagen.browser.analyzer import _consume_task_result

        async def boom():
            raise TimeoutError("Timeout 8000ms exceeded")

        task = asyncio.create_task(boom())
        await asyncio.sleep(0)
        _consume_task_result(task)   # must not raise, and marks it retrieved
        assert isinstance(task.exception(), TimeoutError)


from types import SimpleNamespace


class TestShellDetection:
    """The app-frame split: a header and left menu that persist across URLs are
    furniture, and must not outrank the content area in the action plan."""

    def _element(self, ref: str, selector: str, name: str = "x"):
        from qagen.models import Confidence, Element, ElementKind

        return Element(
            ref=ref, kind=ElementKind.GENERIC_BUTTON, role="button", name=name,
            tag="button", selector=selector, selector_strategy="id",
            confidence=Confidence.HIGH,
        )

    def _page(self, url: str, elements):
        from qagen.models import PageModel

        return PageModel(url=url, normalized_url=url, title="t", elements=elements)

    def test_declared_selectors_are_shell_immediately(self):
        from qagen.browser.shell import ShellDetector

        det = ShellDetector(declared=["#navbar_menuList", "#settingNavbar"])
        assert det.is_shell(self._element("E1", "#navbar_menuList > li"))
        assert det.is_shell(self._element("E2", "#settingNavbar_li_user"))
        assert not det.is_shell(self._element("E3", "#content_addBtn"))

    def test_repetition_across_urls_infers_the_frame(self):
        """No configuration: an element on three different URLs is the frame."""
        from qagen.browser.shell import ShellDetector

        det = ShellDetector(min_urls=3)
        menu = self._element("E1", "#navbar_li_screen", "Screen")
        for url in ("/a", "/b", "/c"):
            det.observe(self._page(url, [menu, self._element("E2", f"#only{url}")]))
        assert det.is_shell(menu)
        assert not det.is_shell(self._element("E2", "#only/a"))

    def test_labels_are_applied_to_the_page(self):
        from qagen.browser.shell import ShellDetector

        det = ShellDetector(declared=["#navbar_li_"])
        page = self._page(
            "/x", [self._element("E1", "#navbar_li_screen"), self._element("E2", "#main_btn")]
        )
        det.label(page)
        assert [e.region for e in page.elements] == ["shell", "main"]
        assert page.main_actionable_count == 1
        assert page.actionable_count == 2

    def test_content_actions_are_planned_before_frame_actions(self):
        """The ordering that decides what a truncated state keeps."""
        from qagen.browser.crawler import Crawler

        frame = self._element("E1", "#navbar_li_screen", "aaa Screen")
        frame.region = "shell"
        content = self._element("E2", "#content_btn", "zzz Add content")
        page = self._page("/x", [frame, content])

        plan = Crawler._plan_actions(_StubCrawler(), page)
        assert [e.ref for e in plan] == ["E2", "E1"], [e.ref for e in plan]


class _StubCrawler:
    """Just enough of a Crawler for _plan_actions, which reads only config."""

    def __init__(self) -> None:
        self.cfg = SimpleNamespace(
            crawl=SimpleNamespace(
                max_clicks_per_state=30,
                action_order="reading",
                content_before_frame=True,
                reading_band_px=20,
                frame_reserve=0,
            )
        )
        self._exercised: dict = {}


class TestReadingOrder:
    """Top to bottom, left to right -- the order a person works down a screen."""

    def _el(self, ref, x, y, region="main", name="x"):
        from qagen.models import Confidence, Element, ElementKind

        return Element(
            ref=ref, kind=ElementKind.GENERIC_BUTTON, role="button", name=name,
            tag="button", selector=f"#{ref}", selector_strategy="id",
            confidence=Confidence.HIGH, x=x, y=y, w=40, h=24, region=region,
        )

    def _plan(self, elements, **crawl):
        from qagen.models import PageModel
        from qagen.browser.crawler import Crawler

        opts = dict(
            max_clicks_per_state=30, action_order="reading",
            content_before_frame=True, reading_band_px=20,
            frame_reserve=0,                # tested separately below
        )
        opts.update(crawl)
        stub = SimpleNamespace(
            cfg=SimpleNamespace(crawl=SimpleNamespace(**opts)), _exercised={}
        )
        page = PageModel(url="/x", normalized_url="/x", title="t", elements=elements)
        return [e.ref for e in Crawler._plan_actions(stub, page)]

    def test_rows_before_columns(self):
        """A lower element never precedes a higher one, whatever its x."""
        els = [
            self._el("bottomleft", x=0, y=500),
            self._el("topright", x=900, y=10),
            self._el("topleft", x=10, y=10),
        ]
        assert self._plan(els) == ["topleft", "topright", "bottomleft"]

    def test_same_row_sorts_left_to_right(self):
        els = [self._el("c", 800, 100), self._el("a", 20, 100), self._el("b", 400, 100)]
        assert self._plan(els) == ["a", "b", "c"]

    def test_near_aligned_elements_count_as_one_row(self):
        """A 32px button and the 24px icon beside it differ by a few pixels
        vertically; raw-y sorting would interleave two rows into a staircase."""
        els = [
            self._el("right_icon", x=900, y=104),
            self._el("left_button", x=20, y=100),
            self._el("next_row", x=20, y=160),
        ]
        assert self._plan(els) == ["left_button", "right_icon", "next_row"]

    def test_content_is_read_before_the_frame(self):
        """The header sits at y=0 but is furniture; content wins anyway."""
        els = [
            self._el("header_item", x=0, y=0, region="shell"),
            self._el("content_item", x=0, y=400, region="main"),
        ]
        assert self._plan(els) == ["content_item", "header_item"]

    def test_strict_reading_order_when_frame_priority_is_off(self):
        els = [
            self._el("header_item", x=0, y=0, region="shell"),
            self._el("content_item", x=0, y=400, region="main"),
        ]
        assert self._plan(els, content_before_frame=False) == [
            "header_item", "content_item",
        ]


class TestUnexercisedReserve:
    """The frame must reach the plan even when content fills the cap.

    A menu-driven SPA navigates only through its left menu, whose items are
    divs with no href -- so they are never enqueued as links. If the per-state
    cap is filled by content before the menu is reached, the crawl runs out of
    places to go. One real run ended with the frontier empty at 34 states and
    the left menu clicked twice in total.
    """

    def _el(self, ref, y, region):
        from qagen.models import Confidence, Element, ElementKind

        return Element(
            ref=ref, kind=ElementKind.GENERIC_BUTTON, role="button", name=ref,
            tag="button", selector=f"#{ref}", selector_strategy="id",
            confidence=Confidence.HIGH, x=0, y=y, w=40, h=24, region=region,
        )

    def _plan(self, elements, exercised=None, reserve=8, cap=3):
        from qagen.models import PageModel
        from qagen.browser.crawler import Crawler

        stub = SimpleNamespace(
            cfg=SimpleNamespace(
                crawl=SimpleNamespace(
                    max_clicks_per_state=cap, action_order="reading",
                    content_before_frame=True, reading_band_px=20,
                    frame_reserve=reserve,
                )
            ),
            _exercised=exercised or {},
        )
        page = PageModel(url="/x", normalized_url="/x", title="t", elements=elements)
        return [e.ref for e in Crawler._plan_actions(stub, page)]

    def test_frame_survives_a_cap_filled_by_content(self):
        els = [self._el(f"c{i}", 100 + i * 40, "main") for i in range(6)]
        els.append(self._el("menu_screen", 200, "shell"))
        plan = self._plan(els, cap=3)
        assert plan[:3] == ["c0", "c1", "c2"], plan
        assert "menu_screen" in plan, plan

    def test_reserve_skips_frame_controls_already_exercised_elsewhere(self):
        """Free by construction: each control costs one click in the whole run."""
        menu = self._el("menu_screen", 200, "shell")
        els = [self._el(f"c{i}", 100 + i * 40, "main") for i in range(6)] + [menu]
        plan = self._plan(els, exercised={menu.identity(): "N001"}, cap=3)
        assert plan == ["c0", "c1", "c2"], plan

    def test_reserve_does_not_smuggle_content_past_the_cap(self):
        """Otherwise the cap silently becomes cap + reserve on every state."""
        els = [self._el(f"c{i}", 100 + i * 40, "main") for i in range(6)]
        assert self._plan(els, cap=3) == ["c0", "c1", "c2"]

    def test_reserve_can_be_switched_off(self):
        els = [self._el(f"c{i}", 100 + i * 40, "main") for i in range(6)]
        els.append(self._el("menu_screen", 200, "shell"))
        assert self._plan(els, reserve=0, cap=3) == ["c0", "c1", "c2"]


class TestLocationWording:
    """Where a control is, said the way a tester would say it.

    This is what lets a generated step read "click the '+' on the Screen card
    (main area, top-left)" instead of quoting a CSS selector at someone who is
    looking at a screen.
    """

    def _el(self, x, y, w=40, h=24, landmark=None):
        from qagen.models import Confidence, Element, ElementKind

        return Element(
            ref="E1", kind=ElementKind.GENERIC_BUTTON, role="button", name="b",
            tag="button", selector="#b", selector_strategy="id",
            confidence=Confidence.HIGH, x=x, y=y, w=w, h=h, landmark=landmark,
        )

    def test_named_landmarks_win(self):
        el = self._el(1100, 20, landmark="header")
        assert el.describe_location(1200, 3000).startswith("header,")

    def test_dialog_beats_position(self):
        """Inside a modal, "main area" would be actively misleading."""
        el = self._el(600, 400, landmark="dialog")
        assert el.describe_location(1200, 3000).startswith("dialog,")

    def test_sidebar_inferred_from_position(self):
        """Apps build sidebars out of plain divs, so geometry stands in for the
        landmark the markup never declared."""
        el = self._el(10, 300, w=200)
        assert el.describe_location(1200, 3000).startswith("left sidebar,")

    def test_vertical_is_measured_against_the_document(self):
        """"Bottom of the page" means the end of the content, not the window."""
        el = self._el(600, 2900)
        assert "bottom" in el.describe_location(1200, 3000)
        assert "top" in self._el(600, 40).describe_location(1200, 3000)

    def test_horizontal_thirds(self):
        assert "left" in self._el(50, 500, w=40).describe_location(1200, 3000)
        assert "centre" in self._el(580, 500, w=40).describe_location(1200, 3000)
        assert "right" in self._el(1100, 500, w=40).describe_location(1200, 3000)

    def test_reads_as_one_phrase(self):
        el = self._el(1100, 20, landmark="header")
        assert el.describe_location(1200, 3000) == "header, top-right"


class TestStateChargedOnce:
    """A state pays the per-URL budget once, however many times it is seen.

    A popup is seen twice -- when a click reveals it, and again when its replay
    item comes off the frontier. Charging both made one popup cost two of its
    page's six slots; on a real run the homepage was exhausted five minutes into
    three hours, and the crawl starved with 49 of 2000 clicks spent.
    """

    def _crawler(self, per_url=2):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(
            crawl=SimpleNamespace(
                max_states_per_url=per_url, max_states_per_section=99,
                module_budgets={},
            )
        )
        c._per_url, c._per_section, c._charged, c._cap_rejections = {}, {}, set(), {}
        c.log = SimpleNamespace(note=lambda *a, **k: None)
        return c

    def _page(self, fp, url="https://x.test/home"):
        from qagen.models import PageModel

        return PageModel(url=url, normalized_url=url, title="t", fingerprint=fp)

    def test_same_state_seen_twice_pays_once(self):
        c = self._crawler(per_url=2)
        popup = self._page("fp-popup")
        assert c._url_budget_ok(popup) is True      # discovered by a click
        assert c._url_budget_ok(popup) is True      # re-entered by replay
        assert c._per_url["https://x.test/home"] == 1

    def test_distinct_states_still_consume_the_budget(self):
        c = self._crawler(per_url=2)
        assert c._url_budget_ok(self._page("fp-1")) is True
        assert c._url_budget_ok(self._page("fp-2")) is True
        assert c._url_budget_ok(self._page("fp-3")) is False

    def test_rejections_are_counted_so_they_cannot_hide(self):
        c = self._crawler(per_url=1)
        c._url_budget_ok(self._page("fp-1"))
        c._url_budget_ok(self._page("fp-2"))
        assert c._cap_rejections["max_states_per_url"] == 1


class TestRestoreDoesNotAbandonTheState:
    """One failed restore must not discard the rest of a screen's plan.

    App-frame controls (header, left menu) are planned last, so they were always
    in the tail that got thrown away. On a real run the entry page had 46
    elements, attempted 28, hit one failed restore, and dropped the remaining 18
    -- the notification bell among them.
    """

    def _crawler(self, max_failures=3):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(
            crawl=SimpleNamespace(
                max_restore_failures=max_failures,
                action_timeout_ms=1000,
            )
        )
        return c

    def test_config_default_allows_recovery(self):
        """The default must be >1, or the old abandon-immediately behaviour
        returns under a different name."""
        from qagen.config import CrawlConfig

        assert CrawlConfig().max_restore_failures >= 2

    def test_hard_reset_is_used_and_bounded(self):
        """The recovery path exists, and repeated failure still terminates."""
        import inspect
        from qagen.browser.crawler import Crawler

        src = inspect.getsource(Crawler._act_on_state)
        assert "_hard_reset" in src, "no recovery path after a failed restore"
        assert "max_restore_failures" in src, "recovery is unbounded"
        assert "state_abandoned" in src, "gives up without saying so"
        # and the old unconditional bail is gone
        assert "ending actions for this state" not in src

    def test_hard_reset_replays_into_a_popup(self):
        """A popup has no URL: reloading alone lands on the page behind it."""
        import inspect
        from qagen.browser.crawler import Crawler

        src = inspect.getsource(Crawler._hard_reset)
        assert "replay" in src, "hard reset cannot return to a popup state"


class TestConsecutiveFailuresResetOnHardReset:
    """The bug found from a real crawl log: the counter that decides "give up
    on this state" only reset on a successful CHEAP restore, never on a
    successful hard reset. On this app the cheap restore's exact-signature
    match rarely holds at all (measured: 67 of 141 failed in one run), so
    every hard reset succeeding was still uncredited -- one state was
    abandoned after exactly 5 actions with 88 still unattempted, even though
    the hard reset had not failed even once.
    """

    def _crawler(self, max_failures=5, hard_reset_result=True):
        from qagen.browser.crawler import Crawler
        from qagen.models import Confidence, Element, ElementKind

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(crawl=SimpleNamespace(max_restore_failures=max_failures))
        c.policy = SimpleNamespace(evaluate=lambda el: SimpleNamespace(allowed=True))
        c.budgets = SimpleNamespace(exhausted=False, take_click=lambda: True)
        c._exercised = {}
        c.log = SimpleNamespace(
            action=lambda *a, **k: None, note=lambda *a, **k: None,
            restore=lambda *a, **k: None,
        )
        c._perform = AsyncMock()
        c._restore = AsyncMock(return_value=False)   # cheap restore always "fails"
        c._hard_reset = AsyncMock(return_value=hard_reset_result)

        def make_el(i):
            return Element(
                ref=f"E{i}", kind=ElementKind.GENERIC_BUTTON, role="button", name=f"e{i}",
                tag="button", selector=f"#e{i}", selector_strategy="id",
                confidence=Confidence.HIGH,
            )

        c._plan = [make_el(i) for i in range(20)]
        c._plan_actions = lambda model, only=frozenset(): c._plan
        return c

    async def _run(self, c):
        node = SimpleNamespace(id="N001")
        item = SimpleNamespace(only_identities=frozenset())
        await c._act_on_state(page=None, model=None, node=node, item=item)

    @pytest.mark.asyncio
    async def test_every_action_runs_when_hard_reset_always_succeeds(self):
        """The core fix: 20 actions, cheap restore fails every time, hard
        reset succeeds every time -- all 20 must still be attempted, not just
        the first max_restore_failures of them."""
        c = self._crawler(max_failures=5, hard_reset_result=True)
        await self._run(c)
        assert c._perform.await_count == 20

    @pytest.mark.asyncio
    async def test_only_true_double_failures_count_toward_abandonment(self):
        """When hard reset also fails every time, abandonment after
        max_restore_failures is still correct and still happens -- the fix
        does not make the crawl un-abandonable, only correctly credited."""
        c = self._crawler(max_failures=5, hard_reset_result=False)
        await self._run(c)
        assert c._perform.await_count == 5

    @pytest.mark.asyncio
    async def test_a_run_of_successes_resets_the_counter_for_a_later_run_of_failures(self):
        """4 recovered failures, then a real success, then failures again --
        the earlier near-miss must not carry over."""
        c = self._crawler(max_failures=5, hard_reset_result=True)
        results = [False] * 4 + [True] + [False] * 20
        c._restore = AsyncMock(side_effect=lambda *a, **k: results.pop(0) if results else False)
        await self._run(c)
        # After the True at position 5 resets the counter, it takes another
        # full 5 failures to abandon -- so the plan runs past position 10.
        assert c._perform.await_count > 10


class TestInertClickRetry:
    """A click that appears to do nothing is retried once for a
    pointer-cursor / inferred-clickable control before it is believed --
    React attaches handlers after hydration, so a click landing a moment
    early is genuinely inert the first time and genuinely not the second.

    Evidence: "Add Screen" and "New Screen Wall" both registered no_change on
    their one and only attempt, each finishing in under a second right after
    two other clicks had each taken the full 10s timeout.
    """

    def _crawler(self):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(
            crawl=SimpleNamespace(action_timeout_ms=1000, max_settle_ms=1000)
        )
        c.log = SimpleNamespace(note=lambda *a, **k: None, outcome=lambda *a, **k: None)
        c.result = SimpleNamespace(skips=[], observations=[])
        c._cheap = {}
        c._seen = {}
        c.graph = SimpleNamespace(add_edge=lambda *a, **k: None)
        c._reversibility = lambda outcome: "goto"
        return c

    def _el(self, kind, pointer_cursor=False):
        from qagen.models import Confidence, Element

        return Element(
            ref="E1", kind=kind, role="button", name="Add Screen", tag="div",
            selector="#addscreen", selector_strategy="data-testid",
            confidence=Confidence.HIGH, pointer_cursor=pointer_cursor,
        )

    def _session_stub(self, blocked=None, dialogs=None):
        empty = SimpleNamespace(
            blocked=blocked or [], dialogs=dialogs or [], new_pages=[],
            file_choosers=[], downloads=[],
        )
        return SimpleNamespace(sink=SimpleNamespace(drain=lambda: empty))

    def _page_stub(self, url="https://x.test/screen"):
        page = AsyncMock()
        page.url = url
        locator = AsyncMock()
        locator.count = AsyncMock(return_value=1)
        page.locator = lambda *a, **k: SimpleNamespace(first=locator)
        return page, locator

    @pytest.mark.asyncio
    async def test_inert_inferred_clickable_is_retried_once(self):
        from qagen.models import ElementKind, PageModel

        c = self._crawler()
        c.session = self._session_stub()
        c.analyzer = SimpleNamespace(
            settle=AsyncMock(), dismiss_consent=AsyncMock(),
            signature=AsyncMock(return_value="same-signature"),
        )
        c._analyze = AsyncMock()
        c._canonicalise = lambda *a, **k: None
        c._canonicalise_inpage = lambda *a, **k: None
        from qagen.models import Outcome

        c._classify_outcome = lambda *a, **k: (Outcome.NO_CHANGE, [])

        page, locator = self._page_stub()
        el = self._el(ElementKind.INFERRED_CLICKABLE)
        model = PageModel(url=page.url, normalized_url=page.url, title="t", fingerprint="fp1")
        node = SimpleNamespace(id="N001")

        await c._perform(page, model, node, el)

        # One click to open the plan, one retry -- two clicks total.
        assert locator.click.await_count == 2

    @pytest.mark.asyncio
    async def test_a_role_based_control_is_not_retried(self):
        """A real <button> that genuinely does nothing must not be clicked
        twice -- retrying every high-confidence control doubles the click
        budget for no gain."""
        from qagen.models import ElementKind, PageModel

        c = self._crawler()
        c.session = self._session_stub()
        c.analyzer = SimpleNamespace(
            settle=AsyncMock(), dismiss_consent=AsyncMock(),
            signature=AsyncMock(return_value="same-signature"),
        )
        c._analyze = AsyncMock()
        c._canonicalise = lambda *a, **k: None
        c._canonicalise_inpage = lambda *a, **k: None
        from qagen.models import Outcome

        c._classify_outcome = lambda *a, **k: (Outcome.NO_CHANGE, [])

        page, locator = self._page_stub()
        el = self._el(ElementKind.GENERIC_BUTTON, pointer_cursor=False)
        model = PageModel(url=page.url, normalized_url=page.url, title="t", fingerprint="fp1")
        node = SimpleNamespace(id="N001")

        await c._perform(page, model, node, el)

        assert locator.click.await_count == 1

    @pytest.mark.asyncio
    async def test_a_blocked_write_is_not_retried(self):
        """The first click already produced a real, useful result -- clicking
        again would just attempt the same write a second time."""
        from qagen.models import ElementKind, PageModel

        c = self._crawler()
        c.session = self._session_stub(blocked=["POST https://x.test/api/y"])
        c.analyzer = SimpleNamespace(
            settle=AsyncMock(), dismiss_consent=AsyncMock(),
            signature=AsyncMock(return_value="same-signature"),
        )
        c._analyze = AsyncMock()
        c._canonicalise = lambda *a, **k: None
        c._canonicalise_inpage = lambda *a, **k: None
        from qagen.models import Outcome

        c._classify_outcome = lambda *a, **k: (Outcome.BLOCKED_MUTATION, [])

        page, locator = self._page_stub()
        el = self._el(ElementKind.INFERRED_CLICKABLE)
        model = PageModel(url=page.url, normalized_url=page.url, title="t", fingerprint="fp1")
        node = SimpleNamespace(id="N001")

        await c._perform(page, model, node, el)

        assert locator.click.await_count == 1


class TestHardResetSurvivesAPartialReplay:
    """_hard_reset's own stated goal is "somewhere we can keep testing from,
    not the exact state" -- but the old code returned total failure the
    instant a single replay step's selector went stale (a virtualised grid
    row that scrolled away, a per-row menu tied to a specific row). Real
    evidence: 10 replay_failed events in one run, several against MUI
    DataGrid positional selectors -- each one used to cost the entire
    remaining plan of that state.
    """

    def _crawler(self):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(crawl=SimpleNamespace(action_timeout_ms=1000))
        c.log = SimpleNamespace(note=lambda *a, **k: None)
        c.budgets = SimpleNamespace(take_navigation=lambda: True)
        c.analyzer = SimpleNamespace(settle=AsyncMock(), dismiss_consent=AsyncMock())
        c._replay_by_fingerprint = {}
        return c

    def _page_with_resolving(self, resolving_selectors):
        from unittest.mock import MagicMock

        page = AsyncMock()
        page.goto = AsyncMock()

        def locator_factory(selector):
            loc = AsyncMock()
            loc.count = AsyncMock(return_value=1 if selector in resolving_selectors else 0)
            return SimpleNamespace(first=loc)

        page.locator = MagicMock(side_effect=locator_factory)
        return page

    @pytest.mark.asyncio
    async def test_a_stale_replay_step_still_returns_true(self):
        """The step at depth 1 no longer resolves -- the old code returned
        False here. The base page load succeeded, which is enough."""
        from qagen.browser.crawler import ReplayStep
        from qagen.models import PageModel

        c = self._crawler()
        page = self._page_with_resolving({"#step0"})   # step1 is gone
        model = PageModel(url="https://x.test/screen", normalized_url="https://x.test/screen", title="t")
        item = SimpleNamespace(
            replay=(ReplayStep(selector="#step0", label="a"), ReplayStep(selector="#step1", label="b"))
        )

        result = await c._hard_reset(page, model, item)
        assert result is True

    @pytest.mark.asyncio
    async def test_every_step_resolving_still_works_as_before(self):
        from qagen.browser.crawler import ReplayStep
        from qagen.models import PageModel

        c = self._crawler()
        page = self._page_with_resolving({"#step0", "#step1"})
        model = PageModel(url="https://x.test/screen", normalized_url="https://x.test/screen", title="t")
        item = SimpleNamespace(
            replay=(ReplayStep(selector="#step0", label="a"), ReplayStep(selector="#step1", label="b"))
        )

        result = await c._hard_reset(page, model, item)
        assert result is True

    @pytest.mark.asyncio
    async def test_the_base_navigation_itself_failing_is_still_a_real_failure(self):
        """Leniency applies to the replay chain, not to the page failing to
        load at all."""
        from qagen.models import PageModel

        c = self._crawler()
        page = AsyncMock()
        page.goto = AsyncMock(side_effect=Exception("net::ERR_CONNECTION_RESET"))
        model = PageModel(url="https://x.test/screen", normalized_url="https://x.test/screen", title="t")
        item = SimpleNamespace(replay=())

        result = await c._hard_reset(page, model, item)
        assert result is False

    @pytest.mark.asyncio
    async def test_no_replay_needed_is_unaffected(self):
        """A plain page (not a popup) has nothing to replay -- must still
        succeed once the base page loads."""
        from qagen.models import PageModel

        c = self._crawler()
        page = self._page_with_resolving(set())
        model = PageModel(url="https://x.test/screen", normalized_url="https://x.test/screen", title="t")
        item = SimpleNamespace(replay=())

        result = await c._hard_reset(page, model, item)
        assert result is True


class TestStateCanonicalisation:
    """The same screen caught mid-render must not become two states.

    Real evidence: two captures of /screen fingerprinted as 4ed56555 and
    91a1db03 -- two states -- while their screenshots were byte-identical (same
    md5) and their anchor sets matched 214 of 214. On one run /screen became 31
    states and the homepage 17, purely from this.
    """

    def _crawler(self, threshold=0.9):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(crawl=SimpleNamespace(state_anchor_threshold=threshold))
        c._page_anchors = {}
        c.log = SimpleNamespace(note=lambda *a, **k: None)
        return c

    def _page(self, fp, anchors, url="https://x.test/screen"):
        from qagen.models import Confidence, Element, ElementKind, PageModel

        els = [
            Element(
                ref=f"E{i}", kind=ElementKind.GENERIC_BUTTON, role="button", name=a,
                tag="button", selector=a, selector_strategy="data-testid",
                confidence=Confidence.HIGH,
            )
            for i, a in enumerate(anchors)
        ]
        return PageModel(
            url=url, normalized_url=url, title="t", fingerprint=fp, elements=els
        )

    def test_identical_anchors_collapse_to_one_state(self):
        c = self._crawler()
        base = [f"[data-testid=\"a{i}\"]" for i in range(20)]
        first = self._page("fp_early", base)
        second = self._page("fp_late", base)
        assert c._canonicalise(first) is False        # first sighting registers
        assert c._canonicalise(second) is True        # second adopts it
        assert second.fingerprint == "fp_early"

    def test_a_few_extra_anchors_still_the_same_screen(self):
        """Mid-render captures differ by a handful of late-arriving controls."""
        c = self._crawler()
        base = [f"[data-testid=\"a{i}\"]" for i in range(40)]
        c._canonicalise(self._page("fp_early", base))
        late = self._page("fp_late", base + ['[data-testid="a40"]', '[data-testid="a41"]'])
        assert c._canonicalise(late) is True
        assert late.fingerprint == "fp_early"

    def test_a_genuinely_different_screen_stays_separate(self):
        c = self._crawler()
        c._canonicalise(self._page("fp_a", [f"[data-testid=\"a{i}\"]" for i in range(20)]))
        other = self._page("fp_b", [f"[data-testid=\"b{i}\"]" for i in range(20)])
        assert c._canonicalise(other) is False
        assert other.fingerprint == "fp_b"

    def test_same_anchors_on_a_different_url_stay_separate(self):
        """Two sections can share a layout; the URL still separates them."""
        c = self._crawler()
        base = [f"[data-testid=\"a{i}\"]" for i in range(20)]
        c._canonicalise(self._page("fp_screen", base, url="https://x.test/screen"))
        other = self._page("fp_content", base, url="https://x.test/content")
        assert c._canonicalise(other) is False

    def test_a_page_with_no_stable_anchors_is_left_alone(self):
        """Nothing dependable to compare -- do not guess."""
        c = self._crawler()
        page = self._page("fp_a", [])
        assert c._canonicalise(page) is False
        assert page.fingerprint == "fp_a"

    def test_threshold_of_one_still_merges_only_exact_matches(self):
        c = self._crawler(threshold=1.0)
        base = [f"[data-testid=\"a{i}\"]" for i in range(10)]
        c._canonicalise(self._page("fp_a", base))
        near = self._page("fp_b", base + ['[data-testid="extra"]'])
        assert c._canonicalise(near) is False        # 91% -- not identical
        exact = self._page("fp_c", base)
        assert c._canonicalise(exact) is True


class TestRevealedOnlyPlanning:
    """A popup is planned against what it revealed, not the page behind it.

    Measured on a real run: the median popup state carries 49 actionable
    elements of which only 7 are new. Planning all 49 lets the per-state click
    budget push the real 7 out of reach entirely -- the crawler opens a menu and
    never touches it.
    """

    def _el(self, ref, y=100, name=None):
        from qagen.models import Confidence, Element, ElementKind

        return Element(
            ref=ref, kind=ElementKind.GENERIC_BUTTON, role="button",
            name=name or ref, tag="button", selector=f"#{ref}",
            selector_strategy="id", confidence=Confidence.HIGH, x=0, y=y, w=40, h=24,
        )

    def _plan(self, elements, only=frozenset(), cap=30):
        from qagen.models import PageModel
        from qagen.browser.crawler import Crawler

        stub = SimpleNamespace(
            cfg=SimpleNamespace(
                crawl=SimpleNamespace(
                    max_clicks_per_state=cap, action_order="reading",
                    content_before_frame=True, reading_band_px=20, frame_reserve=0,
                )
            ),
            _exercised={},
            log=SimpleNamespace(note=lambda *a, **k: None),
        )
        page = PageModel(url="/x", normalized_url="/x", title="t", elements=elements)
        return [e.ref for e in Crawler._plan_actions(stub, page, only=only)]

    def test_only_the_revealed_controls_are_planned(self):
        page_buttons = [self._el(f"page{i}", y=100 + i * 30) for i in range(20)]
        menu = [self._el("menu_upload", y=400), self._el("menu_url", y=430)]
        only = frozenset(e.identity() for e in menu)
        assert self._plan(page_buttons + menu, only=only) == ["menu_upload", "menu_url"]

    def test_the_budget_cannot_push_revealed_controls_out(self):
        """The real bug: with a cap of 3 and the menu sorting last, an
        unrestricted plan never reaches the menu at all."""
        page_buttons = [self._el(f"page{i}", y=100 + i * 30) for i in range(20)]
        menu = [self._el("menu_upload", y=900), self._el("menu_url", y=930)]
        elements = page_buttons + menu
        assert self._plan(elements, cap=3) == ["page0", "page1", "page2"]
        only = frozenset(e.identity() for e in menu)
        assert self._plan(elements, only=only, cap=3) == ["menu_upload", "menu_url"]

    def test_falls_back_to_the_whole_state_when_nothing_matches(self):
        """Never do nothing: a stale diff must not waste the state."""
        page_buttons = [self._el(f"page{i}", y=100 + i * 30) for i in range(3)]
        stale = frozenset({"role\x1fgone\x1f#gone"})
        assert self._plan(page_buttons, only=stale) == ["page0", "page1", "page2"]

    def test_no_restriction_plans_everything(self):
        page_buttons = [self._el(f"page{i}", y=100 + i * 30) for i in range(3)]
        assert self._plan(page_buttons) == ["page0", "page1", "page2"]


class TestPopupQueueDedup:
    """The same popup must not be queued once per route that reaches it.

    Measured on a real run: one "Export" button produced 4 popup states and 21
    unnamed `div` triggers produced 21, because the queue was keyed on the
    selector -- and a quarter of selectors here are positional, so the same
    control looks new every time the list redraws.
    """

    def _el(self, name, selector, strategy="css-path"):
        from qagen.models import Confidence, Element, ElementKind

        return Element(
            ref="E1", kind=ElementKind.GENERIC_BUTTON, role="button", name=name,
            tag="div", selector=selector, selector_strategy=strategy,
            confidence=Confidence.HIGH,
        )

    def test_same_button_at_a_different_position_is_one_popup(self):
        """`li:nth-of-type(3)` becoming `li:nth-of-type(2)` is a redraw, not a
        new button."""
        a = self._el("Export", "ul > li:nth-of-type(3) > div")
        b = self._el("Export", "ul > li:nth-of-type(2) > div")
        assert a.identity() != b.identity()          # the old key: two buttons
        assert a.stable_identity() == b.stable_identity()   # the new key: one

    def test_a_stable_label_is_preferred_over_the_name(self):
        el = self._el("Export", '[data-testid="export_btn"]', "data-testid")
        assert 'data-testid="export_btn"' in el.stable_identity()

    def test_digits_in_a_name_do_not_split_one_control(self):
        """"2 of 2 selected" becoming "3 of 3 selected" is the same toolbar."""
        a = self._el("2 of 2 selected", "div.toolbar > span")
        b = self._el("3 of 3 selected", "div.toolbar > span:nth-of-type(2)")
        assert a.stable_identity() == b.stable_identity()

    def test_genuinely_different_buttons_stay_different(self):
        a = self._el("Export", "div.a")
        b = self._el("Delete", "div.b")
        assert a.stable_identity() != b.stable_identity()

    def test_unnamed_controls_fall_back_to_the_selector(self):
        """No label and no name -- keep the old behaviour rather than merging
        two unrelated controls into one."""
        a = self._el("", "div.x > span:nth-of-type(1)")
        b = self._el("", "div.y > span:nth-of-type(2)")
        assert a.stable_identity() != b.stable_identity()


class TestInpageCanonicalisation:
    """Settings tabs, which swap content without changing the URL, must not
    fork into duplicate states the same way full pages used to.

    Real evidence: two visits to Settings > Plan produced different
    fingerprints while their screenshots were byte-identical and their anchor
    sets matched 100%.
    """

    def _crawler(self, threshold=0.9):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(crawl=SimpleNamespace(state_anchor_threshold=threshold))
        c._inpage_anchors = {}
        c.log = SimpleNamespace(note=lambda *a, **k: None)
        return c

    def _page(self, fp, anchors, url="https://x.test/settings"):
        from qagen.models import Confidence, Element, ElementKind, PageModel

        els = [
            Element(
                ref=f"E{i}", kind=ElementKind.GENERIC_BUTTON, role="button", name=a,
                tag="button", selector=a, selector_strategy="data-testid",
                confidence=Confidence.HIGH,
            )
            for i, a in enumerate(anchors)
        ]
        return PageModel(url=url, normalized_url=url, title="t", fingerprint=fp, elements=els)

    def _trigger(self, name="Plan"):
        from qagen.models import Confidence, Element, ElementKind

        safe = "".join(ch for ch in name.lower() if ch.isalnum()) or "trigger"
        return Element(
            ref="T1", kind=ElementKind.GENERIC_BUTTON, role="button", name=name,
            tag="div", selector=f'[data-testid="settings_{safe}"]',
            selector_strategy="data-testid", confidence=Confidence.HIGH,
        )

    def test_same_tab_visited_twice_merges(self):
        c = self._crawler()
        base = [f'[data-testid="plan_{i}"]' for i in range(15)]
        settings = self._page("settings_fp", [])
        first = self._page("plan_fp_1", base)
        second = self._page("plan_fp_2", base)
        trigger = self._trigger("Plan")
        assert c._canonicalise_inpage(settings, first, trigger) is False
        assert c._canonicalise_inpage(settings, second, trigger) is True
        assert second.fingerprint == "plan_fp_1"

    def test_two_different_tabs_never_merge(self):
        """Plan and Tag share the same base page but must stay distinct."""
        c = self._crawler()
        settings = self._page("settings_fp", [])
        plan = self._page("plan_fp", [f'[data-testid="x{i}"]' for i in range(10)])
        tag = self._page("tag_fp", [f'[data-testid="x{i}"]' for i in range(10)])
        c._canonicalise_inpage(settings, plan, self._trigger("Plan"))
        merged = c._canonicalise_inpage(settings, tag, self._trigger("Tag"))
        assert merged is False
        assert tag.fingerprint == "tag_fp"

    def test_two_different_popups_on_the_same_base_page_never_merge(self):
        """The Notification bell and a card's "+" share a base page too --
        different triggers must keep them fully separate, exactly like tabs."""
        c = self._crawler()
        home = self._page("home_fp", [], url="https://x.test/")
        notif = self._page(
            "notif_fp", [f'[data-testid="n{i}"]' for i in range(5)], url="https://x.test/"
        )
        addmenu = self._page(
            "add_fp", [f'[data-testid="n{i}"]' for i in range(5)], url="https://x.test/"
        )
        c._canonicalise_inpage(home, notif, self._trigger("Notification"))
        merged = c._canonicalise_inpage(home, addmenu, self._trigger("Add"))
        assert merged is False

    def test_no_stable_anchors_is_left_alone(self):
        c = self._crawler()
        settings = self._page("settings_fp", [])
        page = self._page("plan_fp", [])
        assert c._canonicalise_inpage(settings, page, self._trigger("Plan")) is False
        assert page.fingerprint == "plan_fp"


class TestThinCaptureRetry:
    """A page caught mid-render gets one more chance before being accepted.

    The old signal for this fired below hydration_min_elements (default 1),
    which never happens on a real page -- so nothing retried at all.
    """

    def _crawler(self, threshold=0.5):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(
            crawl=SimpleNamespace(
                thin_capture_threshold=threshold, thin_capture_retry_wait_ms=0,
            )
        )
        c._url_typical_count = {}
        c.log = SimpleNamespace(note=lambda *a, **k: None)
        c.analyzer = SimpleNamespace(settle=AsyncMock())
        return c

    def _page(self, n, url="https://x.test/screen"):
        from qagen.models import Confidence, Element, ElementKind, PageModel

        els = [
            Element(
                ref=f"E{i}", kind=ElementKind.GENERIC_BUTTON, role="button", name=f"e{i}",
                tag="button", selector=f"#e{i}", selector_strategy="id",
                confidence=Confidence.HIGH,
            )
            for i in range(n)
        ]
        return PageModel(url=url, normalized_url=url, title="t", elements=els)

    @pytest.mark.asyncio
    async def test_first_visit_is_never_retried(self):
        """Nothing to compare against yet -- accept it and record the baseline."""
        c = self._crawler()
        page = self._page(3)
        c._analyze = AsyncMock()
        result = await c._guard_thin_capture(None, page, 0, "entry")
        c._analyze.assert_not_called()
        assert result is page
        assert c._url_typical_count["https://x.test/screen"] == 3

    @pytest.mark.asyncio
    async def test_a_thin_second_visit_triggers_a_retry(self):
        c = self._crawler(threshold=0.5)
        c._url_typical_count["https://x.test/screen"] = 60
        thin = self._page(10)
        richer = self._page(55)
        c._analyze = AsyncMock(return_value=richer)
        result = await c._guard_thin_capture(None, thin, 0, "entry")
        c._analyze.assert_called_once()
        assert result is richer

    @pytest.mark.asyncio
    async def test_retry_that_does_not_improve_keeps_the_original(self):
        c = self._crawler(threshold=0.5)
        c._url_typical_count["https://x.test/screen"] = 60
        thin = self._page(10)
        still_thin = self._page(9)  # the retry itself raced too -- fewer, not more
        c._analyze = AsyncMock(return_value=still_thin)
        result = await c._guard_thin_capture(None, thin, 0, "entry")
        assert result is thin

    @pytest.mark.asyncio
    async def test_a_normal_capture_is_never_retried(self):
        c = self._crawler(threshold=0.5)
        c._url_typical_count["https://x.test/screen"] = 60
        normal = self._page(50)
        c._analyze = AsyncMock()
        result = await c._guard_thin_capture(None, normal, 0, "entry")
        c._analyze.assert_not_called()
        assert result is normal


class TestModuleBudgets:
    """A per-module budget stops one section (Settings) from starving every
    other one, the way it did when only max_states_per_section existed."""

    def _crawler(self, module_budgets=None):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(
            crawl=SimpleNamespace(
                max_states_per_url=200,
                max_states_per_section=12,
                module_budgets=module_budgets or {},
            )
        )
        c._per_url = {}
        c._per_section = {}
        c._charged = set()
        c._cap_rejections = {}
        c.log = SimpleNamespace(note=lambda *a, **k: None)
        return c

    def _page(self, fp, url):
        from qagen.models import PageModel

        return PageModel(url=url, normalized_url=url, title="t", fingerprint=fp)

    def test_module_budget_overrides_the_shared_cap(self):
        c = self._crawler(module_budgets={"channel": 1})
        assert c._url_budget_ok(self._page("fp1", "https://x.test/channel")) is True
        assert c._url_budget_ok(self._page("fp2", "https://x.test/channel")) is False

    def test_default_key_covers_unlisted_modules(self):
        c = self._crawler(module_budgets={"settings": 50, "default": 2})
        assert c._url_budget_ok(self._page("fp1", "https://x.test/vxtlabs")) is True
        assert c._url_budget_ok(self._page("fp2", "https://x.test/vxtlabs")) is True
        assert c._url_budget_ok(self._page("fp3", "https://x.test/vxtlabs")) is False

    def test_settings_can_no_longer_starve_other_modules(self):
        """The original bug: one shared cap let Settings take 43 of 63 states
        while Screen, Schedule and Channel got zero."""
        c = self._crawler(module_budgets={"settings": 50, "screen": 40, "default": 15})
        for i in range(20):
            assert c._url_budget_ok(
                self._page(f"settings{i}", f"https://x.test/settings/{i}")
            ) is True
        # Settings' generous budget does not touch Screen's separate one.
        assert c._url_budget_ok(self._page("screen1", "https://x.test/screen")) is True

    def test_empty_module_budgets_falls_back_to_the_shared_cap(self):
        """Unchanged behaviour when module_budgets is not configured at all."""
        c = self._crawler(module_budgets={})
        for i in range(12):
            assert c._url_budget_ok(
                self._page(f"fp{i}", f"https://x.test/settings/{i}")
            ) is True
        assert c._url_budget_ok(self._page("fp_over", "https://x.test/settings/over")) is False


class TestModuleSeeds:
    def _crawler(self, module_seeds=None):
        from qagen.browser.crawler import Crawler

        c = Crawler.__new__(Crawler)
        c.cfg = SimpleNamespace(
            target=SimpleNamespace(url="https://x.test/", id_collapse_exceptions=[]),
            crawl=SimpleNamespace(module_seeds=module_seeds or {}),
        )
        c._queued = set()
        c._frontier = deque()
        return c

    def test_seeds_are_queued_at_depth_one(self):
        c = self._crawler({"settings": ["/settings/plan", "/settings/tag"]})
        c._seed_modules()
        urls = {item.url for item in c._frontier}
        assert "https://x.test/settings/plan" in urls
        assert "https://x.test/settings/tag" in urls
        assert all(item.depth == 1 for item in c._frontier)

    def test_seeds_are_deduped_against_already_queued(self):
        c = self._crawler({"settings": ["/settings/plan"]})
        c._queued.add("https://x.test/settings/plan")
        c._seed_modules()
        assert len(c._frontier) == 0

    def test_no_seeds_configured_queues_nothing(self):
        c = self._crawler({})
        c._seed_modules()
        assert len(c._frontier) == 0
