"""CLI entry point.

Config errors are caught before a browser is ever launched -- a bad YAML value
must not cost a browser start.
"""

from __future__ import annotations

import asyncio
import os
import logging
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from .browser.session import AuthError
from .config import RunConfig
from .generation.from_disk import LoadError, load_crawl
from .orchestrator import Orchestrator

app = typer.Typer(add_completion=False, help="Generate QA test cases from a live URL.")
console = Console()


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)-7s %(name)-18s %(message)s",
    )
    logging.getLogger("asyncio").setLevel(logging.WARNING)


@app.command()
def run(
    url: Optional[str] = typer.Option(None, "--url", help="Target URL"),
    config: Optional[Path] = typer.Option(None, "--config", "-c", help="YAML config file"),
    depth: Optional[int] = typer.Option(None, "--depth", help="0 = single page only"),
    out: Optional[Path] = typer.Option(None, "--out", "-o", help="Output directory"),
    auth: Optional[Path] = typer.Option(None, "--auth", help="storage_state / cookie JSON"),
    provider: Optional[str] = typer.Option(None, "--provider", help="claude | stub"),
    model: Optional[str] = typer.Option(None, "--model", help="LLM model id"),
    module: Optional[str] = typer.Option(
        None, "--module",
        help="Restrict the crawl to one module (e.g. 'screen' -> /screen, /screen/*). "
        "Anything reached outside it is captured once and marked as a boundary, not explored.",
    ),
    headed: bool = typer.Option(False, "--headed", help="Run with a visible browser"),
    allow_mutations: bool = typer.Option(
        False,
        "--allow-mutations",
        help="DANGEROUS: disable the network write-guard. Never use on an "
        "environment you do not own.",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Crawl the target and generate test cases."""
    _setup_logging(verbose)

    overrides: dict[str, object] = {
        "target.url": url,
        "target.depth": depth,
        "output.dir": out,
        "auth.storage_state": auth,
        "llm.provider": provider,
        "llm.model": model,
        "browser.headless": False if headed else None,
        "browser.block_mutations": False if allow_mutations else None,
    }
    if module:
        overrides["target.include_paths"] = [f"/{module.strip('/')}", f"/{module.strip('/')}/*"]

    try:
        cfg = RunConfig.load(config, overrides)
    except Exception as exc:
        console.print(f"[bold red]Config error:[/] {exc}")
        raise typer.Exit(code=2)

    if allow_mutations:
        console.print(
            "[bold yellow]⚠ write-guard disabled.[/] The crawler can now send "
            "POST/PUT/PATCH/DELETE to the target."
        )

    console.print(f"[bold]Target:[/] {cfg.target.url}  [dim]depth={cfg.target.depth}[/]")
    if module:
        console.print(f"[bold]Module:[/] {module}  [dim]{cfg.target.include_paths}[/]")
    console.print(f"[bold]Provider:[/] {cfg.llm.provider} ({cfg.llm.model})")
    console.print(f"[bold]Output:[/] {cfg.output.dir}\n")

    try:
        manifest = asyncio.run(Orchestrator(cfg).run())
    except AuthError as exc:
        console.print(f"[bold red]{exc}[/]")
        raise typer.Exit(code=3)
    except KeyboardInterrupt:
        console.print("[yellow]Interrupted.[/]")
        raise typer.Exit(code=130)
    except Exception as exc:
        console.print(f"[bold red]Run failed:[/] {exc}")
        if verbose:
            console.print_exception()
        raise typer.Exit(code=1)

    _summary(manifest, cfg.output.dir)


def _summary(manifest: dict, out_dir: Path) -> None:
    crawl = manifest.get("crawl", {})
    generation = manifest.get("generation", {})
    budgets = crawl.get("budgets", {})

    table = Table(title="Run summary", show_header=False, box=None)
    table.add_row("States discovered", str(crawl.get("states_discovered", 0)))
    table.add_row("Graph", f"{crawl.get('graph_nodes', 0)} nodes / {crawl.get('graph_edges', 0)} edges")
    if crawl.get("actionable_elements") is not None:
        table.add_row(
            "Elements",
            f"{crawl['actionable_elements']} actionable / {crawl.get('total_elements', 0)} extracted",
        )
    table.add_row("Clicks made", str(budgets.get("clicks_made", 0)))
    table.add_row("Elements skipped", str(len(crawl.get("skipped_elements", []))))
    table.add_row("Mutations blocked", str(len(crawl.get("blocked_mutations", []))))
    if not generation.get("skipped"):
        table.add_row("Test cases", str(generation.get("cases_generated", 0)))
    needs = generation.get("cases_needing_review", 0)
    if needs:
        table.add_row("Needs review", f"[yellow]{needs}[/]")
    if budgets.get("stop_reason"):
        table.add_row("Stopped by", f"[yellow]{budgets['stop_reason']}[/]")
    table.add_row("Duration", f"{manifest.get('duration_seconds', 0)}s")
    console.print(table)

    usage = generation.get("usage") or {}
    if usage.get("calls"):
        cached = usage.get("cache_read_input_tokens", 0)
        console.print(
            f"\n[dim]LLM: {usage['calls']} calls, "
            f"{usage.get('input_tokens', 0)} in / {usage.get('output_tokens', 0)} out, "
            f"{cached} cached reads[/]"
        )

    for warning in (generation.get("warnings") or [])[:8]:
        console.print(f"[yellow]![/] {warning}")

    console.print(f"\n[green]Wrote output to[/] {out_dir}")


@app.command()
def crawl(
    url: Optional[str] = typer.Option(None, "--url", help="Target URL"),
    config: Optional[Path] = typer.Option(None, "--config", "-c", help="YAML config file"),
    depth: Optional[int] = typer.Option(None, "--depth", help="0 = single page only"),
    out: Optional[Path] = typer.Option(None, "--out", "-o", help="Output directory"),
    auth: Optional[Path] = typer.Option(None, "--auth", help="storage_state / cookie JSON"),
    module: Optional[str] = typer.Option(
        None, "--module",
        help="Restrict the crawl to one module (e.g. 'screen' -> /screen, /screen/*). "
        "Anything reached outside it is captured once and marked as a boundary, not explored.",
    ),
    headed: bool = typer.Option(False, "--headed", help="Run with a visible browser"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Crawl and build the navigation graph only -- no LLM, no API key needed."""
    _setup_logging(verbose)

    overrides: dict[str, object] = {
        "target.url": url,
        "target.depth": depth,
        "output.dir": out,
        "auth.storage_state": auth,
        "browser.headless": False if headed else None,
    }
    if module:
        overrides["target.include_paths"] = [f"/{module.strip('/')}", f"/{module.strip('/')}/*"]

    try:
        cfg = RunConfig.load(config, overrides)
    except Exception as exc:
        console.print(f"[bold red]Config error:[/] {exc}")
        raise typer.Exit(code=2)

    console.print(f"[bold]Target:[/] {cfg.target.url}  [dim]depth={cfg.target.depth}[/]")
    if module:
        console.print(f"[bold]Module:[/] {module}  [dim]{cfg.target.include_paths}[/]")
    console.print("[bold]Mode:[/] crawl + graph only (no test-case generation)")
    console.print(f"[bold]Output:[/] {cfg.output.dir}\n")

    try:
        manifest = asyncio.run(Orchestrator(cfg, generate=False).run())
    except AuthError as exc:
        console.print(f"[bold red]{exc}[/]")
        raise typer.Exit(code=3)
    except KeyboardInterrupt:
        console.print("[yellow]Interrupted.[/]")
        raise typer.Exit(code=130)
    except Exception as exc:
        console.print(f"[bold red]Run failed:[/] {exc}")
        if verbose:
            console.print_exception()
        raise typer.Exit(code=1)

    _summary(manifest, cfg.output.dir)
    _graph_detail(manifest, cfg.output.dir)


def _graph_detail(manifest: dict, out_dir: Path) -> None:
    """Print the discovered states -- for a crawl-only run this is the result,
    so it belongs on screen rather than only in a file."""
    import json

    graph_path = out_dir / "navgraph.json"
    if not graph_path.exists():
        return
    graph = json.loads(graph_path.read_text(encoding="utf-8"))

    table = Table(title="\nDiscovered states", show_lines=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Type")
    table.add_column("Title", max_width=34)
    table.add_column("URL", max_width=48)
    table.add_column("Main", justify="right")
    table.add_column("Act", justify="right")
    table.add_column("Intr", justify="right")
    table.add_column("DOM", justify="right")
    for node in graph.get("nodes", []):
        marker = " *" if node.get("is_entry") else ""
        table.add_row(
            node["id"] + marker,
            node.get("node_type", ""),
            (node.get("title") or "")[:34],
            node.get("normalized_url", "")[:48],
            str(node.get("main_actionable_count", 0)),
            str(node.get("actionable_count", 0)),
            str(node.get("element_count", 0)),
            str(node.get("dom_nodes", 0) or "-"),
        )
    console.print(table)
    total_act = sum(n.get("actionable_count", 0) for n in graph.get("nodes", []))
    total_main = sum(n.get("main_actionable_count", 0) for n in graph.get("nodes", []))
    console.print(
        "[dim]Main = actionable in the content area (excludes the header/left menu) "
        "· Act = all actionable · Intr = extracted · DOM = nodes on the page.[/]"
    )
    console.print(
        f"[dim]{len(graph.get('nodes', []))} states, "
        f"{len(graph.get('edges', []))} transitions, "
        f"{total_act} actionable elements ({total_main} outside the app frame). "
        f"Open navgraph.mmd in VS Code or GitHub to view the map.[/]"
    )


@app.command()
def generate(
    from_dir: Path = typer.Option(..., "--from", "-f", help="A finished crawl directory"),
    config: Optional[Path] = typer.Option(None, "--config", "-c", help="YAML config file"),
    out: Optional[Path] = typer.Option(None, "--out", "-o", help="Where to write (default: alongside the crawl)"),
    model: Optional[str] = typer.Option(None, "--model", help="Override llm.model"),
    cases: Optional[int] = typer.Option(None, "--cases", help="Max test cases per state"),
    formats: str = typer.Option(
        "markdown,json,xlsx,csv,graph", "--formats",
        help="Comma-separated output formats",
    ),
    stub: bool = typer.Option(False, "--stub", help="Dry run with no API key and no cost"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Generate test cases from a crawl that already ran -- no browser, no re-crawl.

    A crawl of a real app takes hours; generation takes minutes. Keeping them
    separate means the prompt, the model or the case format can change without
    paying for the capture again.
    """
    _setup_logging(verbose)

    overrides: dict[str, object] = {
        "output.dir": out or from_dir,
        "llm.model": model,
        "llm.max_cases_per_page": cases,
        "llm.provider": "stub" if stub else None,
        # A crawl-only config usually sets formats: [graph], which would write
        # the map and silently drop every test case.
        "output.formats": [f.strip() for f in formats.split(",") if f.strip()],
    }
    try:
        cfg = RunConfig.load(config, overrides)
    except Exception as exc:
        console.print(f"[bold red]Config error:[/] {exc}")
        raise typer.Exit(code=2)

    try:
        crawl_result = load_crawl(from_dir)
    except LoadError as exc:
        console.print(f"[bold red]Cannot read that crawl:[/] {exc}")
        raise typer.Exit(code=2)

    if not stub and cfg.llm.provider != "stub" and not os.environ.get("ANTHROPIC_API_KEY"):
        console.print(
            "[bold red]No ANTHROPIC_API_KEY set.[/] Export your key, or pass "
            "--stub for a free dry run that exercises the whole pipeline."
        )
        raise typer.Exit(code=2)

    console.print(f"[bold]Source:[/] {from_dir}  [dim]{len(crawl_result.pages)} states[/]")
    console.print(
        f"[bold]Provider:[/] {cfg.llm.provider}"
        + ("  [yellow](dry run -- no API calls, placeholder text)[/]" if cfg.llm.provider == "stub" else f"  [dim]{cfg.llm.model}[/]")
    )
    console.print(f"[bold]Output:[/] {cfg.output.dir}\n")

    try:
        manifest = asyncio.run(Orchestrator(cfg).generate_only(crawl_result))
    except KeyboardInterrupt:
        console.print("[yellow]Interrupted.[/]")
        raise typer.Exit(code=130)
    except Exception as exc:
        console.print(f"[bold red]Generation failed:[/] {exc}")
        if verbose:
            console.print_exception()
        raise typer.Exit(code=1)

    _summary(manifest, cfg.output.dir)


@app.command()
def validate_config(
    config: Path = typer.Argument(..., help="YAML config file to validate"),
) -> None:
    """Validate a config file without launching a browser."""
    try:
        cfg = RunConfig.load(config, {})
    except Exception as exc:
        console.print(f"[bold red]Invalid:[/] {exc}")
        raise typer.Exit(code=2)
    console.print("[green]Config is valid.[/]")
    console.print(f"  target   {cfg.target.url} (depth {cfg.target.depth})")
    console.print(f"  auth     {cfg.auth.storage_state or 'none'}")
    console.print(f"  provider {cfg.llm.provider} / {cfg.llm.model}")
    console.print(f"  formats  {', '.join(cfg.output.formats)}")


if __name__ == "__main__":
    app()
