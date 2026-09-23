"""The sentinel files that let a supervisor stop a crawl without killing it.

The point of cooperative control is that a stopped run still writes what it
captured. These tests pin the two halves of that: the budget notices STOP on
its next check, and a paused loop resumes when the file goes away.
"""

from __future__ import annotations

import asyncio

import pytest

from qagen.browser.budgets import Budgets
from qagen.config import CrawlConfig
from qagen.control import (
    RunControl,
    clear_all,
    clear_pause,
    request_pause,
    request_stop,
)


@pytest.fixture()
def run_dir(tmp_path):
    return tmp_path / "run"


def test_no_sentinels_means_no_stop(run_dir):
    control = RunControl(run_dir)
    assert control.stop_requested is False
    assert control.paused is False


def test_stop_file_exhausts_the_budget(run_dir):
    control = RunControl(run_dir)
    budgets = Budgets(CrawlConfig(), control=control)

    assert budgets.exhausted is False

    request_stop(run_dir)
    assert budgets.exhausted is True
    assert budgets.stop_reason == "stopped by operator"


def test_stop_reason_is_reported_over_the_wall_clock(run_dir):
    """An operator stop must not be mislabelled as a budget expiring."""
    control = RunControl(run_dir)
    budgets = Budgets(CrawlConfig(max_wall_clock_seconds=10), control=control)
    budgets.started_at -= 999  # the clock has long since run out

    request_stop(run_dir)
    assert budgets.exhausted is True
    assert budgets.stop_reason == "stopped by operator"


def test_budget_without_control_is_unaffected(run_dir):
    """The CLI passes no control; nothing about its behaviour changes."""
    budgets = Budgets(CrawlConfig())
    assert budgets.control is None
    assert budgets.exhausted is False
    assert budgets.snapshot()["paused_seconds"] == 0.0


def test_pause_blocks_until_the_file_is_removed(run_dir):
    control = RunControl(run_dir)
    request_pause(run_dir)
    assert control.paused is True

    seen: list[str] = []

    async def scenario():
        async def release():
            await asyncio.sleep(0.05)
            clear_pause(run_dir)

        asyncio.create_task(release())
        await control.wait_while_paused(on_change=lambda kind, _: seen.append(kind))

    asyncio.run(asyncio.wait_for(scenario(), timeout=10))

    assert control.paused is False
    assert seen == ["paused", "resumed"]
    assert control.paused_seconds > 0


def test_stop_releases_a_paused_run(run_dir):
    """A run paused and then stopped must not wait for an unpause first."""
    control = RunControl(run_dir)
    request_pause(run_dir)

    async def scenario():
        async def stop_it():
            await asyncio.sleep(0.05)
            request_stop(run_dir)

        asyncio.create_task(stop_it())
        await control.wait_while_paused()

    asyncio.run(asyncio.wait_for(scenario(), timeout=10))

    assert control.stop_requested is True
    assert control.paused is True  # the PAUSE file is still there; STOP won


def test_clear_all_removes_both(run_dir):
    request_stop(run_dir)
    request_pause(run_dir)
    control = RunControl(run_dir)
    assert control.stop_requested and control.paused

    clear_all(run_dir)
    assert control.stop_requested is False
    assert control.paused is False


def test_unreadable_directory_does_not_stop_the_crawl(run_dir, monkeypatch):
    """A filesystem hiccup is not a reason to abandon an hours-long run."""
    control = RunControl(run_dir)

    def boom(self):
        raise OSError("device not ready")

    monkeypatch.setattr("pathlib.Path.exists", boom)
    assert control.stop_requested is False
    assert control.paused is False
