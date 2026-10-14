"""Regression tests for the installed server entry point."""

from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path


SERVER_ROOT = Path(__file__).resolve().parents[1]


def test_help_starts_with_mcp_v2() -> None:
    """The CLI must import and parse arguments without a Riot API request."""
    result = subprocess.run(
        [sys.executable, "main.py", "--help"],
        cwd=SERVER_ROOT,
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert "League MCP Server" in result.stdout
    assert "--transport" in result.stdout


def test_main_registers_tools_and_resources(monkeypatch) -> None:
    """MCP v2 preserves the server's decorator-based registrations."""
    import main

    monkeypatch.setattr(sys, "argv", ["league-mcp", "--transport", "stdio"])
    monkeypatch.setattr(main.mcp, "run", lambda **kwargs: None)

    main.main()

    tool_names = {tool.name for tool in asyncio.run(main.mcp.list_tools())}
    resource_uris = {str(resource.uri) for resource in asyncio.run(main.mcp.list_resources())}
    assert "get_account_by_puuid" in tool_names
    assert "ddragon://versions" in resource_uris
