"""
League MCP - Model Context Protocol server for League of Legends data.

This package provides access to League of Legends game data through the Riot Games API
via the Model Context Protocol (MCP). It supports multiple transport types for 
different integration scenarios.
"""

__version__ = "0.2.0"
__author__ = "League MCP Contributors"
__description__ = "Model Context Protocol server for League of Legends game data via Riot Games API"

try:
    from .main import main
except ImportError:
    # The project is also runnable directly from its script-style source root.
    from main import main

__all__ = ["main"] 
