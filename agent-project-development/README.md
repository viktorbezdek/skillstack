# Agent Project Development

> **v1.0.4** | Agent Architecture | 5 iterations

Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, cost estimation, and architectural reduction.

## What Problem Does This Solve

Engineers starting LLM projects frequently build full automation pipelines before verifying the model can actually handle the task — wasting hours when the approach is fundamentally flawed. Even when the model fit is right, poorly structured pipelines mix deterministic and non-deterministic steps, making debugging and iteration slow. This skill provides a structured methodology for validating task-model fit before writing code, architecting pipelines as discrete cacheable stages, and estimating costs so token spend doesn't surprise teams at scale.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Should I use an LLM for this task or just write traditional code?" | Task-model fit framework with clear criteria for LLM-suited vs LLM-unsuited characteristics |
| "How do I structure a batch processing pipeline for 10,000 documents?" | The acquire-prepare-process-parse-render pipeline architecture with file system state machines |
| "My LLM pipeline is hard to debug — intermediate outputs are invisible" | File-per-stage persistence pattern that makes every step inspectable as human-readable files |
| "How much will this LLM project cost at scale?" | Cost estimation formula with token budget calculation, buffer recommendations, and optimization strategies |
| "Should I build one agent or multiple specialized agents?" | Single vs multi-agent decision framework based on context isolation needs and task complexity |
| "My agent pipeline has 17 specialized tools but performance is poor" | Architectural reduction patterns with real case study showing 80% tool removal improving success rate from 80% to 100% |

## When NOT to Use This Skill

- evaluating agent quality or building evaluation rubrics -- use [agent-evaluation](../agent-evaluation/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-project-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the agent-project-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `project-development`
- `pipeline`
- `task-model-fit`
- `cost-estimation`

## What's Inside

- **When to Activate** -- Conditions for applying this methodology vs agent-evaluation or multi-agent-patterns
- **Core Concepts** -- Task-model fit tables, manual prototype validation, the acquire-prepare-process-parse-render pipeline, file system state machine pattern, structured output design, and cost estimation formulas
- **Detailed Topics** -- Single vs multi-agent architecture decision criteria, architectural reduction principles, and iteration planning for production systems
- **Practical Guidance** -- Five-step project planning template covering task analysis, manual validation, architecture selection, cost estimation, and development plan
- **Examples** -- Karpathy's HN Time Capsule batch pipeline ($58, 930 documents) and Vercel d0 architectural reduction (17 tools to 2, 80% to 100% success rate)

## Key Capabilities

- **Discrete**
- **Idempotent**
- **Cacheable**
- **Independent**

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(agent-project-development): add standard keywords and expand README to full format (ca2a55d)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, c...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
