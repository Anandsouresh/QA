"""Deterministic offline adapter.

Exists so the validator and all four renderers can be exercised with zero API
calls and zero flake -- the fast test suite runs entirely on this. It derives
cases mechanically from the inventory rather than calling a model, so the cases
are shallow but structurally real.
"""

from __future__ import annotations

from ..config import LLMConfig
from ..models import Category, Step, TestCase, TestCaseBatch

class StubAdapter:
    name = "stub"

    def __init__(self, cfg: LLMConfig) -> None:
        self.cfg = cfg
        self._current_url = ""
        self._selectors: list[str] = []
        self._calls = 0

    def set_page_context(self, url: str, selectors: list[str]) -> None:
        self._current_url = url
        # Use the page's real selectors rather than scraping them back out of
        # the summary text: role-based locators contain nested brackets, so
        # any regex over the rendered summary mangles them and every case then
        # fails grounding.
        self._selectors = list(selectors)

    def usage(self) -> dict[str, int]:
        return {"calls": self._calls, "input_tokens": 0, "output_tokens": 0}

    def repair(self, summary: str, violations: list[str], max_cases: int) -> TestCaseBatch:
        return self.generate(summary, max_cases)

    def generate(self, summary: str, max_cases: int) -> TestCaseBatch:
        self._calls += 1
        selectors = self._selectors[:6]
        primary = selectors[0] if selectors else "body"
        has_form = "FORMS:" in summary
        cases: list[TestCase] = []

        cases.append(
            TestCase(
                test_id="TC_000",
                category=Category.HAPPY_PATH,
                preconditions=["The page under test is open"],
                steps=[
                    Step(
                        step_number=1,
                        action="Load the page",
                        expected_result="The page renders without console errors",
                    ),
                    Step(
                        step_number=2,
                        action=f"Interact with the primary control [{primary}]",
                        expected_result="The control responds without error",
                    ),
                ],
                overall_expected_result="The primary flow completes successfully",
                source_url=self._current_url,
                source_selectors=[primary],
            )
        )

        cases.append(
            TestCase(
                test_id="TC_000",
                category=Category.UI_UX,
                preconditions=["The page under test is open"],
                steps=[
                    Step(
                        step_number=1,
                        action="Tab through every interactive element",
                        expected_result="Focus order is logical and focus is always visible",
                    )
                ],
                overall_expected_result="The page is keyboard navigable",
                source_url=self._current_url,
                source_selectors=[primary],
            )
        )

        if has_form:
            cases.append(
                TestCase(
                    test_id="TC_000",
                    category=Category.NEGATIVE,
                    preconditions=["The page under test is open", "The form is visible"],
                    steps=[
                        Step(
                            step_number=1,
                            action="Leave every required field empty",
                            expected_result="Required-field indicators remain unsatisfied",
                        ),
                        Step(
                            step_number=2,
                            action="Attempt to submit the form",
                            expected_result="Submission is blocked and validation messages appear",
                        ),
                    ],
                    overall_expected_result="The form rejects an empty submission",
                    source_url=self._current_url,
                    source_selectors=selectors[:2] or [primary],
                )
            )

        return TestCaseBatch(cases=cases[:max_cases])
