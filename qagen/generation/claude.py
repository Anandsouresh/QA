"""The default provider: Anthropic Claude with structured outputs.

Three things carry their weight here:

* **Structured outputs** (``output_config.format`` with a JSON Schema) so the
  response is schema-valid by construction rather than parsed out of prose.
* **Prompt caching** -- the QA system prompt is stable across every page in a
  run and sits behind a cache breakpoint, so most of the input on page 2..N is
  a cache read.
* **Adaptive thinking** at configurable effort. Category coverage and negative-
  path reasoning benefit from it, and this is one call per page, not a hot loop.
"""

from __future__ import annotations

import json
import logging

from ..config import LLMConfig
from ..models import TestCaseBatch
from .prompts import QA_SYSTEM_PROMPT, repair_block, user_block
from .schema import GeneratedBatch, harden_schema, to_test_case

log = logging.getLogger("qagen.claude")


class ClaudeAdapter:
    name = "claude"

    def __init__(self, cfg: LLMConfig) -> None:
        import anthropic  # imported lazily so `--provider stub` needs no SDK

        self.cfg = cfg
        # Zero-arg client: resolves ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, or
        # an `ant auth login` profile. An unset env var is not by itself an error.
        self.client = anthropic.Anthropic()
        self._schema = harden_schema(GeneratedBatch)
        self._usage = {
            "input_tokens": 0,
            "output_tokens": 0,
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": 0,
            "calls": 0,
        }
        self._current_url = ""

    # -- public API -------------------------------------------------------
    def generate(self, summary: str, max_cases: int) -> TestCaseBatch:
        return self._call(user_block(summary, max_cases), summary)

    def repair(self, summary: str, violations: list[str], max_cases: int) -> TestCaseBatch:
        return self._call(repair_block(summary, violations), summary)

    def usage(self) -> dict[str, int]:
        return dict(self._usage)

    def set_page_context(self, url: str, selectors: list[str]) -> None:
        """Provenance for the cases produced by the next call. The selector set
        is not sent to the model -- it already receives the inventory."""
        self._current_url = url

    # -- internals --------------------------------------------------------
    def _call(self, user_text: str, summary: str) -> TestCaseBatch:
        system: list[dict] = [{"type": "text", "text": QA_SYSTEM_PROMPT}]
        if self.cfg.cache_system_prompt:
            system[0]["cache_control"] = {"type": "ephemeral"}

        response = self.client.messages.create(
            model=self.cfg.model,
            max_tokens=self.cfg.max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            output_config={
                "effort": self.cfg.effort,
                "format": {"type": "json_schema", "schema": self._schema},
            },
            messages=[{"role": "user", "content": user_text}],
        )

        self._record_usage(response)

        if response.stop_reason == "refusal":
            detail = getattr(response, "stop_details", None)
            log.warning(
                "generation refused (%s); skipping this page",
                getattr(detail, "category", "unknown"),
            )
            return TestCaseBatch()

        if response.stop_reason == "max_tokens":
            log.warning(
                "generation hit max_tokens; output for this page may be truncated"
            )

        text = next(
            (b.text for b in response.content if getattr(b, "type", "") == "text"), ""
        )
        if not text.strip():
            return TestCaseBatch()

        try:
            batch = GeneratedBatch.model_validate_json(text)
        except Exception as exc:
            log.warning("could not parse structured output: %s", exc)
            try:  # tolerate a stray wrapper object
                batch = GeneratedBatch.model_validate(json.loads(text))
            except Exception:
                return TestCaseBatch()

        return TestCaseBatch(
            cases=[to_test_case(c, self._current_url) for c in batch.cases]
        )

    def _record_usage(self, response: object) -> None:
        usage = getattr(response, "usage", None)
        if usage is None:
            return
        self._usage["calls"] += 1
        for key in (
            "input_tokens",
            "output_tokens",
            "cache_creation_input_tokens",
            "cache_read_input_tokens",
        ):
            self._usage[key] += int(getattr(usage, key, 0) or 0)
