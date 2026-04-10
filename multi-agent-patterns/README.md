# Multi Agent Patterns

> **v1.0.4** | Agent Architecture | 5 iterations

Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, context isolation, consensus mechanisms, and the telephone game solution.

## What Problem Does This Solve

Single LLM agents hit a hard ceiling: as tasks grow complex, context windows fill with accumulated history, tool outputs, and retrieved documents, and performance degrades through attention scattering and context poisoning. Multi-agent architectures solve this by partitioning work across multiple context windows — but naive decomposition into role-based "teams" introduces coordination overhead that can cost more than it saves. This skill provides the architectural patterns and failure-mode mitigations that make multi-agent systems genuinely faster and more capable than single-agent approaches.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent is running out of context on complex research tasks" | Context isolation architecture showing how sub-agents partition work so no single window bears the full burden |
| "How do I structure a supervisor agent that delegates to specialists?" | Supervisor/orchestrator pattern with the `forward_message` fix that eliminates the telephone game accuracy loss |
| "I want agents to hand off to each other without a central controller" | Peer-to-peer/swarm pattern with explicit handoff protocols and state passing between agents |
| "My multi-agent system gives inconsistent answers — agents seem to just agree with each other" | Weighted voting and debate protocol designs that prevent sycophantic consensus on false premises |
| "What's the actual token cost of running multi-agent vs single-agent?" | Token economics table showing 1x/4x/15x multipliers and the research finding that model upgrades often beat raw token increases |
| "A worker agent returned bad output and it broke the whole pipeline" | Error propagation mitigations: output schema constraints, validation before handoff, retry logic with circuit breakers |

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

- **When to Activate** -- Decision checklist for when multi-agent architecture genuinely helps vs adds overhead
- **Core Concepts** -- The three dominant patterns and the primary design principle: context isolation over role metaphors
- **Detailed Topics** -- Why multi-agent architectures work (context bottleneck, token economics, parallelization, specialization), detailed pattern implementations (supervisor, peer-to-peer/swarm, hierarchical), isolation mechanisms, and consensus protocols
- **Practical Guidance** -- Four failure modes with concrete mitigations: supervisor bottleneck, coordination overhead, divergence, and error propagation
- **Examples** -- Research team architecture diagram and a handoff protocol implementation showing agent routing by request type
- **Guidelines** -- Eight production rules from context isolation design through time-to-live limits and output validation
- **Integration** -- Connections to memory-systems for shared state and tool-design for per-agent tool specialization
- **References** -- LangGraph, AutoGen, and CrewAI documentation plus the multi-agent coordination survey

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
