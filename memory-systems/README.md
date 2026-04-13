# Memory Systems

> **v1.0.5** | Agent Architecture | 6 iterations

Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Covers temporal knowledge graphs, memory consolidation, and retrieval strategies.

## What Problem Does This Solve

LLM agents forget everything when a session ends -- user preferences, prior decisions, accumulated domain knowledge, and entity relationships all vanish. Rebuilding that context from scratch each session is expensive and degrades response quality. Naive approaches like stuffing all prior interactions into the prompt hit context limits fast, and unstructured vector dumps degrade as memory grows. This skill addresses how to architect persistent memory layers, choose between production frameworks (Mem0, Zep/Graphiti, Letta, LangMem, Cognee), and design retrieval strategies that remain accurate as memory scales and facts change over time.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent loses context between sessions -- how do I fix that?" | Memory layer architecture decision tree progressing from file-system through vector stores to temporal knowledge graphs |
| "Which memory framework should I use: Mem0, Zep, or Letta?" | Side-by-side framework comparison with benchmark data (LoCoMo, LongMemEval, DMR, HotPotQA) and trade-off analysis across all five production frameworks |
| "How do I track entities consistently across conversations?" | Entity registry patterns and property tracking so "John Doe" stays the same person across sessions |
| "A fact changed -- how do I update memory without poisoning old context?" | Temporal knowledge graph patterns with validity intervals and the invalidate-but-don't-discard principle |
| "My agent's memory retrieval is getting slow and inaccurate as it grows" | Hybrid retrieval strategies (semantic + keyword + graph), consolidation triggers, and Cognee's 14 search modes |

## When NOT to Use This Skill

- Multi-agent coordination or agent handoffs -- use [multi-agent-patterns](../multi-agent-patterns/) instead
- Tool design or tool interfaces for agents -- use [tool-design](../tool-design/) instead
- Hosted agent infrastructure or sandboxed VMs -- use [hosted-agents](../hosted-agents/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install memory-systems@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the memory-systems skill to design a persistent memory layer for my chatbot
```

```
Use the memory-systems skill to compare Mem0 vs Cognee for my multi-hop reasoning use case
```

```
Use the memory-systems skill to implement temporal knowledge graphs for entity tracking
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`agent-memory` · `mem0` · `zep` · `graphiti` · `cognee` · `temporal-knowledge-graph`

## What's Inside

### Skill: memory-systems

Single-skill plugin with two reference files.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering framework landscape, memory layer decision matrix, retrieval strategy comparison, architecture progression, error recovery patterns, and production guidelines |
| **references/implementation.md** | Working code for vector store implementation, Mem0 integration, temporal relationship queries, Cognee knowledge graph ingestion and search, and memory consolidation patterns |
| **references/latest-research-2026.md** | Current benchmark landscape (LoCoMo, LongMemEval, DMR, HotPotQA), detailed framework state for all five production systems, emerging research, sleep-time compute, and decision matrix |
| **evals/** | Trigger evaluation and output quality evaluation test suites |

### Key content areas

- **Production Framework Landscape** -- Comparison table of Mem0, Zep/Graphiti, Letta, Cognee, LangMem, and file-system approaches with architecture, best-for, and trade-off columns
- **Benchmark Performance** -- Head-to-head numbers across DMR accuracy, LoCoMo scores, HotPotQA multi-hop reasoning, and latency measurements
- **Memory Layers** -- Five-layer decision matrix (working, short-term, long-term, entity, temporal KG) with persistence characteristics, implementation approaches, and when-to-use guidance
- **Retrieval Strategies** -- Semantic, entity-based, temporal, and hybrid retrieval with limitations and performance data (Zep's 90% latency reduction, Cognee's 14 search modes)
- **Architecture Progression** -- Step-by-step path from prototype (file-system) through scale (Mem0/vector store) to complex reasoning (Zep/Graphiti/Cognee) to full control (Letta)
- **Error Recovery** -- Patterns for empty retrieval, stale results, conflicting facts, and storage failures
- **Anti-Patterns** -- Stuffing everything into context, ignoring temporal validity, over-engineering early, no consolidation strategy

## Usage Scenarios

1. **Building a customer support agent that remembers user history.** The skill walks you through starting with Mem0 for multi-tenant isolation, designing entity registries for user identity, and implementing hybrid retrieval so the agent surfaces relevant prior interactions without flooding the context window.

2. **Designing a research assistant that accumulates domain knowledge.** Use the memory layer decision matrix to pick long-term storage with entity tracking, then follow the Cognee integration example to build a knowledge graph that supports multi-hop reasoning across accumulated research.

3. **Migrating from a naive vector-store to temporal knowledge graphs.** The architecture progression guide shows when simple approaches fail (conflicting facts, stale information, degraded retrieval quality) and how to add Zep/Graphiti's bi-temporal model to track when facts were true versus when they were recorded.

4. **Evaluating which memory framework fits your stack.** The benchmark comparison and decision matrix in the research reference give concrete numbers (Letta 74% on LoCoMo vs Mem0 68.5%, Zep's 94.8% DMR accuracy) so you can make an evidence-based choice rather than picking based on marketing.

5. **Debugging degraded memory retrieval in production.** The error recovery section and eight production guidelines cover consolidation triggers, temporal validity checks, hybrid retrieval fallbacks, and monitoring patterns for memory growth and latency.

## Version History

- `1.0.5` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.4` fix(memory-systems): add standard keywords and expand README to full format (deb2452)
- `1.0.3` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.2` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.1` docs: add 2025-2026 research references for context and memory plugins (8e815ba)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems with shared memory across agents
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity with memory-based context loading
- **[Agent Evaluation](../agent-evaluation/)** -- Evaluation frameworks for measuring memory quality and agent performance
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted agents that need persistent state
- **[Bdi Mental States](../bdi-mental-states/)** -- BDI cognitive architecture with belief management that connects to memory systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
