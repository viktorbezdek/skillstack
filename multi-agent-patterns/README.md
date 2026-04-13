# Multi Agent Patterns

> **v1.0.4** | Agent Architecture | 5 iterations

Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, context isolation, consensus mechanisms, and the telephone game solution.

## What Problem Does This Solve

Single LLM agents hit a hard ceiling: as tasks grow complex, context windows fill with accumulated history, tool outputs, and retrieved documents, and performance degrades through attention scattering and context poisoning. The intuitive fix -- splitting work across multiple agents -- introduces coordination overhead that can cost more than it saves if done naively. Role-based "teams" where agents are named after job titles but share the same context achieve nothing. This skill provides the architectural patterns, token economics, failure-mode mitigations, and framework-specific implementations that make multi-agent systems genuinely faster and more capable than single-agent approaches.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent is running out of context on complex research tasks" | Context isolation architecture showing how sub-agents partition work so no single window bears the full burden |
| "How do I structure a supervisor agent that delegates to specialists?" | Supervisor/orchestrator pattern with the `forward_message` fix that eliminates the telephone game accuracy loss (50% improvement in LangGraph benchmarks) |
| "I want agents to hand off to each other without a central controller" | Peer-to-peer/swarm pattern with explicit handoff protocols and state passing between agents |
| "My multi-agent system gives inconsistent answers" | Weighted voting and debate protocol designs that prevent sycophantic consensus on false premises |
| "What's the actual token cost of running multi-agent vs single-agent?" | Token economics table showing 1x/4x/15x multipliers and the research finding that model upgrades often beat raw token increases |
| "A worker agent returned bad output and it broke the whole pipeline" | Error propagation mitigations: output schema constraints, validation before handoff, retry logic with circuit breakers |

## When NOT to Use This Skill

- Agent memory or persistence -- use [memory-systems](../memory-systems/) instead
- Tool design or tool interfaces -- use [tool-design](../tool-design/) instead
- Hosted agent infrastructure or sandboxed VMs -- use [hosted-agents](../hosted-agents/) instead
- BDI cognitive models or mental state modeling -- use [bdi-mental-states](../bdi-mental-states/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install multi-agent-patterns@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the multi-agent-patterns skill to design a research team with supervisor and specialists
```

```
Use the multi-agent-patterns skill to implement a swarm handoff protocol
```

```
Use the multi-agent-patterns skill to evaluate whether my task needs multi-agent or single-agent
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`multi-agent` · `supervisor` · `swarm` · `context-isolation` · `langgraph`

## What's Inside

### Skill: multi-agent-patterns

Single-skill plugin with one reference file.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering three architectural patterns, context isolation principles, consensus mechanisms, token economics, failure modes with mitigations, and eight production guidelines |
| **references/frameworks.md** | Implementation details for LangGraph supervisor pattern, AutoGen GroupChat, CrewAI hierarchical processes, and handoff protocol code |
| **evals/** | Trigger evaluation and output quality evaluation test suites |

### Key content areas

- **Why Multi-Agent Works** -- The context bottleneck problem, token economics reality (1x/4x/15x multiplier table), parallelization argument, and specialization argument with evidence from BrowseComp evaluation
- **Three Architectural Patterns** -- Supervisor/orchestrator (centralized control with telephone game fix), peer-to-peer/swarm (flexible handoffs with explicit protocols), and hierarchical (strategy/planning/execution layers)
- **The Telephone Game Problem** -- LangGraph benchmark finding that supervisor architectures perform 50% worse without direct pass-through, plus the `forward_message` solution with working code
- **Context Isolation Mechanisms** -- Full context delegation, instruction passing, and file system memory with trade-off analysis for each
- **Consensus Protocols** -- Weighted voting, debate protocols (adversarial critique outperforms collaborative consensus), and trigger-based intervention for stalls and sycophancy
- **Failure Modes** -- Four failure patterns (supervisor bottleneck, coordination overhead, divergence, error propagation) with concrete mitigations for each
- **Framework Comparison** -- LangGraph (graph-based state machines), AutoGen (conversational/event-driven), CrewAI (role-based process flows) with implementation reference

## Usage Scenarios

1. **Designing a research pipeline with parallel information gathering.** The skill shows how to structure a supervisor that decomposes a research question into independent subtasks, dispatches them to specialist agents with fresh contexts, and aggregates results -- with the `forward_message` pattern to avoid the telephone game problem where the supervisor garbles sub-agent findings.

2. **Building a customer service system with department-specific agents.** Use the peer-to-peer/swarm pattern with the handoff protocol example to route customers between billing, technical support, and sales agents, passing conversation state without a central bottleneck.

3. **Evaluating whether to go multi-agent or upgrade the model.** The token economics section provides the data: multi-agent systems consume ~15x tokens of a single chat agent, and research shows model upgrades often provide larger performance gains than doubling token budgets. The skill gives you the decision framework for when the complexity is justified.

4. **Preventing consensus failures in multi-agent debates.** When multiple agents need to agree on an answer, simple majority voting treats hallucinations from weak models as equal to strong reasoning. The weighted voting and debate protocol sections show how to design consensus that actually improves accuracy.

5. **Implementing a LangGraph supervisor with worker agents.** The frameworks reference file provides working LangGraph code for the supervisor node, worker nodes, and state management, plus comparable implementations in AutoGen and CrewAI.

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(multi-agent-patterns): add standard keywords and expand README to full format (3e90ed8)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Memory Systems](../memory-systems/)** -- Shared state management across agents with persistent memory architectures
- **[Tool Design](../tool-design/)** -- Tool specialization per agent with structured tool descriptions
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure for running background agents in sandboxed environments
- **[Agent Evaluation](../agent-evaluation/)** -- Evaluating multi-agent system performance with rubrics and benchmarks
- **[Bdi Mental States](../bdi-mental-states/)** -- BDI cognitive architecture for modeling agent beliefs, desires, and intentions

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
