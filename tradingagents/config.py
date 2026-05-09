"""Configuration management for TradingAgents.

This module handles loading and validating configuration from environment
variables and configuration files.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()


@dataclass
class LLMConfig:
    """Configuration for LLM providers."""

    openai_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY")
    )
    anthropic_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY")
    )
    google_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("GOOGLE_API_KEY")
    )
    default_model: str = field(
        default_factory=lambda: os.getenv("DEFAULT_LLM_MODEL", "gpt-4o-mini")
    )
    temperature: float = 0.1
    max_tokens: int = 4096


@dataclass
class DataConfig:
    """Configuration for market data sources."""

    finnhub_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("FINNHUB_API_KEY")
    )
    alpha_vantage_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("ALPHA_VANTAGE_API_KEY")
    )
    polygon_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("POLYGON_API_KEY")
    )
    # Cache settings
    cache_enabled: bool = field(
        default_factory=lambda: os.getenv("CACHE_ENABLED", "true").lower() == "true"
    )
    cache_ttl_seconds: int = field(
        default_factory=lambda: int(os.getenv("CACHE_TTL_SECONDS", "3600"))
    )


@dataclass
class AgentConfig:
    """Configuration for trading agent behaviour."""

    max_debate_rounds: int = field(
        default_factory=lambda: int(os.getenv("MAX_DEBATE_ROUNDS", "3"))
    )
    max_risk_discuss_rounds: int = field(
        default_factory=lambda: int(os.getenv("MAX_RISK_DISCUSS_ROUNDS", "3"))
    )
    # Which analyst agents to enable
    enable_fundamental_analyst: bool = True
    enable_sentiment_analyst: bool = True
    enable_technical_analyst: bool = True
    enable_news_analyst: bool = True
    # Online/offline mode — offline uses cached/mock data
    online_tools: bool = field(
        default_factory=lambda: os.getenv("ONLINE_TOOLS", "true").lower() == "true"
    )


@dataclass
class TradingAgentsConfig:
    """Root configuration object for TradingAgents."""

    llm: LLMConfig = field(default_factory=LLMConfig)
    data: DataConfig = field(default_factory=DataConfig)
    agent: AgentConfig = field(default_factory=AgentConfig)
    # Directory used to persist results and logs
    results_dir: str = field(
        default_factory=lambda: os.getenv("RESULTS_DIR", "./results")
    )
    log_level: str = field(
        default_factory=lambda: os.getenv("LOG_LEVEL", "INFO")
    )

    def validate(self) -> None:
        """Raise ValueError if required configuration is missing."""
        if self.agent.online_tools and self.llm.openai_api_key is None:
            # At least one LLM key must be present for online mode
            if (
                self.llm.anthropic_api_key is None
                and self.llm.google_api_key is None
            ):
                raise ValueError(
                    "At least one LLM API key must be set when ONLINE_TOOLS=true. "
                    "Set OPENAI_API_KEY, ANTHROPIC_API_KEY, or GOOGLE_API_KEY."
                )


# Module-level default config instance
_default_config: Optional[TradingAgentsConfig] = None


def get_config() -> TradingAgentsConfig:
    """Return the default (singleton) configuration instance."""
    global _default_config
    if _default_config is None:
        _default_config = TradingAgentsConfig()
    return _default_config


def reset_config() -> None:
    """Reset the singleton config (useful in tests)."""
    global _default_config
    _default_config = None
