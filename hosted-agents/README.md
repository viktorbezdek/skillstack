# Hosted Agents

> **v1.0.4** | Agent Architecture | 5 iterations

Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents, multiplayer support, warm pools, and multi-client integration (Slack, web, Chrome).

## What Problem Does This Solve

Running AI coding agents locally means resource contention with the developer's machine, inconsistent environments between team members, and sessions that only one person can use at a time. Moving agents to hosted sandboxed infrastructure solves all three, but introduces new challenges: slow session start-up, per-session state isolation at scale, multi-client synchronisation, and secure commit attribution. This skill documents the architectural patterns — image registry, warm pools, per-session SQLite, WebSocket hibernation, and self-spawning — that production teams have used to ship reliable hosted agents.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "We want coding agents that run in the cloud, not on developer laptops" | Core sandbox architecture: image registry pattern with 30-minute pre-build cadence and warm pool strategy |
| "Agent sessions take too long to start — users are waiting" | Speed optimisation patterns: predictive warm-up when user starts typing, parallel file reads before git sync completes |
| "Multiple teammates want to collaborate in the same agent session" | Multiplayer implementation requirements: data model changes, per-prompt authorship, shared session links |
| "Our agent needs to spawn sub-agents to tackle parts of a large task in parallel" | Self-spawning agent design: tools for starting sessions, checking status, and prompt engineering guidance for when to spawn |
| "How do we handle hundreds of concurrent agent sessions without cross-contamination?" | Per-session state isolation: dedicated SQLite per session, WebSocket hibernation API for idle connections |
| "We want to reach non-engineering users through Slack" | Slack integration architecture: repository classifier using fast model, virality loop design, natural-language interface |

## When NOT to Use This Skill

- agent coordination patterns or multi-agent design -- use [multi-agent-patterns](../multi-agent-patterns/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/hosted-agents
```

## How to Use

**Direct invocation:**

```
Use the hosted-agents skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `hosted-agents`
- `sandbox`
- `background-agents`
- `multiplayer`
- `infrastructure`

## What's Inside

- **When to Activate** -- Six trigger scenarios for loading this skill: background agents, sandbox design, multiplayer sessions, multi-client interfaces, scaling beyond local machines, and self-spawning systems.
- **Core Concepts** -- Three-layer architecture overview (sandbox infrastructure, API layer, client interfaces) and the primary design insight that setup must complete before the user session begins.
- **Detailed Topics** -- Six in-depth implementation topics: sandbox infrastructure (image registry, snapshots, warm pools), agent framework selection (server-first, plugin system), speed optimisations, self-spawning agents, API layer (per-session isolation, real-time streaming, cross-client sync), and multiplayer support.
- **Practical Guidance** -- Follow-up message handling strategies (queue vs insert), metrics that matter (merged PR rate as primary KPI), and internal adoption patterns.
- **Guidelines** -- Eight numbered implementation rules from image pre-build cadence to multiplayer-from-the-start.
- **Integration** -- How hosted agents connect to multi-agent-patterns, tool-design, context-optimization, and filesystem-context.
- **References** -- Links to internal infrastructure patterns and external resources (Ramp background agent post, Modal Sandboxes, Cloudflare Durable Objects, OpenCode).

## Key Capabilities

- **Queue approach**
- **Insert approach**

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(hosted-agents): add standard keywords and expand README to full format (01b6dd4)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Agent Project Development](../agent-project-development/)** -- Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, c...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
