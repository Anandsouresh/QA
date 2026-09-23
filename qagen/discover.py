"""Shallow module probe.

Answers one question before a real crawl starts: what modules does this app
have, and roughly how big is each one? A module is the first path segment,
which is the same grouping ``Crawler._section_of`` already uses internally for
per-section budgets.

This is deliberately not a crawl. It loads the entry page, reads the links and
route-bearing attributes that are already in the DOM, and stops. Thirty to
sixty seconds, no clicks, no state machine -- so the configuration screen can
offer real modules instead of asking the user to guess them.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlsplit

from .browser.fingerprint import normalize_url
from .browser.session import Session
from .config import RunConfig

log = logging.getLogger("qagen.discover")

#: Segments that are never a product module.
IGNORED = {
    "login", "signin", "sign-in", "logout", "signout", "auth", "oauth",
    "static", "assets", "api", "_next", "favicon.ico", "robots.txt",
}


@dataclass
class Module:
    name: str
    paths: list[str] = field(default_factory=list)
    links: int = 0

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "paths": sorted(self.paths)[:6],
            "path_count": len(self.paths),
            "links": self.links,
        }


def _segment(url: str, origin: str) -> tuple[str, str] | None:
    """(module, normalised path) for a same-origin URL, or None."""
    parts = urlsplit(url)
    if f"{parts.scheme}://{parts.netloc}" != origin:
        return None
    path = parts.path or "/"
    segments = [s for s in path.split("/") if s]
    if not segments:
        return ("(home)", "/")
    head = segments[0].lower()
    if head in IGNORED or "." in head:
        return None
    return (head, path.rstrip("/") or "/")


async def discover_modules(cfg: RunConfig) -> dict:
    """Load the entry page and group everything it links to by first segment."""
    origin = "{0.scheme}://{0.netloc}".format(urlsplit(cfg.target.url))
    modules: dict[str, Module] = defaultdict(lambda: Module(name=""))
    external: set[str] = set()

    async with Session(cfg) as session:
        page = session.page
        assert page is not None

        await session.verify_auth()
        await page.wait_for_timeout(cfg.crawl.post_loader_wait_ms or 800)

        hrefs: list[str] = await page.eval_on_selector_all(
            "a[href]", "els => els.map(e => e.getAttribute('href'))"
        )
        # SPAs that route through divs still tend to carry the route on an
        # attribute, because analytics needs it too.
        routed: list[str] = await page.eval_on_selector_all(
            "[data-href],[data-route],[data-path],[data-to]",
            "els => els.map(e => e.getAttribute('data-href') || e.getAttribute('data-route')"
            " || e.getAttribute('data-path') || e.getAttribute('data-to'))",
        )
        title = await page.title()
        dom_nodes = await page.evaluate("document.getElementsByTagName('*').length")

    for raw in [h for h in (hrefs + routed) if h]:
        if raw.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        absolute = urljoin(cfg.target.url, raw)
        found = _segment(absolute, origin)
        if found is None:
            host = urlsplit(absolute).netloc
            if host and host != urlsplit(origin).netloc:
                external.add(host)
            continue
        name, path = found
        mod = modules[name]
        mod.name = name
        if path not in mod.paths:
            mod.paths.append(path)
        mod.links += 1

    ordered = sorted(modules.values(), key=lambda m: (-m.links, m.name))
    return {
        "target": cfg.target.url,
        "normalized_target": normalize_url(
            cfg.target.url, cfg.target.id_collapse_exceptions
        ),
        "title": title,
        "dom_nodes": dom_nodes,
        "modules": [m.as_dict() for m in ordered],
        "external_hosts": sorted(external)[:12],
    }


def suggest_budgets(modules: list[dict], total_states: int) -> dict[str, int]:
    """Split a state budget across modules by how much surface each one shows.

    Weighted by distinct paths rather than raw link count, because a nav bar
    repeated on every card inflates links without adding anywhere to go. Every
    module gets a floor, so a one-page module is still visited.
    """
    if not modules:
        return {}
    floor = max(4, total_states // (len(modules) * 4))
    weights = {m["name"]: max(1, m["path_count"]) for m in modules}
    total_weight = sum(weights.values())
    remaining = max(0, total_states - floor * len(modules))

    out: dict[str, int] = {}
    for name, weight in weights.items():
        out[name] = floor + int(remaining * weight / total_weight)
    return out
