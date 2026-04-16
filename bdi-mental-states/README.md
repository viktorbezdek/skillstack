# BDI Mental States

> **v1.0.4** | Belief-Desire-Intention cognitive architecture for LLM agents -- formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration.
> 1 skill | 4 references | 15 trigger evals, 3 output evals

## The Problem

LLM agents today operate as opaque input-output functions. They receive a prompt, produce a response, and offer no structured insight into why they chose one action over another. When an agent fails -- makes a bad decision, pursues a contradictory goal, or acts on stale information -- there is no formal way to trace the failure back through its reasoning chain. You can inspect the prompt and the output, but the cognitive process in between is a black box.

This opacity becomes critical in multi-agent systems. When Agent A needs to communicate its understanding of the world to Agent B, it can only pass unstructured text. There is no standard vocabulary for saying "I believe X is true because of evidence Y" or "I intend to do Z because it fulfills desire W." Teams build ad hoc message formats, but these do not compose across systems and cannot be validated against formal reasoning rules. The result is agents that cannot explain their decisions, cannot share structured knowledge, and cannot be audited for rational consistency.

The academic BDI (Belief-Desire-Intention) framework has solved these problems for decades in traditional agent systems. But adapting formal BDI ontology to work with LLM agents -- combining the reasoning power of language models with the structural rigor of cognitive architectures -- requires bridging two very different paradigms. Without guidance, teams either ignore cognitive structure entirely (losing explainability) or implement rigid rule systems that undermine the flexibility that makes LLMs valuable.

## The Solution

This plugin provides a formal BDI ontology for modeling agent mental states -- beliefs, desires, and intentions -- as first-class structured entities. It defines how external knowledge (RDF triples, world states) transforms into agent beliefs, how beliefs motivate desires, how desires commit to intentions, and how intentions specify executable plans. Every mental state is justified, temporally bounded, and traceable.

The core paradigm is T2B2T (Triples-to-Beliefs-to-Triples): external RDF context triggers belief formation through perception processes, BDI reasoning generates desires and intentions, and plan execution produces new RDF output that modifies the world state. This creates a bidirectional bridge between semantic knowledge graphs and agent cognition.

The skill also covers integration with production frameworks (SEMAS, JADE, JADEX), neuro-symbolic AI patterns (Logic Augmented Generation), compositional mental entities for selective updates, temporal reasoning with validity intervals, and SPARQL competency queries for validating implementations. The result is agents that can explain their reasoning, share structured mental states across platforms, and be formally audited for rational consistency.

## Context to Provide

BDI modeling requires precise description of the agent's perception sources, decision context, and what needs to be explainable or auditable. The more specific you are, the more grounded the ontology will be in your actual domain.

**What information to include in your prompt:**

- **Agent purpose**: What does the agent do? What kind of decisions does it make? (e.g., "monitors inventory levels and decides whether to reorder or alert procurement")
- **Perception sources**: What data does the agent receive? What format? (RDF knowledge graph, sensor streams, API responses, database records, user input)
- **World state aspects**: What facts about the world does the agent need to track? (current inventory levels, supplier status, market prices)
- **Goals and desires**: What does the agent want to achieve? List the end-states it pursues.
- **Constraints and policies**: What rules govern the agent's behavior? (only auto-reorder if supplier lead time < 5 days, escalate to human if confidence < 0.7)
- **Temporal requirements**: Do beliefs have expiry? (stock levels valid for 1 hour, market prices valid for 5 minutes)
- **Explainability requirements**: Who needs to trace decisions and to what depth? (regulators, auditors, developers, end users)
- **Integration targets**: Do you need FIPA ACL messaging, JADE/JADEX framework integration, or RDF output for downstream systems?

**What makes results better:**
- Describing a real failure mode ("the agent acts on stale supplier data because it doesn't know the data expired") directly maps to the temporal validity pattern
- Specifying what "explainability" means in your context ("regulators need to trace from loan decision back to specific data points") determines how deep the justification chains need to go
- Providing example inputs (a sample RDF triple set or a data record) enables concrete T2B2T modeling rather than abstract patterns
- Naming the multi-agent partners and what they need to share enables the inter-agent communication protocol design

**What makes results worse:**
- "Add BDI to my chatbot" without describing what the chatbot decides or why traceability matters
- Conflating what the agent believes with the actual world state (these are separate in BDI -- beliefs are the agent's representation, not the ground truth)
- Requesting a model without specifying whether justifications are required (unjustified beliefs are decorative, not auditable)

**Template prompt:**
```
Model the BDI cognitive architecture for an agent that [agent purpose]. The agent perceives [data sources and format]. It needs to track beliefs about [world state aspects]. Its goals are [desired end-states]. Constraints: [rules governing behavior]. Beliefs about [data type] should expire after [duration]. Explainability requirement: [who needs to trace decisions and to what depth]. Output format: RDF/Turtle with SPARQL validation queries.
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent reasoning is a black box -- no way to trace why a decision was made | Every mental state links to justifications: "I believe X because of evidence Y" |
| Multi-agent communication is unstructured text with ad hoc formats | Formal BDI ontology provides standard vocabulary for sharing beliefs, desires, and intentions |
| Stale beliefs persist indefinitely with no expiration mechanism | Temporal validity intervals on every mental state; SPARQL queries find active beliefs at any time |
| Complex beliefs are atomic -- updating one aspect requires replacing the whole thing | Compositional `hasPart` relations enable selective updates to belief components |
| No formal connection between what the agent knows and what it decides to do | Cognitive chain: beliefs motivate desires, desires commit to intentions, intentions specify plans |
| LLM outputs are unconstrained by formal reasoning rules | Logic Augmented Generation validates LLM output against ontological constraints |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install bdi-mental-states@skillstack
```

### Verify installation

After installing, test with:

```
Help me model the mental states for an agent that monitors stock prices and decides when to send alerts
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Model the belief-desire-intention chain for an agent that processes incoming emails and decides which ones need urgent attention`
3. The skill produces RDF/Turtle representations of beliefs (email attributes), desires (handle urgent items), and intentions (specific action plans)
4. Explore deeper: `Add temporal validity to the beliefs so stale information expires after 24 hours`
5. Validate: `Write SPARQL competency queries to verify the BDI model is consistent`

---

## System Overview

```
External World                    Agent Cognitive Architecture
+------------------+              +--------------------------------+
|                  |              |                                |
| RDF Knowledge    |  Triples    | +----------+    +-----------+  |
| Graph / World    | ---------> | | Belief   | -> | Desire    |  |
| State            |  to         | | Process  |    | Process   |  |
|                  |  Beliefs    | +----------+    +-----------+  |
|                  |              |      |               |        |
|                  |              |      v               v        |
|                  |              | +----------+    +-----------+  |
|                  |  Beliefs    | | Beliefs  |    | Desires   |  |
|                  | <--------- | |          | -> |           |  |
|                  |  to         | +----------+    +-----------+  |
|                  |  Triples    |      |               |        |
|                  |              |      v               v        |
+------------------+              | +-----------+  +-----------+  |
                                  | | Intention |  | Plans &   |  |
                                  | | Process   |->| Tasks     |  |
                                  | +-----------+  +-----------+  |
                                  +--------------------------------+
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `bdi-mental-states` | Skill | Core BDI ontology patterns, T2B2T paradigm, cognitive chains, temporal reasoning, and integration guidance |
| `bdi-ontology-core.md` | Reference | Core ontology design patterns and class definitions for Belief, Desire, Intention, WorldState, Plan, and Task |
| `rdf-examples.md` | Reference | Complete RDF/Turtle examples for all mental state types and relationships |
| `sparql-competency.md` | Reference | Validation queries: what beliefs motivated a desire, what desire an intention fulfills, plan task ordering |
| `framework-integration.md` | Reference | SEMAS rule translation, JADE/JADEX integration, Logic Augmented Generation patterns |

### Component Spotlights

#### bdi-mental-states (skill)

**What it does:** Activates when you need to model agent mental states using formal BDI architecture, transform RDF context into beliefs, build cognitive reasoning chains, implement the T2B2T paradigm, or integrate LLMs with formal cognitive structures. Provides ontology patterns in RDF/Turtle with SPARQL queries for validation.

**Input -> Output:** A description of agent behavior and reasoning needs -> Formal BDI model with RDF/Turtle representations of beliefs, desires, intentions, plans, and their relationships, plus SPARQL queries and integration patterns.

**When to use:**
- Processing external RDF context into structured agent beliefs
- Modeling rational agency with perception-deliberation-action cycles
- Building explainable agents with traceable reasoning chains
- Implementing BDI frameworks (SEMAS, JADE, JADEX)
- Augmenting LLMs with formal cognitive structures (Logic Augmented Generation)
- Coordinating mental states across multi-agent platforms
- Adding temporal reasoning to agent beliefs and intentions

**When NOT to use:**
- Multi-agent coordination or handoff protocols -> use `multi-agent-patterns`
- Agent memory persistence or retrieval frameworks -> use `memory-systems`
- Building formal ontologies for domain modeling -> use `ontology-design`

**Try these prompts:**

```
Model the BDI cognitive chain for a customer service agent. The agent perceives: customer account history (RDF triples), sentiment score from NLP analysis, and open ticket count. It should form beliefs about customer frustration level and issue urgency, develop a desire to resolve within SLA, and commit to an intention to either auto-resolve or escalate to a human based on belief combination. Show RDF/Turtle with justification links.
```

```
Implement the T2B2T paradigm for an industrial IoT agent. Input: RDF triples from a sensor knowledge graph (temperature, pressure, vibration readings per machine). The agent should form beliefs about equipment health (valid for 10 minutes), develop desires to maintain uptime, and output RDF triples that trigger maintenance orders or alerts. Show both directions of the T2B2T flow.
```

```
Add temporal validity to market data beliefs in my trading agent BDI model. Price beliefs should expire after 5 minutes, news sentiment beliefs after 1 hour, company fundamentals after 24 hours. Show the SPARQL query that returns only beliefs active at a given timestamp and filters out expired ones.
```

```
Write the four SPARQL competency queries to validate my BDI model: (1) every desire is motivated by at least one active belief, (2) every intention fulfills a desire, (3) no intention contradicts an active belief, (4) all plans have ordered task sequences. My model uses the prefix ex: http://example.org/bdi#.
```

**Key references:**

| Reference | Topic |
|---|---|
| `bdi-ontology-core.md` | Class hierarchy: Belief, Desire, Intention as endurants; BeliefProcess, DesireProcess, IntentionProcess as perdurants; WorldState grounding |
| `rdf-examples.md` | Complete Turtle examples: cognitive chains, world state references, compositional beliefs, temporal intervals |
| `sparql-competency.md` | Validation queries: CQ1 (belief-to-desire), CQ2 (intention-to-desire), CQ3 (process-to-belief), CQ4 (plan task ordering) |
| `framework-integration.md` | SEMAS production rules, JADE/JADEX agent mapping, Logic Augmented Generation pipeline for LLM constraint validation |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Make my agent think" | "Model the belief-desire-intention chain for an agent that monitors server health metrics and decides when to scale infrastructure" |
| "Add BDI to my chatbot" | "Transform incoming customer context (name, history, sentiment) into formal beliefs that motivate the agent's response strategy" |
| "Use ontology for my agent" | "Implement T2B2T: my agent receives RDF triples from a knowledge graph about flight schedules, forms beliefs about available routes, and produces booking intention triples" |

### Structured Prompt Templates

**For modeling a cognitive chain:**
```
Model the BDI cognitive chain for an agent that [perceives what]. The agent should form beliefs about [world state aspects], develop desires to [goals], and commit to intentions that [concrete actions]. Show the full chain in RDF/Turtle with justifications.
```

**For T2B2T integration:**
```
Implement T2B2T for [domain]. Input triples describe [data source]. The agent should transform these into beliefs about [aspects], reason about [decisions], and output triples that [actions/effects]. Show both directions of the flow.
```

**For temporal reasoning:**
```
Add temporal validity to [which mental states] in my BDI model. Beliefs about [data type] should expire after [duration]. Show the SPARQL query to find all active beliefs at a given timestamp.
```

### Prompt Anti-Patterns

- **Conflating mental states with world states**: "The agent's belief IS that the server is down" -- mental states reference world states, they are not world states themselves. A belief about the server being down is a cognitive representation, not the server state.
- **Skipping justifications**: "Just model the beliefs and intentions" -- every mental state should link to a justification for explainability. Without justifications, the BDI model is decoration, not structure.
- **Flat belief structures**: "One belief per fact" -- complex beliefs should use compositional modeling with `hasPart` relations. A belief about a meeting has parts for time, location, and participants that can be updated independently.

## Real-World Walkthrough

**Starting situation:** You are building a supply chain monitoring agent that watches inventory levels across multiple warehouses, detects low-stock situations, and decides whether to reorder automatically or alert a human. The agent receives data from an RDF-based inventory knowledge graph.

**Step 1: World state modeling.** You ask: "Model the world states for a supply chain agent that monitors inventory across 3 warehouses." The skill produces WorldState instances representing current inventory levels, reorder thresholds, supplier lead times, and warehouse capacities -- all as RDF triples that the agent will perceive.

**Step 2: Belief formation (Triples-to-Beliefs).** You ask: "Transform the inventory RDF into agent beliefs." The skill models BeliefProcess instances that consume WorldState triples and generate structured beliefs. When inventory at Warehouse A drops below threshold, a BeliefProcess generates `Belief_low_stock_warehouse_A` with a temporal validity of 1 hour (the belief expires because stock levels change). The belief is justified by the specific inventory reading triple.

**Step 3: Desire generation.** The skill shows how beliefs motivate desires through the cognitive chain. `Belief_low_stock_warehouse_A` motivates `Desire_replenish_warehouse_A`. But the system is not simplistic: a concurrent `Belief_supplier_delayed` (formed from supply chain status triples) also exists. The desire formation process considers both beliefs and generates `Desire_alert_procurement_team` instead of `Desire_auto_reorder` because the supplier delay makes automatic reordering futile.

**Step 4: Intention commitment.** The agent commits to `Intention_send_procurement_alert`, which fulfills `Desire_alert_procurement_team` and is supported by both beliefs (low stock AND supplier delay). The intention specifies `Plan_alert_sequence` with three tasks: compose alert message, send to procurement Slack channel, log the decision.

**Step 5: Beliefs-to-Triples output.** The plan execution produces new RDF triples: a `WorldState_alert_sent` triple recording the alert, and a `WorldState_reorder_pending` triple that will be consumed by the procurement system. The T2B2T cycle completes.

**Step 6: Validation with SPARQL.** You ask: "Write competency queries to validate the model." The skill produces four queries: (1) verify every desire is motivated by at least one belief, (2) verify every intention fulfills a desire, (3) verify no intention contradicts an active belief, (4) find all beliefs active at a given timestamp. Running these against the model confirms structural consistency.

**Gotchas discovered:** The initial model had desires directly triggering actions without an intermediate intention. The skill corrected this: intentions specify plans which contain tasks; actions execute tasks. This three-layer structure (desire -> intention -> plan -> task -> action) is essential because a desire might be fulfilled by different plans depending on context, and intentions can be dropped if circumstances change before execution.

## Usage Scenarios

### Scenario 1: Building an explainable decision agent

**Context:** Your compliance team requires that automated decisions in a financial system be fully traceable -- from input data through reasoning to output action.

**You say:** "Model a BDI architecture for a loan approval agent that must explain every decision. Regulators need to trace from the decision back to the specific data points and reasoning."

**The skill provides:**
- Belief chain from application data through creditworthiness assessment
- Justification links at every step (belief justified by data, desire justified by beliefs, intention justified by desire and policy)
- SPARQL queries regulators can run to trace any decision
- Temporal validity ensuring decisions reference current data

**You end up with:** A formal cognitive model where every loan decision links back to specific data points, reasoning steps, and policy rules through an auditable chain.

### Scenario 2: Implementing neuro-symbolic reasoning for an LLM agent

**Context:** Your LLM agent occasionally generates responses that contradict its own established knowledge. You want to add formal constraints without losing the flexibility of natural language generation.

**You say:** "Implement Logic Augmented Generation so my LLM agent's outputs are validated against a BDI ontology before being returned to the user."

**The skill provides:**
- Ontology serialization pipeline (BDI graph -> Turtle -> prompt context)
- LLM output validation: extract RDF triples from response, validate against ontology
- Retry-with-feedback loop when validation fails
- Integration pattern for production deployment

**You end up with:** A LAG pipeline where the LLM generates responses constrained by formal BDI rules, catching contradictions before they reach users.

### Scenario 3: Multi-agent belief sharing

**Context:** You have three specialized agents (research, analysis, reporting) that need to share their understanding of a situation. Currently they pass unstructured text and often contradict each other.

**You say:** "Design a BDI-based communication protocol so my three agents can share beliefs formally instead of passing unstructured text."

**The skill provides:**
- Shared BDI ontology vocabulary all three agents use
- Belief serialization format for inter-agent communication
- Conflict resolution patterns when agents hold contradictory beliefs
- FIPA ACL integration for cross-platform communication

**You end up with:** A structured communication protocol where agents share typed beliefs with justifications, and contradictions are detected and resolved formally rather than silently.

---

## Decision Logic

**When should you use BDI modeling vs simple prompt engineering?**

BDI modeling adds value when: (1) decisions must be explainable and auditable, (2) multiple agents need to share structured mental states, (3) beliefs have temporal validity and stale information causes failures, (4) you need formal validation that reasoning is consistent. Simple prompt engineering is sufficient when the agent performs straightforward input-output tasks without complex reasoning chains or explainability requirements.

**When to use T2B2T vs direct LLM processing?**

T2B2T is appropriate when external data is already in RDF or can be naturally expressed as triples, when the agent needs to produce structured output that feeds into other systems, and when bidirectional flow between knowledge graphs and agent cognition is the core architecture. Direct LLM processing is simpler when inputs and outputs are natural language without formal structure requirements.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Beliefs without temporal bounds | Agent acts on stale information (yesterday's stock price treated as current) | Add `hasValidity` with TimeInterval to every belief; implement expiration checks in the reasoning cycle |
| Missing justifications | Cannot trace why the agent made a decision; audit fails | Enforce existential restriction: every Belief must link to at least one Justification instance |
| Flat belief structures | Updating one aspect (meeting location changed) requires replacing the entire belief about the meeting | Model complex beliefs with `hasPart` relations; update only the changed component |
| Conflating world states and mental states | Model is structurally wrong; beliefs ARE the world instead of ABOUT the world | Separate WorldState instances (objective) from Belief instances (agent's representation); beliefs reference world states via `refersTo` |

## Ideal For

- **Agent architects building explainable AI systems** who need formal reasoning chains that regulators and auditors can trace
- **Knowledge graph engineers** who work with RDF data and want to bridge it into agent cognition through the T2B2T paradigm
- **Multi-agent system designers** who need structured inter-agent communication beyond unstructured text passing
- **Researchers in neuro-symbolic AI** who want to augment LLM outputs with formal ontological constraints

## Not For

- **Simple chatbot development** -- if your agent answers questions without complex multi-step reasoning, BDI adds overhead without value. Use standard prompt engineering.
- **Multi-agent coordination protocols** -- BDI provides the cognitive model, not the coordination patterns. Use `multi-agent-patterns` for handoffs, routing, and orchestration.
- **Persistent memory and retrieval** -- for storing and retrieving agent memories across sessions, use `memory-systems`.

## Related Plugins

- **multi-agent-patterns** -- Coordinate agents whose mental states this plugin helps you model
- **ontology-design** -- Design formal domain ontologies that BDI agents can reason about
- **memory-systems** -- Persist agent beliefs across sessions
- **agent-evaluation** -- Evaluate the quality of BDI-based agent decisions
- **agent-project-development** -- Plan the overall architecture of agent systems that use BDI cognitive models

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
