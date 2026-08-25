# What happens when the website changes

Samsung VXT gets updated. Someone renames a button. Someone adds a new page.
What does that cost us, and how do we make it cost less?

---

## Part 1: Words used in this document

Read this part first. Everything after it uses these words.

### Screen (we call it a "state")

One thing you can look at. The Home page is a screen. The Home page **with the
`+` menu open** is a *different* screen, because it looks different and has
different buttons.

That is why 200 "states" does not mean 200 pages. It means 200 different things
you could be looking at.

### Selector — the address of a button

To click a button, the tool must be able to find it again later. A **selector**
is the address it writes down.

There are good addresses and bad addresses:

| Address | Example | Is it good? |
|---|---|---|
| **test id** | `[data-testid="dashboard_screen"]` | **Best.** The developers put this label on the button on purpose. It does not change when they redesign. |
| **id** | `#header_logo` | Good. Usually stays the same. |
| **name** | `role=button[name="Save"]` | Okay. Breaks if they rename the button to "Save changes". |
| **path** | `div > ul > li:nth-of-type(6)` | **Worst.** This means *"the 6th item in this list"*. If anything moves, the 6th item is now something else. |

### "nth" — counting position

`nth-of-type(6)` means **"the 6th one"**.

This is dangerous. If the tool writes down *"click the 6th row"*, and next week
a new row is added at the top, then the 6th row is now the wrong row. The click
still works — it just clicks the wrong thing. That is worse than failing.

### Fingerprint — a screen's ID card

The tool needs to know *"have I seen this screen before?"*, otherwise it goes in
circles forever.

So for every screen it makes a short code from the list of buttons on it. Same
buttons = same code = same screen, already seen, skip it.

Example: `853fdef4`

The problem: if even a small thing changes, the code changes, and the tool
thinks it is a brand new screen.

### Crawl

The tool opening the site and clicking through it. A full crawl of your site
takes **3 hours 19 minutes**.

### Replay — going back into a popup

A popup has no web address. You cannot type a URL to reach the `+` menu.

So to go back to it, the tool has to: open the page, then click `+` again. That
re-clicking is called **replay**.

Replay breaks easily. If the button moved, the replay fails.

### Confidence

The tool's own opinion of how good a button's address is.

`low` confidence = *"I found this button, but my address for it is weak and may
stop working."*

---

## Part 2: The problem

Right now, **any** change to your website costs the same:

```
Someone renames one button    ->  3 hours 19 minutes to re-crawl + full AI regeneration
Someone rebuilds the product  ->  3 hours 19 minutes to re-crawl + full AI regeneration
```

That is wrong. A tiny change should cost a tiny amount of work.

**The cost should match the size of the change. Right now it matches the size of
the website.**

---

## Part 3: Kinds of change, from smallest to biggest

### 1. The numbers change, the screen looks the same

Example: `Used 0` becomes `Used 1` because someone added a screen.

**How often:** All the time. It happened *while our own 3-hour crawl was
running.*

**What goes wrong:** The fingerprint changes. The tool thinks it is a new
screen and crawls it all over again.

**We saw this for real.** Fingerprints `853fdef4` and `d4e1cec6` are the same
Home page. They differ only because `Used 0` became `Used 1`.

**Do we handle it?** Half. We already turn numbers into `#`, so `Used 0` and
`Used 1` both become `used #` and match. But `Normal-` becoming `NormalNormal1`
is not a number, so it slips through and still creates a fake new screen.

### 2. A button gets renamed

Example: "Save" becomes "Save changes".

**What goes wrong:** Any button whose address was its *name* is now lost. That
is 8% of buttons.

**Do we handle it?** Mostly yes. 41% of buttons use a **test id**, which does not
care what the button says.

### 3. Things move around on the screen

Example: a button moves from the top-right to the bottom.

**What goes wrong:** Every address of the "6th item in the list" type is now
pointing at the wrong thing. Also, our test steps say things like *"the button
in the header, top-right"* — now wrong.

**Do we handle it?** Badly. See Part 4.

### 4. A new button is added to an existing screen

Example: a new "Duplicate" option inside the `+` menu.

**What goes wrong:** Nothing breaks — but we will not find the new button
unless we crawl that screen again.

### 5. A whole new page appears

Example: a new `/analytics` page.

**What goes wrong:** Nothing. **This is the case we handle best.** The new page
appears in the left menu, and the crawler finds it on its own.

### 6. A whole flow is redesigned

Example: what used to be a popup is now a full page. Or a new "Are you sure?"
step is added before deleting.

**What goes wrong:** A lot. The map is wrong, the replay paths are wrong, and
every test case about that flow has the wrong steps in the wrong order.

**This is the expensive one.** Nothing detects it except crawling again.

### 7. A feature is deleted

**What goes wrong:** Old test cases still mention it. They look fine on paper.
They fail when someone runs them. **Nothing in the tool notices this today.**

---

## Part 4: The one number that matters most

I checked how the tool wrote down the address of all 6,370 buttons it found:

| Kind of address | How many | Survives a redesign? |
|---|---:|---|
| test id | **41%** | **Yes** |
| path ("6th item in list") | **22%** | **No** |
| id | 14% | Usually |
| test id + "nth" | 13% | No, if list order changes |
| name | 8% | No, if renamed |

**Add up the position-based ones: about 24%.**

So roughly **one in four buttons is remembered as "the 6th thing in the list"**.
Those addresses break as soon as anything moves.

We already have proof they are weak. In the last crawl, **16 replays failed** —
the tool went back to click a button, and the button was not where it wrote down.
That happened within **minutes**:

```
[data-testid="search_systemtag_142"] no longer resolves
li._info-card-area-pc:nth-of-type(6) > ul > li.home-card... no longer resolves
```

If an address cannot survive 20 minutes, it will not survive a software release.

One more thing: **87% of our buttons are marked `low` confidence.** The tool
already knows its addresses are weak. It writes this down and then ignores it.

---

## Part 5: Four ways to fix this

### Way A — Just crawl everything again, every time

This is what we do now.

- **Work to build:** none, it already works
- **Cost each time:** 3 hours 19 minutes, even for a one-word change

**Keep this** as the "rebuild everything" button. It is the only option that
cannot miss anything. It should just not be the *normal* option.

### Way B — Check what changed first, then crawl only that

Before crawling properly, do a **fast check**: open each known page, take a quick
look, compare it with last time. Skip anything that looks the same. Only properly
crawl the pages that changed.

We already have the fast-look code, and last run's records are saved.

- **Speed:** 33 pages, about 4 seconds each = **about 3 minutes**, instead of 3
  hours 19 minutes
- **Work to build:** about half a day

**Problem to watch:** the numbers on your dashboard change every day (Part 3.1).
If we are not careful, the fast check will say *"everything changed!"* every
single night, and become useless.

**This gives the most value for the least work.** It turns *"did anything
change?"* from a 3-hour question into a 3-minute one.

### Way C — Only rewrite the test cases that are affected

Right now, if one screen changes, we regenerate **all** test cases. Instead, we
remember which screen each test case came from, and only rewrite the ones whose
screen changed.

- **Work to build:** about one day

**The real benefit is not speed.** Today every regeneration renumbers
everything, so `TC_047` is a different test case each time. You cannot compare
last week's tests with this week's, and you cannot tell which tests a release
broke. Fixing this makes the test suite something you keep, rather than
something you throw away and remake.

### Way D — Write down better addresses

Fix the 24% weak addresses directly:

1. **Write down two addresses per button**, not one. Try the good one first, fall
   back to the weak one. A test only fails if *both* are gone.
2. **Stop using "6th item" when there is a better option available.**
3. **Report weak addresses as a problem with the website.** A button with no test
   id and no readable name is genuinely hard to test — that is useful feedback
   for the VXT developers, not just our problem.

- **Work to build:** about one day

---

## Part 6: What I recommend

Do them in this order. They work together, they are not either/or.

| Order | Do this | Time | Why |
|---|---|---|---|
| 1 | **D** — better addresses | 1 day | Everything else depends on it |
| 2 | **B** — fast change check | half day | 3 hours becomes 3 minutes |
| 3 | **C** — rewrite only what changed | 1 day | Test numbers stop shifting |
| 4 | **A** — keep full crawl | 0 | Safety net |

**Why D must come first:**

B and C both rely on being able to say *"this screen is the same as last time"*.

But right now, a quarter of our addresses move whenever the page moves. So if we
build the fast check (B) first, it would report *"everything changed!"* every
night — because our own addresses moved, not because the site did.

A change detector that is wrong every night is worse than having no detector,
because people stop reading it.

So: fix the addresses first, then build the detector on top.

**Where this ends up:** a 3-minute check every night, a short crawl of only the
pages that changed, rewriting only the test cases affected, and a full rebuild
on whatever schedule you pick.

---

## Part 7: Three things this still will not fix

Being honest about the limits:

**1. A deleted feature.** Nothing tells us a screen that existed last week is
gone. Way B makes this easy to add, and it should be built in from day one.

**2. Screens that need data we do not have.** A "scheduled playlist" screen
cannot be found by an account with no scheduled playlists. We hit this wall many
times. The fix is putting test data in the account, not changing the crawler.

**3. Screens only an admin can see.** Everything here is one logged-in user. If a
feature only appears for administrators, we will never see it.
