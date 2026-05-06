# Changelog — documentation-generator

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.2.0] - 2026-05-06

### Changed

- Rewrote SKILL.md from process-descriptions to output-anchored mandatory deliverables (4 required artifacts per run)
- Replaced all inert "Load skill: X" references with direct behavioral instructions and output schemas
- Added mandatory Audience Analysis table (Phase 2) with Persona/Role/Background/Goal schema — baseline Sonnet does not produce this without explicit requirement
- Added mandatory Prioritized Doc Backlog (Phase 2) with Diátaxis Type + P0/P1/P2 columns
- Added Phase 3 Diátaxis classification: every doc must carry `<!-- Doc-Type: Tutorial|How-To|Reference|Explanation -->` label
- Added per-doc-type required sections: Tutorials need Before You Begin + What You Will Learn + Next Steps; How-Tos need Troubleshooting table; Reference needs code sample at top + error table
- Added mandatory DQI Quality Score (Phase 6) — numeric X/100 required in output
- Added mandatory Known Gaps Register (Phase 6) — explicit gaps or "No known gaps" required
- Added `<examples>` XML block with concrete sample output of all 4 mandatory deliverables
- Inlined ADR heading requirement: `## Status` as heading, NOT `| Status | Accepted |` table row
- Added content owner metadata requirement: `<!-- Last verified: YYYY-MM-DD | Owner: team-name -->`
- Updated evals.json with 3 sharper discriminating assertions targeting new mandatory deliverables
- Removed "Quick Reference: Which Skills to Load When" section (inert in execution context)

### Motivation

Benchmark run 2026-05-06 showed Δ=+0.00 (5/9 Baseline) — baseline Sonnet already produces multi-file docs, structured templates, and service breakdowns without the skill. The skill's unique value (persona-first planning, Diátaxis classification, completeness scoring) was not being enforced. This rewrite makes those behaviors mandatory and observable.

## [1.1.16] - 2026-04-18

### Changed

- update plugin changelogs [skip ci]
- add per-plugin changelog generation workflow
- add decision tree, anti-patterns, when-not-to-use, improve description precision

## [1.1.15] - 2026-04-16

### Changed

- enrich all 54 plugin READMEs with Context to Provide sections
- regenerate README with 4-layer competence model
- regenerate comprehensive README with usage guide
- enhance all 48 skill READMEs with scenario-based use-case guidance
- add installation snippet to all 49 skill README files

### Fixed

- replace vague 'creating docs' with quoted user trigger phrases and NOT clauses

## [1.0.0] - 2026-03-03

### Changed

- remove old file locations after plugin restructure
- update README and install commands to marketplace format
- restructure all 34 skills into proper Claude Code plugin format

### Fixed

- update plugin count and normalize footer in 31 original plugin READMEs
- change author field from string to object in all plugin.json files
- rename all claude-skills references to skillstack

## [0.0.0] - 2026-02-13

### Added

- add documentation-generator with 24 templates

### Changed

- make each skill an independent plugin with own plugin.json
- add detailed README documentation for all 34 skills
- standardize frontmatter and split oversized SKILL.md files
