# Changelog — workflow-automation

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.1.22] - 2026-04-18

### Changed

- update plugin changelogs [skip ci]
- add per-plugin changelog generation workflow
- compress verbose code sections (430→250 lines), add anti-patterns table (10 entries), add When NOT to Use, add decision tree header, trim trailing blanks, bump v1.1.22

## [1.1.21] - 2026-04-16

### Changed

- enrich all 54 plugin READMEs with Context to Provide sections
- regenerate README with 4-layer competence model
- regenerate comprehensive README with usage guide
- regenerate comprehensive README
- enhance all 48 skill READMEs with scenario-based use-case guidance
- add installation snippet to all 49 skill README files

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

- add workflow-automation skill for multi-agent orchestration

### Changed

- make each skill an independent plugin with own plugin.json
- add detailed README documentation for all 34 skills
- standardize frontmatter and split oversized SKILL.md files
- deduplicate scripts between git-workflow, cicd-pipelines, and workflow-automation

### Fixed

- resolve broken links, flatten faber scripts, add validate-patterns.py
- make all shell scripts executable and fix Python syntax errors

### Removed

- restore faber/ subdirectory for FABER framework scripts
