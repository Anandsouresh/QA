import { useEffect, useMemo, useRef, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { api, shotUrl } from "../lib/api";
import { num, pathOf } from "../lib/format";
import { CATEGORY_TONE, moduleTone, TONE_HEX, wash, type Tone } from "../lib/tokens";
import type { StateRec, TestCase } from "../lib/types";
import {
  Button,
  Chip,
  Dot,
  Empty,
  Icon,
  IconButton,
  PanelTitle,
  Tag,
} from "../components/ui";

const CATEGORIES = ["Happy Path", "Negative", "Edge Case", "UI/UX", "Form Filling"] as const;

type Verdict = "approved" | "rejected";

export function TestCases() {
  const [params, setParams] = useSearchParams();
  const [cases, setCases] = useState<TestCase[] | null>(null);
  const [states, setStates] = useState<StateRec[] | null>(null);
  const [category, setCategory] = useState<string | null>(null);
  const [needsOnly, setNeedsOnly] = useState(false);
  const [module, setModule] = useState<string | null>(null);
  const [cursor, setCursor] = useState(0);
  const [verdicts, setVerdicts] = useState<Record<string, Verdict>>({});

  useEffect(() => {
    api.cases().then(setCases).catch(() => undefined);
    api.states().then(setStates).catch(() => undefined);
  }, []);

  const stateFilter = params.get("state");

  const filtered = useMemo(() => {
    if (!cases) return [];
    return cases.filter((c) => {
      if (stateFilter && c.source_state !== stateFilter) return false;
      if (module && c.module !== module) return false;
      if (category && c.category !== category) return false;
      if (needsOnly && !c.needs_review) return false;
      return true;
    });
  }, [cases, category, needsOnly, module, stateFilter]);

  useEffect(() => setCursor(0), [category, needsOnly, module, stateFilter]);

  const current = filtered[Math.min(cursor, Math.max(0, filtered.length - 1))] ?? null;
  const state =
    states?.find((s) => current && s.fingerprint === current.source_fingerprint) ?? null;

  const counts = useMemo(() => {
    const byCat = new Map<string, number>();
    const byMod = new Map<string, number>();
    let needs = 0;
    (cases ?? []).forEach((c) => {
      byCat.set(c.category, (byCat.get(c.category) ?? 0) + 1);
      byMod.set(c.module, (byMod.get(c.module) ?? 0) + 1);
      if (c.needs_review) needs += 1;
    });
    return { byCat, byMod: [...byMod.entries()].sort((a, b) => b[1] - a[1]), needs };
  }, [cases]);

  const siblings = useMemo(
    () => (current ? filtered.filter((c) => c.source_state === current.source_state && c.test_id !== current.test_id).slice(0, 5) : []),
    [filtered, current],
  );

  function judge(v: Verdict) {
    if (!current) return;
    setVerdicts((m) => ({ ...m, [current.test_id]: v }));
    setCursor((c) => Math.min(c + 1, filtered.length - 1));
  }

  return (
    <div className="flex min-w-0 grow flex-col overflow-hidden">
      <header className="flex h-[62px] shrink-0 items-center gap-[14px] border-b border-line-soft px-[22px]">
        <div className="shrink-0">
          <h1 className="font-display text-[18px] leading-none font-semibold tracking-[-0.2px]">
            Test cases
          </h1>
          <div className="mt-[3px] text-[11.5px] text-ink-4">
            {num(filtered.length)} shown of {num(cases?.length ?? 0)} · {num(Object.keys(verdicts).length)} reviewed
          </div>
        </div>
        <div className="grow" />

        <div className="flex gap-[6px]">
          {CATEGORIES.map((c) => (
            <Chip
              key={c}
              tone={CATEGORY_TONE[c] as Tone}
              active={category === c}
              onClick={() => setCategory(category === c ? null : c)}
            >
              {c}
              <span className="font-mono text-[11px] opacity-75">{counts.byCat.get(c) ?? 0}</span>
            </Chip>
          ))}
        </div>

        <Chip tone="amber" active={needsOnly} onClick={() => setNeedsOnly(!needsOnly)}>
          <Icon name="warn" size={14} />
          Needs review {counts.needs}
        </Chip>

        <Button variant="primary">
          <Icon name="download" size={14} color="var(--qg-accent-deep)" strokeWidth={2.2} />
          Export
        </Button>
      </header>

      {stateFilter && (
        <div className="flex items-center gap-2 border-b border-line-soft bg-aside px-[22px] py-[9px]">
          <span className="text-[12px] text-ink-3">Filtered to state</span>
          <Tag tone="accent">{stateFilter}</Tag>
          <button
            type="button"
            onClick={() => setParams({})}
            className="text-[12px] text-accent hover:underline"
          >
            clear
          </button>
        </div>
      )}

      <div className="flex min-h-0 grow">
        {/* tree */}
        <aside className="w-[230px] shrink-0 overflow-y-auto border-r border-line-soft px-3 py-4">
          <div className="mx-[6px] mb-[10px] text-[10.5px] font-semibold tracking-[0.6px] text-ink-4">
            BY MODULE
          </div>
          <button
            type="button"
            onClick={() => setModule(null)}
            className={`mb-[2px] flex w-full items-center gap-[9px] rounded-lg px-[10px] py-2 text-left text-[12.5px] ${
              module === null ? "bg-raised text-ink" : "text-ink-body hover:bg-hover"
            }`}
          >
            <span className="block h-[15px] w-[3px] shrink-0 rounded-sm bg-line-hover" />
            <span className="grow">All modules</span>
            <span className="font-mono text-[11px] text-ink-4">{num(cases?.length ?? 0)}</span>
          </button>
          {counts.byMod.map(([m, n]) => (
            <button
              key={m}
              type="button"
              onClick={() => setModule(module === m ? null : m)}
              className={`mb-[2px] flex w-full items-center gap-[9px] rounded-lg px-[10px] py-2 text-left text-[12.5px] ${
                module === m ? "bg-raised text-ink" : "text-ink-body hover:bg-hover"
              }`}
            >
              <span
                className="block h-[15px] w-[3px] shrink-0 rounded-sm"
                style={{ background: TONE_HEX[moduleTone(m)] }}
              />
              <span className="grow truncate">{m}</span>
              <span className="font-mono text-[11px] text-ink-4">{n}</span>
            </button>
          ))}

          <div className="mx-[6px] mt-5 mb-[10px] text-[10.5px] font-semibold tracking-[0.6px] text-ink-4">
            IN THIS VIEW
          </div>
          <div className="mx-[6px] space-y-[7px]">
            {(["approved", "rejected"] as Verdict[]).map((v) => (
              <div key={v} className="flex items-center gap-[9px]">
                <Dot tone={v === "approved" ? "accent" : "red"} />
                <span className="grow text-[12px] text-ink-2 capitalize">{v}</span>
                <span className="font-mono text-[11px] text-ink-4">
                  {Object.values(verdicts).filter((x) => x === v).length}
                </span>
              </div>
            ))}
          </div>
        </aside>

        {/* case */}
        <section className="flex min-w-0 grow flex-col gap-[14px] overflow-hidden px-[22px] py-[18px]">
          {current ? (
            <>
              <div className="flex items-start gap-[14px]">
                <div className="min-w-0 grow">
                  <div className="mb-[7px] flex flex-wrap items-center gap-[9px]">
                    <Tag>{current.test_id}</Tag>
                    <Tag tone={CATEGORY_TONE[current.category] as Tone}>{current.category}</Tag>
                    <span className="font-mono text-[11.5px] text-ink-4">
                      {current.source_state} · {pathOf(current.source_url)}
                    </span>
                    {verdicts[current.test_id] && (
                      <Tag tone={verdicts[current.test_id] === "approved" ? "accent" : "red"}>
                        {verdicts[current.test_id]}
                      </Tag>
                    )}
                  </div>
                  <h2 className="font-display text-[21px] leading-[1.3] font-semibold tracking-[-0.2px]">
                    {current.title}
                  </h2>
                </div>
                <div className="flex shrink-0 items-center gap-2">
                  <span className="font-mono text-[11.5px] text-ink-4 tabular-nums">
                    {cursor + 1} / {filtered.length}
                  </span>
                  <IconButton
                    icon="left"
                    label="Previous case"
                    onClick={() => setCursor((c) => Math.max(0, c - 1))}
                  />
                  <IconButton
                    icon="right"
                    label="Next case"
                    onClick={() => setCursor((c) => Math.min(filtered.length - 1, c + 1))}
                  />
                </div>
              </div>

              {current.needs_review && current.review_notes.length > 0 && (
                <div
                  className="flex items-start gap-[10px] rounded-[10px] border px-[15px] py-3"
                  style={{ background: wash("amber", 0.09), borderColor: wash("amber", 0.3) }}
                >
                  <Icon name="warn" size={16} color={TONE_HEX.amber} strokeWidth={2} />
                  <div>
                    <div className="text-[12px] font-semibold" style={{ color: TONE_HEX.amber }}>
                      Flagged by the validator
                    </div>
                    <div className="mt-[3px] text-[12px] leading-[1.5] text-ink-2">
                      {current.review_notes.join(" ")}
                    </div>
                  </div>
                </div>
              )}

              <div className="rounded-[10px] border border-rail-line bg-surface px-[15px] py-3">
                <div className="mb-[7px] text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
                  PRECONDITIONS
                </div>
                <div className="flex flex-wrap gap-[7px]">
                  {current.preconditions.map((p) => (
                    <span
                      key={p}
                      className="rounded-md bg-raised px-[10px] py-1 text-[12px] text-ink-body"
                    >
                      {p}
                    </span>
                  ))}
                </div>
                {current.reachability.length > 1 && (
                  <div className="mt-[9px] flex items-center gap-[7px] text-[11.5px] text-ink-4">
                    <Icon name="graph" size={13} color={TONE_HEX.accent} strokeWidth={2} />
                    Reachability taken from the graph, not guessed:{" "}
                    <span className="font-mono text-accent-ink">
                      {current.reachability.join(" → ")}
                    </span>
                  </div>
                )}
              </div>

              <div className="flex min-h-0 grow flex-col overflow-hidden rounded-[10px] border border-rail-line bg-surface">
                <div className="grid grid-cols-[38px_1fr_1fr] gap-x-4 border-b border-rail-line px-4 py-[11px] text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
                  <span>#</span>
                  <span>ACTION</span>
                  <span>EXPECTED RESULT</span>
                </div>

                <div className="min-h-0 grow overflow-y-auto">
                  {current.steps.map((s) => (
                    <div
                      key={s.step_number}
                      className="grid grid-cols-[38px_1fr_1fr] items-start gap-x-4 border-b border-line-soft px-4 py-3"
                    >
                      <span className="font-mono text-[12px] text-accent tabular-nums">
                        {s.step_number}
                      </span>
                      <span className="text-[12.5px] leading-[1.55] text-ink-strong">{s.action}</span>
                      <span className="text-[12.5px] leading-[1.55] text-ink-2">
                        {s.expected_result}
                      </span>
                    </div>
                  ))}

                  {siblings.length > 0 && (
                    <div className="px-4 pt-[14px] pb-2">
                      <div className="mb-[6px] text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
                        OTHER CASES ON THIS STATE
                      </div>
                      {siblings.map((s) => (
                        <button
                          key={s.test_id}
                          type="button"
                          onClick={() =>
                            setCursor(filtered.findIndex((c) => c.test_id === s.test_id))
                          }
                          className="flex w-full items-center gap-[11px] border-b border-line-soft py-2 text-left hover:bg-hover"
                        >
                          <span className="shrink-0 font-mono text-[11.5px] text-ink-4">
                            {s.test_id}
                          </span>
                          <Dot tone={CATEGORY_TONE[s.category] as Tone} />
                          <span className="grow truncate text-[12.5px] text-ink-body">
                            {s.title}
                          </span>
                          {s.needs_review && (
                            <span
                              className="shrink-0 rounded px-[7px] py-[2px] text-[10.5px]"
                              style={{ background: wash("amber", 0.14), color: TONE_HEX.amber }}
                            >
                              needs review
                            </span>
                          )}
                        </button>
                      ))}
                    </div>
                  )}
                </div>

                <div
                  className="border-t px-4 py-[13px]"
                  style={{ background: wash("accent", 0.07), borderColor: wash("accent", 0.28) }}
                >
                  <div className="mb-[5px] text-[10.5px] font-semibold tracking-[0.5px] text-accent">
                    OVERALL EXPECTED RESULT
                  </div>
                  <p className="text-[12.5px] leading-[1.55] text-ink-body">
                    {current.overall_expected_result}
                  </p>
                </div>
              </div>
            </>
          ) : (
            <Empty>
              No case matches these filters. Clear a filter to bring the suite back into view.
            </Empty>
          )}
        </section>

        {/* evidence */}
        <aside className="flex w-[382px] shrink-0 flex-col overflow-hidden border-l border-line-soft bg-aside">
          <div className="px-[18px] pt-4 pb-3">
            <h2 className="font-display mb-[3px] text-[14px] font-semibold">Evidence</h2>
            <p className="text-[11.5px] leading-[1.45] text-ink-4">
              Every selector this case cites was present in the capture. The box is drawn from the
              geometry recorded at extraction.
            </p>
          </div>

          {current && <EvidenceShot testCase={current} state={state} />}

          {current && current.constraints.length > 0 && (
            <div className="px-[18px] pt-4">
              <div className="mb-[9px] text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
                FIELD CONSTRAINTS READ FROM THE DOM
              </div>
              {current.constraints.map((c) => (
                <div
                  key={c.k}
                  className="flex items-center gap-[10px] border-b border-line-soft py-[7px]"
                >
                  <span className="w-[92px] shrink-0 font-mono text-[11.5px] text-ink-3">{c.k}</span>
                  <span className="grow truncate font-mono text-[11.5px] text-ink-strong">{c.v}</span>
                </div>
              ))}
              <p className="mt-[11px] text-[11.5px] leading-[1.5] text-ink-4">
                The negative and edge cases come from these constraints. The form was never
                submitted.
              </p>
            </div>
          )}

          {current && (
            <div className="px-[18px] pt-4">
              <PanelTitle>CITED SELECTORS</PanelTitle>
              <div className="mt-2">
                {current.source_selectors.map((s) => (
                  <div
                    key={s}
                    className="flex items-center gap-2 border-b border-line-soft py-[7px]"
                    title={s}
                  >
                    <Icon name="check" size={13} color={TONE_HEX.accent} strokeWidth={2.4} />
                    <span className="truncate font-mono text-[11px] text-ink-2">{s}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="grow" />

          <div className="flex gap-[9px] border-t border-line-soft px-[18px] pt-[14px] pb-4">
            <Button variant="accent-soft" className="grow" onClick={() => judge("approved")}>
              <Icon name="check" size={15} strokeWidth={2.2} />
              Approve
            </Button>
            <Button className="grow">Edit</Button>
            <IconButton icon="x" label="Reject case" tone="red" size={44} />
          </div>
        </aside>
      </div>
    </div>
  );
}

/** The screenshot with the cited element boxed on it, scaled from the capture's
 *  own viewport width to whatever width the panel gives us. */
function EvidenceShot({ testCase, state }: { testCase: TestCase; state: StateRec | null }) {
  const [width, setWidth] = useState(0);
  const wrap = useRef<HTMLDivElement | null>(null);
  const shot = shotUrl(state?.screenshot ?? null);
  // A transformed container (carousel, drawer) can report a position outside
  // the captured page. Say so rather than boxing the wrong pixels.
  const hl = testCase.highlight_valid ? testCase.highlight : null;

  useEffect(() => {
    const el = wrap.current;
    if (!el) return;
    const ro = new ResizeObserver(([entry]) => setWidth(entry.contentRect.width));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const scale = state && width ? width / (state.viewport_width || 1200) : 0;
  // Keep the cited control in frame rather than showing the top of a long page.
  const offset = hl && scale ? Math.max(0, hl.y * scale - 90) : 0;

  return (
    <div className="px-[18px]">
      <div
        ref={wrap}
        className="relative h-[246px] overflow-hidden rounded-[10px] border border-line bg-well"
      >
        {shot ? (
          <>
            <img
              src={shot}
              alt={`Capture of ${state?.title ?? "the source state"}`}
              className="absolute top-0 left-0 w-full max-w-none"
              style={{ transform: `translateY(${-offset}px)` }}
            />
            {hl && scale > 0 && (
              <div
                className="pointer-events-none absolute"
                style={{
                  left: hl.x * scale,
                  top: hl.y * scale - offset,
                  width: Math.max(10, hl.w * scale),
                  height: Math.max(10, hl.h * scale),
                }}
              >
                <div
                  className="h-full w-full rounded-[4px]"
                  style={{
                    border: `2px solid ${TONE_HEX.amber}`,
                    boxShadow: `0 0 0 4px ${wash("amber", 0.16)}`,
                  }}
                />
                <span
                  className="absolute -top-[10px] left-2 max-w-[240px] truncate rounded px-[5px] py-[1px] font-mono text-[9px] font-medium"
                  style={{ background: TONE_HEX.amber, color: "var(--qg-amber-deep)" }}
                >
                  {hl.label}
                </span>
              </div>
            )}
          </>
        ) : (
          <Empty>No capture stored for this state.</Empty>
        )}
      </div>
      {state && (
        <div className="mt-[6px] truncate font-mono text-[10px] text-ink-4">
          {state.screenshot?.replace("artifacts/", "")} · {state.viewport_width}×
          {state.document_height}
        </div>
      )}
      {!testCase.highlight_valid && testCase.highlight && (
        <div
          className="mt-2 rounded-lg border px-3 py-2 text-[11.5px] leading-[1.5]"
          style={{ background: wash("amber", 0.08), borderColor: wash("amber", 0.28), color: "var(--qg-amber-ink)" }}
        >
          The control sits in a transformed container, so its recorded position falls outside the
          capture. The selector is still grounded; only the box is withheld.
        </div>
      )}
    </div>
  );
}
