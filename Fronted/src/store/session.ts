/** Which backend we are talking to, and which run is on screen.
 *
 *  The app works with no backend at all: if the API does not answer, every
 *  screen falls back to the recorded fixtures and says so. That keeps the demo
 *  honest rather than showing empty panels and looking broken.
 */

import { create } from "zustand";
import { control, invalidate, setSource, type RunRow, type Source } from "../lib/api";

interface SessionStore {
  checked: boolean;
  online: boolean;
  runsDir: string | null;
  runs: RunRow[];
  source: Source;
  error: string | null;
  detect: () => Promise<void>;
  refreshRuns: () => Promise<void>;
  select: (source: Source) => void;
}

const SOURCE_KEY = "qagen.source";

/** Remembered so a reload returns you to the run you were watching. */
function readSource(): Source {
  try {
    const raw = localStorage.getItem(SOURCE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw) as Source;
      if (parsed.kind === "demo" || (parsed.kind === "live" && parsed.runId)) return parsed;
    }
  } catch {
    // Blocked site data or a malformed value: fall back to the demo run.
  }
  return { kind: "demo" };
}

function writeSource(source: Source): void {
  try {
    localStorage.setItem(SOURCE_KEY, JSON.stringify(source));
  } catch {
    // The choice still holds for this session.
  }
}

const initial = readSource();
setSource(initial);

export const useSession = create<SessionStore>((set, get) => ({
  checked: false,
  online: false,
  runsDir: null,
  runs: [],
  source: initial,
  error: null,

  detect: async () => {
    try {
      const health = await control.health();
      set({ online: true, runsDir: health.runs_dir, checked: true, error: null });
      await get().refreshRuns();
      // A remembered run that has since been deleted would leave every screen
      // erroring; fall back to the bundled one instead.
      const current = get().source;
      if (current.kind === "live" && !get().runs.some((r) => r.id === current.runId)) {
        get().select({ kind: "demo" });
      }
    } catch (err) {
      set({
        online: false,
        checked: true,
        error: err instanceof Error ? err.message : String(err),
      });
    }
  },

  refreshRuns: async () => {
    if (!get().online) return;
    try {
      set({ runs: await control.runs() });
    } catch (err) {
      set({ error: err instanceof Error ? err.message : String(err) });
    }
  },

  select: (next) => {
    setSource(next);
    writeSource(next);
    invalidate();
    set({ source: next });
  },
}));

/** True while a selected live run is still producing output. */
export function isRunning(row: RunRow | undefined): boolean {
  return !!row && ["running", "starting", "paused", "stopping"].includes(row.status);
}
