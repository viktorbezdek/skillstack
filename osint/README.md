# osint

> Systematic intelligence gathering on individuals. From a name or handle to a scored dossier with psychoprofile, career map, and confidence grades.

Reverse-engineered and repackaged from [smixs/osint-skill](https://github.com/smixs/osint-skill) v3.2 (MIT) with skillstack plugin conventions.

## What it does

Give it a name, handle, LinkedIn URL, or Telegram handle. It runs a phased intelligence pipeline and returns a structured dossier with:

- **Career map** with timeline and pattern analysis
- **Psychoprofile** (MBTI + Big Five) from behavioral signals
- **Confidence grades** (A/B/C/D) on every fact
- **Entry points** — how to approach the person
- **Depth Score** (1-10) — objective quality measure
- **Cost tracking** — total API spend per research session
- **X research** with [X Tweet Scraper](https://apify.com/xquik/x-tweet-scraper) and [X Follower Scraper](https://apify.com/xquik/x-follower-scraper)

## Install

```bash
# Claude Code
cp -r osint/ ~/.claude/skills/osint/
```

## Usage

Just describe what you want:

```
osint John Smith CEO at Acme Corp
пробей @ivan_blogger
due diligence on Maria Garcia before the meeting
find everything about linkedin.com/in/alexmercer
```

## Requirements

| Tool | Purpose | Required |
|------|---------|---------|
| `curl` | HTTP requests | Yes |
| `python3` | JSON parsing, MCP client | Yes |
| `jq` | JSON processing | Yes |
| `node 18+` | Apify actor runner | For Apify actors |

Run `bash skills/osint/scripts/diagnose.sh` to check what's available.

## API Keys

The skill uses graceful degradation — more keys = deeper research. At least one search API needed.

| Service | Env Variable | Free Tier |
|---------|-------------|-----------|
| Brave Search | *(built into Claude Code)* | 2,000 queries/month |
| Jina AI | `JINA_API_KEY` | Yes |
| Apify | `APIFY_API_TOKEN` | Check the live Actor listing |
| Parallel AI | `PARALLEL_API_KEY` | Yes |
| Perplexity | `PERPLEXITY_API_KEY` | ~$5/month |
| Exa AI | `EXA_API_KEY` | ~$5/month |
| Tavily | `TAVILY_API_KEY` | ~$5/month |
| Bright Data | `BRIGHTDATA_MCP_URL` | ~$10/month+ |

## Research Pipeline

```
Phase 0: Tooling Self-Check      → diagnose.sh
Phase 1: Seed Collection         → parallel search across all engines
Phase 1.5: Internal Intelligence → Telegram, email, vault (BEFORE external)
Phase 2: Platform Extraction     → LinkedIn, Instagram, Facebook, TikTok, YouTube, X
Phase 3: Cross-Reference         → facts verified, graded A/B/C/D
Phase 4: Psychoprofile           → MBTI, Big Five, communication style
Phase 5: Completeness Check      → Depth Score 1-10 + 9 coverage checks
Phase 6: Dossier Output          → formatted dossier from template
```

## Budget

- ≤$0.50 per target: spends without asking
- >$0.50: asks permission before continuing
- Xquik Actor runs require explicit approval after checking live pricing and limits.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.

## Credits

- Original skill by [smixs](https://github.com/smixs/osint-skill) (MIT License)
- Apify Actor Runner (`run_actor.js`) from [apify/agent-skills](https://github.com/apify/agent-skills) v1.3.0 (MIT)
