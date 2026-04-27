# Changelog — skill-foundry

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.2.2] - 2026-04-27

### Changed

- Restructure SKILL.md to put MANDATORY block + literal Template in the first ~50 lines (lines 26 and 38), ahead of philosophy and theory. Validated by benchmark: pass-rate delta moved from −0.11 (regression) to +0.11 (weak signal), stddev halved from 0.39 → 0.20.
- Promote the SKILL.md Template from "example" to "mandatory minimum — copy this literally" with explicit instruction to retain the `When to Use`, `Common Anti-Patterns`, and `NOT for` clause.

### Added

- `## ⛔ MANDATORY in every SKILL.md you create` block enforcing three load-bearing requirements: literal `NOT for` clause in description, anti-pattern block with Symptom/Problem/Solution structure, and dual positive/negative use lists. Includes audit-time directive requiring foundry vocabulary (`anti-pattern`, `philosophy`, `shibboleth`).
- Reinforced literal `NOT for` enforcement in Description Field Engineering section.

## [2.2.1] - 2026-04-24

### Fixed

- address activation/content gaps, bump to v2.2.1

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
