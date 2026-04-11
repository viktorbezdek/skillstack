# Memory Systems

> **v1.0.5** | Agent Architecture | 6 iterations

Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Covers temporal knowledge graphs, memory consolidation, and retrieval strategies.

## What Problem Does This Solve

LLM agents forget everything when a session ends — user preferences, prior decisions, accumulated domain knowledge, and entity relationships all vanish. Rebuilding that context from scratch each session is expensive and degrades the quality of responses. This skill addresses how to architect persistent memory layers, choose between production frameworks (Mem0, Zep/Graphiti, Letta, LangMem, Cognee), and design retrieval strategies that remain accurate as memory grows and facts change over time.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent loses context between sessions — how do I fix that?" | Memory layer architecture decision tree from file-system through vector stores to knowledge graphs |
| "Which memory framework should I use: Mem0, Zep, or Letta?" | Side-by-side framework comparison with benchmark data (LoCoMo, LongMemEval, DMR) and trade-off analysis |
| "How do I track entities consistently across conversations?" | Entity registry patterns and property tracking so "John Doe" stays the same person across sessions |
| "A fact changed — how do I update memory without poisoning old context?" | Temporal knowledge graph patterns with validity intervals and the invalidate-but-don't-discard principle |
| "My agent's memory retrieval is getting slow and inaccurate as it grows" | Hybrid retrieval strategies (semantic + keyword + graph), consolidation triggers, and Cognee's 14 search modes |
| "How do I build a knowledge graph that supports multi-hop reasoning?" | Cognee and Zep/Graphiti integration examples with graph ingestion, entity extraction, and relationship-aware search |

## When NOT to Use This Skill

- multi-agent coordination or agent handoffs -- use [multi-agent-patterns](../multi-agent-patterns/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/memory-systems
```

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

- **When to Activate** -- Checklist of scenarios where memory architecture decisions are needed
- **Core Concepts** -- The key benchmark insight: tool complexity matters less than reliable retrieval, with Letta's filesystem agents outperforming Mem0's specialized tools
- **Detailed Topics** -- Framework landscape table, memory layer decision matrix (working/short-term/long-term/entity/temporal KG), and retrieval strategy comparison
- **Practical Guidance** -- Step-by-step architecture progression from prototype to production, plus error recovery patterns for empty retrieval, stale results, and conflicting facts
- **Examples** -- Working code for Mem0 integration, temporal relationship queries, and Cognee knowledge graph ingestion and search
- **Guidelines** -- Eight production rules covering consolidation, temporal validity, hybrid retrieval, and privacy considerations
- **Integration** -- How this skill connects to context-optimization and multi-agent-patterns for shared memory
- **References** -- Research papers (arXiv), benchmark frameworks, and open-source repos for Graphiti and Cognee

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
