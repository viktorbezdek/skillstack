# BDI Mental State Modeling

> Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration patterns.

## Overview

The Belief-Desire-Intention (BDI) model is a cognitive architecture that enables agents to reason about the world through structured mental states: beliefs about what is true, desires about what should be achieved, and intentions about what actions to take. This skill provides a formal ontology for implementing BDI in LLM agent systems, enabling deliberative reasoning, explainability, and semantic interoperability across multi-agent platforms.

This skill is designed for developers building agents that need to go beyond reactive tool-calling into genuine cognitive modeling. It covers the full BDI architecture from mental state representation in RDF/Turtle through temporal reasoning, compositional belief structures, and the T2B2T (Triples-to-Beliefs-to-Triples) paradigm for bidirectional flow between knowledge graphs and internal agent states. The approach draws on established ontology design patterns (DOLCE, EventCore, BasicPlan) for interoperability.

Within the SkillStack collection, BDI Mental States bridges the gap between context engineering and cognitive AI. It provides formal structures that complement the Context Fundamentals skill's attention mechanics, the Multi-Agent Patterns skill's coordination protocols, and the Memory Systems skill's persistence layer. When agents need to explain their reasoning or coordinate across heterogeneous platforms (SEMAS, JADE, JADEX), this skill provides the formal framework.

## What's Included

### Skill

- `skills/bdi-mental-states/SKILL.md` -- Core BDI methodology covering mental state ontology, cognitive chain patterns, T2B2T paradigm, temporal dimensions, compositional entities, and integration patterns

### References

- **bdi-ontology-core.md** -- Core ontology patterns and class definitions for Belief, Desire, Intention, and supporting mental processes
- **rdf-examples.md** -- Complete RDF/Turtle examples demonstrating cognitive chains, world state grounding, and plan specification
- **sparql-competency.md** -- Full competency question SPARQL queries for validating BDI implementations
- **framework-integration.md** -- Integration patterns for SEMAS, JADE, JADEX, and Logic Augmented Generation (LAG) pipelines

## Key Features

- **Formal BDI ontology** distinguishing endurants (persistent mental states: Belief, Desire, Intention) from perdurants (temporal processes: BeliefProcess, DesireProcess, IntentionProcess)
- **Cognitive chain pattern** linking beliefs to desires through motivation and desires to intentions through fulfillment, with full RDF/Turtle notation
- **T2B2T paradigm** (Triples-to-Beliefs-to-Triples) implementing bidirectional flow between external RDF knowledge graphs and internal mental states
- **Temporal reasoning** with validity intervals on mental states, enabling diachronic queries about what an agent believed at specific moments
- **Compositional mental entities** using `hasPart` relations for selective updates to complex beliefs without full replacement
- **Justification and explainability** linking every mental entity to supporting evidence for traceable reasoning chains
- **Logic Augmented Generation (LAG)** patterns for constraining LLM outputs with ontological structures and validating against formal schemas
- **SPARQL competency queries** for validating implementation correctness against formal requirements

## Usage Examples

Model agent beliefs from external data:
```
I have an RDF knowledge graph of meeting schedules. Help me implement a BDI agent that forms beliefs from this data, generates desires based on scheduling conflicts, and commits to intentions with concrete action plans.
```

Build an explainable agent reasoning system:
```
Design a BDI architecture where every agent decision is traceable through a chain of beliefs, desires, and intentions, each linked to justification evidence. I need to audit why the agent took specific actions.
```

Implement temporal belief tracking:
```
Create a system where agent beliefs have validity intervals so we can query what the agent believed at any point in time. Beliefs should be compositional so we can update parts without replacing the whole.
```

Integrate BDI with an LLM pipeline:
```
I want to augment my LLM agent with formal BDI ontology constraints using the Logic Augmented Generation pattern. The agent should generate RDF triples that are validated against the BDI schema before being accepted.
```

## Quick Start

1. **Define mental state types**: Model your agent's beliefs (world knowledge), desires (goals), and intentions (committed plans) as RDF classes following the BDI ontology.
2. **Implement cognitive chains**: Link beliefs to desires through `bdi:motivates` and desires to intentions through `bdi:fulfils`, creating traceable reasoning paths.
3. **Add temporal dimensions**: Attach `bdi:hasValidity` intervals to all mental states so you can query agent state at any point in time.
4. **Use T2B2T**: Parse external RDF data into beliefs (Triples-to-Beliefs), execute BDI reasoning, then project results back to RDF (Beliefs-to-Triples).
5. **Validate with SPARQL**: Run competency queries to verify your implementation correctly links beliefs to desires, desires to intentions, and intentions to plans.

## Related Skills

- **context-fundamentals** -- Understanding context structure for effective BDI reasoning within LLM agents
- **multi-agent-patterns** -- Coordinating mental states across multi-agent platforms using FIPA ACL
- **memory-systems** -- Persisting mental states across sessions with temporal knowledge graphs
- **agent-evaluation** -- Evaluating the quality of BDI-based reasoning chains
- **tool-design** -- Designing tools that interface with BDI ontology structures

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install bdi-mental-states@skillstack` — 46 production-grade plugins for Claude Code.
