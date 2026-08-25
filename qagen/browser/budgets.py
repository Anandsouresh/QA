"""Hard budgets -- the guarantee that the crawl terminates.

Fingerprinting handles the loop cases we predicted. Budgets handle the ones
nobody predicted. Every counter here is a hard stop, and the crawl loop checks
``exhausted`` on every iteration, so there is no code path that does not
terminate.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field

from ..config import CrawlConfig


@dataclass
class Budgets:
    cfg: CrawlConfig
    started_at: float = field(default_factory=time.monotonic)
    pages_visited: int = 0
    navigations: int = 0
    clicks_made: int = 0
    consecutive_no_new: int = 0
    stop_reason: str | None = None

    # -- accounting -------------------------------------------------------
    def take_navigation(self) -> bool:
        """Charged per goto, including ones that turn out to be duplicates.

        Kept separate from ``take_page`` because a 50-item list enqueues 50
        URLs that all collapse to one state -- charging those against
        ``max_pages`` would exhaust the page budget without discovering
        anything.
        """
        cap = self.cfg.max_navigations or (self.cfg.max_pages * 10)
        if self.navigations >= cap:
            self._stop("max_navigations")
            return False
        self.navigations += 1
        return True

    def take_page(self) -> bool:
        """Charged once per *distinct state* discovered."""
        if self.pages_visited >= self.cfg.max_pages:
            self._stop("max_pages")
            return False
        self.pages_visited += 1
        return True

    def take_click(self) -> bool:
        if self.clicks_made >= self.cfg.max_clicks:
            self._stop("max_clicks")
            return False
        self.clicks_made += 1
        return True

    def note_state(self, is_new: bool) -> None:
        if is_new:
            self.consecutive_no_new = 0
        else:
            self.consecutive_no_new += 1
            if self.consecutive_no_new >= self.cfg.max_consecutive_no_new_states:
                self._stop("max_consecutive_no_new_states")

    # -- queries ----------------------------------------------------------
    @property
    def elapsed(self) -> float:
        return time.monotonic() - self.started_at

    @property
    def exhausted(self) -> bool:
        if self.stop_reason:
            return True
        if self.elapsed >= self.cfg.max_wall_clock_seconds:
            self._stop("max_wall_clock_seconds")
            return True
        return False

    def _stop(self, reason: str) -> None:
        if self.stop_reason is None:
            self.stop_reason = reason

    def snapshot(self) -> dict[str, object]:
        return {
            "pages_visited": self.pages_visited,
            "navigations": self.navigations,
            "max_pages": self.cfg.max_pages,
            "clicks_made": self.clicks_made,
            "max_clicks": self.cfg.max_clicks,
            "elapsed_seconds": round(self.elapsed, 1),
            "max_wall_clock_seconds": self.cfg.max_wall_clock_seconds,
            "consecutive_no_new_states": self.consecutive_no_new,
            "stop_reason": self.stop_reason,
        }
