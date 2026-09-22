# Build prompt — QAGen Control Room

**Audience: an AI coding agent (or a developer) starting cold on this repository.**
Paste this whole file as the opening prompt. It is self-contained: it describes
what already exists, what to build, which stack to use and why, and where the
work stops.

Companion design canvas (four screens, drawn to scale):
`QAGen Control Room` — see the artifact link in the conversation that produced
this file.

---

## 0. The one-paragraph version

QAGen is a working Python CLI that crawls a live web application read-only and
writes QA test cases grounded in what was actually on screen. It works. What it
lacks is a face: a crawl of a real app runs for five hours and shows you a Rich
table at the end. Build a web control room around the existing package — a
FastAPI service that owns run lifecycle plus a React front end that makes a
long crawl legible while it happens. **Do not rewrite the crawler, the graph
builder, the generator or the validator.** They are the product. You are
building the room they run in.

---

## 1. What already exists — read before writing anything

Install and run it once before you touch code. It is the fastest way to
understand what you are wrapping:

```bash
pip install -e .
python -m playwright install chromium
python -m http.server 8899 --directory tests/fixture &
qagen run --url http://127.0.0.1:8899/index.html --depth 1 --provider stub --out ./demo-out
```

Then read, in this order: `README.md`, `ARCHITECTURE.md`,
`CRAWLING_AND_EXTRACTION.md`, `MODULE_CRAWL_PLAN.md`.

### The package

| Path | What it is |
|---|---|
| `qagen/cli.py` | Typer app. Commands: `run`, `crawl`, `generate`, `validate-config`. |
| `qagen/config.py` | `RunConfig` — a Pydantic v2 tree of `target` / `auth` / `crawl` / `interaction` / `llm` / `output` / `browser`. Loads YAML, applies dotted CLI overrides. |
| `qagen/orchestrator.py` | `Orchestrator(cfg, generate=True).run()` and `.generate_only(crawl)`. Async. Returns the run manifest as a dict. |
| `qagen/models.py` | Every data shape: `Element`, `FormSpec`, `PageModel`, `NavNode`, `NavEdge`, `NavGraph`, `Step`, `TestCase`, `TestSuite`. All Pydantic. |
| `qagen/browser/crawler.py` | The crawl loop — frontier, fingerprinting, action planning, restore. ~1500 lines. Leave it alone. |
| `qagen/browser/session.py` | Playwright context, cookie loading, auth verification, the network write-guard. |
| `qagen/browser/actionlog.py` | Streaming log. Writes `crawl-log.jsonl` and `crawl-log.txt`, **flushed per line**. This is your live feed. |
| `qagen/graph/builder.py` | Builds `NavGraph` from crawl state; computes shortest paths from entry. |
| `qagen/generation/` | `adapter.py` (provider protocol), `claude.py`, `stub.py`, `summarizer.py`, `validator.py`, `from_disk.py` (`load_crawl`). |
| `qagen/report/` | `markdown.py`, `json_out.py`, `tabular.py` (xlsx/csv), `graph_html.py`. |

### The run directory is already the database

A finished run writes one self-describing directory. Treat it as the source of
truth and do not duplicate its contents into SQL:

```
<out_dir>/
├── run_manifest.json        config, auth status, budgets, skips, blocked writes, timings
├── crawl-log.jsonl          one JSON object per event, appended live
├── crawl-log.txt            same events, aligned for humans
├── navgraph.json            NavGraph — nodes, edges, boundaries, unexplored
├── navgraph-paths.json      entry → every node, shortest path
├── navgraph.mmd / .dot / .html
├── states.md                human-readable state inventory
├── pages/<fingerprint>.json PageModel per state — the full element inventory
├── artifacts/<Nxxx>_<fp>.png / .html   screenshot + raw DOM per state
└── test-cases.md / .json / .xlsx / .csv
```

### Facts that shape the design

- **A real crawl takes hours.** A recorded run: 175 states, 672 transitions,
  733 clicks, 17,605 seconds. Design for a five-hour job, not a request.
- **Crawl and generation are already separable.** `qagen generate --from <dir>`
  re-runs the LLM half against a finished crawl with no browser. Crawling is
  hours; generation is minutes. The UI must expose this split — it is the
  difference between a cheap iteration and an expensive one.
- **A "module" is the first path segment.** `/screen`, `/content`, `/settings`.
  `crawl.module_budgets` caps distinct states per module so one deep area cannot
  starve the others, and `target.include_paths` scopes a run to a single module.
  This concept already exists in the code; surface it, don't invent it.
- **Safety is three layers and one of them matters.** Deny-list, form policy,
  and the network write-guard that aborts every POST/PUT/PATCH/DELETE at the
  route layer. The UI must show the guard's state at all times and must never
  make `--allow-mutations` a one-click action.
- **Partial output beats no output.** The orchestrator already writes what it
  has when a crawl dies mid-run. Stop must preserve that property.

---

## 2. Tech stack, and why each piece

### Backend — FastAPI over the existing package

Not Flask, not Django, not a rewrite in Node.

- The orchestrator is already `async def`. FastAPI is async-native, so the
  crawl's own concurrency model carries straight through.
- **Every model is already Pydantic v2.** `RunConfig`, `NavGraph`, `PageModel`,
  `TestSuite` all serialize with `.model_dump(mode="json")`. Your response
  schemas are the domain models. There is no translation layer to write and
  none to keep in sync.
- `RunConfig.model_json_schema()` gives you the entire configuration schema for
  free. Serve it and let the front-end config form read it, so a new knob in
  `config.py` appears in the UI without front-end work.
- OpenAPI comes out of FastAPI automatically; generate the TypeScript client
  from it rather than hand-writing types.

### Run execution — subprocess per run, not Celery

Each run is a `qagen run --config <generated.yaml> --out <run_dir>` subprocess
supervised by the API.

- A crawl owns a Chromium instance. If it ran inside the API worker, an API
  restart would kill a four-hour job. A subprocess survives a reload and can be
  adopted again from its PID file.
- Celery or RQ means Redis, a broker, a worker pool and a deployment story, for
  a workload of at most a handful of concurrent runs on one machine. Add it only
  when you genuinely need multi-host scheduling.
- Write `<run_dir>/run.pid` and `<run_dir>/run.status.json` so the API can
  re-attach to running jobs after a restart.

### Live updates — Server-Sent Events, not WebSockets

The data flow is one-directional: server to browser. SSE is a `StreamingResponse`
in FastAPI, reconnects on its own, survives proxies, and needs no client
library. Control actions (pause, stop) are ordinary POSTs. Reach for WebSockets
only if you later add something the browser must push continuously.

Implement the stream by **tailing `crawl-log.jsonl`**. Do not add an in-process
callback into `ActionLog`. Tailing works across the process boundary you already
chose, survives an API restart mid-crawl, and lets a client replay from byte
zero to rebuild the whole run state. The file is flushed per line specifically
so this works.

### Persistence — SQLite for the index only

One small table of runs: `id`, `label`, `target_url`, `status`, `created_at`,
`finished_at`, `run_dir`, `pid`, plus a few denormalized counters for the history
list. Everything else stays in the run directory. Do not import graphs or test
cases into SQL; you will only build a slower copy of files that already parse in
milliseconds.

### Front end — React 18 + TypeScript + Vite

- **Graph rendering: React Flow (`@xyflow/react`)** with **elkjs** for layered
  layout. You need custom nodes carrying a screenshot thumbnail, a state ID and
  a coverage badge — React Flow makes that a component, whereas Cytoscape makes
  it a rendering hack. At 175 nodes and 672 edges, performance is comfortable.
- **Styling: Tailwind CSS + shadcn/ui.** Gives a dense, credible dashboard
  quickly, and every primitive is a file you own rather than a dependency you
  fight.
- **Server state: TanStack Query** for fetch-and-cache. The SSE stream writes
  into a small **Zustand** store for live run state. Keep those two separate —
  conflating them is the usual source of stale dashboards.
- **Tables: TanStack Table + TanStack Virtual.** A 1,200-case suite and an
  8,000-line event log both need virtualization.
- **Charts: Recharts** for budget and coverage; hand-written SVG for anything
  smaller. Do not pull in a charting framework for four progress bars.

Skip xterm.js. A styled, filterable event list beats a terminal emulator here —
the events are structured JSON, and throwing that structure away to render ANSI
text would be a regression.

### Rejected, and why

| Option | Why not |
|---|---|
| Next.js | You need a long-lived Python process and a static SPA. SSR buys nothing and adds a second runtime to deploy. |
| Electron / Tauri desktop app | The crawler is already headless and server-side. A browser client can run anywhere, including against a remote runner. |
| Streamlit / Gradio | Fine for a demo, wrong for a five-hour live job with a graph canvas and an inline review workflow. You will hit the wall in week two. |
| Rewriting the crawler in Node/Playwright-JS | Throws away the fingerprinting, budget and restore logic that is the hard-won part of this repo. |

---

## 3. Changes required inside `qagen/` — keep them small

Six changes. Each is additive and must leave the CLI behaviour identical.

1. **Live frames.** Add `output.live_frames_ms: int = 0` to `OutputConfig`
   (0 = off). When set, the crawler writes `<out_dir>/live.jpg` on that interval
   from the current page, atomically (write to `live.tmp.jpg`, then rename).
   This feeds the live viewport panel and is the single highest-impact change
   for making the system feel alive.

2. **Currently-exercising marker.** The crawler already logs an `action` event
   before each click and an `action_done` after. Add the state ID, element kind,
   accessible name, selector and the element's `location` string to a small
   `<out_dir>/live.json` written alongside, so a late-joining client can render
   the "now exercising" card without replaying the whole log.

3. **Graceful stop.** Each crawl iteration checks for `<out_dir>/STOP`. If
   present, break the loop with `stop_reason="stopped by operator"` and fall
   through to the existing write path. Never kill the process to stop a run —
   that discards the partial output the orchestrator is designed to preserve.

4. **Pause.** Same mechanism, with `<out_dir>/PAUSE`: the loop waits on the
   sentinel instead of breaking. Log `paused` and `resumed` events so the
   timeline shows the gap.

5. **Per-module counters in the budget snapshot.** `Budgets.snapshot()` should
   include `states_per_module: dict[str, int]` next to the existing totals. The
   crawler already computes the section grouping in `_section_of`; expose it.

6. **A module-discovery entry point.** A shallow function —
   `discover_modules(url, auth, timeout_s)` — that loads the entry page, reads
   same-origin links plus the `extra_clickable_selectors` targets, groups by
   first path segment and returns counts. This powers the config screen's
   "probe target" step. Thirty to sixty seconds, no full crawl.

Everything else the UI needs is already on disk.

---

## 4. API surface

```
GET    /api/config/schema              RunConfig.model_json_schema()
POST   /api/preflight/auth             verify a cookie/storage_state file → ok | AUTH_FAILED
POST   /api/preflight/modules          shallow module discovery (change 6)

POST   /api/runs                       body: RunConfig → writes config, spawns subprocess
GET    /api/runs                       list, newest first
GET    /api/runs/{id}                  status + run_manifest.json
POST   /api/runs/{id}/pause            touch PAUSE
POST   /api/runs/{id}/resume           remove PAUSE
POST   /api/runs/{id}/stop             touch STOP  (graceful; partial output is kept)
DELETE /api/runs/{id}                  delete the run directory (confirm in UI)

GET    /api/runs/{id}/events           SSE; ?from_byte= to replay
GET    /api/runs/{id}/live.jpg         latest frame
GET    /api/runs/{id}/live.json        current action + budget snapshot

GET    /api/runs/{id}/graph            navgraph.json
GET    /api/runs/{id}/paths            navgraph-paths.json
GET    /api/runs/{id}/states           node summaries
GET    /api/runs/{id}/states/{fp}      full PageModel
GET    /api/runs/{id}/artifacts/{name} screenshot / raw DOM

GET    /api/runs/{id}/cases            test-cases.json
PATCH  /api/runs/{id}/cases/{tc}       reviewer verdict: approved | rejected | edited
POST   /api/runs/{id}/generate         re-run generation from this crawl (no browser)
GET    /api/runs/{id}/export/{fmt}     md | json | xlsx | csv
```

Two rules:

- **`POST /api/runs` takes a `RunConfig`, not a bespoke body.** Validate with
  the existing model, write the YAML, spawn the CLI. One config shape across
  CLI and UI, forever.
- **Reviewer verdicts are a sidecar**, `<run_dir>/review.json`. Never rewrite
  `test-cases.json`; it is the generator's output and must stay reproducible.

---

## 5. The four screens

The canvas artifact draws all four to scale. Build them in this order.

### 5.1 New run

Configuration that reads as a plan, not a form dump.

- **Target and session.** URL, depth, and an auth file with a live verification
  badge. Verification is a real preflight call, not a checkbox — an expired
  cookie silently redirects to the login page and yields forty confident test
  cases for a login form nobody asked about. Show the result and the timestamp.
- **Modules and state budget.** After a probe, a row per discovered module:
  name, paths found, a state-budget number input, and a share bar. A running
  total that feeds `crawl.max_pages`. This is the screen's centre of gravity and
  the thing the user described wanting most — choosing how many states, per
  module, before a run starts.
- **Safety.** The write-guard shown as armed, with the deny-list visible and
  editable. `--allow-mutations` lives behind a typed confirmation, never a
  toggle.
- **Run plan card.** Host, module count, total states, wall-clock ceiling,
  model, output directory, and a duration estimate computed from the previous
  runs against that host. `Start crawl` and `Crawl only — skip generation`.

### 5.2 Live run — the screen that matters

This is what turns a silent five-hour process into a system you can watch.
Four regions, all fed by the SSE stream:

- **Live viewport.** The `live.jpg` frame in a browser chrome, with the control
  currently being exercised outlined and labelled. One frame per second is
  plenty. Nothing else you build will communicate "this is running" as
  immediately.
- **Now exercising.** State ID, action kind, element name, selector, human
  location, seconds elapsed, and position within the state's action plan.
- **Map so far.** The graph drawing itself as `state_found` events arrive, with
  the newest node ringed. Watching an application's map assemble is the most
  compelling thing this system does; give it room.
- **Budgets.** States, clicks, navigations and wall clock against their caps,
  plus a bar per module. When a run stops, the reason belongs here in plain
  language — a starved module is a configuration finding, not a failure.
- **Events.** The `crawl-log.jsonl` stream, virtualized, one colour per event
  class, filterable. Keep the raw detail string; it is what makes a stalled
  crawl diagnosable.

Top bar carries status, elapsed, estimated remaining, `Pause` and
`Stop & keep`. Say "keep" on the stop button — it is true, and it tells the
operator that stopping is safe.

### 5.3 Graph explorer

Post-crawl exploration of what was found.

- Canvas of states and transitions. Colour by module, shape or border by node
  type (page, modal, drawer, dropdown, boundary). Dashed edges for transitions
  recorded but not traversed.
- Filters: module, state type, has-unexercised-controls, blocked-a-write,
  partial-capture. The coverage filters are how a user finds the gaps.
- Inspector for the selected state: screenshot, counts, the exercised and
  skipped element lists with reasons, network observations, and the shortest
  path from entry rendered as a sequence of node IDs. Every edge on that path
  carries a locator that resolved to exactly one element at capture time — say
  so in the UI, because it is the reason the paths can be trusted.

### 5.4 Test cases

Review, not just display.

- Tree by module then state. Category filter chips. A prominent
  **needs review** filter — that flag is the quality signal the validator
  produces and it should never be buried.
- Case detail in the required QA shape: ID, category, preconditions, numbered
  steps with per-step expected results, overall expected result.
- **Evidence panel.** Show the source screenshot with boxes drawn over the
  elements the case cites, using the `x`, `y`, `w`, `h` already stored on every
  `Element`. Beside it, the field constraints read from the DOM — `required`,
  `maxlength`, `pattern`, `min`/`max`, `autocomplete` — because that is where
  the negative and edge cases actually come from, and showing it is what makes
  a reviewer trust the output. This panel is the standout feature of the whole
  product; do not cut it.
- Approve / edit / reject per case, written to the sidecar. Export honours the
  current filter.

---

## 6. Visual design

Dark, technical, dense but calm. Closer to a monitoring console than a SaaS
marketing dashboard.

```
ground    #0E1116      text        #E7EAF0
surface   #151A21      text-2      #9AA3B2
raised    #1B212A      text-3      #7A8393
line      #242B35

accent    #5FB98F   live, healthy, primary action
amber     #D9924A   attention, budget pressure, needs-review
blue      #6E9FD4   in-page state, modal, informational
red       #D96F6F   error, denied, destructive
violet    #A98BD4   blocked write, boundary
```

- **Type:** Space Grotesk for display and numbers, IBM Plex Sans for body,
  IBM Plex Mono for selectors, IDs, URLs and log lines. Never set a selector in
  a proportional face.
- **Outcome colours are semantic and fixed.** The nine `Outcome` values map to
  colours once, in one module, and every surface uses that map. A reader should
  learn the colours once.
- Real `<button>`, `<a href>`, `<input>` + `<label>`. No click handlers on
  divs. `aria-label` on every icon-only control. Body text at 4.5:1 minimum.
- Motion only where it carries information: the live pulse, a new node
  appearing, a progress bar moving. Nothing decorative.

---

## 7. Milestones

Each one ends somewhere usable.

| # | Deliverable | Done when |
|---|---|---|
| 1 | FastAPI skeleton, run registry, subprocess spawn, SSE tail of an existing log | You can start a run from `curl` and watch events stream |
| 2 | Live run screen: events, budgets, now-exercising | A running crawl is legible end to end in the browser |
| 3 | `qagen` changes 1–5 (live frames, live.json, stop, pause, per-module counters) | Live viewport renders; stop yields partial output |
| 4 | Graph explorer against finished runs | You can find every state with unexercised controls |
| 5 | Test case review + evidence overlay + export | A reviewer can work entirely in the UI |
| 6 | New-run config screen + module probe (change 6) | A run can be configured without touching YAML |
| 7 | Run history and run-to-run diff | You can see what changed between two crawls of the same app |

Milestone 2 before milestone 6 is deliberate. Watching a run is where the value
is; configuring one still works from YAML in the meantime.

---

## 8. Rules

- **Do not modify crawler logic.** Fingerprinting, budgets, restore and the
  action planner are the accumulated result of many real runs against a live
  app. Additive hooks only.
- **The CLI keeps working, unchanged.** Every existing command and flag behaves
  exactly as it does today. The API is a second caller, not a replacement.
- **Never disable the write-guard from the UI without a typed confirmation**
  naming the target host.
- **Never invent data for a panel.** If a capture is partial or a module was
  starved, show that. A visible gap is a finding; a filled-in guess is a lie.
- **No executable script generation.** This system writes test *cases*. The
  graph is deliberately the substrate for scripts later; that is a separate
  project.
- Tests: `pytest tests/ -q` must stay green. Add API tests against a checked-in
  fixture run directory so they need no browser and no API key.
