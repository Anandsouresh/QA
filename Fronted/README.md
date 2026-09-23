# QAGen Control Room — front end

Configure a crawl, watch it run, explore the navigation graph, review the test
cases. The web face of the `qagen` package in the parent directory.

```bash
npm install
npm run dev            # http://localhost:5173
```

It works with or without a backend. Started on its own it reads bundled
fixtures and says so; with the API running it drives real crawls.

```bash
# in the repo root, for live runs
pip install -e ".[api]"
uvicorn api.main:app --port 8000
```

---

## Two data sources, one shape

| | |
|---|---|
| **live** | the FastAPI service in [`../api`](../api), reading a real run directory |
| **demo** | fixtures in `public/data`, extracted from a finished run by `scripts/make_fixtures.py` |

The Runs screen switches between them and the choice survives a reload.
[`src/lib/api.ts`](src/lib/api.ts) is the only file that knows which is in play;
its adapters normalise raw qagen output into the shapes the screens expect and
add nothing the crawler did not record.

Regenerate the demo data from any finished run:

```bash
npm run fixtures                          # defaults to ../samsungvx-200-final05
python scripts/make_fixtures.py ../my-run
```

The crawl half of that data is real: 115 states, 478 transitions, 2,600 log
lines, 102 screenshots with full element geometry. Only the 544 test cases are
synthesised, because every recorded run so far was crawl-only. Even those cite
selectors that exist in their capture and carry that element's real position,
which is what lets the evidence panel box a control on a genuine screenshot.

---

## Screens

| Route | What it does |
|---|---|
| `/` | Target, tokens, module selection with per-module state budgets, safety, and Start |
| `/live` | Live viewport, the control being exercised, the map assembling, budgets, event stream |
| `/graph` | The navigation graph in module bands, with filters and a state inspector |
| `/cases` | Case review with the evidence overlay and approve/reject |
| `/history` | Every run on disk, with stop and delete |

**Modules.** Untick one and it is left out of the run: the selection becomes
`target.include_paths` globs, and each budget becomes an entry in
`crawl.module_budgets`. Press **Discover modules** and the backend loads the
entry page, groups every link by first path segment and suggests budgets
weighted by how many distinct paths each module showed.

**Tokens.** The session token for the target goes in as pasted JSON or a
dropped `.json` file; **Verify session** proves it before you pay for a crawl.
The Anthropic key is separate and is passed to the crawl process as an
environment variable, never written to the run directory.

**Live.** With a run selected the screen subscribes to Server-Sent Events. With
none it replays a recorded log on a timer through the same reducer, so the
components cannot tell the difference. Pause and Stop call the API for a live
run; Stop is cooperative and keeps everything captured so far.

---

## Theme

Dark by default, follows the system when set to *system*, and the toggle at the
bottom of the rail cycles dark → light → system. The choice is remembered.

Every colour resolves through a `--qg-*` CSS variable defined in
[`src/index.css`](src/index.css), so switching costs one attribute on `<html>`
and no re-render. Raw hex appears in exactly one place, that file.

One consequence worth knowing: the strings in `src/lib/tokens.ts` are
`var(--qg-…)` references, which resolve in CSS *properties* but not in SVG
presentation *attributes*. Components therefore pass them through
`style={{ fill: … }}` rather than `fill="…"`.

---

## Layout

```
src/
├── lib/
│   ├── types.ts     mirrors qagen/models.py
│   ├── tokens.ts    tones, the outcome → colour map, wash()
│   ├── api.ts       the only place that knows where data comes from
│   ├── modules.ts   first-path-segment rule, shared with the backend
│   └── format.ts    clocks, counts, URL paths
├── store/
│   ├── session.ts   backend detection, run list, selected source
│   ├── liveRun.ts   one reducer, fed by SSE or by replay
│   └── theme.ts     dark / light / system
├── components/      Rail, and the UI primitives
└── screens/         one file per route
```

---

## Checks

```bash
npx tsc --noEmit                          # types
npm run build                             # production build
npm run preview -- --port 4173

python scripts/shoot_app.py               # every route, both themes
python scripts/test_integration.py        # full stack against the fixture app
```

`shoot_app.py` writes to `screenshots/<theme>/` and exits non-zero on any
console error or failed request.

`test_integration.py` needs the API on 8000, this app on 4173, and the bundled
fixture site on 8899 (`python -m http.server 8899 --directory ../tests/fixture`).
It starts a real crawl, checks the UI streams it, stops it, and asserts the
partial output survived.

---

## Known gaps

- **The live viewport is not 1 fps.** During a live run it shows the newest
  screenshot the crawler has written, refreshed every few seconds. True
  frame-by-frame streaming needs a hook inside the crawl loop; see change 1 in
  [`../WEB_UI_BUILD_PROMPT.md`](../WEB_UI_BUILD_PROMPT.md). Highlight boxes
  therefore only appear once a run has finished and the element inventory is on
  disk.
- **Export and Edit are inert.** The export endpoint exists; the buttons are
  not wired to it yet.
- **Reviewer verdicts live in component state**, so they reset on reload. They
  belong in a `review.json` sidecar beside the run.
- **The graph opens on the product modules.** Settings, Home, Apps and VXT Labs
  are one tick away in the filter panel.
