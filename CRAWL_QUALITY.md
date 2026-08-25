# Making the crawl do a good job

Diagnosis of why the crawler under-covers a real SPA, with the fix for each
issue. Every problem below is evidenced from actual runs against
`www.samsungvx.com`, not predicted.

**The headline number:** on the depth-0 probe the entry page had **17
actionable elements** and the crawler exercised **1** of them. That is the
problem to fix, and issue #1 explains almost all of it.

---

## Evidence

From `crawl-log.jsonl` on two runs:

| Run | States | Actions attempted | Restore failures | Actionable available |
|---|---:|---:|---:|---|
| `vx-probe` (depth 0) | 1 | 1 | **1 of 1** | 17 on the entry page |
| `samsungvx-fast` (depth 1) | 5 | 10 | **2 of 10** | 13–35 per state |

Ten actions across five states, on states carrying 13–35 actionable elements
each. Coverage is roughly **10%**, and it is not the budgets doing it — the run
stopped with `clicks 10/12` and `pages 5/8` unspent.

---

## Issue 0 — the "+" on a card was never extracted at all — **FIXED**

**Severity: critical. Everything below is downstream of it.**

### What happened

`looksClickable` rejected any element with a `cursor: pointer` **ancestor**. Its
comment claimed the opposite ("keep the innermost target"), but the code kept
the *outermost*. On the samsungvx dashboard, where each card is itself
clickable, that discarded every control inside every card:

```
pointer-cursor candidates on the homepage : 78
kept by the old ancestor rule             : 16
dropped because an ancestor was pointer   : 62
```

The `+` buttons, the workspace switcher, the notification bell and the crown
badge were not under-tested — they were **absent from the inventory**.

### Why one element at a time cannot decide this

A card is clickable *and* carries its own action buttons. Both are real,
separate test targets, so no rule that looks at a single element in isolation
gets it right. Extraction is now two-phase: collect every pointer-cursor
candidate, then decide which survive by looking at the set as a whole.

Four rejection rules, in `resolveClickables`:

| Rule | Rejects | Because |
|---|---|---|
| inside a native control | a `<span>` in a styled `<a>` | `cursor` is inherited; the link is the target |
| pass-through | a shell the same size as its child | one control, not two — tie broken by which side has a `data-testid`/stable `id` |
| container | something holding ≥2 candidates each ≥25% of its area | that is a row or grid, not a control |
| text echo | a child repeating an enclosing candidate's exact text | the card title span duplicates its card |

Measuring *area share* rather than counting children is what separates a grid
row from a card: a card's `+` is tiny next to the card, so the card survives as
a click target **and** its buttons survive alongside it.

### The second half: naming what was found

The `+` has no `aria-label`, no `title` and no text — the accname ladder returns
`""`, which is useless in a test step. Its only label is the tooltip the app
reveals on hover, so `PageAnalyzer._name_by_hover` hovers unnamed actionable
elements and reads the revealed text (`crawl.hover_naming`, capped at
`hover_naming_limit` per page).

Hover-derived names are deliberately excluded from `Element.signature()`:
whether the tooltip won the race is a property of our probe, not of the page,
and letting it in would fingerprint one state two different ways.

### Result on the live dashboard

| | before | after |
|---|---:|---:|
| elements extracted from the homepage | 21 | 29 |
| card `+` buttons found | 0 | 4 |
| named `New` by hover | — | 4 |

Six offline regression tests cover the nesting rules and hover naming.

---

## Issue 0b — the menu the "+" opens: four bugs in a row — **FIXED**

Extracting the `+` (issue 0) only got as far as clicking it. Following what it
opens meant fixing four separate things, each of which independently hid the
menu. On the live dashboard the chain now reads:

```
click 'New' [dashboard_screen_newbtn]      -> in_page_state
overlay_open  N008 revealed 3 item(s) via 'New'
   click 'Add Screen'       [dashboard_screen_addbtn_addscreen]     -> in_page_state
   click 'New Screen Wall'  [dashboard_screen_addbtn_newscreenwall] -> in_page_state
```

### 1. Analytics beacons made every click look like a write

The write-guard counted any POST as a mutation. This app sends a Google
Analytics `button_click` beacon on **every** click, so 46 of 46 "blocked
mutations" in one run were GA and not one was the app — and `_classify_outcome`
ranks `BLOCKED_MUTATION` above "nothing happened", so clicking `+` was reported
as a blocked write rather than as the click it was.

Telemetry hosts (`_TELEMETRY_HOSTS` in `session.py`) are still aborted — crawl
traffic does not belong in anyone's analytics — but no longer *recorded* as
application writes. Blocked mutations on that run: 46 → 1.

### 2. The fingerprint could not see a React menu

`interactive_signature` excluded pointer-cursor elements wholesale. That rule
was right about the churn it was written for, but it also meant a menu built
from `div`s changed nothing: clicking `+` revealed "Add Screen" and "New Screen
Wall" and the fingerprint did not move.

The split that works is **selector stability**: a pointer-cursor element found
by `data-testid` or a real `id` is a control the app named on purpose and is
there on every render; one found by css-path is a div that happened to look
clickable this time. The first kind now counts toward state identity
(`Element.stable_selector`), the second still does not.

### 3. The fast path never got as far as the fingerprint

`_perform` compares a cheap signature first and only pays for a real extraction
if it differs — and that cheap signature queried `a,button,input,[role]…`, which
a div menu does not match. So the fix above never ran. `SIGNATURE_JS` now also
records identifier-bearing pointer-cursor elements, by identifier only and never
by text, so a counter still cannot move it.

### 4. A late-committing route change looked like an in-page state

A client-side navigation can commit *during* the extraction, so the URL sampled
a moment earlier is stale. `_perform` now trusts the URL the extraction actually
saw. Without this a card click was recorded as an in-page state, and the next
page's elements would have been traversed as if they were a menu's contents.

### The traversal itself

`Crawler._act_in_place` exercises what a click revealed **while it is still
open**. This is the cheap half of issue 4 below: replay exists to *return* to an
overlay later, but the click that opened this one happened a moment ago, so we
are already standing in it. Re-opening between items costs one click on the
trigger's own selector.

Which elements are "the menu" is a **DOM diff** — elements that were not there
before — not the overlay detector. A dropdown anchored under a `+` covers a few
percent of the viewport and fails every size-based overlay heuristic there is,
but "these were not here a moment ago" needs no heuristic.

Bounded by `crawl.max_overlay_items` (8) and `crawl.max_overlay_depth` (1).

### Modelled as a variant, not a sibling

A menu state is the same page with something on top of it. Recorded as a plain
node it is a second entry with an identical title and no indication of how to
reach it. `NavNode` now carries `parent_state` and `opened_by`, the title reads
`HOME | Samsung VXT CMS — New`, and a purely additive change is typed
`dropdown` rather than `page` (a tab switch *replaces* content, so it stays a
page).

`max_states_per_url` went 3 → 6: one page legitimately carries a modal, a
disclosure panel and a card menu, and at 3 whichever was reached last was
silently dropped.

---

## Issue 0c — the app frame ate the crawl — **FIXED**

**Severity: critical for coverage. Measured, not predicted.**

### What the captured DOM shows

Samsung VXT is a classic CMS shell: a header and a left menu that never move,
and a main area the menu swaps around. Clicking "Content" in the left menu
leaves the menu exactly where it is.

Counting ids across the 60 captured HTML files of one run:

| | |
|---|---|
| states in `/settings` | **43 of 63** |
| states in `/screen`, `/schedule`, `/channel` | **0** |
| states where the 11-item Settings menu was re-extracted | **41** |

Two thirds of the crawl went into one section, the primary product areas were
never reached, and the same eleven menu items were processed forty-one times.

### Fix 1 — know which elements are the frame

`ShellDetector` (`qagen/browser/shell.py`) marks every element `shell` or
`main`, two ways:

* **declared** — `crawl.shell_selectors`, matched as substrings against the
  emitted selector. Exact and instant when you know the app. (Bare tokens, not
  `#id`: the extractor prefers `data-testid`, so the same control can arrive as
  `[data-testid="navbar_li_screen"]` or `#navbar_li_screen`.)
* **observed** — an element identity seen on `shell_min_urls` (3) different URLs
  is part of the frame by definition. No configuration, works on an app nobody
  has tuned.

It is deliberately **advisory**: it never removes an element and never touches a
fingerprint, so a wrong guess costs ordering, not coverage.

Used for two things:

* `_plan_actions` ranks content-area elements **first**. When the budget cuts a
  state short, what is lost is furniture rather than product.
* `Main` in the CLI table and `main_actionable_count` on each node — a Settings
  page reporting 38 actionable elements of which 27 are the header and the left
  menu is really an 11-element page.

### Fix 2 — no section may swallow the crawl

`crawl.max_states_per_section` (default 12, set to 10 for this target) caps
states per top-level path segment, so `/settings` cannot take 43 of 63 while
`/screen` waits forever.

### Result

`Playlist` now reports **11 main-actionable of 23 extracted** — the twelve frame
elements correctly discounted — and the run reports `276 actionable elements
(184 outside the app frame)`.

**Still open:** wall clock, not budgets, ends these runs. Each click costs ~9s,
almost all of it settle and loader waits, so ~45 clicks fill 420 seconds. That
is now the binding constraint on coverage — see issue 7.

---

## Issue 1 — a failed restore silently abandons the rest of the state

**Severity: critical. This is most of the missing coverage.**

### What happens

`Crawler._act_on_state` walks the ranked action plan. After each click it calls
`_restore()`, and:

```python
restored = await self._restore(page, model)
if not restored:
    return          # every remaining action on this state is abandoned
```

One failed restore on the *first* action discards the other 16. That is exactly
what the `vx-probe` log shows: `action` → `restore: FAILED` → `finished`.

### Why restore fails so often here

`_restore` tries Escape → back → goto, and accepts only when the **cheap
signature matches byte-for-byte**. On this app the third attempt reloads the
page, React re-renders, and cards arrive in a slightly different order or with
different data — so the signature legitimately differs even though the page is,
for testing purposes, the same page. Restore reports failure for a page that
came back fine.

### Fix

Two changes, both small:

**1a. Never abandon the state — re-establish it and continue.**

```python
restored = await self._restore(page, model)
if not restored:
    consecutive_failures += 1
    if consecutive_failures >= 3:
        self.log.note("state_abandoned", f"{node.id}: 3 consecutive restore failures")
        return
    # Hard reset and re-plan against whatever we land on, rather than
    # discarding every remaining action.
    await page.goto(model.url, wait_until="domcontentloaded")
    await self.analyzer.settle(page)
    await self.analyzer.dismiss_consent(page)
    continue
else:
    consecutive_failures = 0
```

**1b. Compare with tolerance, not byte equality.**

Restore's job is "are we back somewhere we can act from", not "is the DOM
identical". Accept when **all** of these hold:

- the URL matches the state's URL
- no non-transient overlay is open (nothing is covering the page)
- the set of *actionable* element names matches within a tolerance (say 85%),
  using the digit-normalised names `Element.signature()` already produces

That last rule is the important one: it makes restore immune to a counter
ticking or a list gaining a row, which is what currently breaks it.

**Cost:** ~30 lines in `crawler.py` plus a helper in `analyzer.py`.
**Risk:** low. Worst case a state is re-planned once more than necessary.
**Expected gain:** the largest single improvement available — this alone should
take per-state coverage from ~2 actions to most of the plan.

---

## Issue 2 — coverage is invisible, so nobody notices it is 10%

**Severity: high (it hides everything else).**

### What happens

The run summary reports states, transitions, clicks and blocked writes. None of
those reveal that 17 actionable elements produced 1 action. The crawl looked
successful in every report while covering almost nothing.

### Fix

Track attempts per state and report the ratio. `NavNode` already carries
`actionable_count`; add `exercised_count` and emit:

```
N001  HOME   exercised 1 of 17 actionable   (6%)
```

in the CLI table, `states.md`, and the graph inspector. Add a run-level warning
when the median falls below ~50%:

```
! low coverage: median 12% of actionable elements exercised per state
```

**Cost:** ~20 lines.
**Risk:** none.
**Why it matters:** this is the metric that tells you whether any other fix
worked. Build it first, then fix issue 1 and watch the number move.

---

## Issue 3 — a click that does nothing is recorded as "inert" on first try

**Severity: medium. Main cause of run-to-run variance.**

### What happens

The nav items on this app are `div`s detected by `cursor: pointer`. React binds
their handlers after hydration. If the click lands a moment early, nothing
happens, and `_classify_outcome` records `NO_CHANGE` + `inert` permanently. A
later run whose timing differs records a real navigation. That is why one run
found 19 distinct URLs and another found 11 — same code, same site.

The `samsungvx-fast` log shows `no_change: 1` out of 9 outcomes, and this is
also why a genuinely reachable page sometimes never enters the frontier.

### Fix

Retry once before believing a `NO_CHANGE` on a low-confidence element:

```python
if outcome is Outcome.NO_CHANGE and el.pointer_cursor:
    await asyncio.sleep(0.4)
    await locator.click(...)            # one retry
    await self.analyzer.settle(page)
    # re-classify; only record NO_CHANGE if it happens twice
```

Only retry when the element is `pointer_cursor` or `INFERRED_CLICKABLE` — a
native `<button>` that does nothing really is inert, and retrying every button
doubles the click budget for no gain.

**Cost:** ~15 lines in `_perform`.
**Risk:** low; bounded by one extra click on low-confidence elements only.
**Gain:** should substantially reduce the run-to-run variance.

---

## Issue 4 — modals are captured but never traversed

**Severity: high for test-case quality.**

### What happens

A click producing `IN_PAGE_STATE` creates a node, captures a screenshot, lists
the modal's action elements — and stops. The crawler never clicks anything
*inside* the modal. Modals are where forms, confirmations and destructive
guards live, so the highest-value surface is inventoried but never exercised.

The blocker is not ordering, it is **replay**: a modal has no URL, and the
frontier holds URLs, so a modal state cannot be enqueued.

### Fix

Make a frontier item a **path** rather than a URL:

```python
@dataclass
class FrontierItem:
    url: str | None
    replay: list[NavEdge] | None      # edges to re-execute from entry
    depth: int
    arrival_action: str
```

`GraphBuilder.shortest_paths()` already produces exactly this list, and every
edge already carries a verified selector — the machinery exists. `_visit` grows
a branch: if `replay` is set, navigate to the entry URL and re-execute each
edge's action in order, then proceed normally.

Guard rails this needs:

- a `max_replay_depth` (2 is plenty — modal, then one nested dialog)
- a `replay_failed` outcome when an intermediate selector no longer resolves
  (the row you clicked may be gone)
- a replay budget, because each modal action costs a full replay: navigate +
  N clicks + N settles, which at current timeouts is 15–30s **per action**

**Cost:** the largest item here — a day, not an afternoon.
**Risk:** medium. Replay is inherently fragile against a live app.
**Recommendation:** do issues 1–3 first. They are cheap and they raise coverage
on states you can already reach; this one opens new territory but is costly per
unit of coverage.

**Update:** the cheap half of this is done — see issue 0b. `_act_in_place`
exercises an overlay's items at the moment it opens, which covers menus and
single-level dialogs without any replay at all. What remains here is genuinely
the expensive part: returning to an overlay on a *later* visit, which is only
needed for nested overlays.

---

## Issue 5 — the same popup on different pages becomes many nodes

**Severity: medium. Best effort-to-value ratio of the structural changes.**

### What happens

`compute_fingerprint` mixes the normalised URL into state identity. A "Delete
confirmation" dialog reachable from 12 pages therefore becomes 12 unrelated
nodes, and generates the same test case 12 times.

### Fix

An **overlay-only fingerprint**. When a non-transient overlay is open, identify
the state by the overlay subtree alone, ignoring the page behind it:

```python
def overlay_fingerprint(overlays, elements):
    inside = [e for e in elements if e.in_overlay]     # new flag from EXTRACT_JS
    return sha256(interactive_signature(inside) + overlay_label)
```

Every page that opens it then points at one node with 12 inbound edges — test
it once, and the graph shows every entry point.

Two guards worth designing in:

- do **not** collapse when the overlay's accessible name differs; a delete
  dialog on Screen and on Playlist may look alike but destroy different things
- keep every inbound edge, so context stays visible in the graph

This is the same idea as collapsing `/item/1…50` into `/item/{id}`, applied to
overlays instead of URLs — and it shrinks the problem issue 4 has to solve,
because each distinct popup then needs traversing once rather than once per
page it appears on.

**Cost:** ~40 lines (an `in_overlay` flag in the extraction script, plus a
branch in `compute_fingerprint`).
**Risk:** low, with the name guard in place.

---

## Issue 6 — global dedup can hide context-specific behaviour

**Severity: low, but worth knowing.**

`_exercised` skips an element identity after its first use anywhere. That was
the right call for the VXT assistant and header nav — it stopped the click
budget being spent on the same control on every page. The `samsungvx-fast` log
shows 8 skips of this kind, all correct.

The cost: a control that appears identical but behaves differently per page
(a "Save" button on two different forms) is exercised once and assumed
everywhere. If that becomes a problem, key the identity on
`(selector, name, node_type)` rather than `(role, name, selector)`, so a control
inside a modal is treated as distinct from the same-looking one on a page.

No change recommended yet — wait until a real case appears.

---

## Issue 7 — configuration is currently tuned against itself

**Severity: medium. Free to fix.**

`samsungvx.yaml` has `depth: 5` with `hydration_timeout_ms: 25000`,
`loader_timeout_ms: 20000` and `post_loader_wait_ms: 5000`. A full run takes
~9 minutes and reaches 7 states. The earlier `depth: 1` runs found **more**
distinct URLs in **less** time, because depth-5 spends the wall clock
re-walking deep paths instead of widening.

### Recommended settings

```yaml
target:
  depth: 2                    # breadth beats depth on this app

crawl:
  settle_timeout_ms: 4000
  hydration_timeout_ms: 12000
  hydration_min_elements: 4
  loader_timeout_ms: 10000
  post_loader_wait_ms: 2000   # 5s was generous; the loader wait does the work
  stability_ms: 800
  max_clicks_per_state: 40    # states here have 13-35 actionable elements
  max_wall_clock_seconds: 900
```

The point of `post_loader_wait_ms` is to catch content rendering just behind the
spinner. 2s covers that; the remaining 3s was pure cost, charged on every state
that shows a loader.

---

## Order to do this in

| # | Change | Cost | Gain |
|---|---|---|---|
| 0 | Nesting-aware clickable resolution + hover naming (issue 0) | **done** | Recovered 62 of 78 lost controls |
| 0c | App-frame awareness + per-section budget (issue 0c) | **done** | Settings can no longer take 68% of the crawl |
| 0b | Same-page menus: detected, traversed in place, modelled as variants (issue 0b) | **done** | "Add Screen" / "New Screen Wall" now reached |
| 1 | Coverage metric (issue 2) | ~20 lines | Makes everything else measurable |
| 2 | Restore no longer abandons the state (issue 1) | ~30 lines | **Largest single gain** |
| 3 | Tolerant restore comparison (issue 1b) | ~20 lines | Removes most restore failures |
| 4 | Retry once on inert low-confidence clicks (issue 3) | ~15 lines | Cuts run-to-run variance |
| 5 | Config retune (issue 7) | config only | Faster runs, more breadth |
| 6 | Overlay-only fingerprint (issue 5) | ~40 lines | Deduplicates shared popups |
| 7 | Path-replay frontier (issue 4) | ~1 day | Opens modal interiors |

Items 1–5 are roughly half a day together and should move coverage from ~10% to
most of each state's action plan. Items 6 and 7 are the structural work, and
they are worth doing in that order — 6 makes 7 cheaper.

---

## How to tell it is working

After each change, run the fast profile and watch three numbers:

```
python -m qagen.cli crawl --config samsungvx-fast.yaml
```

1. **Exercised / actionable per state** — the metric from issue 2. Target: >60%.
2. **Restore failure rate** — from `crawl-log.jsonl`:
   ```
   python -c "import json,collections;rows=[json.loads(l) for l in open('samsungvx-fast/crawl-log.jsonl',encoding='utf-8')];print(collections.Counter((r['event'],r.get('ok')) for r in rows if r['event']=='restore'))"
   ```
   Target: under 10%.
3. **Distinct URLs across two consecutive runs** — the variance check. They
   should agree to within one or two.

Run the same profile twice before and after each change. On a live SPA a single
run is not evidence.
