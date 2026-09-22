# Final plan: every open issue, one list, one order

**Status: all seven items implemented and tested (161+ tests passing,
including end-to-end coverage against a live browser). Item 1 was resolved
without needing a manual devtools check -- see below for how.**

This is the single place to look before any implementation work. It replaces
juggling the earlier discussions in your head — everything still open lives
here, in the order I'd build it. `INCREMENTAL_PLAN.md` (re-testing after the
site changes) and `CHANGE_RESILIENCE.md` (selector durability) are separate,
larger initiatives and are not repeated here — this file is scoped to the
crawl-quality issues found in this session's runs.

When you say "implement", name the item number and I start there.

---

## Part 0 — What's already fixed (context, not a to-do)

So the plan below isn't mistaken for new problems, here's what earlier
sessions already closed, each with a test:

| Fixed | What it stops |
|---|---|
| Nesting-aware clickable extraction | A card and the `+` inside it are both found, not one swallowing the other |
| Hover-naming | An icon-only button gets a real name from its tooltip instead of reaching a test case unnamed |
| App-frame detection (`shell_selectors`) | Header/left-menu controls no longer crowd out real content in the click budget |
| Analytics-marker clickability (`extra_clickable_selectors`) | Controls with no role, no tabindex, not even a pointer cursor (the profile avatar) are still found |
| Reading-order planning | Elements are clicked top-to-bottom, left-to-right, like a person would |
| `frame_reserve` | The left menu still gets a few click slots even on a content-heavy page |
| Popups queued, not clicked immediately (BFS, not DFS) | The crawl finishes the current page before diving into what a click opened |
| Charge-once budgeting | A popup seen twice (open + replay) no longer burns two of its page's six state slots |
| Anchor-based page merging (`_canonicalise`) | The same full page, caught at two different loading moments, collapses into one state |
| Settle waits for the render to finish growing | Reduces how often a half-drawn page gets captured as if it were final |
| Revealed-only popup planning (`only_identities`) | A popup's own new buttons can't be pushed out of the click budget by the page behind it |
| Popup queue deduped by identity, not position | The same "Export" button isn't queued four times because a list redrew |
| Restore retry + hard-reset (`max_restore_failures`) | One failed "go back" no longer abandons every remaining button on a page |

None of this needs touching. What follows is what's still open.

---

## Part 1 — The open issues, in the order I'd fix them

### 1. Ambiguous network calls — DONE, confirmed against a real live crawl

**What:** `POST /api/cms/.../resources` and `POST /api/ums/.../places` were
blocked by the write-guard, but both read like list/search calls, not writes.
Rather than guess this from a path name, I ran a bounded, read-only probe
against the live staging target (fresh auth token, page loads only, no
clicking) using the *exact* write-guard logic, capturing the real request and
response for anything it touches. This surfaced five endpoints, not two, and
proved every one of them with the real response body:

```
POST .../screens/search    -> {"rows":[{"screenId":"...","screenName":"New Screen Wall",...}]}
POST .../contents/search   -> {"rows":[{"contentId":"...","contentName":"Mailer_...",...}]}
POST .../playlist/search   -> {"rows":[{"playlistId":"...","playlistName":"New Playlist",...}]}
POST .../programs/search   -> {"rows":[{"programId":"...","programName":"New Schedule (7)",...}]}
POST .../channels/search   -> {"channelList":[{"channelId":"...","channelName":"test",...}]}
```

All five: status 200, a body of just `{"advancedSearch":[]}`, and the real
pagination sitting in the query string
(`orderBy=...&order=desc&start=0&rowsPerPage=50`) rather than the body --
which is exactly what the classifier's body-only check had been blind to.
Fixed by teaching it to read the query string too. All five are now named in
`browser.safe_read_endpoints` on the samsungvx targets -- deterministic, not
dependent on the classifier re-deciding it every run, because they are now
genuinely confirmed rather than guessed.

**Built:**

- `browser.classify_ambiguous_writes` (off by default; on for the samsungvx
  targets) -- `classify_write_candidate` (`session.py`) looks at a blocked
  POST's path, JSON body, *and* query string:
  - PUT/PATCH/DELETE are **never** reclassified, whatever the body looks like
  - a path naming an explicit action (`create`, `delete`, `sign`,
    `chat/start`, `screens/wall`, ...) **stays blocked** regardless of shape
  - a filter/pagination signal in the body (`page`, `sort`, `filter`, ...) or
    the query string (`start`, `rowsPerPage`, `orderBy`, ...), or a path
    ending in `/search`, `/list`, `/query` -- with no competing write-shaped
    field (`name`, `title`, `content`, ...) -- is let through
- `browser.safe_read_endpoints` -- the deterministic counterpart, now
  carrying the five confirmed endpoints above

**Also found and fixed while investigating this, from the same live probe:**

- **Cognito credential calls** (`cognito-identity.*.amazonaws.com`) were
  being blocked as if they were writes. Cognito issues temporary AWS
  credentials the app needs to fetch its *own* protected content (thumbnails,
  media) -- not "safe noise" the way analytics is; blocking it can be why a
  page shows real items with no images. Now let through entirely.
- **AWS CloudWatch RUM**, found live as a matched pair -- an STS call
  assuming a "RUM-Monitor" role, then a data-plane call posting the collected
  metrics (`sts.*.amazonaws.com`, `dataplane.rum.*`) -- and a **Google Ads
  conversion pixel** (`google.com/measurement/conversion`) firing on every
  click. All added to the existing telemetry exclusion.

**Tests:** `tests/test_write_guard_classifier.py` (49 cases total, including
the exact five endpoints and their real query strings) and
`tests/test_write_guard_integration.py` (the guard's live decision end to
end, with fake Route/Request objects -- no browser needed).

---

### 2. Retry on a blank or thin screen — DONE

**What:** today, a screen that renders half-built or empty is accepted as
final with no second look — the only existing signal fires below 1 element,
which never happens in practice.

**Fix:** track each URL's typical element count as the crawl goes. If a fresh
capture comes in far below that (under half), wait a beat longer and
re-extract once before accepting it.

**Effort:** ~half a day. **Depends on:** nothing.

---

### 3. Settings tabs recorded as duplicate states — DONE

**What:** the two "Plan Details" screenshots — same content, two different
graph nodes. Settings swaps its tab content without changing the URL, so it
looks like a popup to the existing anchor-merge logic, and popups are
deliberately excluded from merging (to avoid erasing real ones).

**Fix:** give an in-page state a path identity (`Settings > Plan`, not just a
raw fingerprint) and run the same anchor-similarity check *within that path*,
narrower than the popup-wide exclusion.

**Effort:** ~half a day. **Depends on:** nothing directly, but re-measure
after item 6 (module budgets), since Settings is the module this affects.

---

### 4. Restore-failure tuning + re-measure — DONE, and the re-measure found a real bug

**What:** re-measured against a fresh module-restricted crawl of `/screen`.
The numbers were worse than expected -- **67 of 141 restores failed the
cheap exact-signature check (48%)** -- and 8 states were abandoned outright,
one of them (`N028`) with **88 actions never attempted**.

**Root cause, found by reading the actual log around each abandonment:**
every single one followed the same pattern -- `restore FAILED` →
`state_recovered` (the hard reset succeeding) → `restore FAILED` again →
`state_recovered` again → ... five times → **abandoned anyway**. The counter
that decides "give up on this state" (`consecutive_failures` in
`_act_on_state`) was only ever reset by a successful *cheap* restore, never
by a successful *hard* reset. Since this app's cheap signature essentially
never holds, every hard reset succeeding was still silently uncredited, and
five actions was all it ever took to hit the threshold -- regardless of how
well recovery was actually going.

**Fixed:** `consecutive_failures` now resets on either kind of success. Only
a hard reset that *also* fails counts toward the threshold, which is what the
counter was supposed to mean in the first place.

**Effort:** tuning was ~1 hour as planned; the bug fix (`crawler.py`,
`_act_on_state`) was found and fixed in the same session once real data
exposed it. Three tests in `TestConsecutiveFailuresResetOnHardReset`.

---

### 8. A click that does nothing is believed on the first try — DONE

**What:** "Add Screen" and "New Screen Wall" were each clicked exactly once,
both came back `no_change (inert)`, and neither was ever tried again. Both
finished in under a second, immediately after two *other* clicks had each
taken the full 10-second action timeout -- the profile of a page still
catching up with itself, not of a button that truly does nothing. There was
no retry mechanism at all for this.

**Fix:** a click that appears to do nothing (`unchanged`, and no side effect
at all -- no blocked write, no dialog, nothing) is retried once, but only for
a control found by inference (`pointer_cursor`, or `INFERRED_CLICKABLE`) --
not a real `<button>`, which really is inert if it does nothing, and
retrying every high-confidence control would double the click budget for no
gain. A blocked write is deliberately never retried either: it is already a
real, useful result, and clicking again would just attempt the same write
twice.

**Tests:** `TestInertClickRetry` -- confirms the retry fires for an inferred
control, does not fire for a role-based one, and does not fire after a
blocked write.

---

### 9. `_hard_reset` contradicted its own stated design — DONE

**What:** `_hard_reset`'s own docstring says its goal is "somewhere we can
keep testing from, not the exact state" -- but its code returned total
failure (`False`) the instant a single replay step's selector went stale.
Real evidence: 10 `replay_failed` events in one run, several against MUI
DataGrid positional selectors (`div...nth-of-type(9)`) for virtualised rows
that had simply scrolled out of the DOM. Each one cost the *entire*
remaining plan of that state, via the same abandonment path as item 4.

**Fix:** the replay loop now stops at the first step that cannot resolve or
click, but still returns `True` as long as the base page itself loaded --
landing at whatever depth the replay chain still supports is exactly
"somewhere we can keep testing from". Logged as `hard_reset_replay_partial`
so it is visible, not silent.

**Deliberately not changed:** `_replay` (a different function, used only
when a *queued popup* frontier item is first re-entered) keeps its
fail-fast behaviour. Its job is to land specifically *inside* that popup so
the popup's own items can be explored; a partial replay there would mean
exploring the wrong state under the popup's name, which is a correctness
bug, not a coverage one.

**Tests:** `TestHardResetSurvivesAPartialReplay` -- a stale step mid-chain,
every step resolving, the base navigation itself failing, and a plain page
with nothing to replay.

---

### 5. Cross-module boundary capture — DONE

**What:** when a module-restricted crawl (see item 6) clicks something that
leads outside the module, that destination should be captured once — a real
screenshot, its own graph node — and then left alone. Not fully explored, not
merged into one generic "left the module" marker.

**Fix, precisely:**

- The scope check goes into `_perform`'s `NAVIGATION` branch (`crawler.py`,
  around line 809), which today has no scope check at all — a same-origin
  navigation is always fully captured and queued regardless of module.
- When `scope.in_scope(after_url)` fails specifically for "not in
  include_paths" (a module restriction, not a real exclusion like `/logout`):
  take one screenshot via the existing `_capture_artifacts`, create one graph
  node keyed by **destination URL** (not by origin — this is the fix needed in
  `add_boundary`, which today collapses every out-of-module destination into
  one shared marker with no picture at all), mark it `node_type="boundary"`,
  and do not append it to the frontier.
- When no module restriction is active (`include_paths` empty — the normal
  full-run case), `scope.in_scope` always passes for same-origin URLs, so this
  entire branch is never entered. A full run is unaffected.

**Effort:** ~half a day. **Depends on:** item 6 existing to actually exercise
this path (a full run never triggers it).

---

### 6. Module-wise crawling: per-module budgets + seeded sub-pages — DONE

**What:** confirmed from the crawl logs — every URL groups cleanly under a
first path segment (`screen`, `content`, `playlist`, `schedule`, `channel`,
`settings` + its 21 sub-pages). One shared budget let Settings starve every
other module in the earliest runs.

**Fix:**

```yaml
crawl:
  module_budgets:
    screen: 40
    content: 40
    playlist: 30
    schedule: 30
    channel: 20
    settings: 50
    default: 15

  module_seeds:
    settings: [/settings/general, /settings/organization, /settings/workspace,
               /settings/user, /settings/plan, /settings/tag, /settings/event,
               /settings/screenpreset, /settings/place, /settings/emergencyalert,
               /settings/subscription, /settings/edithome, /settings/activitylog,
               /settings/techinquiry]
    schedule: [/schedule/create]
    playlist: [/playlist/create, /playlist/sync/create]
```

`_url_budget_ok` reads `module_budgets` instead of the single
`max_states_per_section`; `run()` enqueues `module_seeds` at startup alongside
the entry URL, as a floor under normal discovery, not a replacement for it.

**Already usable today, no code needed:** for a quick single-module crawl
right now (to test any fix above in isolation), `target.include_paths` already
restricts scope:

```yaml
target:
  include_paths: ["/screen", "/screen/*"]
```

**Effort:** ~1 day for the full budgets/seeds mechanism. **Depends on:**
nothing, but items 1-4 are worth having in first so a module-wise crawl isn't
just measuring the same old bugs at smaller scale.

---

### 7. `--module` flag — DONE

**What:** a thin CLI convenience — `qagen crawl --module screen` sets
`include_paths` for you, for fast one-off testing of any fix above.

**Effort:** ~2 hours. **Depends on:** item 6 (the budgets config it would
also apply).

---

## Part 2 — The order, as one table

| # | Item | Effort | Depends on |
|---|---|---|---|
| 1 | Ambiguous network calls (classifier + Cognito fix) | done | nothing |
| 2 | Retry on thin capture | ~half day | nothing |
| 3 | Settings tab de-duplication | ~half day | nothing (re-measure after 6) |
| 4 | Restore-failure tuning | ~1 hour | nothing |
| 5 | Cross-module boundary capture | ~half day | needs 6 to be exercised |
| 6 | Module budgets + seeds | ~1 day | benefits from 1-4 first |
| 7 | `--module` flag | ~2 hours | 6 |

**Total: roughly 3-3.5 days, plus your 5 minutes on item 1.**

**Suggested build order:** 1 → 2 → 4 → 3 → 6 → 5 → 7.

Reasoning: 1, 2, and 4 are independent and cheap — do them first so every
later run is measuring against cleaner data. 3 goes before 6 because Settings'
duplicate-tab problem is worth fixing before Settings gets its own generous
module budget (no point giving 50 slots to a module that's still recording
the same tab twice). 6 goes before 5 because the cross-module boundary logic
has nothing to do until a module restriction actually exists to trigger it.
7 is last because it's a convenience wrapper over 6, not a fix in its own
right.

---

## Part 3 — How to tell it worked

After each item, one thing to check rather than trusting it blind:

1. **Endpoints confirmed** → re-crawl Content/Places, check element counts rise
2. **Thin-capture retry** → `retry_thin_capture` count in the log should be
   low but nonzero; blank-looking screenshots for populated sections should
   stop appearing
3. **Settings dedup** → the two "Plan Details" screenshots become one node
4. **Restore tuning** → `state_abandoned` count in a fresh run should drop
   below the 22 seen before
5. **Module budgets** → re-run the full crawl; Settings should no longer be
   40%+ of all states; every module should show non-zero states
6. **Cross-module boundary** → a Screen-only crawl (`include_paths:
   ["/screen","/screen/*"]`) should show Content/Playlist/Schedule as single
   boundary nodes, each with a real screenshot, none with any outgoing edges
   of their own
7. **`--module` flag** → `qagen crawl --module screen` produces the same
   result as manually setting `include_paths`

---

## Implementation notes (added after building items 2-7)

- **Config split:** `samsungvx-200-final.yaml` was deliberately built with
  every cap lifted (its own header says so) to answer "how many states exist
  at all". Adding `module_budgets` there would have quietly undone that. A new
  file, `samsungvx-modules.yaml`, carries the module budgets/seeds instead --
  same target, different question ("how much of each module got covered").
- **`--module` sets `target.include_paths` for a single run** without editing
  any YAML; `samsungvx-modules.yaml`'s own `module_budgets`/`module_seeds`
  still apply underneath it for a *full*, unrestricted crawl.
- **Item 5's guard is exact:** it only activates when a same-origin
  navigation fails scope for the specific reason `"not in include_paths"` --
  a real exclusion (`/logout`, `/auth/**`) still behaves as it always has.
  Confirmed end-to-end: a full unrestricted crawl of the fixture reaches
  `settings.html` as a normal page, never as a boundary.
- **New tests:** `tests/test_module_boundary.py` (graph-level, pure) plus
  `TestInpageCanonicalisation`, `TestThinCaptureRetry`, `TestModuleBudgets`,
  `TestModuleSeeds` in `tests/test_policy_budgets.py`, plus four end-to-end
  tests in `tests/test_crawl_integration.py::TestCrossModuleBoundary` that
  exercise the real click-to-navigation path against the offline fixture
  (its dashboard cards navigate via `location.href` on click, which is what
  reaches `_perform`'s `NAVIGATION` branch -- the same path a live SPA's
  in-page navigation takes).
