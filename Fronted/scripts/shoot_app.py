"""Screenshot every route in both themes and report any console error.

    npm run build && npm run preview -- --port 4173
    python scripts/shoot_app.py            # both themes
    python scripts/shoot_app.py dark       # one theme
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent.parent / "screenshots"
BASE = "http://localhost:4173"

ROUTES = [
    ("/", "01-new-run", 1400),
    ("/live", "02-live-run", 4500),
    ("/graph", "03-graph-explorer", 2800),
    ("/cases", "04-test-cases", 2200),
    ("/history", "05-runs", 1400),
]

THEMES = sys.argv[1:] or ["dark", "light"]

problems: list[str] = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    for theme in THEMES:
        folder = OUT / theme
        folder.mkdir(parents=True, exist_ok=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
            color_scheme="light" if theme == "light" else "dark",
        )
        # The app reads its stored preference before React mounts.
        context.add_init_script(
            f"try {{ localStorage.setItem('qagen.theme', '{theme}'); }} catch (e) {{}}"
        )
        page = context.new_page()
        page.on("console", lambda m: problems.append(f"console.{m.type}: {m.text}")
                if m.type in ("error", "warning") else None)
        page.on("pageerror", lambda e: problems.append(f"pageerror: {e}"))
        page.on("requestfailed", lambda r: problems.append(
            f"requestfailed: {r.url.split('/')[-1]} {r.failure}")
            if "localhost:8000" not in r.url else None)   # the API is optional

        print(f"\n[{theme}]")
        for route, name, settle in ROUTES:
            page.goto(f"{BASE}{route}", wait_until="networkidle")
            page.wait_for_timeout(settle)
            target = folder / f"{name}.png"
            page.screenshot(path=str(target))
            print(f"  {name:<22} {target.stat().st_size // 1024:>4} KB")
        context.close()
    browser.close()

if problems:
    unique = list(dict.fromkeys(problems))
    print(f"\n{len(unique)} console/network problem(s):")
    for line in unique:
        print("  -", line[:170])
    sys.exit(1)
print("\nno console errors, no failed requests")
