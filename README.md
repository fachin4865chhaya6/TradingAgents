<p align="center">
  <img src="assets/TauricResearch.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2412.20138" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2412.20138-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.com/invite/hk9PGKShPK" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-TradingResearch-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="./assets/wechat.png" target="_blank"><img alt="WeChat" src="https://img.shields.io/badge/WeChat-TauricResearch-brightgreen?logo=wechat&logoColor=white"/></a>
  <a href="https://x.com/TauricResearch" target="_blank"><img alt="X Follow" src="https://img.shields.io/badge/X-TauricResearch-white?logo=x&logoColor=white"/></a>
  <br>
  <a href="https://github.com/TauricResearch/" target="_blank"><img alt="Community" src="https://img.shields.io/badge/Join_GitHub_Community-TauricResearch-14C290?logo=discourse"/></a>
</div>

<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de">Deutsch</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es">Español</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr">français</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja">日本語</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko">한국어</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt">Português</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru">Русский</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh">中文</a>
</div>

---

# TradingAgents: Multi-Agents LLM Financial Trading Framework

> **Personal fork** — I'm using this to learn LLM-based trading strategies and experiment with different model providers. Main changes from upstream: testing DeepSeek as the default LLM backend and tweaking the analyst debate rounds for faster iteration.

## My Personal Notes

- **Default debate rounds**: Set to 1 (down from 2) in my local config — speeds up experimentation significantly with minimal quality loss for quick tests.
- **Preferred backend**: `deepseek-chat` — cheapest option I've found that still produces coherent analyst reports.
- **TODO**: Try swapping in `deepseek-reasoner` for the bull/bear debate step only and see if it improves signal quality.
- **TODO**: Benchmark `deepseek-chat` vs `gpt-4o-mini` on a fixed set of 10 tickers to get a cost/quality comparison with real numbers.
- **Observation**: On tech stocks, the sentiment analyst tends to over-weight recent news. May need to tune the prompt to emphasize a longer lookback window.
- **Observation (2026-05)**: Ran a quick 5-ticker spot check (AAPL, MSFT, NVDA, AMZN, GOOGL) — `deepseek-chat` produced reasonable bull/bear arguments but occasionally hallucinated specific earnings figures. Always cross-check numbers against a real data source before acting on output.
- **Observation (2026-05)**: `deepseek-reasoner` is noticeably slower (~3-4x) than `deepseek-chat` for the debate step, but the reasoning traces are easier to audit. Worth the cost for final validation runs, not for rapid iteration.
