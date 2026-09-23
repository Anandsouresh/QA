export function clock(seconds: number): string {
  const s = Math.max(0, Math.floor(seconds));
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  const pad = (n: number) => String(n).padStart(2, "0");
  return h > 0 ? `${h}:${pad(m)}:${pad(sec)}` : `${m}:${pad(sec)}`;
}

export function compactDuration(seconds: number): string {
  const s = Math.max(0, Math.floor(seconds));
  const h = Math.floor(s / 3600);
  const m = Math.round((s % 3600) / 60);
  if (h === 0) return `${m}m`;
  return m === 0 ? `${h}h` : `${h}h ${m}m`;
}

export function num(n: number | undefined | null): string {
  return (n ?? 0).toLocaleString("en-US");
}

export function pct(part: number, whole: number): number {
  if (!whole) return 0;
  return Math.min(100, Math.round((part / whole) * 100));
}

/** `https://stg.samsungvx.com/screen/1234` -> `/screen/1234` */
export function pathOf(url: string): string {
  try {
    const u = new URL(url);
    return (u.pathname === "/" ? "/" : u.pathname.replace(/\/$/, "")) + u.search;
  } catch {
    return url;
  }
}

export function hostOf(url: string): string {
  try {
    return new URL(url).host;
  } catch {
    return url;
  }
}

/** Element inventory lines look like
 *  `generic_button: Add Screen [[data-testid="x"]] (main area, top-centre) [app frame]` */
export function parseActionLine(line: string): {
  kind: string;
  name: string;
  selector: string;
  where: string;
  frame: boolean;
} {
  const kind = line.split(":")[0]?.trim() ?? "";
  const rest = line.slice(kind.length + 1).trim();
  const selMatch = rest.match(/\[(.+?)\]\s*(\(|$)/);
  const whereMatch = rest.match(/\(([^()]*)\)\s*(\[app frame\])?\s*(->.*)?$/);
  const name = rest.split("[")[0]?.trim() || "(unnamed)";
  return {
    kind,
    name,
    selector: selMatch ? selMatch[1] : "",
    where: whereMatch ? whereMatch[1] : "",
    frame: line.includes("[app frame]"),
  };
}

export function titleOf(state: { title: string; url: string }): string {
  const t = (state.title || "").split("|")[0].trim();
  return t || pathOf(state.url);
}
