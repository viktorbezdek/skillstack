# Multi-Agent Architecture Patterns

> Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, context isolation, consensus mechanisms, and the telephone game solution.

## Overview

Multi-agent architectures distribute work across multiple language model instances, each with its own context window. When designed well, this distribution enables capabilities beyond single-agent limits: parallel execution, specialized context per subtask, and protection against context degradation. When designed poorly, it introduces coordination overhead that negates all benefits. The critical insight is that sub-agents exist primarily to isolate context, not to anthropomorphize organizational roles.

This skill covers three dominant architectural patterns (supervisor/orchestrator, peer-to-peer/swarm, and hierarchical), the context isolation principle that motivates them, and the coordination mechanisms (consensus, voting, debate protocols) that keep them aligned. It addresses key failure modes including the "telephone game" problem where supervisors paraphrase sub-agent responses incorrectly (solved by a direct forward_message tool), supervisor bottlenecks, coordination overhead, divergence, and error propagation. Token economics data shows multi-agent systems consume approximately 15x baseline tokens, but BrowseComp research validates this investment when context isolation improves quality.

Within the SkillStack collection, Multi-Agent Patterns builds on Context Fundamentals and Context Degradation (understanding why context isolation matters). It connects to Memory Systems for shared state across agents, Tool Design for specialized tool sets per agent, Context Optimization for partitioning strategies, and Hosted Agents for infrastructure that supports self-spawning agent sessions.

## What's Included

### Skill

- `skills/multi-agent-patterns/SKILL.md` -- Core patterns covering supervisor/orchestrator, peer-to-peer/swarm, hierarchical architectures, context isolation mechanisms, consensus protocols, failure modes, and framework considerations (LangGraph, AutoGen, CrewAI)

### References

- **frameworks.md** -- Detailed framework implementation patterns for LangGraph (graph-based state machines), AutoGen (conversational/event-driven), and CrewAI (role-based process flows)

## Key Features

- **Three architectural patterns**: supervisor/orchestrator (centralized control, clear decomposition), peer-to-peer/swarm (flexible exploration, no single point of failure), and hierarchical (layered abstraction with strategy/planning/execution)
- **Context isolation as design principle** with three mechanisms: full context delegation, instruction passing, and file system memory, each with distinct trade-offs
- **Telephone game solution** using a `forward_message` tool that lets sub-agents pass responses directly to users, eliminating supervisor synthesis errors that caused 50% worse performance in LangGraph benchmarks
- **Token economics data**: single agent ~1x, with tools ~4x, multi-agent ~15x baseline, validated by BrowseComp research showing token usage explains 80% of performance variance
- **Consensus mechanisms** including weighted voting (by confidence/expertise), debate protocols (adversarial critique for higher accuracy), and trigger-based intervention (stall detection, sycophancy detection)
- **Failure mode catalog** with mitigations: supervisor bottleneck (output schema constraints), coordination overhead (batch results, async patterns), divergence (objective boundaries, TTL limits), and error propagation (validation, circuit breakers)
- **Framework comparison**: LangGraph (graph-based state machines), AutoGen (conversational/event-driven GroupChat), CrewAI (role-based hierarchical crews)
- **Parallelization argument** where total time approaches the longest subtask rather than the sum of all subtasks

## Usage Examples

Design a multi-agent research system:
```
Build a research system where a supervisor coordinates a web searcher, a document analyzer, a fact-checker, and a report writer. Each specialist should have isolated context focused on its subtask.
```

Implement the swarm pattern for customer support:
```
Design a peer-to-peer agent system for customer support where requests are handed off between billing, technical, and sales agents based on intent classification. Include explicit handoff protocols with state passing.
```

Solve the telephone game problem:
```
Our supervisor agent is paraphrasing sub-agent responses and losing important details. Implement the forward_message pattern so sub-agents can pass responses directly to users when synthesis would degrade quality.
```

Choose between single and multi-agent architecture:
```
I have a task that requires searching 5 data sources, analyzing results, and writing a synthesis report. Help me evaluate whether a single agent or multi-agent approach is better, considering token costs and quality trade-offs.
```

## Quick Start

1. **Verify you need multi-agent**: Single agents are simpler and cheaper (~1x vs ~15x tokens). Choose multi-agent only when context limits constrain quality or tasks decompose into parallelizable subtasks.
2. **Select a pattern**: Supervisor for clear task decomposition with oversight, swarm for flexible exploration, hierarchical for large-scale layered projects.
3. **Design for context isolation**: Each sub-agent should operate in a clean context focused on its subtask. Use instruction passing for simple subtasks, file system memory for complex shared state.
4. **Implement the forward_message tool**: Prevent the telephone game by letting sub-agents pass responses directly to users when supervisor synthesis would lose fidelity.
5. **Handle failures**: Set TTL limits on agent execution, validate outputs before passing between agents, and implement retry logic with circuit breakers.

## Related Skills

- **context-fundamentals** -- Understanding why context isolation is the primary motivation for multi-agent systems
- **context-degradation** -- The degradation patterns that context isolation prevents
- **memory-systems** -- Shared memory architectures for cross-agent state management
- **tool-design** -- Designing specialized tool sets per agent role
- **context-optimization** -- Context partitioning as a form of optimization
- **hosted-agents** -- Infrastructure for self-spawning agent sessions and parallel execution

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install multi-agent-patterns@skillstack` — 46 production-grade plugins for Claude Code.
