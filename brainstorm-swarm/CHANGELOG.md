# Changelog — brainstorm-swarm

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-04-28

### Added

- Initial release.
- 12 persona subagents in `agents/` for true-parallel brainstorming via the Task() tool: pm, engineer, designer, skeptic, user-advocate, pre-mortem-specialist, junior, veteran, first-principles-thinker, constraint-setter, optimist, operator.
- 4 skills:
  - **swarm-protocol** — orchestration logic, persona-subset selection, parallel invocation patterns
  - **interview-facilitation** — interview arcs, question design, depth-vs-breadth tradeoffs
  - **swarm-synthesis** — frameworks for combining multi-persona outputs (consensus matrix, dissent log, open-questions, decision synthesis)
  - **custom-personas** — designing ad-hoc personas when the canonical 12 don't fit
- 1 slash command: `/brainstorm-swarm:start <topic>`
