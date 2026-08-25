"""Telling the application shell apart from the page content.

Every CMS-shaped app is built the same way: a header and a left menu that never
change, and a main area that is the actual product. Samsung VXT is a textbook
case -- clicking "Content" in the left menu keeps the menu exactly where it is
and swaps only the region to its right.

A crawler that does not know this wastes most of its budget. On one real run of
this app, the eleven-item Settings menu was re-extracted on 41 of 63 states, and
`/settings` consumed 43 of them while `/screen`, `/schedule` and `/channel` were
never reached at all.

Two mechanisms, in priority order:

1. **Declared** -- ``crawl.shell_selectors`` in the config. Instant, exact, and
   the right answer when you already know the app.
2. **Observed** -- an element identity that turns up on several *different*
   URLs is part of the frame by definition. Needs no configuration and works on
   an app nobody has tuned, at the cost of needing a few states first.

Deliberately advisory: nothing here removes an element or changes a
fingerprint. It reorders the action plan and labels the output, so a wrong
guess costs ordering, never coverage.
"""

from __future__ import annotations

from collections import defaultdict

from ..models import Element, PageModel


class ShellDetector:
    def __init__(self, declared: list[str] | None = None, min_urls: int = 3) -> None:
        #: Substrings matched against an element's selector. A prefix of the
        #: real selector is enough -- "#navbar_menuList" marks the container and
        #: anything whose selector is built from it.
        self.declared = [s for s in (declared or []) if s]
        self.min_urls = max(min_urls, 2)
        #: element identity -> the distinct normalised URLs it was seen on.
        self._seen_on: dict[str, set[str]] = defaultdict(set)

    # -- learning ---------------------------------------------------------
    def observe(self, page: PageModel) -> None:
        for el in page.elements:
            self._seen_on[el.identity()].add(page.normalized_url)

    # -- classifying ------------------------------------------------------
    def is_shell(self, el: Element) -> bool:
        selector = el.selector or ""
        for marker in self.declared:
            if marker in selector:
                return True
        return len(self._seen_on.get(el.identity(), ())) >= self.min_urls

    def label(self, page: PageModel) -> None:
        """Tag every element on a page. Call after ``observe``."""
        for el in page.elements:
            el.region = "shell" if self.is_shell(el) else "main"

    # -- reporting --------------------------------------------------------
    def summary(self) -> dict[str, int]:
        known = sum(1 for urls in self._seen_on.values() if len(urls) >= self.min_urls)
        return {"identities_tracked": len(self._seen_on), "shell_identities": known}
