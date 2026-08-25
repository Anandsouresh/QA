"""Integration tests against the local fixture app.

One test per claim the design makes about crawling and extraction. These need
Chromium:

    python -m playwright install chromium

The crawl runs once per session (see conftest.crawled); each test below is a
read against that single result.
"""

from __future__ import annotations

import asyncio

import pytest

from qagen.models import ElementKind, Outcome

playwright_installed = True
try:
    from playwright.async_api import async_playwright  # noqa: F401
except Exception:  # pragma: no cover
    playwright_installed = False

requires_browser = pytest.mark.skipif(
    not playwright_installed, reason="playwright is not installed"
)


@requires_browser
class TestExtraction:
    def test_captures_the_dashboard(self, crawled):
        result, *_ = crawled
        assert result.pages
        assert any("index.html" in p.url for p in result.pages)

    def test_inferred_form_without_form_tag_is_found(self, crawled):
        """Quick-add has no <form> tag; only the inferred-cluster pass finds it,
        and React apps mostly look like quick-add."""
        result, *_ = crawled
        inferred = [f for p in result.pages for f in p.forms if f.origin == "inferred"]
        assert inferred, "inferred form cluster was not detected"

    def test_explicit_form_constraints_extracted(self, crawled):
        """Constraints are what turn 'enter invalid text' into a real negative
        case, so they have to survive extraction."""
        result, *_ = crawled
        fields = [f for p in result.pages for form in p.forms for f in form.fields]
        emails = [f for f in fields if f.input_type == "email"]
        assert emails, "no email field extracted"
        assert any(f.required for f in emails)
        assert any(f.semantic_hint == "email" for f in emails)

    def test_maxlength_and_pattern_survive(self, crawled):
        result, *_ = crawled
        fields = [f for p in result.pages for form in p.forms for f in form.fields]
        assert any(f.maxlength for f in fields), "maxlength not captured"
        assert any(f.pattern for f in fields), "pattern not captured"

    def test_select_options_captured(self, crawled):
        result, *_ = crawled
        selects = [
            f
            for p in result.pages
            for form in p.forms
            for f in form.fields
            if f.input_type == "select"
        ]
        assert selects and selects[0].options

    def test_placeholder_only_label_is_low_confidence(self, crawled):
        """A field labelled only by its placeholder is an accessibility defect,
        and we mark it so it reaches the UI/UX category."""
        result, *_ = crawled
        fields = [f for p in result.pages for form in p.forms for f in form.fields]
        placeholder_labelled = [f for f in fields if f.label_source == "placeholder"]
        for field in placeholder_labelled:
            assert field.confidence.value == "low"

    def test_search_control_detected(self, crawled):
        result, *_ = crawled
        assert any(p.searches for p in result.pages)

    def test_every_element_has_a_selector(self, crawled):
        """The property that makes the graph a viable codegen substrate."""
        result, *_ = crawled
        for page in result.pages:
            for el in page.elements:
                assert el.selector, f"element {el.ref} on {page.url} has no selector"

    def test_unlabelled_div_classifies_as_inferred_clickable(self, crawled):
        """React's favourite pattern, and the reason the write-guard exists."""
        result, *_ = crawled
        kinds = {el.kind for p in result.pages for el in p.elements}
        assert ElementKind.INFERRED_CLICKABLE in kinds

    def test_card_and_the_button_inside_it_are_both_extracted(self, crawled):
        """The nesting claim, and the bug that motivated it.

        A dashboard card is clickable *and* carries its own "+" -- two separate
        test targets. The previous rule rejected any element with a
        pointer-cursor ancestor, so every control inside every clickable card
        was discarded; on a real dashboard that was 62 of 78 candidates.
        """
        result, *_ = crawled
        home = next(p for p in result.pages if "index.html" in p.url)
        selectors = {el.selector for el in home.elements}
        assert "#card-screen" in selectors, "clickable card was dropped"
        assert "#card-screen-add" in selectors, "the '+' inside the card was dropped"

    def test_passthrough_wrapper_yields_to_its_child(self, crawled):
        """Same box as its child means it is a shell -- report one, not two."""
        result, *_ = crawled
        home = next(p for p in result.pages if "index.html" in p.url)
        selectors = {el.selector for el in home.elements}
        assert "#wrapped-target" in selectors
        assert "#wrap-passthrough" not in selectors

    def test_container_row_is_not_reported_as_a_control(self, crawled):
        """`cursor` is inherited, so the flex row holding three cards computes
        to pointer too. A row is not something a tester clicks."""
        result, *_ = crawled
        home = next(p for p in result.pages if "index.html" in p.url)
        assert "#card-row" not in {el.selector for el in home.elements}

    def test_text_echo_of_a_clickable_ancestor_is_dropped(self, crawled):
        """The title span inside a card inherits pointer and repeats the card's
        own text; keeping it duplicates the card under a worse selector."""
        result, *_ = crawled
        home = next(p for p in result.pages if "index.html" in p.url)
        named_screen = [el for el in home.elements if el.name == "Screen"]
        assert len(named_screen) == 1, [el.selector for el in named_screen]

    def test_icon_only_control_is_named_by_its_hover_tooltip(self, crawled):
        """The "+" has no aria-label, no title and no text: the accname ladder
        returns "". Its only label is the tooltip shown on hover."""
        result, *_ = crawled
        home = next(p for p in result.pages if "index.html" in p.url)
        add = next(el for el in home.elements if el.selector == "#card-screen-add")
        assert add.name == "New"
        assert add.name_from_hover is True

    def test_hover_names_stay_out_of_the_fingerprint(self, crawled):
        """Whether the tooltip won the race is a property of our probe, not of
        the page -- letting it in would fingerprint one state two ways."""
        result, *_ = crawled
        home = next(p for p in result.pages if "index.html" in p.url)
        add = next(el for el in home.elements if el.selector == "#card-screen-add")
        assert add.signature()[1] == ""

    def test_same_page_menu_becomes_a_variant_of_its_page(self, crawled):
        """Clicking "+" leaves you on the same page with options showing. That
        is a real state, but it is a *variant* of the page -- recorded as a
        sibling it is just a second node with the same title and no way back."""
        _, graph, _, _ = crawled
        built = graph.build()
        menu = next(
            (n for n in built.nodes if n.opened_by == "Click 'New'"), None
        )
        assert menu is not None, [n.title for n in built.nodes]
        assert menu.node_type == "dropdown"
        assert menu.parent_state
        assert "New" in menu.title

    def test_popup_items_are_queued_not_clicked_immediately(self, crawled):
        """The BFS contract.

        Clicking a popup's items the moment it opens is depth-first: it dives to
        the bottom of one menu before the rest of the page has been touched. The
        popup is recorded, its revealed items are listed, and it goes on the
        frontier for the next depth instead.
        """
        _, graph, _, _ = crawled
        menu = next(n for n in graph.build().nodes if n.opened_by == "Click 'New'")
        queued = [line for line in menu.not_exercised if "queued for depth" in line]
        assert queued, menu.not_exercised
        assert any("Upload file" in line for line in queued), queued

    def test_a_queued_popup_is_re_entered_and_exercised(self, crawled):
        """And the queue is honoured: a popup with no URL of its own is reached
        again by replaying the click that opened it, then worked through like
        any other state."""
        _, graph, _, _ = crawled
        built = graph.build()
        popups = {n.id for n in built.nodes if n.parent_state}
        outgoing = {e.source for e in built.edges if e.source in popups}
        assert outgoing, "no popup was ever re-entered and acted on"

    def test_structural_roles_excluded_from_inventory(self, crawled):
        """role=region / role=search containers are not things a tester clicks."""
        result, *_ = crawled
        roles = {el.role for p in result.pages for el in p.elements}
        assert "region" not in roles
        assert "banner" not in roles


@requires_browser
class TestLoopPrevention:
    def test_templated_routes_collapse(self, crawled):
        """50 item URLs must become one state, not fifty."""
        result, *_ = crawled
        item_states = [p for p in result.pages if "item.html" in p.url]
        assert len(item_states) <= 1, f"item route did not collapse: {len(item_states)}"

    def test_no_duplicate_fingerprints(self, crawled):
        result, *_ = crawled
        prints = [p.fingerprint for p in result.pages]
        assert len(prints) == len(set(prints))

    def test_crawl_terminates_within_budget(self, crawled):
        _, _, budgets, cfg = crawled
        assert budgets.pages_visited <= cfg.crawl.max_pages
        assert budgets.clicks_made <= cfg.crawl.max_clicks
        assert budgets.elapsed < cfg.crawl.max_wall_clock_seconds

    def test_modal_becomes_its_own_state(self, crawled):
        """URL never changes, so a URL-keyed visited-set would miss it entirely."""
        _, graph, _, _ = crawled
        assert any(n.node_type == "modal" for n in graph.build().nodes)

    def test_toast_does_not_create_a_state(self, crawled):
        """A transient overlay must not make the same page a new state."""
        result, *_ = crawled
        index_states = [
            p for p in result.pages if p.normalized_url.endswith("index.html")
        ]
        # base + modal + disclosure-expanded + card menu is the legitimate
        # maximum here. The toast must not add a fifth.
        assert len(index_states) <= 4, [p.fingerprint for p in index_states]


@requires_browser
class TestOverlayHandling:
    def test_crawl_finished_rather_than_hanging(self, crawled):
        """The file-chooser and beforeunload handlers exist precisely so this
        holds -- unhandled, either one stalls the crawl instead of erroring."""
        _, _, budgets, cfg = crawled
        assert budgets.stop_reason != "max_wall_clock_seconds"

    def test_destructive_button_skipped_with_reason(self, crawled):
        result, *_ = crawled
        reasons = " ".join(s.reason for s in result.skips)
        assert "destructive" in reasons

    def test_file_input_recorded_but_not_exercised(self, crawled):
        result, *_ = crawled
        reasons = " ".join(s.reason for s in result.skips)
        assert "file input" in reasons

    def test_external_link_recorded_as_boundary(self, crawled):
        _, graph, _, _ = crawled
        assert any("example.com" in b.origin for b in graph.build().boundaries)

    def test_download_cancelled_and_recorded(self, crawled):
        result, *_ = crawled
        assert any(o.kind == "download" for o in result.observations)

    def test_mutations_blocked(self, crawled):
        """The write-guard catches what the deny-list cannot: an unlabelled div
        whose click handler POSTs."""
        result, *_ = crawled
        blocked = {m.split("?")[0] for p in result.pages for m in p.blocked_mutations}
        assert blocked, "no mutation was blocked; is the write-guard armed?"
        assert any("wipe" in b for b in blocked), blocked

    def test_consent_banner_dismissed(self, crawled):
        """A standing banner would appear in every fingerprint."""
        result, *_ = crawled
        names = {
            el.name.lower() for p in result.pages for el in p.elements
        }
        assert "accept all" not in names


@requires_browser
class TestNavigationGraph:
    def test_graph_has_entry_and_edges(self, crawled):
        _, graph, _, _ = crawled
        built = graph.build()
        assert built.entry_node
        assert built.nodes and built.edges

    def test_edges_carry_verified_locators(self, crawled):
        """Path -> script is only mechanical if every edge has a real locator."""
        _, graph, _, _ = crawled
        for edge in graph.build().edges:
            if edge.action == "click":
                assert edge.selector, f"click edge {edge.id} has no selector"

    def test_paths_reach_states_from_entry(self, crawled):
        _, graph, _, _ = crawled
        paths = graph.shortest_paths()
        assert paths
        assert paths[graph.build().entry_node] == []

    def test_blocked_edges_annotated_mutating(self, crawled):
        _, graph, _, _ = crawled
        mutating = [
            e for e in graph.build().edges if "mutating" in e.annotations
        ]
        assert mutating, "no edge was annotated as mutating"

    def test_mermaid_renders(self, crawled):
        from qagen.graph.render import to_mermaid

        _, graph, _, _ = crawled
        mermaid = to_mermaid(graph.build())
        assert mermaid.startswith("graph LR")
        assert "-->" in mermaid


@requires_browser
class TestEndToEnd:
    def test_full_run_writes_every_output(self, run_config):
        """Stub provider, so this is deterministic and needs no API key."""
        from qagen.orchestrator import Orchestrator

        manifest = asyncio.run(Orchestrator(run_config).run())
        out = run_config.output.dir

        for name in (
            "test-cases.md",
            "test-cases.json",
            "test-cases.xlsx",
            "test-cases.csv",
            "navgraph.json",
            "navgraph.mmd",
            "navgraph.dot",
            "navgraph-paths.json",
            "run_manifest.json",
        ):
            assert (out / name).exists(), f"{name} was not written"

        assert manifest["crawl"]["states_discovered"] > 0
        assert manifest["generation"]["cases_generated"] > 0
        assert manifest["auth_status"] == "ok"

        # The manifest is the audit trail -- it must explain what was skipped.
        assert manifest["crawl"]["skipped_elements"]
        assert manifest["crawl"]["blocked_mutations"]

    def test_a_popup_reached_again_is_still_exercised(self, crawled):
        """A replay that lands on a state we already know must still act.

        `_visit` used to recognise the fingerprint, log "seen this" and return
        -- so the menu was navigated to, re-opened, and then abandoned. In one
        real run that left 49 of 101 popups with no outgoing edges at all.
        """
        _, graph, _, _ = crawled
        built = graph.build()
        popups = {n.id for n in built.nodes if n.parent_state}
        assert popups, "no popup states captured"
        acted = {e.source for e in built.edges if e.source in popups}
        assert acted, "every popup was left unexercised"

    def test_every_state_keeps_its_page_model(self, crawled):
        """The generation phase reads page models; a state missing one produces
        no test cases however well it was crawled."""
        result, graph, _, _ = crawled
        have = {p.fingerprint for p in result.pages}
        missing = [
            n.id for n in graph.build().nodes
            if n.node_type not in ("boundary", "external") and n.fingerprint not in have
        ]
        assert not missing, f"states with no page model: {missing}"

    def test_completion_reason_describes_the_work(self, crawled):
        """"frontier empty" says nothing about coverage."""
        _, _, budgets, _ = crawled
        reason = budgets.stop_reason or ""
        assert reason, "no stop reason recorded"
        assert "actionable elements" in reason, reason
