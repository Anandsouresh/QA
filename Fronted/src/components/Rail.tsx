import { NavLink } from "react-router-dom";
import { resolved, useTheme, type ThemeChoice } from "../store/theme";
import { Icon } from "./ui";

const ITEMS = [
  { to: "/", icon: "plus", label: "New run", end: true },
  { to: "/live", icon: "pulse", label: "Live run" },
  { to: "/graph", icon: "graph", label: "Graph explorer" },
  { to: "/cases", icon: "checks", label: "Test cases" },
  { to: "/history", icon: "clock", label: "Run history" },
];

const THEME_ICON: Record<ThemeChoice, string> = {
  dark: "moon",
  light: "sun",
  system: "monitor",
};

const THEME_LABEL: Record<ThemeChoice, string> = {
  dark: "Theme: dark. Switch to light.",
  light: "Theme: light. Follow the system instead.",
  system: "Theme: following the system. Switch to dark.",
};

export function Rail() {
  const choice = useTheme((s) => s.choice);
  const cycle = useTheme((s) => s.cycle);

  return (
    <nav
      aria-label="Main"
      className="bg-panel flex w-[72px] shrink-0 flex-col items-center gap-2 border-r border-rail-line py-[18px]"
    >
      <div className="mb-[14px] flex h-[38px] w-[38px] items-center justify-center rounded-[10px] bg-accent text-accent-deep">
        <Icon name="logo" size={21} strokeWidth={2} />
      </div>

      {ITEMS.map((item) => (
        <NavLink
          key={item.to}
          to={item.to}
          end={item.end}
          aria-label={item.label}
          title={item.label}
          className={({ isActive }) =>
            `flex h-[46px] w-[46px] items-center justify-center rounded-[11px] border transition-colors ${
              isActive
                ? "border-accent-line bg-accent-dim text-accent"
                : "border-transparent text-ink-3 hover:bg-hover hover:text-ink-2"
            }`
          }
        >
          <Icon name={item.icon} size={19} />
        </NavLink>
      ))}

      <div className="grow" />

      <button
        type="button"
        onClick={cycle}
        aria-label={THEME_LABEL[choice]}
        title={THEME_LABEL[choice]}
        className="flex h-[46px] w-[46px] items-center justify-center rounded-[11px] border border-transparent text-ink-3 transition-colors hover:bg-hover hover:text-ink-2"
      >
        <Icon name={THEME_ICON[choice]} size={19} />
      </button>
      <span className="font-mono text-[9px] tracking-[0.4px] text-ink-4 uppercase">
        {choice === "system" ? `sys·${resolved(choice)[0]}` : choice}
      </span>

      <button
        type="button"
        aria-label="Settings"
        title="Settings"
        className="mt-1 flex h-[46px] w-[46px] items-center justify-center rounded-[11px] border border-transparent text-ink-3 transition-colors hover:bg-hover hover:text-ink-2"
      >
        <Icon name="sliders" size={19} />
      </button>
    </nav>
  );
}
