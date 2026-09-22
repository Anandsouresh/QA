"""Emit four standalone HTML mockups of the QAGen Control Room, then they get
screenshotted by shoot.py. No framework, no runtime -- plain HTML so Chromium
renders them exactly as written."""

from pathlib import Path

OUT = Path(__file__).parent / "html"
OUT.mkdir(parents=True, exist_ok=True)

A = "#5FB98F"   # accent / live
AM = "#D9924A"  # amber
BL = "#6E9FD4"  # blue
RD = "#D96F6F"  # red
VI = "#A98BD4"  # violet

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>%s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
*{box-sizing:border-box}
body{margin:0;width:1440px;height:900px;overflow:hidden;
     font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;background:#0E1116;color:#E7EAF0}
.dsp{font-family:"Space Grotesk","IBM Plex Sans",sans-serif}
.mono{font-family:"IBM Plex Mono","Consolas",monospace}
button{font-family:inherit;cursor:pointer}
input{font-family:inherit}
h1,h2,p{margin:0}
.card{background:#151A21;border:1px solid #232A34;border-radius:13px}
.ell{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
</style></head><body>"""

FOOT = "</body></html>"


def icon(name, color="currentColor", size=19):
    p = {
        "plus": '<path d="M12 5v14"/><path d="M5 12h14"/>',
        "pulse": '<path d="M3 12h4l3 8 4-16 3 8h4"/>',
        "graph": '<circle cx="5.5" cy="6" r="2.4"/><circle cx="18.5" cy="12" r="2.4"/>'
                 '<circle cx="5.5" cy="18" r="2.4"/><path d="M7.6 7.2 16.4 10.8"/>'
                 '<path d="M16.4 13.2 7.6 16.8"/>',
        "checks": '<path d="M4 6.5 6 8.5 9.5 5"/><path d="M4 17.5 6 19.5 9.5 16"/>'
                  '<path d="M13 7h7"/><path d="M13 18h7"/>',
        "clock": '<circle cx="12" cy="12" r="8.2"/><path d="M12 7.6V12l3 1.8"/>',
        "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 3v2.2M12 18.8V21M21 12h-2.2M5.2 12H3'
                'M18.4 5.6 16.8 7.2M7.2 16.8 5.6 18.4M18.4 18.4 16.8 16.8M7.2 7.2 5.6 5.6"/>',
        "check": '<path d="M20 6 9 17l-5-5"/>',
        "shield": '<path d="M12 3 4.6 6.1v5.5c0 4.4 3 8.2 7.4 9.4 4.4-1.2 7.4-5 7.4-9.4V6.1z"/>'
                  '<path d="M9.2 12.2 11.3 14.3 15 10.6"/>',
        "down": '<path d="M12 3.5v11"/><path d="M7.5 10 12 14.5 16.5 10"/><path d="M4.5 19.5h15"/>',
        "search": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16 20.5 20.5"/>',
        "filter": '<path d="M4 6h16"/><path d="M7 12h10"/><path d="M10 18h4"/>',
        "warn": '<path d="M12 8v5"/><path d="M10.3 4.2 2.9 17.4A1.9 1.9 0 0 0 4.6 20.3h14.8'
                'a1.9 1.9 0 0 0 1.7-2.9L13.7 4.2a1.9 1.9 0 0 0-3.4 0z"/>',
        "left": '<path d="M14.5 5.5 8 12l6.5 6.5"/>',
        "right": '<path d="M9.5 5.5 16 12l-6.5 6.5"/>',
        "x": '<path d="M6.5 6.5 17.5 17.5"/><path d="M17.5 6.5 6.5 17.5"/>',
        "ext": '<path d="M14 4h6v6"/><path d="M20 4 11 13"/><path d="M18 14v5a1.5 1.5 0 0 1-1.5 '
               '1.5h-11A1.5 1.5 0 0 1 4 19V8a1.5 1.5 0 0 1 1.5-1.5H10"/>',
        "fit": '<path d="M4 9V4h5"/><path d="M20 9V4h-5"/><path d="M4 15v5h5"/><path d="M20 15v5h-5"/>',
        "minus": '<path d="M6 12h12"/>',
        "logo": '<circle cx="6" cy="6" r="2.6"/><circle cx="18" cy="6" r="2.6"/>'
                '<circle cx="12" cy="18" r="2.6"/><path d="M8.2 7.4 10.6 15.6"/>'
                '<path d="M15.8 7.4 13.4 15.6"/>',
    }[name]
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round">{p}</svg>')


def rail(active):
    items = [("plus", "New run"), ("pulse", "Live run"), ("graph", "Graph explorer"),
             ("checks", "Test cases"), ("clock", "Run history")]
    out = [f'<div style="width:72px;flex-shrink:0;background:#11151B;border-right:1px solid #222831;'
           f'display:flex;flex-direction:column;align-items:center;padding:18px 0 16px;gap:8px">'
           f'<div style="width:38px;height:38px;border-radius:10px;background:{A};display:flex;'
           f'align-items:center;justify-content:center;margin-bottom:14px">'
           f'{icon("logo", "#0E1116", 21)}</div>']
    for i, (ic, label) in enumerate(items):
        on = i == active
        bd = "#2E4A3E" if on else "transparent"
        bg = "#172620" if on else "transparent"
        co = A if on else "#7A8393"
        out.append(f'<button aria-label="{label}" style="width:46px;height:46px;border-radius:11px;'
                   f'border:1px solid {bd};background:{bg};color:{co};display:flex;'
                   f'align-items:center;justify-content:center">{icon(ic)}</button>')
    out.append('<div style="flex-grow:1"></div>')
    out.append('<button aria-label="Settings" style="width:46px;height:46px;border-radius:11px;'
               'border:1px solid transparent;background:transparent;color:#7A8393;display:flex;'
               'align-items:center;justify-content:center">' + icon("gear") + '</button></div>')
    return "".join(out)


# ───────────────────────── 1. NEW RUN ─────────────────────────
def screen_new_run():
    mods = [
        ("Screen", "/screen · /screen/{id}", "40", "20%", A),
        ("Content", "/content · /content/{id}", "40", "20%", A),
        ("Playlist", "/playlist · /playlist/create · /playlist/{id}", "30", "15%", BL),
        ("Schedule", "/schedule · /schedule/create · /schedule/{id}", "30", "15%", BL),
        ("Channel", "/channel", "20", "10%", VI),
        ("Settings", "/settings + 20 sub-pages", "40", "20%", AM),
    ]
    rows = "".join(
        f'<div style="display:grid;grid-template-columns:150px 1fr 92px 150px;gap:0 14px;'
        f'align-items:center;padding:5px 2px;border-bottom:1px solid #1B212A">'
        f'<span style="font-size:13px;font-weight:500">{n}</span>'
        f'<span class="mono ell" style="font-size:11.5px;color:#7A8393">{p}</span>'
        f'<input type="number" value="{b}" aria-label="State budget" class="mono" '
        f'style="width:100%;height:32px;padding:0 9px;border-radius:7px;border:1px solid #2A313C;'
        f'background:#0F1319;color:#E7EAF0;font-size:12.5px;text-align:right">'
        f'<div style="height:7px;border-radius:4px;background:#1E242D;overflow:hidden">'
        f'<div style="height:100%;width:{s};border-radius:4px;background:{t}"></div></div></div>'
        for n, p, b, s, t in mods)

    deny = ["delete", "remove", "pay", "purchase", "submit",
            "confirm", "logout", "deactivate"]
    chips = "".join(
        f'<span class="mono" style="padding:4px 9px;border-radius:6px;background:#241A1A;'
        f'border:1px solid #3D2A2A;font-size:11.5px;color:#D99A9A">{d}</span>' for d in deny)

    plan = [("Host", "stg.samsungvx.com"), ("Modules", "6 in scope"), ("States", "200 max"),
            ("Wall clock", "24h ceiling"), ("Model", "claude-opus-5"),
            ("Output", "runs/2026-09-23-vx")]
    planrows = "".join(
        f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:12px;'
        f'padding:9px 0;border-bottom:1px solid #1E242D">'
        f'<span style="font-size:12.5px;color:#7A8393;flex-shrink:0">{k}</span>'
        f'<span class="mono ell" style="font-size:12.5px;color:#D6DCE6">{v}</span></div>'
        for k, v in plan)

    return HEAD % "New run" + f"""
<div style="display:flex;width:1440px;height:900px">{rail(0)}
<div style="flex-grow:1;padding:24px 30px 26px;display:flex;flex-direction:column;gap:20px;min-width:0">

  <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:24px">
    <div>
      <h1 class="dsp" style="font-size:27px;font-weight:600;letter-spacing:-.4px;margin-bottom:5px">New run</h1>
      <p style="font-size:13.5px;color:#9AA3B2">Crawl a live application read-only, then write grounded QA test cases from what was actually on screen.</p>
    </div>
    <div style="display:flex;gap:10px;flex-shrink:0">
      <button style="height:44px;padding:0 16px;border-radius:9px;border:1px solid #2A313C;background:#171C24;color:#C3CAD6;font-size:13.5px;font-weight:500">Load config&hellip;</button>
      <button style="height:44px;padding:0 16px;border-radius:9px;border:1px solid #2A313C;background:#171C24;color:#C3CAD6;font-size:13.5px;font-weight:500">Clone last run</button>
    </div>
  </div>

  <div style="display:flex;gap:22px;flex-grow:1;min-height:0">
    <div style="flex-grow:1;display:flex;flex-direction:column;gap:13px;min-width:0">

      <div class="card" style="padding:18px 20px 19px">
        <div style="display:flex;align-items:center;gap:9px;margin-bottom:15px">
          <span class="mono" style="font-size:11px;color:{A}">01</span>
          <h2 class="dsp" style="font-size:14.5px;font-weight:600">Target &amp; session</h2>
        </div>
        <div style="display:flex;gap:14px;align-items:flex-end">
          <div style="flex-grow:1;min-width:0">
            <label for="u" style="display:block;font-size:11.5px;font-weight:500;color:#7A8393;margin-bottom:6px;letter-spacing:.2px">TARGET URL</label>
            <input id="u" type="url" value="https://stg.samsungvx.com/" class="mono" style="width:100%;height:44px;padding:0 13px;border-radius:9px;border:1px solid #2E3641;background:#0F1319;color:#E7EAF0;font-size:13px">
          </div>
          <div style="width:118px;flex-shrink:0">
            <label for="d" style="display:block;font-size:11.5px;font-weight:500;color:#7A8393;margin-bottom:6px;letter-spacing:.2px">DEPTH</label>
            <input id="d" type="number" value="20" class="mono" style="width:100%;height:44px;padding:0 13px;border-radius:9px;border:1px solid #2E3641;background:#0F1319;color:#E7EAF0;font-size:13px">
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:13px;padding:10px 12px;border-radius:9px;background:#12271E;border:1px solid #2B4A3A">
          {icon("check", A, 17)}
          <span style="font-size:12.5px;color:#C3CAD6">Session verified &mdash; <span class="mono" style="color:#9AA3B2">secrets/samsungvx.json</span> resolved to a logged-in user 8 seconds ago.</span>
          <div style="flex-grow:1"></div>
          <button style="height:30px;padding:0 12px;border-radius:7px;border:1px solid #2E3641;background:#171C24;color:#C3CAD6;font-size:12px;font-weight:500">Re-check</button>
        </div>
      </div>

      <div class="card" style="padding:18px 20px 16px;display:flex;flex-direction:column">
        <div style="display:flex;align-items:center;gap:9px;margin-bottom:4px">
          <span class="mono" style="font-size:11px;color:{A}">02</span>
          <h2 class="dsp" style="font-size:14.5px;font-weight:600">Modules &amp; state budget</h2>
          <div style="flex-grow:1"></div>
          <button style="height:30px;padding:0 12px;border-radius:7px;border:1px solid #2E3641;background:#171C24;color:#C3CAD6;font-size:12px;font-weight:500">Re-probe target</button>
        </div>
        <p style="font-size:12px;color:#7A8393;margin-bottom:13px">Six modules in scope from a 40-second shallow probe. A budget is a ceiling on distinct states, so one deep area cannot starve the rest.</p>
        <div style="display:grid;grid-template-columns:150px 1fr 92px 150px;gap:0 14px;padding:0 2px 8px;border-bottom:1px solid #232A34;font-size:10.5px;font-weight:600;letter-spacing:.5px;color:#6E7784">
          <span>MODULE</span><span>PATHS DISCOVERED</span><span style="text-align:right">STATES</span><span>SHARE</span>
        </div>
        {rows}
        <div style="display:grid;grid-template-columns:150px 1fr 92px 150px;gap:0 14px;align-items:center;padding:11px 2px 0">
          <span style="font-size:12.5px;font-weight:600;color:#9AA3B2">Total</span>
          <span style="font-size:12px;color:#6E7784">stops at whichever comes first</span>
          <span class="mono" style="font-size:14px;color:{A};text-align:right">200</span>
          <span style="font-size:12px;color:#6E7784">distinct states</span>
        </div>
      </div>

      <div class="card" style="padding:16px 20px 17px">
        <div style="display:flex;align-items:center;gap:9px;margin-bottom:13px">
          <span class="mono" style="font-size:11px;color:{A}">03</span>
          <h2 class="dsp" style="font-size:14.5px;font-weight:600">Safety</h2>
        </div>
        <div style="display:flex;gap:14px">
          <div style="flex-shrink:0;width:260px;padding:12px 14px;border-radius:10px;background:#12271E;border:1px solid #2B4A3A;display:flex;align-items:center;gap:12px">
            {icon("shield", A, 26)}
            <div>
              <div style="font-size:13px;font-weight:600">Write-guard armed</div>
              <div style="font-size:11.5px;color:#8FB8A2;line-height:1.45;margin-top:2px">POST, PUT, PATCH and DELETE are aborted at the route layer, then recorded.</div>
            </div>
          </div>
          <div style="flex-grow:1;min-width:0">
            <div style="font-size:11.5px;font-weight:500;color:#7A8393;margin-bottom:8px;letter-spacing:.2px">NEVER CLICKED</div>
            <div style="display:flex;flex-wrap:wrap;gap:6px">{chips}
              <button style="padding:4px 10px;border-radius:6px;background:transparent;border:1px dashed #3A424E;font-size:11.5px;color:#7A8393">edit list</button>
            </div>
          </div>
        </div>
      </div>
      <div style="flex-grow:1"></div>
    </div>

    <div style="width:330px;flex-shrink:0;background:#151A21;border:1px solid #2B3340;border-radius:13px;padding:20px;display:flex;flex-direction:column">
      <h2 class="dsp" style="font-size:15px;font-weight:600;margin-bottom:3px">Run plan</h2>
      <p style="font-size:12px;color:#7A8393;margin-bottom:16px">Estimates from your last three runs on this host.</p>
      {planrows}
      <div style="margin-top:18px;padding:13px 14px;border-radius:10px;background:#14191F;border:1px solid #242B35">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:7px">
          <span style="font-size:12px;color:#9AA3B2">Estimated duration</span>
          <span class="dsp" style="font-size:20px;font-weight:600;color:{A}">4h 50m</span>
        </div>
        <div style="height:5px;border-radius:3px;background:#1E242D;overflow:hidden;margin-bottom:8px">
          <div style="height:100%;width:72%;background:linear-gradient(90deg,#3E6F58,{A})"></div>
        </div>
        <p style="font-size:11.5px;line-height:1.5;color:#6E7784">Crawling is the slow half. Test-case generation runs separately in about nine minutes and can be repeated against this crawl without paying for capture again.</p>
      </div>
      <div style="flex-grow:1"></div>
      <button style="width:100%;height:48px;margin-top:18px;border-radius:10px;border:none;background:{A};color:#0B1F17;font-size:14.5px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:9px" class="dsp">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="#0B1F17"><path d="M8 5.5 18.5 12 8 18.5z"/></svg>Start crawl
      </button>
      <button style="width:100%;height:44px;margin-top:9px;border-radius:10px;border:1px solid #2A313C;background:#171C24;color:#C3CAD6;font-size:13.5px;font-weight:500">Crawl only &mdash; skip generation</button>
      <p style="font-size:11.5px;line-height:1.5;color:#6E7784;text-align:center;margin-top:11px">Nothing on the target is created, edited or deleted.</p>
    </div>
  </div>
</div></div>""" + FOOT


# ───────────────────────── 2. LIVE RUN ─────────────────────────
def screen_live():
    clocks = "".join(
        f'<div style="text-align:right;padding-right:18px;border-right:1px solid #242B35">'
        f'<div style="font-size:10.5px;letter-spacing:.5px;color:#6E7784">{k}</div>'
        f'<div class="mono" style="font-size:15px;color:#D6DCE6;margin-top:2px">{v}</div></div>'
        for k, v in [("ELAPSED", "4:53:25"), ("EST. LEFT", "2:41:10")])

    navrows = "".join(
        f'<span style="height:6px;border-radius:3px;background:{t};width:{w};display:block"></span>'
        for w, t in [("100%", "#2E3641"), ("74%", "#262D38"), ("86%", "#262D38"),
                     ("64%", "#262D38"), ("92%", "#262D38"), ("58%", "#262D38")])

    cards = "".join(
        f'<div style="border-radius:6px;background:#1B212A;border:1px solid #242B35;padding:9px;'
        f'display:flex;flex-direction:column;gap:6px">'
        f'<span style="height:32px;border-radius:4px;background:{t};display:block"></span>'
        f'<span style="height:5px;width:78%;border-radius:3px;background:#2E3641;display:block"></span>'
        f'<span style="height:5px;width:48%;border-radius:3px;background:#262D38;display:block"></span></div>'
        for t in ["#242B35", "#262D38", "#242B35", "#262D38", "#242B35", "#242B35"])

    meters = "".join(
        f'<div><div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">'
        f'<span style="font-size:11px;color:#7A8393">{k}</span>'
        f'<span class="mono" style="font-size:11px;color:#6E7784">{cap}</span></div>'
        f'<div class="dsp" style="font-size:20px;font-weight:600;color:{t};margin-bottom:7px">{v}</div>'
        f'<div style="height:5px;border-radius:3px;background:#1E242D;overflow:hidden">'
        f'<div style="height:100%;width:{p};border-radius:3px;background:{t}"></div></div></div>'
        for k, v, cap, p, t in [("States", "116", "/ 200", "58%", A),
                                ("Clicks", "733", "no cap", "41%", BL),
                                ("Navigations", "345", "no cap", "33%", BL),
                                ("Wall clock", "20%", "/ 24h", "20%", AM)])

    permod = "".join(
        f'<div style="display:flex;align-items:center;gap:9px">'
        f'<span style="width:62px;flex-shrink:0;font-size:11.5px;color:#9AA3B2">{n}</span>'
        f'<div style="flex-grow:1;height:6px;border-radius:3px;background:#1E242D;overflow:hidden">'
        f'<div style="height:100%;width:{p};border-radius:3px;background:{t}"></div></div>'
        f'<span class="mono" style="width:42px;flex-shrink:0;text-align:right;font-size:11px;color:#7A8393">{v}</span></div>'
        for n, p, v, t in [("Screen", "78%", "31/40", A), ("Content", "60%", "24/40", A),
                           ("Playlist", "47%", "14/30", BL), ("Schedule", "30%", "9/30", BL),
                           ("Channel", "100%", "20/20", AM), ("Settings", "72%", "18/25", AM)])

    legend = "".join(
        f'<div style="display:flex;align-items:center;gap:6px">'
        f'<span style="width:8px;height:8px;border-radius:50%;background:{t};display:block"></span>'
        f'<span style="font-size:11px;color:#7A8393">{k}</span></div>'
        for k, t in [("page", "#4E5A6B"), ("modal", BL), ("boundary", VI), ("new", A)])

    evs = [
        ("17604.8", "ACTION", "#1B212A", "#9AA3B2", "N047 click generic_button 'New'"),
        ("17592.1", "RESTORE", "#1B212A", "#7A8393", "N047 ok via escape/back/goto"),
        ("17581.4", "OUTCOME", "#1F3830", A, "'Screens' -&gt; navigation [2.1s]"),
        ("17549.0", "STATE", "#1F3830", A, "N116 /screen/{id} (54 elements, 1 form)"),
        ("17548.2", "OUTCOME", "#1A2733", BL, "'Edit' -&gt; in_page_state (modal)"),
        ("17531.7", "BLOCKED", "#241C33", VI, "PUT /api/dms/screens/{guid} aborted"),
        ("17522.9", "SKIP", "#241A1A", "#D99A9A", "'Delete' -- deny-list match"),
        ("17510.3", "ACTION", "#1B212A", "#9AA3B2", "N115 click tab 'Playback'"),
        ("17498.6", "OUTCOME", "#1B212A", "#7A8393", "'Refresh' -&gt; no_change (inert)"),
        ("17471.2", "DIALOG", "#2A2416", AM, "confirm() recorded, then dismissed"),
        ("17455.8", "STATE", "#1F3830", A, "N115 /screen (49 elements, 0 forms)"),
        ("17440.1", "DUPLICATE", "#1B212A", "#7A8393", "/screen fp=a3f91c collapsed"),
        ("17429.4", "NAVIGATE", "#1B212A", "#9AA3B2", "-&gt; /screen (depth 2)"),
        ("17418.0", "BUDGET", "#1B212A", "#7A8393", "states=115/200 clicks=731"),
    ]
    events = "".join(
        f'<div style="padding:7px 15px;border-bottom:1px solid #1B212A;display:flex;flex-direction:column;gap:3px">'
        f'<div style="display:flex;align-items:center;gap:7px">'
        f'<span class="mono" style="font-size:10px;color:#5C6675;width:46px;flex-shrink:0">{t}</span>'
        f'<span style="font-size:10px;font-weight:600;letter-spacing:.3px;padding:2px 6px;'
        f'border-radius:4px;background:{bg};color:{fg}">{k}</span></div>'
        f'<div class="mono ell" style="font-size:10.5px;line-height:1.5;color:#8B94A3;padding-left:53px">{d}</div></div>'
        for t, k, bg, fg, d in evs)

    return HEAD % "Live run" + f"""
<div style="display:flex;width:1440px;height:900px">{rail(1)}
<div style="flex-grow:1;padding:18px 22px 20px;display:flex;flex-direction:column;gap:14px;min-width:0">

  <div style="display:flex;align-items:center;gap:16px;height:46px;flex-shrink:0">
    <div style="display:flex;align-items:center;gap:8px;padding:7px 13px 7px 11px;border-radius:8px;background:#12271E;border:1px solid #2B4A3A">
      <span style="width:8px;height:8px;border-radius:50%;background:{A};display:block"></span>
      <span class="dsp" style="font-size:12.5px;font-weight:600;letter-spacing:.7px;color:{A}">CRAWLING</span>
    </div>
    <div style="min-width:0">
      <div class="mono ell" style="font-size:13px;color:#D6DCE6">stg.samsungvx.com</div>
      <div style="font-size:11.5px;color:#6E7784">run 2026-09-23-vx &middot; depth 20 &middot; write-guard on</div>
    </div>
    <div style="flex-grow:1"></div>{clocks}
    <button style="height:44px;padding:0 15px;margin-left:4px;border-radius:9px;border:1px solid #2A313C;background:#171C24;color:#C3CAD6;font-size:13px;font-weight:500;display:flex;align-items:center;gap:7px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><rect x="7" y="5" width="3.6" height="14" rx="1"/><rect x="13.4" y="5" width="3.6" height="14" rx="1"/></svg>Pause</button>
    <button style="height:44px;padding:0 15px;border-radius:9px;border:1px solid #4A2C2C;background:#241A1A;color:#E09A9A;font-size:13px;font-weight:500;display:flex;align-items:center;gap:7px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>Stop &amp; keep</button>
  </div>

  <div style="display:flex;gap:14px;flex-grow:1;min-height:0">

    <div style="width:616px;flex-shrink:0;display:flex;flex-direction:column;gap:14px;min-height:0">
      <div class="card" style="padding:14px;display:flex;flex-direction:column;height:458px">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:11px">
          <span style="width:6px;height:6px;border-radius:50%;background:{RD};display:block"></span>
          <h2 class="dsp" style="font-size:13px;font-weight:600;letter-spacing:.3px">LIVE VIEWPORT</h2>
          <div style="flex-grow:1"></div>
          <span class="mono" style="font-size:11px;color:#6E7784">1200 &times; 900 &middot; frame 4281</span>
        </div>
        <div style="flex-grow:1;border-radius:9px;overflow:hidden;border:1px solid #2A313C;display:flex;flex-direction:column;background:#0A0D12">
          <div style="height:30px;flex-shrink:0;background:#1A1F27;border-bottom:1px solid #262D38;display:flex;align-items:center;gap:7px;padding:0 11px">
            <span style="width:8px;height:8px;border-radius:50%;background:#3A424E;display:block"></span>
            <span style="width:8px;height:8px;border-radius:50%;background:#3A424E;display:block"></span>
            <span style="width:8px;height:8px;border-radius:50%;background:#3A424E;display:block"></span>
            <span class="mono ell" style="margin-left:8px;font-size:10.5px;color:#6E7784">stg.samsungvx.com/screen</span>
          </div>
          <div style="flex-grow:1;position:relative;background:#12161C;padding:12px">
            <div style="height:26px;border-radius:5px;background:#1B212A;margin-bottom:10px;display:flex;align-items:center;padding:0 10px;gap:14px">
              <span style="width:44px;height:7px;border-radius:3px;background:#2E3641;display:block"></span>
              <span style="width:30px;height:6px;border-radius:3px;background:#262D38;display:block"></span>
              <span style="width:34px;height:6px;border-radius:3px;background:#262D38;display:block"></span>
              <div style="flex-grow:1"></div>
              <span style="width:18px;height:18px;border-radius:50%;background:#2E3641;display:block"></span>
            </div>
            <div style="display:flex;gap:10px;height:232px">
              <div style="width:84px;flex-shrink:0;border-radius:5px;background:#1B212A;padding:9px 8px;display:flex;flex-direction:column;gap:9px">{navrows}</div>
              <div style="flex-grow:1;display:flex;flex-direction:column;gap:10px;min-width:0">
                <div style="display:flex;align-items:center;gap:9px">
                  <span style="width:88px;height:11px;border-radius:3px;background:#2E3641;display:block"></span>
                  <div style="flex-grow:1"></div>
                  <div style="position:relative;flex-shrink:0">
                    <span style="display:block;width:58px;height:24px;border-radius:5px;background:#1F3830;border:2px solid {A};box-shadow:0 0 0 4px rgba(95,185,143,.18)"></span>
                    <span class="mono" style="position:absolute;top:-21px;right:0;white-space:nowrap;font-size:9.5px;padding:2px 6px;border-radius:4px;background:{A};color:#0B1F17;font-weight:500">clicking &middot; New</span>
                  </div>
                </div>
                <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px;flex-grow:1">{cards}</div>
              </div>
            </div>
          </div>
        </div>
        <p style="font-size:11.5px;color:#6E7784;line-height:1.45;margin-top:10px">Streamed from the crawler's own Chromium at 1 frame per second. The outlined control is the one being exercised this instant.</p>
      </div>

      <div class="card" style="padding:15px 17px 16px;flex-grow:1;display:flex;flex-direction:column;min-height:0">
        <h2 class="dsp" style="font-size:13px;font-weight:600;letter-spacing:.3px;margin-bottom:13px">BUDGETS</h2>
        <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:13px;margin-bottom:15px">{meters}</div>
        <div style="font-size:10.5px;font-weight:600;letter-spacing:.5px;color:#6E7784;margin-bottom:9px">STATES PER MODULE</div>
        <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 18px">{permod}</div>
        <div style="flex-grow:1"></div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:12px;padding:10px 12px;border-radius:9px;background:#14191F;border:1px solid #242B35">
          <span style="width:7px;height:7px;border-radius:50%;background:{AM};display:block;flex-shrink:0"></span>
          <span style="font-size:11.5px;color:#9AA3B2;line-height:1.45">Channel reached its cap at 20 states and stopped early. Every other module is still taking work from the frontier.</span>
        </div>
      </div>
    </div>

    <div style="width:392px;flex-shrink:0;display:flex;flex-direction:column;gap:14px;min-height:0">
      <div style="background:#151A21;border:1px solid #2E4A3E;border-radius:13px;padding:15px 17px 16px;flex-shrink:0;position:relative;overflow:hidden">
        <div style="position:absolute;top:0;left:14%;width:30%;height:2px;background:linear-gradient(90deg,transparent,{A},transparent)"></div>
        <div style="display:flex;align-items:center;gap:9px;margin-bottom:12px">
          <h2 class="dsp" style="font-size:13px;font-weight:600;letter-spacing:.3px">NOW EXERCISING</h2>
          <div style="flex-grow:1"></div>
          <span class="mono" style="font-size:11.5px;color:{A}">12.4s</span>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:11px">
          <span class="mono" style="font-size:12px;padding:4px 8px;border-radius:6px;background:#1F3830;color:{A}">N047</span>
          <span style="font-size:12px;padding:4px 8px;border-radius:6px;background:#1B212A;color:#9AA3B2">click</span>
          <span style="font-size:12px;padding:4px 8px;border-radius:6px;background:#1B212A;color:#9AA3B2">generic_button</span>
        </div>
        <div class="dsp" style="font-size:17px;font-weight:600;margin-bottom:5px">&ldquo;New&rdquo;</div>
        <div class="mono ell" style="font-size:11.5px;color:#7A8393;margin-bottom:9px">[data-testid="dashboard_screen_newbtn"]</div>
        <div style="font-size:11.5px;color:#6E7784">main area, top-left &middot; action 9 of 31 planned for this state</div>
      </div>

      <div class="card" style="padding:15px 17px 14px;flex-grow:1;display:flex;flex-direction:column;min-height:0">
        <div style="display:flex;align-items:center;gap:9px;margin-bottom:4px">
          <h2 class="dsp" style="font-size:13px;font-weight:600;letter-spacing:.3px">MAP SO FAR</h2>
          <div style="flex-grow:1"></div>
          <span class="mono" style="font-size:11px;color:#6E7784">116 states &middot; 345 edges</span>
        </div>
        <p style="font-size:11.5px;color:#6E7784;margin-bottom:8px">Nodes appear the moment a new state is fingerprinted.</p>
        <div style="flex-grow:1;border-radius:9px;background:#10141A;border:1px solid #1E242D;overflow:hidden;min-height:0">
          <svg viewBox="0 0 360 400" width="100%" height="100%" fill="none" preserveAspectRatio="xMidYMid meet">
            <g stroke="#2A323D" stroke-width="1.2">
              <path d="M180 40 L90 108"/><path d="M180 40 L180 108"/><path d="M180 40 L270 108"/>
              <path d="M90 108 L48 186"/><path d="M90 108 L118 186"/><path d="M180 108 L180 186"/>
              <path d="M180 108 L232 186"/><path d="M270 108 L300 186"/><path d="M48 186 L36 266"/>
              <path d="M118 186 L108 266"/><path d="M118 186 L162 266"/><path d="M180 186 L216 266"/>
              <path d="M232 186 L262 266"/><path d="M300 186 L316 266"/><path d="M108 266 L86 338"/>
              <path d="M162 266 L170 338"/><path d="M216 266 L238 338"/>
            </g>
            <g stroke="#2A323D" stroke-width="1.2" stroke-dasharray="3 3">
              <path d="M36 266 L30 338"/><path d="M316 266 L308 338"/>
            </g>
            <g fill="{BL}"><circle cx="90" cy="108" r="6"/><circle cx="180" cy="108" r="6"/><circle cx="270" cy="108" r="6"/></g>
            <g fill="#4E5A6B">
              <circle cx="48" cy="186" r="5"/><circle cx="118" cy="186" r="5"/><circle cx="180" cy="186" r="5"/>
              <circle cx="232" cy="186" r="5"/><circle cx="300" cy="186" r="5"/><circle cx="36" cy="266" r="5"/>
              <circle cx="108" cy="266" r="5"/><circle cx="162" cy="266" r="5"/><circle cx="216" cy="266" r="5"/>
              <circle cx="262" cy="266" r="5"/><circle cx="316" cy="266" r="5"/><circle cx="86" cy="338" r="5"/>
              <circle cx="170" cy="338" r="5"/>
            </g>
            <g fill="{VI}"><circle cx="30" cy="338" r="4.5"/><circle cx="308" cy="338" r="4.5"/></g>
            <circle cx="180" cy="40" r="9" fill="{A}"/>
            <text x="180" y="24" fill="#7A8393" font-size="10" font-family="IBM Plex Mono, monospace" text-anchor="middle">N001 entry</text>
            <circle cx="238" cy="338" r="7.5" fill="{A}"/>
            <circle cx="238" cy="338" r="14" stroke="{A}" stroke-width="1.4" opacity=".45"/>
            <circle cx="238" cy="338" r="21" stroke="{A}" stroke-width="1" opacity=".18"/>
            <text x="238" y="368" fill="{A}" font-size="10" font-family="IBM Plex Mono, monospace" text-anchor="middle">N116 new</text>
          </svg>
        </div>
        <div style="display:flex;gap:14px;margin-top:10px;flex-wrap:wrap">{legend}</div>
      </div>
    </div>

    <div style="flex-grow:1;min-width:0;background:#151A21;border:1px solid #232A34;border-radius:13px;padding:15px 0 12px;display:flex;flex-direction:column">
      <div style="display:flex;align-items:center;gap:8px;padding:0 15px;margin-bottom:11px">
        <h2 class="dsp" style="font-size:13px;font-weight:600;letter-spacing:.3px">EVENTS</h2>
        <div style="flex-grow:1"></div>
        <button aria-label="Filter events" style="width:26px;height:26px;border-radius:6px;border:1px solid #2A313C;background:#171C24;color:#7A8393;display:flex;align-items:center;justify-content:center">{icon("filter", "currentColor", 13)}</button>
      </div>
      <div style="flex-grow:1;overflow:hidden">{events}</div>
      <div style="padding:10px 15px 0;border-top:1px solid #232A34">
        <div style="display:flex;align-items:center;gap:7px">
          <span style="width:6px;height:6px;border-radius:50%;background:{A};display:block"></span>
          <span style="font-size:11px;color:#6E7784">streaming &middot; 8,412 events</span>
        </div>
      </div>
    </div>
  </div>
</div></div>""" + FOOT


# ───────────────────────── 3. EXPLORER ─────────────────────────
def screen_explorer():
    modf = "".join(
        f'<label style="display:flex;align-items:center;gap:9px;padding:5px 0">'
        f'<input type="checkbox" {"checked" if on else ""} style="width:14px;height:14px;accent-color:{A};margin:0">'
        f'<span style="width:9px;height:9px;border-radius:2px;background:{t};display:block;flex-shrink:0"></span>'
        f'<span style="font-size:12.5px;color:#C3CAD6;flex-grow:1">{n}</span>'
        f'<span class="mono" style="font-size:11px;color:#6E7784">{c}</span></label>'
        for n, c, on, t in [("Screen", "31", True, A), ("Content", "28", True, A),
                            ("Playlist", "22", True, BL), ("Schedule", "19", True, BL),
                            ("Channel", "12", True, VI), ("Settings", "46", True, AM),
                            ("Other", "17", True, "#5C6675")])

    typef = "".join(
        f'<label style="display:flex;align-items:center;gap:9px;padding:5px 0">'
        f'<input type="checkbox" {"checked" if on else ""} style="width:14px;height:14px;accent-color:{A};margin:0">'
        f'<span style="font-size:12.5px;color:#C3CAD6;flex-grow:1">{n}</span>'
        f'<span class="mono" style="font-size:11px;color:#6E7784">{c}</span></label>'
        for n, c, on in [("Page", "118", True), ("Modal", "31", True), ("Drawer", "9", True),
                         ("Dropdown", "11", True), ("Boundary", "6", False)])

    cov = "".join(
        f'<label style="display:flex;align-items:flex-start;gap:9px;padding:5px 0">'
        f'<input type="checkbox" style="width:14px;height:14px;accent-color:{AM};margin:2px 0 0">'
        f'<span style="font-size:12.5px;color:#C3CAD6;line-height:1.4">{t}</span></label>'
        for t in ["Has unexercised controls", "Blocked a write", "Capture was partial"])

    stats = "".join(
        f'<div style="padding:10px;border-radius:9px;background:#151A21;border:1px solid #222831">'
        f'<div class="dsp" style="font-size:19px;font-weight:600;color:{t}">{v}</div>'
        f'<div style="font-size:10.5px;color:#6E7784;margin-top:2px;line-height:1.3">{k}</div></div>'
        for k, v, t in [("actionable", "54", "#E7EAF0"), ("exercised", "41", A),
                        ("writes blocked", "2", VI)])

    acts = "".join(
        f'<div style="display:flex;align-items:center;gap:9px;padding:6px 0;border-bottom:1px solid #1A1F27">'
        f'<span style="width:7px;height:7px;border-radius:50%;background:{t};display:block;flex-shrink:0"></span>'
        f'<span class="ell" style="font-size:12px;color:#C3CAD6;flex-grow:1">{n}</span>'
        f'<span class="mono" style="font-size:10.5px;color:#6E7784;flex-shrink:0">{o}</span></div>'
        for n, o, t in [("Screen name (text input)", "form", BL), ("Resolution (select)", "form", BL),
                        ("Orientation (radio)", "in_page", A), ("Pick layout", "in_page", A),
                        ("Advanced settings", "in_page", A), ("Cancel", "no_change", "#7A8393"),
                        ("Save", "blocked", VI)])

    def node(x, y, w, h, title, sub, stroke, fill="#161B23", subcol="#6E7784"):
        cx = x + w / 2
        t = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" '
             f'stroke="{stroke}" stroke-width="1.5"/>')
        if sub:
            t += (f'<text x="{cx}" y="{y+16}" fill="#D6DCE6" font-size="11" text-anchor="middle" '
                  f'font-family="IBM Plex Sans,sans-serif">{title}</text>'
                  f'<text x="{cx}" y="{y+28}" fill="{subcol}" font-size="9" text-anchor="middle" '
                  f'font-family="IBM Plex Mono,monospace">{sub}</text>')
        else:
            t += (f'<text x="{cx}" y="{y+h/2+4}" fill="#D6DCE6" font-size="11" text-anchor="middle" '
                  f'font-family="IBM Plex Sans,sans-serif">{title}</text>')
        return t

    nodes = (
        node(296, 60, 108, 32, "", "", A, "#152A22") +
        f'<text x="350" y="80" fill="{A}" font-size="12" text-anchor="middle" font-family="IBM Plex Mono,monospace">N001 HOME</text>' +
        node(128, 176, 108, 34, "Screens", "N004 · 54 act", A) +
        node(296, 176, 108, 34, "Content", "N009 · 47 act", "#2E3641") +
        node(468, 176, 108, 34, "Settings", "N021 · 38 act", "#2E3641") +
        node(70, 300, 100, 34, "Screen detail", "N033", "#2E3641") +
        node(196, 300, 96, 34, "New Screen", "N047 · modal", BL, "#17222C", BL) +
        node(290, 300, 92, 34, "Upload", "", "#2E3641") +
        node(402, 300, 84, 34, "Tags", "", "#2E3641") +
        node(512, 300, 96, 34, "Plan", "", "#2E3641") +
        node(48, 432, 96, 34, "Preview", "", "#2E3641") +
        node(180, 432, 96, 34, "Pick layout", "N052 · drawer", BL, "#17222C", BL) +
        node(304, 432, 96, 34, "Schedule", "", "#2E3641") +
        node(414, 432, 96, 34, "Channels", "", "#2E3641") +
        node(540, 432, 96, 34, "Organization", "", "#2E3641") +
        f'<rect x="36" y="560" width="96" height="30" rx="8" fill="#1A1626" stroke="{VI}" stroke-dasharray="4 3"/>'
        f'<text x="84" y="579" fill="{VI}" font-size="10" text-anchor="middle" font-family="IBM Plex Mono,monospace">boundary</text>' +
        node(164, 560, 96, 30, "Confirm", "", "#2E3641") +
        node(316, 560, 96, 30, "Playlists", "", "#2E3641") +
        f'<rect x="556" y="560" width="96" height="30" rx="8" fill="#1A1626" stroke="{VI}" stroke-dasharray="4 3"/>'
        f'<text x="604" y="579" fill="{VI}" font-size="10" text-anchor="middle" font-family="IBM Plex Mono,monospace">boundary</text>'
    )

    return HEAD % "Graph explorer" + f"""
<div style="display:flex;width:1440px;height:900px">{rail(2)}
<div style="flex-grow:1;display:flex;flex-direction:column;min-width:0">

  <div style="height:62px;flex-shrink:0;border-bottom:1px solid #1E242D;padding:0 22px;display:flex;align-items:center;gap:16px">
    <div>
      <h1 class="dsp" style="font-size:18px;font-weight:600;letter-spacing:-.2px">Navigation graph</h1>
      <div style="font-size:11.5px;color:#6E7784;margin-top:1px">175 states &middot; 672 transitions &middot; captured 12 Sep</div>
    </div>
    <div style="flex-grow:1"></div>
    <div style="position:relative;width:250px">
      <input type="search" aria-label="Search states" placeholder="Search title, URL or selector" style="width:100%;height:40px;padding:0 12px 0 34px;border-radius:9px;border:1px solid #2A313C;background:#151A21;color:#E7EAF0;font-size:12.5px">
      <span style="position:absolute;left:11px;top:12px">{icon("search", "#6E7784", 15)}</span>
    </div>
    <div style="display:flex;border-radius:9px;border:1px solid #2A313C;overflow:hidden">
      <button style="height:40px;padding:0 14px;border:none;background:#1F3830;color:{A};font-size:12.5px;font-weight:500">Graph</button>
      <button style="height:40px;padding:0 14px;border:none;border-left:1px solid #2A313C;background:#151A21;color:#7A8393;font-size:12.5px;font-weight:500">List</button>
    </div>
    <button style="height:40px;padding:0 15px;border-radius:9px;border:1px solid #2A313C;background:#151A21;color:#C3CAD6;font-size:12.5px;font-weight:500;display:flex;align-items:center;gap:7px">{icon("down","currentColor",14)}Export</button>
  </div>

  <div style="flex-grow:1;display:flex;min-height:0">
    <div style="width:208px;flex-shrink:0;border-right:1px solid #1E242D;padding:18px 16px;display:flex;flex-direction:column;gap:20px;overflow:hidden">
      <div><div style="font-size:10.5px;font-weight:600;letter-spacing:.6px;color:#6E7784;margin-bottom:10px">MODULE</div>{modf}</div>
      <div><div style="font-size:10.5px;font-weight:600;letter-spacing:.6px;color:#6E7784;margin-bottom:10px">STATE TYPE</div>{typef}</div>
      <div><div style="font-size:10.5px;font-weight:600;letter-spacing:.6px;color:#6E7784;margin-bottom:10px">COVERAGE</div>{cov}</div>
    </div>

    <div style="flex-grow:1;min-width:0;position:relative;background:#0B0E13">
      <svg viewBox="0 0 700 700" width="100%" height="100%" fill="none" preserveAspectRatio="xMidYMid meet">
        <defs><pattern id="g" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" stroke="#151A21" stroke-width="1"/></pattern></defs>
        <rect width="700" height="700" fill="url(#g)"/>
        <g stroke="#2A323D" stroke-width="1.3">
          <path d="M350 92 L182 176"/><path d="M350 92 L350 176"/><path d="M350 92 L522 176"/>
          <path d="M182 210 L120 300"/><path d="M182 210 L244 300"/><path d="M350 210 L336 300"/>
          <path d="M350 210 L444 300"/><path d="M522 210 L560 300"/><path d="M120 334 L96 432"/>
          <path d="M244 334 L228 432"/><path d="M336 334 L352 432"/><path d="M444 334 L462 432"/>
          <path d="M560 334 L588 432"/><path d="M228 466 L212 560"/><path d="M352 466 L364 560"/>
        </g>
        <g stroke="#2A323D" stroke-width="1.3" stroke-dasharray="4 4"><path d="M96 466 L84 560"/><path d="M588 466 L604 560"/></g>
        <path d="M350 92 L182 176" stroke="{A}" stroke-width="2"/>
        <path d="M182 210 L244 300" stroke="{A}" stroke-width="2"/>
        <path d="M244 334 L228 432" stroke="{A}" stroke-width="2"/>
        {nodes}
      </svg>
      <div style="position:absolute;left:18px;bottom:18px;padding:11px 14px;border-radius:10px;background:#12271E;border:1px solid #2B4A3A;max-width:400px">
        <div style="font-size:11px;font-weight:600;letter-spacing:.4px;color:{A};margin-bottom:6px">SHORTEST PATH FROM ENTRY &middot; 3 STEPS</div>
        <div class="mono" style="font-size:11.5px;color:#C3CAD6;line-height:1.6">N001 &rarr; N004 &rarr; N047 &rarr; N052</div>
        <div style="font-size:11px;color:#8FB8A2;margin-top:5px">Every edge carries a locator that resolved to exactly one element at capture time.</div>
      </div>
      <div style="position:absolute;right:16px;bottom:16px;display:flex;flex-direction:column;border-radius:9px;border:1px solid #2A313C;overflow:hidden;background:#151A21">
        <button aria-label="Zoom in" style="width:38px;height:38px;border:none;background:transparent;color:#9AA3B2;display:flex;align-items:center;justify-content:center">{icon("plus","currentColor",15)}</button>
        <button aria-label="Zoom out" style="width:38px;height:38px;border:none;border-top:1px solid #242B35;background:transparent;color:#9AA3B2;display:flex;align-items:center;justify-content:center">{icon("minus","currentColor",15)}</button>
        <button aria-label="Fit to screen" style="width:38px;height:38px;border:none;border-top:1px solid #242B35;background:transparent;color:#9AA3B2;display:flex;align-items:center;justify-content:center">{icon("fit","currentColor",15)}</button>
      </div>
    </div>

    <div style="width:358px;flex-shrink:0;border-left:1px solid #1E242D;background:#12161C;display:flex;flex-direction:column;overflow:hidden">
      <div style="padding:16px 18px 14px;border-bottom:1px solid #1E242D">
        <div style="display:flex;align-items:center;gap:9px;margin-bottom:9px">
          <span class="mono" style="font-size:12px;padding:3px 8px;border-radius:6px;background:#17222C;color:{BL}">N047</span>
          <span style="font-size:11.5px;padding:3px 8px;border-radius:6px;background:#1B212A;color:#9AA3B2">modal</span>
          <span style="font-size:11.5px;padding:3px 8px;border-radius:6px;background:#1B212A;color:#9AA3B2">depth 2</span>
        </div>
        <h2 class="dsp" style="font-size:16px;font-weight:600;margin-bottom:4px">New Screen</h2>
        <div class="mono ell" style="font-size:11px;color:#6E7784">/screen &middot; opened by &ldquo;New&rdquo;</div>
      </div>
      <div style="padding:14px 18px 0">
        <div style="border-radius:9px;border:1px solid #242B35;overflow:hidden;background:#0A0D12;height:168px;position:relative">
          <div style="position:absolute;inset:0;padding:12px;display:flex;flex-direction:column;gap:8px">
            <span style="height:8px;width:40%;border-radius:3px;background:#2E3641;display:block"></span>
            <div style="flex-grow:1;border-radius:6px;background:#14191F;border:1px solid #222831;display:flex;flex-direction:column;gap:7px;padding:10px">
              <span style="height:22px;border-radius:4px;background:#1B212A;display:block"></span>
              <span style="height:22px;border-radius:4px;background:#1B212A;display:block"></span>
              <span style="height:22px;width:60%;border-radius:4px;background:#1B212A;display:block"></span>
              <div style="flex-grow:1"></div>
              <div style="display:flex;gap:7px;justify-content:flex-end">
                <span style="height:20px;width:52px;border-radius:4px;background:#242B35;display:block"></span>
                <span style="height:20px;width:52px;border-radius:4px;background:#3E6F58;display:block"></span>
              </div>
            </div>
          </div>
          <span class="mono" style="position:absolute;bottom:7px;left:9px;font-size:9.5px;color:#5C6675">N047_41a2d7d0.png</span>
        </div>
      </div>
      <div style="padding:14px 18px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px">{stats}</div>
      <div style="flex-grow:1;overflow:hidden;padding:0 18px">
        <div style="display:flex;gap:18px;border-bottom:1px solid #1E242D;margin-bottom:11px">
          <button style="padding:0 0 9px;border:none;background:transparent;border-bottom:2px solid {A};color:#E7EAF0;font-size:12.5px;font-weight:600">Exercised</button>
          <button style="padding:0 0 9px;border:none;background:transparent;border-bottom:2px solid transparent;color:#7A8393;font-size:12.5px;font-weight:500">Skipped 6</button>
          <button style="padding:0 0 9px;border:none;background:transparent;border-bottom:2px solid transparent;color:#7A8393;font-size:12.5px;font-weight:500">Network</button>
        </div>{acts}
      </div>
      <div style="padding:13px 18px 16px;border-top:1px solid #1E242D;display:flex;gap:9px">
        <button style="flex-grow:1;height:42px;border-radius:9px;border:none;background:{A};color:#0B1F17;font-size:13px;font-weight:600">View 9 test cases</button>
        <button aria-label="Open raw capture" style="width:42px;height:42px;flex-shrink:0;border-radius:9px;border:1px solid #2A313C;background:#171C24;color:#9AA3B2;display:flex;align-items:center;justify-content:center">{icon("ext","currentColor",16)}</button>
      </div>
    </div>
  </div>
</div></div>""" + FOOT


# ───────────────────────── 4. TEST CASES ─────────────────────────
def screen_cases():
    chips = "".join(
        f'<button style="height:36px;padding:0 12px;border-radius:8px;border:1px solid {ln};'
        f'background:{bg};color:{fg};font-size:12px;font-weight:500;display:flex;align-items:center;gap:7px">'
        f'{k}<span class="mono" style="font-size:11px;opacity:.75">{n}</span></button>'
        for k, n, bg, fg, ln in [("Happy Path", "412", "#1F3830", A, "#2E4A3E"),
                                 ("Negative", "337", "#151A21", "#C3CAD6", "#2A313C"),
                                 ("Edge Case", "241", "#151A21", "#C3CAD6", "#2A313C"),
                                 ("UI/UX", "186", "#151A21", "#C3CAD6", "#2A313C"),
                                 ("Form", "108", "#151A21", "#C3CAD6", "#2A313C")])

    tree = "".join(
        f'<button style="width:100%;display:flex;align-items:center;gap:9px;padding:8px 10px;'
        f'margin-bottom:2px;border-radius:8px;border:none;background:{bg};color:{fg};font-size:12.5px;text-align:left">'
        f'<span style="width:3px;height:15px;border-radius:2px;background:{t};display:block;flex-shrink:0"></span>'
        f'<span class="ell" style="flex-grow:1;padding-left:{ind}">{n}</span>'
        f'<span class="mono" style="font-size:11px;color:#6E7784;flex-shrink:0">{c}</span></button>'
        for n, c, ind, t, bg, fg in [
            ("Screen", "284", "0px", A, "transparent", "#C3CAD6"),
            ("Screen list", "61", "12px", "transparent", "transparent", "#9AA3B2"),
            ("New Screen", "39", "12px", "transparent", "#1B212A", "#E7EAF0"),
            ("Screen detail", "44", "12px", "transparent", "transparent", "#9AA3B2"),
            ("Content", "236", "0px", A, "transparent", "#C3CAD6"),
            ("Playlist", "193", "0px", BL, "transparent", "#C3CAD6"),
            ("Schedule", "167", "0px", BL, "transparent", "#C3CAD6"),
            ("Settings", "288", "0px", AM, "transparent", "#C3CAD6")])

    pre = "".join(
        f'<span style="font-size:12px;color:#C3CAD6;padding:4px 10px;border-radius:6px;background:#1B212A">{t}</span>'
        for t in ["User is signed in", "Screens list is open", "New Screen dialog is open"])

    steps = "".join(
        f'<div style="display:grid;grid-template-columns:38px 1fr 1fr;gap:0 16px;padding:12px 16px;'
        f'border-bottom:1px solid #1A1F27;align-items:start">'
        f'<span class="mono" style="font-size:12px;color:{t}">{n}</span>'
        f'<span style="font-size:12.5px;line-height:1.55;color:#D6DCE6">{a}</span>'
        f'<span style="font-size:12.5px;line-height:1.55;color:#9AA3B2">{e}</span></div>'
        for n, a, e, t in [
            ("1", "Open the Screen name field in the dialog, main area top-left.", "The field is focused and empty.", A),
            ("2", "Paste a 51-character name.", "Only the first 50 characters are accepted.", A),
            ("3", "Move focus out of the field.", "A character-count hint reads 50 / 50 with no error state.", A),
            ("4", "Read the Save button.", "Save is enabled, because the truncated value is now valid.", AM),
            ("5", "Clear the field and move focus out.", "A required-field message appears and Save becomes disabled.", A)])

    sibs = "".join(
        f'<button style="width:100%;display:flex;align-items:center;gap:11px;padding:8px 0;'
        f'border:none;border-bottom:1px solid #1A1F27;background:transparent;text-align:left">'
        f'<span class="mono" style="font-size:11.5px;color:#6E7784;flex-shrink:0">{i}</span>'
        f'<span style="width:7px;height:7px;border-radius:50%;background:{t};display:block;flex-shrink:0"></span>'
        f'<span class="ell" style="font-size:12.5px;color:#C3CAD6;flex-grow:1">{n}</span>'
        f'{flag}</button>'
        for i, n, t, flag in [
            ("TC_044", "Create a screen with valid details", A, ""),
            ("TC_045", "Cancel the dialog without saving", A, ""),
            ("TC_046", "Accept a name at exactly 50 characters", AM, ""),
            ("TC_048", "Reject a name containing angle brackets", "#E09A9A",
             f'<span style="font-size:10.5px;padding:2px 7px;border-radius:5px;background:#2A2416;'
             f'color:{AM};flex-shrink:0">needs review</span>'),
            ("TC_049", "Dialog traps focus and closes on Escape", BL, "")])

    cons = "".join(
        f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid #1A1F27">'
        f'<span class="mono" style="font-size:11.5px;color:#7A8393;width:92px;flex-shrink:0">{k}</span>'
        f'<span class="mono" style="font-size:11.5px;color:{t};flex-grow:1">{v}</span></div>'
        for k, v, t in [("required", "true", "#D6DCE6"), ("maxlength", "50", A),
                        ("pattern", "^[^&lt;&gt;]+$", "#D6DCE6"), ("label", "Screen name", "#D6DCE6")])

    return HEAD % "Test cases" + f"""
<div style="display:flex;width:1440px;height:900px">{rail(3)}
<div style="flex-grow:1;display:flex;flex-direction:column;min-width:0">

  <div style="height:62px;flex-shrink:0;border-bottom:1px solid #1E242D;padding:0 22px;display:flex;align-items:center;gap:14px">
    <div>
      <h1 class="dsp" style="font-size:18px;font-weight:600;letter-spacing:-.2px">Test cases</h1>
      <div style="font-size:11.5px;color:#6E7784;margin-top:1px">1,284 cases from 175 states &middot; generated in 9m 12s</div>
    </div>
    <div style="flex-grow:1"></div>
    <div style="display:flex;gap:6px">{chips}</div>
    <button style="height:40px;padding:0 13px;border-radius:9px;border:1px solid #4A3A22;background:#2A2416;color:{AM};font-size:12.5px;font-weight:500;display:flex;align-items:center;gap:7px">{icon("warn","currentColor",14)}Needs review 38</button>
    <button style="height:40px;padding:0 15px;border-radius:9px;border:none;background:{A};color:#0B1F17;font-size:12.5px;font-weight:600;display:flex;align-items:center;gap:7px">{icon("down","#0B1F17",14)}Export</button>
  </div>

  <div style="flex-grow:1;display:flex;min-height:0">
    <div style="width:230px;flex-shrink:0;border-right:1px solid #1E242D;padding:16px 12px;overflow:hidden">
      <div style="font-size:10.5px;font-weight:600;letter-spacing:.6px;color:#6E7784;margin:0 6px 10px">BY MODULE</div>{tree}
    </div>

    <div style="flex-grow:1;min-width:0;padding:18px 22px;overflow:hidden;display:flex;flex-direction:column;gap:14px">
      <div style="display:flex;align-items:flex-start;gap:14px">
        <div style="min-width:0;flex-grow:1">
          <div style="display:flex;align-items:center;gap:9px;margin-bottom:7px">
            <span class="mono" style="font-size:12.5px;padding:3px 9px;border-radius:6px;background:#1B212A;color:#9AA3B2">TC_047</span>
            <span style="font-size:11.5px;padding:3px 9px;border-radius:6px;background:#2A1C1C;color:#E09A9A">Negative</span>
            <span class="mono" style="font-size:11.5px;color:#6E7784">N047 &middot; /screen</span>
          </div>
          <h2 class="dsp" style="font-size:21px;font-weight:600;letter-spacing:-.2px;line-height:1.3">Reject a screen name longer than the 50-character limit</h2>
        </div>
        <div style="display:flex;gap:8px;flex-shrink:0">
          <button aria-label="Previous case" style="width:40px;height:40px;border-radius:9px;border:1px solid #2A313C;background:#151A21;color:#9AA3B2;display:flex;align-items:center;justify-content:center">{icon("left","currentColor",15)}</button>
          <button aria-label="Next case" style="width:40px;height:40px;border-radius:9px;border:1px solid #2A313C;background:#151A21;color:#9AA3B2;display:flex;align-items:center;justify-content:center">{icon("right","currentColor",15)}</button>
        </div>
      </div>

      <div style="padding:12px 15px;border-radius:10px;background:#151A21;border:1px solid #222831">
        <div style="font-size:10.5px;font-weight:600;letter-spacing:.5px;color:#6E7784;margin-bottom:7px">PRECONDITIONS</div>
        <div style="display:flex;flex-wrap:wrap;gap:7px">{pre}</div>
        <div style="font-size:11.5px;color:#6E7784;margin-top:9px;display:flex;align-items:center;gap:7px">
          {icon("graph", A, 13)}Reachability taken from the graph, not guessed: <span class="mono" style="color:#8FB8A2">N001 &rarr; N004 &rarr; N047</span>
        </div>
      </div>

      <div style="flex-grow:1;border-radius:10px;background:#151A21;border:1px solid #222831;overflow:hidden;display:flex;flex-direction:column;min-height:0">
        <div style="display:grid;grid-template-columns:38px 1fr 1fr;gap:0 16px;padding:11px 16px;border-bottom:1px solid #222831;font-size:10.5px;font-weight:600;letter-spacing:.5px;color:#6E7784">
          <span>#</span><span>ACTION</span><span>EXPECTED RESULT</span>
        </div>{steps}
        <div style="padding:14px 16px 6px;flex-grow:1;overflow:hidden">
          <div style="font-size:10.5px;font-weight:600;letter-spacing:.5px;color:#6E7784;margin-bottom:6px">OTHER CASES ON THIS STATE</div>{sibs}
        </div>
        <div style="padding:13px 16px;background:#12271E;border-top:1px solid #2B4A3A">
          <div style="font-size:10.5px;font-weight:600;letter-spacing:.5px;color:{A};margin-bottom:5px">OVERALL EXPECTED RESULT</div>
          <p style="font-size:12.5px;line-height:1.55;color:#C3CAD6">The screen is not created. The name field stops accepting input at 50 characters and the Save button stays disabled until the value is within the limit.</p>
        </div>
      </div>
    </div>

    <div style="width:382px;flex-shrink:0;border-left:1px solid #1E242D;background:#12161C;display:flex;flex-direction:column;overflow:hidden">
      <div style="padding:16px 18px 12px">
        <h2 class="dsp" style="font-size:14px;font-weight:600;margin-bottom:3px">Evidence</h2>
        <p style="font-size:11.5px;color:#6E7784;line-height:1.45">Every selector this case cites was present in the capture. Boxes are drawn from the geometry recorded at extraction.</p>
      </div>
      <div style="padding:0 18px">
        <div style="border-radius:10px;border:1px solid #242B35;overflow:hidden;background:#0A0D12;height:246px;position:relative">
          <div style="position:absolute;inset:0;padding:14px;display:flex;flex-direction:column;gap:9px">
            <span style="height:9px;width:34%;border-radius:3px;background:#2E3641;display:block"></span>
            <div style="flex-grow:1;border-radius:7px;background:#14191F;border:1px solid #222831;padding:12px;display:flex;flex-direction:column;gap:11px">
              <div style="position:relative">
                <span style="display:block;height:30px;border-radius:5px;background:#1B212A;border:2px solid {AM}"></span>
                <span class="mono" style="position:absolute;top:-9px;left:8px;font-size:9px;padding:1px 5px;border-radius:3px;background:{AM};color:#1A1206;font-weight:500">#screen_nameInput</span>
              </div>
              <span style="height:30px;border-radius:5px;background:#1B212A;display:block"></span>
              <span style="height:30px;width:62%;border-radius:5px;background:#1B212A;display:block"></span>
              <div style="flex-grow:1"></div>
              <div style="display:flex;gap:8px;justify-content:flex-end;align-items:center">
                <span style="height:26px;width:62px;border-radius:5px;background:#242B35;display:block"></span>
                <div style="position:relative">
                  <span style="display:block;height:26px;width:62px;border-radius:5px;background:#2A3D34;border:2px solid {A}"></span>
                  <span class="mono" style="position:absolute;top:-11px;right:0;font-size:9px;padding:1px 5px;border-radius:3px;background:{A};color:#0B1F17;font-weight:500">#screen_saveBtn</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="padding:16px 18px 0">
        <div style="font-size:10.5px;font-weight:600;letter-spacing:.5px;color:#6E7784;margin-bottom:9px">FIELD CONSTRAINTS READ FROM THE DOM</div>{cons}
        <p style="font-size:11.5px;line-height:1.5;color:#6E7784;margin-top:11px">The negative and edge cases come from these constraints. The form was never submitted.</p>
      </div>
      <div style="flex-grow:1"></div>
      <div style="padding:14px 18px 16px;border-top:1px solid #1E242D;display:flex;gap:9px">
        <button style="flex-grow:1;height:42px;border-radius:9px;border:1px solid #2E4A3E;background:#172620;color:{A};font-size:12.5px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:7px">{icon("check","currentColor",15)}Approve</button>
        <button style="flex-grow:1;height:42px;border-radius:9px;border:1px solid #2A313C;background:#171C24;color:#C3CAD6;font-size:12.5px;font-weight:500">Edit</button>
        <button aria-label="Reject case" style="width:42px;height:42px;flex-shrink:0;border-radius:9px;border:1px solid #3D2A2A;background:#1F1717;color:#D99A9A;display:flex;align-items:center;justify-content:center">{icon("x","currentColor",15)}</button>
      </div>
    </div>
  </div>
</div></div>""" + FOOT


PAGES = {
    "01-new-run": screen_new_run,
    "02-live-run": screen_live,
    "03-graph-explorer": screen_explorer,
    "04-test-cases": screen_cases,
}

for name, fn in PAGES.items():
    (OUT / f"{name}.html").write_text(fn(), encoding="utf-8")
    print("wrote", OUT / f"{name}.html")
