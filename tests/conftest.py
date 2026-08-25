"""Shared fixtures.

The fixture app is served from a background thread on a free port, so the
integration tests are deterministic and fully offline -- no live target, no
network, safe for CI.

The crawl itself runs **once** per session (see ``crawled``). Re-crawling per
test turned a 30-second suite into an eight-minute one, and every assertion is
a read against the same result anyway.
"""

from __future__ import annotations

import asyncio
import functools
import http.server
import socket
import socketserver
import threading
from pathlib import Path

import pytest

FIXTURE_DIR = Path(__file__).parent / "fixture"


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args, **kwargs) -> None:  # noqa: D102
        pass

    def do_POST(self) -> None:  # the write-guard should abort before we see these
        self.send_response(200)
        self.end_headers()

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_POST


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


@pytest.fixture(scope="session")
def fixture_server():
    port = _free_port()
    handler = functools.partial(_QuietHandler, directory=str(FIXTURE_DIR))
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        server.shutdown()
        server.server_close()


def _build_config(base_url: str, out_dir: Path):
    from qagen.config import RunConfig

    return RunConfig.model_validate(
        {
            "target": {"url": f"{base_url}/index.html", "depth": 1},
            "crawl": {
                "max_pages": 12,
                "max_clicks": 60,
                # The fixture deliberately carries several same-page states off
                # index.html (modal, disclosure, card menu); the default cap of
                # 3 would drop whichever came last.
                "max_states_per_url": 8,
                "max_wall_clock_seconds": 150,
                "settle_timeout_ms": 900,
            },
            "llm": {"provider": "stub"},
            "output": {
                "dir": str(out_dir),
                "formats": ["markdown", "json", "xlsx", "csv", "graph"],
            },
        }
    )


@pytest.fixture
def run_config(fixture_server, tmp_path):
    """Fresh config with an isolated output dir, for the end-to-end test."""
    return _build_config(fixture_server, tmp_path / "out")


@pytest.fixture(scope="session")
def crawled(fixture_server, tmp_path_factory):
    """Crawl the fixture app exactly once; every integration test reads this.

    Driven with ``asyncio.run`` in a sync fixture rather than an async one --
    that keeps the whole thing independent of pytest-asyncio's fixture
    loop-scope rules, which are the usual source of "browser has been closed"
    errors in shared async fixtures.
    """
    from qagen.browser.crawler import Crawler
    from qagen.browser.session import Session

    cfg = _build_config(fixture_server, tmp_path_factory.mktemp("crawl"))

    async def _run():
        async with Session(cfg) as session:
            await session.verify_auth()
            crawler = Crawler(cfg, session)
            result = await crawler.run()
            return result, crawler.graph, crawler.budgets, cfg

    return asyncio.run(_run())
