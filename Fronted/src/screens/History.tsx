import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { control, type RunRow } from "../lib/api";
import { hostOf, num, pathOf } from "../lib/format";
import { TONE_HEX, wash, type Tone } from "../lib/tokens";
import { isRunning, useSession } from "../store/session";
import { Banner, Button, Card, Dot, Empty, Icon, PanelTitle, Tag } from "../components/ui";

const STATUS_TONE: Record<string, Tone> = {
  running: "accent",
  starting: "accent",
  paused: "amber",
  stopping: "amber",
  stopped: "amber",
  finished: "muted",
  failed: "red",
};

export function History() {
  const navigate = useNavigate();
  const { online, checked, runs, runsDir, source, detect, refreshRuns, select } = useSession();
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!checked) detect();
  }, [checked, detect]);

  // A crawl runs for hours; a slow poll is enough to keep the list honest.
  useEffect(() => {
    if (!online) return;
    const id = window.setInterval(refreshRuns, 5000);
    return () => window.clearInterval(id);
  }, [online, refreshRuns]);

  async function act(id: string, action: "stop" | "remove") {
    setBusy(id);
    setError(null);
    try {
      await control[action](id);
      await refreshRuns();
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(null);
    }
  }

  function open(row: RunRow) {
    select({ kind: "live", runId: row.id });
    navigate(isRunning(row) ? "/live" : row.has_cases ? "/cases" : "/graph");
  }

  const demoActive = source.kind === "demo";

  return (
    <div className="flex min-w-0 grow flex-col overflow-hidden">
      <header className="flex h-[62px] shrink-0 items-center gap-4 border-b border-line-soft px-[22px]">
        <div>
          <h1 className="font-display text-[18px] leading-none font-semibold tracking-[-0.2px]">
            Runs
          </h1>
          <div className="mt-[3px] text-[11.5px] text-ink-4">
            {online ? (
              <>
                {runs.length} on disk · <span className="font-mono">{runsDir}</span>
              </>
            ) : (
              "backend offline"
            )}
          </div>
        </div>
        <div className="grow" />
        <Button onClick={refreshRuns} disabled={!online}>
          <Icon name="refresh" size={14} />
          Refresh
        </Button>
        <Button variant="primary" onClick={() => navigate("/")}>
          <Icon name="plus" size={14} />
          New run
        </Button>
      </header>

      <div className="min-h-0 grow overflow-y-auto px-[22px] py-[18px]">
        {error && (
          <div className="mb-4">
            <Banner tone="red" title="That action failed">
              {error}
            </Banner>
          </div>
        )}

        {/* the recorded run, always available */}
        <Card
          className="mb-4 flex items-center gap-4 px-5 py-4"
          style={
            demoActive
              ? { background: wash("accent", 0.06), borderColor: wash("accent", 0.28) }
              : undefined
          }
        >
          <Dot tone={demoActive ? "accent" : "muted"} size={9} />
          <div className="min-w-0 grow">
            <div className="text-[13.5px] font-semibold">Recorded run — samsungvx-200-final05</div>
            <div className="mt-[2px] text-[12px] text-ink-3">
              175 states, 672 transitions, 102 captures. Bundled with the app, so every screen works
              with no backend.
            </div>
          </div>
          <Button
            variant={demoActive ? "accent-soft" : "ghost"}
            onClick={() => {
              select({ kind: "demo" });
              navigate("/graph");
            }}
          >
            {demoActive ? "Now viewing" : "View this"}
          </Button>
        </Card>

        {!online && checked && (
          <Banner tone="amber" title="No backend, so there are no live runs to list">
            Start it with <span className="font-mono text-ink">uvicorn api.main:app --port 8000</span>{" "}
            from the repository root, then press Refresh.
          </Banner>
        )}

        {online && runs.length === 0 && (
          <Card className="py-10">
            <Empty>
              No runs yet. Configure one on the New run screen and it will appear here while it
              works.
            </Empty>
          </Card>
        )}

        {online && runs.length > 0 && (
          <Card className="overflow-hidden">
            <div className="grid grid-cols-[210px_96px_1fr_88px_96px_150px] items-center gap-x-4 border-b border-line px-5 py-3 text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
              <span>RUN</span>
              <span>STATUS</span>
              <span>TARGET</span>
              <span className="text-right">STATES</span>
              <span className="text-right">LOG</span>
              <span />
            </div>

            {runs.map((r) => {
              const active = source.kind === "live" && source.runId === r.id;
              return (
                <div
                  key={r.id}
                  className="grid grid-cols-[210px_96px_1fr_88px_96px_150px] items-center gap-x-4 border-b border-line-soft px-5 py-[13px]"
                  style={active ? { background: wash("accent", 0.05) } : undefined}
                >
                  <button
                    type="button"
                    onClick={() => open(r)}
                    className="flex min-w-0 items-center gap-2 text-left font-mono text-[12px] text-ink-strong hover:text-accent"
                  >
                    <Dot tone={STATUS_TONE[r.status] ?? "muted"} pulse={isRunning(r)} />
                    <span className="truncate">{r.id}</span>
                  </button>

                  <Tag tone={STATUS_TONE[r.status] ?? "muted"}>{r.status}</Tag>

                  <span className="truncate text-[12px] text-ink-2" title={r.target}>
                    {hostOf(r.target)}
                    <span className="text-ink-4">{pathOf(r.target)}</span>
                  </span>

                  <span className="text-right font-mono text-[12.5px] tabular-nums">
                    <span style={{ color: r.has_graph ? TONE_HEX.ink : TONE_HEX.muted }}>
                      {r.max_states ? `≤${num(r.max_states)}` : "—"}
                    </span>
                  </span>

                  <span className="text-right font-mono text-[11.5px] text-ink-4 tabular-nums">
                    {r.log_bytes ? `${(r.log_bytes / 1024).toFixed(0)} kB` : "—"}
                  </span>

                  <div className="flex justify-end gap-2">
                    {isRunning(r) ? (
                      <Button
                        size="sm"
                        variant="danger"
                        disabled={busy === r.id}
                        onClick={() => act(r.id, "stop")}
                      >
                        Stop
                      </Button>
                    ) : (
                      <Button
                        size="sm"
                        disabled={busy === r.id}
                        onClick={() => act(r.id, "remove")}
                        title="Delete this run directory"
                      >
                        <Icon name="trash" size={13} />
                      </Button>
                    )}
                    <Button size="sm" variant={active ? "accent-soft" : "ghost"} onClick={() => open(r)}>
                      {active ? "Viewing" : "Open"}
                    </Button>
                  </div>
                </div>
              );
            })}
          </Card>
        )}

        <div className="mt-[18px] grid grid-cols-2 gap-[14px]">
          <Card className="px-5 py-[18px]">
            <PanelTitle>WHY A RUN STOPPED IS A FINDING</PanelTitle>
            <p className="mt-2 text-[12.5px] leading-[1.6] text-ink-2">
              A run that ends because one module ate the budget is telling you about your
              configuration, not about the application. Per-module budgets exist for exactly that,
              and the reason is recorded in the manifest either way.
            </p>
          </Card>

          <Card
            className="px-5 py-[18px]"
            style={{ background: wash("accent", 0.06), borderColor: wash("accent", 0.25) }}
          >
            <PanelTitle>STOPPING KEEPS EVERYTHING</PanelTitle>
            <p className="mt-2 text-[12.5px] leading-[1.6] text-ink-2">
              Stop writes a sentinel file the crawler checks each iteration. It finishes the state
              it is on, then writes the graph, the captures and the manifest. The process is never
              killed, so partial output is never lost.
            </p>
            <div className="mt-3 flex items-center gap-2">
              <Tag tone="accent">touch &lt;run&gt;/STOP</Tag>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
