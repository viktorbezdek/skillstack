# Agent Project Development

> **v1.0.4** | Agent Architecture | 5 iterations

Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, cost estimation, and architectural reduction.

## What Problem Does This Solve

This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development. The methodology applies whether building a batch processing pipeline, a multi-agent research system, or an interactive agent application.

## When to Use This Skill

This skill should be used when the user asks to "start an LLM project", "design batch pipeline", "evaluate task-model fit", "structure agent project", or mentions pipeline architecture, agent-assisted development, cost estimation, or choosing between LLM and traditional approaches.

## When NOT to Use This Skill

- evaluating agent quality or building evaluation rubrics -- use [agent-evaluation](../agent-evaluation/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/agent-project-development
```

## How to Use

**Direct invocation:**

```
Use the agent-project-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `project-development`
- `pipeline`
- `task-model-fit`
- `cost-estimation`

## What's Inside

- **When to Activate**
- **Core Concepts**
- **Summary**
- **Score**
- **Details**
- **Detailed Topics**
- **Practical Guidance**
- **Examples**

## Key Capabilities

- **Discrete**
- **Idempotent**
- **Cacheable**
- **Independent**

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(agent-project-development): add standard keywords and expand README to full format (ca2a55d)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, c...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
