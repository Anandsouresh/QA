# Control-room API

HTTP in front of the `qagen` package. It adds no crawling logic of its own: a
run is the existing CLI in a subprocess, the run directory is its database, and
stopping is a sentinel file the crawl checks on its own schedule.

```bash
pip install -e ".[api]"
python -m playwright install chromium
uvicorn api.main:app --reload --port 8000
```

Runs land in `./runs/<id>/`, or wherever `QAGEN_RUNS_DIR` points.

---

## The three design decisions

**A run is a subprocess, not a task in this process.** A crawl holds a Chromium
instance for hours. Running it inside the API worker would mean a reload kills
four hours of work. The API spawns `python -m qagen.cli run --config …`, records
the pid, and can re-attach to it after a restart because liveness is derived
from the process table, never trusted from the database.

**Stopping is cooperative.** `POST /api/runs/{id}/stop` writes a `STOP` file.
The crawl notices on its next iteration, finishes the state it is on, and exits
through the normal path that writes the graph, the captures and the manifest.
Killing the process would throw away exactly the partial output the
orchestrator is built to preserve. `PAUSE` works the same way and is checked
between states, never mid-state, because pausing halfway through an action plan
would leave the page somewhere the restore logic cannot reason about.

**The event stream is a file tail.** `GET /api/runs/{id}/events` reads
`crawl-log.jsonl`, which `ActionLog` already flushes per line. Tailing rather
than hooking in-process means it works across the subprocess boundary, survives
an API restart mid-run, and lets a client replay from byte zero to rebuild the
whole picture.

---

## Endpoints

| | |
|---|---|
| `GET /api/health` | liveness, and where runs are stored |
| `GET /api/config/schema` | `RunConfig.model_json_schema()`, so a client never drifts from `qagen/config.py` |
| `POST /api/preflight/auth` | verify a session token against the target before anyone pays for a crawl |
| `POST /api/preflight/modules` | 40-second shallow probe; modules grouped by first path segment, with suggested budgets |
| `GET`/`POST` `/api/runs` | list, or start one |
| `GET /api/runs/{id}` | status plus the run manifest |
| `POST /api/runs/{id}/stop` `/pause` `/resume` | the sentinels |
| `DELETE /api/runs/{id}` | remove a finished run's directory |
| `GET /api/runs/{id}/events` | SSE; `?from_byte=` to replay |
| `GET /api/runs/{id}/graph` `/paths` `/states` `/cases` | the artefacts |
| `GET /api/runs/{id}/frame` | the newest capture, as a stand-in live viewport |
| `GET /api/runs/{id}/artifacts/{name}` | one screenshot or DOM dump |
| `GET /api/runs/{id}/export/{md,json,xlsx,csv}` | download |

`POST /api/runs` takes module names mapped to state budgets. Those become
`crawl.module_budgets`, their sum becomes `crawl.max_pages`, and the selected
names become `target.include_paths` globs, which is how deselecting a module
actually keeps the crawler out of it. The generated YAML is written to
`<run>/config.yaml`, so any run can be reproduced from the CLI.

**Not-yet-written is not an error.** A crawl writes `navgraph.json` at the end,
so asking for it ten minutes in is a normal thing a client does. Those
endpoints return an empty but valid payload with `ready: false` rather than a
404, which keeps the special case out of every caller.

---

## Secrets

Two arrive with a start request and they are handled differently on purpose.

The **session token** for the target site is written to
`<run>/secrets/auth.json` with 0600 where the platform honours it, because the
crawl subprocess needs a file path for `auth.storage_state`.

The **Anthropic API key** is never written to disk. It reaches the child
through its environment and nothing else.

Neither is echoed back by any endpoint. `runs/` should not be committed.

---

## What it does not do

No authentication, no multi-user separation, no TLS. It binds localhost and
assumes the person who can reach it is the person who owns the machine. Putting
it anywhere else needs an auth layer in front, and `allow_origins` in
`main.py` narrowed to the real front-end origin.
