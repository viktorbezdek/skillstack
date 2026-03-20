# Agent Evaluation

> **v1.0.4** | Agent Architecture | 5 iterations

Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, direct scoring, confidence calibration, and continuous monitoring.

## What Problem Does This Solve

Evaluation of agent systems requires fundamentally different approaches than traditional software testing or standard language model benchmarking. Agents make dynamic decisions, are non-deterministic between runs, and often lack single correct answers. Effective evaluation must account for these characteristics while providing actionable feedback.

## When to Use This Skill

This skill should be used when the user asks to "evaluate agent performance", "build test framework", "measure agent quality", "create evaluation rubrics", "implement LLM-as-judge", "compare model outputs", "mitigate evaluation bias", or mentions multi-dimensional evaluation, agent testing, quality gates, direct scoring, pairwise comparison, position bias, evaluation pipelines, or automated quality assessment for LLM agent systems.

## When NOT to Use This Skill

- testing code or applications -- use [testing-framework](../testing-framework/) instead

## How to Use

**Direct invocation:**

```
Use the agent-evaluation skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `evaluation`
- `llm-as-judge`
- `bias-mitigation`
- `rubrics`
- `pairwise-comparison`

## What's Inside

- **When to Activate**
- **Fundamentals**
- **Rubric Design**
- **The Bias Landscape**
- **Evaluation Approaches in Detail**
- **Task**
- **Original Prompt**
- **Response to Evaluate**

## Key Capabilities

- **Token budgets matter**
- **Model upgrades beat token increases**
- **Multi-agent validation**
- **Factual accuracy**
- **Completeness**
- **Citation accuracy**

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(agent-evaluation): add standard keywords and expand README to full format (55c6ea2)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Project Development](../agent-project-development/)** -- Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, c...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
