/** Mirrors the Pydantic models in qagen/models.py. When the FastAPI service
 *  lands, generate this file from its OpenAPI schema instead of hand-editing. */

export type Outcome =
  | "no_change"
  | "in_page_state"
  | "navigation"
  | "new_tab"
  | "native_dialog"
  | "file_chooser"
  | "download"
  | "blocked_mutation"
  | "error";

export type NodeType =
  | "page"
  | "modal"
  | "drawer"
  | "dropdown"
  | "panel"
  | "boundary"
  | "external";

export type Category =
  | "Happy Path"
  | "Negative"
  | "Edge Case"
  | "UI/UX"
  | "Form Filling";

export interface NavNode {
  id: string;
  fingerprint: string;
  url: string;
  normalized_url: string;
  title: string;
  depth: number;
  node_type: NodeType;
  module: string;
  element_count: number;
  actionable_count: number;
  main_actionable_count: number;
  dom_nodes: number;
  is_entry: boolean;
  visit_count: number;
  screenshot: string | null;
  actions: string[];
  actions_total: number;
  not_exercised: string[];
  not_exercised_total: number;
  parent_state: string | null;
  opened_by: string | null;
}

export interface NavEdge {
  id: string;
  source: string;
  target: string;
  action: string;
  label: string;
  selector: string;
  element_role: string;
  element_name: string;
  outcome: Outcome;
  annotations: string[];
  reversible_by: string;
}

export interface Graph {
  target: string;
  generated_at: string;
  entry_node: string;
  total_nodes: number;
  total_edges: number;
  nodes: NavNode[];
  edges: NavEdge[];
  paths: Record<string, string[]>;
  module_tone: Record<string, string>;
}

export interface ElementRec {
  kind: string;
  role: string;
  name: string;
  selector: string;
  region: "shell" | "main";
  location: string;
  enabled: boolean;
  x: number;
  y: number;
  w: number;
  h: number;
}

export interface StateRec {
  fingerprint: string;
  url: string;
  normalized_url: string;
  title: string;
  module: string;
  depth: number;
  arrival_action: string;
  viewport_width: number;
  viewport_height: number;
  document_height: number;
  dom_nodes: number;
  screenshot: string | null;
  blocked_mutations: string[];
  console_errors: string[];
  elements: ElementRec[];
}

export interface Step {
  step_number: number;
  action: string;
  expected_result: string;
}

export interface TestCase {
  test_id: string;
  category: Category;
  title: string;
  preconditions: string[];
  steps: Step[];
  overall_expected_result: string;
  source_state: string;
  source_fingerprint: string;
  source_url: string;
  module: string;
  source_selectors: string[];
  highlight: { x: number; y: number; w: number; h: number; label: string } | null;
  highlight_valid: boolean;
  reachability: string[];
  needs_review: boolean;
  review_notes: string[];
  constraints: { k: string; v: string }[];
}

/** One line of crawl-log.jsonl. Written by qagen/browser/actionlog.py. */
export interface LogEvent {
  t: number;
  event: string;
  detail: string;
  node?: string;
  url?: string;
  elements?: number;
  forms?: number;
  depth?: number;
  kind?: string;
  name?: string;
  selector?: string;
  outcome?: string;
  annotations?: string[];
  seconds?: number;
  reason?: string;
  element?: string;
  ok?: boolean;
  how?: string;
  [k: string]: unknown;
}

export interface RunSummary {
  id: string;
  target: string;
  status: "running" | "paused" | "finished" | "stopped";
  started_at: string;
  duration_seconds: number;
  auth_status: string;
  states_discovered: number;
  graph_nodes: number;
  graph_edges: number;
  actionable_elements: number;
  total_elements: number;
  blocked_mutations: string[];
  skipped_elements: { url: string; element: string; reason: string }[];
  budgets: {
    pages_visited: number;
    navigations: number;
    max_pages: number;
    clicks_made: number;
    max_clicks: number;
    elapsed_seconds: number;
    max_wall_clock_seconds: number;
    consecutive_no_new_states: number;
    stop_reason: string | null;
  };
  module_budgets: Record<string, number>;
  module_states: Record<string, number>;
  config: {
    depth: number;
    headless: boolean;
    block_mutations: boolean;
    model: string;
    deny_text: string[];
  };
}
