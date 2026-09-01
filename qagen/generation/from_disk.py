"""Generate test cases from a crawl that already happened.

A crawl of this app takes hours; generation takes minutes. Tying them together
in one command means any change to the prompt, the model, or the case format
costs a full re-crawl -- so a five-hour capture could only ever be used once.

Everything generation needs is already written to disk by a crawl:
``pages/*.json`` (the page models) and ``navgraph.json`` (for reachability
paths). This module loads those back into the shapes the generator expects.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from ..browser.crawler import CrawlResult, SkipRecord
from ..graph.builder import GraphBuilder
from ..models import NavEdge, NavNode, PageModel

log = logging.getLogger("qagen.from_disk")


class LoadError(RuntimeError):
    pass


def load_crawl(run_dir: Path) -> CrawlResult:
    """Rebuild a CrawlResult from a finished run directory."""
    pages_dir = run_dir / "pages"
    graph_path = run_dir / "navgraph.json"

    if not pages_dir.is_dir():
        raise LoadError(
            f"{pages_dir} not found. Generation needs the page models, which are "
            f"written when output.save_page_models is true."
        )

    pages: list[PageModel] = []
    for path in sorted(pages_dir.glob("*.json")):
        try:
            pages.append(PageModel.model_validate(json.loads(path.read_text("utf-8"))))
        except Exception as exc:      # one bad file must not lose the run
            log.warning("skipping unreadable page model %s: %s", path.name, exc)

    if not pages:
        raise LoadError(f"no readable page models in {pages_dir}")

    builder = GraphBuilder(target=pages[0].url)
    if graph_path.is_file():
        _restore_graph(builder, json.loads(graph_path.read_text("utf-8")))
    else:
        log.warning(
            "%s not found; generating without navigation paths, so preconditions "
            "will not cite a route from the entry page",
            graph_path,
        )

    return CrawlResult(pages=pages, skips=_load_skips(run_dir), graph=builder)


def _restore_graph(builder: GraphBuilder, raw: dict) -> None:
    """Repopulate a GraphBuilder so shortest_paths() and node_for() work.

    Fingerprint is the key the generator looks nodes up by, so the
    ``_by_fingerprint`` index has to be rebuilt, not just the node list.
    """
    builder.graph.target = raw.get("target", builder.graph.target)
    builder.graph.entry_node = raw.get("entry_node")

    for node_raw in raw.get("nodes", []):
        try:
            node = NavNode.model_validate(node_raw)
        except Exception as exc:
            log.debug("skipping unreadable node: %s", exc)
            continue
        builder.graph.nodes.append(node)
        builder._by_fingerprint[node.fingerprint] = node

    for edge_raw in raw.get("edges", []):
        try:
            builder.graph.edges.append(NavEdge.model_validate(edge_raw))
        except Exception as exc:
            log.debug("skipping unreadable edge: %s", exc)


def _load_skips(run_dir: Path) -> list[SkipRecord]:
    """Elements the crawler deliberately did not click.

    These feed the "NOT EXERCISED BY THE CRAWLER" block in the prompt, which is
    what lets the model write cases for a Delete button it was never allowed to
    press. Absent on older runs, so this is best-effort.
    """
    path = run_dir / "skips.json"
    if not path.is_file():
        return []
    try:
        raw = json.loads(path.read_text("utf-8"))
    except Exception:
        return []
    return [
        SkipRecord(url=r.get("url", ""), element=r.get("element", ""), reason=r.get("reason", ""))
        for r in raw
        if isinstance(r, dict)
    ]
