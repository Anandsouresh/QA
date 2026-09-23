"""Build the front-end's demo fixtures from a real QAGen run directory.

The crawl data (graph, events, states, element geometry, screenshots) is REAL --
taken straight from the run. Only the test cases are synthesised, because the
recorded runs were crawl-only; they are still grounded in real selectors, real
element positions and real reachability paths, so the evidence panel draws
genuine boxes over genuine screenshots.

    python scripts/make_fixtures.py [../samsungvx-200-final05]
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRONT = HERE.parent
DATA = FRONT / "public" / "data"
SHOTS = FRONT / "public" / "artifacts"

RUN = Path(sys.argv[1]) if len(sys.argv) > 1 else FRONT.parent / "samsungvx-200-final05"

MODULE_LABEL = {
    "(home)": "Home", "screen": "Screen", "content": "Content", "playlist": "Playlist",
    "schedule": "Schedule", "channel": "Channel", "settings": "Settings",
    "apps": "Apps", "vxtlabs": "VXT Labs",
}
MODULE_TONE = {
    "Screen": "accent", "Content": "accent", "Playlist": "blue", "Schedule": "blue",
    "Channel": "violet", "Settings": "amber", "Home": "accent", "Apps": "muted",
    "VXT Labs": "muted", "Other": "muted",
}


def module_of(normalized_url: str) -> str:
    path = re.sub(r"^https?://[^/]+", "", normalized_url or "")
    parts = [p for p in path.split("/") if p]
    if not parts:
        return "Home" if normalized_url.startswith("http") else "Other"
    return MODULE_LABEL.get(parts[0].lower(), "Other")


def load(name: str):
    return json.loads((RUN / name).read_text(encoding="utf-8"))


# ── graph ──────────────────────────────────────────────────────────────────
graph = load("navgraph.json")
paths = load("navgraph-paths.json")
manifest = load("run_manifest.json")

for node in graph["nodes"]:
    node["module"] = module_of(node.get("normalized_url", ""))

# Keep a readable subgraph: the entry, everything at depth <= 2, and enough of
# the deeper tail to show the shape. 175 nodes renders, but 60 reads.
by_id = {n["id"]: n for n in graph["nodes"]}
keep: list[str] = []
for node in graph["nodes"]:
    if node.get("is_entry") or node["depth"] <= 1:
        keep.append(node["id"])
per_module: Counter = Counter()
for node in graph["nodes"]:
    if node["id"] in keep:
        continue
    if per_module[node["module"]] < 7:
        per_module[node["module"]] += 1
        keep.append(node["id"])
keep_set = set(keep)

sub_nodes = [by_id[i] for i in keep if i in by_id]
for n in sub_nodes:
    n["actions_total"] = len(n.get("actions", []))
    n["actions"] = n.get("actions", [])[:40]
    n["not_exercised_total"] = len(n.get("not_exercised", []))
    n["not_exercised"] = n.get("not_exercised", [])[:20]
sub_edges = [e for e in graph["edges"]
             if e["source"] in keep_set and e["target"] in keep_set]

(DATA / "graph.json").write_text(json.dumps({
    "target": graph["target"],
    "generated_at": graph["generated_at"],
    "entry_node": graph.get("entry_node", ""),
    "total_nodes": len(graph["nodes"]),
    "total_edges": len(graph["edges"]),
    "nodes": sub_nodes,
    "edges": sub_edges,
    "paths": {k: v for k, v in paths.items() if k in keep_set},
    "module_tone": MODULE_TONE,
}, indent=1), encoding="utf-8")
print(f"graph.json      {len(sub_nodes)} nodes / {len(sub_edges)} edges "
      f"(of {len(graph['nodes'])}/{len(graph['edges'])})")

# ── events ─────────────────────────────────────────────────────────────────
raw = (RUN / "crawl-log.jsonl").read_text(encoding="utf-8").splitlines()
events = []
for line in raw:
    line = line.strip()
    if not line:
        continue
    try:
        events.append(json.loads(line))
    except json.JSONDecodeError:
        continue
# A contiguous slice keeps the action -> outcome -> restore rhythm intact.
slice_ = events[:2600]
(DATA / "events.json").write_text(json.dumps(slice_, indent=1), encoding="utf-8")
print(f"events.json     {len(slice_)} events (of {len(events)})")

# ── states (page models, with real element geometry) ───────────────────────
pages_dir = RUN / "pages"
shot_for = {}
for node in graph["nodes"]:
    if node.get("screenshot"):
        shot_for[node["fingerprint"]] = node["screenshot"]

states = []
wanted = {n["fingerprint"] for n in sub_nodes}
for f in sorted(pages_dir.glob("*.json")):
    page = json.loads(f.read_text(encoding="utf-8"))
    fp = page.get("fingerprint") or f.stem
    if fp not in wanted:
        continue
    elements = [{
        "kind": e["kind"], "role": e["role"], "name": e["name"],
        "selector": e["selector"], "region": e.get("region", "main"),
        "location": e.get("location", ""), "enabled": e.get("enabled", True),
        "x": e.get("x", 0), "y": e.get("y", 0), "w": e.get("w", 0), "h": e.get("h", 0),
    } for e in page.get("elements", []) if e.get("visible", True)][:150]
    states.append({
        "fingerprint": fp,
        "url": page["url"],
        "normalized_url": page.get("normalized_url", ""),
        "title": page.get("title", ""),
        "module": module_of(page.get("normalized_url", "")),
        "depth": page.get("depth", 0),
        "arrival_action": page.get("arrival_action", ""),
        "viewport_width": page.get("viewport_width", 1200),
        "viewport_height": page.get("viewport_height", 900),
        "document_height": page.get("document_height", 900) or 900,
        "dom_nodes": page.get("dom_nodes", 0),
        "screenshot": shot_for.get(fp) or page.get("screenshot_path"),
        "blocked_mutations": page.get("blocked_mutations", [])[:8],
        "console_errors": page.get("console_errors", [])[:5],
        "elements": elements,
    })
_node_index = {n["fingerprint"]: i for i, n in enumerate(sub_nodes)}
states.sort(key=lambda s: _node_index.get(s["fingerprint"], 10**6))

(DATA / "states.json").write_text(json.dumps(states, indent=1), encoding="utf-8")
print(f"states.json     {len(states)} states, "
      f"{sum(len(s['elements']) for s in states)} elements")

# ── screenshots ────────────────────────────────────────────────────────────
copied = 0
for s in states:
    if not s["screenshot"]:
        continue
    src = RUN / s["screenshot"]
    if src.exists():
        shutil.copy2(src, SHOTS / src.name)
        s["screenshot"] = f"artifacts/{src.name}"
        copied += 1
    else:
        s["screenshot"] = None
(DATA / "states.json").write_text(json.dumps(states, indent=1), encoding="utf-8")
print(f"artifacts/      {copied} screenshots copied")

# ── test cases (synthesised, grounded in real selectors) ───────────────────
CATEGORIES = ["Happy Path", "Negative", "Edge Case", "UI/UX", "Form Filling"]

TEMPLATES = [
    ("Happy Path", "Open {name} from {where}", [
        ("Locate the {kind} labelled “{name}” in the {where}.",
         "The control is visible and enabled."),
        ("Activate it.", "The application responds without a console error."),
        ("Observe the resulting view.", "The expected panel or page is rendered in full."),
    ], "The control performs its action and the user lands in the expected state."),
    ("UI/UX", "“{name}” exposes an accessible name", [
        ("Move keyboard focus onto the {kind} at {where}.",
         "A visible focus ring appears on the control."),
        ("Read the control with a screen reader.",
         "The control announces a meaningful name, not its tag or position."),
        ("Press Enter.", "The control activates the same way a pointer click does."),
    ], "The control is operable by keyboard and announces a name that describes what it does."),
    ("Negative", "Reject an over-long value in {name}", [
        ("Focus the {kind} “{name}” in the {where}.", "The field accepts focus."),
        ("Enter a value longer than the field permits.",
         "Input stops at the maximum length."),
        ("Move focus out of the field.",
         "A validation hint appears and no request is sent."),
    ], "The form blocks the value and explains the limit on the field itself."),
    ("Edge Case", "“{name}” stays stable on rapid repeat activation", [
        ("Activate the {kind} “{name}” three times in quick succession.",
         "Only one request is issued."),
        ("Wait for the view to settle.", "No duplicate panel or overlay is left open."),
        ("Reload the page.", "The state is consistent with a single activation."),
    ], "Repeat activation is idempotent and leaves no duplicate state behind."),
    ("Form Filling", "Complete the {name} flow with valid input", [
        ("Open “{name}” from the {where}.", "The form is rendered with empty fields."),
        ("Fill every required field with valid values.",
         "Each field clears its own validation state."),
        ("Read the primary action.", "The primary action becomes enabled."),
    ], "Every required field accepts valid input and the primary action becomes available."),
]

INTERESTING = {
    "generic_button", "overlay_trigger", "tab", "menuitem", "switch",
    "text_input", "search", "select", "checkbox", "submit", "inferred_clickable",
}

cases = []
tc = 1
for state in states:
    node = next((n for n in sub_nodes if n["fingerprint"] == state["fingerprint"]), None)
    if node is None:
        continue
    route = paths.get(node["id"]) or []
    pre = ["User is signed in"]
    if state["module"] != "Home":
        pre.append(f"{state['module']} module is open")
    if node.get("opened_by"):
        pre.append(f"“{node['opened_by']}” has been activated")

    picks = [e for e in state["elements"]
             if e["kind"] in INTERESTING and e["name"].strip() and e["region"] == "main"]
    picks = picks[:6]
    for i, el in enumerate(picks):
        cat, title, steps, overall = TEMPLATES[(tc + i) % len(TEMPLATES)]
        name = el["name"][:44].strip()
        kind = el["kind"].replace("_", " ")
        where = el["location"] or "main area"
        cases.append({
            "test_id": f"TC_{tc:03d}",
            "category": cat,
            "title": title.format(name=name, where=where, kind=kind),
            "preconditions": pre,
            "steps": [{
                "step_number": j + 1,
                "action": a.format(name=name, where=where, kind=kind),
                "expected_result": r,
            } for j, (a, r) in enumerate(steps)],
            "overall_expected_result": overall,
            "source_state": node["id"],
            "source_fingerprint": state["fingerprint"],
            "source_url": state["url"],
            "module": state["module"],
            "source_selectors": [el["selector"]],
            "highlight": {"x": el["x"], "y": el["y"], "w": el["w"], "h": el["h"],
                          "label": el["selector"]},
            # Transformed containers (carousels, drawers) can report a position
            # outside the captured page. Say so rather than drawing a box in the
            # wrong place.
            "highlight_valid": (
                el["x"] >= 0 and el["y"] >= 0 and el["w"] > 0 and el["h"] > 0
                and el["y"] + el["h"] <= state["document_height"] + 20
            ),
            "reachability": route,
            "needs_review": (tc % 11 == 0),
            "review_notes": (["Element has no accessible name in the DOM; the step text "
                              "relies on a hover tooltip."] if tc % 11 == 0 else []),
            "constraints": ([
                {"k": "required", "v": "true"}, {"k": "maxlength", "v": "50"},
                {"k": "pattern", "v": "^[^<>]+$"},
                {"k": "label", "v": name or "(unnamed)"},
            ] if el["kind"] in {"text_input", "search"} else []),
        })
        tc += 1

(DATA / "cases.json").write_text(json.dumps(cases, indent=1), encoding="utf-8")
print(f"cases.json      {len(cases)} cases "
      f"({sum(1 for c in cases if c['needs_review'])} need review)")

# ── run summary ────────────────────────────────────────────────────────────
crawl = manifest.get("crawl", {})
budgets = crawl.get("budgets", {})
mod_counts = Counter(n["module"] for n in graph["nodes"])
(DATA / "run.json").write_text(json.dumps({
    "id": "2026-09-12-vx",
    "target": graph["target"],
    "status": "running",
    "started_at": manifest.get("started_at"),
    "duration_seconds": manifest.get("duration_seconds"),
    "auth_status": manifest.get("auth_status"),
    "states_discovered": crawl.get("states_discovered"),
    "graph_nodes": crawl.get("graph_nodes"),
    "graph_edges": crawl.get("graph_edges"),
    "actionable_elements": crawl.get("actionable_elements"),
    "total_elements": crawl.get("total_elements"),
    "blocked_mutations": crawl.get("blocked_mutations", [])[:12],
    "skipped_elements": crawl.get("skipped_elements", [])[:40],
    "budgets": budgets,
    "module_budgets": {
        "Screen": 40, "Content": 40, "Playlist": 30,
        "Schedule": 30, "Channel": 20, "Settings": 40,
    },
    "module_states": dict(mod_counts),
    "config": {
        "depth": manifest.get("config", {}).get("target", {}).get("depth"),
        "headless": manifest.get("config", {}).get("browser", {}).get("headless"),
        "block_mutations": manifest.get("config", {}).get("browser", {}).get("block_mutations"),
        "model": manifest.get("config", {}).get("llm", {}).get("model"),
        "deny_text": manifest.get("config", {}).get("interaction", {}).get("deny_text", [])[:8],
    },
}, indent=1), encoding="utf-8")
print("run.json        written")
print("\nfixtures ready in", DATA)
