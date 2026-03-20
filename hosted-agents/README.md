# Hosted Agents

> **v1.0.4** | Agent Architecture | 5 iterations

Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents, multiplayer support, warm pools, and multi-client integration (Slack, web, Chrome).

## What Problem Does This Solve

Hosted agents run in remote sandboxed environments rather than on local machines. When designed well, they provide unlimited concurrency, consistent execution environments, and multiplayer collaboration. The critical insight is that session speed should be limited only by model provider time-to-first-token, with all infrastructure setup completed before the user starts their session.

## When to Use This Skill

This skill should be used when the user asks to "build background agent", "create hosted coding agent", "set up sandboxed execution", "implement multiplayer agent", or mentions background agents, sandboxed VMs, agent infrastructure, Modal sandboxes, self-spawning agents, or remote coding environments.

## When NOT to Use This Skill

- agent coordination patterns or multi-agent design -- use [multi-agent-patterns](../multi-agent-patterns/) instead

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

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Practical Guidance**
- **Guidelines**
- **Integration**
- **References**
- **Skill Metadata**

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
