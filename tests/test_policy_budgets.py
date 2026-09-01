"""Policy, scope and budget rules. Pure functions, no browser."""

from __future__ import annotations

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
                max_states_per_url=per_url, max_states_per_section=99
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
