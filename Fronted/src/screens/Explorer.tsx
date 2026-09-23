import { useCallback, useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Background,
  BackgroundVariant,
  Controls,
  Handle,
  Position,
  ReactFlow,
  type Edge,
  type Node,
  type NodeProps,
} from "@xyflow/react";
import { api, shotUrl } from "../lib/api";
import { num, pathOf, titleOf } from "../lib/format";
import { C, moduleTone, NODE_TYPE_TONE, OUTCOME_TONE, TONE_HEX, wash } from "../lib/tokens";
import type { Graph, NavNode, StateRec } from "../lib/types";
import { Button, Dot, Empty, Icon, IconButton, PanelTitle, Tag } from "../components/ui";

const COL_W = 236;        // node width + gutter
const ROW_H = 104;
const ROWS_PER_COL = 10;  // a module taller than this wraps into sub-columns
const MODULE_GAP = 64;

/** The product modules, shown first. Everything else is one tick away in the
 *  filter panel -- opening on all nine is a wall of unreadable cards. */
const DEFAULT_MODULES = ["Screen", "Content", "Playlist", "Schedule", "Channel"];

type NodeData = { node: NavNode; selected: boolean };

function StateNode({ data }: NodeProps) {
  const { node } = data as unknown as NodeData;
  const tone = node.node_type === "page" ? moduleTone(node.module) : NODE_TYPE_TONE[node.node_type] ?? "muted";
  const unexercised = node.not_exercised_total ?? 0;

  return (
    <div
      className="w-[214px] rounded-[10px] border px-[11px] py-[9px] transition-colors"
      style={{
        background: node.is_entry ? wash("accent", 0.1) : "var(--qg-card)",
        borderColor: node.is_entry ? TONE_HEX.accent : wash(tone, 0.45),
        borderStyle: node.node_type === "boundary" ? "dashed" : "solid",
      }}
    >
      <Handle type="target" position={Position.Top} />
      <div className="mb-[5px] flex items-center gap-[6px]">
        <span className="font-mono text-[10px]" style={{ color: TONE_HEX[tone] }}>
          {node.id}
        </span>
        {node.is_entry && (
          <span className="font-mono text-[9px] text-accent">entry</span>
        )}
        <div className="grow" />
        {unexercised > 0 && (
          <span
            className="rounded px-[5px] py-[1px] font-mono text-[9px]"
            style={{ background: wash("amber", 0.16), color: TONE_HEX.amber }}
            title={`${unexercised} actionable controls were never exercised`}
          >
            {unexercised}
          </span>
        )}
      </div>
      <div className="truncate text-[12px] font-medium text-ink">{titleOf(node)}</div>
      <div className="truncate font-mono text-[9.5px] text-ink-4">{pathOf(node.url)}</div>
      <div className="mt-[6px] flex items-center gap-[7px]">
        <Dot tone={tone} size={6} />
        <span className="text-[9.5px] text-ink-4">
          {node.node_type} · {node.actionable_count} actionable
        </span>
      </div>
      <Handle type="source" position={Position.Bottom} />
    </div>
  );
}

function BandNode({ data }: NodeProps) {
  const { module, count, width } = data as unknown as {
    module: string;
    count: number;
    width: number;
  };
  const tone = moduleTone(module);
  return (
    <div style={{ width }} className="pointer-events-none select-none">
      <div className="mb-[6px] flex items-baseline gap-2">
        <span className="font-display text-[13px] font-semibold" style={{ color: TONE_HEX[tone] }}>
          {module}
        </span>
        <span className="font-mono text-[10.5px] text-ink-4">{count} states</span>
      </div>
      <div className="h-[2px] rounded-full" style={{ background: wash(tone, 0.35) }} />
    </div>
  );
}

const nodeTypes = { state: StateNode, band: BandNode };

export function Explorer() {
  const navigate = useNavigate();
  const [graph, setGraph] = useState<Graph | null>(null);
  const [states, setStates] = useState<StateRec[] | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [modules, setModules] = useState<Set<string>>(new Set());
  const [types, setTypes] = useState<Set<string>>(new Set());
  const [onlyGaps, setOnlyGaps] = useState(false);
  const [query, setQuery] = useState("");

  useEffect(() => {
    api.graph().then((g) => {
      setGraph(g);
      setSelected(g.entry_node || g.nodes[0]?.id || null);
      const all = new Set(g.nodes.map((n) => n.module));
      const focus = DEFAULT_MODULES.filter((m) => all.has(m));
      setModules(new Set(focus.length >= 2 ? focus : all));
      setTypes(new Set(g.nodes.map((n) => n.node_type)));
    });
    api.states().then(setStates).catch(() => undefined);
  }, []);

  const moduleCounts = useMemo(() => {
    const m = new Map<string, number>();
    graph?.nodes.forEach((n) => m.set(n.module, (m.get(n.module) ?? 0) + 1));
    return [...m.entries()].sort((a, b) => b[1] - a[1]);
  }, [graph]);

  const typeCounts = useMemo(() => {
    const m = new Map<string, number>();
    graph?.nodes.forEach((n) => m.set(n.node_type, (m.get(n.node_type) ?? 0) + 1));
    return [...m.entries()].sort((a, b) => b[1] - a[1]);
  }, [graph]);

  const visible = useMemo(() => {
    if (!graph) return [];
    const q = query.trim().toLowerCase();
    return graph.nodes.filter((n) => {
      if (!modules.has(n.module)) return false;
      if (!types.has(n.node_type)) return false;
      if (onlyGaps && (n.not_exercised_total ?? 0) === 0) return false;
      if (q && !(`${n.id} ${n.title} ${n.url}`.toLowerCase().includes(q))) return false;
      return true;
    });
  }, [graph, modules, types, onlyGaps, query]);

  const { flowNodes, flowEdges } = useMemo(() => {
    const ids = new Set(visible.map((n) => n.id));

    // One block per module, laid left to right. A module with more states than
    // ROWS_PER_COL wraps into sub-columns rather than running off the canvas,
    // which is what made Settings a 25-node vertical ribbon.
    const byModule = new Map<string, NavNode[]>();
    visible.forEach((n) => {
      if (!byModule.has(n.module)) byModule.set(n.module, []);
      byModule.get(n.module)!.push(n);
    });

    const pos = new Map<string, { x: number; y: number }>();
    const bands: { module: string; x: number; w: number }[] = [];
    let cursor = 0;
    for (const [mod, list] of byModule) {
      const subCols = Math.max(1, Math.ceil(list.length / ROWS_PER_COL));
      list.forEach((n, i) => {
        pos.set(n.id, {
          x: cursor + Math.floor(i / ROWS_PER_COL) * COL_W,
          y: (i % ROWS_PER_COL) * ROW_H,
        });
      });
      bands.push({ module: mod, x: cursor, w: subCols * COL_W - 22 });
      cursor += subCols * COL_W + MODULE_GAP;
    }

    const nodes: Node[] = [
      ...bands.map((b) => ({
        id: `band-${b.module}`,
        type: "band",
        position: { x: b.x, y: -54 },
        data: { module: b.module, count: byModule.get(b.module)!.length, width: b.w },
        draggable: false,
        selectable: false,
      })),
      ...visible.map((n) => ({
        id: n.id,
        type: "state",
        position: pos.get(n.id) ?? { x: 0, y: 0 },
        data: { node: n, selected: n.id === selected },
        selected: n.id === selected,
      })),
    ];

    const edges: Edge[] = (graph?.edges ?? [])
      .filter((e) => ids.has(e.source) && ids.has(e.target) && e.source !== e.target)
      .slice(0, 400)
      .map((e) => ({
        id: e.id,
        source: e.source,
        target: e.target,
        style: {
          stroke: wash(OUTCOME_TONE[e.outcome] ?? "muted", 0.5),
          strokeWidth: 1.1,
        },
      }));

    return { flowNodes: nodes, flowEdges: edges };
  }, [visible, graph, selected]);

  const node = graph?.nodes.find((n) => n.id === selected) ?? null;
  const state = states?.find((s) => s.fingerprint === node?.fingerprint) ?? null;
  const route = (node && graph?.paths[node.id]) || [];

  const toggle = useCallback((set: Set<string>, key: string, apply: (s: Set<string>) => void) => {
    const next = new Set(set);
    if (next.has(key)) next.delete(key);
    else next.add(key);
    apply(next);
  }, []);

  return (
    <div className="flex min-w-0 grow flex-col overflow-hidden">
      <header className="flex h-[62px] shrink-0 items-center gap-4 border-b border-line-soft px-[22px]">
        <div>
          <h1 className="font-display text-[18px] leading-none font-semibold tracking-[-0.2px]">
            Navigation graph
          </h1>
          <div className="mt-[3px] text-[11.5px] text-ink-4">
            {num(graph?.nodes.length ?? 0)} of {num(graph?.total_nodes ?? 0)} states ·{" "}
            {num(flowEdges.length)} transitions shown
          </div>
        </div>
        <div className="grow" />
        <div className="relative w-[250px]">
          <input
            type="search"
            aria-label="Search states"
            placeholder="Search title, URL or id"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="h-10 w-full rounded-[9px] border border-line-strong bg-surface pr-3 pl-[34px] text-[12.5px] text-ink outline-none focus:border-accent-line"
          />
          <span className="pointer-events-none absolute top-[12px] left-[11px]">
            <Icon name="search" size={15} color={C.ink4} strokeWidth={2} />
          </span>
        </div>
        <Button>
          <Icon name="download" size={14} />
          Export
        </Button>
      </header>

      <div className="flex min-h-0 grow">
        {/* filters */}
        <aside className="w-[208px] shrink-0 overflow-y-auto border-r border-line-soft px-4 py-[18px]">
          <FilterGroup title="MODULE">
            {moduleCounts.map(([m, n]) => (
              <FilterRow
                key={m}
                label={m}
                count={n}
                tone={moduleTone(m)}
                checked={modules.has(m)}
                onChange={() => toggle(modules, m, setModules)}
              />
            ))}
          </FilterGroup>

          <FilterGroup title="STATE TYPE">
            {typeCounts.map(([t, n]) => (
              <FilterRow
                key={t}
                label={t}
                count={n}
                checked={types.has(t)}
                onChange={() => toggle(types, t, setTypes)}
              />
            ))}
          </FilterGroup>

          <FilterGroup title="COVERAGE">
            <label className="flex cursor-pointer items-start gap-[9px] py-[5px]">
              <input
                type="checkbox"
                checked={onlyGaps}
                onChange={(e) => setOnlyGaps(e.target.checked)}
                className="mt-[2px] h-[14px] w-[14px] accent-amber"
              />
              <span className="text-[12.5px] leading-[1.4] text-ink-body">
                Has unexercised controls
              </span>
            </label>
          </FilterGroup>
        </aside>

        {/* canvas */}
        <div className="relative min-w-0 grow bg-canvas">
          {graph ? (
            <ReactFlow
              nodes={flowNodes}
              edges={flowEdges}
              nodeTypes={nodeTypes}
              onNodeClick={(_, n) => setSelected(n.id)}
              fitView
              fitViewOptions={{ padding: 0.14, maxZoom: 0.9 }}
              minZoom={0.08}
              maxZoom={1.6}
              proOptions={{ hideAttribution: true }}
            >
              <Background variant={BackgroundVariant.Dots} gap={26} size={1} color="var(--qg-canvas-dot)" />
              <Controls showInteractive={false} />
              {/* No minimap: the module bands plus Controls are enough to navigate,
                  and an empty inset box reads as a broken panel. */}
            </ReactFlow>
          ) : (
            <Empty>Loading the graph…</Empty>
          )}

          {route.length > 1 && (
            <div
              className="absolute bottom-[18px] left-[18px] max-w-[420px] rounded-[10px] border px-[14px] py-[11px]"
              style={{ background: wash("accent", 0.09), borderColor: wash("accent", 0.32) }}
            >
              <div className="mb-[6px] text-[11px] font-semibold tracking-[0.4px] text-accent">
                SHORTEST PATH FROM ENTRY · {route.length - 1} STEPS
              </div>
              <div className="font-mono text-[11.5px] leading-[1.6] text-ink-body">
                {route.join(" → ")}
              </div>
              <div className="mt-[5px] text-[11px] text-accent-ink">
                Every edge carries a locator that resolved to exactly one element at capture time.
              </div>
            </div>
          )}
        </div>

        {/* inspector */}
        <aside className="flex w-[358px] shrink-0 flex-col overflow-hidden border-l border-line-soft bg-aside">
          {node ? (
            <>
              <div className="border-b border-line-soft px-[18px] pt-4 pb-[14px]">
                <div className="mb-[9px] flex flex-wrap items-center gap-[7px]">
                  <Tag tone={NODE_TYPE_TONE[node.node_type] ?? "muted"}>{node.id}</Tag>
                  <Tag>{node.node_type}</Tag>
                  <Tag>depth {node.depth}</Tag>
                  <Tag tone={moduleTone(node.module)}>{node.module}</Tag>
                </div>
                <h2 className="font-display mb-1 text-[16px] font-semibold">{titleOf(node)}</h2>
                <div className="truncate font-mono text-[11px] text-ink-4">
                  {pathOf(node.url)}
                  {node.opened_by ? ` · opened by “${node.opened_by}”` : ""}
                </div>
              </div>

              <div className="px-[18px] pt-[14px]">
                <div className="relative h-[168px] overflow-hidden rounded-[9px] border border-line bg-well">
                  {shotUrl(state?.screenshot ?? node.screenshot) ? (
                    <img
                      src={shotUrl(state?.screenshot ?? node.screenshot)!}
                      alt={`Capture of ${titleOf(node)}`}
                      className="w-full"
                      style={{ objectFit: "cover", objectPosition: "top" }}
                    />
                  ) : (
                    <Empty>No capture for this state.</Empty>
                  )}
                </div>
              </div>

              <div className="grid grid-cols-3 gap-[10px] px-[18px] py-[14px]">
                {[
                  ["actionable", node.actionable_count, "ink"],
                  ["exercised", node.actions_total ?? 0, "accent"],
                  ["not exercised", node.not_exercised_total ?? 0, "amber"],
                ].map(([k, v, tone]) => (
                  <div
                    key={k as string}
                    className="rounded-[9px] border border-rail-line bg-surface p-[10px]"
                  >
                    <div
                      className="font-display text-[19px] leading-none font-semibold tabular-nums"
                      style={{ color: TONE_HEX[tone as "ink"] }}
                    >
                      {num(v as number)}
                    </div>
                    <div className="mt-[3px] text-[10.5px] leading-[1.3] text-ink-4">
                      {k as string}
                    </div>
                  </div>
                ))}
              </div>

              <div className="min-h-0 grow overflow-y-auto px-[18px]">
                <PanelTitle>WHAT A TESTER CAN DO HERE</PanelTitle>
                <div className="mt-2">
                  {node.actions.slice(0, 24).map((line, i) => {
                    const kind = line.split(":")[0];
                    const rest = line.slice(kind.length + 1).trim();
                    return (
                      <div
                        key={i}
                        className="flex items-center gap-[9px] border-b border-line-soft py-[6px]"
                      >
                        <Dot tone={kind.includes("input") || kind === "select" ? "blue" : "accent"} />
                        <span className="grow truncate text-[12px] text-ink-body" title={rest}>
                          {rest.split("[")[0].trim() || "(unnamed)"}
                        </span>
                        <span className="shrink-0 font-mono text-[10px] text-ink-4">{kind}</span>
                      </div>
                    );
                  })}
                  {node.actions.length === 0 && (
                    <div className="py-4 text-[12px] text-ink-4">
                      Nothing actionable was extracted from this state.
                    </div>
                  )}
                </div>

                {state && state.blocked_mutations.length > 0 && (
                  <div className="mt-4 mb-4">
                    <PanelTitle>WRITES BLOCKED HERE</PanelTitle>
                    <div className="mt-2">
                      {state.blocked_mutations.map((m) => (
                        <div
                          key={m}
                          className="truncate border-b border-line-soft py-[6px] font-mono text-[10.5px]"
                          style={{ color: TONE_HEX.violet }}
                          title={m}
                        >
                          {m}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              <div className="flex gap-[9px] border-t border-line-soft px-[18px] pt-[13px] pb-4">
                <Button
                  variant="primary"
                  className="grow"
                  onClick={() => navigate(`/cases?state=${node.id}`)}
                >
                  View test cases
                </Button>
                <IconButton icon="ext" label="Open raw capture" size={42} />
              </div>
            </>
          ) : (
            <Empty>Select a state to inspect it.</Empty>
          )}
        </aside>
      </div>
    </div>
  );
}

function FilterGroup({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="mb-5">
      <div className="mb-[10px] text-[10.5px] font-semibold tracking-[0.6px] text-ink-4">
        {title}
      </div>
      {children}
    </div>
  );
}

function FilterRow({
  label,
  count,
  tone,
  checked,
  onChange,
}: {
  label: string;
  count: number;
  tone?: ReturnType<typeof moduleTone>;
  checked: boolean;
  onChange: () => void;
}) {
  return (
    <label className="flex cursor-pointer items-center gap-[9px] py-[5px]">
      <input
        type="checkbox"
        checked={checked}
        onChange={onChange}
        className="h-[14px] w-[14px] accent-accent"
      />
      {tone && (
        <span
          className="block h-[9px] w-[9px] shrink-0 rounded-[2px]"
          style={{ background: TONE_HEX[tone] }}
        />
      )}
      <span className="grow truncate text-[12.5px] text-ink-body">{label}</span>
      <span className="font-mono text-[11px] text-ink-4">{count}</span>
    </label>
  );
}

