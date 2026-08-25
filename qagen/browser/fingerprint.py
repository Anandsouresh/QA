"""State identity: normalize_url + interactive_signature -> fingerprint.

This module is the loop-prevention core. It is deliberately pure (no Playwright
imports) so every rule here is unit-testable without a browser.

    fingerprint = sha256( normalize_url(url) || interactive_signature(elements) )

Catches both directions of the SPA crawling problem:

* same URL, different DOM  -> different fingerprint -> modals get explored
* different URL, same DOM   -> same fingerprint      -> /product/1..9000 collapses
"""

from __future__ import annotations

import fnmatch
import hashlib
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from ..models import Element, OverlaySpec

#: Query parameters that never identify a state.
TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "utm_id", "gclid", "fbclid", "msclkid", "mc_cid", "mc_eid",
    "ref", "referrer", "_ga", "_gl", "igshid", "si", "yclid",
}

_NUMERIC = re.compile(r"^\d+$")
_UUID = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I
)
_LONG_HEX = re.compile(r"^[0-9a-f]{16,}$", re.I)
_MONGO_ID = re.compile(r"^[0-9a-f]{24}$", re.I)
#: Mixed alphanumeric slugs that are clearly generated, e.g. "a7Fk92Lm".
_OPAQUE = re.compile(r"^(?=.*\d)(?=.*[a-z])[a-z0-9_-]{12,}$", re.I)


def looks_like_id(segment: str) -> bool:
    """True when a path segment is an identifier rather than a route name."""
    if not segment:
        return False
    return bool(
        _NUMERIC.match(segment)
        or _UUID.match(segment)
        or _MONGO_ID.match(segment)
        or _LONG_HEX.match(segment)
        or _OPAQUE.match(segment)
    )


def normalize_url(url: str, id_collapse_exceptions: list[str] | None = None) -> str:
    """Collapse a URL to the state it represents.

    Lowercases scheme/host, drops tracking params, sorts the rest, strips the
    trailing slash, and replaces identifier-looking path segments with ``{id}``.

    The ``{id}`` rule is the one most likely to need per-site tuning: a site
    with meaningful numeric routes (``/year/2024``) should list a glob in
    ``target.id_collapse_exceptions`` so that segment survives intact.
    """
    exceptions = id_collapse_exceptions or []
    parts = urlsplit(url.strip())

    scheme = parts.scheme.lower()
    host = parts.hostname.lower() if parts.hostname else ""
    if parts.port and not (
        (scheme == "http" and parts.port == 80)
        or (scheme == "https" and parts.port == 443)
    ):
        host = f"{host}:{parts.port}"

    segments = [s for s in parts.path.split("/") if s]
    collapsed: list[str] = []
    for idx, seg in enumerate(segments):
        parent = segments[idx - 1] if idx else ""
        exempt = any(
            fnmatch.fnmatch(seg, pat) or fnmatch.fnmatch(f"{parent}/{seg}", pat)
            for pat in exceptions
        )
        collapsed.append("{id}" if (looks_like_id(seg) and not exempt) else seg.lower())
    path = "/" + "/".join(collapsed) if collapsed else "/"

    # Identifier-looking *query values* collapse for the same reason path
    # segments do: /item?id=1 .. /item?id=9000 are one state, not nine thousand.
    # This matters more than the path rule in practice -- query-string ids are
    # at least as common as path ids on real apps.
    kept = sorted(
        (k, "{id}" if looks_like_id(v) else v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in TRACKING_PARAMS
    )
    query = urlencode(kept)

    # A hash route (#/settings) identifies a state; a plain anchor (#section)
    # does not.
    fragment = parts.fragment if parts.fragment.startswith("/") else ""

    return urlunsplit((scheme, host, path, query, fragment))


def interactive_signature(
    elements: list[Element], overlays: list[OverlaySpec] | None = None
) -> str:
    """Hash of the visible, non-transient interactive surface.

    Text content is deliberately excluded -- a rendered timestamp or a live
    counter would otherwise make every poll a brand new state. Transient
    overlays (toast, tooltip) are excluded for the same reason.

    Pointer-cursor elements are the subtle case. Excluding them wholesale (the
    original rule) stopped one Settings page fingerprinting a dozen ways, but it
    also made every React menu invisible: on a real dashboard, clicking "+"
    revealed "Add Screen" and "New Screen Wall" and the fingerprint did not
    move, so the crawler recorded the click as inert and never saw the menu.

    The split that works is **selector stability**. A pointer-cursor element
    found by ``data-testid`` or a real ``id`` is a control the app named on
    purpose and it is there on every render; one found by css-path is a div that
    happened to look clickable this time round, and that is the set that churns.
    """
    tuples = sorted(
        {
            e.signature()
            for e in elements
            if e.visible and not e.transient and (not e.pointer_cursor or e.stable_selector)
        }
    )
    body = "|".join(f"{r}\x1f{n}\x1f{int(en)}\x1f{k}" for r, n, en, k in tuples)

    persistent = sorted(
        f"{o.overlay_type}:{(o.label or '').strip().lower()}"
        for o in (overlays or [])
        if not o.transient
    )
    if persistent:
        body += "\x1e" + "|".join(persistent)

    return hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]


def compute_fingerprint(
    url: str,
    elements: list[Element],
    overlays: list[OverlaySpec] | None = None,
    id_collapse_exceptions: list[str] | None = None,
) -> str:
    """The composite fingerprint. This is the visited-set key."""
    normalized = normalize_url(url, id_collapse_exceptions)
    signature = interactive_signature(elements, overlays)
    digest = hashlib.sha256(f"{normalized}\x00{signature}".encode("utf-8"))
    return digest.hexdigest()[:20]
