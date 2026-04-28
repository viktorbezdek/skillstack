# Changelog — plugin-dev

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.2.0] - 2026-04-28

### Added

- bump to v1.2.0 — bundle run_eval.py into scaffolded plugins

## [1.1.1] - 2026-04-18

### Changed

- update plugin changelogs [skip ci]
- add per-plugin changelog generation workflow
- trim documenter SKILL.md from 578 to 423 lines, add anti-patterns and decision tree to validation skill

### Fixed

- rename UPPERCASE references to lowercase, sync plugin-dev validator

## [1.1.0] - 2026-04-13

### Added

- rename skill-creator to skill-forge, differentiate from Anthropic's bundled skill-creator
- add plugin-documenter skill — generates docs for any Claude plugin

### Changed

- regenerate README with 4-layer competence model
- skill-forge -> skill-foundry (unique on skills.sh)
- regenerate comprehensive README with usage guide
- regenerate comprehensive README

### Fixed

- update drift test to reference skill-foundry instead of skill-creator

## [1.0.0] - 2026-04-12

### Added

- add plugin authoring toolkit — 7 skills, 4 scripts, 48 tests

### Changed

- add eval running instructions to plugin-dev and root READMEs
