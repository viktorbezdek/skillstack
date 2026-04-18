# Changelog — api-design

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.2.24] - 2026-04-18

### Changed

- update plugin changelogs [skip ci]
- add per-plugin changelog generation workflow
- add API style selection decision tree, condense anti-patterns into table with solutions, add PUT/PATCH and Federation anti-patterns, remove trailing blank lines, improve progressive disclosure

## [1.2.23] - 2026-04-16

### Changed

- enrich all 54 plugin READMEs with Context to Provide sections
- regenerate README with 4-layer competence model
- regenerate comprehensive README with usage guide
- regenerate comprehensive README
- enhance all 48 skill READMEs with scenario-based use-case guidance
- add installation snippet to all 49 skill README files

### Fixed

- add explicit trigger phrases and NOT for node/mcp

## [1.0.0] - 2026-03-01

### Changed

- remove old file locations after plugin restructure
- update README and install commands to marketplace format
- restructure all 34 skills into proper Claude Code plugin format

### Fixed

- repair broken cross-references to legacy skill names
- change author field from string to object in all plugin.json files
- rename all claude-skills references to skillstack

## [0.0.0] - 2026-02-13

### Added

- add api-design skill for REST, GraphQL, gRPC

### Changed

- make each skill an independent plugin with own plugin.json
- add detailed README documentation for all 34 skills
- standardize frontmatter and split oversized SKILL.md files

### Fixed

- make all shell scripts executable and fix Python syntax errors
