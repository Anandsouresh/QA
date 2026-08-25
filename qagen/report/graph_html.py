"""Self-contained interactive view of the navigation graph.

Emits a single ``navgraph.html`` with the graph data and every screenshot
inlined as a data URI, so it opens from disk with no server and no assets
directory. Mermaid renders the same graph as a static picture; this is for
actually working with the result -- selecting a state, reading its action
inventory, seeing the screenshot the crawler captured.

Layout is layered by reachability depth from the entry node rather than
force-directed: depth is real information the crawl produced, and a spring
layout would spend that information on looking busy.
"""

from __future__ import annotations

import base64
import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

from ..models import NavGraph

_MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}

#: Outcomes that represent a transition a tester could actually follow.
_TRAVERSABLE = {"navigation", "in_page_state"}


def _data_uri(path: Path) -> str | None:
    try:
        raw = path.read_bytes()
    except Exception:
        return None
    mime = _MIME.get(path.suffix.lower(), "application/octet-stream")
    return f"data:{mime};base64," + base64.b64encode(raw).decode("ascii")


def _depths(graph: NavGraph) -> dict[str, int]:
    """BFS depth from the entry node over traversable edges."""
    adjacency: dict[str, list[str]] = defaultdict(list)
    for edge in graph.edges:
        if edge.outcome.value in _TRAVERSABLE and edge.source != edge.target:
            adjacency[edge.source].append(edge.target)

    depth = {graph.entry_node: 0} if graph.entry_node else {}
    queue = deque(depth)
    while queue:
        current = queue.popleft()
        for nxt in adjacency.get(current, []):
            if nxt not in depth:
                depth[nxt] = depth[current] + 1
                queue.append(nxt)

    # Anything unreachable by a followable edge (boundaries, blocked targets)
    # sits in a trailing column rather than being hidden.
    if depth:
        orphan_column = max(depth.values()) + 1
    else:
        orphan_column = 0
    for node in graph.nodes:
        depth.setdefault(node.id, orphan_column)
    return depth


def build_payload(graph: NavGraph, out_dir: Path, manifest: dict[str, Any] | None = None) -> dict:
    depth = _depths(graph)
    nodes = []
    for node in graph.nodes:
        shot = None
        if node.screenshot:
            shot = _data_uri(out_dir / node.screenshot)
        nodes.append(
            {
                "id": node.id,
                "title": node.title or node.normalized_url,
                "url": node.url,
                "path": node.normalized_url,
                "type": node.node_type,
                "depth": depth.get(node.id, 0),
                "crawlDepth": node.depth,
                "elements": node.element_count,
                "actionable": node.actionable_count,
                "dom": node.dom_nodes,
                "visits": node.visit_count,
                "isEntry": node.is_entry,
                "actions": node.actions,
                "notExercised": node.not_exercised,
                "shot": shot,
                "html": node.html,
            }
        )

    edges = [
        {
            "id": e.id,
            "source": e.source,
            "target": e.target,
            "label": e.label,
            "action": e.action,
            "outcome": e.outcome.value,
            "annotations": e.annotations,
            "selector": e.selector,
            "value": e.input_value,
        }
        for e in graph.edges
    ]

    crawl = (manifest or {}).get("crawl", {})
    budgets = crawl.get("budgets", {})
    summary = {
        "target": graph.target,
        "generated": graph.generated_at.isoformat(timespec="seconds"),
        "states": len(graph.nodes),
        "transitions": len(graph.edges),
        "actionable": sum(n.actionable_count for n in graph.nodes),
        "elements": sum(n.element_count for n in graph.nodes),
        "clicks": budgets.get("clicks_made"),
        "skipped": len(crawl.get("skipped_elements", []) or []),
        "blocked": len(crawl.get("blocked_mutations", []) or []),
        "stopReason": budgets.get("stop_reason"),
        "seconds": (manifest or {}).get("duration_seconds"),
        "boundaries": [b.get("origin") for b in crawl.get("boundaries", []) or []],
    }
    return {"summary": summary, "nodes": nodes, "edges": edges}


def render(payload: dict) -> str:
    return _TEMPLATE.replace("__PAYLOAD__", json.dumps(payload))


def write(
    graph: NavGraph, out_dir: Path, manifest: dict[str, Any] | None = None
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "navgraph.html"
    path.write_text(render(build_payload(graph, out_dir, manifest)), encoding="utf-8")
    return path


_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Crawl schematic</title>
<style>
/* ---- tokens: complete light palette on bare :root ---------------------- */
:root{
  --paper:#eef2f5; --surface:#ffffff; --surface-2:#e3eaf0; --raised:#f7fafc;
  --ink:#0d1b26; --ink-2:#3d5364; --ink-3:#6d8496;
  --line:#c7d5e0; --line-soft:#dfe8ee;
  --accent:#0d7d9c; --accent-ink:#ffffff; --accent-soft:#d5ecf3;
  --ok:#2c7a56; --warn:#9c6318; --stop:#b03a47; --inert:#7f92a1;
  --shadow:0 1px 2px rgba(13,27,38,.07), 0 8px 24px rgba(13,27,38,.06);
  --mono:ui-monospace,"Cascadia Mono","SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  --sans:ui-sans-serif,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#071219; --surface:#0d1d28; --surface-2:#142835; --raised:#12242f;
    --ink:#e4eef5; --ink-2:#a6bfcf; --ink-3:#6f8ca0;
    --line:#1e3444; --line-soft:#162936;
    --accent:#4ec7ea; --accent-ink:#04222e; --accent-soft:#0b2c3a;
    --ok:#4fb587; --warn:#d99b4a; --stop:#e0697a; --inert:#6d8395;
    --shadow:0 1px 2px rgba(0,0,0,.5), 0 10px 30px rgba(0,0,0,.4);
  }
}
:root[data-theme="dark"]{
  --paper:#071219; --surface:#0d1d28; --surface-2:#142835; --raised:#12242f;
  --ink:#e4eef5; --ink-2:#a6bfcf; --ink-3:#6f8ca0;
  --line:#1e3444; --line-soft:#162936;
  --accent:#4ec7ea; --accent-ink:#04222e; --accent-soft:#0b2c3a;
  --ok:#4fb587; --warn:#d99b4a; --stop:#e0697a; --inert:#6d8395;
  --shadow:0 1px 2px rgba(0,0,0,.5), 0 10px 30px rgba(0,0,0,.4);
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:var(--sans); font-size:15px; line-height:1.55;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3{margin:0; text-wrap:balance}

/* instrument-panel labelling: the mono face is the display face here */
.label{
  font-family:var(--mono); font-size:10.5px; font-weight:600;
  letter-spacing:.14em; text-transform:uppercase; color:var(--ink-3);
}
.mono{font-family:var(--mono); font-size:12.5px}
.tnum{font-variant-numeric:tabular-nums}

/* ---- header ------------------------------------------------------------ */
header{
  border-bottom:1px solid var(--line); background:var(--surface);
  padding:18px clamp(16px,3vw,28px);
  display:flex; flex-wrap:wrap; gap:20px 32px; align-items:flex-end;
  justify-content:space-between;
}
.brand h1{
  font-family:var(--mono); font-size:clamp(17px,2.4vw,22px); font-weight:700;
  letter-spacing:.1em; text-transform:uppercase;
}
.brand .sub{color:var(--ink-2); font-size:13px; margin-top:4px; word-break:break-all}
.stats{display:flex; flex-wrap:wrap; gap:8px}
.stat{
  background:var(--surface-2); border:1px solid var(--line-soft);
  border-radius:3px; padding:7px 11px; min-width:74px;
}
.stat .n{font-family:var(--mono); font-size:17px; font-weight:700; font-variant-numeric:tabular-nums}
.stat .k{font-family:var(--mono); font-size:9.5px; letter-spacing:.12em;
  text-transform:uppercase; color:var(--ink-3); margin-top:1px}
.stat.alert .n{color:var(--stop)}

/* ---- layout ------------------------------------------------------------ */
main{
  display:grid; grid-template-columns:minmax(0,1fr) 390px;
  gap:0; align-items:stretch; min-height:calc(100vh - 92px);
}
@media (max-width:1020px){ main{grid-template-columns:minmax(0,1fr)} }

.canvas-pane{display:flex; flex-direction:column; min-width:0; background:var(--paper)}
.toolbar{
  display:flex; flex-wrap:wrap; gap:14px 18px; align-items:center;
  padding:12px clamp(16px,3vw,28px); border-bottom:1px solid var(--line-soft);
}
.filters{display:flex; flex-wrap:wrap; gap:6px}
.filter{
  display:inline-flex; align-items:center; gap:6px; cursor:pointer;
  border:1px solid var(--line); background:var(--surface); color:var(--ink-2);
  border-radius:3px; padding:5px 9px;
  font-family:var(--mono); font-size:10.5px; letter-spacing:.09em; text-transform:uppercase;
}
.filter:hover{border-color:var(--accent)}
.filter input{margin:0; accent-color:var(--accent)}
.filter .swatch{width:16px; height:3px; border-radius:2px}
.filter[data-off="1"]{opacity:.42}
.hint{color:var(--ink-3); font-size:12px; margin-left:auto}

.scroller{overflow:auto; flex:1; padding:8px clamp(8px,2vw,20px) 24px}
svg{display:block; min-width:100%}
.node rect{
  fill:var(--surface); stroke:var(--line); stroke-width:1.5px;
  transition:stroke .12s ease, fill .12s ease;
}
.node.entry rect{stroke:var(--accent); stroke-width:2.5px}
.node.boundary rect, .node.external rect{
  fill:var(--surface-2); stroke-dasharray:4 3;
}
.node .stripe{stroke-width:0}
.node .t{font-family:var(--sans); font-size:12.5px; font-weight:600; fill:var(--ink)}
.node .p{font-family:var(--mono); font-size:10.5px; fill:var(--ink-3)}
.node .id{font-family:var(--mono); font-size:9.5px; letter-spacing:.1em; fill:var(--ink-3)}
.node .cnt{font-family:var(--mono); font-size:9.5px; fill:var(--ink-3)}
.node{cursor:pointer}
.node:hover rect{stroke:var(--accent)}
.node:focus{outline:none}
.node:focus rect{stroke:var(--accent); stroke-width:3px}
.node.selected rect{stroke:var(--accent); stroke-width:3px; fill:var(--raised)}
.node.dim{opacity:.26}
.edge{fill:none; stroke-width:1.6px; transition:opacity .12s ease}
.edge.dim{opacity:.07}
.edge.hot{stroke-width:3px}
.edge-hit{fill:none; stroke:transparent; stroke-width:14px; cursor:pointer}

/* ---- inspector --------------------------------------------------------- */
.inspector{
  border-left:1px solid var(--line); background:var(--surface);
  padding:20px clamp(16px,2vw,22px) 40px; overflow:auto;
  max-height:calc(100vh - 92px);
}
@media (max-width:1020px){ .inspector{border-left:none; border-top:1px solid var(--line); max-height:none} }
.inspector h2{
  font-family:var(--mono); font-size:14px; font-weight:700;
  letter-spacing:.08em; text-transform:uppercase; margin-bottom:2px;
}
.inspector .path{
  font-family:var(--mono); font-size:12px; color:var(--accent);
  word-break:break-all; margin-bottom:14px;
}
.meta{display:flex; flex-wrap:wrap; gap:6px; margin-bottom:16px}
.chip{
  font-family:var(--mono); font-size:10px; letter-spacing:.08em; text-transform:uppercase;
  border:1px solid var(--line); border-radius:2px; padding:3px 7px; color:var(--ink-2);
  background:var(--surface-2);
}
.chip.entry{border-color:var(--accent); color:var(--accent)}
.shot{
  width:100%; border:1px solid var(--line); border-radius:3px;
  display:block; margin-bottom:6px; background:var(--surface-2);
}
.shot-note{font-size:11.5px; color:var(--ink-3); margin-bottom:18px}
.sect{margin-top:22px}
.sect > .label{display:block; margin-bottom:8px}
ul.list{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:5px}
ul.list li{
  font-family:var(--mono); font-size:11.5px; line-height:1.45; color:var(--ink-2);
  border-left:2px solid var(--line); padding:2px 0 2px 9px; word-break:break-word;
}
ul.list li b{color:var(--ink); font-weight:600}
ul.list li.warn{border-left-color:var(--warn)}
.trans{display:flex; flex-direction:column; gap:7px}
.trans button{
  text-align:left; width:100%; cursor:pointer; font:inherit;
  background:var(--surface-2); color:var(--ink); border:1px solid var(--line-soft);
  border-left:3px solid var(--inert); border-radius:3px; padding:8px 10px;
}
.trans button:hover{border-color:var(--accent)}
.trans button:focus-visible{outline:2px solid var(--accent); outline-offset:2px}
.trans .row1{display:flex; justify-content:space-between; gap:10px; align-items:baseline}
.trans .lab{font-size:12.5px; font-weight:600}
.trans .out{font-family:var(--mono); font-size:9.5px; letter-spacing:.09em;
  text-transform:uppercase; color:var(--ink-3); white-space:nowrap}
.trans .sel{font-family:var(--mono); font-size:10.5px; color:var(--ink-3);
  margin-top:3px; word-break:break-all}
.trans .ann{font-family:var(--mono); font-size:9.5px; letter-spacing:.08em;
  text-transform:uppercase; margin-top:4px}
.empty{color:var(--ink-3); font-size:13px; font-style:italic}
footer{
  border-top:1px solid var(--line); background:var(--surface);
  padding:14px clamp(16px,3vw,28px); color:var(--ink-3); font-size:12px;
}
a{color:var(--accent)}
@media (prefers-reduced-motion: reduce){ *{transition:none !important} }
</style>
</head>
<body>
<header>
  <div class="brand">
    <h1>Crawl schematic</h1>
    <div class="sub" id="target"></div>
  </div>
  <div class="stats" id="stats"></div>
</header>

<main>
  <section class="canvas-pane">
    <div class="toolbar">
      <span class="label">Transitions</span>
      <div class="filters" id="filters"></div>
      <span class="hint">Click a state to inspect it · badge is actionable / extracted · columns are hops from entry</span>
    </div>
    <div class="scroller"><svg id="svg" role="img" aria-label="Navigation graph"></svg></div>
  </section>
  <aside class="inspector" id="inspector" aria-live="polite"></aside>
</main>

<footer id="footer"></footer>

<script>
const DATA = __PAYLOAD__;

const OUTCOME = {
  navigation:       {color:"var(--accent)", dash:"",      name:"navigation"},
  in_page_state:    {color:"var(--ok)",     dash:"",      name:"in-page state"},
  new_tab:          {color:"var(--warn)",   dash:"5 4",   name:"new tab"},
  blocked_mutation: {color:"var(--stop)",   dash:"3 3",   name:"blocked write"},
  file_chooser:     {color:"var(--warn)",   dash:"3 3",   name:"file chooser"},
  native_dialog:    {color:"var(--warn)",   dash:"3 3",   name:"dialog"},
  download:         {color:"var(--warn)",   dash:"3 3",   name:"download"},
  no_change:        {color:"var(--inert)",  dash:"2 4",   name:"no change"},
  error:            {color:"var(--stop)",   dash:"2 4",   name:"error"}
};
const TYPE_COLOR = {
  page:"var(--accent)", modal:"var(--ok)", drawer:"var(--ok)",
  dropdown:"var(--ok)", panel:"var(--ok)",
  boundary:"var(--warn)", external:"var(--warn)"
};

const byId = new Map(DATA.nodes.map(n => [n.id, n]));
const active = new Set(Object.keys(OUTCOME));
let selected = DATA.nodes.find(n => n.isEntry)?.id || DATA.nodes[0]?.id || null;

/* ---- summary ---------------------------------------------------------- */
const S = DATA.summary;
document.getElementById("target").textContent = S.target + "  ·  " + S.generated.replace("T", " ");
const statDefs = [
  ["states", S.states, false],
  ["transitions", S.transitions, false],
  ["actionable", S.actionable, false],
  ["elements found", S.elements, false],
  ["clicks", S.clicks, false],
  ["skipped", S.skipped, false],
  ["writes blocked", S.blocked, true],
  ["seconds", S.seconds, false]
];
document.getElementById("stats").innerHTML = statDefs
  .filter(([, v]) => v !== null && v !== undefined)
  .map(([k, v, alert]) =>
    `<div class="stat${alert && v ? " alert" : ""}"><div class="n tnum">${v}</div><div class="k">${k}</div></div>`)
  .join("");

const stopped = S.stopReason
  ? `Crawl stopped by <b>${S.stopReason}</b>.`
  : "Crawl completed — the frontier emptied on its own.";
document.getElementById("footer").innerHTML =
  stopped + (S.boundaries.length ? ` External origins reached: ${S.boundaries.join(", ")}.` : "") +
  " Dashed transitions were recorded but not traversed — the crawler never followed them.";

/* ---- filters ---------------------------------------------------------- */
const present = [...new Set(DATA.edges.map(e => e.outcome))];
document.getElementById("filters").innerHTML = present.map(o => {
  const m = OUTCOME[o] || {color:"var(--inert)", name:o};
  return `<label class="filter" data-o="${o}">
    <input type="checkbox" checked data-o="${o}">
    <span class="swatch" style="background:${m.color}"></span>${m.name}</label>`;
}).join("");
document.getElementById("filters").addEventListener("change", ev => {
  const o = ev.target.dataset.o;
  if (!o) return;
  ev.target.checked ? active.add(o) : active.delete(o);
  document.querySelector(`.filter[data-o="${o}"]`).dataset.off = ev.target.checked ? "0" : "1";
  draw();
});

/* ---- layout ------------------------------------------------------------ */
const NW = 188, NH = 62, GAP_X = 96, GAP_Y = 26, PAD = 28;

function layout(){
  const cols = new Map();
  DATA.nodes.forEach(n => {
    if (!cols.has(n.depth)) cols.set(n.depth, []);
    cols.get(n.depth).push(n);
  });
  const keys = [...cols.keys()].sort((a,b) => a-b);
  const tallest = Math.max(...keys.map(k => cols.get(k).length), 1);
  const height = PAD*2 + tallest*NH + (tallest-1)*GAP_Y;
  keys.forEach((k, ci) => {
    const list = cols.get(k);
    const blockH = list.length*NH + (list.length-1)*GAP_Y;
    const top = (height - blockH)/2;
    list.forEach((n, ri) => {
      n._x = PAD + ci*(NW+GAP_X);
      n._y = top + ri*(NH+GAP_Y);
    });
  });
  const width = PAD*2 + keys.length*NW + (keys.length-1)*GAP_X;
  return {width, height, columns:keys.length};
}

function edgePath(e){
  const a = byId.get(e.source), b = byId.get(e.target);
  if (!a || !b) return null;
  if (a === b){                       // self-transition: arc over the top
    const x = a._x + NW*0.5, y = a._y;
    return `M ${x-26} ${y} C ${x-26} ${y-40}, ${x+26} ${y-40}, ${x+26} ${y}`;
  }
  const forward = b._x > a._x;
  const x1 = forward ? a._x + NW : a._x, y1 = a._y + NH/2;
  const x2 = forward ? b._x : b._x + NW, y2 = b._y + NH/2;
  const dx = Math.max(40, Math.abs(x2-x1)*0.45) * (forward ? 1 : -1);
  return `M ${x1} ${y1} C ${x1+dx} ${y1}, ${x2-dx} ${y2}, ${x2} ${y2}`;
}

function esc(s){
  return String(s ?? "").replace(/[&<>"]/g, c =>
    ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
}
function clip(s, n){ s = String(s ?? ""); return s.length > n ? s.slice(0, n-1) + "…" : s; }

/* ---- draw -------------------------------------------------------------- */
const svg = document.getElementById("svg");

function draw(){
  const {width, height} = layout();
  const shown = DATA.edges.filter(e => active.has(e.outcome));
  const neighbours = new Set([selected]);
  shown.forEach(e => {
    if (e.source === selected) neighbours.add(e.target);
    if (e.target === selected) neighbours.add(e.source);
  });

  let defs = `<defs>`;
  Object.entries(OUTCOME).forEach(([k, m]) => {
    defs += `<marker id="ar-${k}" viewBox="0 0 8 8" refX="7" refY="4"
      markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L8,4 L0,8 z" fill="${m.color}"/></marker>`;
  });
  defs += `</defs>`;

  const edgeSvg = shown.map(e => {
    const d = edgePath(e);
    if (!d) return "";
    const m = OUTCOME[e.outcome] || {color:"var(--inert)", dash:"2 4"};
    const related = e.source === selected || e.target === selected;
    const cls = "edge" + (related ? " hot" : (selected ? " dim" : ""));
    return `<g><path class="${cls}" d="${d}" stroke="${m.color}"
        stroke-dasharray="${m.dash}" marker-end="url(#ar-${e.outcome})"></path>
      <path class="edge-hit" d="${d}"><title>${esc(e.label)} → ${esc(e.outcome)}</title></path></g>`;
  }).join("");

  const nodeSvg = DATA.nodes.map(n => {
    const stripe = TYPE_COLOR[n.type] || "var(--inert)";
    const dim = selected && !neighbours.has(n.id) ? " dim" : "";
    const cls = `node ${n.type}${n.isEntry ? " entry" : ""}${n.id === selected ? " selected" : ""}${dim}`;
    return `<g class="${cls}" data-id="${n.id}" tabindex="0" role="button"
        aria-label="${esc(n.title)} ${esc(n.path)}" transform="translate(${n._x},${n._y})">
      <rect width="${NW}" height="${NH}" rx="3"></rect>
      <rect class="stripe" width="4" height="${NH}" rx="2" fill="${stripe}"></rect>
      <text class="id" x="13" y="16">${n.id}${n.isEntry ? " · ENTRY" : ""}</text>
      <text class="t"  x="13" y="34">${esc(clip(n.title, 26))}</text>
      <text class="p"  x="13" y="49">${esc(clip(n.path.replace(/^https?:\/\/[^/]+/, "") || "/", 30))}</text>
      <text class="cnt" x="${NW-13}" y="16" text-anchor="end">${n.actionable}/${n.elements}</text>
    </g>`;
  }).join("");

  svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
  svg.setAttribute("width", width);
  svg.setAttribute("height", height);
  svg.innerHTML = defs + edgeSvg + nodeSvg;

  svg.querySelectorAll(".node").forEach(g => {
    g.addEventListener("click", () => select(g.dataset.id));
    g.addEventListener("keydown", ev => {
      if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); select(g.dataset.id); }
    });
  });
}

/* ---- inspector --------------------------------------------------------- */
function select(id){ selected = id; draw(); inspect(); }

function inspect(){
  const n = byId.get(selected);
  const box = document.getElementById("inspector");
  if (!n){ box.innerHTML = `<p class="empty">No state selected.</p>`; return; }

  const out = DATA.edges.filter(e => e.source === n.id && active.has(e.outcome));
  const inc = DATA.edges.filter(e => e.target === n.id && e.source !== n.id && active.has(e.outcome));

  const chips = [
    n.isEntry ? `<span class="chip entry">entry</span>` : "",
    `<span class="chip">${n.type}</span>`,
    `<span class="chip">${n.actionable} actionable</span>`,
    `<span class="chip">${n.elements} interactive</span>`,
    n.dom ? `<span class="chip">${n.dom} DOM nodes</span>` : "",
    `<span class="chip">${n.visits} visit${n.visits === 1 ? "" : "s"}</span>`,
    `<span class="chip">depth ${n.crawlDepth}</span>`
  ].join("");

  const shot = n.shot
    ? `<img class="shot" src="${n.shot}" alt="Screenshot of ${esc(n.title)}">
       <div class="shot-note">Captured the moment this state was first reached.</div>`
    : `<p class="empty">No screenshot captured for this state.</p>`;

  const actions = n.actions.length
    ? `<ul class="list">${n.actions.map(a => {
        const i = a.indexOf(":");
        const kind = i > 0 ? a.slice(0, i) : "";
        const rest = i > 0 ? a.slice(i+1) : a;
        return `<li><b>${esc(kind)}</b>${esc(rest)}</li>`;
      }).join("")}</ul>`
    : `<p class="empty">No actionable elements extracted.</p>`;

  const transitions = out.length
    ? `<div class="trans">${out.map(e => {
        const m = OUTCOME[e.outcome] || {color:"var(--inert)", name:e.outcome};
        const t = byId.get(e.target);
        const dest = e.target === n.id ? "stays here" : `→ ${e.target} ${clip(t ? t.title : "", 22)}`;
        return `<button data-go="${e.target}" style="border-left-color:${m.color}">
          <span class="row1"><span class="lab">${esc(e.label)}</span>
          <span class="out">${esc(m.name)}</span></span>
          ${e.selector ? `<div class="sel">${esc(e.selector)}</div>` : ""}
          <div class="sel">${esc(dest)}</div>
          ${e.annotations.length ? `<div class="ann" style="color:${m.color}">${esc(e.annotations.join(" · "))}</div>` : ""}
        </button>`;
      }).join("")}</div>`
    : `<p class="empty">No outgoing transitions match the current filters.</p>`;

  const notDone = n.notExercised.length
    ? `<ul class="list">${n.notExercised.map(x => `<li class="warn">${esc(x)}</li>`).join("")}</ul>`
    : "";

  box.innerHTML = `
    <h2>${esc(n.title)}</h2>
    <div class="path">${esc(n.url)}</div>
    <div class="meta">${chips}</div>
    ${shot}
    <div class="sect"><span class="label">Action elements · ${n.actions.length}</span>${actions}</div>
    <div class="sect"><span class="label">Outgoing transitions · ${out.length}</span>${transitions}</div>
    ${inc.length ? `<div class="sect"><span class="label">Reached by</span>
      <ul class="list">${inc.map(e => `<li><b>${esc(e.source)}</b> ${esc(e.label)}</li>`).join("")}</ul></div>` : ""}
    ${notDone ? `<div class="sect"><span class="label">Not exercised</span>${notDone}</div>` : ""}
  `;
  box.querySelectorAll("[data-go]").forEach(b =>
    b.addEventListener("click", () => select(b.dataset.go)));
  box.scrollTop = 0;
}

draw();
inspect();
</script>
</body>
</html>
"""
