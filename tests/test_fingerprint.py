"""Unit tests for the loop-prevention core. No browser required."""

from __future__ import annotations

from qagen.browser.fingerprint import (
    compute_fingerprint,
    interactive_signature,
    looks_like_id,
    normalize_url,
)
from qagen.models import Confidence, Element, ElementKind, OverlaySpec, OverlayType


def el(name: str, role: str = "button", enabled: bool = True, visible: bool = True) -> Element:
    return Element(
        ref="E1", kind=ElementKind.GENERIC_BUTTON, role=role, name=name,
        tag="button", selector=f"[data-testid={name}]", selector_strategy="data-testid",
        confidence=Confidence.CERTAIN, enabled=enabled, visible=visible,
    )


class TestLooksLikeId:
    def test_numeric(self):
        assert looks_like_id("42")

    def test_uuid(self):
        assert looks_like_id("3f2504e0-4f89-11d3-9a0c-0305e82c3301")

    def test_mongo_id(self):
        assert looks_like_id("507f1f77bcf86cd799439011")

    def test_route_name_is_not_an_id(self):
        assert not looks_like_id("settings")
        assert not looks_like_id("billing")


class TestNormalizeUrl:
    def test_templated_routes_collapse(self):
        """The rule that stops /product/1..9000 becoming 9000 states."""
        a = normalize_url("https://x.test/product/1")
        b = normalize_url("https://x.test/product/9000")
        assert a == b == "https://x.test/product/{id}"

    def test_id_collapse_exception(self):
        """Sites with meaningful numeric routes need an escape hatch."""
        plain = normalize_url("https://x.test/year/2024")
        exempt = normalize_url("https://x.test/year/2024", ["year/*"])
        assert plain == "https://x.test/year/{id}"
        assert exempt == "https://x.test/year/2024"

    def test_tracking_params_dropped(self):
        clean = normalize_url("https://x.test/a?utm_source=t&gclid=9")
        assert clean == "https://x.test/a"

    def test_params_sorted(self):
        assert normalize_url("https://x.test/a?b=2&a=1") == normalize_url(
            "https://x.test/a?a=1&b=2"
        )

    def test_plain_anchor_dropped_hash_route_kept(self):
        assert normalize_url("https://x.test/a#section") == "https://x.test/a"
        assert normalize_url("https://x.test/a#/settings").endswith("#/settings")

    def test_default_port_and_trailing_slash(self):
        assert normalize_url("https://X.TEST:443/a/") == normalize_url("https://x.test/a")


class TestInteractiveSignature:
    def test_order_independent(self):
        assert interactive_signature([el("Save"), el("Cancel")]) == interactive_signature(
            [el("Cancel"), el("Save")]
        )

    def test_invisible_elements_excluded(self):
        assert interactive_signature([el("Save")]) == interactive_signature(
            [el("Save"), el("Hidden", visible=False)]
        )

    def test_enabled_state_matters(self):
        assert interactive_signature([el("Save")]) != interactive_signature(
            [el("Save", enabled=False)]
        )

    def test_transient_overlays_excluded(self):
        """A toast that auto-dismisses must not make the page a new state."""
        base = interactive_signature([el("Save")])
        toast = interactive_signature(
            [el("Save")], [OverlaySpec(overlay_type=OverlayType.TOAST, label="Saved")]
        )
        assert base == toast

    def test_persistent_overlay_changes_signature(self):
        base = interactive_signature([el("Save")])
        modal = interactive_signature(
            [el("Save")], [OverlaySpec(overlay_type=OverlayType.MODAL, label="Edit")]
        )
        assert base != modal


class TestCompositeFingerprint:
    def test_same_url_different_dom_differs(self):
        """The modal case: URL unchanged, DOM changed -> must be explored."""
        before = compute_fingerprint("https://x.test/dash", [el("Edit")])
        after = compute_fingerprint("https://x.test/dash", [el("Edit"), el("Save")])
        assert before != after

    def test_different_url_same_dom_matches(self):
        """The template case: 50 URLs, one state."""
        a = compute_fingerprint("https://x.test/item/1", [el("Fav")])
        b = compute_fingerprint("https://x.test/item/2", [el("Fav")])
        assert a == b

    def test_self_referential_navigation_matches(self):
        """Clicking 'Home' while on Home must not re-enqueue."""
        page = [el("Home"), el("Settings")]
        assert compute_fingerprint("https://x.test/", page) == compute_fingerprint(
            "https://x.test/", page
        )
