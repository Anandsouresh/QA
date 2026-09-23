"""End-to-end check: API starts a real crawl, the UI streams it live.

Needs three things already running:

    python -m http.server 8899 --directory ../tests/fixture
    uvicorn api.main:app --port 8000          (from the repo root)
    npm run preview -- --port 4173

    python scripts/test_integration.py

Exits non-zero on any console error, failed request, or missing live data.
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

API = "http://localhost:8000"
UI = "http://localhost:4173"
TARGET = "http://127.0.0.1:8899/index.html"
OUT = Path(__file__).resolve().parent.parent / "screenshots" / "integration"
OUT.mkdir(parents=True, exist_ok=True)


def post(path: str, body: dict) -> dict:
    req = urllib.request.Request(
        f"{API}{path}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.loads(res.read())


def get(path: str) -> dict | list:
    with urllib.request.urlopen(f"{API}{path}", timeout=30) as res:
        return json.loads(res.read())


failures: list[str] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}{f' — {detail}' if detail else ''}")
    if not ok:
        failures.append(label)


print("1. starting a real crawl through the API")
started = post("/api/runs", {
    "url": TARGET,
    "depth": 1,
    "modules": {},
    "generate": False,
    "headless": True,
    "max_wall_clock_seconds": 180,
})
run_id = started["id"]
check("run created", bool(run_id), run_id)
check("subprocess spawned", bool(started.get("pid")), f"pid {started.get('pid')}")

print("2. waiting for the crawler to emit events")
log_bytes = 0
for _ in range(40):
    time.sleep(1.5)
    row = get(f"/api/runs/{run_id}")
    log_bytes = row.get("log_bytes", 0)
    if log_bytes > 500:
        break
check("crawl-log.jsonl is growing", log_bytes > 500, f"{log_bytes} bytes")

print("3. opening the UI against that run")
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    context.add_init_script(
        "try {"
        f" localStorage.setItem('qagen.source', JSON.stringify({{kind:'live',runId:'{run_id}'}}));"
        " localStorage.setItem('qagen.theme','dark');"
        "} catch (e) {}"
    )
    problems: list[str] = []
    page = context.new_page()
    page.on("console", lambda m: problems.append(f"console.{m.type}: {m.text}")
            if m.type == "error" else None)
    page.on("pageerror", lambda e: problems.append(f"pageerror: {e}"))

    page.goto(f"{UI}/live", wait_until="networkidle")
    page.wait_for_timeout(9000)
    page.screenshot(path=str(OUT / "live-streaming.png"))

    body = page.inner_text("body")
    check("shows the live run id", run_id in body, run_id)
    check("labelled live, not replay", "recorded replay" not in body)
    check("event stream is populated", "streaming" in body or "EVENTS" in body)
    check("no console errors", not problems, "; ".join(problems[:2]))

    print("4. stopping it from the UI's own endpoint")
    post(f"/api/runs/{run_id}/stop", {})
    for _ in range(30):
        time.sleep(1.5)
        row = get(f"/api/runs/{run_id}")
        if row["status"] in {"stopped", "finished", "failed"}:
            break
    check("stopped cleanly", row["status"] == "stopped", row["status"])
    check("graph still written", bool(row.get("has_graph")))
    manifest = row.get("manifest") or {}
    reason = (manifest.get("crawl", {}).get("budgets") or {}).get("stop_reason")
    check("reason recorded as operator stop", reason == "stopped by operator", str(reason))
    states = manifest.get("crawl", {}).get("states_discovered", 0)
    check("partial output kept", states > 0, f"{states} states")

    page.goto(f"{UI}/graph", wait_until="networkidle")
    page.wait_for_timeout(2500)
    page.screenshot(path=str(OUT / "graph-of-live-run.png"))
    check("graph screen renders the live run", "Navigation graph" in page.inner_text("body"))

    context.close()
    browser.close()

print()
if failures:
    print(f"{len(failures)} check(s) failed: {', '.join(failures)}")
    sys.exit(1)
print(f"all checks passed — screenshots in {OUT}")
