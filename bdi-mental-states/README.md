# BDI Mental States

> **v1.0.4** | Agent Architecture | 5 iterations

> Formal Belief-Desire-Intention cognitive architecture for LLM agents -- model what agents believe, want, and commit to doing, with RDF ontology, explainable reasoning chains, and neuro-symbolic integration.

## The Problem

LLM agents make decisions, but nobody can explain why. When an agent takes an unexpected action -- purchasing the wrong item, scheduling a conflicting meeting, ignoring a critical constraint -- there is no cognitive trace to inspect. The agent's "reasoning" is a black box of token generation. You cannot ask "what did the agent believe about the meeting time?" or "what desire motivated this purchase?" because there is no formal model of beliefs, desires, or intentions.

This matters in production. Multi-agent systems need to share what they know -- but without a formal representation of beliefs, agents cannot communicate cognitive states, cannot negotiate based on differing beliefs, and cannot explain disagreements. Temporal reasoning is impossible: you cannot ask "what did the agent believe at 10am?" because beliefs are not tracked over time. And when an agent acts irrationally, you cannot trace the reasoning chain from perception through deliberation to action because no such chain exists in the system.

The BDI (Belief-Desire-Intention) model from cognitive science provides the theoretical foundation, but applying it to LLM agents requires ontology design, RDF modeling, SPARQL queries, and integration patterns that span philosophy, knowledge representation, and practical engineering. This knowledge exists in academic papers but is not readily accessible to engineers building agent systems.

## The Solution

This plugin provides a complete BDI implementation framework for LLM agents: formal ontology patterns for beliefs, desires, and intentions; the T2B2T (Triples-to-Beliefs-to-Triples) paradigm for bidirectional flow between RDF knowledge graphs and internal mental states; temporal validity intervals for tracking how beliefs change over time; compositional mental entities that support selective updates; justification chains that make every reasoning step explainable; and integration patterns for SEMAS, JADE, JADEX, and Logic Augmented Generation (LAG).

The skill walks you through modeling an agent's cognitive architecture: what it believes about the world (and why), what it wants to achieve (and what motivates those desires), and what it commits to doing (with plans decomposed into ordered tasks). Every mental state links to supporting evidence, has temporal bounds, and can be queried with SPARQL. When something goes wrong, you trace the chain: perception formed a belief, that belief motivated a desire, that desire became an intention, that intention specified a plan, and the plan's tasks executed in sequence.

You end up with agents whose reasoning is inspectable, communicable across platforms, and formally grounded in established cognitive science -- not just "the model decided."

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent decisions are black boxes with no explainable reasoning chain | Every decision traces from perception through belief to desire to intention to plan |
| No formal way to represent what an agent "believes" or "wants" | Formal BDI ontology with typed mental states, processes, and relationships |
| Agents cannot share cognitive states across platforms | RDF-based mental state representation enables cross-platform communication via FIPA ACL |
| No temporal tracking of how beliefs change over time | Validity intervals on every mental state enable "what did the agent believe at 10am?" queries |
| Complex beliefs are all-or-nothing -- update one aspect and you replace everything | Compositional mental entities with `hasPart` relations enable selective updates |
| Agent reasoning cannot be audited for compliance or debugging | Justification instances link every mental entity to supporting evidence |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install bdi-mental-states@skillstack
```

### Verify Installation

After installing, test with:

```
Help me model the cognitive architecture for a scheduling agent that needs to reason about meeting conflicts
```

The skill activates automatically when you mention BDI, mental states, or cognitive agent architecture.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your agent's cognitive requirements:
   ```
   I'm building an agent that manages purchase orders -- it needs to reason about budget constraints, approval requirements, and vendor reliability
   ```
3. The skill models the agent's beliefs (budget status, vendor ratings), desires (cost minimization, timely delivery), and intentions (specific purchase plans with task sequences).
4. You get RDF/Turtle representations, SPARQL validation queries, and integration patterns for your framework.
5. Add explainability:
   ```
   Make every purchase decision traceable -- I need to audit why the agent chose vendor X over vendor Y
   ```

## What's Inside

This is a single-skill plugin with four reference documents covering the full BDI implementation stack.

| Component | Purpose |
|---|---|
| **bdi-mental-states** skill | Core methodology: mental state architecture (beliefs, desires, intentions), cognitive chain patterns, world state grounding, goal-directed planning, T2B2T paradigm, notation selection by C4 level, justification/explainability, temporal dimensions, compositional entities, LAG integration, SEMAS rules, 10 guidelines, 5 anti-patterns, competency queries |
| **bdi-ontology-core.md** | Core ontology patterns: class hierarchy for mental states and processes, property definitions, existential restrictions, OWL axioms |
| **rdf-examples.md** | Complete RDF/Turtle examples: full cognitive workflows from perception through action, compositional beliefs, temporal reasoning |
| **sparql-competency.md** | Full SPARQL competency queries: validating belief motivation chains, intention-desire fulfillment, plan task ordering, temporal state queries |
| **framework-integration.md** | Integration patterns: SEMAS rule translation, JADE agent platform mapping, JADEX goal lifecycle, Logic Augmented Generation (LAG) pipeline |

**Eval coverage:** 15 trigger eval cases + 3 output eval cases.

### How to Use: bdi-mental-states

**What it does:** Guides you through modeling agent cognitive architecture using the Belief-Desire-Intention framework. Activates when you need to represent what agents believe, want, and commit to; when you need explainable agent reasoning; when building agents that share cognitive states across platforms; or when integrating formal ontology with LLM-based agents. Produces RDF/Turtle models, SPARQL queries, and framework integration code.

**Try these prompts:**

```
Design the cognitive architecture for a customer service agent that needs to reason about customer history, product knowledge, and escalation policies
```

```
I need my agents to explain their decisions -- model the justification chain from perception to action for an inventory management agent
```

```
Help me implement the T2B2T paradigm -- I have RDF triples from our knowledge graph and need to transform them into agent beliefs, then project decisions back as RDF
```

```
How do I model temporal belief evolution? My agent's beliefs about stock levels change throughout the day and I need to query what it believed at specific times
```

```
Integrate BDI mental states with our JADE multi-agent platform -- map the ontology to JADE agent behaviors and message passing
```

**Key references:**

| Reference | Topic |
|---|---|
| `bdi-ontology-core.md` | Class hierarchy, property definitions, OWL axioms, existential restrictions |
| `rdf-examples.md` | Complete Turtle examples for cognitive workflows, compositional beliefs, temporal reasoning |
| `sparql-competency.md` | Validation queries for belief chains, intention fulfillment, plan ordering, temporal states |
| `framework-integration.md` | SEMAS production rules, JADE mapping, JADEX goal lifecycle, LAG pipeline patterns |

## Real-World Walkthrough

You are building a procurement agent for a manufacturing company. The agent needs to monitor inventory levels, evaluate vendor options, make purchase recommendations within budget constraints, and explain every decision to the compliance team. The compliance requirement is non-negotiable -- every purchase recommendation must trace back to specific beliefs about inventory, vendor reliability, and budget status.

You start by modeling the agent's belief system:

```
Design the belief structure for a procurement agent that tracks inventory levels, vendor performance ratings, budget constraints, and delivery timelines
```

The skill models four belief categories as RDF/Turtle:

- `Belief_inventory_widget_A` with value "150 units, reorder threshold 200" and validity interval (updated every 4 hours from the ERP system)
- `Belief_vendor_reliability_acme` with value "98.5% on-time delivery rate, average lead time 5 days" justified by historical delivery data
- `Belief_budget_q2_remaining` with value "$45,000 remaining in Q2 procurement budget" linked to the finance system world state
- `Belief_delivery_timeline_critical` with value "Widget A production line needs replenishment by March 15" motivated by the production schedule

Each belief references its source world state, has temporal validity bounds, and links to a justification instance documenting the evidence.

Next, the desire layer:

```
What desires should the procurement agent form based on these beliefs?
```

The cognitive chain pattern triggers: `Belief_inventory_widget_A` (below reorder threshold) motivates `Desire_replenish_widget_A`. The desire is not just "buy widgets" -- it has specific parameters: sufficient quantity, within budget, before the production deadline. The `isMotivatedBy` link connects the desire back to the triggering beliefs, creating the first link in the explainability chain.

Now intentions and plans:

```
Model how the agent commits to a specific vendor and creates an actionable purchase plan
```

The deliberation process evaluates `Desire_replenish_widget_A` against available vendor beliefs and budget constraints. `Intention_purchase_acme_500` commits to purchasing 500 Widget A units from Acme Corp. The intention specifies `Plan_acme_purchase` which decomposes into ordered tasks: `Task_verify_budget` (confirm $12,500 available) precedes `Task_generate_po` (create purchase order) precedes `Task_submit_approval` (route to manager) precedes `Task_confirm_delivery` (verify delivery date before March 15).

Each intention links back through `fulfils` to the desire and through `isSupportedBy` to the beliefs that justified the vendor selection. When the compliance team asks "why did the agent choose Acme over Beta Corp?", you query:

```sparql
SELECT ?belief ?justification WHERE {
    :Intention_purchase_acme_500 bdi:isSupportedBy ?belief .
    ?belief bdi:isJustifiedBy ?justification .
}
```

The query returns: Acme was chosen because of `Belief_vendor_reliability_acme` (98.5% on-time rate, justified by 24 months of delivery data) and `Belief_acme_price_competitive` (10% below Beta Corp quote, justified by the latest RFQ response). Every link in the chain is traceable.

You then implement temporal belief updates:

```
The inventory level changes throughout the day as production consumes widgets -- how do I model belief evolution?
```

Each inventory belief gets a validity interval. When the ERP system reports a new level, a `BeliefProcess` generates a new belief with an updated validity interval and marks the previous belief's interval as ended. You can query the agent's belief at any point in time using the temporal SPARQL patterns from `sparql-competency.md`.

Finally, you implement the T2B2T paradigm: RDF triples from the ERP system flow through belief formation processes, the BDI reasoning engine deliberates and commits to intentions, and the resulting purchase decisions are projected back as RDF triples to the procurement system. The bidirectional flow means the knowledge graph stays synchronized with the agent's cognitive state.

The compliance team now has full audit trails. The production team trusts the agent's recommendations because every decision is explainable. And when the agent makes an unexpected choice, you debug it by inspecting the belief chain rather than guessing at token probabilities.

## Usage Scenarios

### Scenario 1: Building an explainable decision agent

**Context:** You are building an agent for a regulated industry (healthcare, finance, legal) where every decision must be auditable. Regulators require traceability from input data to final recommendation.

**You say:** "I need a loan approval agent where every decision is fully traceable -- regulators must be able to audit why a specific loan was approved or denied"

**The skill provides:**
- Belief modeling for applicant data (income, credit score, employment history) with justification links to source documents
- Desire formation based on risk assessment beliefs (desire to approve if risk is acceptable)
- Intention commitment with full reasoning chain from beliefs through desires to approval/denial
- SPARQL queries for auditors to trace any decision back to its supporting evidence
- Temporal validity so auditors can see what the agent believed at the time of decision

**You end up with:** A BDI-modeled loan approval agent where every decision links to specific beliefs, each belief cites its source data, and regulators can run SPARQL queries to audit the complete reasoning chain.

### Scenario 2: Multi-agent belief sharing

**Context:** You have three specialized agents (market analyst, risk assessor, portfolio manager) that need to share their beliefs and coordinate decisions in a trading system.

**You say:** "My three trading agents need to share what they believe about market conditions -- design the mental state communication layer"

**The skill provides:**
- Shared BDI ontology so all agents model beliefs using the same vocabulary
- RDF-based belief serialization for cross-agent communication
- FIPA ACL integration patterns for belief sharing messages
- Conflict resolution when agents hold contradictory beliefs about the same world state
- Compositional beliefs with `hasPart` so agents can update specific aspects independently

**You end up with:** A shared cognitive communication layer where agents exchange typed beliefs as RDF triples, detect contradictions, and coordinate intentions based on their collective understanding of market conditions.

### Scenario 3: Integrating BDI with an LLM pipeline

**Context:** You have an LLM-based agent that makes good decisions but cannot explain them. You want to add BDI structure to make the reasoning inspectable without replacing the LLM.

**You say:** "I want to augment my LLM agent with BDI mental states using the Logic Augmented Generation pattern -- the LLM handles reasoning but BDI provides the structure"

**The skill provides:**
- Logic Augmented Generation (LAG) pipeline: ontology context injected into LLM prompts
- Post-generation validation: extracting RDF triples from LLM output and validating against BDI axioms
- Belief formation from LLM perception: translating LLM observations into formal beliefs
- Intention extraction: mapping LLM action plans to BDI intention-plan-task structures
- Consistency checking between LLM outputs and existing belief states

**You end up with:** An LLM agent whose outputs are post-processed into formal BDI structures, making every decision inspectable and auditable while preserving the LLM's reasoning capabilities.

## Ideal For

- **Teams building agents for regulated industries** -- the justification chains and SPARQL audit queries meet compliance requirements for explainable AI
- **Researchers implementing cognitive agent architectures** -- the formal BDI ontology with OWL axioms and DOLCE alignment provides academically grounded foundations
- **Engineers building multi-agent systems** -- RDF-based mental state representation enables cross-platform belief sharing and coordination
- **Anyone needing explainable agent reasoning** -- the perception-belief-desire-intention-plan-task chain makes every decision traceable
- **Teams combining LLMs with formal reasoning** -- the LAG integration pattern and T2B2T paradigm bridge neural and symbolic approaches

## Not For

- **Multi-agent coordination protocols and handoff patterns** -- use [multi-agent-patterns](../multi-agent-patterns/) for supervisor, swarm, and hierarchical architectures
- **Agent memory persistence and retrieval** -- use [memory-systems](../memory-systems/) for production memory frameworks (Mem0, Zep/Graphiti, Letta, Cognee, LangMem)
- **Evaluating agent output quality** -- use [agent-evaluation](../agent-evaluation/) for rubrics, LLM-as-judge, and evaluation pipelines

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through four reference documents.

The **SKILL.md** body provides the conceptual framework: the mental reality architecture (beliefs, desires, intentions as endurants; belief processes, desire processes, intention processes as perdurants), the cognitive chain pattern showing how beliefs motivate desires that become intentions specifying plans, world state grounding, the T2B2T paradigm for bidirectional RDF flow, justification and explainability patterns, temporal dimensions with validity intervals, compositional mental entities, and integration patterns for LAG and SEMAS.

When deeper implementation detail is needed, Claude draws from the references:

- **bdi-ontology-core.md** provides the formal class hierarchy, OWL property definitions, existential restrictions, and axioms for the BDI ontology
- **rdf-examples.md** provides complete RDF/Turtle examples showing full cognitive workflows from perception through action
- **sparql-competency.md** provides SPARQL queries for validating ontology implementations against competency questions (what beliefs motivated a desire, which tasks compose a plan, what was the agent's state at time T)
- **framework-integration.md** provides concrete integration code for SEMAS production rules, JADE agent behaviors, JADEX goal lifecycle, and LAG pipeline implementation

Simple questions ("what is the BDI model?") are answered from the core skill. Ontology design pulls from `bdi-ontology-core.md`. Implementation questions pull from `rdf-examples.md` and `framework-integration.md`. Validation queries pull from `sparql-competency.md`.

## Related Plugins

- **[Agent Evaluation](../agent-evaluation/)** -- Rubrics, LLM-as-judge, bias mitigation for measuring agent quality
- **[Agent Project Development](../agent-project-development/)** -- Methodology for starting LLM projects: task-model fit, pipeline architecture
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for background agents: sandboxes, registries, self-spawning
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Supervisor, swarm, and hierarchical patterns for multi-agent systems
- **[Ontology Design](../ontology-design/)** -- Formal knowledge models with classes, properties, relationships, and taxonomies

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
