# Changelog

All notable changes to the osint plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-06

### Added
- Initial release: reverse-engineered and repackaged from [smixs/osint-skill](https://github.com/smixs/osint-skill) v3.2 (MIT)
- SKILL.md with skillstack conventions: `NOT for` clause, `allowed-tools`, anti-pattern block
- 8-phase research pipeline (0 → 6): tooling check, seed collection, internal intelligence, platform extraction, cross-reference, psychoprofile, completeness evaluation, dossier output
- Swarm mode: 3-5 parallel Sonnet sub-agents for 5x speed improvement
- 4-level research escalation (free → $0.50 budget gate)
- 55+ Apify actors across Instagram (12), Facebook (14), TikTok (14), YouTube (5), Google Maps (4)
- 7 search API wrappers: Perplexity, Exa, Tavily, Jina, Parallel, Bright Data, Brave
- Confidence scoring system: grades A/B/C/D per fact
- Internal intelligence: Telegram history, email (himalaya), vault/CRM
- Psychoprofile engine: MBTI + Big Five from behavioral signals
- Completeness evaluation: Depth Score (1-10) with 8 weighted axes
- `diagnose.sh` — capability self-check before research starts
- `first-volley.sh` + `merge-volley.sh` — parallel multi-engine seed collection
- `run_actor.js` + `run-actor.sh` — universal Apify runner (embedded from apify/agent-skills v1.3.0)
- `mcp-client.py` — lightweight MCP client for Bright Data (stdlib only)
- Reference files: tools.md, platforms.md, psychoprofile.md, content-extraction.md
- Dossier template with confidence map, entry points, and cost tracking
- Trigger evals (18 positive, 5 negative) and output quality evals (3 scenarios)
