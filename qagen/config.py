"""Configuration model and YAML loading.

Everything site-specific lives in the YAML file; the CLI overrides only a
handful of top-level values. Validation happens before a browser is ever
launched -- a config error must not cost a browser start.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field, field_validator

DEFAULT_DENY_TEXT = [
    "delete", "remove", "destroy", "erase", "drop",
    "pay", "purchase", "checkout", "buy", "subscribe", "order",
    "submit", "confirm", "approve", "publish", "send",
    "logout", "log out", "sign out",
    "deactivate", "disable account", "cancel subscription",
    "reset", "revoke", "archive", "merge", "transfer",
]

DEFAULT_DENY_SELECTORS = [
    "[data-destructive]",
    "[data-testid*='delete' i]",
    ".btn-danger",
]

CONSENT_VOCAB = [
    "accept all", "accept cookies", "allow all", "got it", "i agree",
    "agree", "consent", "understood", "ok, got it", "allow cookies",
]


class TargetConfig(BaseModel):
    url: str
    depth: int = Field(default=0, ge=0, le=500)
    same_origin_only: bool = True
    include_paths: list[str] = Field(default_factory=list)
    exclude_paths: list[str] = Field(default_factory=lambda: ["/logout", "/signout"])
    #: Path segments matching these are NOT collapsed to {id}. Escape hatch for
    #: sites with meaningful numeric routes such as /year/2024.
    id_collapse_exceptions: list[str] = Field(default_factory=list)


class AuthConfig(BaseModel):
    storage_state: Path | None = None
    verify_selector: str | None = None
    verify_timeout_ms: int = 5000

    @field_validator("storage_state")
    @classmethod
    def _exists(cls, v: Path | None) -> Path | None:
        if v is not None and not v.exists():
            raise ValueError(f"auth.storage_state file not found: {v}")
        return v


class CrawlConfig(BaseModel):
    max_pages: int = Field(default=25, ge=1)
    #: Cap on goto() calls, including duplicates. Defaults to max_pages * 10.
    max_navigations: int | None = Field(default=None, ge=1)
    max_clicks: int = Field(default=200, ge=1)
    max_wall_clock_seconds: int = Field(default=900, ge=10)
    max_clicks_per_state: int = Field(default=30, ge=1)
    #: Distinct states to keep per normalised URL. An in-page editor (a
    #: dashboard where each click adds or removes a card) produces a genuinely
    #: new state every click; those are real, but a dozen of them is low value
    #: and crowds out the rest of the app.
    #: 6 rather than 3: one page routinely carries several legitimate same-page
    #: states -- a modal, a disclosure panel, and the menu each "+" opens -- and
    #: at 3 whichever was reached last was silently dropped.
    max_states_per_url: int = Field(default=6, ge=1)
    #: Cap on states kept per top-level section (the first path segment).
    #: Without it one deep area swallows the crawl: on a real run `/settings`
    #: took 43 of 63 states while `/screen`, `/schedule` and `/channel` were
    #: never reached at all.
    max_states_per_section: int = Field(default=12, ge=1)
    #: Selectors (matched as substrings) belonging to the persistent app frame
    #: -- header, left menu, floating assistant. Elements inside them are still
    #: extracted and still clicked once, but they rank below content-area
    #: actions so the budget goes to the part of the app that changes.
    #: Left empty, the shell is inferred from what repeats across URLs.
    shell_selectors: list[str] = Field(default_factory=list)
    #: Site-specific markers for "this element is clickable", used when the
    #: platform gives us nothing to go on -- no role, no tabindex, not even a
    #: pointer cursor. Analytics instrumentation is usually the best source:
    #: whatever a team tracks button clicks with is, by definition, attached to
    #: every button. The generic attribute forms below are always included.
    extra_clickable_selectors: list[str] = Field(
        default_factory=lambda: [
            "[data-ga]", "[data-analytics]", "[data-track]", "[data-tracking]",
            "[data-event]", "[data-gtm]",
        ]
    )
    #: How many distinct URLs an element must appear on before it is inferred
    #: to be part of the frame.
    shell_min_urls: int = Field(default=3, ge=2)
    #: Backstop only. A templated list that collapses correctly produces one
    #: duplicate per item by design, so this must comfortably exceed the
    #: largest list on the site. max_navigations is the real bound.
    max_consecutive_no_new_states: int = Field(default=100, ge=1)
    settle_timeout_ms: int = Field(default=3000, ge=200)
    #: How long to wait for an SPA to render *anything* interactive before
    #: giving up and extracting whatever is there. Separate from the stability
    #: cap because an unhydrated page is stable-but-empty, and extracting it
    #: yields a state with zero elements.
    hydration_timeout_ms: int = Field(default=10000, ge=0)
    #: How long the interactive signature must hold still before we call the
    #: page settled. Two consecutive polls is not enough on a dashboard that
    #: loads its cards one API response at a time.
    stability_ms: int = Field(default=400, ge=0)
    #: How many interactive elements count as "hydrated". Default 1 (any
    #: content). Raise it for a heavy SPA whose shell renders a spinner and
    #: holds still -- but only there: a genuinely small page that never reaches
    #: the bar waits out the whole hydration timeout on every single visit.
    hydration_min_elements: int = Field(default=1, ge=1)
    #: Wait for the app's own loading indicator to disappear. Set to 0 to skip.
    loader_timeout_ms: int = Field(default=15000, ge=0)
    #: Extra site-specific loader selectors, on top of the built-in patterns
    #: (aria-busy, role=progressbar, class/id containing loader/spinner/skeleton).
    loader_selectors: list[str] = Field(default_factory=list)
    #: Grace period after a loader disappears, so content that renders just
    #: behind it is captured. Charged only when a loader was actually seen.
    post_loader_wait_ms: int = Field(default=5000, ge=0)
    #: Hover unnamed clickables to read the tooltip the app reveals. An
    #: icon-only "+" has no accessible name at all, so without this it reaches
    #: the report as an unnamed element and produces a useless test step.
    #: Costs one hover + one evaluate per unnamed element, capped below.
    hover_naming: bool = True
    #: Upper bound on hover probes per page, so a page full of icon buttons
    #: cannot turn one extraction into a hundred round-trips.
    hover_naming_limit: int = Field(default=12, ge=0)
    #: How long to let the tooltip animate in before reading it.
    hover_settle_ms: int = Field(default=350, ge=0)
    #: How many restores may fail in a row before a state is given up on.
    #:
    #: A single failure used to end the state, discarding every remaining
    #: action. Because app-frame controls (header, left menu) are planned last,
    #: they were always in the discarded tail -- the notification bell went
    #: unclicked on the entry page for exactly this reason.
    max_restore_failures: int = Field(default=3, ge=1)
    action_timeout_ms: int = Field(default=8000, ge=500)
    nav_timeout_ms: int = Field(default=20000, ge=1000)
    #: A popup has no URL, so returning to it means replaying the click that
    #: opened it: navigate to the page, then re-click the trigger. This caps how
    #: many such steps a single frontier item may carry -- 2 covers a menu and
    #: one dialog inside it, and every extra step is another chance for the
    #: replay to land somewhere else on a live app.
    max_replay_steps: int = Field(default=2, ge=1)
    #: Order the crawler works through a state's elements.
    #:
    #: "reading" walks the page the way a person does -- top to bottom, left to
    #: right -- which makes the action log and the generated steps follow the
    #: layout, and makes a truncated state a coherent top-slice of the page
    #: rather than a scatter. "priority" is the older behaviour: most-informative
    #: kind first (overlay triggers, then tabs, then buttons).
    action_order: Literal["reading", "priority"] = "reading"
    #: Extra slots, beyond ``max_clicks_per_state``, reserved for app-frame
    #: controls no state has exercised yet.
    #:
    #: Without this the per-state cap and ``content_before_frame`` combine into
    #: a trap: a page with 40 content elements fills a 10-click plan before the
    #: header or left menu is reached, and in a menu-driven SPA the left menu is
    #: the *only* way to another section -- its items are divs with no href, so
    #: they are never enqueued as links either. One real run starved on exactly
    #: this, ending with the frontier empty at 34 states, `/settings` at zero,
    #: and the left menu clicked twice in total.
    #:
    #: These slots are nearly free: global dedup means each control is exercised
    #: once in the whole crawl, so the cost is one click per control, ever.
    #: Strictly the frame: content past the cap is a deliberate truncation, and
    #: admitting it here would just turn the cap into cap + reserve.
    frame_reserve: int = Field(default=8, ge=0)
    #: Within the chosen order, do the content area before the app frame. Left
    #: on, a page is walked in reading order twice: once through the content,
    #: then once through the header and left menu. Turn it off for strict
    #: whole-page reading order.
    content_before_frame: bool = True
    #: Rows are rarely pixel-aligned, so vertical position is bucketed into
    #: bands this tall before left-to-right ordering applies. Too small and a
    #: 32px button sorts above the 24px icon beside it; too large and distinct
    #: rows merge.
    reading_band_px: int = Field(default=20, ge=1)
    probe_search: bool = True
    search_probe_term: str = "qa"


class InteractionConfig(BaseModel):
    policy: Literal["safe_click", "passive"] = "safe_click"
    deny_text: list[str] = Field(default_factory=lambda: list(DEFAULT_DENY_TEXT))
    deny_selectors: list[str] = Field(
        default_factory=lambda: list(DEFAULT_DENY_SELECTORS)
    )
    allow_selectors: list[str] = Field(default_factory=list)
    dismiss_consent: bool = True
    consent_vocab: list[str] = Field(default_factory=lambda: list(CONSENT_VOCAB))


class LLMConfig(BaseModel):
    provider: Literal["claude", "stub"] = "claude"
    model: str = "claude-opus-5"
    effort: Literal["low", "medium", "high", "xhigh", "max"] = "high"
    max_tokens: int = 16000
    cache_system_prompt: bool = True
    max_cases_per_page: int = 12


class OutputConfig(BaseModel):
    dir: Path = Path("./qagen-out")
    formats: list[Literal["markdown", "json", "xlsx", "csv", "graph"]] = Field(
        default_factory=lambda: ["markdown", "json", "xlsx", "graph"]
    )
    save_page_models: bool = True
    save_summaries: bool = False
    #: One screenshot + one raw-DOM dump per discovered state. Cheap, and the
    #: fastest way to see why a capture looks wrong -- a blank screenshot means
    #: the settle heuristic fired before the app rendered, which no amount of
    #: reading the element inventory would tell you.
    save_screenshots: bool = True
    save_html: bool = True
    screenshot_full_page: bool = True
    #: Stream every action to crawl-log.jsonl / crawl-log.txt as it happens.
    #: Flushed per line, so `tail -f` shows exactly where a stalled crawl is.
    action_log: bool = True

    @field_validator("formats")
    @classmethod
    def _non_empty(cls, v: list[str]) -> list[str]:
        if not v:
            raise ValueError("output.formats must not be empty")
        return v


class BrowserConfig(BaseModel):
    headless: bool = True
    viewport_width: int = 1440
    viewport_height: int = 900
    user_agent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0 Safari/537.36 QAGen/0.1"
    )
    #: The network write-guard. Turning this off allows real mutations against
    #: the target -- never do it on an environment you do not own.
    block_mutations: bool = True
    slow_mo_ms: int = 0


class RunConfig(BaseModel):
    target: TargetConfig
    auth: AuthConfig = Field(default_factory=AuthConfig)
    crawl: CrawlConfig = Field(default_factory=CrawlConfig)
    interaction: InteractionConfig = Field(default_factory=InteractionConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    browser: BrowserConfig = Field(default_factory=BrowserConfig)

    @classmethod
    def load(
        cls,
        config_path: Path | None = None,
        overrides: dict[str, Any] | None = None,
    ) -> "RunConfig":
        """Load YAML, then apply CLI overrides on top (CLI wins)."""
        data: dict[str, Any] = {}
        if config_path is not None:
            if not config_path.exists():
                raise ValueError(f"config file not found: {config_path}")
            loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
            if not isinstance(loaded, dict):
                raise ValueError("config file must contain a YAML mapping")
            data = loaded

        for dotted, value in (overrides or {}).items():
            if value is None:
                continue
            section, _, key = dotted.partition(".")
            if not key:
                data[section] = value
                continue
            data.setdefault(section, {})
            if not isinstance(data[section], dict):
                raise ValueError(f"cannot override '{dotted}': '{section}' is not a mapping")
            data[section][key] = value

        if "target" not in data or not data["target"].get("url"):
            raise ValueError("target.url is required (pass --url or set it in the config)")

        return cls.model_validate(data)
