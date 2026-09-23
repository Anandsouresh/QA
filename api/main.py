"""QAGen control-room API.

Wraps the existing `qagen` package without changing how it works: a run is the
CLI in a subprocess, its directory is its database, and control is the sentinel
files in qagen/control.py. Restarting this service never kills a crawl.

    uvicorn api.main:app --reload --port 8000
"""

from __future__ import annotations

import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, AsyncIterator, Literal

import yaml
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qagen.config import RunConfig  # noqa: E402
from qagen.control import clear_all, clear_pause, request_pause, request_stop  # noqa: E402
from qagen.discover import discover_modules, suggest_budgets  # noqa: E402

from .store import REPO_ROOT, RUNS_DIR, RunStore, next_run_id, pid_alive  # noqa: E402

app = FastAPI(title="QAGen Control Room", version="0.1.0")
# Any loopback port, not a fixed list. Vite's dev server moves to 5174, 5175 and
# so on whenever the previous port is busy, and a hardcoded allowlist turns that
# ordinary event into a wall of CORS failures. This service binds localhost and
# carries no credentials, so the loopback host is the real boundary; put an auth
# layer in front and narrow this before exposing it anywhere else.
LOCAL_ORIGIN = r"^https?://(localhost|127\.0\.0\.1|\[::1\])(:\d+)?$"

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=LOCAL_ORIGIN,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

store = RunStore()


# ── request models ────────────────────────────────────────────────────────


class AuthPayload(BaseModel):
    """The session token for the TARGET site.

    Either a Playwright storage_state object or a raw cookie array exported by
    a browser extension; qagen detects which by shape. Pasted as text so the
    browser never has to hand us a file path.
    """

    storage_state: str | None = Field(default=None, description="JSON text")
    verify_selector: str | None = None


class ProbeRequest(BaseModel):
    url: str
    auth: AuthPayload = Field(default_factory=AuthPayload)
    total_states: int = 200


class StartRequest(BaseModel):
    url: str
    depth: int = 20
    #: module name -> state budget. Only these modules are crawled.
    modules: dict[str, int] = Field(default_factory=dict)
    auth: AuthPayload = Field(default_factory=AuthPayload)
    #: Never written to disk; passed to the child process environment only.
    anthropic_key: str | None = None
    generate: bool = True
    headless: bool = True
    max_wall_clock_seconds: int = 86400
    label: str = ""


# ── helpers ───────────────────────────────────────────────────────────────


def _write_auth(run_dir: Path, auth: AuthPayload) -> Path | None:
    if not auth.storage_state or not auth.storage_state.strip():
        return None
    try:
        parsed = json.loads(auth.storage_state)
    except json.JSONDecodeError as exc:
        raise HTTPException(400, f"auth.storage_state is not valid JSON: {exc}") from exc

    secrets = run_dir / "secrets"
    secrets.mkdir(parents=True, exist_ok=True)
    path = secrets / "auth.json"
    path.write_text(json.dumps(parsed), encoding="utf-8")
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass  # best effort; Windows ACLs do not map onto this
    return path


def _build_config(req: StartRequest, run_dir: Path, auth_path: Path | None) -> dict:
    """Turn a UI request into the same YAML a CLI user would hand-write."""
    modules = {k: int(v) for k, v in req.modules.items() if int(v) > 0}
    include: list[str] = []
    for name in modules:
        if name.lower() in {"(home)", "home"}:
            continue
        slug = name.strip("/").lower()
        include += [f"/{slug}", f"/{slug}/*"]

    cfg: dict[str, Any] = {
        "target": {
            "url": req.url,
            "depth": req.depth,
            "same_origin_only": True,
            "exclude_paths": ["/logout", "/signout", "/login", "/auth/**"],
        },
        "auth": {},
        "crawl": {
            "max_pages": sum(modules.values()) or 25,
            "max_wall_clock_seconds": req.max_wall_clock_seconds,
            "module_budgets": modules,
            "max_states_per_section": max(modules.values()) if modules else 12,
        },
        "output": {
            "dir": str(run_dir),
            "formats": ["markdown", "json", "xlsx", "graph"] if req.generate else ["graph"],
            "save_page_models": True,
            "action_log": True,
        },
        "browser": {"headless": req.headless, "block_mutations": True},
    }
    # An empty include_paths means "the whole origin". Only narrow the scope
    # when the user actually deselected something.
    if include:
        cfg["target"]["include_paths"] = include
    if auth_path:
        cfg["auth"]["storage_state"] = str(auth_path)
    if req.auth.verify_selector:
        cfg["auth"]["verify_selector"] = req.auth.verify_selector
    return cfg


async def _probe_config(url: str, auth: AuthPayload, tmp: Path) -> RunConfig:
    auth_path = _write_auth(tmp, auth)
    data: dict[str, Any] = {
        "target": {"url": url, "depth": 0},
        "auth": {},
        "output": {"dir": str(tmp), "action_log": False, "save_page_models": False,
                   "save_screenshots": False, "save_html": False},
        "browser": {"headless": True, "block_mutations": True},
    }
    if auth_path:
        data["auth"]["storage_state"] = str(auth_path)
    if auth.verify_selector:
        data["auth"]["verify_selector"] = auth.verify_selector
    return RunConfig.model_validate(data)


def _run_dir(run_id: str) -> Path:
    run = store.get(run_id)
    if run is None:
        raise HTTPException(404, f"no run {run_id!r}")
    return run.run_dir


def _read_json(path: Path, default: Any = None) -> Any:
    """Missing is not an error while a run is still working.

    A crawl writes navgraph.json at the end, so asking for it ten minutes in is
    a normal thing a client does. Returning 404 would push that special case
    into every caller; an empty but valid payload with `ready: false` does not.
    """
    if not path.exists():
        if default is None:
            raise HTTPException(404, f"{path.name} not written yet")
        return default
    return json.loads(path.read_text(encoding="utf-8"))


# ── meta ──────────────────────────────────────────────────────────────────


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "runs_dir": str(RUNS_DIR), "repo": str(REPO_ROOT)}


@app.get("/api/config/schema")
def config_schema() -> dict:
    """The whole RunConfig schema, so the UI never drifts from qagen/config.py."""
    return RunConfig.model_json_schema()


# ── preflight ─────────────────────────────────────────────────────────────


@app.post("/api/preflight/auth")
async def preflight_auth(req: ProbeRequest) -> dict:
    """Prove the session is live before anyone pays for a crawl."""
    from qagen.browser.session import AuthError, Session

    tmp = RUNS_DIR / "_preflight"
    tmp.mkdir(parents=True, exist_ok=True)
    try:
        cfg = await _probe_config(req.url, req.auth, tmp)
    except Exception as exc:
        return {"ok": False, "code": "CONFIG_ERROR", "detail": str(exc)}

    try:
        async with Session(cfg) as session:
            await session.verify_auth()
            page = session.page
            assert page is not None
            return {
                "ok": True,
                "landed_on": page.url,
                "title": await page.title(),
                "used_storage_state": bool(cfg.auth.storage_state),
            }
    except AuthError as exc:
        return {"ok": False, "code": "AUTH_FAILED", "detail": str(exc)}
    except Exception as exc:
        return {"ok": False, "code": "BROWSER_ERROR", "detail": str(exc)}


@app.post("/api/preflight/modules")
async def preflight_modules(req: ProbeRequest) -> dict:
    """Group everything the entry page links to by first path segment."""
    tmp = RUNS_DIR / "_preflight"
    tmp.mkdir(parents=True, exist_ok=True)
    cfg = await _probe_config(req.url, req.auth, tmp)
    try:
        found = await discover_modules(cfg)
    except Exception as exc:
        raise HTTPException(502, f"probe failed: {exc}") from exc
    found["suggested_budgets"] = suggest_budgets(found["modules"], req.total_states)
    return found


# ── runs ──────────────────────────────────────────────────────────────────


@app.get("/api/runs")
def list_runs() -> list[dict]:
    return [r.as_dict() for r in store.list()]


@app.post("/api/runs")
def start_run(req: StartRequest) -> dict:
    run_id = next_run_id(req.url, [r.id for r in store.list()])
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    auth_path = _write_auth(run_dir, req.auth)
    cfg_data = _build_config(req, run_dir, auth_path)

    try:
        RunConfig.model_validate(cfg_data)      # fail before spawning a browser
    except Exception as exc:
        raise HTTPException(400, f"invalid configuration: {exc}") from exc

    cfg_path = run_dir / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg_data, sort_keys=False), encoding="utf-8")
    clear_all(run_dir)

    env = dict(os.environ)
    env["PYTHONPATH"] = str(REPO_ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONUNBUFFERED"] = "1"
    if req.anthropic_key:
        # Deliberately not persisted: it reaches the child through the
        # environment and never touches the run directory.
        env["ANTHROPIC_API_KEY"] = req.anthropic_key

    command = "run" if req.generate else "crawl"
    argv = [sys.executable, "-m", "qagen.cli", command, "--config", str(cfg_path)]

    store.create(
        run_id=run_id,
        target=req.url,
        run_dir=run_dir,
        mode="full" if req.generate else "crawl-only",
        modules=req.modules,
        max_states=cfg_data["crawl"]["max_pages"],
        label=req.label,
    )

    stdout = (run_dir / "console.log").open("w", encoding="utf-8")
    proc = subprocess.Popen(
        argv, cwd=str(REPO_ROOT), env=env,
        stdout=stdout, stderr=subprocess.STDOUT,
    )
    store.set_pid(run_id, proc.pid)

    return {
        "id": run_id,
        "pid": proc.pid,
        "run_dir": str(run_dir),
        "command": " ".join(argv[1:]),
        "max_states": cfg_data["crawl"]["max_pages"],
        "modules": req.modules,
    }


@app.get("/api/runs/{run_id}")
def get_run(run_id: str) -> dict:
    run = store.get(run_id)
    if run is None:
        raise HTTPException(404, f"no run {run_id!r}")
    out = run.as_dict()
    manifest = run.run_dir / "run_manifest.json"
    out["manifest"] = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else None
    out["alive"] = pid_alive(run.pid)
    return out


@app.post("/api/runs/{run_id}/stop")
def stop_run(run_id: str) -> dict:
    run_dir = _run_dir(run_id)
    request_stop(run_dir)
    store.set_status(run_id, "stopping")
    return {
        "ok": True,
        "note": "The crawl finishes its current state, then writes everything "
                "it captured. Nothing is discarded.",
    }


@app.post("/api/runs/{run_id}/pause")
def pause_run(run_id: str) -> dict:
    request_pause(_run_dir(run_id))
    store.set_status(run_id, "paused")
    return {"ok": True}


@app.post("/api/runs/{run_id}/resume")
def resume_run(run_id: str) -> dict:
    clear_pause(_run_dir(run_id))
    store.set_status(run_id, "running")
    return {"ok": True}


@app.delete("/api/runs/{run_id}")
def delete_run(run_id: str) -> dict:
    run = store.get(run_id)
    if run is None:
        raise HTTPException(404, f"no run {run_id!r}")
    if pid_alive(run.pid):
        raise HTTPException(409, "that run is still going; stop it first")
    import shutil

    shutil.rmtree(run.run_dir, ignore_errors=True)
    store.delete(run_id)
    return {"ok": True}


# ── artefacts ─────────────────────────────────────────────────────────────


EMPTY_GRAPH: dict[str, Any] = {
    "target": "", "generated_at": "", "nodes": [], "edges": [],
    "entry_node": "", "boundaries": [], "unexplored": [], "ready": False,
}


@app.get("/api/runs/{run_id}/graph")
def get_graph(run_id: str) -> Any:
    run = store.get(run_id)
    if run is None:
        raise HTTPException(404, f"no run {run_id!r}")
    return _read_json(run.run_dir / "navgraph.json", {**EMPTY_GRAPH, "target": run.target})


@app.get("/api/runs/{run_id}/paths")
def get_paths(run_id: str) -> Any:
    return _read_json(_run_dir(run_id) / "navgraph-paths.json", {})


@app.get("/api/runs/{run_id}/states")
def get_states(run_id: str) -> list[dict]:
    pages = _run_dir(run_id) / "pages"
    if not pages.exists():
        return []
    out = []
    for f in sorted(pages.glob("*.json")):
        out.append(json.loads(f.read_text(encoding="utf-8")))
    return out


@app.get("/api/runs/{run_id}/cases")
def get_cases(run_id: str) -> Any:
    """Empty until generation has run. A crawl-only run never fills it."""
    return _read_json(_run_dir(run_id) / "test-cases.json", {"cases": [], "ready": False})


@app.get("/api/runs/{run_id}/artifacts/{name}")
def get_artifact(run_id: str, name: str) -> FileResponse:
    if "/" in name or "\\" in name or ".." in name:
        raise HTTPException(400, "bad artifact name")
    path = _run_dir(run_id) / "artifacts" / name
    if not path.exists():
        raise HTTPException(404, name)
    return FileResponse(path)


@app.get("/api/runs/{run_id}/frame")
def latest_frame(run_id: str) -> FileResponse:
    """The most recent capture, as a stand-in for a live viewport.

    True 1-frame-per-second streaming needs a hook inside the crawl loop (see
    WEB_UI_BUILD_PROMPT.md, change 1). Until that exists, the newest screenshot
    the crawler has already written is real, current within a state, and costs
    nothing: no extra browser work and no new configuration.
    """
    artifacts = _run_dir(run_id) / "artifacts"
    if not artifacts.exists():
        raise HTTPException(404, "no captures yet")
    shots = sorted(artifacts.glob("*.png"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not shots:
        raise HTTPException(404, "no captures yet")
    return FileResponse(shots[0], headers={"Cache-Control": "no-store"})


@app.get("/api/runs/{run_id}/export/{fmt}")
def export(run_id: str, fmt: Literal["md", "json", "xlsx", "csv"]) -> FileResponse:
    names = {
        "md": "test-cases.md", "json": "test-cases.json",
        "xlsx": "test-cases.xlsx", "csv": "test-cases.csv",
    }
    path = _run_dir(run_id) / names[fmt]
    if not path.exists():
        raise HTTPException(404, f"{names[fmt]} was not written by this run")
    return FileResponse(path, filename=names[fmt])


# ── the live stream ───────────────────────────────────────────────────────


@app.get("/api/runs/{run_id}/events")
async def stream_events(run_id: str, from_byte: int = Query(0, ge=0)) -> StreamingResponse:
    """Server-Sent Events, by tailing crawl-log.jsonl.

    Tailing rather than an in-process hook, because the crawl is a separate
    process: this survives an API restart mid-run, and a client can replay the
    whole run from byte zero to rebuild its state.
    """
    run = store.get(run_id)
    if run is None:
        raise HTTPException(404, f"no run {run_id!r}")
    log_path = run.run_dir / "crawl-log.jsonl"

    async def generator() -> AsyncIterator[bytes]:
        offset = from_byte
        idle = 0.0
        yield b": connected\n\n"
        while True:
            if log_path.exists():
                with log_path.open("r", encoding="utf-8", errors="replace") as fh:
                    fh.seek(offset)
                    chunk = fh.read()
                    offset = fh.tell()
                if chunk:
                    idle = 0.0
                    for line in chunk.splitlines():
                        line = line.strip()
                        if not line:
                            continue
                        yield f"data: {line}\n\n".encode("utf-8")
                    yield f"event: offset\ndata: {offset}\n\n".encode("utf-8")
                else:
                    idle += 0.5
            else:
                idle += 0.5

            current = store.get(run_id)
            if current and not pid_alive(current.pid) and idle > 2.0:
                yield b"event: done\ndata: {}\n\n"
                return
            if idle > 15.0:
                yield b": keepalive\n\n"
                idle = 0.0
            await asyncio.sleep(0.5)

    return StreamingResponse(
        generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
