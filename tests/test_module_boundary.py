"""GraphBuilder.add_module_boundary -- cross-module clicks, captured once.

When a module-restricted crawl clicks something that leads outside its
module, the destination is captured once (a real screenshot) and marked as a
boundary, not explored further. Unlike add_boundary (used for genuine
external links), this is keyed by the destination's own URL, not by origin --
Content and Playlist must get their own markers, not collapse into one shared
"left the module" node with no picture at all.
"""

from __future__ import annotations

from qagen.graph.builder import GraphBuilder
from qagen.models import PageModel


def _page(url: str, elements=None) -> PageModel:
    return PageModel(url=url, normalized_url=url, title="t", elements=elements or [])


class TestModuleBoundary:
    def test_creates_a_boundary_node(self):
        g = GraphBuilder(target="https://x.test/")
        node = g.add_module_boundary(
            _page("https://x.test/content"), "not in include_paths", "Click 'Content'"
        )
        assert node.node_type == "boundary"
        assert node.normalized_url == "https://x.test/content"

    def test_two_different_destinations_get_two_nodes(self):
        """The bug this fixes: add_boundary keys by origin, so every
        out-of-module destination on the same site collapsed into one shared
        marker. Content and Playlist must be distinct."""
        g = GraphBuilder(target="https://x.test/")
        a = g.add_module_boundary(_page("https://x.test/content"), "r", None)
        b = g.add_module_boundary(_page("https://x.test/playlist"), "r", None)
        assert a.id != b.id
        assert a.normalized_url != b.normalized_url

    def test_the_same_destination_reached_twice_reuses_the_node(self):
        g = GraphBuilder(target="https://x.test/")
        a = g.add_module_boundary(_page("https://x.test/content"), "r", None)
        b = g.add_module_boundary(_page("https://x.test/content"), "r", None)
        assert a.id == b.id
        assert b.visit_count == 2

    def test_captures_the_real_element_count(self):
        """The point of this over a plain boundary marker: real data, not a
        blank stand-in."""
        from qagen.models import Confidence, Element, ElementKind

        els = [
            Element(
                ref="E1", kind=ElementKind.GENERIC_BUTTON, role="button", name="x",
                tag="button", selector="#x", selector_strategy="id",
                confidence=Confidence.HIGH,
            )
        ]
        g = GraphBuilder(target="https://x.test/")
        node = g.add_module_boundary(_page("https://x.test/content", els), "r", None)
        assert node.element_count == 1

    def test_records_a_boundary_entry(self):
        g = GraphBuilder(target="https://x.test/")
        g.add_module_boundary(_page("https://x.test/content"), "not in include_paths", "Click 'X'")
        built = g.build()
        assert any(b.url == "https://x.test/content" for b in built.boundaries)

    def test_does_not_collide_with_a_real_external_boundary(self):
        """A genuine cross-origin link (add_boundary) and a same-origin
        module boundary must never be confused with each other."""
        g = GraphBuilder(target="https://x.test/")
        external = g.add_boundary("https://other.test/", "other.test", "different origin", None)
        internal = g.add_module_boundary(
            _page("https://x.test/content"), "not in include_paths", None
        )
        assert external.id != internal.id
        assert external.node_type == "external"
        assert internal.node_type == "boundary"
