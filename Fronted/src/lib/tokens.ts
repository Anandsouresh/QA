/** Semantic colour, in one place.
 *
 *  Every value here is a reference to a runtime CSS variable defined in
 *  index.css, never a literal. That is what lets the theme switch without a
 *  re-render: the browser re-resolves `var(--qg-accent)` when `data-theme`
 *  changes on <html>.
 *
 *  Consequence worth knowing: these strings are only valid in CSS *properties*
 *  (a `style` object, a stylesheet). SVG presentation *attributes* do not
 *  resolve var(), so components pass them through `style={{ fill: … }}` rather
 *  than `fill="…"`. See Icon in components/ui.tsx.
 */

export const C = {
  ground: "var(--qg-ground)",
  panel: "var(--qg-panel)",
  aside: "var(--qg-aside)",
  surface: "var(--qg-surface)",
  card: "var(--qg-card)",
  raised: "var(--qg-raised)",
  ghost: "var(--qg-ghost)",
  inset: "var(--qg-inset)",
  sunken: "var(--qg-sunken)",
  well: "var(--qg-well)",
  canvas: "var(--qg-canvas)",
  canvasDot: "var(--qg-canvas-dot)",
  chrome: "var(--qg-chrome)",
  hover: "var(--qg-hover)",
  track: "var(--qg-track)",

  line: "var(--qg-line)",
  lineSoft: "var(--qg-line-soft)",
  lineStrong: "var(--qg-line-strong)",
  lineHover: "var(--qg-line-hover)",
  railLine: "var(--qg-rail-line)",

  ink: "var(--qg-ink)",
  inkStrong: "var(--qg-ink-strong)",
  inkBody: "var(--qg-ink-body)",
  ink2: "var(--qg-ink-2)",
  ink3: "var(--qg-ink-3)",
  ink4: "var(--qg-ink-4)",
  inkLog: "var(--qg-ink-log)",

  accent: "var(--qg-accent)",
  accentDim: "var(--qg-accent-dim)",
  accentLine: "var(--qg-accent-line)",
  accentDeep: "var(--qg-accent-deep)",
  accentInk: "var(--qg-accent-ink)",

  amber: "var(--qg-amber)",
  amberInk: "var(--qg-amber-ink)",
  amberDeep: "var(--qg-amber-deep)",
  blue: "var(--qg-blue)",
  red: "var(--qg-red)",
  redInk: "var(--qg-red-ink)",
  violet: "var(--qg-violet)",
  muted: "var(--qg-muted)",
} as const;

export type Tone = "accent" | "amber" | "blue" | "red" | "violet" | "muted" | "ink";

export const TONE_HEX: Record<Tone, string> = {
  accent: C.accent,
  amber: C.amber,
  blue: C.blue,
  red: C.red,
  violet: C.violet,
  muted: C.muted,
  ink: C.ink,
};

/** The nine outcomes an action can have (qagen/models.py::Outcome). */
export const OUTCOME_TONE: Record<string, Tone> = {
  navigation: "accent",
  in_page_state: "blue",
  new_tab: "blue",
  no_change: "muted",
  native_dialog: "amber",
  file_chooser: "amber",
  download: "amber",
  blocked_mutation: "violet",
  error: "red",
};

export const NODE_TYPE_TONE: Record<string, Tone> = {
  page: "muted",
  modal: "blue",
  drawer: "blue",
  dropdown: "blue",
  panel: "blue",
  boundary: "violet",
  external: "violet",
};

/** Event classes as ActionLog emits them. */
export const EVENT_TONE: Record<string, Tone> = {
  state_found: "accent",
  state_duplicate: "muted",
  navigate: "ink",
  action: "ink",
  action_done: "muted",
  outcome: "blue",
  overlay_queued: "blue",
  restore: "muted",
  skip: "red",
  budget: "muted",
  finished: "accent",
  blocked: "violet",
  dialog: "amber",
  paused: "amber",
  resumed: "accent",
  completion: "accent",
  cap_summary: "amber",
};

export const EVENT_LABEL: Record<string, string> = {
  state_found: "STATE",
  state_duplicate: "DUPLICATE",
  navigate: "NAVIGATE",
  action: "ACTION",
  action_done: "DONE",
  outcome: "OUTCOME",
  overlay_queued: "OVERLAY",
  restore: "RESTORE",
  skip: "SKIP",
  budget: "BUDGET",
  finished: "FINISHED",
  paused: "PAUSED",
  resumed: "RESUMED",
  completion: "COMPLETE",
  cap_summary: "CAP",
};

export const CATEGORY_TONE: Record<string, Tone> = {
  "Happy Path": "accent",
  Negative: "red",
  "Edge Case": "amber",
  "UI/UX": "blue",
  "Form Filling": "violet",
};

/** A translucent wash of a tone, for chip and badge backgrounds.
 *
 *  `color-mix` rather than hex arithmetic, because the tones are now CSS
 *  variables whose value depends on the active theme and is not known here. */
export function wash(tone: Tone, alpha = 0.14): string {
  const pct = Math.round(Math.max(0, Math.min(1, alpha)) * 100);
  return `color-mix(in srgb, ${TONE_HEX[tone]} ${pct}%, transparent)`;
}

export function moduleTone(module: string): Tone {
  const map: Record<string, Tone> = {
    Screen: "accent",
    Content: "accent",
    Home: "accent",
    "(home)": "accent",
    Playlist: "blue",
    Schedule: "blue",
    Channel: "violet",
    Settings: "amber",
    Apps: "muted",
    "VXT Labs": "muted",
    Other: "muted",
  };
  return map[module] ?? "muted";
}
