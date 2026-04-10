# Memory Systems

> **v1.0.5** | Agent Architecture | 6 iterations

Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Covers temporal knowledge graphs, memory consolidation, and retrieval strategies.

## What Problem Does This Solve

Memory provides the persistence layer that allows agents to maintain continuity across sessions and reason over accumulated knowledge. Simple agents rely entirely on context for memory, losing all state when sessions end. Sophisticated agents implement layered memory architectures that balance immediate context needs with long-term knowledge retention. The evolution from vector stores to knowledge graphs to temporal knowledge graphs represents increasing investment in structured memory for improved retrieval and reasoning.

## When to Use This Skill

Guides implementation of agent memory systems, compares production frameworks (Mem0, Zep/Graphiti, Letta, LangMem, Cognee), and designs persistence architectures for cross-session knowledge retention. Use when the user asks to "implement agent memory", "persist state across sessions", "build knowledge graph for agents", "track entities over time", "add long-term memory", "choose a memory framework", or mentions temporal knowledge graphs, vector stores, entity memory, adaptive memory, dynamic memory, or memory benchmarks (LoCoMo, LongMemEval).

## When NOT to Use This Skill

- multi-agent coordination or agent handoffs -- use [multi-agent-patterns](../multi-agent-patterns/) instead

## How to Use

**Direct invocation:**

```
Use the memory-systems skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `agent-memory`
- `mem0`
- `zep`
- `graphiti`
- `cognee`
- `temporal-knowledge-graph`

## What's Inside

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Practical Guidance**
- **Examples**
- **Guidelines**
- **Integration**
- **References**

## Key Capabilities

- **Empty retrieval**
- **Stale results**
- **Conflicting facts**
- **Storage failure**
- **Stuffing everything into context**
- **Ignoring temporal validity**

## Version History

- `1.0.5` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.4` fix(memory-systems): add standard keywords and expand README to full format (deb2452)
- `1.0.3` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.2` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.1` docs: add 2025-2026 research references for context and memory plugins (8e815ba)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Agent Project Development](../agent-project-development/)** -- Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, c...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 48 production-grade plugins for Claude Code.
