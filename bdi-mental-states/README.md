# BDI Mental States

> **v1.0.4** | Agent Architecture | 5 iterations

Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration patterns.

## What Problem Does This Solve

LLM agents that rely purely on prompt context lack structured internal representations of what they believe, want, and intend. Their deliberation is opaque -- you cannot trace why an agent chose one action over another, verify that its beliefs are grounded in evidence, or determine when a belief expired. When multiple agents need to share mental states, there is no interoperable format for communicating beliefs across platforms.

The BDI (Belief-Desire-Intention) architecture addresses this by providing a formal cognitive model that separates perception from deliberation from action. Each mental state (belief, desire, intention) is a first-class entity with temporal validity, justification links, and compositional structure. This enables explainable reasoning chains, selective belief updates without replacing entire knowledge structures, and cross-agent communication via standard RDF/SPARQL interfaces. The skill covers the ontology itself, the T2B2T (Triples-to-Beliefs-to-Triples) paradigm for bidirectional RDF integration, and patterns for connecting BDI structures to production rule engines and LLM pipelines.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install bdi-mental-states@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention BDI, cognitive architecture, or ontology topics, or you can invoke it explicitly with `Use the bdi-mental-states skill to ...`.

## What's Inside

This is a single-skill plugin with four reference documents:

| Component | What It Covers |
|---|---|
| **SKILL.md** | Mental Reality Architecture (endurants: Belief, Desire, Intention; perdurants: BeliefProcess, DesireProcess, IntentionProcess), cognitive chain pattern (Belief motivates Desire, Desire fulfilled by Intention, Intention specifies Plan), world state grounding, goal-directed planning with task sequences, T2B2T paradigm (bidirectional RDF-to-beliefs-to-RDF), C4 notation mapping, justification and explainability patterns, temporal validity intervals, compositional mental entities with `hasPart` for selective updates, Logic Augmented Generation integration, SEMAS rule translation, and SPARQL competency queries for validation |
| **references/bdi-ontology-core.md** | Core ontology class definitions, property hierarchies, existential restrictions, OWL axioms, and alignment with DOLCE upper ontology |
| **references/rdf-examples.md** | Complete RDF/Turtle examples for all ontology patterns: beliefs, desires, intentions, plans, world states, justifications, temporal constructs, and compositional structures |
| **references/sparql-competency.md** | Full SPARQL queries for competency questions: what beliefs motivated a desire, which desire an intention fulfills, what process generated a belief, task ordering in plans, active mental states at a time point, and justification chains |
| **references/framework-integration.md** | Integration patterns for SEMAS (production rules), JADE/JADEX (Java agent frameworks), FIPA ACL (agent communication language), and Logic Augmented Generation (LLM constraint with ontological context) |

## Usage Scenarios

**1. "I need my agent to explain why it chose a particular action."**
Use the justification pattern: every mental entity links to a `Justification` instance with explicit evidence. When the agent forms a belief from a notification, the belief references the notification as justification. When a desire motivates an intention, the intention links back through `fulfils` and `isSupportedBy`. Tracing backward from any action through its intention, desire, and belief chain produces a complete explanation grounded in evidence.

**2. "How do I represent an agent's beliefs about the world in a way that other systems can query?"**
Model beliefs as RDF triples using the BDI ontology. Each belief references a `WorldState` (the objective situation) via `refersTo`, has temporal validity via `hasValidity` with start/end times, and can be queried with standard SPARQL. Other systems can ask "what does Agent A believe about the meeting?" by querying for beliefs that refer to the relevant world state.

**3. "I want my LLM agent to reason with formal cognitive structures instead of just generating text."**
Use the Logic Augmented Generation (LAG) pattern: serialize the relevant BDI ontology context as Turtle, prepend it to the LLM prompt, extract RDF triples from the response, and validate them against ontology constraints. This constrains the LLM to produce outputs consistent with the cognitive model rather than hallucinating arbitrary structures.

**4. "My agent has complex beliefs that should be partially updatable."**
Use compositional mental entities with `hasPart`. A belief about a meeting (`Belief_meeting`) decomposes into `Belief_meeting_time` and `Belief_meeting_location`. When the location changes, a `BeliefProcess` modifies only `Belief_meeting_location` without invalidating the parent belief or the time component. This prevents wholesale belief replacement when only one aspect changes.

**5. "I need agents on different platforms to share their mental states."**
Use FIPA ACL integration with RDF serialization. The BDI ontology provides a shared vocabulary: agents serialize their beliefs, desires, and intentions as RDF triples using the common ontology namespace. Receiving agents parse these triples into their own mental state representations. The SPARQL competency queries work across any compliant implementation.

## When to Use / When NOT to Use

**Use when:**
- Implementing cognitive agent architectures with formal reasoning
- Building explainable AI systems where decision chains must be traceable
- Integrating LLM agents with RDF knowledge graphs or semantic web infrastructure
- Modeling temporal evolution of agent beliefs and intentions
- Connecting agents across platforms via shared ontology

**Do NOT use when:**
- Coordinating multiple agents or designing handoff protocols -- use [multi-agent-patterns](../multi-agent-patterns/) instead
- Building agent memory frameworks for persistence across sessions -- use [memory-systems](../memory-systems/) instead
- Building simple agents that do not need formal cognitive structure -- use [agent-project-development](../agent-project-development/) instead

## Related Plugins

- **[Agent Evaluation](../agent-evaluation/)** -- Rubrics and LLM-as-judge for measuring agent quality
- **[Agent Project Development](../agent-project-development/)** -- Task-model fit, pipeline architecture, cost estimation for LLM projects
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for background agents
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Supervisor, swarm, and hierarchical patterns for multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
