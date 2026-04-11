# BDI Mental States

> **v1.0.4** | Agent Architecture | 5 iterations

Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration patterns.

## What Problem Does This Solve

LLM agents that rely purely on prompt context lack structured internal representations of what they believe, want, and intend — making deliberation opaque, reasoning unjustifiable, and coordination across agents fragile. The BDI (Belief-Desire-Intention) architecture provides a formal cognitive model that separates perception from deliberation from action, enabling agents to explain their reasoning chains, maintain temporally-bounded mental states, and interoperate with other agents via established ontologies.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "How do I give my agent a structured representation of what it believes about the world?" | BDI ontology patterns in RDF/Turtle with Belief, WorldState, and temporal validity constructs |
| "I need my agent's reasoning to be explainable and traceable" | Justification linking pattern connecting every mental state to explicit evidence instances |
| "How do I integrate external RDF knowledge graphs into agent reasoning?" | T2B2T (Triples-to-Beliefs-to-Triples) paradigm for bidirectional flow between RDF context and internal mental states |
| "I want to implement a cognitive agent that forms intentions from beliefs" | Complete Belief → Desire → Intention → Plan → Task chain with RDF examples and SPARQL competency queries |
| "How do I connect BDI mental states to production rules in SEMAS or JADE?" | Framework integration patterns translating BDI ontology to SEMAS rule notation and JADE agent execution |
| "My LLM agent needs ontological constraints to prevent hallucinating structured outputs" | Logic Augmented Generation (LAG) integration pattern augmenting LLM prompts with BDI ontology context |

## When NOT to Use This Skill

- multi-agent coordination or agent handoffs -- use [multi-agent-patterns](../multi-agent-patterns/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install bdi-mental-states@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the bdi-mental-states skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `bdi`
- `cognitive-architecture`
- `rdf`
- `ontology`
- `neuro-symbolic`

## What's Inside

- **When to Activate** -- Conditions distinguishing BDI use cases from multi-agent-patterns and memory-systems
- **Core Concepts** -- Mental Reality Architecture distinguishing endurants (Belief, Desire, Intention) from perdurants (BeliefProcess, DesireProcess, IntentionProcess), with world state grounding and goal-directed planning examples
- **T2B2T Paradigm** -- Bidirectional RDF-to-beliefs-to-RDF transformation with complete Turtle notation examples for both phases
- **Notation Selection by Level** -- C4 architecture level mapping (Context/Container/Component/Code) to ArchiMate and UML notations for BDI system documentation
- **Justification and Explainability** -- Pattern for linking every mental entity to explicit Justification instances enabling traceable reasoning chains
- **Temporal Dimensions** -- Validity interval modeling for bounded mental states with SPARQL query for time-point mental state retrieval
- **Compositional Mental Entities** -- Meronymic `hasPart` structures enabling selective belief updates without replacing entire complex beliefs
- **Integration Patterns** -- Logic Augmented Generation for LLM constraint, SEMAS rule translation, and FIPA ACL cross-platform communication

## Key Capabilities

- **RDF Processing**
- **Semantic Reasoning**
- **Multi-Agent Communication**
- **Temporal Context**
- **Explainable AI**
- **Neuro-Symbolic AI**

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(bdi-mental-states): add standard keywords and expand README to full format (9cb523a)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Agent Project Development](../agent-project-development/)** -- Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, c...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
