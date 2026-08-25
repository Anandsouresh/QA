# QAGen — Implementation Flow

Companion to [ARCHITECTURE.md](ARCHITECTURE.md). That document says *what the system is*; this one says *what happens, in order, and in what sequence we build it*.

> [CRAWLING_AND_EXTRACTION.md](CRAWLING_AND_EXTRACTION.md) expands Phases 4–5 into a nine-step state machine, defines the six overlay kinds and the nine click outcomes, specifies the navigation graph, and gives the full per-phase I/O contract table (§5 there). Read it alongside Part A; it supersedes this document on crawl detail.

---

## Part A — Runtime flow

### A.0 End-to-end sequence

```
CLI ──▶ Config ──▶ Session ──▶ Auth verify ──▶ Crawl loop ──▶ Generate ──▶ Validate ──▶ Report
                                    │              │
                                    │              └── per state: analyze → fingerprint → click → enqueue
                                    └── abort early if auth is dead
```

Nine phases follow. Each states its inputs, what it does, and its exit condition.

---

### Phase 1 — Config resolution

**In:** CLI args + YAML file · **Out:** validated `RunConfig`

1. Parse CLI (`--url`, `--config`, `--depth`, `--out`).
2. Load YAML; CLI values override file values.
3. Validate through pydantic. Reject early on: unreachable `storage_state` path, `depth < 0`, empty `output.formats`, unknown `llm.provider`.
4. Resolve the LLM credential. Claude resolves via the standard chain (`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or an `ant auth login` profile) — a zero-arg client picks up whichever is present, so an unset env var is not by itself an error.
5. Create `output.dir`; write `run_manifest.json` (config snapshot, timestamp, tool version) for reproducibility.

**Exit:** valid config, or a clear error naming the offending field. No browser has launched yet — config errors must never cost a browser start.

---

### Phase 2 — Session bring-up

**In:** `RunConfig` · **Out:** live `BrowserContext`

1. Launch Chromium (headless by default; `--headed` for debugging).
2. Build the context with `storage_state=<auth file>`, a fixed viewport (1440×900), and a fixed user agent — both fixed so fingerprints are reproducible across runs.
3. Install the **network write-guard**: a `context.route("**/*")` handler that aborts every non-GET request and records it as a `blocked_mutation`.
4. Install the **popup handler**: `context.on("page", ...)` so tabs opened by any means land in the crawler's hands (§A.5).
5. Install `add_init_script` shimming `window.open` to record-and-suppress.

**Exit:** a context that is authenticated, instrumented, and incapable of mutating the target.

**Note on the cookie file.** Playwright's native `storage_state` JSON is accepted as-is. A raw cookie-array export (EditThisCookie and similar) is normalized into that shape first: map `expirationDate → expires`, `sameSite` values to Playwright's casing, and wrap in `{"cookies": [...], "origins": []}`. Both forms are detected by inspecting the top-level JSON type, so the user does not have to declare which one they have.

---

### Phase 3 — Auth verification

**In:** context · **Out:** go / no-go

1. Navigate to `target.url`.
2. If `auth.verify_selector` is set, wait for it (5 s cap). Present → authenticated.
3. If absent, or the final URL matches a login-page heuristic (`/login`, `/signin`, `/auth`), **abort the run**.

This gate exists because of a specific failure mode worth naming: an expired cookie silently redirects to the login page, the crawler happily explores it, and the tool confidently emits 40 test cases for a login form the user never asked about. Failing loudly here is much better than succeeding wrongly.

**Exit:** confirmed authenticated session, or abort with `AUTH_FAILED` and remediation text ("re-export your cookies / re-run the login recorder").

---

### Phase 4 — Crawl loop

The heart of the tool. Frontier is a FIFO deque of `(url, depth, arrival_action)`.

```
frontier ← [(target.url, 0, "initial navigation")]
seen     ← {}                       # fingerprint → StateRecord
pages    ← []

while frontier and not budgets.exhausted():
    url, depth, arrival = frontier.popleft()

    ── 4.1 Navigate ──────────────────────────────────────────────
    goto(url); settle()                       # §A.4.1
    if out_of_scope(page.url): continue       # origin / include / exclude

    ── 4.2 Analyze ───────────────────────────────────────────────
    model = analyze(page)                     # a11y + DOM  → PageModel

    ── 4.3 Fingerprint ───────────────────────────────────────────
    fp = fingerprint(page.url, model)
    if fp in seen:
        seen[fp].hit_count += 1
        continue                              # ◀ loop broken here
    seen[fp] = StateRecord(fp, url, depth, arrival)
    pages.append(model)

    ── 4.4 Enqueue links ─────────────────────────────────────────
    if depth < config.depth:
        for href in same_origin_links(model):
            frontier.append((href, depth + 1, f"navigate to {href}"))

    ── 4.5 Safe-click in-page elements ───────────────────────────
    for el in clickable(model)[:max_clicks_per_state]:
        if policy.denies(el):
            log_skip(el, policy.reason); continue
        if not budgets.take_click(): break

        before = fp
        click(el); settle()

        if page.url_changed() or fingerprint_changed():
            new_fp = fingerprint(page.url, analyze(page))
            if new_fp not in seen:
                frontier.append((page.url, depth, f"click '{el.name}'"))
            restore(before)                   # §A.4.2
```

#### A.4.1 `settle()`

```
wait_for_load_state("domcontentloaded")
race(networkidle, timeout=settle_timeout_ms)
poll interactive-signature every 150ms
  → settled when unchanged twice in a row, or cap reached
```

No fixed `sleep()`. Handles hydration, lazy routes, and permanently-polling apps alike.

#### A.4.2 `restore(fingerprint)` — returning to a known state

Attempted in order, cheapest first, stopping at the first that lands on the target fingerprint:

1. Press `Escape` — closes most modals, dropdowns, and drawers
2. `page.go_back()` — if history advanced
3. `page.goto(state.url)` + settle — hard reset

If none restores the target fingerprint, the current state is re-fingerprinted and treated as a fresh state. A failed restore never aborts the crawl.

#### A.4.3 Budget accounting

Every navigation, click, and second is debited from `budgets` before it happens. Exhaustion sets a flag the loop checks each iteration; the run finishes cleanly with partial results and a `budget_exhausted` note in the manifest. The crawl has no path that does not terminate — this is the property the whole design is organized around.

---

### Phase 5 — Overlay, popup and dialog handling

Six distinct kinds, six handlers — all armed at session bring-up, all firing asynchronously rather than being tied to a particular click. Full detail in [CRAWLING_AND_EXTRACTION.md §2](CRAWLING_AND_EXTRACTION.md#2-popups-and-overlays--six-kinds-six-handlers).

| Kind | API | Handling |
|---|---|---|
| In-DOM overlay (modal, drawer, dropdown, toast) | none — DOM diff | New state if persistent; toasts/tooltips excluded from the fingerprint |
| New tab / window | `context.on("page")` | Below |
| Native dialog (`alert`/`confirm`/`prompt`/`beforeunload`) | `page.on("dialog")` | Record, then dismiss (accept `beforeunload`) |
| File chooser | `page.on("filechooser")` | Record `accept`/`multiple`, then `set_files([])` |
| Download | `page.on("download")` | Record, then `cancel()` |
| Permission prompt | `permissions=[]` at context creation | Never appears |

**The last three are not optional.** An unhandled `filechooser` makes the click hang until timeout, and an unhandled `beforeunload` blocks navigation — both present as unexplained crawl stalls, not errors.

New tabs specifically:

```
on new page:
    wait for its first navigation (2s cap)
    if same origin and in scope:
        fingerprint it → enqueue if new
    else:
        record boundary observation (origin, trigger element)
    close the page
```

The crawler therefore never juggles more than one live page. This single handler covers `target=_blank`, `window.open`, and JS-initiated tabs identically, which is why failure mode #3 from the architecture doc does not need its own special-casing.

---

### Phase 6 — Page summarization

**In:** `PageModel[]` · **Out:** compact prompt block per page

Each `PageModel` compresses into roughly 2–5 KB, structured and deterministically ordered:

```
URL: /settings/profile          (reached by: click 'Settings')
TITLE: Account Settings

LANDMARKS: navigation(main), main, complementary(sidebar)

INTERACTIVE:
  button   "Save changes"     [data-testid=save-profile]     enabled
  button   "Cancel"           getByRole(button,name=Cancel)  enabled
  button   "Delete account"   [data-testid=danger-delete]    enabled  DENIED
  link     "Billing"          → /settings/billing
  checkbox "Email me updates" #notify-email                  unchecked

FORMS:
  form#profile-form (POST /api/profile)
    input  name=fullName  type=text   required  maxlength=64   label="Full name"
    input  name=email     type=email  required  pattern=...    label="Email"
    select name=timezone  required  options=38                 label="Timezone"

BOUNDARIES: popup → accounts.google.com (from 'Connect Google')
BLOCKED:    POST /api/profile (write-guard)
```

Two design points worth stating:

- **Ordering is deterministic** — sorted by role then name. Non-deterministic ordering would silently break prompt caching, which is most of the cost saving on a multi-page run.
- **Denied and blocked items are included, not hidden.** A "Delete account" button the crawler refused to click is still excellent input for a negative/confirmation test case. Withholding it would make the output worse, not safer.

---

### Phase 7 — Test-case generation

One LLM call per page. Claude is the default adapter.

1. **System prompt** (stable, cached): the QA persona, the five category definitions, the required output structure, and the hard rules — *only reference elements present in the supplied inventory; never invent selectors; number steps from 1; write each expected result as observable behavior, not implementation.*
2. **User message** (volatile): the page summary block from Phase 6.
3. **Structured output**: `output_format=TestCaseBatch` via `client.messages.parse()`, so the response is a validated Pydantic instance rather than prose to be parsed. Schema violations become an API-level failure instead of a silent downstream one.
4. **Adaptive thinking** at `effort: high` — category coverage and negative-path reasoning benefit from it, and this is a per-page call, not a hot loop.
5. Retries on transient errors are handled by the SDK's built-in backoff.

**Category targeting.** The prompt requests all five categories per page, with the count scaled to what the page actually offers: a page with a form should produce Form Filling and Negative cases; a static informational page legitimately produces mostly UI/UX. We do not force a fixed count per category — quotas produce padding, and padded test cases are what makes a QA suite untrustworthy.

---

### Phase 8 — Validation

Schema conformance is already guaranteed. This phase enforces what a schema cannot:

| Check | Rule | On failure |
|---|---|---|
| ID uniqueness | `TC_001`…`TC_NNN`, globally unique | Renumber |
| Step contiguity | Steps number 1..N with no gaps | Renumber |
| Non-empty | ≥1 step; every step has action + expected | Repair round-trip |
| Category validity | One of the five enum values | Guaranteed by schema |
| Coverage | ≥3 distinct categories across the suite | Warn (not fatal) |
| **Selector grounding** | Every `source_selector` exists in the source `PageModel` | Repair round-trip |
| Precondition sanity | Non-empty for non-trivial cases | Warn |

**Selector grounding is the important one.** It is the check that catches a plausible-looking but fabricated test case — a step referencing a button that was never on the page. A single repair round-trip is attempted with the specific violations named; if it still fails, the case is emitted with `needs_review: true` rather than dropped. A flagged case a reviewer can reject is more useful than a silently missing one.

---

### Phase 9 — Report generation

One `TestSuite`, three renderers, written to `output.dir`.

**`test-cases.md`** — grouped by source page, one table per test case. The review artifact.

```markdown
### TC_004 — Reject invalid email format
**Category:** Negative
**Preconditions:** User is logged in · Profile settings page is open

| # | Action | Expected Result |
|---|--------|-----------------|
| 1 | Clear the "Email" field | Field is empty; no error shown yet |
| 2 | Enter `not-an-email` | Field accepts the text |
| 3 | Move focus out of the field | Inline validation message appears |

**Overall Expected Result:** The form blocks submission and shows a
format-specific validation message on the Email field.
```

**`test-cases.json`** — full fidelity: every field of `TestCase`, plus `source_url` and `source_selectors`. This is the downstream-tooling format.

**`test-cases.xlsx`** (and `.csv`) — **one row per step**, which is what TestRail / Zephyr / Xray import cleanly:

| Test ID | Category | Preconditions | Step # | Action | Step Expected Result | Overall Expected Result |
|---|---|---|---|---|---|---|
| TC_004 | Negative | User is logged in… | 1 | Clear the "Email" field | Field is empty… | The form blocks submission… |
| TC_004 | | | 2 | Enter `not-an-email` | Field accepts the text | |
| TC_004 | | | 3 | Move focus out | Validation message appears | |

Group-level columns repeat only on the first row of each group — the convention those tools expect.

**`navgraph.json` / `.mmd` / `.dot` / `navgraph-paths.json`** — the application's state graph. Nodes are distinct states, edges are actions carrying verified locators. `navgraph-paths.json` (entry → every node) feeds Phase 6, so preconditions cite real reachability paths rather than guesses. The Mermaid file renders directly in GitHub and VS Code with no tooling. See [CRAWLING_AND_EXTRACTION.md §4](CRAWLING_AND_EXTRACTION.md#4-the-navigation-graph).

**`run_manifest.json`** — pages crawled, states seen, clicks made, elements denied (with reasons), mutations blocked, boundaries hit, budget status, token usage, wall-clock. This is the audit trail that answers "why didn't it test X?" without a re-run.

---

## Part B — Build sequence

Seven milestones. Each ends at something runnable, so progress is verifiable rather than assumed.

### M1 — Skeleton and config
Package layout, `RunConfig` models, CLI wiring, manifest output.
**Done when:** `qagen run --url X --config site.yaml` validates the config and writes an empty manifest. No browser yet.

### M2 — Session, auth, and all six overlay handlers
Playwright bring-up, `storage_state` loading (both formats), write-guard, **all six overlay handlers** (Phase 5), auth verification.
**Done when:** the tool logs into a real authenticated page, confirms `verify_selector`, and exits cleanly. Verify the write-guard by watching a POST get aborted, and verify the `filechooser` and `dialog` handlers explicitly against the fixture app — those two are the ones whose absence causes hangs rather than errors, so they must be proven, not assumed.

### M3 — Page analysis and classification
A11y snapshot, DOM walk, **the element classification cascade** (CRAWLING §1.2), **two-pass form detection** (§1.3), field extraction with label ladder and constraint capture, search-control detection, selector-synthesis ladder with verification, settle routine.
**Done when:** given a URL, the tool dumps a `PageModel` where **every** synthesized selector resolves to exactly one element, React forms built without a `<form>` tag are detected as inferred clusters, and every field carries its constraints. This is the milestone with the most React-specific work — budget accordingly.

### M4 — Fingerprinting, crawl, and navigation graph
`normalize_url`, `interactive_signature` (with transient overlays excluded), `StateRegistry`, the 4A–4J state machine, ranked action planning, the nine-outcome classifier, search probing, `restore()`, budgets — and `NavGraph` assembly with all four graph artifacts.
**Done when:** every loop failure mode is provably handled on the fixture app. Test each explicitly: open a modal (new state, explored), click the current nav item (skipped), open a `_blank` link (captured and closed), crawl a templated list (collapsed to one state), trigger a `confirm()` (recorded and dismissed), click a file input (dismissed, not hung), let a toast fire (fingerprint unchanged), and probe a search box (probed once, results collapsed). The emitted `navgraph.mmd` should render and visibly match the fixture's real structure — that visual check catches fingerprinting bugs faster than any assertion. **This is the milestone the whole tool is judged on.**

### M5 — LLM generation
Summarizer, `LLMAdapter` protocol, Claude implementation with structured outputs and prompt caching, prompt authoring.
**Done when:** one page produces schema-valid test cases across ≥3 categories, and `usage.cache_read_input_tokens` is non-zero on the second page — proof the caching is actually working rather than just configured.

### M6 — Validation and reporting
Validator rules, repair round-trip, five renderers (md / json / xlsx+csv / graph / manifest), manifest enrichment.
**Done when:** a full run produces the complete output set (Flow §9 / CRAWLING §5.1), the Excel imports into a test management tool without hand-editing, and `navgraph.mmd` renders correctly.

### M7 — Hardening
Failure paths from ARCHITECTURE §7, deny-list tuning against the target, budget defaults tuned to observed timings, docs.
**Done when:** a run survives a mid-crawl page timeout and an LLM rate-limit without losing completed work.

---

## Part C — Testing the tool itself

QA tooling that is not itself tested is a hard sell. Three layers:

**Unit — pure functions, no browser.**
`normalize_url` (ID collapsing, param stripping, hash routes) · `interactive_signature` (ordering stability, visibility filtering) · selector-ladder preference order · deny-list matching · budget arithmetic.

**Integration — local fixture app.**
A small React app checked into the repo, deliberately containing every hazard the design claims to handle — one fixture element per claim, so no claim goes unverified:

| Hazard | Verifies |
|---|---|
| Modal that does not change the URL | Composite fingerprint catches in-page states |
| Self-referential nav link | Loop termination |
| `target=_blank` link + `window.open` button | Both new-tab paths |
| Templated list route (`/item/1..50`) | `{id}` collapsing |
| `confirm()` on delete | Native dialog handler |
| `<input type=file>` | File-chooser handler — **the hang case** |
| Download link | Download handler |
| Toast that auto-dismisses | Transient exclusion from fingerprint |
| Cookie consent banner | 4B reconciliation |
| Form with no `<form>` tag | Inferred form clusters |
| Form with `pattern`/`maxlength`/`autocomplete` | Constraint + semantic-hint extraction |
| Search box with live suggestions | Search probe, probed once |
| `<div onClick>` with no label | `INFERRED_CLICKABLE` + write-guard backstop |
| Permanently-polling widget | Settle heuristic |

Every crawler behavior is asserted against this fixture. It is deterministic and offline, so these tests run in CI with no network and no live target.

**Contract — LLM layer with a stub adapter.**
A `StubAdapter` returning canned `TestCaseBatch` objects lets the Validator and all three renderers be tested with zero API calls and zero flake. A single live Claude smoke test runs separately, outside the fast suite.

---

## Part D — Open items for you

Nothing here blocks the build; each is a value I would rather confirm than guess, and each has a working default so the answer can arrive late.

1. **Target site for M4 validation.** The fixture app covers the known hazards, but tuning `normalize_url` and the deny-list needs the real thing. Access to a staging environment would sharpen this considerably.
2. **`{id}` collapsing exceptions.** If the target has meaningful numeric routes (`/year/2024`, `/v2/api`), the default rule over-collapses them. A list of exception patterns fixes it.
3. **Test ID continuity across runs.** Currently `TC_001` restarts each run. If these feed a tracking system, a persistent counter or a URL-derived ID scheme would be better — say the word and it goes into M6.
4. **Budget defaults.** 25 pages / 200 clicks / 15 minutes is a deliberately conservative first pass. Real timings from M4 will tell us where they should actually sit.

---

## Summary

| Question you raised | Where it is answered |
|---|---|
| React element extraction | ARCHITECTURE §3 — a11y tree primary, DOM walk + verified selector synthesis for reproducibility, Fiber deliberately excluded |
| Cookie-based auth | ARCHITECTURE §2.2, Flow Phase 2–3 — `storage_state` with both formats accepted, plus a hard auth gate before crawling |
| **Crawl loops** | ARCHITECTURE §4, Flow Phase 4 — composite fingerprint (URL + interactive signature), same-URL-modal and different-URL-same-template both handled, plus hard budgets guaranteeing termination |
| **Popups / new tabs** | ARCHITECTURE §4.2, Flow Phase 5 — single context-level handler, captured and closed, never juggling live pages |
| Required test-case format | ARCHITECTURE §6, Flow Phase 9 — data model mirrors your spec exactly; Excel is one row per step |
| **Does Playwright know it's a form?** | CRAWLING §0 and §1.2–1.3 — no, it has no semantics. A rule cascade over the a11y tree + DOM produces typed elements with confidence levels; forms are detected in two passes because React usually omits `<form>` |
| **What exactly gets extracted** | CRAWLING §1 — classified elements, explicit + inferred forms, per-field constraints and `autocomplete` hints, search controls, overlays, network endpoints, console errors |
| **Search boxes** | CRAWLING §3.6 — dedicated probe, once per state, results template-collapsed |
| **Navigation graph** | CRAWLING §4 — nodes + edges with verified locators; `navgraph.json/.mmd/.dot/-paths.json`; the substrate that makes codegen mechanical later |
| **Per-phase input/output** | CRAWLING §5 — contract table for all 9 phases plus the 10 crawl sub-phases |
