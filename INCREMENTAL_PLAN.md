# Incremental re-testing: architecture and implementation plan

**Status: design only. Nothing here is built yet.**

When you say "implement this", read this file and start at §8 Milestone 1.

---

## 1. The problem, stated once

The website changes. Today that costs a full 3h 19m crawl and a full
regeneration of every test case — whether one button was renamed or the whole
product was rebuilt.

The money is not the issue. The real bill is:

| | 2,400 cases (200 states) | 5,000 cases (~416 states) |
|---|---|---|
| Crawl | 3h 19m | ~7h |
| AI regeneration | ~$20 | ~$42 |
| **Human re-review at 1 min/case** | **40 hours** | **83 hours** |
| Human edits, bug links, notes | **all lost** | **all lost** |

**Goal: change as few test cases as possible, and know exactly which ones.**

---

## 2. What actually invalidates a test case

Our test steps contain **no selectors** — only human words plus a location
hint. `Step` has three fields: `step_number`, `action`, `expected_result`.
Selectors live in a separate hidden field, `source_selectors`.

That narrows the problem considerably:

| Change on the site | Case still valid for a human tester? |
|---|---|
| Internal selector changed | **Yes** — the step reads the same |
| Control moved position | **Mostly** — only the "(top-left)" hint is stale |
| Control renamed | **No** — step text is wrong |
| Control removed | **No** — step is impossible |
| Flow changed (extra confirm step, reorder) | **No** — steps out of order |
| Page renamed or moved | **No** — precondition is wrong |

Only the bottom four matter. The hidden selectors are still what lets us
*detect* those cases automatically — a selector that no longer resolves is how
we know a control is gone, without a human reading anything.

---

## 3. Architecture: two kinds of run

Today there is one kind of run. There will be two.

```
BASELINE RUN  (what we do now, unchanged)
   crawl everything -> graph + page models -> generate all cases -> write baseline store

INCREMENTAL RUN  (new)
   load baseline store
        |
   [1] DETECT   cheap probe of known screens         ~3 min, no AI
        |         -> unchanged / changed / gone / new
   [2] CRAWL    only changed + new areas             minutes, not hours
        |
   [3] GENERATE only affected states                 ~$2, not $42
        |
   [4] MERGE    new cases + untouched old cases      instant
        |
   write updated baseline store + a CHANGE REPORT
```

The change report is the actual deliverable for a human:

```
17 screens checked
 14 unchanged      -> 4,880 test cases untouched
  2 changed        ->    24 test cases regenerated
  1 gone           ->     8 test cases marked OBSOLETE
  1 new screen     ->    12 test cases added
```

---

## 4. What we keep between runs (the baseline store)

A new directory written at the end of every run:

```
<output_dir>/baseline/
    manifest.json        run id, target, timestamp, config hash, tool version
    screens.json         one entry per state (see below)
    cases.json           one entry per test case, with its identity + provenance
    signatures.json      screen id -> cheap signature, for the fast probe
```

### 4.1 `screens.json` — one entry per state

```json
{
  "screen_id": "scr_home_a1b2c3",
  "normalized_url": "https://www.samsungvx.com/",
  "node_type": "page",
  "title": "HOME | Samsung VXT CMS",
  "parent_screen": null,
  "opened_by": null,
  "identity_anchors": ["[data-testid=\"dashboard_screen\"]", "#header_logo", "..."],
  "fingerprint": "d4e1cec673ba8f2782c1",
  "cheap_signature": "…",
  "element_count": 51,
  "last_seen_run": "run_2026_08_25_01"
}
```

**`screen_id` is the important field.** It must survive a release. It is *not*
`N001` — node ids are assigned in discovery order and are worthless across runs
(measured: only 22 of 179 lined up between two real runs).

**`identity_anchors`** is the set of stable selectors (`data-testid` / real
`id`) present on that screen. Two screens are "the same" when their anchor sets
overlap by >= 60%. Measured on two real crawls of this site: **152 of 165
screens matched** this way, versus 93 by fingerprint and 22 by node id.

### 4.2 `cases.json` — one entry per test case

```json
{
  "case_id": "TC_a7f3c2",
  "title": "Add a screen from the dashboard",
  "screen_ids": ["scr_home_a1b2c3", "scr_home_newmenu_9f2e"],
  "source_selectors": ["[data-testid=\"dashboard_screen_newbtn\"]", "..."],
  "content_hash": "…",
  "status": "active",
  "generated_in_run": "run_2026_08_24_01",
  "human_edited": false,
  "annotations": {}
}
```

- **`case_id` must be stable.** Derive it from *what the case tests* (a hash of
  category + the screens + the controls it touches), never from a counter.
  Today `TC_047` means "the 47th case produced this run", which is why suites
  cannot be diffed.
- **`screen_ids` is a list**, not one value. A flow case spans screens; if
  *any* of them changed, the case must be re-checked.
- **`human_edited` and `annotations`** are never overwritten by the tool. This
  is the field that protects your team's work.

---

## 5. The three mechanisms

### 5.1 DETECT — the cheap probe (no AI)

For each screen in `screens.json` that has a URL:

1. `goto(url)`, `settle(quick=True)`
2. Run `SIGNATURE_JS` and compare with the stored `cheap_signature`
3. Batch-check every `source_selectors` entry used by that screen's cases, in
   **one** `page.evaluate` (the same trick `_verify_selectors` already uses)

Classify each screen:

| Result | Meaning | Action |
|---|---|---|
| signature matches | unchanged | skip entirely |
| signature differs, anchors >= 60% match | **changed** | re-crawl + regenerate |
| URL 404s or redirects to login | **gone** | mark its cases obsolete |
| screen in graph, not in baseline | **new** | crawl + generate |

Popup screens have no URL, so they are probed by replaying their stored path —
the machinery already exists (`ReplayStep`, `_replay`).

**Cost:** 33 distinct URLs x ~4s = **2-3 minutes.**

**Known limitation:** the cheap signature is narrow. A reworded label on a plain
`div` will not move it. So the incremental run must never fully replace a
scheduled baseline run.

### 5.2 CRAWL — targeted

Seed the frontier with only the changed and new URLs instead of just
`target.url`. Everything else in the crawler is unchanged — same BFS, same
budgets, same popup queueing.

### 5.3 GENERATE — targeted, then merge

Regenerate cases only for affected screens. Merge: new cases replace old ones
with the same `case_id`; untouched cases are copied through byte-identical, with
their annotations intact.

---

## 6. Second run behaviour — answering the direct question

**Question: on the second run, should the crawler start from the saved graph or
crawl normally?**

**Neither, exactly. It should be *seeded* by the saved graph.**

- **Not from the graph alone** — the graph is a record of what the site looked
  like *last time*. Trusting it without looking would miss every change, which
  defeats the purpose.
- **Not a normal crawl** — that is the 3h 19m we are trying to avoid.

So: **read the baseline, verify it cheaply, and crawl only where reality
disagrees with the record.**

Concretely, the default for `qagen crawl` and `qagen run` becomes:

```
if <output_dir>/baseline/ exists  ->  incremental run
else                             ->  baseline run
```

with explicit overrides:

| Flag | Behaviour |
|---|---|
| *(none)* | Incremental if a baseline exists, otherwise full |
| `--full` | Ignore the baseline, crawl everything, overwrite it |
| `--baseline <dir>` | Compare against a baseline from somewhere else |
| `--detect-only` | Run the probe, print the change report, crawl nothing |

`--detect-only` is the one to run nightly.

---

## 7. Changes to the current code, file by file

Nothing below is written yet. This is the map to follow.

### 7.1 New files

| File | Contains |
|---|---|
| `qagen/baseline/store.py` | Read/write `baseline/`, the `Screen` and `CaseRecord` models |
| `qagen/baseline/identity.py` | `screen_id_for(page)`, `case_id_for(case)`, anchor-overlap matching |
| `qagen/baseline/detect.py` | The cheap probe; returns `ChangeReport` |
| `qagen/baseline/merge.py` | Merge new cases into the old suite, preserving annotations |
| `tests/test_baseline_identity.py` | Anchor matching, stable ids, the 1-to-1 assignment rule |
| `tests/test_baseline_merge.py` | Annotations survive; obsolete marking; id stability |

### 7.2 Existing files to touch

| File | Change |
|---|---|
| `qagen/models.py` | Add `screen_id` to `PageModel`/`NavNode`; add `case_id`, `screen_ids`, `content_hash`, `human_edited`, `annotations` to `TestCase` |
| `qagen/orchestrator.py` | `run()` branches baseline vs incremental; add `_detect()` and `_merge()` between `_crawl()` and `_generate()`; `_generate()` takes a screen filter |
| `qagen/browser/crawler.py` | `run()` accepts seed URLs instead of always starting from `target.url` |
| `qagen/cli.py` | Add `--full`, `--baseline`, `--detect-only` to `crawl` and `run`; new `qagen diff <a> <b>` command; print the change report |
| `qagen/report/json_out.py` | Write the baseline store alongside the existing outputs |
| `qagen/generation/prompts.py` | Nothing — steps already carry no selectors |
| `qagen/config.py` | `baseline.enabled`, `baseline.anchor_match_threshold` (0.6), `baseline.probe_timeout_ms` |

### 7.3 Deliberately *not* changing

- The crawler's BFS, budgets, popup queueing, reading order — all unaffected
- The prompt and the test-case format the tester reads
- The write-guard

---

## 8. Milestones

Do them in this order. Each is independently useful and shippable.

### Milestone 1 — Stable identity *(~1 day)*

Nothing else works until ids stop shifting.

1. `screen_id_for(page)` from the anchor set + normalized URL + node type
2. `case_id_for(case)` from category + `screen_ids` + the controls it touches
3. Write `baseline/` at the end of every run
4. `qagen diff <run_a> <run_b>` — offline, no browser, prints added / removed /
   changed screens

**Done when:** two crawls of the same site produce the same `screen_id` for the
same screen, and `qagen diff` on the two existing runs prints a sane report.

### Milestone 2 — The detector *(~1 day)*

5. `detect.py` — probe known screens, classify, emit `ChangeReport`
6. `--detect-only` flag, change report printed and written as JSON

**Done when:** running it twice with no site change reports "0 changed", and
renaming a button in the local test fixture reports exactly that screen.

### Milestone 3 — Targeted crawl *(~1 day)*

7. Seed the frontier from the change report
8. Default to incremental when a baseline exists; `--full` to override

**Done when:** an incremental run on an unchanged site finishes in minutes and
produces the same graph.

### Milestone 4 — Targeted generation and merge *(~1-2 days)*

9. `_generate()` filtered by affected screens
10. `merge.py` — carry untouched cases through byte-identical, preserve
    `annotations` and `human_edited`, mark orphaned cases `obsolete`

**Done when:** changing one screen regenerates only its cases, every other case
is byte-identical to the previous run, and hand-written annotations survive.

---

## 9. Risks and how we handle them

| Risk | Handling |
|---|---|
| **Silent miss** — probe says unchanged, but the screen did change | Never let incremental fully replace a scheduled `--full` run. Weekly full rebuild. |
| **Data churn** — dashboard counters make everything look changed | Probe must apply the same digit-normalisation the fingerprint uses (`_normalise_name`). Watch for a first run that reports "everything changed". |
| **Anchor matching maps two screens onto one** | Seen in real data: two Home variants both matched the same screen. Require a 1-to-1 assignment and break ties with `opened_by` / `parent_screen`. |
| **Flow cases span screens** | `screen_ids` is a list; regenerate if *any* member changed. |
| **Baseline drifts from reality over many increments** | Store `last_seen_run`; force a full run when a baseline is older than N runs or the config hash changed. |
| **Someone edits a case by hand, then we overwrite it** | `human_edited: true` — the merge never overwrites, it flags a conflict for review. |

---

## 10. What this still will not solve

- **A control that exists but now behaves differently.** The probe checks
  presence, not behaviour. Only a real crawl catches it.
- **Screens gated behind data we do not have.** A schedule screen needs a
  schedule to exist. Fixtures problem, not a crawler problem.
- **Role-gated features.** Everything here assumes one logged-in user.
