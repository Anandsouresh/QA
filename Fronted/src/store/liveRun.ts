/** Live-run state.
 *
 *  Two ways in, one reducer:
 *
 *  - **stream**  an EventSource on `GET /api/runs/{id}/events`, which the API
 *                produces by tailing crawl-log.jsonl as the crawler writes it.
 *  - **replay**  a recorded log played back on a timer, used when no backend is
 *                running so the screen is still demonstrable.
 *
 *  `reduce` is pure and shared, so both paths produce identical state and the
 *  components cannot tell which one they are watching.
 */

import { create } from "zustand";
import { api, API_BASE } from "../lib/api";
import { moduleOf } from "../lib/modules";
import type { LogEvent } from "../lib/types";

export interface DiscoveredState {
  id: string;
  url: string;
  module: string;
  elements: number;
  depth: number;
  t: number;
}

export interface CurrentAction {
  node: string;
  kind: string;
  name: string;
  selector: string;
  startedAt: number;
  index: number;
}

export interface Derived {
  elapsed: number;
  clicks: number;
  navigations: number;
  skips: number;
  blockedWrites: number;
  dialogs: number;
  states: DiscoveredState[];
  moduleStates: Record<string, number>;
  current: CurrentAction | null;
  lastOutcome: { name: string; outcome: string; annotations: string[] } | null;
  feed: LogEvent[];
  finished: boolean;
  stopReason: string | null;
}

const EMPTY: Derived = {
  elapsed: 0,
  clicks: 0,
  navigations: 0,
  skips: 0,
  blockedWrites: 0,
  dialogs: 0,
  states: [],
  moduleStates: {},
  current: null,
  lastOutcome: null,
  feed: [],
  finished: false,
  stopReason: null,
};

const FEED_LIMIT = 60;
const STATE_LIMIT = 400;

export function reduce(d: Derived, e: LogEvent): Derived {
  const feed = [e, ...d.feed].slice(0, FEED_LIMIT);
  const next: Derived = { ...d, feed, elapsed: e.t ?? d.elapsed };

  switch (e.event) {
    case "state_found": {
      const url = String(e.url ?? "");
      const mod = moduleOf(url);
      next.states = [
        ...d.states,
        {
          id: String(e.node ?? ""),
          url,
          module: mod,
          elements: Number(e.elements ?? 0),
          depth: Number(e.depth ?? 0),
          t: e.t,
        },
      ].slice(-STATE_LIMIT);
      next.moduleStates = { ...d.moduleStates, [mod]: (d.moduleStates[mod] ?? 0) + 1 };
      break;
    }
    case "action":
      next.clicks = d.clicks + 1;
      next.current = {
        node: String(e.node ?? ""),
        kind: String(e.kind ?? ""),
        name: String(e.name ?? "") || "(unnamed)",
        selector: String(e.selector ?? ""),
        startedAt: e.t,
        index: d.clicks + 1,
      };
      next.lastOutcome = null;
      break;
    case "navigate":
      next.navigations = d.navigations + 1;
      break;
    case "outcome":
      next.lastOutcome = {
        name: String(e.name ?? ""),
        outcome: String(e.outcome ?? ""),
        annotations: (e.annotations as string[]) ?? [],
      };
      if (String(e.outcome) === "blocked_mutation") next.blockedWrites = d.blockedWrites + 1;
      break;
    case "skip":
      next.skips = d.skips + 1;
      break;
    case "action_done":
      next.current = null;
      break;
    case "finished":
    case "completion":
      next.finished = true;
      next.stopReason = e.detail ?? null;
      next.current = null;
      break;
    default:
      if (e.event.includes("dialog")) next.dialogs = d.dialogs + 1;
      if (e.event.includes("blocked")) next.blockedWrites = d.blockedWrites + 1;
      break;
  }
  return next;
}

type Mode = "idle" | "replay" | "stream";

interface LiveStore {
  mode: Mode;
  loaded: boolean;
  error: string | null;
  events: LogEvent[];
  cursor: number;
  playing: boolean;
  speed: number;
  runId: string | null;
  derived: Derived;

  startReplay: () => Promise<void>;
  startStream: (runId: string) => void;
  disconnect: () => void;
  play: () => void;
  pause: () => void;
  toggle: () => void;
  setSpeed: (s: number) => void;
}

let timer: number | null = null;
let stream: EventSource | null = null;

function clearTimer() {
  if (timer !== null) {
    window.clearTimeout(timer);
    timer = null;
  }
}

function closeStream() {
  if (stream) {
    stream.close();
    stream = null;
  }
}

export const useLiveRun = create<LiveStore>((set, get) => ({
  mode: "idle",
  loaded: false,
  error: null,
  events: [],
  cursor: 0,
  playing: false,
  speed: 1,
  runId: null,
  derived: EMPTY,

  // ── recorded replay (no backend) ──────────────────────────────────────
  startReplay: async () => {
    if (get().mode === "replay" && get().loaded) return;
    get().disconnect();
    try {
      const events = await api.events();
      // Open partway in, so the screen looks like a run in progress rather
      // than a set of empty panels at t=0.
      const seed = Math.min(1500, Math.floor(events.length * 0.55));
      let d = EMPTY;
      for (let i = 0; i < seed; i++) d = reduce(d, events[i]);
      set({ mode: "replay", loaded: true, events, cursor: seed, derived: d, runId: null });
      get().play();
    } catch (err) {
      set({
        mode: "replay",
        loaded: true,
        error: err instanceof Error ? err.message : String(err),
      });
    }
  },

  // ── live stream ───────────────────────────────────────────────────────
  startStream: (runId) => {
    if (get().mode === "stream" && get().runId === runId && stream) return;
    get().disconnect();
    set({ mode: "stream", runId, derived: EMPTY, loaded: true, error: null, playing: true });

    // from_byte=0 replays the log from the beginning, so a client that joins
    // an hour in still rebuilds the whole picture.
    const es = new EventSource(`${API_BASE}/api/runs/${runId}/events?from_byte=0`);
    stream = es;

    es.onmessage = (msg) => {
      if (!msg.data) return;
      try {
        const event = JSON.parse(msg.data) as LogEvent;
        set((s) => ({ derived: reduce(s.derived, event), cursor: s.cursor + 1 }));
      } catch {
        /* a partially written line; the next read picks it up whole */
      }
    };
    es.addEventListener("done", () => {
      set((s) => ({ playing: false, derived: { ...s.derived, finished: true } }));
      closeStream();
    });
    es.onerror = () => {
      // EventSource reconnects on its own; only report if it gave up.
      if (es.readyState === EventSource.CLOSED) {
        set({ playing: false, error: "the event stream closed" });
      }
    };
  },

  disconnect: () => {
    clearTimer();
    closeStream();
    set({ playing: false });
  },

  // ── transport controls (replay only) ──────────────────────────────────
  play: () => {
    if (get().mode !== "replay" || timer !== null) return;
    set({ playing: true });
    const tick = () => {
      const { cursor, events, speed, derived } = get();
      if (cursor >= events.length) {
        clearTimer();
        set({ playing: false });
        return;
      }
      set({ cursor: cursor + 1, derived: reduce(derived, events[cursor]) });
      timer = window.setTimeout(tick, 460 / speed);
    };
    timer = window.setTimeout(tick, 460 / get().speed);
  },

  pause: () => {
    clearTimer();
    set({ playing: false });
  },

  toggle: () => (get().playing ? get().pause() : get().play()),

  setSpeed: (speed) => {
    const wasPlaying = get().playing;
    set({ speed });
    if (wasPlaying && get().mode === "replay") {
      get().pause();
      get().play();
    }
  },
}));
