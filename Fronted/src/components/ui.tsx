import type { CSSProperties, ReactNode } from "react";
import { TONE_HEX, wash, type Tone } from "../lib/tokens";

/* ── icons ──────────────────────────────────────────────────────────────── */

const PATHS: Record<string, ReactNode> = {
  plus: (
    <>
      <path d="M12 5v14" />
      <path d="M5 12h14" />
    </>
  ),
  minus: <path d="M6 12h12" />,
  pulse: <path d="M3 12h4l3 8 4-16 3 8h4" />,
  graph: (
    <>
      <circle cx="5.5" cy="6" r="2.4" />
      <circle cx="18.5" cy="12" r="2.4" />
      <circle cx="5.5" cy="18" r="2.4" />
      <path d="M7.6 7.2 16.4 10.8" />
      <path d="M16.4 13.2 7.6 16.8" />
    </>
  ),
  checks: (
    <>
      <path d="M4 6.5 6 8.5 9.5 5" />
      <path d="M4 17.5 6 19.5 9.5 16" />
      <path d="M13 7h7" />
      <path d="M13 18h7" />
    </>
  ),
  clock: (
    <>
      <circle cx="12" cy="12" r="8.2" />
      <path d="M12 7.6V12l3 1.8" />
    </>
  ),
  gear: (
    <>
      <circle cx="12" cy="12" r="3" />
      <path d="M12 3v2.2M12 18.8V21M21 12h-2.2M5.2 12H3M18.4 5.6 16.8 7.2M7.2 16.8 5.6 18.4M18.4 18.4 16.8 16.8M7.2 7.2 5.6 5.6" />
    </>
  ),
  check: <path d="M20 6 9 17l-5-5" />,
  x: (
    <>
      <path d="M6.5 6.5 17.5 17.5" />
      <path d="M17.5 6.5 6.5 17.5" />
    </>
  ),
  shield: (
    <>
      <path d="M12 3 4.6 6.1v5.5c0 4.4 3 8.2 7.4 9.4 4.4-1.2 7.4-5 7.4-9.4V6.1z" />
      <path d="M9.2 12.2 11.3 14.3 15 10.6" />
    </>
  ),
  download: (
    <>
      <path d="M12 3.5v11" />
      <path d="M7.5 10 12 14.5 16.5 10" />
      <path d="M4.5 19.5h15" />
    </>
  ),
  search: (
    <>
      <circle cx="11" cy="11" r="6.5" />
      <path d="M16 16 20.5 20.5" />
    </>
  ),
  filter: (
    <>
      <path d="M4 6h16" />
      <path d="M7 12h10" />
      <path d="M10 18h4" />
    </>
  ),
  warn: (
    <>
      <path d="M12 8v5" />
      <path d="M12 16.4v.2" />
      <path d="M10.3 4.2 2.9 17.4A1.9 1.9 0 0 0 4.6 20.3h14.8a1.9 1.9 0 0 0 1.7-2.9L13.7 4.2a1.9 1.9 0 0 0-3.4 0z" />
    </>
  ),
  left: <path d="M14.5 5.5 8 12l6.5 6.5" />,
  right: <path d="M9.5 5.5 16 12l-6.5 6.5" />,
  ext: (
    <>
      <path d="M14 4h6v6" />
      <path d="M20 4 11 13" />
      <path d="M18 14v5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 4 19V8a1.5 1.5 0 0 1 1.5-1.5H10" />
    </>
  ),
  logo: (
    <>
      <circle cx="6" cy="6" r="2.6" />
      <circle cx="18" cy="6" r="2.6" />
      <circle cx="12" cy="18" r="2.6" />
      <path d="M8.2 7.4 10.6 15.6" />
      <path d="M15.8 7.4 13.4 15.6" />
    </>
  ),
  refresh: (
    <>
      <path d="M20 11a8 8 0 1 0-.6 4" />
      <path d="M20 4.5V11h-6.2" />
    </>
  ),
  sliders: (
    <>
      <path d="M4 8h8.2" />
      <path d="M17 8h3" />
      <circle cx="14.6" cy="8" r="2.4" />
      <path d="M4 16h2.4" />
      <path d="M11.2 16h8.8" />
      <circle cx="8.8" cy="16" r="2.4" />
    </>
  ),
  sun: (
    <>
      <circle cx="12" cy="12" r="4.1" />
      <path d="M12 2.8v2.1M12 19.1v2.1M21.2 12h-2.1M4.9 12H2.8M18.5 5.5l-1.5 1.5M7 17l-1.5 1.5M18.5 18.5 17 17M7 7 5.5 5.5" />
    </>
  ),
  moon: <path d="M20 13.4A8.2 8.2 0 0 1 10.6 4a8.2 8.2 0 1 0 9.4 9.4z" />,
  monitor: (
    <>
      <rect x="3" y="4.5" width="18" height="12" rx="2" />
      <path d="M9 20h6" />
      <path d="M12 16.5V20" />
    </>
  ),
  upload: (
    <>
      <path d="M12 16.5v-11" />
      <path d="M7.5 10 12 5.5 16.5 10" />
      <path d="M4.5 19.5h15" />
    </>
  ),
  key: (
    <>
      <circle cx="8" cy="12" r="3.6" />
      <path d="M11.6 12H20" />
      <path d="M17 12v3.2" />
      <path d="M20 12v2.4" />
    </>
  ),
  play: <path d="M8 5.5 18.5 12 8 18.5z" />,
  link: (
    <>
      <path d="M10 13.5a3.5 3.5 0 0 0 5 0l3-3a3.5 3.5 0 0 0-5-5l-1.2 1.2" />
      <path d="M14 10.5a3.5 3.5 0 0 0-5 0l-3 3a3.5 3.5 0 0 0 5 5l1.2-1.2" />
    </>
  ),
  trash: (
    <>
      <path d="M4.5 6.5h15" />
      <path d="M9 6.5V4.8h6v1.7" />
      <path d="M6.5 6.5 7.4 19a1.4 1.4 0 0 0 1.4 1.3h6.4A1.4 1.4 0 0 0 16.6 19l.9-12.5" />
    </>
  ),
};

export function Icon({
  name,
  size = 18,
  color = "currentColor",
  strokeWidth = 1.8,
}: {
  name: keyof typeof PATHS | string;
  size?: number;
  color?: string;
  strokeWidth?: number;
}) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      style={{ stroke: color, strokeWidth }}
    >
      {PATHS[name] ?? PATHS.plus}
    </svg>
  );
}

export function PlayGlyph({ size = 16, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" aria-hidden="true" style={{ fill: color }}>
      <path d="M8 5.5 18.5 12 8 18.5z" />
    </svg>
  );
}

export function PauseGlyph({ size = 15, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" aria-hidden="true" style={{ fill: color }}>
      <rect x="7" y="5" width="3.6" height="14" rx="1" />
      <rect x="13.4" y="5" width="3.6" height="14" rx="1" />
    </svg>
  );
}

export function StopGlyph({ size = 15, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" aria-hidden="true" style={{ fill: color }}>
      <rect x="6" y="6" width="12" height="12" rx="2" />
    </svg>
  );
}

/* ── surfaces ───────────────────────────────────────────────────────────── */

export function Card({
  children,
  className = "",
  style,
  accent = false,
}: {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
  accent?: boolean;
}) {
  return (
    <div
      className={`bg-surface rounded-[13px] border ${
        accent ? "border-accent-line" : "border-line"
      } ${className}`}
      style={style}
    >
      {children}
    </div>
  );
}

export function PanelTitle({
  children,
  right,
  step,
}: {
  children: ReactNode;
  right?: ReactNode;
  step?: string;
}) {
  return (
    <div className="flex items-center gap-[9px]">
      {step && <span className="font-mono text-[11px] text-accent">{step}</span>}
      <h2 className="font-display text-[13.5px] font-semibold tracking-[0.3px] text-ink">
        {children}
      </h2>
      {right && (
        <>
          <div className="grow" />
          {right}
        </>
      )}
    </div>
  );
}

export function Chip({
  children,
  tone = "muted",
  active = false,
  onClick,
  title,
}: {
  children: ReactNode;
  tone?: Tone;
  active?: boolean;
  onClick?: () => void;
  title?: string;
}) {
  const hex = TONE_HEX[tone];
  const style: CSSProperties = active
    ? { background: wash(tone, 0.16), color: hex, borderColor: wash(tone, 0.4) }
    : { background: "var(--qg-surface)", color: "var(--qg-ink-body)", borderColor: "var(--qg-line-strong)" };
  const Tag = onClick ? "button" : "span";
  return (
    <Tag
      type={onClick ? "button" : undefined}
      onClick={onClick}
      title={title}
      style={style}
      className="inline-flex h-9 items-center gap-[7px] rounded-lg border px-3 text-[12px] font-medium whitespace-nowrap"
    >
      {children}
    </Tag>
  );
}

export function Tag({ children, tone = "muted" }: { children: ReactNode; tone?: Tone }) {
  return (
    <span
      style={{ background: wash(tone, 0.14), color: TONE_HEX[tone] }}
      className="inline-block rounded-md px-[7px] py-[2px] font-mono text-[10.5px] leading-[1.5] font-medium whitespace-nowrap"
    >
      {children}
    </span>
  );
}

export function Dot({ tone = "muted", size = 7, pulse = false }: { tone?: Tone; size?: number; pulse?: boolean }) {
  return (
    <span
      className={`block shrink-0 rounded-full ${pulse ? "qg-pulse" : ""}`}
      style={{ width: size, height: size, background: TONE_HEX[tone] }}
    />
  );
}

export function Meter({
  label,
  value,
  cap,
  percent,
  tone = "accent",
}: {
  label: string;
  value: string;
  cap?: string;
  percent: number;
  tone?: Tone;
}) {
  return (
    <div>
      <div className="mb-[6px] flex items-baseline justify-between gap-2">
        <span className="text-[11px] text-ink-3">{label}</span>
        {cap && <span className="font-mono text-[11px] text-ink-4">{cap}</span>}
      </div>
      <div
        className="font-display mb-[7px] text-[20px] leading-none font-semibold tabular-nums"
        style={{ color: TONE_HEX[tone] }}
      >
        {value}
      </div>
      <Bar percent={percent} tone={tone} />
    </div>
  );
}

export function Bar({ percent, tone = "accent", height = 5 }: { percent: number; tone?: Tone; height?: number }) {
  return (
    <div className="overflow-hidden rounded-full bg-track" style={{ height }}>
      <div
        className="h-full rounded-full transition-[width] duration-500 ease-out"
        style={{ width: `${Math.max(0, Math.min(100, percent))}%`, background: TONE_HEX[tone] }}
      />
    </div>
  );
}

export function Field({
  label,
  children,
  hint,
}: {
  label: string;
  children: ReactNode;
  hint?: string;
}) {
  return (
    <label className="block min-w-0">
      <span className="mb-[6px] block text-[11.5px] font-medium tracking-[0.2px] text-ink-3">
        {label}
      </span>
      {children}
      {hint && <span className="mt-[5px] block text-[11px] text-ink-4">{hint}</span>}
    </label>
  );
}

export function TextInput(props: React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      {...props}
      className={`bg-sunken h-11 w-full rounded-[9px] border border-line-strong-2 px-[13px] font-mono text-[13px] text-ink outline-none focus:border-accent-line focus:ring-1 focus:ring-accent/40 ${
        props.className ?? ""
      }`}
    />
  );
}

export function Button({
  children,
  variant = "ghost",
  size = "md",
  ...rest
}: {
  children: ReactNode;
  variant?: "primary" | "ghost" | "danger" | "accent-soft";
  size?: "sm" | "md" | "lg";
} & React.ButtonHTMLAttributes<HTMLButtonElement>) {
  const sizes = {
    sm: "h-[30px] px-3 text-[12px] rounded-[7px]",
    md: "h-11 px-4 text-[13px] rounded-[9px]",
    lg: "h-12 px-5 text-[14.5px] rounded-[10px]",
  }[size];
  const variants = {
    primary: "bg-accent text-accent-deep font-semibold border border-transparent hover:brightness-110",
    ghost: "bg-ghost text-ink-body border border-line-strong hover:border-line-hover",
    danger: "bg-red-dim text-red-ink border border-red-line hover:border-red-line-2",
    "accent-soft": "bg-accent-dim text-accent border border-accent-line hover:brightness-125",
  }[variant];
  return (
    <button
      type="button"
      {...rest}
      className={`inline-flex shrink-0 items-center justify-center gap-[7px] font-medium transition-colors ${sizes} ${variants} ${
        rest.className ?? ""
      }`}
    >
      {children}
    </button>
  );
}

export function IconButton({
  icon,
  label,
  tone = "muted",
  onClick,
  size = 40,
}: {
  icon: string;
  label: string;
  tone?: Tone;
  onClick?: () => void;
  size?: number;
}) {
  return (
    <button
      type="button"
      aria-label={label}
      title={label}
      onClick={onClick}
      style={{ width: size, height: size, color: TONE_HEX[tone] }}
      className="flex shrink-0 items-center justify-center rounded-[9px] border border-line-strong bg-surface transition-colors hover:border-line-hover"
    >
      <Icon name={icon} size={Math.round(size * 0.38)} />
    </button>
  );
}

export function TextArea(props: React.TextareaHTMLAttributes<HTMLTextAreaElement>) {
  return (
    <textarea
      {...props}
      className={`bg-sunken w-full resize-y rounded-[9px] border border-line-strong-2 p-3 font-mono text-[11.5px] leading-[1.6] text-ink outline-none focus:border-accent-line ${
        props.className ?? ""
      }`}
    />
  );
}

export function Toggle({
  checked,
  onChange,
  label,
  hint,
}: {
  checked: boolean;
  onChange: (next: boolean) => void;
  label: string;
  hint?: string;
}) {
  return (
    <label className="flex cursor-pointer items-start gap-3">
      <button
        type="button"
        role="switch"
        aria-checked={checked}
        aria-label={label}
        onClick={() => onChange(!checked)}
        className="mt-[2px] flex h-[22px] w-[38px] shrink-0 items-center rounded-full border px-[2px] transition-colors"
        style={{
          background: checked ? wash("accent", 0.28) : "var(--qg-track)",
          borderColor: checked ? TONE_HEX.accent : "var(--qg-line-strong)",
        }}
      >
        <span
          className="block h-[16px] w-[16px] rounded-full transition-transform"
          style={{
            background: checked ? TONE_HEX.accent : "var(--qg-ink-4)",
            transform: `translateX(${checked ? 16 : 0}px)`,
          }}
        />
      </button>
      <span className="min-w-0">
        <span className="block text-[12.5px] font-medium text-ink">{label}</span>
        {hint && <span className="mt-[2px] block text-[11.5px] leading-[1.45] text-ink-4">{hint}</span>}
      </span>
    </label>
  );
}

export function Banner({
  tone = "amber",
  title,
  children,
  action,
}: {
  tone?: Tone;
  title: string;
  children?: ReactNode;
  action?: ReactNode;
}) {
  return (
    <div
      className="flex items-start gap-3 rounded-[10px] border px-4 py-3"
      style={{ background: wash(tone, 0.08), borderColor: wash(tone, 0.3) }}
    >
      <span className="mt-[5px]">
        <Dot tone={tone} />
      </span>
      <div className="min-w-0 grow">
        <div className="text-[12.5px] font-semibold" style={{ color: TONE_HEX[tone] }}>
          {title}
        </div>
        {children && (
          <div className="mt-[3px] text-[12px] leading-[1.5] text-ink-2">{children}</div>
        )}
      </div>
      {action}
    </div>
  );
}

export function Empty({ children }: { children: ReactNode }) {
  return (
    <div className="flex h-full items-center justify-center p-8 text-center text-[12.5px] leading-relaxed text-ink-4">
      {children}
    </div>
  );
}

export function Scroll({ children, className = "" }: { children: ReactNode; className?: string }) {
  return <div className={`min-h-0 grow overflow-y-auto ${className}`}>{children}</div>;
}
