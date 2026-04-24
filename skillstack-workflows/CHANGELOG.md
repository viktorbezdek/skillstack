# Changelog — skillstack-workflows

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.2.0] - 2026-04-24

### Added

- new workflow `evaluate-plugin-or-skill` — multi-pass audit that grades a user-provided plugin or single SKILL.md across five dimensions (structure, activation, content, output, documentation) and returns a single verdict: SHIP, IMPROVE, or REWORK. Composes plugin-validation, plugin-evaluation, and skill-foundry.

### Changed

- bump workflow count to twenty (added `evaluate-plugin-or-skill`)
- add `update-a-plugin` row to the README Meta workflows table (was already in the skills tree but missing from the catalog)
- plugin manifest description updated, version bumped to 2.2.0

## [2.1.0] - 2026-04-22

### Added

- add update-a-plugin workflow skill

## [2.0.1] - 2026-04-18

### Changed

- update plugin changelogs [skip ci]
- add per-plugin changelog generation workflow
- add decision trees and anti-patterns tables to 7 weakest workflows (onboard-to-codebase, context-engineering-pipeline, design-review-sprint, security-hardening-audit, api-to-production, product-story-to-ship, storytelling-for-stakeholders), bump v2.0.1

## [2.0.0] - 2026-04-16

### Added

- rename skill-creator to skill-forge, differentiate from Anthropic's bundled skill-creator

### Changed

- enrich all 54 plugin READMEs with Context to Provide sections
- regenerate README with 4-layer competence model
- skill-forge -> skill-foundry (unique on skills.sh)
- regenerate comprehensive README with usage guide
