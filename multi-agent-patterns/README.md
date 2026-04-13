# Multi-Agent Patterns

> **v1.0.4** | Agent Architecture | 5 iterations

---

## The Problem

When a single LLM agent hits the ceiling -- context window filled, reasoning degraded, tools overloaded -- the natural instinct is to add more agents. Teams spin up "researcher," "writer," "reviewer" agents modeled after human org charts and immediately hit problems that no amount of prompt engineering fixes.

The supervisor agent becomes a bottleneck, accumulating context from every worker until it degrades like any overloaded single agent. The "telephone game" kicks in: the supervisor paraphrases sub-agent responses, losing fidelity with each pass, and LangGraph benchmarks show this causes 50% worse performance than optimized architectures. Peer-to-peer agents diverge without central coordination, pursuing different goals until outputs are irreconcilable. Error propagation turns a single agent's hallucination into a cascading failure across the entire system.

Token economics compound the architectural challenges. Production data shows multi-agent systems consume roughly 15x the tokens of a single-agent chat. Teams discover too late that upgrading to a better model often provides larger performance gains than doubling token budgets across agents. Research on BrowseComp found that token usage alone explains 80% of performance variance -- meaning architecture decisions that waste tokens on coordination overhead directly reduce output quality.

Without structured patterns for context isolation, consensus mechanisms, and failure recovery, teams reinvent these solutions project by project. They build supervisor architectures that bottleneck, swarm architectures that diverge, and hierarchical architectures that misalign strategy with execution. Each failure costs weeks and thousands of dollars in wasted compute.

## The Solution

The Multi-Agent Patterns plugin gives Claude expertise in the three dominant multi-agent architecture patterns -- supervisor/orchestrator, peer-to-peer/swarm, and hierarchical -- with concrete guidance on when each pattern fits, how to implement context isolation, and how to prevent the specific failure modes each pattern introduces.

The plugin provides a single skill backed by a frameworks reference document covering LangGraph, AutoGen, and CrewAI implementations. It addresses the core design principle that most teams miss: sub-agents exist primarily to isolate context, not to simulate organizational roles. It covers the telephone game problem and its solution (direct message forwarding), weighted voting and debate protocols for consensus, and trigger-based intervention for detecting stalls and sycophancy.

The practical guidance includes token economics data so you can evaluate whether multi-agent architecture is justified for your use case, failure mode mitigations for supervisor bottleneck, coordination overhead, divergence, and error propagation, and framework-specific implementation patterns.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Design multi-agent systems by mirroring org charts (researcher, writer, reviewer) | Design by context isolation needs -- sub-agents partition context, not simulate roles |
| Supervisor paraphrases sub-agent responses, losing 50% fidelity (telephone game) | Direct message forwarding pattern eliminates translation errors |
| No data on whether multi-agent is worth the token cost for your use case | Token economics table: single agent (1x) vs tools (4x) vs multi-agent (15x) with performance variance data |
| Agents in swarm architectures drift from objectives without convergence constraints | Explicit convergence checks, time-to-live limits, and objective boundaries per agent |
| Consensus devolves into sycophancy -- agents agree on false premises | Weighted voting, debate protocols, and trigger-based intervention for stall/sycophancy detection |
| Errors in one agent cascade to all downstream consumers | Output validation between agents, retry logic with circuit breakers, idempotent operations |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install multi-agent-patterns@skillstack
```

### Prerequisites

None. For cross-agent memory, also install `memory-systems`. For tool specialization per agent, also install `tool-design`.

### Verify installation

After installing, test with:

```
I need to design a multi-agent system for a research pipeline -- one agent searches, one analyzes, one writes. What architecture pattern should I use?
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `My single agent is hitting context limits on complex research tasks -- should I split it into multiple agents?`
3. The skill evaluates your use case against token economics and parallelization benefits to determine if multi-agent is justified
4. You receive an architecture recommendation (supervisor, swarm, or hierarchical) with context isolation strategy
5. Next, try: `Show me how to implement a supervisor pattern that avoids the telephone game problem`

---

## System Overview

```
multi-agent-patterns/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
└── skills/
    └── multi-agent-patterns/
        ├── SKILL.md             # Core skill (patterns, context isolation, consensus, failure modes)
        ├── references/
        │   └── frameworks.md    # LangGraph, AutoGen, CrewAI implementation patterns
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

The plugin is a single skill with one deep-dive reference. The SKILL.md covers architecture selection, context isolation, consensus, and failure modes. The frameworks reference provides implementation code for LangGraph (graph-based state machines), AutoGen (event-driven GroupChat), and CrewAI (role-based hierarchical crews).

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `multi-agent-patterns` | Skill | Architecture pattern selection, context isolation, consensus mechanisms, failure modes |
| `frameworks.md` | Reference | LangGraph supervisor/swarm implementation, AutoGen GroupChat, CrewAI hierarchical crews |

### Component Spotlight

#### multi-agent-patterns (skill)

**What it does:** Activates when you need to design, evaluate, or troubleshoot multi-agent LLM systems. Provides the three dominant architecture patterns with selection criteria, context isolation mechanisms, consensus protocols, and failure mode mitigations backed by production benchmark data.

**Input -> Output:** A description of your multi-agent requirements (task complexity, parallelization needs, coordination model) -> An architecture recommendation with pattern selection, context isolation strategy, consensus mechanism, and failure recovery design.

**When to use:**
- Single-agent context limits constrain task complexity
- Tasks decompose naturally into parallel subtasks
- Different subtasks require different tool sets or system prompts
- Building production systems with multiple specialized agent components
- Debugging existing multi-agent systems that bottleneck, diverge, or cascade errors

**When NOT to use:**
- Agent memory or persistence across sessions (use `memory-systems`)
- Tool design or function calling interfaces (use `tool-design`)
- Hosted agent infrastructure or sandboxed execution (use `hosted-agents`)
- BDI cognitive models or mental state modeling (use `bdi-mental-states`)

**Try these prompts:**

```
I'm building a research pipeline with search, analysis, and writing stages -- should I use a supervisor or let agents hand off to each other?
```

```
My supervisor agent is becoming a bottleneck -- it accumulates context from all workers and quality is degrading. How do I fix this?
```

```
Design a multi-agent debate system where three agents evaluate a business proposal and reach consensus without sycophancy
```

```
What's the token cost of going multi-agent? My single agent costs $0.50 per task -- what should I expect with a 3-agent supervisor setup?
```

```
Show me how to implement agent handoffs in a swarm architecture with explicit state passing
```

**Key references:**

| Reference | Topic |
|---|---|
| `frameworks.md` | LangGraph supervisor with state machines, AutoGen GroupChat patterns, CrewAI hierarchical process flows |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "How do I use multiple agents?" | "Design a supervisor architecture for a code review pipeline with security, performance, and style agents" |
| "Tell me about swarms" | "Should I use a swarm or supervisor pattern for a customer support system where requests route to billing, technical, or sales specialists?" |
| "My agents aren't working" | "My supervisor agent paraphrases sub-agent responses and loses important details -- how do I implement direct message forwarding?" |
| "Make my agent system better" | "My 3-agent research system costs 15x more tokens than a single agent -- is the quality improvement worth it?" |

### Structured Prompt Templates

**For architecture selection:**
```
I need a multi-agent system for [use case]. The task involves [describe subtasks]. Key requirements: [parallelizable / sequential], [centralized control / flexible routing], [human oversight needed / fully autonomous]. Which pattern fits?
```

**For failure diagnosis:**
```
My multi-agent system uses [pattern: supervisor/swarm/hierarchical] but I'm seeing [specific problem: bottleneck / divergence / error cascade / sycophancy]. Architecture: [describe agent roles and communication]. How do I fix this?
```

**For consensus design:**
```
I have [N] agents that need to [agree on / vote on / debate] [what]. How do I prevent [sycophancy / false consensus / deadlock] while ensuring [quality outcome]?
```

### Prompt Anti-Patterns

- **Designing by org chart** -- "I need a manager agent, worker agents, and a QA agent" anthropomorphizes roles instead of designing for context isolation; describe the task decomposition instead
- **Assuming multi-agent is always better** -- the skill includes token economics to help you evaluate whether multi-agent is justified; a single agent with better model choice may outperform a 3-agent system
- **Ignoring coordination cost** -- asking for "10 parallel agents" without considering that coordination overhead can negate parallelization benefits
- **Requesting implementation before architecture** -- ask for pattern selection first, then implementation details for the chosen pattern

## Real-World Walkthrough

**Starting situation:** You are building an automated code review system for a platform team. Currently, a single Claude agent handles all reviews -- security checks, performance analysis, style enforcement, test coverage assessment, and documentation quality. The context window fills up on large PRs, and review quality degrades as the agent tries to hold security rules, performance benchmarks, style guides, and test coverage thresholds simultaneously.

**Step 1: Evaluating the multi-agent case.** You ask: "My single code review agent degrades on large PRs because it's holding too many concerns in context. Should I split it into specialized agents?"

The skill confirms this is a strong multi-agent candidate: the subtasks (security, performance, style, tests, docs) are parallelizable, each benefits from different system prompts and tool sets, and you need centralized aggregation of findings. Token economics: expect ~15x token usage, but quality improvement on large PRs justifies the cost for a platform-wide tool. The skill also notes that upgrading to a stronger model may provide comparable gains at lower cost -- consider that first.

**Step 2: Pattern selection.** The skill recommends the supervisor/orchestrator pattern. Reasoning: you need a central coordinator to decompose the PR into review concerns, route to specialists, and aggregate findings into a unified review. The alternatives are weaker here -- swarm would risk divergent review standards, and hierarchical adds unnecessary layers for a flat review pipeline.

**Step 3: Solving the telephone game.** You ask about the supervisor synthesizing specialist findings, and the skill immediately flags the telephone game risk. It provides the `forward_message` pattern: specialist agents pass their review findings directly to the output rather than through supervisor synthesis. The supervisor handles routing and aggregation structure, but specialist outputs are preserved verbatim. LangGraph benchmarks show this eliminates the 50% fidelity loss.

**Step 4: Context isolation design.** The skill designs the isolation strategy: each specialist receives only the PR diff plus its domain-specific rules (security agent gets OWASP guidelines, performance agent gets benchmark thresholds, etc.). No specialist carries another specialist's context. The supervisor receives only structured summaries (severity, file, line, finding) rather than full specialist reasoning.

**Step 5: Consensus on conflicting findings.** The security agent flags a dependency as vulnerable; the performance agent recommends it for speed. The skill provides a weighted voting approach: security findings carry higher weight by default for public-facing code, with confidence scores from each agent. Conflicts are surfaced to the developer rather than auto-resolved.

**Step 6: Failure mode design.** The skill maps out recovery for each failure mode: supervisor bottleneck (output schema constraints so specialists return only distilled summaries), coordination overhead (batch results, minimize inter-agent communication), error propagation (validate specialist outputs before aggregation, circuit breaker on repeated failures), and divergence (clear objective boundaries per specialist with convergence checks).

**Final outcome:** A 5-specialist supervisor architecture with direct message forwarding, instruction-based context isolation, weighted consensus for conflicts, and failure recovery for the four primary failure modes. Review quality on large PRs improves because each specialist operates in a clean context focused on its domain, and the telephone game is eliminated.

**Gotchas discovered:** The skill warned that the supervisor itself needs context management -- receiving summaries from 5 specialists on a large PR can fill the supervisor's context. Solution: use structured output schemas (JSON with severity/file/line/finding) instead of free-text summaries.

## Usage Scenarios

### Scenario 1: Research pipeline with parallel search

**Context:** You are building a market research system that needs to search financial databases, news archives, social media, and patent filings simultaneously, then synthesize findings into a report.

**You say:** "Design a multi-agent research pipeline that searches four data sources in parallel and synthesizes findings. Each source requires different search tools and query strategies."

**The skill provides:**
- Supervisor pattern with four specialist agents (financial, news, social, patent) working in parallel
- Context isolation via instruction passing: each specialist gets only its search domain and query
- Aggregation strategy: supervisor receives structured findings (source, relevance, key facts) not raw search results
- Direct message forwarding for the final report to preserve specialist nuance

**You end up with:** A parallel research pipeline that completes in the time of the slowest source search rather than the sum of all four, with clean context isolation preventing cross-domain contamination.

### Scenario 2: Customer support routing

**Context:** You have a customer support system where requests need to route to billing, technical, or sales specialists based on intent, with smooth handoffs when a conversation shifts topics.

**You say:** "Should I use a supervisor or swarm for customer support routing? Conversations often shift from billing questions to technical issues mid-conversation."

**The skill provides:**
- Swarm/peer-to-peer pattern recommendation: conversations shift dynamically, rigid supervisor routing would require re-classification at every turn
- Handoff protocol with explicit state passing (conversation history, customer context, resolved issues)
- Context isolation: each specialist carries only its domain knowledge plus the handoff state
- Convergence constraint: conversations must resolve within a specialist, not ping-pong between agents

**You end up with:** A swarm architecture where agents hand off based on conversation intent shifts, with explicit state passing that preserves context without accumulation.

### Scenario 3: Multi-agent debate for decision quality

**Context:** You want three agents to evaluate a product strategy proposal from different perspectives (market opportunity, technical feasibility, financial viability) and reach a consensus recommendation.

**You say:** "Design a multi-agent debate where three agents evaluate a business proposal from different angles and reach consensus without falling into sycophancy."

**The skill provides:**
- Debate protocol with adversarial critique over multiple rounds
- Sycophancy triggers: detection when agents mimic each other's answers without unique reasoning
- Weighted voting based on domain expertise (market agent's opinion weighted higher on market questions)
- Stall triggers: escalation when no progress is made after N rounds

**You end up with:** A structured debate system with explicit anti-sycophancy mechanisms and weighted consensus, producing a multi-perspective evaluation that avoids false agreement.

### Scenario 4: Hierarchical task execution

**Context:** You are building a project management agent system where high-level goals need to decompose into plans, then into executable tasks, with different levels of abstraction at each layer.

**You say:** "I need a hierarchical agent system: strategy layer defines goals, planning layer creates tasks, execution layer implements them. How do I prevent misalignment between layers?"

**The skill provides:**
- Three-layer hierarchical pattern with explicit interface contracts between layers
- Strategy-to-planning interface: goals with measurable success criteria
- Planning-to-execution interface: atomic tasks with input/output schemas
- Misalignment detection: execution results verified against planning expectations, with escalation to strategy when drift exceeds threshold

**You end up with:** A hierarchical architecture with contracts between layers that detect misalignment early rather than discovering it after execution completes.

---

## Decision Logic

**When Supervisor vs Swarm vs Hierarchical?**

- **Supervisor/Orchestrator** -- when tasks have clear decomposition, you need centralized control, human oversight matters, or you need to aggregate results from parallel workers. Most common pattern. Risk: supervisor bottleneck and telephone game.
- **Peer-to-Peer/Swarm** -- when tasks require flexible routing, conversations shift dynamically between domains, or rigid planning is counterproductive. Best for customer-facing agents with unpredictable intent. Risk: divergence without convergence constraints.
- **Hierarchical** -- when the problem has natural abstraction layers (strategy -> planning -> execution), mirrors organizational structure, or requires different context structures at different levels. Best for large-scale project management. Risk: misalignment between layers and complex error propagation.

**When is multi-agent NOT justified?**

When a single agent with a better model achieves comparable quality. Claude Sonnet 4.5 showed larger performance gains than doubling tokens on earlier Sonnet versions. Check model upgrade before adding agent complexity. Also unjustified when coordination overhead exceeds parallelization benefit -- typically when subtasks are sequential, not parallel.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Supervisor bottleneck | Supervisor context fills from worker outputs, quality degrades on complex tasks | Constrain worker output schemas to structured summaries; checkpoint supervisor state |
| Telephone game | Supervisor paraphrases specialist output, losing critical details | Implement `forward_message` for direct pass-through; use structured output schemas |
| Swarm divergence | Agents pursue different goals, outputs are irreconcilable | Define objective boundaries per agent; add convergence checks and time-to-live limits |
| Sycophantic consensus | Agents agree on false premises without independent reasoning | Use debate protocols with adversarial critique; add sycophancy triggers for detection |
| Error propagation | One agent's hallucination poisons all downstream consumers | Validate outputs before passing between agents; circuit breakers on repeated failures |
| Token cost explosion | Multi-agent system costs 15x single agent without proportional quality gain | Evaluate token economics first; consider model upgrade before multi-agent architecture |

## Integration Patterns

- **memory-systems + multi-agent-patterns** -- shared persistent memory across agents using file-system coordination or entity registries, enabling agents to build on each other's findings across sessions
- **tool-design + multi-agent-patterns** -- specialized tool sets per agent, reducing context overhead by giving each agent only the tools it needs
- **context-optimization + multi-agent-patterns** -- context partitioning strategies that complement agent-level context isolation

## Ideal For

- **Platform engineers** building production multi-agent systems who need architecture patterns backed by benchmark data and failure mode analysis
- **Agent developers** hitting single-agent context limits who need to evaluate whether multi-agent architecture is justified for their use case
- **Teams with existing multi-agent systems** experiencing bottlenecks, divergence, or error cascades and needing systematic diagnosis and fixes
- **Architects** designing customer-facing agent systems that need dynamic routing, handoffs, and consensus mechanisms
- **Technical leads** evaluating LangGraph vs AutoGen vs CrewAI for multi-agent implementation and needing framework-specific guidance

## Not For

- **Agent memory** -- persistent state across sessions is handled by `memory-systems`, not coordination patterns
- **BDI cognitive models** -- mental state modeling with beliefs, desires, and intentions uses `bdi-mental-states`
- **Hosted agent infrastructure** -- sandboxed execution, VM management, and deployment patterns use `hosted-agents`
- **Single-agent optimization** -- if your problem fits in one context window, use `context-optimization` instead of adding agents

## Related Plugins

- **memory-systems** -- shared state management across agents, entity consistency, temporal knowledge graphs
- **bdi-mental-states** -- cognitive architecture for individual agents within a multi-agent system
- **tool-design** -- designing tool interfaces for specialized agents
- **context-fundamentals** -- context engineering foundations that multi-agent patterns build upon
- **context-degradation** -- diagnosing context failures that often manifest as multi-agent coordination problems
- **hosted-agents** -- infrastructure for deploying and running multi-agent systems in production

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
