"""Navigation graph assembly.

Nodes are distinct application states, edges are the actions that move between
them. This falls out of the crawl for almost free -- the crawler already
computes both -- and it earns its keep twice:

* preconditions can cite a **real** reachability path instead of guessing
* a path from entry to any node is a test script, since every edge already
  carries a verified locator and a concrete action
"""

from __future__ import annotations

from collections import deque

from ..models import (
    Boundary,
    NavEdge,
    NavGraph,
    NavNode,
    Outcome,
    OverlayType,
    PageModel,
    is_actionable,
)


def _action_lines(page: PageModel) -> list[str]:
    """What a tester can actually do on this state, one line each.

    Uses the same predicate as ``actionable_count`` so the list length and the
    reported number can never disagree.
    """
    lines: list[str] = []
    for el in sorted(page.elements, key=lambda e: (e.kind.value, e.name.lower())):
        if not is_actionable(el):
            continue
        state = "" if el.enabled else " (disabled)"
        target = f" -> {el.href}" if el.href else ""
        # Where it lives matters to a tester: "in the left menu" and "in the
        # content area" are different preconditions.
        where = f" ({el.location})" if el.location else ""
        frame = " [app frame]" if el.region == "shell" else ""
        lines.append(
            f"{el.kind.value}: {el.name or '(unnamed)'} [{el.selector}]{state}{where}{frame}{target}"
        )
    for form in page.forms:
        fields = ", ".join(f.name or f.label or "?" for f in form.fields)
        lines.append(
            f"form ({form.origin}): submit={form.submit_label or '?'} "
            f"[{form.submit_selector or form.selector}] fields=({fields})"
        )
    return lines


class GraphBuilder:
    def __init__(self, target: str) -> None:
        self.graph = NavGraph(target=target)
        self._by_fingerprint: dict[str, NavNode] = {}
        self._node_seq = 0
        self._edge_seq = 0

    # -- nodes ------------------------------------------------------------
    def add_state(self, page: PageModel, is_entry: bool = False) -> NavNode:
        existing = self._by_fingerprint.get(page.fingerprint)
        if existing is not None:
            existing.visit_count += 1
            # A later visit may have captured artifacts the first one missed.
            existing.screenshot = existing.screenshot or page.screenshot_path
            existing.html = existing.html or page.html_path
            return existing

        self._node_seq += 1
        node = NavNode(
            id=f"N{self._node_seq:03d}",
            fingerprint=page.fingerprint,
            url=page.url,
            normalized_url=page.normalized_url,
            title=page.title or page.normalized_url,
            depth=page.depth,
            node_type=self._node_type(page),
            element_count=len(page.elements),
            actionable_count=page.actionable_count,
            main_actionable_count=page.main_actionable_count,
            dom_nodes=page.dom_nodes,
            form_ids=[f.form_id for f in page.forms],
            is_entry=is_entry,
            screenshot=page.screenshot_path,
            html=page.html_path,
            actions=_action_lines(page),
        )
        self._by_fingerprint[page.fingerprint] = node
        self.graph.nodes.append(node)
        if is_entry and not self.graph.entry_node:
            self.graph.entry_node = node.id
        return node

    def add_boundary(self, url: str, origin: str, reason: str, triggered_by: str | None) -> NavNode:
        key = f"boundary::{origin}"
        existing = self._by_fingerprint.get(key)
        if existing is not None:
            existing.visit_count += 1
            return existing

        self._node_seq += 1
        node = NavNode(
            id=f"N{self._node_seq:03d}",
            fingerprint=key,
            url=url,
            normalized_url=origin,
            title=origin,
            depth=0,
            node_type="external" if reason == "different origin" else "boundary",
        )
        self._by_fingerprint[key] = node
        self.graph.nodes.append(node)
        self.graph.boundaries.append(
            Boundary(origin=origin, url=url, reason=reason, triggered_by=triggered_by)
        )
        return node

    def node_for(self, fingerprint: str) -> NavNode | None:
        return self._by_fingerprint.get(fingerprint)

    def _node_type(self, page: PageModel) -> str:
        for overlay in page.overlays:
            if overlay.transient or overlay.overlay_type is OverlayType.CONSENT:
                continue
            if overlay.overlay_type is OverlayType.MODAL:
                return "modal"
            if overlay.overlay_type is OverlayType.DRAWER:
                return "drawer"
            if overlay.overlay_type is OverlayType.DROPDOWN:
                return "dropdown"
        return "page"

    # -- edges ------------------------------------------------------------
    def add_edge(
        self,
        source: NavNode,
        target: NavNode,
        action: str,
        label: str,
        outcome: Outcome,
        selector: str = "",
        role: str = "",
        name: str = "",
        input_value: str | None = None,
        annotations: list[str] | None = None,
        reversible_by: str = "goto",
    ) -> NavEdge:
        # Collapse duplicate transitions rather than accumulating parallel edges.
        for existing in self.graph.edges:
            if (
                existing.source == source.id
                and existing.target == target.id
                and existing.selector == selector
                and existing.action == action
            ):
                for note in annotations or []:
                    if note not in existing.annotations:
                        existing.annotations.append(note)
                return existing

        self._edge_seq += 1
        edge = NavEdge(
            id=f"E{self._edge_seq:03d}",
            source=source.id,
            target=target.id,
            action=action,  # type: ignore[arg-type]
            label=label,
            selector=selector,
            element_role=role,
            element_name=name,
            input_value=input_value,
            outcome=outcome,
            annotations=annotations or [],
            reversible_by=reversible_by,  # type: ignore[arg-type]
        )
        self.graph.edges.append(edge)
        return edge

    def mark_unexplored(self, fingerprints: list[str]) -> None:
        self.graph.unexplored = fingerprints

    # -- reachability -----------------------------------------------------
    def shortest_paths(self) -> dict[str, list[NavEdge]]:
        """BFS from the entry node to every reachable node.

        This is what turns "User is on the profile page" from a guess into a
        stated navigation path -- and it is the direct input to code generation
        later, since each edge already carries a verified locator.
        """
        if not self.graph.entry_node:
            return {}

        adjacency: dict[str, list[NavEdge]] = {}
        for edge in self.graph.edges:
            if edge.outcome in {Outcome.NO_CHANGE, Outcome.BLOCKED_MUTATION, Outcome.ERROR}:
                continue  # not a usable traversal
            adjacency.setdefault(edge.source, []).append(edge)

        paths: dict[str, list[NavEdge]] = {self.graph.entry_node: []}
        queue = deque([self.graph.entry_node])
        while queue:
            current = queue.popleft()
            for edge in adjacency.get(current, []):
                if edge.target in paths:
                    continue
                paths[edge.target] = paths[current] + [edge]
                queue.append(edge.target)
        return paths

    def build(self) -> NavGraph:
        return self.graph
