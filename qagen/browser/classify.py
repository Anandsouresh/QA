"""The classification cascade (CRAWLING_AND_EXTRACTION.md §1.2).

Playwright has no semantics -- it gives us the DOM and computed role/name, and
nothing more. Every semantic label in our output is produced here, by fourteen
ordered rules. First match wins; the rule that fired sets the confidence.

Rules 13 and 14 are where React's habits land, and they are exactly why the
network write-guard is not optional: an unlabelled ``<div onClick={deleteUser}>``
classifies as INFERRED_CLICKABLE with no destructive signal at all. Text
matching cannot catch it. Only blocking the outbound mutation can.
"""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import urljoin, urlsplit

from ..models import Confidence, Element, ElementKind

SEARCH_HINT = re.compile(r"search|query|find|filter|^q$|lookup", re.I)

TYPED_INPUT: dict[str, ElementKind] = {
    "email": ElementKind.EMAIL_INPUT,
    "password": ElementKind.PASSWORD_INPUT,
    "tel": ElementKind.TEL_INPUT,
    "url": ElementKind.URL_INPUT,
    "number": ElementKind.NUMBER_INPUT,
    "date": ElementKind.DATE_INPUT,
    "datetime-local": ElementKind.DATE_INPUT,
    "month": ElementKind.DATE_INPUT,
    "week": ElementKind.DATE_INPUT,
    "time": ElementKind.DATE_INPUT,
    "file": ElementKind.FILE_INPUT,
    "checkbox": ElementKind.CHECKBOX,
    "radio": ElementKind.RADIO,
    "range": ElementKind.RANGE,
    "color": ElementKind.COLOR,
    "text": ElementKind.TEXT_INPUT,
}

ROLE_KIND: dict[str, ElementKind] = {
    "tab": ElementKind.TAB,
    "menuitem": ElementKind.MENUITEM,
    "menuitemcheckbox": ElementKind.MENUITEM,
    "menuitemradio": ElementKind.MENUITEM,
    "option": ElementKind.OPTION,
    "switch": ElementKind.SWITCH,
    "checkbox": ElementKind.CHECKBOX,
    "radio": ElementKind.RADIO,
}

HASPOPUP_VALUES = {"dialog", "menu", "listbox", "tree", "grid", "true"}

_CONFIDENCE = {
    "certain": Confidence.CERTAIN,
    "high": Confidence.HIGH,
    "medium": Confidence.MEDIUM,
    "low": Confidence.LOW,
}


def classify(
    raw: dict[str, Any],
    page_url: str,
    same_origin: "Callable[[str], bool]",  # noqa: F821 - injected from ScopeRules
    destructive_match: "Callable[[str], str | None]",  # noqa: F821
) -> Element:
    """Run the cascade over one raw JS record and return a typed Element."""
    tag: str = raw.get("tag", "")
    role: str = raw.get("role") or ""
    name: str = raw.get("name") or ""
    itype: str | None = raw.get("input_type")
    href: str | None = raw.get("href")
    target: str | None = raw.get("target")
    haspopup: str | None = raw.get("aria_haspopup")
    expanded: str | None = raw.get("aria_expanded")

    kind = ElementKind.UNKNOWN
    confidence = Confidence.MEDIUM
    rule = 0

    # 1 -- role="search" on the node or an ancestor
    if role == "search" or raw.get("in_search_landmark"):
        if tag in {"input", "textarea"} or role in {"searchbox", "textbox", "combobox"}:
            kind, confidence, rule = ElementKind.SEARCH, Confidence.CERTAIN, 1

    # 2 -- input[type=search]
    if kind is ElementKind.UNKNOWN and itype == "search":
        kind, confidence, rule = ElementKind.SEARCH, Confidence.CERTAIN, 2

    # 3 -- typed inputs
    if kind is ElementKind.UNKNOWN and tag == "input" and itype in TYPED_INPUT:
        kind, confidence, rule = TYPED_INPUT[itype], Confidence.CERTAIN, 3
    if kind is ElementKind.UNKNOWN and tag == "textarea":
        kind, confidence, rule = ElementKind.TEXTAREA, Confidence.CERTAIN, 3

    # 4 -- selects / comboboxes
    if kind is ElementKind.UNKNOWN and (tag == "select" or role in {"combobox", "listbox"}):
        kind, confidence, rule = ElementKind.SELECT, Confidence.CERTAIN, 4

    # 5 / 6 -- links, split by origin
    if kind is ElementKind.UNKNOWN and tag == "a" and href:
        absolute = _absolutize(href, page_url)
        external = bool(target == "_blank") or (
            absolute is not None and not same_origin(absolute)
        )
        if absolute is None:
            kind, confidence, rule = ElementKind.INFERRED_CLICKABLE, Confidence.LOW, 6
        else:
            kind = ElementKind.EXTERNAL_LINK if external else ElementKind.NAV_LINK
            confidence, rule = Confidence.CERTAIN, 6 if external else 5
            href = absolute

    # 7 -- submit controls
    if kind is ElementKind.UNKNOWN and (
        itype in {"submit", "image"} or (raw.get("form_ref") and itype == "submit")
    ):
        kind, confidence, rule = ElementKind.SUBMIT, Confidence.CERTAIN, 7

    # 8 -- aria-haspopup
    if kind is ElementKind.UNKNOWN and haspopup and haspopup.lower() in HASPOPUP_VALUES:
        kind, confidence, rule = ElementKind.OVERLAY_TRIGGER, Confidence.HIGH, 8

    # 9 -- aria-expanded
    if kind is ElementKind.UNKNOWN and expanded is not None:
        kind, confidence, rule = ElementKind.DISCLOSURE, Confidence.HIGH, 9

    # 10 -- explicit widget roles
    if kind is ElementKind.UNKNOWN and role in ROLE_KIND:
        kind, confidence, rule = ROLE_KIND[role], Confidence.HIGH, 10

    # 11 -- search by naming convention
    if kind is ElementKind.UNKNOWN and tag in {"input", "textarea"}:
        blob = " ".join(filter(None, [name, raw.get("autocomplete") or ""]))
        if SEARCH_HINT.search(blob):
            kind, confidence, rule = ElementKind.SEARCH, Confidence.MEDIUM, 11

    # 12 -- destructive vocabulary
    if kind is ElementKind.UNKNOWN and destructive_match(name):
        kind, confidence, rule = ElementKind.DESTRUCTIVE, Confidence.MEDIUM, 12

    # 12b -- pointer cursor on a non-semantic tag. React's actual habit: the
    # onClick lives in the framework, not the DOM, so this is all we can see.
    if kind is ElementKind.UNKNOWN and raw.get("pointer_cursor"):
        kind, confidence, rule = ElementKind.INFERRED_CLICKABLE, Confidence.LOW, 14

    # 13 -- plain button
    if kind is ElementKind.UNKNOWN and (tag == "button" or role == "button"):
        kind, confidence, rule = ElementKind.GENERIC_BUTTON, Confidence.MEDIUM, 13

    # 14 -- non-semantic tag wired with a handler. React's favourite.
    if kind is ElementKind.UNKNOWN:
        kind, confidence, rule = ElementKind.INFERRED_CLICKABLE, Confidence.LOW, 14

    # A destructive label always wins over a generic classification, whatever
    # rule assigned it -- "Delete" on a button must not read as GENERIC_BUTTON.
    if kind in {ElementKind.GENERIC_BUTTON, ElementKind.INFERRED_CLICKABLE, ElementKind.SUBMIT}:
        if destructive_match(name):
            kind, rule = ElementKind.DESTRUCTIVE, 12

    selector_conf = _CONFIDENCE.get(raw.get("selector_confidence", "medium"), Confidence.MEDIUM)
    # Overall confidence is the weaker of "what is it" and "can we find it again".
    final_conf = min(confidence, selector_conf, key=_confidence_rank)

    return Element(
        ref=raw.get("ref", ""),
        kind=kind,
        role=role or tag,
        name=name,
        tag=tag,
        selector=raw.get("selector", ""),
        selector_strategy=raw.get("selector_strategy", ""),
        confidence=final_conf,
        enabled=bool(raw.get("enabled", True)),
        visible=bool(raw.get("visible", True)),
        href=href,
        target=target,
        input_type=itype,
        aria_haspopup=haspopup,
        aria_expanded=expanded,
        form_ref=raw.get("form_ref"),
        landmark=raw.get("landmark"),
        x=int(raw.get("x") or 0),
        y=int(raw.get("y") or 0),
        w=int(raw.get("w") or 0),
        h=int(raw.get("h") or 0),
        transient=bool(raw.get("transient", False)),
        pointer_cursor=bool(raw.get("pointer_cursor", False)),
        classification_rule=rule,
    )


def _confidence_rank(c: Confidence) -> int:
    return {
        Confidence.LOW: 0,
        Confidence.MEDIUM: 1,
        Confidence.HIGH: 2,
        Confidence.CERTAIN: 3,
    }[c]


def _absolutize(href: str, base: str) -> str | None:
    href = href.strip()
    if not href or href.startswith(("javascript:", "mailto:", "tel:", "#")):
        return None
    try:
        absolute = urljoin(base, href)
    except ValueError:
        return None
    return absolute if urlsplit(absolute).scheme.startswith("http") else None
