# Agent Evaluation

> **v1.0.4** | Agent Architecture | 5 iterations

Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, direct scoring, confidence calibration, and continuous monitoring.

## What Problem Does This Solve

Agent systems are non-deterministic, can take multiple valid paths to the same goal, and produce outputs where no single "correct" answer exists — making traditional unit tests useless for measuring quality. Teams iterating on prompts, context strategies, or model versions have no reliable way to know whether a change improved or degraded performance. This skill provides the frameworks, rubric designs, and pipeline patterns to build systematic evaluation that catches regressions, validates improvements, and produces results that correlate with human judgment.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "How do I know if my prompt change made the agent better or worse?" | Test set design, baseline metric establishment, and evaluation pipeline patterns for comparing agent versions |
| "My LLM judge seems biased toward longer answers" | Position bias and length bias mitigation protocols including position-swap pairwise comparison |
| "I need to score agent responses on multiple dimensions like accuracy, completeness, and efficiency" | Multi-dimensional rubric design with weighted scoring, scale calibration, and strictness levels |
| "How do I build an automated evaluation pipeline for production?" | Production pipeline architecture with continuous monitoring, quality gates, and confidence scoring |
| "Should I use direct scoring or pairwise comparison for evaluating tone?" | Decision framework distinguishing objective criteria (direct scoring) from preference-based evaluation (pairwise) |
| "My automated evaluation disagrees with human reviewers — how do I fix this?" | Human evaluation protocols, correlation analysis, and feedback loops to calibrate automated judges |

## When NOT to Use This Skill

- testing code or applications -- use [testing-framework](../testing-framework/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-evaluation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

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

- **When to Activate** -- Conditions that indicate this skill should be used over testing-framework or multi-agent-patterns
- **Fundamentals** -- Why agent evaluation differs from software testing, the 95% performance variance finding, direct vs pairwise taxonomy, and metric selection by task type
- **Rubric Design** -- Multi-dimensional rubric structure, scale calibration (1-3, 1-5, 1-10), strictness levels, and domain adaptation guidance
- **The Bias Landscape** -- Documented LLM judge biases (position, length, self-enhancement, verbosity, authority) with specific mitigation strategies for each
- **Evaluation Approaches in Detail** -- Prompt structures for direct scoring and pairwise comparison, chain-of-thought requirements, and position-swap protocols
- **Test Set Design** -- Sample selection from real usage patterns, complexity stratification across four levels, and context degradation testing

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
