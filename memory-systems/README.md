# Memory Systems

> **v1.0.5** | Agent Architecture | 6 iterations

> Production memory architectures for LLM agents -- choose the right framework, design retrieval that scales, and stop losing context between sessions.

## The Problem

Every time an LLM agent session ends, everything it learned disappears. User preferences, prior decisions, accumulated domain knowledge, entity relationships -- gone. The next session starts from zero, and the user has to re-explain context they already provided. This is not a minor inconvenience; it fundamentally limits what agents can do.

The naive fix -- stuffing all prior interactions into the prompt -- hits context limits fast and degrades response quality as the window fills up. Teams that try unstructured vector dumps find that retrieval accuracy erodes as memory grows: the agent confidently surfaces outdated facts, confuses entities with similar names, and cannot answer questions that require connecting information across multiple past conversations.

Choosing a memory framework is its own maze. Mem0, Zep/Graphiti, Letta, Cognee, and LangMem each make compelling claims, but their architectures differ fundamentally -- vector stores vs. temporal knowledge graphs vs. self-editing tiered storage. Without benchmark data and clear trade-off analysis, teams pick based on marketing, discover limitations six weeks later, and face a costly migration. Meanwhile, the agent keeps forgetting.

## The Solution

This plugin gives you a structured decision framework for designing agent memory that actually persists. It walks you through the five-layer memory model (working, short-term, long-term, entity, temporal knowledge graph), helps you choose the right layer for each type of knowledge, and provides side-by-side framework comparisons backed by real benchmark numbers -- Letta's 74% on LoCoMo, Zep's 94.8% DMR accuracy, Cognee's top HotPotQA scores.

You get an architecture progression path that starts simple (file-system memory for prototyping) and scales incrementally through vector stores, graph databases, and temporal knowledge graphs -- adding complexity only when retrieval quality demands it. Each step includes working code, integration patterns, and the specific signals that tell you it is time to move to the next tier.

The skill also covers the hard operational problems: memory consolidation strategies that prevent unbounded growth, temporal validity tracking so stale facts do not poison context, hybrid retrieval approaches that combine semantic search with graph traversal, and error recovery patterns for empty results, conflicting facts, and storage failures.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent forgets everything between sessions; users re-explain context repeatedly | Layered memory architecture retains preferences, decisions, and domain knowledge across sessions |
| Pick a memory framework based on blog posts and hope it works | Side-by-side benchmark comparison (LoCoMo, DMR, HotPotQA) with concrete numbers for evidence-based decisions |
| Naive vector dump degrades as memory grows; retrieval accuracy drops silently | Hybrid retrieval strategies (semantic + keyword + graph) with consolidation triggers that maintain quality at scale |
| Outdated facts surface alongside current ones, confusing the agent | Temporal knowledge graph patterns with validity intervals -- stale facts are invalidated, not deleted |
| Over-engineer a complex memory system on day one and waste weeks | Architecture progression path: file-system to vector store to temporal KG, adding complexity only when needed |
| Entity confusion -- "John Doe" in session 3 is a different person than session 7 | Entity registry patterns with consistent identity tracking across conversations |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install memory-systems@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Start a conversation about your agent's memory needs:
   ```
   My chatbot forgets user preferences between sessions -- how should I add persistent memory?
   ```
3. The skill provides a layered memory architecture tailored to your use case, starting with the simplest approach that works.
4. Ask for framework-specific guidance:
   ```
   Compare Mem0 and Cognee for my use case -- I need multi-hop reasoning over customer support history
   ```
5. Get working integration code and a progression path for scaling your memory layer as your agent grows.

## What's Inside

Single-skill plugin with deep reference material and evaluation suites.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering framework landscape, memory layer decision matrix, retrieval strategies, architecture progression, error recovery, and production guidelines |
| **references/implementation.md** | Working code for vector store implementation, Mem0 integration, temporal relationship queries, Cognee knowledge graph ingestion and search, and memory consolidation patterns |
| **references/latest-research-2026.md** | Current benchmark landscape (LoCoMo, LongMemEval, DMR, HotPotQA), detailed framework state for all five production systems, emerging research, and decision matrix |
| **evals/** | 15 trigger evaluation cases + 3 output quality evaluation cases |

### memory-systems

**What it does:** Activates when you need to design, implement, or troubleshoot persistent memory for LLM agents. It provides a decision framework spanning five production frameworks (Mem0, Zep/Graphiti, Letta, Cognee, LangMem), five memory layers (working through temporal knowledge graph), and four retrieval strategies -- all backed by benchmark data from LoCoMo, LongMemEval, DMR, and HotPotQA.

**Try these prompts:**

```
My agent loses context between sessions -- how do I fix that?
```

```
Which memory framework should I use for a multi-tenant customer support bot: Mem0, Zep, or Cognee?
```

```
I need to track how user preferences change over time without losing the history of what they used to prefer
```

```
My agent's memory retrieval is getting slow and less accurate as the knowledge base grows -- what do I do?
```

```
Walk me through adding Cognee's knowledge graph to my existing RAG pipeline for multi-hop reasoning
```

```
A user changed their address but my agent keeps surfacing the old one -- how do I handle facts that change?
```

**Key references:**

| Reference | Topic |
|---|---|
| `implementation.md` | Working code patterns for vector stores, Mem0, Cognee, temporal queries, and memory consolidation |
| `latest-research-2026.md` | 2025-2026 benchmark data, detailed framework comparisons, emerging research directions, and production patterns at scale |

## Real-World Walkthrough

You are building a customer support agent for a SaaS platform with 50,000 active users. The agent handles billing questions, feature requests, and technical troubleshooting. Right now, every session starts cold -- a user who explained their complex enterprise setup three times last month has to do it again today.

**Step 1: Assess your memory needs.**

You start by describing the situation:

```
I'm building a support agent for a SaaS platform. Users come back repeatedly, and the agent needs to remember their account context, prior issues, and preferences. We have 50K users and need multi-tenant isolation. What memory architecture should I use?
```

The skill walks you through the memory layer decision matrix. For your case, you need: working memory (current conversation scratchpad), long-term memory (user preferences and account context persisted across sessions), and entity memory (tracking that "Acme Corp" is the same customer across all their support tickets). You do not need a full temporal knowledge graph yet -- your facts mostly do not change retroactively.

**Step 2: Choose a framework.**

The skill presents the framework comparison table with benchmark numbers. For multi-tenant SaaS with 50K users, Mem0 stands out: it was designed for multi-tenant isolation, offers managed infrastructure for fast deployment, and scored 68.5% on LoCoMo. Cognee scores higher on multi-hop reasoning benchmarks, but your support queries are mostly direct factual lookups ("What plan is this user on?"), not multi-hop chains. You go with Mem0 for now, knowing you can migrate later if reasoning demands grow.

**Step 3: Implement the memory layer.**

You ask for integration guidance:

```
Show me how to integrate Mem0 for user-scoped memory with preference tracking and prior issue history
```

The skill provides the Mem0 integration pattern -- adding memories scoped by `user_id`, searching with semantic queries, and handling the case where a user's preference changes (Mem0 surfaces the most recent fact). You implement a memory layer that stores three types of information per user: account context (plan, team size, integrations), interaction history (prior issues and resolutions), and stated preferences (communication style, technical depth).

**Step 4: Add entity tracking.**

Two weeks in, you notice the agent sometimes confuses users who share a company account. You ask:

```
How do I maintain consistent entity identity when multiple users belong to the same organization?
```

The skill guides you to add an entity registry layer on top of Mem0. Each organization and user gets a stable entity ID. When the agent encounters "Acme Corp", it resolves to the same entity regardless of which team member is chatting. The entity registry links users to their organization, so the agent can say "I see your colleague Maria reported a similar issue last week" without confusing identities.

**Step 5: Plan for scale.**

Three months later, with growing memory per user, retrieval latency creeps up and some queries return stale information. You ask:

```
My memory retrieval is getting slower and sometimes surfaces outdated billing info -- how do I fix this at scale?
```

The skill identifies two issues: no consolidation strategy (memory is growing unbounded) and no temporal validity on billing facts. It recommends adding consolidation triggers (when a user's memory count exceeds a threshold, summarize and archive older entries) and temporal validity metadata on facts that change (plan upgrades, billing changes). If these measures are not enough, the architecture progression path shows when to consider migrating to Zep/Graphiti for native temporal knowledge graph support -- but only when the data justifies the infrastructure investment.

The result: your support agent now remembers each user's context across sessions, resolves entity identity correctly, manages memory growth through consolidation, and handles changing facts without surfacing stale information. Support satisfaction scores improve because users stop repeating themselves, and the agent can reference prior interactions to provide contextually rich responses.

## Usage Scenarios

### Scenario 1: Choosing a memory framework for a new project

**Context:** You are starting an agent project and need to decide between Mem0, Zep/Graphiti, Letta, and Cognee before writing any code.

**You say:** "I'm building a research assistant that needs to accumulate domain knowledge across sessions and answer questions that connect information from multiple sources. Which memory framework should I use?"

**The skill provides:**
- Side-by-side framework comparison with architecture differences and trade-offs
- Benchmark numbers relevant to multi-hop reasoning (HotPotQA scores, LoCoMo results)
- Architecture-specific strengths: Cognee's multi-layer semantic graphs for interconnected knowledge, Zep's temporal model for evolving facts
- A recommendation based on your specific retrieval pattern (multi-hop vs. direct lookup)

**You end up with:** An evidence-based framework choice with a clear rationale you can explain to your team, plus an implementation starting point.

### Scenario 2: Debugging degraded retrieval quality

**Context:** Your agent has been running in production for months. Users report it sometimes gives outdated answers or misses relevant context it used to surface correctly.

**You say:** "My agent's memory worked well initially but now it's returning stale results and missing relevant context. Memory has grown to 200K entries. What's going wrong?"

**The skill provides:**
- Diagnostic checklist: unbounded growth, no consolidation, missing temporal validity
- Consolidation trigger strategies (count-based, quality-based, scheduled)
- Hybrid retrieval patterns that combine semantic search with graph traversal for better accuracy
- The "invalidate but don't discard" principle for handling stale facts
- Monitoring patterns for memory growth and retrieval latency

**You end up with:** A consolidation strategy and retrieval upgrade plan that restores accuracy without losing historical context.

### Scenario 3: Adding temporal awareness to existing memory

**Context:** Your agent tracks user profiles but surfaces outdated information when facts change -- old addresses, previous job titles, expired subscription plans.

**You say:** "A fact changed -- how do I update memory without poisoning old context? Users change jobs, move addresses, upgrade plans, and my agent keeps mixing old and new information."

**The skill provides:**
- Temporal knowledge graph patterns with `valid_from` and `valid_until` intervals
- The bi-temporal model (when the fact was true vs. when it was recorded)
- Working code for temporal relationship queries
- Migration path from flat memory to temporal-aware storage
- Zep/Graphiti's native temporal model vs. building temporal tracking on top of Mem0

**You end up with:** A temporal validity layer that correctly answers "What was true at time T?" while preserving full history.

### Scenario 4: Designing memory for multi-agent systems

**Context:** You have multiple specialized agents (planner, researcher, executor) that need to share accumulated knowledge without duplicating storage or creating conflicts.

**You say:** "I have three agents that each discover different things during a task. How do I share memory across agents without conflicts when two agents update the same entity?"

**The skill provides:**
- Shared memory architecture patterns with conflict resolution strategies
- Entity registry design for multi-agent identity consistency
- Framework-specific multi-agent support (Letta's agent-scoped vs. shared memory tiers)
- Cross-reference to multi-agent-patterns for coordination concerns beyond memory

**You end up with:** A shared memory layer design with clear ownership rules and conflict resolution, plus pointers to multi-agent-patterns for the coordination aspects.

## Ideal For

- **Teams building production agents that need cross-session memory** -- the framework comparison and benchmark data prevent weeks of trial-and-error with the wrong tool
- **Developers migrating from naive vector stores to structured memory** -- the architecture progression path shows exactly when and why to add complexity
- **Architects evaluating memory frameworks (Mem0, Zep, Letta, Cognee)** -- side-by-side benchmarks on LoCoMo, DMR, and HotPotQA replace guesswork with evidence
- **Engineers debugging degraded retrieval in production** -- error recovery patterns, consolidation strategies, and monitoring guidelines address real operational pain
- **Anyone building agents that track entities and relationships over time** -- temporal knowledge graph patterns with validity intervals solve the stale-fact problem

## Not For

- **Multi-agent coordination and handoffs** -- use [multi-agent-patterns](../multi-agent-patterns/) for supervisor architectures, communication protocols, and agent orchestration
- **Tool design and agent tool interfaces** -- use [tool-design](../tool-design/) for designing the tools agents call, not the memory they persist
- **Hosted agent infrastructure and sandboxed execution** -- use [hosted-agents](../hosted-agents/) for VM provisioning, sandboxing, and deployment patterns
- **Context window optimization without persistent storage** -- use [context-optimization](../context-optimization/) for making the most of a single session's context

## How It Works Under the Hood

The skill is structured around a progressive disclosure model. The core SKILL.md provides the framework landscape, memory layer decision matrix, retrieval strategies, and practical guidance -- enough for most decisions. When you need implementation detail, the skill draws on two reference files:

**implementation.md** contains working code patterns: a from-scratch vector store, Mem0 integration with user-scoped memory, temporal relationship queries with validity intervals, Cognee knowledge graph ingestion and multi-hop search, and memory consolidation routines. These are not toy examples -- they cover error handling, edge cases, and production considerations.

**latest-research-2026.md** tracks the current state of the field as of March 2026: benchmark results across LoCoMo, LongMemEval, DMR, and HotPotQA for all five frameworks, architectural deep-dives into each framework's internals, emerging research directions (sleep-time compute, memory-augmented transformers), and a decision matrix that maps use cases to framework recommendations.

The evaluation suite (15 trigger cases, 3 output quality cases) ensures the skill activates reliably on memory-related queries and produces structurally sound guidance.

## Related Plugins

- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems with shared memory across agents
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity with memory-based context loading
- **[Agent Evaluation](../agent-evaluation/)** -- Evaluation frameworks for measuring memory quality and agent performance
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted agents that need persistent state
- **[BDI Mental States](../bdi-mental-states/)** -- BDI cognitive architecture with belief management that connects to memory systems

## Version History

- `1.0.5` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins
- `1.0.4` fix(memory-systems): add standard keywords and expand README to full format
- `1.0.3` fix: change author field from string to object in all plugin.json files
- `1.0.2` fix: rename all claude-skills references to skillstack
- `1.0.1` docs: add 2025-2026 research references for context and memory plugins
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
