"""Semantic validation -- what the schema cannot guarantee.

Structured outputs already guarantee shape. This file enforces meaning: IDs
unique and sequential, steps contiguous from 1, and -- the important one --
**selector grounding**: every selector a test case cites must exist in the
source PageModel.

Grounding is what catches a plausible-looking but fabricated test case. A case
that fails it is flagged rather than dropped: a flagged case a reviewer can
reject is more useful than a silently missing one.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from ..models import Category, PageModel, TestCase, TestCaseBatch

log = logging.getLogger("qagen.validator")


@dataclass
class ValidationReport:
    violations: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    dropped: int = 0
    flagged: int = 0

    @property
    def repairable(self) -> bool:
        return bool(self.violations)


class Validator:
    def __init__(self) -> None:
        self._counter = 0

    def check_page_batch(
        self, batch: TestCaseBatch, page: PageModel
    ) -> tuple[list[TestCase], ValidationReport]:
        """Validate one page's batch. Returns surviving cases plus a report."""
        report = ValidationReport()
        grounded = page.selector_set()
        kept: list[TestCase] = []

        for case in batch.cases:
            problems: list[str] = []

            if not case.steps:
                report.violations.append("a test case had no steps")
                report.dropped += 1
                continue

            for index, step in enumerate(case.steps, start=1):
                if step.step_number != index:
                    problems.append(
                        f"step numbering was not contiguous (saw {step.step_number}, expected {index})"
                    )
                    step.step_number = index
                if not step.action.strip():
                    problems.append("a step had an empty action")
                if not step.expected_result.strip():
                    problems.append("a step had an empty expected result")

            if not case.overall_expected_result.strip():
                problems.append("overall_expected_result was empty")

            if not case.preconditions:
                report.warnings.append(
                    f"{case.category.value} case has no preconditions"
                )

            # -- selector grounding: the anti-hallucination check ----------
            ungrounded = [s for s in case.source_selectors if s and s not in grounded]
            if ungrounded:
                problems.append(
                    "these selectors are not present on the page: "
                    + ", ".join(sorted(set(ungrounded))[:5])
                )

            if problems:
                report.violations.extend(problems)
                case.needs_review = True
                case.review_notes.extend(problems)
                report.flagged += 1

            case.source_url = case.source_url or page.url
            kept.append(case)

        if kept and not any(c.category is Category.UI_UX for c in kept):
            report.warnings.append("no UI/UX case generated for this page")

        return kept, report

    def finalize(self, cases: list[TestCase]) -> tuple[list[TestCase], list[str]]:
        """Assign globally unique sequential IDs and check suite-level coverage."""
        warnings: list[str] = []
        for case in cases:
            self._counter += 1
            case.test_id = f"TC_{self._counter:03d}"

        categories = {c.category for c in cases}
        if len(categories) < 3:
            warnings.append(
                f"suite covers only {len(categories)} of 5 categories "
                f"({', '.join(sorted(c.value for c in categories)) or 'none'})"
            )

        flagged = sum(1 for c in cases if c.needs_review)
        if flagged:
            warnings.append(f"{flagged} case(s) flagged needs_review")

        return cases, warnings
