# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0] - 2026-04-02

### Added

- **gws-cli** plugin: Google Workspace CLI (gws) skill covering all 18 Workspace APIs (Drive, Gmail, Sheets, Calendar, Docs, Slides, Tasks, People, Chat, Classroom, Forms, Keep, Meet, Events, Script, Admin Reports, Model Armor, Workflow). Includes complete command reference, helper shortcuts, schema introspection, auth guide, query syntax references, and daily workflow examples.
- Marketplace now contains 47 plugins total (up from 46)

## [2.1.0] - 2026-03-14

### Added

- 12 new context engineering and agent architecture plugins:
  - **Context Engineering**: context-fundamentals, context-degradation, context-compression, context-optimization, filesystem-context
  - **Agent Architecture**: multi-agent-patterns, memory-systems, tool-design, hosted-agents, agent-evaluation, agent-project-development, bdi-mental-states
- Research references with latest 2025-2026 advances for memory-systems, multi-agent-patterns, and context engineering
- Marketplace now contains 46 plugins total (up from 34)

### Changed

- Updated marketplace.json to include all 46 plugins with new categories: context-engineering, agent-architecture
- Updated README with Context Engineering and Agent Architecture catalog sections

## [2.0.0] - 2026-03-14

### Changed

- **BREAKING**: Restructured all 34 skills into proper Claude Code plugin format
  - `plugin.json` moved to `.claude-plugin/plugin.json` for each plugin
  - `SKILL.md` and supporting files moved to `skills/<name>/` subdirectories
  - Plugin component directories (`commands/`) remain at plugin root
- Replaced top-level `plugin.json` with `.claude-plugin/marketplace.json`
- Installation method changed from `claude plugin add github:...` to marketplace-based `/plugin install <name>@skillstack`
- Standardized all repository references to use `skillstack`

### Added

- `.claude-plugin/marketplace.json` with all 34 plugins listed with categories and tags
- Marketplace install instructions in all README files
- This changelog

### Removed

- Top-level `plugin.json` (replaced by marketplace.json)

## [1.0.0] - 2026-03-12

### Added

- 34 expert skills covering development, DevOps, testing, API design, documentation, and strategic thinking
- Individual `plugin.json` manifests for each skill
- Per-skill README documentation with install commands
- Hero image and marketplace-style README

### Skills

- **Development**: python-development, typescript-development, react-development, nextjs-development, frontend-design, prompt-engineering, skill-creator
- **DevOps**: cicd-pipelines, docker-containerization, git-workflow
- **Quality**: test-driven-development, testing-framework, debugging, code-review
- **API & Architecture**: api-design, mcp-server
- **Documentation**: documentation-generator, workflow-automation
- **Strategic Thinking**: creative-problem-solving, critical-intuition
- **Helper**: consistency-standards, content-modelling, edge-case-coverage, example-design, navigation-design, ontology-design, outcome-orientation, persona-definition, persona-mapping, prioritization, risk-management, systems-thinking, user-journey-design, ux-writing

### Fixed

- Security vulnerabilities in 6 dependencies (Dependabot alerts)
- All shell scripts marked executable
- Python syntax errors in skill-generator.py and design_token_generator.py
- Broken internal links in SKILL.md documentation
- Non-English content translated to English

### Security

- Scrubbed hardcoded credentials from scripts
- Replaced `eval` usage with safe alternatives
- Added XSS warnings in template outputs
