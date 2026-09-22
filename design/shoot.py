"""Screenshot each mockup at 1440x900, 2x device scale, into <repo>/design/."""

from pathlib import Path
from playwright.sync_api import sync_playwright

HTML = Path(__file__).parent / "html"
OUT = Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1440, "height": 900},
        device_scale_factor=2,
    )
    for f in sorted(HTML.glob("*.html")):
        page.goto(f.as_uri())
        # give the Google Fonts request a moment; falls back cleanly if offline
        try:
            page.wait_for_load_state("networkidle", timeout=8000)
        except Exception:
            pass
        page.wait_for_timeout(600)
        target = OUT / (f.stem + ".png")
        page.screenshot(path=str(target))
        print(f"{target.name}  {target.stat().st_size // 1024} KB")
    browser.close()

print("\nall written to", OUT)
