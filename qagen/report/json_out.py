"""JSON renderers -- full fidelity, including provenance."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..models import PageModel, TestSuite


def write_suite(suite: TestSuite, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "test-cases.json"
    path.write_text(suite.model_dump_json(indent=2), encoding="utf-8")
    return path


def write_page_models(pages: list[PageModel], out_dir: Path) -> list[Path]:
    """Raw PageModel per state -- the debugging record behind every test case."""
    target = out_dir / "pages"
    target.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for page in pages:
        name = page.fingerprint or f"page{len(written):03d}"
        path = target / f"{name}.json"
        path.write_text(page.model_dump_json(indent=2), encoding="utf-8")
        written.append(path)
    return written


def write_manifest(manifest: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "run_manifest.json"
    path.write_text(json.dumps(manifest, indent=2, default=str), encoding="utf-8")
    return path
