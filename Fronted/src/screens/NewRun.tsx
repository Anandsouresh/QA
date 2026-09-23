import { useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { control } from "../lib/api";
import { compactDuration, hostOf } from "../lib/format";
import { titleCase } from "../lib/modules";
import { moduleTone, TONE_HEX, wash } from "../lib/tokens";
import { useSession } from "../store/session";
import {
  Bar,
  Banner,
  Button,
  Card,
  Field,
  Icon,
  PanelTitle,
  PlayGlyph,
  TextArea,
  TextInput,
  Toggle,
} from "../components/ui";

/** Seconds per discovered state, measured on the recorded run: 17,605s for
 *  116 states. The duration on screen is derived, never invented. */
const SECONDS_PER_STATE = 151;

interface ModuleRow {
  name: string;
  paths: string[];
  pathCount: number;
  budget: number;
  selected: boolean;
}

const FALLBACK: ModuleRow[] = [
  { name: "Screen", paths: ["/screen", "/screen/{id}"], pathCount: 2, budget: 40, selected: true },
  { name: "Content", paths: ["/content", "/content/{id}"], pathCount: 2, budget: 40, selected: true },
  { name: "Playlist", paths: ["/playlist", "/playlist/create"], pathCount: 3, budget: 30, selected: true },
  { name: "Schedule", paths: ["/schedule", "/schedule/create"], pathCount: 3, budget: 30, selected: true },
  { name: "Channel", paths: ["/channel"], pathCount: 1, budget: 20, selected: true },
  { name: "Settings", paths: ["/settings", "+20 sub-pages"], pathCount: 21, budget: 40, selected: true },
];

type Verify =
  | { state: "idle" }
  | { state: "checking" }
  | { state: "ok"; landed: string; title: string }
  | { state: "failed"; code: string; detail: string };

export function NewRun() {
  const navigate = useNavigate();
  const online = useSession((s) => s.online);
  const checked = useSession((s) => s.checked);
  const detect = useSession((s) => s.detect);
  const select = useSession((s) => s.select);
  const refreshRuns = useSession((s) => s.refreshRuns);

  const [url, setUrl] = useState("https://stg.samsungvx.com/");
  const [depth, setDepth] = useState(20);
  const [storageState, setStorageState] = useState("");
  const [verifySelector, setVerifySelector] = useState("");
  const [anthropicKey, setAnthropicKey] = useState("");
  const [generate, setGenerate] = useState(true);
  const [headless, setHeadless] = useState(true);
  const [modules, setModules] = useState<ModuleRow[]>(FALLBACK);
  const [verify, setVerify] = useState<Verify>({ state: "idle" });
  const [probing, setProbing] = useState(false);
  const [probeNote, setProbeNote] = useState<string | null>(null);
  const [starting, setStarting] = useState(false);
  const [startError, setStartError] = useState<string | null>(null);
  const fileInput = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    if (!checked) detect();
  }, [checked, detect]);

  const chosen = modules.filter((m) => m.selected);
  const total = useMemo(() => chosen.reduce((n, m) => n + (m.budget || 0), 0), [chosen]);
  const estimate = total * SECONDS_PER_STATE;
  const authBody = {
    url,
    auth: { storage_state: storageState || null, verify_selector: verifySelector || null },
  };

  function patch(name: string, next: Partial<ModuleRow>) {
    setModules((rows) => rows.map((r) => (r.name === name ? { ...r, ...next } : r)));
  }

  async function onFile(file: File) {
    const text = await file.text();
    try {
      JSON.parse(text);
      setStorageState(text);
      setVerify({ state: "idle" });
    } catch {
      setVerify({
        state: "failed",
        code: "NOT_JSON",
        detail: `${file.name} is not valid JSON. Export the cookies again.`,
      });
    }
  }

  async function runVerify() {
    setVerify({ state: "checking" });
    try {
      const res = await control.probeAuth(authBody);
      setVerify(
        res.ok
          ? { state: "ok", landed: res.landed_on ?? url, title: res.title ?? "" }
          : { state: "failed", code: res.code ?? "FAILED", detail: res.detail ?? "" },
      );
    } catch (err) {
      setVerify({
        state: "failed",
        code: "NO_BACKEND",
        detail: err instanceof Error ? err.message : String(err),
      });
    }
  }

  async function runProbe() {
    setProbing(true);
    setProbeNote(null);
    try {
      const res = await control.probeModules({ ...authBody, total_states: 200 });
      const rows: ModuleRow[] = res.modules.map((m) => ({
        name: titleCase(m.name),
        paths: m.paths,
        pathCount: m.path_count,
        budget: res.suggested_budgets[m.name] ?? 15,
        selected: true,
      }));
      setModules(rows.length ? rows : FALLBACK);
      setProbeNote(
        `${res.modules.length} modules from ${res.dom_nodes.toLocaleString()} DOM nodes` +
          (res.external_hosts.length ? ` · ${res.external_hosts.length} external hosts ignored` : ""),
      );
    } catch (err) {
      setProbeNote(err instanceof Error ? err.message : String(err));
    } finally {
      setProbing(false);
    }
  }

  async function start() {
    setStarting(true);
    setStartError(null);
    try {
      const res = await control.start({
        url,
        depth,
        modules: Object.fromEntries(chosen.map((m) => [m.name, m.budget])),
        auth: {
          storage_state: storageState || null,
          verify_selector: verifySelector || null,
        },
        anthropic_key: generate ? anthropicKey || null : null,
        generate,
        headless,
      });
      await refreshRuns();
      select({ kind: "live", runId: res.id });
      navigate("/live");
    } catch (err) {
      setStartError(err instanceof Error ? err.message : String(err));
    } finally {
      setStarting(false);
    }
  }

  return (
    <div className="flex min-w-0 grow flex-col gap-5 overflow-y-auto px-[30px] py-6">
      <header className="flex items-end justify-between gap-6">
        <div>
          <h1 className="font-display mb-[5px] text-[27px] leading-none font-semibold tracking-[-0.4px]">
            New run
          </h1>
          <p className="text-[13.5px] text-ink-2">
            Crawl a live application read-only, then write grounded QA test cases from what was
            actually on screen.
          </p>
        </div>
        <div className="flex shrink-0 items-center gap-[10px]">
          <span
            className="flex items-center gap-2 rounded-lg border px-3 py-[7px] text-[12px]"
            style={{
              background: wash(online ? "accent" : "amber", 0.08),
              borderColor: wash(online ? "accent" : "amber", 0.3),
              color: TONE_HEX[online ? "accent" : "amber"],
            }}
          >
            <span className={`block h-[7px] w-[7px] rounded-full ${online ? "qg-pulse" : ""}`}
                  style={{ background: "currentColor" }} />
            {online ? "backend connected" : "backend offline"}
          </span>
          <Button onClick={detect}>
            <Icon name="refresh" size={14} />
            Re-check
          </Button>
        </div>
      </header>

      {checked && !online && (
        <Banner tone="amber" title="No backend, so this form cannot start a crawl">
          Everything else stays explorable against the recorded run. To start real crawls:{" "}
          <span className="font-mono text-ink">uvicorn api.main:app --port 8000</span> from the
          repository root.
        </Banner>
      )}

      {startError && (
        <Banner tone="red" title="The run did not start">
          {startError}
        </Banner>
      )}

      <div className="flex min-h-0 grow gap-[22px]">
        {/* ── configuration ── */}
        <div className="flex min-w-0 grow flex-col gap-[13px]">
          {/* 01 target */}
          <Card className="px-5 pt-[18px] pb-[19px]">
            <PanelTitle step="01">Target</PanelTitle>
            <div className="mt-[15px] flex items-end gap-[14px]">
              <div className="min-w-0 grow">
                <Field label="TARGET URL">
                  <TextInput value={url} onChange={(e) => setUrl(e.target.value)} type="url" />
                </Field>
              </div>
              <div className="w-[118px] shrink-0">
                <Field label="DEPTH">
                  <TextInput
                    value={depth}
                    onChange={(e) => setDepth(Number(e.target.value) || 0)}
                    type="number"
                  />
                </Field>
              </div>
            </div>
          </Card>

          {/* 02 tokens */}
          <Card className="px-5 pt-[18px] pb-[19px]">
            <PanelTitle step="02">Tokens</PanelTitle>
            <p className="mt-1 mb-[14px] text-[12px] text-ink-3">
              Two different secrets. The session token proves you are logged into the target; the
              model key pays for test-case generation.
            </p>

            <div className="grid grid-cols-2 gap-[18px]">
              <div>
                <Field label="SESSION TOKEN FOR THE TARGET">
                  <TextArea
                    rows={5}
                    value={storageState}
                    spellCheck={false}
                    onChange={(e) => {
                      setStorageState(e.target.value);
                      setVerify({ state: "idle" });
                    }}
                    placeholder={'Paste a Playwright storage_state object, or a cookie array\nexported by a browser extension. Both are accepted.'}
                  />
                </Field>
                <div className="mt-[9px] flex items-center gap-2">
                  <input
                    ref={fileInput}
                    type="file"
                    accept="application/json,.json"
                    hidden
                    onChange={(e) => {
                      const f = e.target.files?.[0];
                      if (f) onFile(f);
                    }}
                  />
                  <Button size="sm" onClick={() => fileInput.current?.click()}>
                    <Icon name="upload" size={13} />
                    Load .json
                  </Button>
                  <Button size="sm" onClick={runVerify} disabled={!online || verify.state === "checking"}>
                    {verify.state === "checking" ? "Verifying…" : "Verify session"}
                  </Button>
                  {storageState && (
                    <span className="font-mono text-[11px] text-ink-4">
                      {(storageState.length / 1024).toFixed(1)} kB
                    </span>
                  )}
                </div>
              </div>

              <div className="flex flex-col">
                <Field
                  label="ANTHROPIC API KEY"
                  hint="Sent to the crawl process as an environment variable. Never written to the run directory."
                >
                  <TextInput
                    type="password"
                    autoComplete="off"
                    value={anthropicKey}
                    onChange={(e) => setAnthropicKey(e.target.value)}
                    placeholder="sk-ant-…"
                  />
                </Field>
                <div className="mt-[14px]">
                  <Field
                    label="VERIFY SELECTOR"
                    hint="Something only a signed-in user sees. Without it an expired cookie crawls the login page."
                  >
                    <TextInput
                      value={verifySelector}
                      onChange={(e) => setVerifySelector(e.target.value)}
                      placeholder='[data-testid="user-menu"]'
                    />
                  </Field>
                </div>
              </div>
            </div>

            {verify.state !== "idle" && verify.state !== "checking" && (
              <div className="mt-[14px]">
                {verify.state === "ok" ? (
                  <Banner tone="accent" title="Session verified">
                    Landed on <span className="font-mono">{verify.landed}</span>
                    {verify.title ? ` — “${verify.title}”` : ""} as a signed-in user.
                  </Banner>
                ) : (
                  <Banner tone="red" title={verify.code}>
                    {verify.detail}
                  </Banner>
                )}
              </div>
            )}
          </Card>

          {/* 03 modules */}
          <Card className="flex flex-col px-5 pt-[18px] pb-4">
            <PanelTitle
              step="03"
              right={
                <Button size="sm" onClick={runProbe} disabled={!online || probing}>
                  {probing ? "Probing…" : "Discover modules"}
                </Button>
              }
            >
              Modules &amp; state budget
            </PanelTitle>
            <p className="mt-1 mb-[13px] text-[12px] text-ink-3">
              {probeNote ??
                "Untick a module to leave it out of the run entirely. A budget is a ceiling on distinct states, so one deep area cannot starve the rest."}
            </p>

            <div className="grid grid-cols-[26px_140px_1fr_92px_140px] items-center gap-x-3 border-b border-line px-[2px] pb-2 text-[10.5px] font-semibold tracking-[0.5px] text-ink-4">
              <span />
              <span>MODULE</span>
              <span>PATHS DISCOVERED</span>
              <span className="text-right">STATES</span>
              <span>SHARE</span>
            </div>

            {modules.map((m) => (
              <div
                key={m.name}
                className="grid grid-cols-[26px_140px_1fr_92px_140px] items-center gap-x-3 border-b border-line-soft px-[2px] py-[5px]"
                style={{ opacity: m.selected ? 1 : 0.42 }}
              >
                <input
                  type="checkbox"
                  aria-label={`Include ${m.name}`}
                  checked={m.selected}
                  onChange={(e) => patch(m.name, { selected: e.target.checked })}
                  className="h-[15px] w-[15px] accent-accent"
                />
                <span className="truncate text-[13px] font-medium">{m.name}</span>
                <span className="truncate font-mono text-[11.5px] text-ink-3" title={m.paths.join(" · ")}>
                  {m.paths.join(" · ") || "—"}
                  {m.pathCount > m.paths.length ? ` +${m.pathCount - m.paths.length}` : ""}
                </span>
                <input
                  type="number"
                  aria-label={`${m.name} state budget`}
                  value={m.budget}
                  disabled={!m.selected}
                  onChange={(e) => patch(m.name, { budget: Math.max(0, Number(e.target.value)) })}
                  className="bg-sunken h-8 w-full rounded-[7px] border border-line-strong px-[9px] text-right font-mono text-[12.5px] text-ink outline-none focus:border-accent-line disabled:opacity-40"
                />
                <Bar
                  percent={total ? (m.budget / total) * 100 : 0}
                  tone={moduleTone(m.name)}
                  height={7}
                />
              </div>
            ))}

            <div className="grid grid-cols-[26px_140px_1fr_92px_140px] items-center gap-x-3 px-[2px] pt-[11px]">
              <span />
              <span className="text-[12.5px] font-semibold text-ink-2">Total</span>
              <span className="text-[12px] text-ink-4">
                {chosen.length} of {modules.length} modules in scope
              </span>
              <span className="text-right font-mono text-[14px] text-accent tabular-nums">
                {total}
              </span>
              <span className="text-[12px] text-ink-4">distinct states</span>
            </div>
          </Card>

          {/* 04 safety */}
          <Card className="px-5 pt-4 pb-[17px]">
            <PanelTitle step="04">Safety &amp; mode</PanelTitle>
            <div className="mt-[13px] flex gap-[18px]">
              <div
                className="flex w-[268px] shrink-0 items-center gap-3 rounded-[10px] border px-[14px] py-3"
                style={{ background: wash("accent", 0.09), borderColor: wash("accent", 0.32) }}
              >
                <Icon name="shield" size={26} color={TONE_HEX.accent} strokeWidth={1.6} />
                <div>
                  <div className="text-[13px] font-semibold">Write-guard armed</div>
                  <div className="mt-[2px] text-[11.5px] leading-[1.45] text-accent-ink">
                    POST, PUT, PATCH and DELETE are aborted at the route layer, then recorded.
                  </div>
                </div>
              </div>

              <div className="flex grow flex-col justify-center gap-[14px]">
                <Toggle
                  checked={generate}
                  onChange={setGenerate}
                  label="Generate test cases after the crawl"
                  hint="Off writes only the graph and the captures. Generation can be re-run later against the same crawl without re-crawling."
                />
                <Toggle
                  checked={headless}
                  onChange={setHeadless}
                  label="Headless browser"
                  hint="Off opens a visible Chromium. Useful once, for watching a target that behaves oddly."
                />
              </div>
            </div>
          </Card>
        </div>

        {/* ── run plan ── */}
        <aside className="bg-surface flex w-[330px] shrink-0 flex-col rounded-[13px] border border-line-strong p-5">
          <h2 className="font-display mb-[3px] text-[15px] font-semibold">Run plan</h2>
          <p className="mb-4 text-[12px] text-ink-3">
            Duration derived from the last recorded run on this host.
          </p>

          {[
            ["Host", hostOf(url)],
            ["Modules", `${chosen.length} in scope`],
            ["States", `${total} max`],
            ["Session", storageState ? "token supplied" : "none"],
            ["Model key", anthropicKey ? "supplied" : generate ? "missing" : "not needed"],
            ["Mode", generate ? "crawl + generate" : "crawl only"],
          ].map(([k, v]) => (
            <div
              key={k}
              className="flex items-baseline justify-between gap-3 border-b border-line-soft py-[9px]"
            >
              <span className="shrink-0 text-[12.5px] text-ink-3">{k}</span>
              <span className="truncate font-mono text-[12.5px] text-ink-strong">{v}</span>
            </div>
          ))}

          <div className="mt-[18px] rounded-[10px] border border-line bg-inset px-[14px] py-[13px]">
            <div className="mb-[7px] flex items-baseline justify-between">
              <span className="text-[12px] text-ink-2">Estimated duration</span>
              <span className="font-display text-[20px] font-semibold text-accent tabular-nums">
                {compactDuration(estimate)}
              </span>
            </div>
            <Bar percent={Math.min(100, (estimate / (24 * 3600)) * 400)} tone="accent" />
            <p className="mt-2 text-[11.5px] leading-[1.5] text-ink-4">
              Crawling is the slow half. Generation runs separately in about nine minutes.
            </p>
          </div>

          <div className="grow" />

          {generate && !anthropicKey && (
            <p className="mb-2 text-[11.5px] leading-[1.5] text-amber">
              No model key. The crawl will run, then generation will fail for want of one.
            </p>
          )}

          <Button
            variant="primary"
            size="lg"
            className="mt-2 w-full"
            disabled={!online || starting || total === 0}
            onClick={start}
            title={!online ? "Start the API first" : total === 0 ? "Select at least one module" : ""}
          >
            <PlayGlyph />
            {starting ? "Starting…" : "Start crawl"}
          </Button>
          <p className="mt-[11px] text-center text-[11.5px] leading-[1.5] text-ink-4">
            Nothing on the target is created, edited or deleted.
          </p>
        </aside>
      </div>
    </div>
  );
}
