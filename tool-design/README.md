# Tool Design

> **v1.0.4** | Agent Architecture | 5 iterations

> Design tools that agents actually use correctly -- the difference between an agent that completes tasks and one that flails.

## The Problem

When an agent system underperforms, teams blame the model, the prompts, or the orchestration logic. In practice, the single largest source of agent failure is the tool interface itself. Overlapping tool descriptions cause the agent to pick the wrong tool -- not occasionally, but systematically. Vague parameter names like `query`, `val`, or `param1` force the model to guess what to pass. Missing error context means that when a tool call fails, the agent has no path to recovery and either retries blindly or gives up.

The problem compounds as tool collections grow. Each new tool adds description tokens that eat into the context budget. Each tool with a scope that partially overlaps another tool creates selection ambiguity. Teams that started with 5 clear tools end up with 30+ fuzzy ones, and task completion drops even though each individual tool "works." The standard response -- more prompt engineering, longer system messages, few-shot examples of correct tool use -- treats the symptom while the disease spreads.

Most teams design tools the way they design human-facing APIs: clear enough for a developer who can read documentation, run experiments, and build mental models over time. But an agent gets one shot. It reads a description, infers a contract, and generates a call. Every ambiguity in that description is a coin flip. No amount of retry logic fixes a tool set where the agent cannot reliably distinguish tool A from tool B.

## The Solution

This plugin applies two core principles -- the Consolidation Principle and Architectural Reduction -- to transform how you design agent tools. The Consolidation Principle says: if a human engineer cannot definitively say which tool to use in a given situation, an agent cannot either. The fix is merging overlapping tools into single comprehensive tools with unambiguous scopes, cutting tool count from 30+ to the recommended 10-20 range.

Architectural Reduction takes this further. A production text-to-SQL agent was rebuilt from 17 specialized tools (GetEntityJoins, LoadCatalog, SearchSchema, etc.) down to 2 primitive tools (ExecuteCommand, ExecuteSQL). The result: average execution time dropped from 275s to 77s, success rate went from 80% to 100%, and token usage dropped 37%. The plugin teaches you when this radical simplification works and when it does not.

Beyond consolidation, the skill provides a four-question framework for description engineering (what does it do, when should it be used, what inputs does it accept, what does it return), error message design that enables agent self-correction, response format optimization for token efficiency, and MCP naming conventions that prevent "tool not found" failures.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent picks the wrong tool when multiple tools have overlapping descriptions | Each tool has an unambiguous scope -- the Consolidation Principle eliminates overlap |
| Tool errors return generic messages; agent retries blindly | Error messages include recovery guidance: retry timing, corrected format, alternatives |
| Tool collection grows to 30+ tools, consuming context budget | Tool set stays in the 10-20 range with namespacing for logical grouping |
| Parameter names like `query`, `val`, `x` force the model to guess | Parameters follow consistent naming conventions with types, constraints, and defaults |
| Specialized wrapper tools constrain what the model can do | Primitive tools let the model chain capabilities flexibly |
| Tool descriptions say "Search the database" with no usage context | Descriptions answer what, when, inputs, and outputs with concrete examples |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install tool-design@skillstack
```

### Prerequisites

No additional dependencies. Works with any Claude Code session.

### Verify installation

After installing, test with:

```
Review my agent's tool set -- I have 25 tools and the agent keeps picking the wrong one
```

## Quick Start

1. Install the plugin with the commands above
2. Describe your situation: `My agent has 20 tools and frequently calls the wrong one when the user asks about customer data`
3. The skill analyzes your tool set for overlap, ambiguity, and description quality
4. You get a concrete consolidation plan: which tools to merge, how to rewrite descriptions, and what error contracts to add
5. Next, try: `Should I give my agent file system access or build custom tools for data exploration?`

## What's Inside

This is a **single-skill plugin** with deep reference material and eval coverage.

| Component | Purpose |
|---|---|
| `skills/tool-design/SKILL.md` | Core methodology: Consolidation Principle, Architectural Reduction, description engineering, error message design, MCP naming, tool collection sizing |
| `references/best_practices.md` | Extended guidelines: description structure, naming conventions, error message schemas, response format optimization, anti-pattern catalog, design checklist |
| `references/architectural_reduction.md` | Production case study: text-to-SQL agent rebuilt from 17 specialized tools to 2 primitives -- 3.5x faster, 37% fewer tokens, 100% success rate |
| `evals/trigger-evals.json` | 13 trigger scenarios including 3 NOT-for boundary tests |
| `evals/evals.json` | 3 output quality scenarios for design walkthroughs, reviews, and greenfield setup |

### tool-design

**What it does:** Activates when you need to design, review, or optimize tools that agents use. It walks you through the Consolidation Principle to merge overlapping tools, Architectural Reduction to eliminate unnecessary complexity, description engineering to make each tool unambiguous, and error message design that gives agents a path to recovery. Works for greenfield tool design and retrofitting existing tool sets.

**Try these prompts:**

```
I'm building an agent that manages cloud infrastructure -- help me design the tool set from scratch
```

```
My agent has 25 tools and keeps calling searchCustomers when it should call getCustomerById -- what's wrong?
```

```
Review this tool description and tell me why agents might misuse it: "search(query: str) -> Search the database"
```

```
Should I build a custom data exploration tool or just give the agent bash access to query files directly?
```

```
How should I write error messages so my agent can recover instead of retrying the same bad call?
```

**Key references:**

| Reference | Topic |
|---|---|
| `best_practices.md` | Description structure, naming conventions, error schemas, response format optimization, anti-pattern catalog |
| `architectural_reduction.md` | Production case study: 17 specialized tools reduced to 2 primitives with measurable performance gains |

## Real-World Walkthrough

You are building an internal support agent for a SaaS company. The agent needs to look up customer accounts, check subscription status, view recent support tickets, search the knowledge base, and escalate issues to human agents. Your first pass produces 12 tools:

```
getCustomer, searchCustomers, getSubscription, listSubscriptions,
getTicket, searchTickets, createTicket, updateTicket,
searchKnowledgeBase, getArticle, escalateToHuman, getAgentAvailability
```

You deploy and immediately see problems. When a user says "what's going on with Acme Corp's account?", the agent calls `searchCustomers` instead of `getCustomer` because it does not know whether the user has a customer ID or a name. When a user asks "are there similar tickets?", the agent calls `searchKnowledgeBase` instead of `searchTickets` because "similar" could mean knowledge base articles or past tickets.

You ask the skill to review your tool set:

```
Review my support agent's 12 tools -- the agent keeps confusing searchCustomers with getCustomer and searchTickets with searchKnowledgeBase
```

The skill applies the Consolidation Principle. It identifies three overlap clusters: `getCustomer`/`searchCustomers` (both retrieve customer data), `getTicket`/`searchTickets` (both retrieve ticket data), and `searchKnowledgeBase`/`getArticle` (both retrieve knowledge content). The recommendation: merge each pair into a single tool that accepts flexible identifiers.

`lookupCustomer` replaces both customer tools. It accepts an ID, email, or company name and returns the right customer. No ambiguity about which tool to call -- there is only one. `lookupTicket` replaces both ticket tools, accepting a ticket ID, customer reference, or search keywords. `lookupKnowledge` replaces both knowledge tools.

Your 12 tools become 7: `lookupCustomer`, `lookupTicket`, `lookupKnowledge`, `createTicket`, `updateTicket`, `escalateToHuman`, `getAgentAvailability`. But the skill does not stop there.

It examines description quality. Your `escalateToHuman` tool description says "Escalate the current issue to a human agent." The skill flags this: when should the agent escalate? What information should it include? The revised description specifies triggers (customer explicitly requests human help, issue requires account-level changes the agent cannot make, three failed resolution attempts), required parameters (customer ID, conversation summary, attempted solutions), and return value (escalation ID and estimated wait time).

It also examines error messages. Your `createTicket` tool returns `{"error": "Invalid priority"}` when the agent passes an unsupported priority level. The skill rewrites this to `{"error": "INVALID_PRIORITY", "message": "Priority must be one of: low, medium, high, critical", "provided": "urgent", "suggestion": "Did you mean 'high'? Use 'critical' only for production outages."}` -- giving the agent everything it needs to self-correct on the next call.

After consolidation and description improvements, the agent's task completion rate on your internal test suite goes from 72% to 91%. Tool selection accuracy jumps from 68% to 95%. The total description token count drops by 40%, freeing context for longer conversations.

The entire process -- from "my agent keeps picking the wrong tool" to a redesigned, tested tool set -- takes one focused session. No model changes, no prompt rewrites, no orchestration logic changes. Just better tools.

## Usage Scenarios

### Scenario 1: Greenfield agent tool set design

**Context:** You are starting a new agent project -- a coding assistant that can read files, run tests, search code, and manage git operations. You need to design the initial tool set before writing any implementation.

**You say:** `I'm building a coding assistant agent -- help me design the tool set. It needs to handle file operations, test running, code search, and git.`

**The skill provides:**
- Workflow decomposition: what distinct agent tasks map to which tools
- Consolidation analysis: where a single tool can cover multiple related actions (e.g., `fileOperation` covering read, write, list, and search)
- Description templates for each tool following the four-question framework
- Recommended tool count (10-20) with namespacing strategy for growth

**You end up with:** A documented tool set design with unambiguous scopes, complete descriptions, and error contracts -- ready to implement.

### Scenario 2: Debugging tool selection failures

**Context:** Your customer service agent has 30 tools and keeps calling the wrong one. When users ask about order status, it sometimes calls `getOrder`, sometimes `searchOrders`, and sometimes `getCustomerHistory`.

**You say:** `My agent has 30 tools and frequently picks the wrong one -- here are the three tools it confuses most. How do I fix this?`

**The skill provides:**
- Overlap analysis identifying which tools have ambiguous scopes
- Consolidation plan merging overlapping tools into single comprehensive tools
- Rewritten descriptions with clear "when to use" triggers
- Before/after comparison showing eliminated ambiguity

**You end up with:** A reduced tool set (likely 15-18 tools) where each tool has a unique, unambiguous purpose.

### Scenario 3: Deciding between custom tools and primitives

**Context:** You are building a data analysis agent and debating whether to create specialized tools (QueryDatabase, VisualizePlot, SummarizeData) or give the agent access to bash and SQL directly.

**You say:** `Should I build custom data analysis tools or just give the agent bash and SQL access? Our data is in PostgreSQL and well-documented.`

**The skill provides:**
- The Architectural Reduction framework with the text-to-SQL case study (17 tools to 2)
- Decision criteria: documentation quality, data consistency, model capability, safety requirements
- Risk assessment for the primitive approach in your specific context
- Hybrid recommendations where some specialized tools complement primitive access

**You end up with:** A clear decision with rationale, plus an implementation plan for whichever approach fits your situation.

### Scenario 4: Writing tool descriptions that work

**Context:** You have a working tool but agents misuse it. The tool fetches pricing data, but agents call it when they should be using the product catalog tool instead.

**You say:** `Agents keep calling my pricing tool when they should use the product catalog. Here's the current description -- what's wrong with it?`

**The skill provides:**
- Diagnosis of description weaknesses (missing "when to use" context, vague scope)
- Rewritten description following the four-question framework
- Negative triggers ("NOT for product catalog lookups -- use `getProductCatalog` for feature/spec questions")
- Error message improvements for common misuse patterns

**You end up with:** A revised tool description that agents select correctly, plus patterns to apply to your other tools.

### Scenario 5: Optimizing tool response formats

**Context:** Your agent is running out of context window because tool responses return full objects with 40+ fields when the agent usually only needs 3-4 fields.

**You say:** `My tool responses are huge -- 40 fields per object -- and they're eating my agent's context. How do I fix this without breaking functionality?`

**The skill provides:**
- Response format optimization strategy: concise vs detailed modes
- Implementation pattern for format parameters (`format: "concise" | "detailed"`)
- Guidance on which fields to include in concise mode (the ones agents actually use for decisions)
- Description additions that teach agents when to request which format

**You end up with:** Tool responses that default to minimal tokens, with detailed mode available when the agent explicitly needs full context.

## Ideal For

- **Teams whose agents pick the wrong tool** -- the Consolidation Principle directly eliminates the most common source of tool selection errors
- **Agent architects starting greenfield projects** -- the design framework prevents the tool sprawl that cripples agents at 30+ tools
- **Engineers maintaining large tool collections** -- Architectural Reduction provides a principled approach to simplifying without losing capability
- **Anyone writing tool descriptions** -- the four-question framework and anti-pattern catalog turn vague docs into precise contracts

## Not For

- **Building MCP servers or implementing the MCP protocol** -- use [mcp-server](../mcp-server/) for server implementation, transport layer, and protocol compliance
- **Designing multi-agent coordination or agent handoffs** -- use [multi-agent-patterns](../multi-agent-patterns/) for supervisor/worker topologies, swarm architectures, and inter-agent communication
- **Implementing agent memory or persistence** -- use [memory-systems](../memory-systems/) for episodic, semantic, and procedural memory architectures

## How It Works Under the Hood

The plugin is a single skill with two reference documents providing depth. When activated, the skill loads the core methodology covering the Consolidation Principle, Architectural Reduction, description engineering, error message design, and MCP naming conventions.

The `best_practices.md` reference extends the core with detailed description structure patterns, naming convention rules, error message schemas, response format optimization techniques, and a complete anti-pattern catalog with a design checklist.

The `architectural_reduction.md` reference provides production evidence: the full case study of a text-to-SQL agent rebuilt from 17 specialized tools to 2 primitives, with before/after metrics on execution time, success rate, and token usage.

The skill activates from natural language -- mentioning tool design, MCP tools, consolidation, or architectural reduction triggers it automatically. No slash commands needed.

## Related Plugins

- **[Agent Evaluation](../agent-evaluation/)** -- Measure tool usage effectiveness with rubrics and LLM-as-judge scoring
- **[Agent Project Development](../agent-project-development/)** -- End-to-end agent project methodology including tool selection strategy
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Coordination patterns where each agent gets its own tool set
- **[MCP Server](../mcp-server/)** -- Build the MCP servers that expose the tools this skill teaches you to design
- **[Memory Systems](../memory-systems/)** -- Agent memory architectures that complement well-designed tool interfaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
