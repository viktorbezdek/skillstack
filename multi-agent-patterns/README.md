# Multi Agent Patterns

> **v1.0.4** | Agent Architecture | 5 iterations

Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, context isolation, consensus mechanisms, and the telephone game solution.

## What Problem Does This Solve

Multi-agent architectures distribute work across multiple language model instances, each with its own context window. When designed well, this distribution enables capabilities beyond single-agent limits. When designed poorly, it introduces coordination overhead that negates benefits. The critical insight is that sub-agents exist primarily to isolate context, not to anthropomorphize role division.

## When to Use This Skill

This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture", "coordinate multiple agents", or mentions multi-agent patterns, context isolation, agent handoffs, sub-agents, or parallel agent execution.

## When NOT to Use This Skill

- agent memory or persistence -- use [memory-systems](../memory-systems/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/multi-agent-patterns
```

## How to Use

**Direct invocation:**

```
Use the multi-agent-patterns skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `multi-agent`
- `supervisor`
- `swarm`
- `context-isolation`
- `langgraph`

## What's Inside

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Practical Guidance**
- **Examples**
- **Guidelines**
- **Integration**
- **References**

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(multi-agent-patterns): add standard keywords and expand README to full format (3e90ed8)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Agent Project Development](../agent-project-development/)** -- Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
