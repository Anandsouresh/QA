"""Run registry.

The run directory is the database. This file only keeps the index -- what runs
exist, where they live, and whether their process is still alive -- so nothing
here duplicates the graph, the captures or the test cases, all of which already
parse from disk in milliseconds.

SQLite because the index must survive an API restart: a crawl runs for hours
and must be re-attachable afterwards.
"""

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import threading
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = Path(os.environ.get("QAGEN_RUNS_DIR", REPO_ROOT / "runs"))
DB_PATH = RUNS_DIR / "index.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id            TEXT PRIMARY KEY,
    label         TEXT,
    target        TEXT NOT NULL,
    status        TEXT NOT NULL,
    mode          TEXT NOT NULL,
    run_dir       TEXT NOT NULL,
    pid           INTEGER,
    created_at    TEXT NOT NULL,
    finished_at   TEXT,
    exit_code     INTEGER,
    modules       TEXT,
    max_states    INTEGER
);
"""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect() -> sqlite3.Connection:
    """One shared connection in autocommit mode.

    FastAPI runs sync endpoints on a threadpool, so several requests touch this
    connection at once. `isolation_level=None` means sqlite3 opens no implicit
    transaction, which is what made a concurrent `commit()` raise "cannot commit
    - no transaction is active"; every write below is a single statement, so
    autocommit is the right shape. `_LOCK` serialises them.
    """
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.executescript(SCHEMA)
    return conn


_LOCK = threading.RLock()


@dataclass
class Run:
    id: str
    label: str
    target: str
    status: str
    mode: str
    run_dir: Path
    pid: int | None
    created_at: str
    finished_at: str | None
    exit_code: int | None
    modules: dict[str, int]
    max_states: int

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Run":
        return cls(
            id=row["id"],
            label=row["label"] or row["id"],
            target=row["target"],
            status=row["status"],
            mode=row["mode"],
            run_dir=Path(row["run_dir"]),
            pid=row["pid"],
            created_at=row["created_at"],
            finished_at=row["finished_at"],
            exit_code=row["exit_code"],
            modules=json.loads(row["modules"] or "{}"),
            max_states=row["max_states"] or 0,
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "label": self.label,
            "target": self.target,
            "status": self.status,
            "mode": self.mode,
            "pid": self.pid,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "exit_code": self.exit_code,
            "modules": self.modules,
            "max_states": self.max_states,
            "has_graph": (self.run_dir / "navgraph.json").exists(),
            "has_cases": (self.run_dir / "test-cases.json").exists(),
            "log_bytes": _size(self.run_dir / "crawl-log.jsonl"),
        }


def _size(path: Path) -> int:
    try:
        return path.stat().st_size
    except OSError:
        return 0


def pid_alive(pid: int | None) -> bool:
    if not pid:
        return False
    if sys.platform == "win32":
        out = subprocess.run(
            ["tasklist", "/FI", f"PID eq {pid}", "/NH"],
            capture_output=True, text=True,
        )
        return str(pid) in out.stdout
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


class RunStore:
    def __init__(self) -> None:
        self.conn = connect()

    # -- reads ------------------------------------------------------------
    def list(self) -> list[Run]:
        with _LOCK:
            rows = self.conn.execute(
                "SELECT * FROM runs ORDER BY created_at DESC"
            ).fetchall()
        runs = [Run.from_row(r) for r in rows]
        for run in runs:
            self._reconcile(run)
        return runs

    def get(self, run_id: str) -> Run | None:
        with _LOCK:
            row = self.conn.execute(
                "SELECT * FROM runs WHERE id = ?", (run_id,)
            ).fetchone()
        if row is None:
            return None
        run = Run.from_row(row)
        self._reconcile(run)
        return run

    def _reconcile(self, run: Run) -> None:
        """A run marked running whose process is gone has finished; say so.

        This is what makes the index survive an API restart: state is derived
        from the process table and the run directory, never trusted blindly.
        """
        # "stopping" and "starting" are transient too: a run whose process has
        # exited is finished regardless of which of them it was last marked.
        if run.status not in {"running", "paused", "stopping", "starting"}:
            return
        if pid_alive(run.pid):
            if run.status == "stopping":
                return  # a stop is in flight; leave the label alone
            run.status = "paused" if (run.run_dir / "PAUSE").exists() else "running"
            with _LOCK:
                self.conn.execute(
                    "UPDATE runs SET status = ? WHERE id = ?", (run.status, run.id)
                )
                return
        manifest = run.run_dir / "run_manifest.json"
        if manifest.exists():
            run.status = "stopped" if (run.run_dir / "STOP").exists() else "finished"
        else:
            run.status = "failed"
        run.finished_at = run.finished_at or _now()
        with _LOCK:
            self.conn.execute(
                "UPDATE runs SET status = ?, finished_at = ? WHERE id = ?",
                (run.status, run.finished_at, run.id),
            )

    # -- writes -----------------------------------------------------------
    def create(
        self,
        run_id: str,
        target: str,
        run_dir: Path,
        mode: str,
        modules: dict[str, int],
        max_states: int,
        label: str = "",
    ) -> Run:
        with _LOCK:
            self.conn.execute(
                "INSERT INTO runs (id, label, target, status, mode, run_dir, created_at,"
                " modules, max_states) VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    run_id, label or run_id, target, "starting", mode, str(run_dir),
                    _now(), json.dumps(modules), max_states,
                ),
            )
        return self.get(run_id)  # type: ignore[return-value]

    def set_pid(self, run_id: str, pid: int) -> None:
        with _LOCK:
            self.conn.execute(
                "UPDATE runs SET pid = ?, status = 'running' WHERE id = ?", (pid, run_id)
            )

    def set_status(self, run_id: str, status: str) -> None:
        with _LOCK:
            self.conn.execute("UPDATE runs SET status = ? WHERE id = ?", (status, run_id))

    def finish(self, run_id: str, exit_code: int) -> None:
        with _LOCK:
            self.conn.execute(
                "UPDATE runs SET status = ?, finished_at = ?, exit_code = ? WHERE id = ?",
                ("finished" if exit_code == 0 else "failed", _now(), exit_code, run_id),
            )

    def delete(self, run_id: str) -> None:
        with _LOCK:
            self.conn.execute("DELETE FROM runs WHERE id = ?", (run_id,))


def next_run_id(target: str, existing: Iterable[str]) -> str:
    from urllib.parse import urlsplit

    host = (urlsplit(target).netloc or "run").split(":")[0]
    slug = host.replace(".", "-")[:28]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    base = f"{stamp}-{slug}"
    taken = set(existing)
    if base not in taken:
        return base
    for n in range(2, 100):
        candidate = f"{base}-{n}"
        if candidate not in taken:
            return candidate
    return f"{base}-{int(time.time())}"
