# Module-wise crawling + the four open issues: implementation plan

**Status: design only. Nothing here is built yet.**

When you say "implement this", read this file and start at the milestone you name.

---

## Part 0 — What the logs actually show about "modules"

You asked me to look at the crawl logs to confirm the module boundary. I did —
every URL the crawler ever recorded, across two full runs, grouped by the
**first path segment**:

| Module | Distinct URL shapes seen |
|---|---|
| `screen` | `/screen`, `/screen/{id}` |
| `content` | `/content`, `/content/{id}` |
| `playlist` | `/playlist`, `/playlist/create`, `/playlist/sync/create`, `/playlist/{id}` |
| `schedule` | `/schedule`, `/schedule/create`, `/schedule/{id}` |
| `channel` | `/channel` |
| `settings` | `/settings`, `/settings/general`, `/settings/organization`, `/settings/workspace`, `/settings/user`, `/settings/plan`, `/settings/tag`, `/settings/tag/{id}`, `/settings/event`, `/settings/event/create`, `/settings/screenpreset`, `/settings/place`, `/settings/place/{id}`, `/settings/emergencyalert`, `/settings/emergencyalert/create`, `/settings/subscription`, `/settings/subscription/{id}`, `/settings/edithome`, `/settings/activitylog`, `/settings/techinquiry`, `/settings/techinquirynew` |
| `vxtlabs`, `apps` | standalone, one page each |
| `terms`, `privacy`, `cookie`, `euda` | legal pages, standalone |

**This confirms exactly what you said: `target_url/screen/*` is a real, clean
boundary.** Every URL under `/screen` is the Screen module and nothing else
leaks into it. Same for Content, Playlist, Schedule, Channel. Settings is the
one module with many sub-pages under one prefix, which is exactly why it kept
swallowing the crawl budget in earlier runs.

**The important discovery: the tool can already do this, today, with no code
change.** `TargetConfig.include_paths` (`qagen/config.py`) is matched with
wildcard globs in `ScopeRules.in_scope` (`qagen/browser/policy.py:150`).
Setting

```yaml
target:
  include_paths: ["/screen", "/screen/*"]
```

already restricts the crawl to the Screen module and nothing else. This is
Approach 1 from the module-crawling discussion, and it needs zero new code —
only new config files, one per module. I'll include this as Milestone 0 below
because it's usable immediately, before any of the other work.

The crawler's per-section budget (`_section_of` in `crawler.py`) already
computes this same first-path-segment grouping internally, for a different
purpose (capping how many states one section can take). So "module" is not a
new concept for this codebase — it already exists in two places and just
hasn't been exposed as a per-run target.

---

## Part 1 — The four issues, root cause and fix plan

### Issue A — Settings tabs recorded as duplicate states

**Evidence:** `N011` and `N012` in `samsungvx-200-final05` are the same "Plan
Details" screen — identical title, identical numbers, identical layout —
recorded as two states.

**Root cause:** Settings swaps its content without changing the URL, exactly
like a popup. The anchor-based merge I built earlier (`_canonicalise` in
`crawler.py`) deliberately **excludes** anything that behaves like a popup,
because a popup and the page behind it share 95%+ of the same anchors, and
merging those would erase real popups. Settings tabs are the same technical
shape as a popup, so they get excluded by the same rule that protects real
popups — collateral damage, not a separate bug.

**Fix plan:**

1. Give an in-page state a **path identity**, not just a fingerprint: the
   sequence of tab labels clicked to reach it (`Settings > Plan`). This already
   exists in spirit as `NavNode.opened_by` / `parent_state`; it needs to become
   a stable, comparable key rather than free text.
2. When two in-page states share the same **path identity** on the same base
   page, run the anchor-similarity check (`anchor_similarity`, already built)
   between them specifically — not against the whole popup population, only
   against other arrivals at the same named tab.
3. Merge on high similarity, exactly as `_canonicalise` already does for full
   pages — same function, narrower scope.

**Effort:** ~half a day. Reuses `anchor_set`/`anchor_similarity` entirely; the
new part is deriving and comparing the path identity.

---

### Issue B — No retry when a screen renders blank/thin

**Evidence:** the only existing signal, `thin_capture`
(`crawler.py:294`), fires when a page has **fewer than
`hydration_min_elements`** — default 1. In practice this never fires on a real
page, so a screen that rendered half-built or empty is accepted as final with
no second attempt.

**Fix plan:**

1. Track a **typical element count per normalized URL** across the run (a
   running median is enough — no new infra, a small dict keyed by URL).
2. After settling, if the captured count is dramatically below that URL's
   typical count (e.g. under 50%) **and** this is not the first visit to that
   URL, treat it as a thin capture:
   - wait an extra beat (reuse the existing `post_loader_wait_ms` grace period)
   - re-extract once
   - keep the richer of the two captures
3. Log `retry_thin_capture` either way, so a page that is *genuinely* sparse
   (an empty workspace) is distinguishable from one that render-raced.

**Guard:** only retry once per state, and never retry the *first* visit to a
URL (there's no baseline to compare against yet) — this keeps the cost bounded
and avoids an infinite loop on a page that is legitimately always thin.

**Effort:** ~half a day.

---

### Issue C — Some blocked POST/PUT calls are reads, not writes

**Evidence, from real blocked-mutation logs across two runs:**

```
POST /api/cms/{id}/{id}/resources     -- likely a content list/search call
POST /api/ums/{id}/places             -- likely a places/workspace list call
```

against confirmed genuine writes that should stay blocked:

```
PUT  /api/dms/.../screens/{guid}         -- editing a specific screen
POST /api/ums/{id}/{id}/organizations    -- updating org settings
POST /api/dms/.../screens/wall           -- creating a screen wall
```

**Root cause:** the write-guard (`session.py`) blocks every
POST/PUT/PATCH/DELETE unconditionally. That's the safe default, but this app
uses POST for at least two read/list endpoints — a common pattern when a
filter body is too complex for a query string.

**Fix plan — staged, safety first:**

1. **New config list, `crawl.safe_read_endpoints`** (substrings or globs,
   matched against the path). Anything matching is let through even though its
   HTTP method is normally blocked. Empty by default — behaviour does not
   change until you explicitly name an endpoint.
2. **You confirm the two candidates** (`.../resources`, `.../places`) actually
   are reads — five minutes with real devtools open against this app settles
   it definitively; I will not guess this from the outside.
3. Once confirmed, they go in the config for this target only —
   `samsungvx-200-final.yaml`, not the tool's defaults.
4. Every request that matches `safe_read_endpoints` is still logged distinctly
   (`allowed_read_like_write` observation) so the exception is always visible
   in the manifest, never silent.

**Explicitly not doing:** auto-detecting "this POST looks like a read" by
pattern-matching words like `search`/`list`/`query` in the path. That was
Approach B from the earlier discussion and I'd still avoid it — a badly-named
write endpoint could slip through, and the entire point of the write-guard is
that it never has to be trusted to guess.

**Effort:** ~2 hours once the two endpoints are confirmed.

---

### Issue D — Schedule's "+" button, and restore-abandon tuning

**Evidence:** in an **old** run, one search-box click opened a dropdown, the
"go back" failed once, and the entire rest of the page — including "New
Schedule" — was abandoned. That was the original one-strike-and-you're-done
restore bug.

**Current state, checked against a recent run:**

```
104 restore failures
 82 recovered (hard-reset succeeded, the plan continued)
 22 abandoned (3 failures in a row, or hard-reset itself failed)
```

So this exact complaint is **already fixed** — "New Schedule" was clicked
successfully in the recent run. What's left is real but smaller: 22 states
still give up entirely.

**Fix plan:**

1. Raise `max_restore_failures` from 3 to a config-tunable value and try 5 on
   this target — cheap to test, no code change needed, just the YAML value.
2. Look at what makes `_hard_reset` itself fail (the 22 cases) — likely the
   same class of problem as Issue A: a replay path whose trigger selector no
   longer resolves. Once Issue A's path-identity work lands, re-measure this
   number; a chunk of the 22 may disappear as a side effect.

**Effort:** ~1 hour to tune and re-measure; deeper work only if the number
stays high after that.

---

## Part 2 — Module-wise crawling: the design

### The boundary rule (confirmed above)

A module is the **first path segment**: `screen`, `content`, `playlist`,
`schedule`, `channel`, `settings`, plus the small standalone pages. This is
already what `_section_of()` computes internally.

### Recommended shape: one crawl, per-module budgets, seeded sub-page list

From the four approaches discussed earlier, this is the one I'd build:

- **One crawl process**, not six separate ones — so the header, the profile
  menu, the notification bell, and other shared chrome are still tested once
  each, not once per module.
- **A hard budget per module**, enforced live, so Settings (21 sub-pages)
  cannot starve Channel (1 page) the way it did in the very first runs.
- **A seeded list of known sub-pages per module** (the table in Part 0) used
  as a floor — if the crawler's own discovery misses a sub-page, the seed list
  still gets it queued.

### Config additions

```yaml
crawl:
  # Replaces the single max_states_per_section with per-module control.
  module_budgets:
    screen: 40
    content: 40
    playlist: 30
    schedule: 30
    channel: 20
    settings: 50          # generous -- it has the most real sub-pages
    default: 15            # anything not listed above (vxtlabs, apps, ...)

  # Known sub-pages, enqueued at depth 1 regardless of whether the crawler's
  # own link discovery finds them. A floor, not a ceiling -- discovery still
  # runs normally and can find MORE than this list.
  module_seeds:
    settings:
      - /settings/general
      - /settings/organization
      - /settings/workspace
      - /settings/user
      - /settings/plan
      - /settings/tag
      - /settings/event
      - /settings/screenpreset
      - /settings/place
      - /settings/emergencyalert
      - /settings/subscription
      - /settings/edithome
      - /settings/activitylog
      - /settings/techinquiry
    schedule:
      - /schedule/create
    playlist:
      - /playlist/create
      - /playlist/sync/create
```

### Cross-module clicks: capture once, mark it, do not explore it

This is the piece confirmed in discussion, and it has an exact final shape now:

**When a click leads outside the module the crawler was told to stay in:**

1. **Still take one snapshot.** Navigate there, settle, take the screenshot and
   the raw DOM dump — exactly the same capture step already used for every
   other state. You get to *see* what the button leads to.
2. **Record it as its own state**, not a shared generic marker. `/content` and
   `/playlist` reached from a Screen-only crawl must be two different nodes,
   each with its own screenshot — not one node that stands in for
   "everywhere outside Screen." This is the part the current code gets wrong
   for this case (see below).
3. **Mark it as a boundary** — visually distinct in the graph (the existing
   `node_type: "boundary"` already renders with its own colour in the HTML
   viewer), so anyone looking at the map can see at a glance which states were
   captured-but-not-explored.
4. **Do not act on it.** No `_act_on_state`, no clicking its buttons, no
   following its own links. One capture, one node, done — the opposite of a
   full visit.

**What the code does today, and the specific gap:**

`add_boundary` (`graph/builder.py`) already exists and already sets
`node_type="boundary"` for anything that fails the scope check for a reason
other than "different origin" — which includes "not in include_paths". But it
keys the node by **origin** (`boundary::{hostname}`), not by the destination
page. That means today, every click that leaves the module — whether it leads
to Content, Playlist, or Schedule — collapses onto **one shared node**, and
that node never gets a screenshot at all (`add_boundary` never captures one).

So the fix is really two changes to the same function's family:

- Key this specific kind of boundary (same-origin, out-of-module) by the
  **destination's normalized URL**, not by origin. Cross-origin boundaries
  (a genuine external link to another company's site) keep the current
  one-node-per-origin behaviour — that part is correct as is and shouldn't
  change.
- Give it one real capture: reuse `_capture_artifacts`, the same function
  every normal state already uses, called once and only once for this node.

**Where this plugs into `_perform`:** the `NAVIGATION` branch (`crawler.py`,
around line 809) is where a same-origin navigation is currently always turned
into a fully-queued state with no scope check at all. That is exactly the gap
identified earlier. The fix sits right there: before calling `add_state`,
check `scope.in_scope(after_url)`. If it fails **and the reason is
"not in include_paths"** (i.e. this is a module restriction, not a real
exclusion like `/logout`), take the one-time capture-and-mark path instead of
the normal one, and do not append anything to the frontier for it.

**The "full run" half of this, exactly as asked:** all of the above is
conditional on a module restriction being active in the first place. When
`include_paths` is empty (a full, unrestricted run — the normal case today),
`scope.in_scope` always returns allowed for any same-origin URL, so this new
branch is never taken and nothing changes. A full run behaves exactly as it
does now; this entire mechanism only activates when you deliberately scope a
crawl to one module.

### Also usable immediately, with zero code changes

For a **single-module test crawl right now** (e.g. "just re-crawl Screen after
the Issue B fix, don't touch the rest"), `include_paths` already does this:

```yaml
target:
  include_paths: ["/screen", "/screen/*"]
```

This is worth running as a quick sanity check on any one fix, independent of
the bigger module-budget work below.

### What changes in the code

| File | Change |
|---|---|
| `qagen/config.py` | Add `module_budgets: dict[str, int]` and `module_seeds: dict[str, list[str]]` to `CrawlConfig` |
| `qagen/browser/crawler.py` | `_url_budget_ok` reads `module_budgets` instead of the single `max_states_per_section`; `run()` enqueues `module_seeds` at startup alongside the entry URL |
| `qagen/cli.py` | `--module <name>` convenience flag that sets `include_paths` for a single-module crawl, for the "test one module quickly" case |
| `samsungvx-200-final.yaml` | The actual budgets/seeds table for this target |

### Milestones

1. **Module seeds + per-module budgets** (~1 day) — the config additions above,
   wired into `_url_budget_ok` and `run()`. Done when a crawl of this target
   shows every module represented roughly in proportion to its real size, and
   Settings can no longer take more than its configured share.
2. **`--module` flag for one-off module crawls** (~2 hours) — thin wrapper over
   `include_paths`, useful for testing any of the four fixes above in
   isolation without a full 3-hour run.
3. **Cross-module boundary capture** (~half day) — the scope check in
   `_perform`'s `NAVIGATION` branch, keying this kind of boundary by
   destination URL instead of origin, and the one-time `_capture_artifacts`
   call. Done when a Screen-only crawl shows Content, Playlist, Schedule etc.
   each as their own single boundary node with a real screenshot, none of them
   explored further, and a full unrestricted run is byte-for-byte unchanged.

---

## Part 3 — Suggested order across everything in this document

| # | Item | Effort | Why this position |
|---|---|---|---|
| 1 | Confirm the two ambiguous endpoints (Issue C) | 5 min, your side | Blocks nothing else, but the sooner it's confirmed the sooner Content/Places stop looking artificially empty |
| 2 | Retry on thin capture (Issue B) | ~half day | Cheap, independent, immediately improves data quality for everything after it |
| 3 | Settings tab de-duplication (Issue A) | ~half day | Directly fixes what you screenshotted; reuses existing anchor code |
| 4 | Restore-failure tuning + re-measure (Issue D) | ~1 hour + observation | Quick to try; informs whether more work is needed here at all |
| 5 | Module seeds + per-module budgets | ~1 day | The bigger structural change; benefits most once 1-4 are in, since a module-wise crawl is only as good as the states it captures |
| 6 | `--module` flag | ~2 hours | Convenience on top of 5, for fast iteration afterward |

Total: roughly 3 days of focused work, plus the five minutes of your time on
item 1 that nothing else depends on.
