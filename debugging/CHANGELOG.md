# Changelog — debugging

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.27] - 2026-04-18

### Changed

- add NOT clause for feature dev/refactoring, add 3 anti-patterns (one-test-pass, no-failing-test, ignore-env), refine description keywords with test pollution/flaky/E2E

## [1.1.26] - 2026-04-16

### Added

- rename skill-creator to skill-forge, differentiate from Anthropic's bundled skill-creator

### Changed

- enrich all 54 plugin READMEs with Context to Provide sections
- regenerate README with 4-layer competence model
- regenerate comprehensive README with usage guide
- regenerate comprehensive README
- enhance all 48 skill READMEs with scenario-based use-case guidance
- add installation snippet to all 49 skill README files

### Fixed

- update basic-ftp 5.2.0→5.2.2 to resolve CVE-2026-39983

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

- add Chrome DevTools scripts and E2E workflow
- add debugging skill with systematic methodology

### Changed

- make each skill an independent plugin with own plugin.json
- add detailed README documentation for all 34 skills
- standardize frontmatter and split oversized SKILL.md files
- add Puppeteer reference link
- add browser automation script catalog
- add red flags list for process violations
- improve four phases formatting
- add verification before completion checklist
- add quick decision matrix for issue types
- add real-world impact statistics
- clarify Phase 1 root cause investigation steps

### Fixed

- make all shell scripts executable and fix Python syntax errors
- add AI-powered error classification patterns
- add E2E testing workflow phases overview
- add multi-component evidence gathering steps
- add CI/CD pipeline debugging and test polluter finder
- add defense-in-depth validation and verification checklist
