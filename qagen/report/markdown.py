"""Markdown renderer -- the human review artifact."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from ..models import NavGraph, TestSuite


def _escape_cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render(suite: TestSuite, graph: NavGraph | None = None) -> str:
    lines: list[str] = [
        "# QA Test Cases",
        "",
        f"**Target:** {suite.target}  ",
        f"**Generated:** {suite.generated_at.isoformat(timespec='seconds')}  ",
        f"**Total cases:** {len(suite.cases)}",
        "",
    ]

    by_category: dict[str, int] = defaultdict(int)
    for case in suite.cases:
        by_category[case.category.value] += 1
    if by_category:
        lines += ["## Coverage", "", "| Category | Cases |", "|---|---:|"]
        for name in sorted(by_category):
            lines.append(f"| {name} | {by_category[name]} |")
        lines.append("")

    flagged = [c for c in suite.cases if c.needs_review]
    if flagged:
        lines += [
            f"> **{len(flagged)} case(s) flagged `needs_review`.** These failed a "
            "validation rule (usually selector grounding) and survived one repair "
            "attempt. Review before use.",
            "",
        ]

    by_page: dict[str, list] = defaultdict(list)
    for case in suite.cases:
        by_page[case.source_url or "(unknown page)"].append(case)

    for url in sorted(by_page):
        lines += [f"## {url}", ""]
        for case in by_page[url]:
            lines.append(f"### {case.test_id} — {_title_of(case)}")
            lines.append("")
            lines.append(f"**Category:** {case.category.value}")
            if case.needs_review:
                lines.append("")
                lines.append(f"> ⚠ needs review: {'; '.join(case.review_notes) or 'unspecified'}")
            lines.append("")
            pre = " · ".join(case.preconditions) if case.preconditions else "None"
            lines.append(f"**Preconditions:** {pre}")
            lines.append("")
            lines.append("| # | Action | Expected Result |")
            lines.append("|---|--------|-----------------|")
            for step in case.steps:
                lines.append(
                    f"| {step.step_number} | {_escape_cell(step.action)} "
                    f"| {_escape_cell(step.expected_result)} |"
                )
            lines.append("")
            lines.append(f"**Overall Expected Result:** {case.overall_expected_result}")
            lines.append("")

    if graph and graph.nodes:
        lines += [
            "## Application map",
            "",
            f"{len(graph.nodes)} states, {len(graph.edges)} transitions.",
            "",
            "```mermaid",
        ]
        from ..graph.render import to_mermaid

        lines.append(to_mermaid(graph).rstrip())
        lines += ["```", ""]

    return "\n".join(lines)


def _title_of(case) -> str:
    for note in case.review_notes:
        if note.startswith("title: "):
            return note[len("title: "):]
    return case.category.value


def write(suite: TestSuite, out_dir: Path, graph: NavGraph | None = None) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "test-cases.md"
    path.write_text(render(suite, graph), encoding="utf-8")
    return path
