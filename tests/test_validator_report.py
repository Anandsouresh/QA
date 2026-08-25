"""Validator, graph and renderers -- exercised through the stub adapter, so the
whole file runs with zero API calls and zero flake."""

from __future__ import annotations

import json

import pytest

from qagen.config import LLMConfig
from qagen.generation.stub import StubAdapter
from qagen.generation.validator import Validator
from qagen.graph.builder import GraphBuilder
from qagen.graph.render import to_dot, to_mermaid
from qagen.models import (
    Category,
    Confidence,
    Element,
    ElementKind,
    Outcome,
    PageModel,
    Step,
    TestCase,
    TestCaseBatch,
    TestSuite,
)
from qagen.report import json_out, markdown, tabular


def page_with(selectors: list[str]) -> PageModel:
    return PageModel(
        url="https://app.test/dash",
        normalized_url="https://app.test/dash",
        title="Dash",
        fingerprint="fp1",
        elements=[
            Element(
                ref=f"E{i}", kind=ElementKind.GENERIC_BUTTON, role="button",
                name=f"Button {i}", tag="button", selector=sel,
                selector_strategy="data-testid", confidence=Confidence.CERTAIN,
            )
            for i, sel in enumerate(selectors)
        ],
    )


def case(selectors: list[str], steps: int = 2) -> TestCase:
    return TestCase(
        test_id="TC_000",
        category=Category.HAPPY_PATH,
        preconditions=["Logged in"],
        steps=[
            Step(step_number=i + 1, action=f"Do {i}", expected_result=f"See {i}")
            for i in range(steps)
        ],
        overall_expected_result="It works",
        source_selectors=selectors,
    )


class TestSelectorGrounding:
    def test_grounded_case_passes(self):
        page = page_with(["[data-testid=a]"])
        kept, report = Validator().check_page_batch(
            TestCaseBatch(cases=[case(["[data-testid=a]"])]), page
        )
        assert len(kept) == 1
        assert not kept[0].needs_review
        assert not report.violations

    def test_fabricated_selector_is_flagged_not_dropped(self):
        """A flagged case a reviewer can reject beats a silently missing one."""
        page = page_with(["[data-testid=a]"])
        kept, report = Validator().check_page_batch(
            TestCaseBatch(cases=[case(["[data-testid=does-not-exist]"])]), page
        )
        assert len(kept) == 1
        assert kept[0].needs_review
        assert report.repairable

    def test_empty_steps_dropped(self):
        page = page_with(["[data-testid=a]"])
        empty = case(["[data-testid=a]"], steps=0)
        kept, report = Validator().check_page_batch(TestCaseBatch(cases=[empty]), page)
        assert kept == []
        assert report.dropped == 1

    def test_step_numbers_renumbered(self):
        page = page_with(["[data-testid=a]"])
        broken = case(["[data-testid=a]"])
        broken.steps[0].step_number = 7
        kept, _ = Validator().check_page_batch(TestCaseBatch(cases=[broken]), page)
        assert [s.step_number for s in kept[0].steps] == [1, 2]


class TestFinalize:
    def test_ids_unique_and_sequential(self):
        v = Validator()
        cases = [case(["a"]) for _ in range(3)]
        finalized, _ = v.finalize(cases)
        assert [c.test_id for c in finalized] == ["TC_001", "TC_002", "TC_003"]

    def test_low_coverage_warns(self):
        _, warnings = Validator().finalize([case(["a"])])
        assert any("categories" in w for w in warnings)


class TestStubAdapter:
    def test_produces_multiple_categories(self):
        adapter = StubAdapter(LLMConfig(provider="stub"))
        batch = adapter.generate("INTERACTIVE ELEMENTS:\n  button [data-testid=a]\nFORMS:\n", 10)
        categories = {c.category for c in batch.cases}
        assert Category.HAPPY_PATH in categories
        assert Category.UI_UX in categories
        assert len(categories) >= 3


class TestGraph:
    def _graph(self) -> GraphBuilder:
        g = GraphBuilder("https://app.test")
        a = g.add_state(page_with(["[data-testid=a]"]), is_entry=True)
        second = page_with(["[data-testid=b]"])
        second.fingerprint = "fp2"
        second.url = "https://app.test/settings"
        b = g.add_state(second)
        g.add_edge(a, b, "click", "Click 'Settings'", Outcome.NAVIGATION,
                   selector="[data-testid=nav]")
        return g

    def test_revisiting_a_state_does_not_duplicate_nodes(self):
        g = self._graph()
        g.add_state(page_with(["[data-testid=a]"]))
        assert len(g.graph.nodes) == 2
        assert g.graph.nodes[0].visit_count == 2

    def test_duplicate_edges_collapse(self):
        g = self._graph()
        a, b = g.graph.nodes
        g.add_edge(a, b, "click", "Click 'Settings'", Outcome.NAVIGATION,
                   selector="[data-testid=nav]")
        assert len(g.graph.edges) == 1

    def test_shortest_paths_from_entry(self):
        g = self._graph()
        paths = g.shortest_paths()
        assert paths["N001"] == []
        assert len(paths["N002"]) == 1
        assert paths["N002"][0].selector == "[data-testid=nav]"

    def test_inert_edges_are_not_traversable(self):
        """A blocked mutation records the edge but must not be a nav path."""
        g = GraphBuilder("https://app.test")
        a = g.add_state(page_with(["a"]), is_entry=True)
        p2 = page_with(["b"])
        p2.fingerprint = "fp2"
        b = g.add_state(p2)
        g.add_edge(a, b, "click", "Click 'Save'", Outcome.BLOCKED_MUTATION)
        assert "N002" not in g.shortest_paths()

    def test_mermaid_and_dot_render(self):
        g = self._graph()
        mermaid = to_mermaid(g.build())
        assert mermaid.startswith("graph LR")
        assert "N001" in mermaid and "N002" in mermaid
        assert to_dot(g.build()).startswith("digraph qagen {")


class TestRenderers:
    @pytest.fixture
    def suite(self) -> TestSuite:
        cases, _ = Validator().finalize([case(["[data-testid=a]"]), case(["[data-testid=b]"])])
        return TestSuite(target="https://app.test", cases=cases)

    def test_markdown_contains_required_format(self, suite, tmp_path):
        path = markdown.write(suite, tmp_path)
        text = path.read_text(encoding="utf-8")
        assert "TC_001" in text
        assert "**Preconditions:**" in text
        assert "| # | Action | Expected Result |" in text
        assert "**Overall Expected Result:**" in text

    def test_json_roundtrips(self, suite, tmp_path):
        path = json_out.write_suite(suite, tmp_path)
        data = json.loads(path.read_text(encoding="utf-8"))
        assert len(data["cases"]) == 2
        assert data["cases"][0]["test_id"] == "TC_001"

    def test_csv_is_one_row_per_step(self, suite, tmp_path):
        path = tabular.write_csv(suite, tmp_path)
        lines = path.read_text(encoding="utf-8-sig").strip().splitlines()
        total_steps = sum(len(c.steps) for c in suite.cases)
        assert len(lines) == total_steps + 1  # + header

    def test_csv_repeats_group_columns_only_on_first_row(self, suite, tmp_path):
        rows = tabular.rows(suite)
        assert rows[0][0] == "TC_001"
        assert rows[1][0] == ""      # continuation row

    def test_xlsx_written(self, suite, tmp_path):
        path = tabular.write_xlsx(suite, tmp_path)
        assert path.exists() and path.stat().st_size > 0
