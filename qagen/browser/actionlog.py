"""Streaming action log.

Every state discovery, click, outcome, skip and restore is appended to disk
**immediately** and flushed. That is the whole point: if the crawl stalls, the
last line in the log is the thing it stalled on. A log written at the end of
the run tells you nothing about a run that never ended.

Two files, same events:

* ``crawl-log.jsonl`` -- one JSON object per line, for tooling
* ``crawl-log.txt``   -- aligned and human-readable, for watching live

    tail -f qagen-out/crawl-log.txt
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, TextIO


class ActionLog:
    def __init__(self, out_dir: Path, enabled: bool = True) -> None:
        self.enabled = enabled
        self.started = time.monotonic()
        self._jsonl: TextIO | None = None
        self._text: TextIO | None = None
        self.counts: dict[str, int] = {}

        if not enabled:
            return
        out_dir.mkdir(parents=True, exist_ok=True)
        self._jsonl = (out_dir / "crawl-log.jsonl").open("w", encoding="utf-8")
        self._text = (out_dir / "crawl-log.txt").open("w", encoding="utf-8")
        self._write_text(
            f"{'time':>8}  {'event':<18} {'detail'}\n"
            f"{'-' * 8}  {'-' * 18} {'-' * 60}\n"
        )

    # -- public events ----------------------------------------------------
    def state_found(self, node_id: str, url: str, elements: int, forms: int, depth: int) -> None:
        self._emit(
            "state_found",
            f"{node_id}  {url}  ({elements} elements, {forms} forms, depth {depth})",
            node=node_id, url=url, elements=elements, forms=forms, depth=depth,
        )

    def state_seen(self, url: str, fingerprint: str) -> None:
        self._emit("state_duplicate", f"{url}  fp={fingerprint[:10]}",
                   url=url, fingerprint=fingerprint)

    def navigating(self, url: str, depth: int) -> None:
        self._emit("navigate", f"-> {url} (depth {depth})", url=url, depth=depth)

    def action(self, node_id: str, kind: str, name: str, selector: str) -> None:
        self._emit(
            "action",
            f"{node_id}  click {kind} {name!r}  [{selector}]",
            node=node_id, kind=kind, name=name, selector=selector,
        )

    def outcome(self, node_id: str, name: str, outcome: str,
                annotations: list[str], seconds: float) -> None:
        notes = f"  ({', '.join(annotations)})" if annotations else ""
        self._emit(
            "outcome",
            f"{node_id}  {name!r} -> {outcome}{notes}  [{seconds:.1f}s]",
            node=node_id, name=name, outcome=outcome,
            annotations=annotations, seconds=round(seconds, 2),
        )

    def skip(self, url: str, element: str, reason: str) -> None:
        self._emit("skip", f"{element}  -- {reason}", url=url,
                   element=element, reason=reason)

    def restore(self, node_id: str, ok: bool, how: str) -> None:
        self._emit(
            "restore",
            f"{node_id}  {'ok via ' + how if ok else 'FAILED (' + how + ')'}",
            node=node_id, ok=ok, how=how,
        )

    def note(self, kind: str, detail: str, **extra: Any) -> None:
        self._emit(kind, detail, **extra)

    def budget(self, snapshot: dict[str, Any]) -> None:
        self._emit(
            "budget",
            f"pages={snapshot.get('pages_visited')}/{snapshot.get('max_pages')} "
            f"clicks={snapshot.get('clicks_made')}/{snapshot.get('max_clicks')} "
            f"navs={snapshot.get('navigations')} "
            f"elapsed={snapshot.get('elapsed_seconds')}s",
            **snapshot,
        )

    # -- internals --------------------------------------------------------
    def _emit(self, event: str, detail: str, **fields: Any) -> None:
        self.counts[event] = self.counts.get(event, 0) + 1
        if not self.enabled:
            return
        elapsed = time.monotonic() - self.started
        record = {"t": round(elapsed, 2), "event": event, "detail": detail, **fields}
        if self._jsonl:
            self._jsonl.write(json.dumps(record, default=str) + "\n")
            self._jsonl.flush()          # flush: a stalled crawl must still be readable
        self._write_text(f"{elapsed:8.1f}  {event:<18} {detail}\n")

    def _write_text(self, line: str) -> None:
        if self._text:
            self._text.write(line)
            self._text.flush()

    def close(self, stop_reason: str | None = None) -> None:
        if stop_reason:
            self._emit("finished", f"crawl stopped: {stop_reason}")
        else:
            self._emit("finished", "crawl completed (frontier empty)")
        for handle in (self._jsonl, self._text):
            if handle:
                try:
                    handle.close()
                except Exception:
                    pass
        self._jsonl = self._text = None
