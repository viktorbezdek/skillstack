# BDI Mental States

> **v1.0.4** | Agent Architecture | 5 iterations

Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration patterns.

## What Problem Does This Solve

Transform external RDF context into agent mental states (beliefs, desires, intentions) using formal BDI ontology patterns. This skill enables agents to reason about context through cognitive architecture, supporting deliberative reasoning, explainability, and semantic interoperability within multi-agent systems.

## When to Use This Skill

This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "build cognitive agent", or mentions BDI ontology, mental state modeling, rational agency, or neuro-symbolic AI integration.

## When NOT to Use This Skill

- multi-agent coordination or agent handoffs -- use [multi-agent-patterns](../multi-agent-patterns/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/bdi-mental-states
```

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

- **When to Activate**
- **Core Concepts**
- **T2B2T Paradigm**
- **Notation Selection by Level**
- **Justification and Explainability**
- **Temporal Dimensions**
- **Compositional Mental Entities**
- **Integration Patterns**

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
