# QAGen — Architecture

**Automated QA test-case generation from a live URL.**

Input: a URL (plus optional auth state). Output: structured, human-readable test cases covering Happy Path, Negative, Edge Case, UI/UX, and Form Filling — plus a navigation graph of the application.

> **Deep dive:** [CRAWLING_AND_EXTRACTION.md](CRAWLING_AND_EXTRACTION.md) covers element classification, the six overlay/popup kinds, the crawl state machine, the navigation graph, and per-phase I/O contracts. It supersedes this document wherever the two differ on crawl detail.

---

## 0. Decisions locked with you

These were confirmed before this document was written. They are not assumptions.

| Area | Decision |
|---|---|
| Language | Python 3.11+ |
| Browser driver | Playwright (async API) |
| Authentication | Cookie JSON / Playwright `storage_state` file |
| LLM | Pluggable adapter layer; **Anthropic Claude is the default provider** |
| Crawl scope | Configurable depth. `depth=0` → single page. `depth>0` → same-origin, depth-limited |
| Interaction policy | Safe-click only (destructive deny-list, no real form submissions) |
| Element extraction | Accessibility tree **+** DOM heuristics with stable selector synthesis |
| Loop prevention | Composite state fingerprint (normalized URL + interactive-element signature) + global budgets |
| Output formats | Markdown, JSON, and Excel/CSV — all three |
| Interface | CLI + YAML config |
| Deliverable now | Documentation only. No code until you approve. |

---

## 1. System overview

```
                        ┌──────────────────────────────┐
   qagen run  ─────────▶│         CLI + Config          │
   --url --config       │  (typer + pydantic-settings)  │
                        └───────────────┬───────────────┘
                                        │ RunConfig
                                        ▼
                        ┌──────────────────────────────┐
                        │      Orchestrator             │
                        │  owns budgets + run lifecycle │
                        └───┬───────────────────────┬───┘
                            │                       │
              ┌─────────────▼──────────┐   ┌────────▼─────────────┐
              │   Browser Layer         │   │   Generation Layer   │
              │  ┌──────────────────┐   │   │  ┌────────────────┐  │
              │  │ SessionManager   │   │   │  │ PageSummarizer │  │
              │  │ (storage_state)  │   │   │  │  (token diet)  │  │
              │  ├──────────────────┤   │   │  ├────────────────┤  │
              │  │ PageAnalyzer     │   │   │  │  LLMAdapter    │  │
              │  │ (a11y + DOM)     │   │   │  │  ├ Claude ◀dflt│  │
              │  ├──────────────────┤   │   │  │  └ (pluggable) │  │
              │  │ Crawler          │   │   │  ├────────────────┤  │
              │  │ (safe-click BFS) │   │   │  │  Validator     │  │
              │  ├──────────────────┤   │   │  │  (schema+rules)│  │
              │  │ StateRegistry    │   │   │  └────────────────┘  │
              │  │ (fingerprints)   │   │   └────────┬─────────────┘
              │  └──────────────────┘   │            │
              └────────────┬────────────┘            │
                           │  PageModel[]             │ TestCase[]
                           └────────────┬─────────────┘
                                        ▼
                        ┌──────────────────────────────┐
                        │       Reporting Layer         │
                        │   Markdown │ JSON │ XLSX/CSV  │
                        └──────────────────────────────┘
```

Data flows one direction: **Browser → PageModel → LLM → TestCase → Reports.** Nothing downstream writes back to the browser layer. That keeps the LLM strictly out of the crawl control loop, which matters for both cost and determinism.

---

## 2. Layer responsibilities

### 2.1 CLI + Config

`qagen run --url https://app.example.com --config site.yaml`

The YAML config is the single source of truth for anything site-specific. The CLI only overrides a handful of top-level values.

```yaml
target:
  url: https://app.example.com
  depth: 1                    # 0 = single page only
  same_origin_only: true
  include_paths: ["/dashboard/**", "/settings/**"]
  exclude_paths: ["/logout", "/admin/**"]

auth:
  storage_state: ./secrets/auth.json   # Playwright storage_state or cookie JSON
  verify_selector: "[data-testid=user-menu]"   # proves login worked

crawl:
  max_pages: 25
  max_clicks: 200
  max_wall_clock_seconds: 900
  max_clicks_per_state: 30
  settle_timeout_ms: 3000

interaction:
  policy: safe_click
  deny_text: ["delete", "remove", "pay", "purchase", "submit", "confirm",
              "logout", "sign out", "deactivate", "cancel subscription"]
  deny_selectors: ["[data-destructive]", "form[method=post] button[type=submit]"]
  allow_selectors: []          # explicit overrides win over deny

llm:
  provider: claude             # default
  model: claude-opus-5
  effort: high
  max_tokens: 16000
  cache_system_prompt: true

output:
  dir: ./qagen-out
  formats: [markdown, json, xlsx]
```

### 2.2 Browser Layer

Four components, each with one job.

**SessionManager** — owns the Playwright lifecycle. Launches Chromium, creates a `BrowserContext` seeded with `storage_state`, and applies global route interception. It is also the enforcement point for the write-guard (§5.3).

**PageAnalyzer** — turns a settled page into a `PageModel`. Combines Playwright's accessibility snapshot with a DOM walk (§3).

**Crawler** — breadth-first frontier over *states*, not URLs. Decides what to click next, subject to the interaction policy and the budgets.

**StateRegistry** — the visited-set. Holds composite fingerprints and answers one question: "have I already been here?" (§4).

### 2.3 Generation Layer

**PageSummarizer** — the cost control. A rendered React page can be 500 KB of DOM; the LLM needs maybe 4 KB of it. This component compresses a `PageModel` into a compact, deterministic text block: element inventory grouped by role, form field inventory with types and validation attributes, navigation landmarks, and observed network endpoints. Deterministic ordering matters — it keeps the prompt cacheable.

**LLMAdapter** — a narrow protocol with Claude as the shipped default:

```python
class LLMAdapter(Protocol):
    def generate_test_cases(
        self, page: PageSummary, categories: list[Category]
    ) -> list[TestCase]: ...
```

The Claude implementation uses the `anthropic` SDK with **structured outputs** so every returned test case is schema-guaranteed rather than parsed out of prose:

```python
response = client.messages.parse(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    system=[{"type": "text", "text": QA_SYSTEM_PROMPT,
             "cache_control": {"type": "ephemeral"}}],
    messages=[{"role": "user", "content": page_summary_block}],
    output_format=TestCaseBatch,          # pydantic model → validated instance
)
batch = response.parsed_output
```

The stable QA system prompt sits behind a cache breakpoint, and the volatile per-page summary comes after it. Across a 25-page crawl that turns most of the input into cache reads.

**Validator** — schema conformance is guaranteed by the API, but semantics are not. This layer enforces the rules a schema cannot: Test IDs are unique and sequential, step numbers are contiguous from 1, every test case has ≥1 step, each of the five categories is represented, and no generated step references a selector that does not exist in the source `PageModel` (the anti-hallucination check).

### 2.4 Reporting Layer

Two in-memory models — `TestSuite` and `NavGraph` — and five renderers.

- **Markdown** — one section per page, tables per test case. Human review artifact.
- **JSON** — full fidelity including selectors and source page URL. Machine-readable.
- **Excel/CSV** — one row per *step*, with Test ID / Category / Preconditions repeated on the group's first row. This is the shape TestRail, Zephyr, and Xray import cleanly.
- **Navigation graph** — `navgraph.json` (nodes + edges with verified locators), `navgraph.mmd` (Mermaid, renders in GitHub/VS Code), `navgraph.dot` (Graphviz), and `navgraph-paths.json` (entry → every node). See [CRAWLING_AND_EXTRACTION.md §4](CRAWLING_AND_EXTRACTION.md#4-the-navigation-graph).
- **Manifest** — `run_manifest.json`, the audit trail: every skipped element with its reason, blocked mutations, boundaries, budget status, token usage.

The navigation graph is a byproduct of the crawl rather than extra work — the crawler already computes states and transitions. It earns its place twice: it lets the LLM cite **real reachability paths** in preconditions instead of guessing them, and it is the substrate that makes executable-script generation a mechanical transform later (§9).

---

## 3. Element extraction on React apps

You raised this specifically. React ships obfuscated class names (`css-1x7k2p`), no stable IDs, and portals that render modals outside the component tree. Three techniques compensate; we run the first two, and deliberately skip the third.

### 3.1 Accessibility tree — the primary signal

Playwright's `page.accessibility.snapshot()` returns a role/name tree derived from the browser's own a11y computation. This is framework-agnostic — it does not care that React rendered it, and it survives class-name obfuscation entirely.

It also maps directly onto how a human tester writes a step. `{role: "button", name: "Save changes"}` becomes *"Click the 'Save changes' button"* with no translation layer.

### 3.2 DOM walk + selector synthesis — for reproducibility

The a11y tree tells us *what* is there; it does not give us a locator a test can replay. So we walk the DOM in parallel for every interactive node (`a`, `button`, `input`, `select`, `textarea`, `[role]`, `[onclick]`, `[tabindex]`, `[contenteditable]`) and synthesize a locator using a strict preference ladder:

1. `data-testid` / `data-test` / `data-cy` — author-declared, most stable
2. `id`, if it does not look generated (rejects `:r3:`, `ember42`, long hex/UUID)
3. `getByRole(role, name=...)` — the a11y pair, Playwright-native
4. `getByLabel` / `getByPlaceholder` — good for form fields
5. Scoped CSS path from the nearest stable ancestor, with obfuscated classes stripped
6. Ordinal fallback (`nth`), flagged `low_confidence` in the output

Each synthesized locator is **verified before it is recorded**: we resolve it and assert it matches exactly one element. A locator that resolves to zero or many is downgraded to the next rung. This is what stops the tool from emitting test steps that look plausible and fail on first run.

### 3.3 React Fiber introspection — deliberately excluded

We could read `__reactFiber$*` to recover component names like `PaymentForm`. We are not doing it: it breaks on production builds, shifts between React versions, and is absent behind Preact/Solid/Vue. The a11y role + accessible name already gives us semantic identity that is stable across all of them.

### 3.4 Settling — the SPA timing problem

A React route change resolves no network request and fires no `load` event. Waiting for `networkidle` alone either returns too early (before hydration) or never (with polling/websockets). Our settle routine:

1. `wait_for_load_state("domcontentloaded")`
2. Race `networkidle` against a hard `settle_timeout_ms` cap
3. Poll the interactive-element signature every 150 ms; consider it settled when unchanged across two consecutive polls, or the cap expires

Bounded, framework-agnostic, no `sleep()`.

---

## 4. Loop prevention — the core problem

You flagged this as the main task, and it is the part of the design that carries the most weight. Naive crawlers break on modern apps in four specific ways.

| Failure | What happens | Why URL-only visited-sets fail |
|---|---|---|
| In-place modal | Click "Edit" → dialog opens, URL unchanged | Fingerprint identical → never explored |
| Self-referential nav | Click "Home" while on Home | Re-queues the current state forever |
| New tab / popup | `target=_blank` or `window.open` | Escapes the crawler's page handle |
| Template explosion | `/product/1` … `/product/9000` | 9000 near-identical states crawled |

### 4.1 The composite fingerprint

A state is identified by the hash of two parts:

```
fingerprint = sha256( normalize_url(url) || interactive_signature(dom) )
```

**`normalize_url`** — lowercase scheme/host, drop the fragment unless it is a hash route, drop tracking params (`utm_*`, `gclid`, `fbclid`, `ref`), sort remaining params, strip trailing slash, and **replace numeric/UUID path segments with `{id}`**. That last rule is what collapses `/product/1` … `/product/9000` into a single `/product/{id}` state. It is also the rule most likely to need per-site tuning, which is why it is configurable.

**`interactive_signature`** — the sorted, deduplicated set of `(role, accessible_name, enabled)` triples for every interactive element currently visible, hashed. Visible only: an element behind `display:none` is not part of the current state. Text content is *not* included — otherwise a rendered timestamp or a live counter makes every poll a new state.

This composite catches both failure directions:

- **Same URL, different DOM** → different fingerprint → the modal *is* explored. Fixes failure #1.
- **Different URL, same DOM** → same fingerprint → templated pages collapse. Fixes failure #4.

### 4.2 Popup and tab handling

> **"Popup" is six different things, not one.** In-DOM overlays, new browser tabs, native JS dialogs (`alert`/`confirm`/`beforeunload`), file choosers, downloads, and permission prompts each need a different Playwright API — and two of them (`filechooser`, `beforeunload`) **hang the crawl** rather than erroring when unhandled. The full taxonomy and handler for each is [CRAWLING_AND_EXTRACTION.md §2](CRAWLING_AND_EXTRACTION.md#2-popups-and-overlays--six-kinds-six-handlers). This section covers only the new-tab case.

The `BrowserContext` gets a `page` event handler at startup, so nothing escapes:

- New page opens → fingerprint it. If unseen and in-scope, enqueue it as a normal frontier state, then **close the tab**. The crawler never holds more than one active page.
- Out-of-origin popup (OAuth, payment, third-party widget) → record it as a `boundary` observation with its origin, close it, and continue. Boundaries are valuable QA signal in their own right, so they appear in the output rather than being silently dropped.
- `window.open` is additionally shimmed via `add_init_script` so the URL is captured even if the browser suppresses the popup.

### 4.3 Budgets — the guarantee of termination

Fingerprinting handles the common cases. Budgets handle the ones nobody predicted. Every one of these is a hard stop:

| Budget | Default | Guards against |
|---|---|---|
| `max_pages` | 25 | Unbounded frontier growth |
| `max_clicks` | 200 | Deep in-page interaction trees |
| `max_wall_clock_seconds` | 900 | Slow pages, hung requests |
| `max_clicks_per_state` | 30 | One page with 500 buttons |
| `max_depth` | 1 | Crawling the whole internet |
| `max_consecutive_no_new_states` | 20 | Live-updating widgets that churn the fingerprint |

The crawl terminates when the frontier is empty **or** any budget is exhausted — whichever comes first. There is no code path where it does not terminate. That is the property you asked for.

### 4.4 Worked trace

```
enqueue  /dashboard                                    fp=a1b2 depth=0
visit    /dashboard → 14 interactive elements
click    "Settings" (link)   → /settings               fp=c3d4  NEW    enqueue
back     → /dashboard                                  fp=a1b2  seen
click    "Edit profile"      → /dashboard (modal open) fp=e5f6  NEW    enqueue
esc      → /dashboard                                  fp=a1b2  seen
click    "Home"              → /dashboard              fp=a1b2  seen   skip ◀ loop broken
click    "Docs" (_blank)     → popup docs.example.com  out-of-origin   record + close
click    "Delete account"                              DENY-LIST       skip, log
budget   clicks 14/200 · pages 1/25 · elapsed 11s
```

---

## 5. Interaction safety

Safe-click, as agreed. Enforced in three independent layers, because one is not enough.

### 5.1 Deny-list (pre-click)

An element is skipped if its accessible name, `aria-label`, or visible text matches a destructive term, or if it matches a denied selector. Config-extensible per site. Every skip is logged with its reason so a review can confirm nothing important was silently dropped.

### 5.2 Form policy

Forms are **analyzed, never submitted**. Field inventory — name, type, `required`, `pattern`, `min`/`max`, `maxlength`, `aria-invalid`, associated label — is extracted statically and handed to the LLM, which generates form-filling and validation test cases from the *schema* rather than from a live submission. This is the correct trade: submitting a real form on a live app is exactly the mutation we promised not to make, and the field metadata is sufficient to write good negative and edge-case tests without it.

### 5.3 Network write-guard (the backstop)

A Playwright `route` handler aborts every non-GET request (`POST`/`PUT`/`PATCH`/`DELETE`) that the page attempts, regardless of what triggered it. If a click slips past the deny-list — a mislabeled button, an unlabeled icon, a handler that fires on hover — the mutation still does not reach the server. Aborted requests are logged as `blocked_mutation` observations, which double as useful test-case input.

Defense in depth: label-based filtering catches intent, network filtering catches consequence.

---

## 6. Data model

```python
class Category(StrEnum):
    HAPPY_PATH = "Happy Path"
    NEGATIVE = "Negative"
    EDGE_CASE = "Edge Case"
    UI_UX = "UI/UX"
    FORM_FILLING = "Form Filling"

class Step(BaseModel):
    step_number: int
    action: str                       # "Click the 'Save changes' button"
    expected_result: str              # per-step expected outcome

class TestCase(BaseModel):
    test_id: str                      # TC_001
    category: Category
    preconditions: list[str]
    steps: list[Step]
    overall_expected_result: str
    source_url: str                   # provenance
    source_selectors: list[str]       # provenance — validated against PageModel

class TestSuite(BaseModel):
    target: str
    generated_at: datetime
    cases: list[TestCase]
```

The navigation graph is a parallel model over the same crawl:

```python
class NavNode(BaseModel):      # a distinct application state
    id: str                    # N001
    fingerprint: str
    url: str
    node_type: Literal["page", "modal", "drawer", "dropdown",
                       "panel", "boundary", "external"]
    depth: int

class NavEdge(BaseModel):      # an action that moves between states
    source: str; target: str
    action: Literal["navigate", "click", "type", "select",
                    "press_enter", "check", "hover"]
    label: str                 # "Click 'Save changes'"
    selector: str              # verified locator — the codegen payload
    outcome: Outcome
    annotations: list[str]     # mutating │ confirmation_required │ upload │ error
```

Full definitions in [CRAWLING_AND_EXTRACTION.md §4.1](CRAWLING_AND_EXTRACTION.md#41-model).

This mirrors your required format exactly. `source_url` and `source_selectors` are additions — they are what make the Validator's anti-hallucination check possible, and they let a reviewer trace any test case back to the element that produced it.

---

## 7. Failure handling

| Failure | Behavior |
|---|---|
| Auth state expired | Detected via `verify_selector` before crawling. Abort with a clear message — never crawl a login wall and generate 40 test cases for a login form you did not intend to test. |
| Page timeout | Record partial `PageModel`, mark `incomplete`, continue |
| Element detaches mid-click | Catch, re-fingerprint, continue (normal in React) |
| LLM rate limit / 5xx | SDK retries with backoff; on exhaustion, mark that page ungenerated and continue |
| Validation failure | One repair round-trip with the specific violations; if it still fails, emit with a `needs_review` flag rather than dropping |
| Zero interactive elements | Emit a UI/UX-only test case; do not fail the run |

Partial output always beats no output. A crawl that dies at page 18 of 25 still writes the 17 pages it completed.

---

## 8. Project layout

```
qagen/
├── cli.py                  # typer entry point
├── config.py               # pydantic-settings models
├── orchestrator.py         # run lifecycle, budget ownership
├── browser/
│   ├── session.py          # Playwright lifecycle, storage_state, write-guard
│   ├── analyzer.py         # a11y snapshot + DOM walk → PageModel
│   ├── selectors.py        # selector synthesis ladder + verification
│   ├── crawler.py          # BFS frontier, safe-click, popup handling
│   ├── fingerprint.py      # normalize_url + interactive_signature
│   └── policy.py           # deny/allow evaluation
├── generation/
│   ├── summarizer.py       # PageModel → compact prompt block
│   ├── adapter.py          # LLMAdapter protocol
│   ├── claude.py           # default provider, structured outputs
│   ├── prompts.py          # cacheable system prompt
│   └── validator.py        # uniqueness, coverage, anti-hallucination
├── models.py               # TestCase, Step, PageModel, TestSuite
└── report/
    ├── markdown.py
    ├── json_out.py
    └── excel.py
```

---

## 9. Deliberately out of scope

Named explicitly so scope stays where we agreed:

- **Executable test scripts** (runnable Playwright/Selenium code) — this tool writes test *cases*, not test *scripts*. The navigation graph we now emit (§2.4) is deliberately the substrate for this: each edge already carries a verified locator and a concrete action, so path → script is a mechanical transform. It is deferred because script generation needs an assertion strategy, test-data/fixture management, and a page-object decision — each its own design conversation. Emitting the graph now means that conversation can happen later without re-crawling.
- Visual regression / screenshot diffing
- Cross-browser matrix execution
- Performance or accessibility auditing (Lighthouse, axe)
- Authenticated multi-role crawling in one run — one `storage_state` per run
- Test management tool API integration (we export importable files; we do not push)

---

## 10. Where I'd expect tuning

Being upfront about the parts that will need iteration on a real target, rather than presenting the design as finished:

1. **`normalize_url` ID collapsing** — the `{id}` rule is a heuristic. A site with meaningful numeric routes (`/year/2024`) will over-collapse and need a config exception.
2. **Deny-list coverage** — icon-only buttons with no accessible name are invisible to text matching. The network write-guard is what protects us there, which is exactly why it is not optional.
3. **Settle heuristic** — apps with permanent polling never reach `networkidle`. The signature-stability poll handles it, but the timeout may need raising on slow apps.
4. **Prompt cost at scale** — 25 pages × ~4 KB summaries is cheap with caching. A 200-page crawl would want summary batching, which is a straightforward later addition.
