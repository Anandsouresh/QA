"""Graph renderers: Mermaid, Graphviz DOT, and the precomputed path file.

Mermaid is the one that matters day to day -- it renders directly in GitHub and
VS Code with no tooling, which makes the graph a review artifact rather than
just a data file. Solid edges are transitions we actually performed; dashed
edges are blocked or boundary transitions we recorded but did not traverse.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..models import NavEdge, NavGraph, Outcome

_DASHED = {Outcome.BLOCKED_MUTATION, Outcome.ERROR, Outcome.DOWNLOAD, Outcome.NEW_TAB}

_SHAPES = {
    "page": ("[\"", "\"]"),
    "modal": ("{{\"", "\"}}"),
    "drawer": ("{{\"", "\"}}"),
    "dropdown": ("(\"", "\")"),
    "panel": ("(\"", "\")"),
    "boundary": ("[/\"", "\"/]"),
    "external": ("[/\"", "\"/]"),
}

_ANNOTATION_MARK = {
    "mutating": "!",
    "confirmation_required": "?",
    "upload": "^",
    "error": "x",
    "denied": "-",
}


def _escape(text: str) -> str:
    return (
        (text or "")
        .replace('"', "'")
        .replace("[", "(")
        .replace("]", ")")
        .replace("{", "(")
        .replace("}", ")")
        .replace("|", "/")
        .strip()[:60]
    )


def _edge_caption(edge: NavEdge) -> str:
    marks = "".join(_ANNOTATION_MARK.get(a, "") for a in edge.annotations)
    caption = _escape(edge.label)
    return f"{caption} {marks}".strip()


def to_mermaid(graph: NavGraph) -> str:
    lines = ["graph LR"]
    for node in graph.nodes:
        open_tag, close_tag = _SHAPES.get(node.node_type, _SHAPES["page"])
        title = _escape(node.title or node.normalized_url)
        sub = _escape(node.normalized_url)
        label = f"{title}<br/>{sub}" if sub and sub != title else title
        marker = "*" if node.is_entry else ""
        lines.append(f"  {node.id}{open_tag}{marker}{label}{close_tag}")

    lines.append("")
    for edge in graph.edges:
        arrow = "-.->" if edge.outcome in _DASHED else "-->"
        lines.append(f"  {edge.source} {arrow}|\"{_edge_caption(edge)}\"| {edge.target}")

    lines += [
        "",
        "  %% legend: * entry  ! mutating  ? confirmation  ^ upload  x error",
        "  %% dashed edges were recorded but not traversed",
    ]
    return "\n".join(lines) + "\n"


def to_dot(graph: NavGraph) -> str:
    lines = [
        "digraph qagen {",
        "  rankdir=LR;",
        '  node [shape=box, style=rounded, fontname="Helvetica", fontsize=10];',
        '  edge [fontname="Helvetica", fontsize=9];',
    ]
    for node in graph.nodes:
        shape = {
            "modal": "component", "drawer": "component", "dropdown": "ellipse",
            "boundary": "note", "external": "note",
        }.get(node.node_type, "box")
        peripheries = 2 if node.is_entry else 1
        label = _escape(f"{node.title}\\n{node.normalized_url}")
        lines.append(
            f'  {node.id} [label="{label}", shape={shape}, peripheries={peripheries}];'
        )
    for edge in graph.edges:
        style = "dashed" if edge.outcome in _DASHED else "solid"
        lines.append(
            f'  {edge.source} -> {edge.target} '
            f'[label="{_escape(_edge_caption(edge))}", style={style}];'
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def paths_document(graph: NavGraph, paths: dict[str, list[NavEdge]]) -> dict:
    by_id = {n.id: n for n in graph.nodes}
    out = []
    for node_id, edges in sorted(paths.items()):
        node = by_id.get(node_id)
        if node is None:
            continue
        out.append(
            {
                "node_id": node_id,
                "url": node.url,
                "title": node.title,
                "node_type": node.node_type,
                "hops": len(edges),
                "steps": [
                    {
                        "action": e.action,
                        "label": e.label,
                        "selector": e.selector,
                        "input_value": e.input_value,
                    }
                    for e in edges
                ],
            }
        )
    return {"entry_node": graph.entry_node, "target": graph.target, "paths": out}


def states_markdown(graph: NavGraph, paths: dict[str, list[NavEdge]]) -> str:
    """Per-state report: how to reach it, what you can do on it, what we didn't.

    This is the crawl's human-readable deliverable. The graph JSON has the same
    content, but nobody reviews coverage by reading JSON.
    """
    by_id = {n.id: n for n in graph.nodes}
    lines: list[str] = [
        "# Discovered states",
        "",
        f"**Target:** {graph.target}  ",
        f"**Generated:** {graph.generated_at.isoformat(timespec='seconds')}  ",
        f"**States:** {len(graph.nodes)} · **Transitions:** {len(graph.edges)} "
        f"· **Actionable elements:** {sum(n.actionable_count for n in graph.nodes)} "
        f"of {sum(n.element_count for n in graph.nodes)} extracted",
        "",
    ]

    for node in graph.nodes:
        marker = " *(entry)*" if node.is_entry else ""
        lines += [f"## {node.id} — {node.title or node.normalized_url}{marker}", ""]
        lines += [
            f"- **URL:** {node.url}",
            f"- **Type:** {node.node_type} · **Depth:** {node.depth} "
            f"· **Actionable:** {node.actionable_count} "
            f"· **Interactive extracted:** {node.element_count} "
            f"· **DOM nodes:** {node.dom_nodes or 'n/a'} "
            f"· **Visits:** {node.visit_count}",
        ]

        route = paths.get(node.id)
        if route:
            steps = " → ".join(e.label for e in route)
            lines.append(f"- **Reached by:** {steps}")
        elif node.is_entry:
            lines.append("- **Reached by:** entry point")
        else:
            lines.append("- **Reached by:** _(no path from entry — recorded, not traversed)_")

        if node.screenshot:
            lines.append(f"- **Screenshot:** [{node.screenshot}]({node.screenshot})")
        if node.html:
            lines.append(f"- **DOM:** [{node.html}]({node.html})")
        lines.append("")

        if node.actions:
            lines += ["**Action elements**", "", "```"]
            lines += node.actions
            lines += ["```", ""]
        else:
            lines += ["_No actionable elements extracted._", ""]

        outgoing = [e for e in graph.edges if e.source == node.id]
        if outgoing:
            lines += [
                "**Transitions**", "",
                "| Action | Outcome | Goes to | Notes |",
                "|---|---|---|---|",
            ]
            for edge in outgoing:
                target = by_id.get(edge.target)
                dest = "(self)" if edge.target == node.id else (
                    f"{edge.target} {target.title[:28]}" if target else edge.target
                )
                notes = ", ".join(edge.annotations) or "—"
                lines.append(
                    f"| {edge.label} | {edge.outcome.value} | {dest} | {notes} |"
                )
            lines.append("")

        if node.not_exercised:
            lines += ["**Not exercised by the crawler**", ""]
            lines += [f"- {entry}" for entry in node.not_exercised]
            lines.append("")

    return "\n".join(lines) + "\n"


def write_all(
    graph: NavGraph,
    paths: dict[str, list[NavEdge]],
    out_dir: Path,
    manifest: dict | None = None,
) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    j = out_dir / "navgraph.json"
    j.write_text(graph.model_dump_json(indent=2), encoding="utf-8")
    written.append(j)

    m = out_dir / "navgraph.mmd"
    m.write_text(to_mermaid(graph), encoding="utf-8")
    written.append(m)

    d = out_dir / "navgraph.dot"
    d.write_text(to_dot(graph), encoding="utf-8")
    written.append(d)

    p = out_dir / "navgraph-paths.json"
    p.write_text(json.dumps(paths_document(graph, paths), indent=2), encoding="utf-8")
    written.append(p)

    st = out_dir / "states.md"
    st.write_text(states_markdown(graph, paths), encoding="utf-8")
    written.append(st)

    # Interactive, self-contained: screenshots inlined, opens straight from disk.
    from ..report.graph_html import write as write_graph_html

    written.append(write_graph_html(graph, out_dir, manifest))

    return written
