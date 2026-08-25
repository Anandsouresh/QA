"""Run lifecycle: config -> session -> auth -> crawl -> generate -> validate -> report.

Partial output always beats no output. A crawl that dies at page 18 of 25 still
writes the 17 pages it completed, and a page whose generation fails still leaves
its PageModel and its node in the graph.
"""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .browser.crawler import Crawler, CrawlResult
from .browser.session import AuthError, Session
from .config import RunConfig
from .generation.adapter import build_adapter
from .generation.summarizer import summarize
from .generation.validator import Validator
from .graph import render as graph_render
from .models import NavGraph, TestSuite
from .report import json_out, markdown, tabular

log = logging.getLogger("qagen.orchestrator")


class Orchestrator:
    def __init__(self, cfg: RunConfig, generate: bool = True) -> None:
        self.cfg = cfg
        #: When False, stop after the crawl and emit only the graph and the raw
        #: captures. No LLM adapter is constructed, so no API key is needed.
        self.generate = generate
        self.manifest: dict[str, Any] = {
            "tool": "qagen 0.1.0",
            "mode": "full" if generate else "crawl-only",
            "started_at": datetime.now(timezone.utc).isoformat(),
            "config": cfg.model_dump(mode="json"),
        }

    async def run(self) -> dict[str, Any]:
        out_dir = self.cfg.output.dir
        out_dir.mkdir(parents=True, exist_ok=True)
        started = time.monotonic()

        crawl = await self._crawl()

        if self.generate:
            suite, gen_stats = self._generate(crawl)
        else:
            suite, gen_stats = TestSuite(target=self.cfg.target.url), {"skipped": True}

        graph = crawl.graph.build() if crawl.graph else NavGraph(target=self.cfg.target.url)
        paths = crawl.graph.shortest_paths() if crawl.graph else {}

        self.manifest.update(
            {
                "finished_at": datetime.now(timezone.utc).isoformat(),
                "duration_seconds": round(time.monotonic() - started, 1),
                "crawl": {
                    "states_discovered": len(crawl.pages),
                    "graph_nodes": len(graph.nodes),
                    "graph_edges": len(graph.edges),
                    "actionable_elements": sum(n.actionable_count for n in graph.nodes),
                    "total_elements": sum(n.element_count for n in graph.nodes),
                    "boundaries": [b.model_dump(mode="json") for b in graph.boundaries],
                    "unexplored_at_stop": len(graph.unexplored),
                    "budgets": crawl.budgets.snapshot() if crawl.budgets else {},
                    "skipped_elements": [
                        {"url": s.url, "element": s.element, "reason": s.reason}
                        for s in crawl.skips
                    ],
                    "observations": [o.model_dump(mode="json") for o in crawl.observations],
                    "blocked_mutations": sorted(
                        {m for p in crawl.pages for m in p.blocked_mutations}
                    ),
                },
                "generation": gen_stats,
            }
        )

        written = self._write(suite, graph, paths, crawl)
        self.manifest["outputs"] = [str(p) for p in written]
        json_out.write_manifest(self.manifest, out_dir)
        return self.manifest

    # -- phases -----------------------------------------------------------
    async def _crawl(self) -> CrawlResult:
        async with Session(self.cfg) as session:
            try:
                await session.verify_auth()
                self.manifest["auth_status"] = "ok"
            except AuthError:
                self.manifest["auth_status"] = "failed"
                raise
            crawler = Crawler(self.cfg, session)
            return await crawler.run()

    def _generate(self, crawl: CrawlResult) -> tuple[TestSuite, dict[str, Any]]:
        suite = TestSuite(target=self.cfg.target.url)
        stats: dict[str, Any] = {
            "provider": self.cfg.llm.provider,
            "model": self.cfg.llm.model,
            "pages_attempted": 0,
            "pages_failed": 0,
            "repairs_attempted": 0,
            "warnings": [],
        }

        if not crawl.pages:
            stats["warnings"].append("no pages were captured; nothing to generate")
            return suite, stats

        adapter = build_adapter(self.cfg.llm)
        validator = Validator()

        paths = crawl.graph.shortest_paths() if crawl.graph else {}
        skips_by_url: dict[str, list[tuple[str, str]]] = {}
        for skip in crawl.skips:
            skips_by_url.setdefault(skip.url, []).append((skip.element, skip.reason))

        summaries_dir = self.cfg.output.dir / "summaries"

        for page in crawl.pages:
            stats["pages_attempted"] += 1
            node = crawl.graph.node_for(page.fingerprint) if crawl.graph else None
            reachability = paths.get(node.id) if node else None

            summary = summarize(page, reachability, skips_by_url.get(page.url))

            if self.cfg.output.save_summaries:
                summaries_dir.mkdir(parents=True, exist_ok=True)
                (summaries_dir / f"{page.fingerprint}.txt").write_text(
                    summary, encoding="utf-8"
                )

            if hasattr(adapter, "set_page_context"):
                adapter.set_page_context(  # type: ignore[attr-defined]
                    page.url, sorted(page.selector_set())
                )

            try:
                batch = adapter.generate(summary, self.cfg.llm.max_cases_per_page)
            except Exception as exc:
                log.warning("generation failed for %s: %s", page.url, exc)
                stats["pages_failed"] += 1
                stats["warnings"].append(f"generation failed for {page.url}: {exc}")
                continue

            cases, report = validator.check_page_batch(batch, page)

            if report.repairable:
                stats["repairs_attempted"] += 1
                log.info("repairing %d violation(s) for %s", len(report.violations), page.url)
                try:
                    repaired = adapter.repair(
                        summary, report.violations, self.cfg.llm.max_cases_per_page
                    )
                    recases, rereport = validator.check_page_batch(repaired, page)
                    if recases and len(rereport.violations) < len(report.violations):
                        cases, report = recases, rereport
                except Exception as exc:
                    log.warning("repair failed for %s: %s", page.url, exc)

            stats["warnings"].extend(report.warnings)
            suite.cases.extend(cases)

        suite.cases, suite_warnings = validator.finalize(suite.cases)
        stats["warnings"].extend(suite_warnings)
        stats["cases_generated"] = len(suite.cases)
        stats["cases_needing_review"] = sum(1 for c in suite.cases if c.needs_review)
        stats["usage"] = adapter.usage()
        return suite, stats

    def _write(
        self,
        suite: TestSuite,
        graph: NavGraph,
        paths: dict[str, list],
        crawl: CrawlResult,
    ) -> list[Path]:
        out_dir = self.cfg.output.dir
        formats = set(self.cfg.output.formats)
        written: list[Path] = []

        if not self.generate:
            # Crawl-only: the graph and the raw captures are the deliverable.
            written.extend(graph_render.write_all(graph, paths, out_dir, self.manifest))
            written.extend(json_out.write_page_models(crawl.pages, out_dir))
            return written

        if "markdown" in formats:
            written.append(markdown.write(suite, out_dir, graph if "graph" in formats else None))
        if "json" in formats:
            written.append(json_out.write_suite(suite, out_dir))
        if "xlsx" in formats:
            written.append(tabular.write_xlsx(suite, out_dir))
        if "csv" in formats:
            written.append(tabular.write_csv(suite, out_dir))
        if "graph" in formats:
            written.extend(graph_render.write_all(graph, paths, out_dir, self.manifest))
        if self.cfg.output.save_page_models:
            written.extend(json_out.write_page_models(crawl.pages, out_dir))

        return written
