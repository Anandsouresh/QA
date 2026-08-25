"""PageModel -> compact prompt block.

A rendered React page can be 500 KB of DOM; the model needs maybe 4 KB of it.
Two properties matter here:

* **Deterministic ordering** -- sorted by role then name. Non-deterministic
  ordering silently breaks prompt caching, which is most of the cost saving on
  a multi-page run.
* **Denied and blocked items are included, not hidden.** A "Delete account"
  button we refused to click is excellent input for a confirmation test case.
  Withholding it makes the output worse, not safer.
"""

from __future__ import annotations

from ..models import Element, ElementKind, NavEdge, PageModel

_SKIP_IN_INVENTORY = {ElementKind.UNKNOWN}


def _describe(el: Element) -> str:
    bits = [f"{el.kind.value:<18}", f'"{el.name}"' if el.name else "(unnamed)"]
    bits.append(f"[{el.selector}]")
    if el.location:
        # The human half of "where is it": a tester following the step reads
        # this, the automation reads the selector.
        bits.append(f"({el.location})")
    if el.href:
        bits.append(f"-> {el.href}")
    if not el.enabled:
        bits.append("DISABLED")
    if el.confidence.value in {"low", "medium"}:
        bits.append(f"confidence={el.confidence.value}")
    return "  " + " ".join(bits)


def summarize(
    page: PageModel,
    reachability: list[NavEdge] | None = None,
    denied: list[tuple[str, str]] | None = None,
) -> str:
    """Build the per-page prompt block."""
    lines: list[str] = []

    lines.append(f"URL: {page.url}")
    lines.append(f"NORMALIZED: {page.normalized_url}")
    lines.append(f"TITLE: {page.title or '(none)'}")
    lines.append(f"REACHED BY: {page.arrival_action}")

    if reachability:
        path = " -> ".join(e.label for e in reachability)
        lines.append(f"NAVIGATION PATH FROM ENTRY: {path}")
    elif reachability is not None:
        lines.append("NAVIGATION PATH FROM ENTRY: (this is the entry page)")

    if page.landmarks:
        marks = ", ".join(
            f"{l.role}({l.label})" if l.label else l.role for l in page.landmarks
        )
        lines.append(f"LANDMARKS: {marks}")

    if page.overlays:
        open_overlays = ", ".join(
            f"{o.overlay_type.value}({o.label or 'unlabelled'})" for o in page.overlays
        )
        lines.append(f"OPEN OVERLAYS: {open_overlays}")

    # -- interactive inventory, deterministically ordered ------------------
    inventory = sorted(
        (e for e in page.elements if e.kind not in _SKIP_IN_INVENTORY),
        key=lambda e: (e.kind.value, e.name.lower(), e.selector),
    )
    if inventory:
        lines.append("")
        lines.append("INTERACTIVE ELEMENTS:")
        lines.extend(_describe(el) for el in inventory[:120])
        if len(inventory) > 120:
            lines.append(f"  ... {len(inventory) - 120} more omitted")

    # -- forms -------------------------------------------------------------
    if page.forms:
        lines.append("")
        lines.append("FORMS:")
        for form in sorted(page.forms, key=lambda f: f.form_id):
            head = f"  {form.form_id} ({form.origin}"
            if form.method or form.action:
                head += f", {form.method or '?'} {form.action or '?'}"
            head += f") submit={form.submit_label or 'none'}"
            lines.append(head)
            for field in form.fields:
                constraints = field.constraint_summary()
                lines.append(
                    f"    {field.input_type:<12} "
                    f"name={field.name or '?'} "
                    f'label="{field.label or "?"}" '
                    f"[{field.selector}] {constraints}".rstrip()
                )
                if field.options:
                    shown = ", ".join(field.options[:8])
                    more = "" if len(field.options) <= 8 else f" (+{len(field.options)-8})"
                    lines.append(f"      options: {shown}{more}")
                if field.validation_message:
                    lines.append(f"      existing validation text: {field.validation_message}")

    if page.searches:
        lines.append("")
        lines.append("SEARCH CONTROLS:")
        for s in page.searches:
            lines.append(
                f"  input=[{s.input_selector}] submit={s.submit_selector or 'Enter key'} "
                f"via={s.submits_via} live_suggestions={s.live_suggestions}"
            )

    # -- what we deliberately did not do ----------------------------------
    if denied:
        lines.append("")
        lines.append("NOT EXERCISED BY THE CRAWLER (still worth testing):")
        for label, reason in denied[:25]:
            lines.append(f"  {label} -- {reason}")

    if page.blocked_mutations:
        lines.append("")
        lines.append("SERVER WRITES ATTEMPTED AND BLOCKED (these endpoints exist):")
        for entry in sorted(set(page.blocked_mutations))[:15]:
            lines.append(f"  {entry}")

    if page.observations:
        lines.append("")
        lines.append("OBSERVED BEHAVIOUR:")
        for obs in page.observations[:15]:
            trigger = f" (from {obs.triggered_by})" if obs.triggered_by else ""
            lines.append(f"  {obs.kind}: {obs.detail}{trigger}")

    endpoints = sorted(
        {f"{n.method} {n.url.split('?')[0]}" for n in page.network if not n.blocked}
    )
    if endpoints:
        lines.append("")
        lines.append("NETWORK ENDPOINTS OBSERVED:")
        lines.extend(f"  {e}" for e in endpoints[:20])

    if page.console_errors:
        lines.append("")
        lines.append("CONSOLE ERRORS (UI/UX defect signal):")
        lines.extend(f"  {e}" for e in sorted(set(page.console_errors))[:10])

    if page.capture_status != "complete":
        lines.append("")
        lines.append(f"NOTE: capture was {page.capture_status}; inventory may be incomplete.")

    return "\n".join(lines)
