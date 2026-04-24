# Changelog — skill-foundry

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.2.1] - 2026-04-24

### Changed

- Replace flat reference index in SKILL.md with a conditional dispatch table — "when you are X, load Y" — to eliminate Orphaned Sections. Complete catalog moved to `references/README.md`.
- SKILL.md reduced from 469 to 415 lines, giving headroom against the 500-line progressive-disclosure ceiling.
- Rewrite `evals/trigger-evals.json` with 15 domain-specific queries (9 positive, 6 negative) using the actual trigger phrases from the frontmatter description instead of auto-generated "skill creator" templates.
- Rewrite `evals/evals.json` with 6 scenario-based output evals whose `expected_behavior` lists verifiable criteria tied to the four pillars (description formula, anti-pattern structure, progressive disclosure, decision trees).

### Added

- `references/README.md` — exhaustive catalog of all 47 references grouped by purpose, loaded when the dispatch table in SKILL.md does not match.

## [2.2.0] - 2026-04-18

### Changed

- update plugin changelogs [skip ci]
- add per-plugin changelog generation workflow
- update README and plugin.json for v2.2.0
- v2.2.0 — restructure references, cleanup examples/templates

### Fixed

- rename UPPERCASE references to lowercase, sync plugin-dev validator

## [2.0.0] - 2026-04-16

### Changed

- enrich all 54 plugin READMEs with Context to Provide sections
- regenerate README with 4-layer competence model
- skill-forge -> skill-foundry (unique on skills.sh)

### Fixed

- scope to SKILL.md authoring, add NOT for prompt-engineering/plugin-architecture
