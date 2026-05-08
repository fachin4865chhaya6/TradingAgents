"""TradingAgents - A multi-agent framework for AI-driven trading decisions.

This package provides a collection of specialized AI agents that collaborate
to analyze markets, manage risk, and execute trading strategies.

Based on the original TauricResearch/TradingAgents project with additional
enhancements for enterprise use cases.

Personal fork notes:
- Forked for learning and experimentation with multi-agent trading systems
- See NOTES.md for personal observations and experiment results
- Added __author_email__ and __url__ for easier package metadata access
- Added __author__ and __license__ to __all__ for completeness
- Added __author_email__ to __all__ so all metadata fields are consistently exported
- Updated __url__ to point to this personal fork instead of the upstream repo
"""

__version__ = "0.1.0"
__author__ = "TradingAgents Contributors"
__author_email__ = ""
__license__ = "Apache-2.0"
# Updated to point to my personal fork rather than the upstream repository
__url__ = "https://github.com/my-username/TradingAgents"

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

__all__ = [
    "TradingAgentsGraph",
    "DEFAULT_CONFIG",
    "__version__",
    "__author__",
    "__author_email__",
    "__license__",
    "__url__",
]
