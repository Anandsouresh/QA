"""The LLM adapter protocol and the provider registry.

Claude is the shipped default. The protocol is deliberately narrow -- one
method -- so swapping providers never leaks into the crawl or reporting layers.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ..config import LLMConfig
from ..models import TestCaseBatch


@runtime_checkable
class LLMAdapter(Protocol):
    name: str

    def generate(self, summary: str, max_cases: int) -> TestCaseBatch:
        """Generate test cases for one page summary."""
        ...

    def repair(self, summary: str, violations: list[str], max_cases: int) -> TestCaseBatch:
        """One corrective round-trip after validation failures."""
        ...

    def usage(self) -> dict[str, int]:
        """Cumulative token usage, for the run manifest."""
        ...

    def set_page_context(self, url: str, selectors: list[str]) -> None:
        """Provenance for the cases produced by the next call.

        ``selectors`` is the page's grounded selector set. Providers that
        generate rather than infer (Claude) only need the URL; the offline stub
        uses the selector set so its output passes the same grounding check
        real output has to pass.
        """
        ...


def build_adapter(cfg: LLMConfig) -> LLMAdapter:
    if cfg.provider == "claude":
        from .claude import ClaudeAdapter

        return ClaudeAdapter(cfg)
    if cfg.provider == "stub":
        from .stub import StubAdapter

        return StubAdapter(cfg)
    raise ValueError(f"unknown llm.provider: {cfg.provider}")
