# Changelog — skillstack-workflows

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.2.1] - 2026-04-27

### Changed

- Capitalize `Not for` → `NOT for` in 12 workflow skill descriptions (router and auditors look for the literal capitalized phrase per skill-foundry v2.2.2 convention). Affected: build-ai-agent, content-platform-build, debug-complex-issue, design-review-sprint, evaluate-and-improve-agent, legacy-rescue, llm-cost-optimization, pitch-sprint, storytelling-for-stakeholders, strategic-decision, user-research-to-insight, write-your-own-skill. The exclusion content was already present — this is purely a casing fix to satisfy literal-string lookups.

## [2.2.0] - 2026-04-24

### Added

- add evaluate-plugin-or-skill workflow

### Changed

- update plugin changelogs [skip ci]

## [2.1.0] - 2026-04-22

### Added

- add update-a-plugin workflow skill

### Changed

- update plugin changelogs [skip ci]

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
