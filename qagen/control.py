"""Out-of-process run control, via sentinel files in the run directory.

A crawl runs for hours as its own process. The web service supervises it but
must not kill it: the orchestrator is built so that a run which ends early
still writes the states it completed, and SIGKILL throws that away.

So control is cooperative. The service touches a file, the crawl notices on its
next iteration and unwinds through the normal exit path.

    <out_dir>/STOP    stop after the current state, keep everything captured
    <out_dir>/PAUSE   hold before the next state; delete the file to resume

Both are plain files so they survive an API restart and can be driven by hand:

    touch qagen-out/STOP
"""

from __future__ import annotations

import asyncio
import logging
from pathlib import Path

log = logging.getLogger("qagen.control")

STOP_FILE = "STOP"
PAUSE_FILE = "PAUSE"

#: How often a paused crawl re-checks for the sentinel going away.
POLL_SECONDS = 1.0


class RunControl:
    """Reads the sentinels. Never writes them -- that is the caller's job."""

    def __init__(self, out_dir: Path) -> None:
        self.out_dir = Path(out_dir)
        self.stop_file = self.out_dir / STOP_FILE
        self.pause_file = self.out_dir / PAUSE_FILE
        self.paused_seconds = 0.0

    @property
    def stop_requested(self) -> bool:
        try:
            return self.stop_file.exists()
        except OSError:
            # An unreadable run directory is not a reason to stop crawling.
            return False

    @property
    def paused(self) -> bool:
        try:
            return self.pause_file.exists()
        except OSError:
            return False

    async def wait_while_paused(self, on_change=None) -> None:
        """Block while PAUSE is present. Returns as soon as it is removed.

        STOP wins over PAUSE: a paused run that is then stopped must not sit
        here forever waiting for someone to unpause it first.
        """
        if not self.paused:
            return

        log.info("paused by operator (%s)", self.pause_file)
        if on_change:
            on_change("paused", f"waiting on {PAUSE_FILE}")

        waited = 0.0
        while self.paused and not self.stop_requested:
            await asyncio.sleep(POLL_SECONDS)
            waited += POLL_SECONDS

        self.paused_seconds += waited
        log.info("resumed after %.0fs", waited)
        if on_change:
            on_change("resumed", f"held for {waited:.0f}s")


# -- the writing half, used by the API and by hand -------------------------


def request_stop(out_dir: Path) -> Path:
    path = Path(out_dir) / STOP_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("stop requested\n", encoding="utf-8")
    return path


def request_pause(out_dir: Path) -> Path:
    path = Path(out_dir) / PAUSE_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("pause requested\n", encoding="utf-8")
    return path


def clear_pause(out_dir: Path) -> None:
    (Path(out_dir) / PAUSE_FILE).unlink(missing_ok=True)


def clear_all(out_dir: Path) -> None:
    for name in (STOP_FILE, PAUSE_FILE):
        (Path(out_dir) / name).unlink(missing_ok=True)
