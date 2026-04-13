# Multi-Agent Patterns

> **v1.0.4** | Agent Architecture | 5 iterations

> Architecture patterns for multi-agent LLM systems -- supervisor, swarm, and hierarchical designs that actually coordinate instead of just consuming more tokens.

## The Problem

Single-agent LLM systems hit a ceiling fast. As tasks grow complex, the context window fills with accumulated history, retrieved documents, and tool outputs. Performance degrades through predictable patterns: lost-in-middle effects, attention scarcity, and context poisoning. The agent tries to be a researcher, analyzer, fact-checker, and writer simultaneously, and does all of them poorly.

Teams that recognize this problem and try to split work across multiple agents run into a different set of failures. Without clear architectural patterns, they build supervisor agents that become bottlenecks -- accumulating context from every worker until they are as overloaded as the single agent they replaced. They implement the "telephone game" pattern where supervisors paraphrase sub-agent responses incorrectly, losing fidelity (LangGraph benchmarks found this causes 50% worse performance). They create peer-to-peer swarms that diverge from objectives because no one defined convergence constraints.

The token economics make mistakes expensive. Multi-agent systems consume roughly 15x the tokens of a single-agent chat. Building the wrong architecture does not just waste engineering time -- it burns through API budgets while delivering worse results than a well-prompted single agent would have achieved.

## The Solution

This plugin provides three battle-tested architectural patterns for multi-agent systems -- supervisor/orchestrator, peer-to-peer/swarm, and hierarchical -- with clear decision criteria for when each pattern fits. It reframes multi-agent design around the insight that matters: sub-agents exist primarily to isolate context, not to anthropomorphize organizational roles.

You get concrete implementation guidance including the telephone game fix (a `forward_message` tool that lets sub-agents bypass supervisor synthesis), context isolation mechanisms with explicit trade-off analysis, consensus protocols that avoid sycophancy through weighted voting and adversarial debate, and failure mode catalogs with specific mitigations for bottlenecks, divergence, and error propagation.

The skill covers framework-specific implementations across LangGraph, AutoGen, and CrewAI, so you can apply these patterns in whatever stack you are already using. Every pattern includes working code, token economics data, and the specific signals that tell you when the pattern is failing.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Single agent chokes on complex tasks as context window fills up | Context isolation across multiple agents, each with a clean window focused on its subtask |
| Supervisor paraphrases sub-agent responses, losing 50% of fidelity | Telephone game fix with direct pass-through -- sub-agents forward responses to users when synthesis would lose detail |
| Pick multi-agent architecture based on org-chart metaphors | Choose architecture based on coordination needs, context isolation requirements, and token economics |
| Multi-agent consensus devolves into agreement on false premises | Weighted voting and adversarial debate protocols that catch hallucinations and prevent sycophancy |
| No idea whether multi-agent is even worth the 15x token cost | Token economics data showing when parallelization and specialization justify the overhead |
| Agents diverge from objectives in swarm architectures | Convergence constraints, time-to-live limits, and trigger-based intervention patterns |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install multi-agent-patterns@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your multi-agent challenge:
   ```
   I need to build a research system that searches multiple sources in parallel and synthesizes findings -- should I use a supervisor or swarm pattern?
   ```
3. The skill analyzes your coordination needs and recommends the right architecture with trade-off analysis.
4. Dive into implementation details:
   ```
   Show me how to implement the supervisor pattern with LangGraph, including the telephone game fix
   ```
5. Get working code, failure mode mitigations, and framework-specific integration patterns.

## What's Inside

Single-skill plugin with framework reference material and evaluation suites.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering three architectural patterns, context isolation mechanisms, consensus protocols, token economics, failure modes, and production guidelines |
| **references/frameworks.md** | Framework-specific implementations for LangGraph (graph-based state machines), AutoGen (conversational/event-driven), and CrewAI (role-based process flows) |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### multi-agent-patterns

**What it does:** Activates when you need to design, implement, or debug multi-agent LLM systems. It provides three architectural patterns (supervisor/orchestrator, peer-to-peer/swarm, hierarchical), context isolation strategies, consensus mechanisms, and framework-specific implementation guidance for LangGraph, AutoGen, and CrewAI.

**Try these prompts:**

```
I need to coordinate multiple AI agents for a complex research task -- what architecture should I use?
```

```
My supervisor agent is becoming a bottleneck -- it's accumulating too much context from workers. How do I fix this?
```

```
Design a swarm architecture where specialized agents hand off customer requests based on topic
```

```
How do I prevent my multi-agent system from reaching consensus on wrong answers? The agents just agree with each other.
```

```
Compare LangGraph vs AutoGen vs CrewAI for building a hierarchical agent system with three layers
```

```
What's the token cost of multi-agent vs single-agent, and when is the overhead worth it?
```

**Key references:**

| Reference | Topic |
|---|---|
| `frameworks.md` | Implementation patterns for LangGraph supervisor nodes, AutoGen GroupChat, and CrewAI hierarchical crews with working code |

## Real-World Walkthrough

You are building an automated due diligence system for a venture capital firm. When a startup applies for funding, the system needs to research the company across multiple dimensions simultaneously: market analysis, competitive landscape, team background, financial health, and technology assessment. A single agent cannot hold all this context and produce quality analysis -- it needs to be distributed.

**Step 1: Choose your architecture.**

You describe the problem:

```
I'm building a due diligence system that needs to research startups across 5 dimensions in parallel: market, competition, team, financials, and technology. Each dimension requires different tools and data sources. What multi-agent architecture fits?
```

The skill identifies this as a classic supervisor/orchestrator use case: clear task decomposition, independent subtasks that can run in parallel, and a final synthesis step. It explains why swarm would be wrong here (the dimensions are predefined, not emergent) and why hierarchical would be overengineered (there is no strategic/planning/execution separation needed).

**Step 2: Design the supervisor.**

You ask for the implementation:

```
Show me how to implement the supervisor with context isolation so each researcher has a clean window
```

The skill provides a supervisor architecture where a coordinator agent receives the startup name and funding application, decomposes the task into five research subtasks, and dispatches each to a specialized agent. Each researcher agent gets instruction passing (not full context delegation) because the subtasks are well-defined. The skill warns about the telephone game problem: when the supervisor tries to synthesize five detailed research reports into one summary, it will paraphrase and lose critical details.

**Step 3: Fix the telephone game.**

You implement the `forward_message` tool so that each researcher can pass its report directly to the final output when the supervisor determines no cross-referencing is needed. For the synthesis step -- where findings from different dimensions need to be combined (e.g., "the team's ML expertise maps well to the market opportunity") -- the supervisor receives only distilled summaries from each researcher, not their full reports.

**Step 4: Add consensus for conflicting findings.**

Two weeks in, you notice that the market researcher and competition researcher sometimes reach contradictory conclusions about market size. You ask:

```
My market and competition agents disagree on TAM estimates. How do I resolve conflicts between agents?
```

The skill introduces weighted voting: the agent with higher confidence (backed by more data sources) gets more weight. For genuinely ambiguous cases, it recommends a debate protocol where both agents critique each other's estimates over two rounds, with the supervisor making the final call based on the quality of arguments rather than simple averaging.

**Step 5: Handle failure modes.**

In production, the financial analysis agent occasionally times out when scraping public filings. You ask about resilience:

```
One of my agents keeps timing out. How do I prevent it from blocking the whole pipeline?
```

The skill covers three mitigations: time-to-live limits so no agent runs indefinitely, circuit breakers that route around failed agents (the supervisor notes "financial analysis unavailable" rather than blocking), and idempotent retry logic so the agent can resume from its last checkpoint if the timeout was transient.

The result: a five-agent due diligence system that researches startups in parallel (total time equals the slowest researcher, not the sum of all five), produces high-fidelity reports without telephone game degradation, resolves conflicting findings through structured debate, and handles individual agent failures without blocking the pipeline. The 15x token cost is justified because parallel execution cuts wall-clock time from 25 minutes to 6 minutes, and the quality improvement from specialized context isolation is measurable in the reports.

## Usage Scenarios

### Scenario 1: Building a customer support routing system

**Context:** You have a support platform handling billing, technical, and sales queries. You want specialized agents for each domain with seamless handoffs.

**You say:** "Design a multi-agent system where customer queries get routed to the right specialist agent. I need billing, technical, and sales agents with handoff between them."

**The skill provides:**
- Swarm/peer-to-peer pattern recommendation (handoffs are emergent, not hierarchically planned)
- Explicit handoff protocol with state passing so the receiving agent knows the conversation history
- Implementation code using function-return-based agent transfer
- Escalation patterns for queries that span multiple domains

**You end up with:** A working handoff architecture where any agent can transfer control to any other, with conversation state preserved across transfers.

### Scenario 2: Parallelizing a research pipeline

**Context:** You are building a research assistant that needs to search academic papers, news articles, and patent databases simultaneously, then synthesize findings.

**You say:** "I need to search three different sources in parallel and combine the results. How do I structure this as a multi-agent system?"

**The skill provides:**
- Supervisor pattern with parallel dispatch to three specialized search agents
- Context isolation strategy: each agent gets only the search query and source-specific instructions
- Output schema constraints so agents return structured summaries (not raw documents)
- Synthesis guidance with the telephone game fix for preserving search result fidelity

**You end up with:** A supervisor architecture that dispatches parallel searches, collects structured results, and synthesizes findings without losing detail from any source.

### Scenario 3: Preventing groupthink in multi-agent review

**Context:** You have multiple agents reviewing a document for quality, but they keep agreeing with each other's assessments even when one agent's critique is clearly wrong.

**You say:** "My review agents are sycophantic -- they agree with each other instead of providing independent critique. How do I get genuine disagreement?"

**The skill provides:**
- Adversarial debate protocol where agents must critique each other's outputs
- Weighted voting based on confidence and evidence quality
- Sycophancy triggers that detect when agents mimic reasoning without independent analysis
- Stall triggers for when discussions make no progress

**You end up with:** A debate-based review system where agents provide independent critiques, conflicts are resolved through evidence quality rather than majority vote.

### Scenario 4: Choosing the right framework

**Context:** You have decided on a supervisor architecture but need to pick between LangGraph, AutoGen, and CrewAI for implementation.

**You say:** "Compare LangGraph, AutoGen, and CrewAI for a supervisor pattern with 4 worker agents. I'm already using LangChain in my stack."

**The skill provides:**
- Framework philosophy comparison: LangGraph (graph-based state machines), AutoGen (conversational/event-driven), CrewAI (role-based process flows)
- Integration considerations for existing LangChain codebases
- Working implementation patterns for each framework
- Trade-off analysis on flexibility, debugging, and production readiness

**You end up with:** A framework choice grounded in your existing stack and coordination requirements, with a reference implementation to start from.

## Ideal For

- **Teams whose single-agent system has hit context limits** -- the context isolation patterns show how to distribute work without just adding complexity
- **Developers building their first multi-agent system** -- the three-pattern taxonomy prevents reinventing architectures that already have established solutions
- **Engineers debugging coordination failures in production** -- failure mode catalogs with specific mitigations for bottlenecks, divergence, and error propagation
- **Architects evaluating LangGraph vs AutoGen vs CrewAI** -- framework-specific implementations of the same patterns enable apples-to-apples comparison
- **Anyone spending 15x tokens on multi-agent and not seeing proportional quality gains** -- token economics analysis and the telephone game fix address the most common ROI killers

## Not For

- **Agent memory and persistence across sessions** -- use [memory-systems](../memory-systems/) for vector stores, temporal knowledge graphs, and memory framework comparison
- **Tool design and agent tool interfaces** -- use [tool-design](../tool-design/) for designing tools that agents call, not the agents that call them
- **Hosted agent infrastructure and sandboxed execution** -- use [hosted-agents](../hosted-agents/) for VM provisioning, sandboxing, and deployment patterns
- **BDI cognitive models and mental state modeling** -- use [bdi-mental-states](../bdi-mental-states/) for belief-desire-intention architectures

## How It Works Under the Hood

The skill is structured around a progressive complexity model. The core SKILL.md covers three architectural patterns in depth -- supervisor/orchestrator, peer-to-peer/swarm, and hierarchical -- with decision criteria, implementation code, and explicit trade-offs for each. It then layers on cross-cutting concerns: context isolation mechanisms (full delegation vs. instruction passing vs. file-system memory), consensus protocols (weighted voting, debate, trigger-based intervention), and a failure mode catalog with mitigations.

The **frameworks.md** reference provides working implementations of these patterns in LangGraph (graph-based state machines with explicit nodes and edges), AutoGen (conversational GroupChat patterns), and CrewAI (role-based hierarchical crews). These are not toy examples -- they include state management, error handling, and the specific idioms each framework expects.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates on multi-agent queries and produces architecturally sound recommendations.

## Related Plugins

- **[Memory Systems](../memory-systems/)** -- Shared memory across agents with persistence, entity tracking, and temporal knowledge graphs
- **[Context Optimization](../context-optimization/)** -- Context partitioning strategies that complement multi-agent context isolation
- **[Tool Design](../tool-design/)** -- Designing the tools that specialized agents call
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure for deploying multi-agent systems in production
- **[BDI Mental States](../bdi-mental-states/)** -- Cognitive architectures for agents that need belief-desire-intention reasoning

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins
- `1.0.3` fix(multi-agent-patterns): add standard keywords and expand README to full format
- `1.0.2` fix: change author field from string to object in all plugin.json files
- `1.0.1` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
