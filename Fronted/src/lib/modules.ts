/** Module identity.
 *
 *  A module is the first path segment, which is the same grouping the crawler
 *  already uses internally for per-section budgets (Crawler._section_of) and
 *  that qagen/discover.py reports. Keeping the rule in one place means the
 *  config screen, the graph and the case list all agree on what "Settings" is.
 */

const LABEL: Record<string, string> = {
  screen: "Screen",
  content: "Content",
  playlist: "Playlist",
  schedule: "Schedule",
  channel: "Channel",
  settings: "Settings",
  apps: "Apps",
  vxtlabs: "VXT Labs",
};

export function moduleOf(url: string): string {
  try {
    const seg = new URL(url).pathname.split("/").filter(Boolean)[0];
    if (!seg) return "Home";
    return LABEL[seg.toLowerCase()] ?? titleCase(seg);
  } catch {
    return "Other";
  }
}

export function titleCase(slug: string): string {
  if (slug === "(home)") return "Home";
  return slug.charAt(0).toUpperCase() + slug.slice(1).replace(/[-_]/g, " ");
}
