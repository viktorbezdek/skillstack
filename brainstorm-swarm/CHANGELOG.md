# Changelog — brainstorm-swarm

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.0] - 2026-04-28

### Changed

- **swarm-protocol SKILL.md authority upgrade.** Surfaced the canonical 12 persona names AND the 4 named arcs in the SKILL.md main body (previously buried in `references/persona-catalog.md`). Added explicit "MUST USE — literal subagent types, not examples" framing with anti-pattern callouts ("DO NOT invent your own persona names"). The list of literal subagent types (`brainstorm-swarm:pm`, `brainstorm-swarm:engineer`, etc.) now appears at the top of the skill, before the orchestration mechanics.

### Why

- Round 1 benchmark (2026-04-28T13-49-08Z) showed 7 of 9 assertions Unreachable — the with-skill executor was inventing its own persona archetypes ("Visionary, Pragmatist, Synthesizer", "Bear Case Analyst", "Risk Manager") instead of using the canonical 12. The skill was being read but not treated as authoritative on the literal names. The same pattern with the Arc taxonomy: with-skill produced "Pre-Mortem Arc / Red-Team Phase / ATTACK→STRESS-TEST→MITIGATE" instead of "Arc 4 / Phase 3 / convergent closing". This release elevates both vocabularies to the top of the SKILL.md.

## [1.0.0] - 2026-04-28

### Added

- introduce v1.0.0 — parallel persona-swarm brainstorm plugin
