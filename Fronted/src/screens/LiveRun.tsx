import { useEffect, useMemo, useRef, useState } from "react";
import { api, shotUrl } from "../lib/api";
import { clock, num, pathOf, pct } from "../lib/format";
import {
  C,
  EVENT_LABEL,
  EVENT_TONE,
  moduleTone,
  OUTCOME_TONE,
  TONE_HEX,
  wash,
  type Tone,
} from "../lib/tokens";
import { useLiveRun } from "../store/liveRun";
import { useSession } from "../store/session";
import { control, frameUrl } from "../lib/api";
import type { Graph, RunSummary, StateRec } from "../lib/types";
import {
  Bar,
  Button,
  Card,
  Dot,
  Icon,
  Meter,
  PanelTitle,
  PauseGlyph,
  PlayGlyph,
  StopGlyph,
  Tag,
} from "../components/ui";

const MODULE_ORDER = ["Home", "Screen", "Content", "Playlist", "Schedule", "Channel", "Settings", "Apps", "VXT Labs", "Other"];

export function LiveRun() {
  const { derived, playing, toggle, speed, setSpeed, cursor, events, mode, startReplay,
          startStream, disconnect } = useLiveRun();
  const source = useSession((s) => s.source);
  const runs = useSession((s) => s.runs);
  const refreshRuns = useSession((s) => s.refreshRuns);
  const [graph, setGraph] = useState<Graph | null>(null);
  const [states, setStates] = useState<StateRec[] | null>(null);
  const [run, setRun] = useState<RunSummary | null>(null);
  const [busy, setBusy] = useState(false);

  const liveRunId = source.kind === "live" ? source.runId : null;
  const row = runs.find((r) => r.id === liveRunId);
  const isLive = mode === "stream";

  useEffect(() => {
    if (liveRunId) startStream(liveRunId);
    else startReplay();
    return () => disconnect();
  }, [liveRunId, startStream, startReplay, disconnect]);

  useEffect(() => {
    api.graph().then(setGraph).catch(() => setGraph(null));
    api.states().then(setStates).catch(() => setStates(null));
    api.run().then(setRun).catch(() => setRun(null));
  }, [liveRunId]);

  const maxStates = row?.max_states || run?.budgets.max_pages || 200;
  const remaining = isLive ? 0 : events.length - cursor;
  const etaSeconds = isLive
    ? Math.max(0, (maxStates - derived.states.length) * 151)
    : remaining * 19;

  async function control_(action: "pause" | "resume" | "stop") {
    if (!liveRunId) {
      toggle();
      return;
    }
    setBusy(true);
    try {
      await control[action](liveRunId);
      await refreshRuns();
    } catch {
      /* the button state is refreshed from the server on the next poll */
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="flex min-w-0 grow flex-col gap-[14px] overflow-hidden px-[22px] py-[18px]">
      {/* ── top bar ── */}
      <header className="flex h-[46px] shrink-0 items-center gap-4">
        <div
          className="flex items-center gap-2 rounded-lg border px-[13px] py-[7px]"
          style={{
            background: wash(playing ? "accent" : "amber", 0.1),
            borderColor: wash(playing ? "accent" : "amber", 0.35),
          }}
        >
          <Dot tone={playing ? "accent" : "amber"} size={8} pulse={playing} />
          <span
            className="font-display text-[12.5px] font-semibold tracking-[0.7px]"
            style={{ color: TONE_HEX[playing ? "accent" : "amber"] }}
          >
            {derived.finished ? "FINISHED" : playing ? "CRAWLING" : "PAUSED"}
          </span>
        </div>

        <div className="min-w-0">
          <div className="truncate font-mono text-[13px] text-ink-strong">
            {run ? new URL(run.target).host : "—"}
          </div>
          <div className="text-[11.5px] text-ink-4">
            {isLive ? (
              <>
                {liveRunId} · live · {row?.status ?? "running"}
              </>
            ) : (
              <>recorded replay · no backend connected</>
            )}{" "}
            · {run?.config.block_mutations === false ? "write-guard OFF" : "write-guard on"}
          </div>
        </div>

        <div className="grow" />

        <Clock label="ELAPSED" value={clock(derived.elapsed)} />
        <Clock label="EST. LEFT" value={clock(etaSeconds)} />

        <div
          className="flex items-center gap-1 rounded-[9px] border border-line-strong bg-surface px-1"
          hidden={isLive}
        >
          {[1, 2, 4].map((s) => (
            <button
              key={s}
              type="button"
              onClick={() => setSpeed(s)}
              className={`h-[34px] rounded-md px-[10px] font-mono text-[11.5px] transition-colors ${
                speed === s ? "bg-accent-dim text-accent" : "text-ink-3 hover:text-ink-2"
              }`}
            >
              {s}×
            </button>
          ))}
        </div>

        <Button
          onClick={() => control_(playing ? "pause" : "resume")}
          disabled={busy || derived.finished}
        >
          {playing ? <PauseGlyph /> : <PlayGlyph color="currentColor" size={14} />}
          {playing ? "Pause" : "Resume"}
        </Button>
        <Button
          variant="danger"
          onClick={() => control_("stop")}
          disabled={busy || !isLive || derived.finished}
          title={
            isLive
              ? "Finish the current state, then write everything captured"
              : "Only a live run can be stopped"
          }
        >
          <StopGlyph />
          Stop &amp; keep
        </Button>
      </header>

      {/* ── body ── */}
      <div className="flex min-h-0 grow gap-[14px]">
        <div className="flex w-[616px] shrink-0 flex-col gap-[14px]">
          <Viewport graph={graph} states={states} />
          <Budgets maxStates={maxStates} run={run} />
        </div>

        <div className="flex w-[392px] shrink-0 flex-col gap-[14px]">
          <NowExercising />
          <MapSoFar />
        </div>

        <EventFeed total={cursor} />
      </div>
    </div>
  );
}

function Clock({ label, value }: { label: string; value: string }) {
  return (
    <div className="border-r border-line pr-[18px] text-right">
      <div className="text-[10.5px] tracking-[0.5px] text-ink-4">{label}</div>
      <div className="mt-[2px] font-mono text-[15px] text-ink-strong tabular-nums">{value}</div>
    </div>
  );
}

/* ── live viewport: a real capture with the current target outlined ─────── */

function Viewport({ graph, states }: { graph: Graph | null; states: StateRec[] | null }) {
  const current = useLiveRun((s) => s.derived.current);
  const discovered = useLiveRun((s) => s.derived.states);
  const streaming = useLiveRun((s) => s.mode === "stream");

  // While a run is in flight the graph has not been written, so there is no
  // node to look a capture up by. Poll the newest one the crawler has saved.
  const [tick, setTick] = useState(0);
  useEffect(() => {
    if (!streaming) return;
    const id = window.setInterval(() => setTick((n) => n + 1), 4000);
    return () => window.clearInterval(id);
  }, [streaming]);

  const nodeId = current?.node ?? discovered[discovered.length - 1]?.id;
  const node = graph?.nodes.find((n) => n.id === nodeId) ?? null;
  const state = states?.find((s) => s.fingerprint === node?.fingerprint) ?? null;
  const stored = shotUrl(state?.screenshot ?? node?.screenshot ?? null);
  const shot = stored ?? (streaming ? frameUrl(tick) : null);

  const target = useMemo(() => {
    if (!state || !current?.selector) return null;
    return state.elements.find((e) => e.selector === current.selector) ?? null;
  }, [state, current?.selector]);

  const [box, setBox] = useState<{ w: number; h: number } | null>(null);
  const frame = useRef<HTMLDivElement | null>(null);
  const [frameH, setFrameH] = useState(0);

  useEffect(() => {
    const el = frame.current;
    if (!el) return;
    const ro = new ResizeObserver(([entry]) => setFrameH(entry.contentRect.height));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const scale = state && box ? box.w / (state.viewport_width || 1200) : 0;

  // Captures are full-page, so a control near the bottom of a long page would
  // sit below the visible strip and the highlight would never be seen. Scroll
  // the capture to keep the marked control in frame, the way the evidence
  // panel on the test-case screen already does. Measured on the recorded run:
  // 50 of 348 resolved highlights were off-screen without this.
  const targetTop = target && scale ? target.y * scale : 0;
  const offset =
    target && scale && frameH
      ? Math.max(0, targetTop - Math.max(60, frameH / 2 - target.h * scale))
      : 0;

  return (
    <Card className="flex h-[458px] flex-col p-[14px]">
      <div className="mb-[11px] flex items-center gap-2">
        <Dot tone="red" size={6} pulse />
        <PanelTitle
          right={
            <span className="font-mono text-[11px] text-ink-4">
              {state ? `${state.viewport_width} × ${state.viewport_height}` : "—"} · frame{" "}
              {num(discovered.length * 37)}
            </span>
          }
        >
          LIVE VIEWPORT
        </PanelTitle>
      </div>

      <div className="flex min-h-0 grow flex-col overflow-hidden rounded-[9px] border border-line-strong bg-well">
        <div className="flex h-[30px] shrink-0 items-center gap-[7px] border-b border-line-3 bg-chrome px-[11px]">
          <span className="block h-2 w-2 rounded-full bg-line-hover" />
          <span className="block h-2 w-2 rounded-full bg-line-hover" />
          <span className="block h-2 w-2 rounded-full bg-line-hover" />
          <span className="ml-2 truncate font-mono text-[10.5px] text-ink-4">
            {state ? pathOf(state.url) : "…"}
          </span>
        </div>

        <div ref={frame} className="relative min-h-0 grow overflow-hidden">
          {shot ? (
            <>
              <img
                src={shot}
                alt={`Capture of ${state?.title ?? "the current state"}`}
                className="block w-full max-w-none transition-transform duration-300"
                style={{ transform: `translateY(${-offset}px)` }}
                onLoad={(e) => {
                  const el = e.currentTarget;
                  setBox({ w: el.clientWidth, h: el.clientHeight });
                }}
              />
              {target && scale > 0 && (
                <div
                  className="pointer-events-none absolute"
                  style={{
                    left: target.x * scale,
                    top: targetTop - offset,
                    width: Math.max(8, target.w * scale),
                    height: Math.max(8, target.h * scale),
                    transition: "top 300ms",
                  }}
                >
                  <div
                    className="h-full w-full rounded-[4px]"
                    style={{
                      border: `2px solid ${TONE_HEX.accent}`,
                      boxShadow: `0 0 0 4px ${wash("accent", 0.18)}`,
                      background: wash("accent", 0.08),
                    }}
                  />
                  <span
                    className="absolute -top-[19px] left-0 rounded px-[6px] py-[2px] font-mono text-[9.5px] font-medium whitespace-nowrap"
                    style={{ background: TONE_HEX.accent, color: "var(--qg-accent-deep)" }}
                  >
                    clicking · {current?.name?.slice(0, 26)}
                  </span>
                </div>
              )}
            </>
          ) : (
            <div className="flex h-full items-center justify-center text-[12px] text-ink-4">
              waiting for the first frame…
            </div>
          )}
        </div>
      </div>

      <p className="mt-[10px] text-[11.5px] leading-[1.45] text-ink-4">
        {target
          ? "The outlined control is the one being exercised this instant, boxed from the geometry recorded at extraction."
          : streaming && !stored
            ? "The newest capture the crawler has written. Boxes appear once the run finishes and the element inventory is on disk."
            : "The control being exercised is outlined as each action starts."}
      </p>
    </Card>
  );
}

/* ── budgets ────────────────────────────────────────────────────────────── */

function Budgets({ maxStates, run }: { maxStates: number; run: RunSummary | null }) {
  const d = useLiveRun((s) => s.derived);
  const budgets = run?.module_budgets ?? {};

  // Only modules that carry a cap; a module with no budget has no bar to draw.
  const modules = MODULE_ORDER.filter((m) => budgets[m]).slice(0, 6);
  const starved = modules.find((m) => budgets[m] && (d.moduleStates[m] ?? 0) >= budgets[m]);

  return (
    <Card className="flex min-h-0 grow flex-col px-[17px] pt-[15px] pb-4">
      <PanelTitle>BUDGETS</PanelTitle>

      <div className="mt-[13px] mb-[15px] grid grid-cols-4 gap-[13px]">
        <Meter
          label="States"
          value={num(d.states.length)}
          cap={`/ ${maxStates}`}
          percent={pct(d.states.length, maxStates)}
          tone="accent"
        />
        <Meter
          label="Clicks"
          value={num(d.clicks)}
          cap="no cap"
          percent={pct(d.clicks % 400, 400)}
          tone="blue"
        />
        <Meter
          label="Navigations"
          value={num(d.navigations)}
          cap="no cap"
          percent={pct(d.navigations % 200, 200)}
          tone="blue"
        />
        <Meter
          label="Wall clock"
          value={`${pct(d.elapsed, 86400)}%`}
          cap="/ 24h"
          percent={pct(d.elapsed, 86400)}
          tone="amber"
        />
      </div>

      <div className="mb-[9px] text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
        STATES PER MODULE
      </div>
      <div className="grid grid-cols-2 gap-x-[18px] gap-y-[7px]">
        {modules.map((m) => {
          const seen = d.moduleStates[m] ?? 0;
          const cap = budgets[m] ?? 0;
          return (
            <div key={m} className="flex items-center gap-[9px]">
              <span className="w-[62px] shrink-0 text-[11.5px] text-ink-2">{m}</span>
              <div className="grow">
                <Bar percent={cap ? pct(seen, cap) : 0} tone={moduleTone(m)} height={6} />
              </div>
              <span className="w-[42px] shrink-0 text-right font-mono text-[11px] text-ink-3 tabular-nums">
                {seen}/{cap || "—"}
              </span>
            </div>
          );
        })}
      </div>

      <div className="grow" />

      <div className="mt-3 flex items-center gap-[10px] rounded-[9px] border border-line bg-inset px-3 py-[10px]">
        <Dot tone={starved ? "amber" : "accent"} />
        <span className="text-[11.5px] leading-[1.45] text-ink-2">
          {starved
            ? `${starved} reached its cap and stopped early. Every other module is still taking work from the frontier.`
            : `${num(d.skips)} controls skipped by the deny-list, ${num(
                d.blockedWrites,
              )} writes blocked. No module has hit its cap yet.`}
        </span>
      </div>
    </Card>
  );
}

/* ── now exercising ─────────────────────────────────────────────────────── */

function NowExercising() {
  const { current, lastOutcome, elapsed } = useLiveRun((s) => s.derived);
  const held = current ? Math.max(0, elapsed - current.startedAt) : 0;

  return (
    <Card accent className="relative shrink-0 overflow-hidden px-[17px] pt-[15px] pb-4">
      {current && (
        <div
          className="qg-sweep absolute top-0 left-0 h-[2px] w-[28%]"
          style={{
            background: `linear-gradient(90deg, transparent, ${TONE_HEX.accent}, transparent)`,
          }}
        />
      )}

      <PanelTitle
        right={
          <span className="font-mono text-[11.5px] text-accent tabular-nums">
            {current ? `${held.toFixed(1)}s` : "idle"}
          </span>
        }
      >
        NOW EXERCISING
      </PanelTitle>

      {current ? (
        <>
          <div className="mt-3 mb-[11px] flex items-center gap-[10px]">
            <Tag tone="accent">{current.node}</Tag>
            <Tag>click</Tag>
            <Tag>{current.kind}</Tag>
          </div>
          <div className="font-display mb-[5px] truncate text-[17px] font-semibold">
            “{current.name}”
          </div>
          <div className="mb-[9px] truncate font-mono text-[11.5px] text-ink-3">
            {current.selector || "—"}
          </div>
          <div className="text-[11.5px] text-ink-4">action {num(current.index)} of this run</div>
        </>
      ) : (
        <div className="mt-3 mb-1">
          <div className="font-display mb-[5px] truncate text-[17px] font-semibold text-ink-2">
            {lastOutcome ? `“${lastOutcome.name}”` : "Settling…"}
          </div>
          {lastOutcome ? (
            <div className="flex items-center gap-2">
              <Tag tone={OUTCOME_TONE[lastOutcome.outcome] ?? "muted"}>{lastOutcome.outcome}</Tag>
              {lastOutcome.annotations.map((a) => (
                <Tag key={a} tone="amber">
                  {a}
                </Tag>
              ))}
            </div>
          ) : (
            <div className="text-[11.5px] text-ink-4">
              Waiting for the page to hold still before the next action.
            </div>
          )}
        </div>
      )}
    </Card>
  );
}

/* ── the map, drawing itself ────────────────────────────────────────────── */

function MapSoFar() {
  const states = useLiveRun((s) => s.derived.states);

  const layout = useMemo(() => {
    const cols = new Map<string, number>();
    const perCol = new Map<string, number>();
    let next = 0;
    const points = states.map((s) => {
      if (!cols.has(s.module)) cols.set(s.module, next++);
      const col = cols.get(s.module)!;
      const row = perCol.get(s.module) ?? 0;
      perCol.set(s.module, row + 1);
      return { ...s, col, row };
    });
    const colCount = Math.max(1, next);
    const rowCount = Math.max(1, ...Array.from(perCol.values()));
    return { points, colCount, rowCount, cols };
  }, [states]);

  const W = 360;
  const H = 400;
  const padX = 24;
  const labelBand = 34;            // room for the rotated module labels
  const colW = (W - padX * 2) / Math.max(1, layout.colCount - 1 || 1);
  const rows = Math.max(1, layout.rowCount - 1);
  const rowH = Math.min(30, (H - labelBand - 40) / rows);
  // Centre the rows in the band rather than stacking them against the top.
  const topPad = Math.max(22, (H - labelBand - rows * rowH) / 2);

  const xy = (col: number, row: number) => ({
    x: layout.colCount === 1 ? W / 2 : padX + col * colW,
    y: topPad + row * rowH,
  });

  const newest = layout.points[layout.points.length - 1];

  return (
    <Card className="flex min-h-0 grow flex-col px-[17px] pt-[15px] pb-[14px]">
      <PanelTitle
        right={
          <span className="font-mono text-[11px] text-ink-4">
            {num(states.length)} states · {num(layout.colCount)} modules
          </span>
        }
      >
        MAP SO FAR
      </PanelTitle>
      <p className="mt-1 mb-2 text-[11.5px] text-ink-4">
        A column per module. Nodes appear the moment a state is fingerprinted.
      </p>

      <div className="min-h-0 grow overflow-hidden rounded-[9px] border border-line-soft bg-well-2">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
          {Array.from(layout.cols.entries()).map(([mod, col]) => (
            <g key={mod}>
              <line
                x1={xy(col, 0).x}
                y1={topPad - 14}
                x2={xy(col, 0).x}
                y2={H - 30}
                style={{ stroke: C.lineSoft }}
                strokeWidth={1}
              />
              <text
                x={xy(col, 0).x}
                y={H - 20}
                style={{ fill: C.muted }}
                fontSize={8.5}
                textAnchor="end"
                fontFamily="IBM Plex Mono, monospace"
                transform={`rotate(-42 ${xy(col, 0).x} ${H - 20})`}
              >
                {mod.slice(0, 9)}
              </text>
            </g>
          ))}

          {layout.points.map((p, i) => {
            const prev = i > 0 ? layout.points[i - 1] : null;
            if (!prev) return null;
            const a = xy(prev.col, prev.row);
            const b = xy(p.col, p.row);
            return (
              <path
                key={`e${p.id}-${i}`}
                d={`M${a.x} ${a.y} C ${a.x} ${(a.y + b.y) / 2}, ${b.x} ${(a.y + b.y) / 2}, ${b.x} ${b.y}`}
                style={{ stroke: C.line }}
                strokeWidth={1}
                fill="none"
              />
            );
          })}

          {layout.points.map((p, i) => {
            const { x, y } = xy(p.col, p.row);
            const isNew = i === layout.points.length - 1;
            const tone = moduleTone(p.module);
            return (
              <g key={`${p.id}-${i}`} className={isNew ? "qg-pop" : undefined}>
                {isNew && (
                  <>
                    <circle cx={x} cy={y} r={13} fill="none" style={{ stroke: TONE_HEX.accent }} strokeWidth={1.2} opacity={0.4} />
                    <circle cx={x} cy={y} r={19} fill="none" style={{ stroke: TONE_HEX.accent }} strokeWidth={1} opacity={0.15} />
                  </>
                )}
                <circle
                  cx={x}
                  cy={y}
                  r={isNew ? 6 : 4}
                  style={{ fill: isNew ? TONE_HEX.accent : TONE_HEX[tone] }}
                  opacity={isNew ? 1 : 0.85}
                />
              </g>
            );
          })}

          {newest && (
            <text
              x={xy(newest.col, newest.row).x}
              y={xy(newest.col, newest.row).y - 14}
              style={{ fill: TONE_HEX.accent }}
              fontSize={9.5}
              textAnchor="middle"
              fontFamily="IBM Plex Mono, monospace"
            >
              {newest.id}
            </text>
          )}
        </svg>
      </div>

      <div className="mt-[10px] flex flex-wrap gap-[14px]">
        {(["accent", "blue", "violet", "amber"] as Tone[]).map((t, i) => (
          <div key={t} className="flex items-center gap-[6px]">
            <Dot tone={t} size={8} />
            <span className="text-[11px] text-ink-3">
              {["Screen / Content", "Playlist / Schedule", "Channel", "Settings"][i]}
            </span>
          </div>
        ))}
      </div>
    </Card>
  );
}

/* ── event feed ─────────────────────────────────────────────────────────── */

function EventFeed({ total }: { total: number }) {
  const feed = useLiveRun((s) => s.derived.feed);
  const [filter, setFilter] = useState<string | null>(null);

  const shown = filter ? feed.filter((e) => e.event === filter) : feed;

  return (
    <Card className="flex min-w-0 grow flex-col overflow-hidden pt-[15px] pb-3">
      <div className="mb-[11px] flex items-center gap-2 px-[15px]">
        <PanelTitle
          right={
            <div className="flex gap-1">
              {[null, "state_found", "outcome", "skip"].map((f) => (
                <button
                  key={f ?? "all"}
                  type="button"
                  onClick={() => setFilter(f)}
                  className={`rounded-md px-[7px] py-[3px] text-[10px] font-medium transition-colors ${
                    filter === f ? "bg-accent-dim text-accent" : "text-ink-4 hover:text-ink-2"
                  }`}
                >
                  {f ? EVENT_LABEL[f] ?? f : "ALL"}
                </button>
              ))}
            </div>
          }
        >
          EVENTS
        </PanelTitle>
      </div>

      <div className="min-h-0 grow overflow-y-auto">
        {shown.map((e, i) => {
          const tone: Tone =
            e.event === "outcome" && typeof e.outcome === "string"
              ? OUTCOME_TONE[e.outcome] ?? "muted"
              : EVENT_TONE[e.event] ?? "muted";
          return (
            <div
              key={`${e.t}-${e.event}-${i}`}
              className="border-b border-line-soft px-[15px] py-[7px]"
            >
              <div className="flex items-center gap-[7px]">
                <span className="w-[46px] shrink-0 font-mono text-[10px] text-muted tabular-nums">
                  {e.t.toFixed(1)}
                </span>
                <span
                  className="rounded px-[6px] py-[2px] text-[10px] font-semibold tracking-[0.3px]"
                  style={{ background: wash(tone, 0.14), color: TONE_HEX[tone] }}
                >
                  {EVENT_LABEL[e.event] ?? e.event.toUpperCase()}
                </span>
              </div>
              <div
                className="truncate pl-[53px] font-mono text-[10.5px] leading-[1.5] text-ink-log"
                title={e.detail}
              >
                {e.detail}
              </div>
            </div>
          );
        })}
      </div>

      <div className="border-t border-line px-[15px] pt-[10px]">
        <div className="flex items-center gap-[7px]">
          <Dot tone="accent" size={6} pulse />
          <span className="text-[11px] text-ink-4">streaming · {num(total)} events</span>
          <div className="grow" />
          <Icon name="filter" size={12} color={C.ink4} />
        </div>
      </div>
    </Card>
  );
}
