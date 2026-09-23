/** The only place that knows where data comes from.
 *
 *  Two sources, one shape:
 *
 *  - **live**  the FastAPI service in ../api, reading a real run directory.
 *  - **demo**  the fixtures under public/data, extracted from a finished run
 *              by scripts/make_fixtures.py. Used when the service is not
 *              running, so the UI is always explorable.
 *
 *  The adapters below normalise the raw qagen output into the shapes the
 *  screens expect. They add nothing the crawler did not record: `module` is
 *  derived from the URL the same way the crawler groups sections, and a case's
 *  highlight is a lookup of a selector it already cites.
 */

import { moduleOf } from "./modules";
import type {
  Graph,
  LogEvent,
  NavNode,
  RunSummary,
  StateRec,
  TestCase,
} from "./types";

const BASE = import.meta.env.BASE_URL || "/";
export const API_BASE =
  (import.meta.env.VITE_API_BASE as string | undefined) || "http://localhost:8000";

export type Source = { kind: "demo" } | { kind: "live"; runId: string };

let source: Source = { kind: "demo" };

export function getSource(): Source {
  return source;
}

export function setSource(next: Source): void {
  source = next;
  cache.clear();
}

/** One in-flight promise per key, so panels mounting together share a read. */
const cache = new Map<string, Promise<unknown>>();
function once<T>(key: string, load: () => Promise<T>): Promise<T> {
  if (!cache.has(key)) cache.set(key, load());
  return cache.get(key) as Promise<T>;
}

export function invalidate(): void {
  cache.clear();
}

async function fixture<T>(file: string): Promise<T> {
  const res = await fetch(`${BASE}data/${file}`);
  if (!res.ok) throw new Error(`${file}: ${res.status}`);
  return (await res.json()) as T;
}

async function live<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!res.ok) {
    let detail = `${res.status} ${res.statusText}`;
    try {
      const body = await res.json();
      if (body?.detail) detail = String(body.detail);
    } catch {
      /* the body was not JSON; the status line is what we have */
    }
    throw new Error(detail);
  }
  return (await res.json()) as T;
}

/* ── control plane ─────────────────────────────────────────────────────── */

export interface RunRow {
  id: string;
  label: string;
  target: string;
  status: string;
  mode: string;
  pid: number | null;
  created_at: string;
  finished_at: string | null;
  exit_code: number | null;
  modules: Record<string, number>;
  max_states: number;
  has_graph: boolean;
  has_cases: boolean;
  log_bytes: number;
}

export const control = {
  health: () => live<{ ok: boolean; runs_dir: string }>("/api/health"),
  runs: () => live<RunRow[]>("/api/runs"),
  run: (id: string) => live<RunRow & { manifest: any; alive: boolean }>(`/api/runs/${id}`),
  start: (body: unknown) =>
    live<{ id: string; pid: number; max_states: number; command: string }>("/api/runs", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  stop: (id: string) => live(`/api/runs/${id}/stop`, { method: "POST" }),
  pause: (id: string) => live(`/api/runs/${id}/pause`, { method: "POST" }),
  resume: (id: string) => live(`/api/runs/${id}/resume`, { method: "POST" }),
  remove: (id: string) => live(`/api/runs/${id}`, { method: "DELETE" }),
  probeAuth: (body: unknown) =>
    live<{ ok: boolean; code?: string; detail?: string; landed_on?: string; title?: string }>(
      "/api/preflight/auth",
      { method: "POST", body: JSON.stringify(body) },
    ),
  probeModules: (body: unknown) =>
    live<{
      title: string;
      dom_nodes: number;
      modules: { name: string; paths: string[]; path_count: number; links: number }[];
      suggested_budgets: Record<string, number>;
      external_hosts: string[];
    }>("/api/preflight/modules", { method: "POST", body: JSON.stringify(body) }),
};

/* ── adapters ──────────────────────────────────────────────────────────── */

function adaptGraph(raw: any): Graph {
  const nodes: NavNode[] = (raw.nodes ?? []).map((n: any) => ({
    ...n,
    module: n.module ?? moduleOf(n.normalized_url || n.url || ""),
    actions: n.actions ?? [],
    actions_total: n.actions_total ?? (n.actions?.length ?? 0),
    not_exercised: n.not_exercised ?? [],
    not_exercised_total: n.not_exercised_total ?? (n.not_exercised?.length ?? 0),
  }));
  return {
    target: raw.target ?? "",
    generated_at: raw.generated_at ?? "",
    entry_node: raw.entry_node || nodes.find((n) => n.is_entry)?.id || nodes[0]?.id || "",
    total_nodes: raw.total_nodes ?? nodes.length,
    total_edges: raw.total_edges ?? (raw.edges?.length ?? 0),
    nodes,
    edges: raw.edges ?? [],
    paths: raw.paths ?? {},
    module_tone: raw.module_tone ?? {},
  };
}

function adaptStates(raw: any[], runId?: string): StateRec[] {
  return (raw ?? []).map((p) => ({
    fingerprint: p.fingerprint ?? "",
    url: p.url ?? "",
    normalized_url: p.normalized_url ?? "",
    title: p.title ?? "",
    module: p.module ?? moduleOf(p.normalized_url || p.url || ""),
    depth: p.depth ?? 0,
    arrival_action: p.arrival_action ?? "",
    viewport_width: p.viewport_width || 1200,
    viewport_height: p.viewport_height || 900,
    document_height: p.document_height || p.viewport_height || 900,
    dom_nodes: p.dom_nodes ?? 0,
    screenshot: normaliseShot(p.screenshot ?? p.screenshot_path ?? null, runId),
    blocked_mutations: p.blocked_mutations ?? [],
    console_errors: p.console_errors ?? [],
    elements: (p.elements ?? []).filter((e: any) => e.visible !== false),
  }));
}

/** `artifacts/N001_ab12.png` resolves against the fixtures or the API. */
function normaliseShot(path: string | null, runId?: string): string | null {
  if (!path) return null;
  const name = path.split(/[\\/]/).pop()!;
  return runId ? `${API_BASE}/api/runs/${runId}/artifacts/${name}` : `artifacts/${name}`;
}

const TITLE_NOTE = "title: ";

function adaptCases(raw: any[], states: StateRec[], graph: Graph): TestCase[] {
  const byUrl = new Map<string, StateRec>();
  states.forEach((s) => {
    if (!byUrl.has(s.url)) byUrl.set(s.url, s);
  });
  const nodeByFp = new Map(graph.nodes.map((n) => [n.fingerprint, n]));

  return (raw ?? []).map((c: any, i: number) => {
    if (c.title !== undefined && c.highlight !== undefined) return c as TestCase;

    const notes: string[] = c.review_notes ?? [];
    // The generator smuggles the title through review_notes; qagen's own
    // markdown writer reads it back the same way (report/markdown.py).
    const titleNote = notes.find((n) => n.startsWith(TITLE_NOTE));
    const state = byUrl.get(c.source_url) ?? null;
    const node = state ? nodeByFp.get(state.fingerprint) : undefined;
    const selector: string | undefined = (c.source_selectors ?? [])[0];
    const el = selector ? state?.elements.find((e) => e.selector === selector) : undefined;
    const validGeometry =
      !!el && el.x >= 0 && el.y >= 0 && el.w > 0 && el.h > 0 &&
      el.y + el.h <= (state?.document_height ?? 0) + 20;

    return {
      test_id: c.test_id ?? `TC_${String(i + 1).padStart(3, "0")}`,
      category: c.category,
      title: titleNote ? titleNote.slice(TITLE_NOTE.length) : firstSentence(c.overall_expected_result),
      preconditions: c.preconditions ?? [],
      steps: c.steps ?? [],
      overall_expected_result: c.overall_expected_result ?? "",
      source_state: node?.id ?? "",
      source_fingerprint: state?.fingerprint ?? "",
      source_url: c.source_url ?? "",
      module: state?.module ?? moduleOf(c.source_url ?? ""),
      source_selectors: c.source_selectors ?? [],
      highlight: el ? { x: el.x, y: el.y, w: el.w, h: el.h, label: el.selector } : null,
      highlight_valid: validGeometry,
      reachability: node ? graph.paths[node.id] ?? [] : [],
      needs_review: !!c.needs_review,
      review_notes: notes.filter((n) => !n.startsWith(TITLE_NOTE)),
      constraints: c.constraints ?? [],
    } as TestCase;
  });
}

function firstSentence(text: string | undefined): string {
  if (!text) return "Untitled case";
  const cut = text.split(/(?<=\.)\s/)[0];
  return cut.length > 90 ? `${cut.slice(0, 88)}…` : cut;
}

function adaptRun(row: any): RunSummary {
  const m = row.manifest ?? {};
  const crawl = m.crawl ?? {};
  return {
    id: row.id,
    target: row.target,
    status: row.status,
    started_at: m.started_at ?? row.created_at,
    duration_seconds: m.duration_seconds ?? 0,
    auth_status: m.auth_status ?? "unknown",
    states_discovered: crawl.states_discovered ?? crawl.states_loaded ?? 0,
    graph_nodes: crawl.graph_nodes ?? 0,
    graph_edges: crawl.graph_edges ?? 0,
    actionable_elements: crawl.actionable_elements ?? 0,
    total_elements: crawl.total_elements ?? 0,
    blocked_mutations: crawl.blocked_mutations ?? [],
    skipped_elements: crawl.skipped_elements ?? [],
    budgets: {
      pages_visited: 0, navigations: 0, max_pages: row.max_states ?? 0,
      clicks_made: 0, max_clicks: 0, elapsed_seconds: 0,
      max_wall_clock_seconds: 86400, consecutive_no_new_states: 0, stop_reason: null,
      ...(crawl.budgets ?? {}),
    },
    module_budgets: row.modules ?? {},
    module_states: {},
    config: {
      depth: m.config?.target?.depth ?? 0,
      headless: m.config?.browser?.headless ?? true,
      block_mutations: m.config?.browser?.block_mutations ?? true,
      model: m.config?.llm?.model ?? "claude-opus-5",
      deny_text: m.config?.interaction?.deny_text ?? [],
    },
  };
}

/* ── the data the screens read ─────────────────────────────────────────── */

export const api = {
  run: (): Promise<RunSummary> =>
    once("run", async () => {
      if (source.kind === "demo") return fixture<RunSummary>("run.json");
      return adaptRun(await control.run(source.runId));
    }),

  graph: (): Promise<Graph> =>
    once("graph", async () => {
      if (source.kind === "demo") return adaptGraph(await fixture<any>("graph.json"));
      const [raw, paths] = await Promise.all([
        live<any>(`/api/runs/${source.runId}/graph`),
        live<any>(`/api/runs/${source.runId}/paths`).catch(() => ({})),
      ]);
      return adaptGraph({ ...raw, paths });
    }),

  states: (): Promise<StateRec[]> =>
    once("states", async () => {
      if (source.kind === "demo") return adaptStates(await fixture<any[]>("states.json"));
      return adaptStates(await live<any[]>(`/api/runs/${source.runId}/states`), source.runId);
    }),

  cases: (): Promise<TestCase[]> =>
    once("cases", async () => {
      if (source.kind === "demo") return fixture<TestCase[]>("cases.json");
      const [raw, states, graph] = await Promise.all([
        live<any>(`/api/runs/${source.runId}/cases`),
        api.states(),
        api.graph(),
      ]);
      return adaptCases(raw.cases ?? raw, states, graph);
    }),

  /** Only the demo replay uses this; a live run streams over SSE instead. */
  events: (): Promise<LogEvent[]> => once("events", () => fixture<LogEvent[]>("events.json")),
};

/** The newest capture of a live run, or null in demo mode.
 *  `tick` busts the browser cache so the panel actually refreshes. */
export function frameUrl(tick: number): string | null {
  if (source.kind !== "live") return null;
  return `${API_BASE}/api/runs/${source.runId}/frame?t=${tick}`;
}

/** Resolve a screenshot reference for <img src>. */
export function shotUrl(path: string | null | undefined): string | null {
  if (!path) return null;
  if (path.startsWith("http")) return path;
  return `${BASE}${path.replace(/^\/+/, "")}`;
}
