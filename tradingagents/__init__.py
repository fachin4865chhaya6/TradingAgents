"""TradingAgents - A multi-agent framework for AI-driven trading decisions.

This package provides a collection of specialized AI agents that collaborate
to analyze markets, manage risk, and execute trading strategies.

Based on the original TauricResearch/TradingAgents project with additional
enhancements for enterprise use cases.

Personal fork notes:
- Forked for learning and experimentation with multi-agent trading systems
- See NOTES.md for personal observations and experiment results
- Added __author_email__ and __url__ for easier package metadata access
"""

__version__ = "0.1.0"
__author__ = "TradingAgents Contributors"
__author_email__ = ""
__license__ = "Apache-2.0"
__url__ = "https://github.com/TauricResearch/TradingAgents"

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

__all__ = [
    "TradingAgentsGraph",
    "DEFAULT_CONFIG",
    "__version__",
    "__url__",
]
