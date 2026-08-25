"""Interaction policy and scope rules.

Layer 1 of the three safety layers: intent-based filtering by label and
selector. Layer 2 is the form policy (analyse, never submit). Layer 3 is the
network write-guard in session.py, which is what actually protects us when an
unlabelled ``<div onClick={deleteAccount}>`` slips past this file.
"""

from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass
from urllib.parse import urlsplit

from ..config import InteractionConfig, TargetConfig
from ..models import Element, ElementKind


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str = ""


class InteractionPolicy:
    def __init__(self, cfg: InteractionConfig) -> None:
        self.cfg = cfg
        self._deny_words = [w.lower().strip() for w in cfg.deny_text if w.strip()]
        self._consent_words = [w.lower().strip() for w in cfg.consent_vocab if w.strip()]

    # -- destructive vocabulary -------------------------------------------
    def matches_destructive_text(self, text: str) -> str | None:
        low = (text or "").lower()
        if not low.strip():
            return None
        for word in self._deny_words:
            # Word-boundary match so "resettings" does not trip on "reset",
            # but "Delete account" does trip on "delete".
            if re.search(rf"(?<![a-z]){re.escape(word)}(?![a-z])", low):
                return word
        return None

    def is_consent_text(self, text: str) -> bool:
        low = (text or "").lower().strip()
        return any(word in low for word in self._consent_words)

    # -- the gate ---------------------------------------------------------
    def evaluate(self, el: Element) -> Decision:
        if self.cfg.policy == "passive":
            return Decision(False, "passive policy: no interaction")

        # Explicit allow beats every deny rule. Per-site escape hatch.
        for pattern in self.cfg.allow_selectors:
            if _selector_matches(el.selector, pattern):
                return Decision(True, "")

        if not el.enabled:
            return Decision(False, "element disabled")
        if not el.visible:
            return Decision(False, "element not visible")

        if el.kind is ElementKind.DESTRUCTIVE:
            return Decision(False, "classified destructive")
        if el.kind is ElementKind.SUBMIT:
            return Decision(False, "form submit (forms are analysed, never submitted)")
        if el.kind is ElementKind.FILE_INPUT:
            return Decision(False, "file input (chooser dismissed, not exercised)")
        if el.kind is ElementKind.EXTERNAL_LINK:
            return Decision(False, "external origin (recorded as boundary)")

        for pattern in self.cfg.deny_selectors:
            if _selector_matches(el.selector, pattern):
                return Decision(False, f"deny selector: {pattern}")

        word = self.matches_destructive_text(f"{el.name}")
        if word:
            return Decision(False, f"destructive vocabulary: '{word}'")

        return Decision(True, "")


_ATTR_PATTERN = re.compile(
    r"""^\[\s*
        (?P<attr>[\w:.-]+)\s*
        (?:(?P<op>[~^$*|]?=)\s*['"]?(?P<value>[^'"\]]*)['"]?\s*(?P<flag>[iIsS])?\s*)?
    \]$""",
    re.X,
)


def _selector_matches(selector: str, pattern: str) -> bool:
    """Match a synthesised selector against a configured deny/allow pattern.

    We compare selector strings rather than re-querying the DOM, which keeps
    policy evaluation pure and fast. Attribute patterns are parsed properly --
    matching on the attribute name alone would make ``[data-testid*='delete']``
    deny every element that has a ``data-testid`` at all.

    The cost of the string approach is that it only catches patterns that
    survived selector synthesis: an element denied by ``[data-destructive]``
    whose selector came out as ``[data-testid=...]`` slips through here. The
    network write-guard is what covers that gap.
    """
    if not selector or not pattern:
        return False
    if selector == pattern:
        return True

    match = _ATTR_PATTERN.match(pattern.strip())
    if match:
        attr, op, value, flag = (
            match.group("attr"), match.group("op"),
            match.group("value"), match.group("flag"),
        )
        if attr not in selector:
            return False
        if op is None:          # presence test, e.g. [data-destructive]
            return True
        if not value:
            return True
        haystack = selector.lower() if flag and flag.lower() == "i" else selector
        needle = value.lower() if flag and flag.lower() == "i" else value
        if op == "=":
            return f"={needle}" in haystack or f'="{needle}"' in haystack
        return needle in haystack

    if pattern.startswith((".", "#")):
        return pattern[1:] in selector
    return pattern in selector


class ScopeRules:
    """Origin / include / exclude / depth gating."""

    def __init__(self, cfg: TargetConfig) -> None:
        self.cfg = cfg
        self.root = urlsplit(cfg.url)

    def same_origin(self, url: str) -> bool:
        parts = urlsplit(url)
        if not parts.scheme.startswith("http"):
            return False
        return (parts.scheme, parts.hostname, parts.port) == (
            self.root.scheme,
            self.root.hostname,
            self.root.port,
        )

    def in_scope(self, url: str) -> Decision:
        parts = urlsplit(url)
        if not parts.scheme.startswith("http"):
            return Decision(False, f"non-http scheme: {parts.scheme or 'none'}")
        if self.cfg.same_origin_only and not self.same_origin(url):
            return Decision(False, f"different origin: {parts.hostname}")

        path = parts.path or "/"
        for pattern in self.cfg.exclude_paths:
            if fnmatch.fnmatch(path, pattern):
                return Decision(False, f"excluded path: {pattern}")

        if self.cfg.include_paths:
            if not any(fnmatch.fnmatch(path, p) for p in self.cfg.include_paths):
                return Decision(False, "not in include_paths")

        return Decision(True, "")
