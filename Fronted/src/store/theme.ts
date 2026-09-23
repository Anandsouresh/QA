/** Theme preference.
 *
 *  Three states, not two. "system" is the default and follows the OS; picking
 *  light or dark stamps `data-theme` on <html>, which the CSS in index.css
 *  treats as an override in both directions. Colours are CSS variables, so a
 *  switch costs one attribute write and no React re-render.
 */

import { create } from "zustand";

export type ThemeChoice = "system" | "light" | "dark";

const KEY = "qagen.theme";

function read(): ThemeChoice {
  try {
    const stored = localStorage.getItem(KEY);
    if (stored === "light" || stored === "dark" || stored === "system") return stored;
  } catch {
    // Private windows and blocked site data both throw here. A missing
    // preference is not an error; it just means "system".
  }
  return "system";
}

function write(choice: ThemeChoice): void {
  try {
    if (choice === "system") localStorage.removeItem(KEY);
    else localStorage.setItem(KEY, choice);
  } catch {
    // Nothing to do; the choice still applies for this session.
  }
}

function paint(choice: ThemeChoice): void {
  const root = document.documentElement;
  if (choice === "system") root.removeAttribute("data-theme");
  else root.setAttribute("data-theme", choice);
}

/** What the viewer actually sees right now, resolving "system". */
export function resolved(choice: ThemeChoice): "light" | "dark" {
  if (choice !== "system") return choice;
  return window.matchMedia?.("(prefers-color-scheme: light)").matches ? "light" : "dark";
}

interface ThemeStore {
  choice: ThemeChoice;
  set: (choice: ThemeChoice) => void;
  /** Cycles dark → light → system, so the toggle can reach all three. */
  cycle: () => void;
}

export const useTheme = create<ThemeStore>((set, get) => ({
  choice: read(),
  set: (choice) => {
    write(choice);
    paint(choice);
    set({ choice });
  },
  cycle: () => {
    const order: ThemeChoice[] = ["dark", "light", "system"];
    const next = order[(order.indexOf(get().choice) + 1) % order.length];
    get().set(next);
  },
}));

/** Applied before React mounts so the first paint is already correct. */
export function initTheme(): void {
  paint(read());
}
