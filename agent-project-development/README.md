# Agent Project Development

> **v1.0.4** | Agent Architecture | 5 iterations

Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, cost estimation, and architectural reduction.

## What Problem Does This Solve

Engineers starting LLM projects frequently build full automation pipelines before verifying the model can actually handle the task -- wasting hours when the approach is fundamentally flawed. Even when the model fit is right, poorly structured pipelines mix deterministic and non-deterministic steps, making debugging impossible and iteration slow. Token costs compound at scale without anyone noticing until the bill arrives.

This skill provides a structured methodology covering the entire project lifecycle: validating task-model fit before writing code, architecting pipelines as discrete cacheable stages where only the LLM call is non-deterministic, using the file system as a state machine for natural idempotency, estimating costs before committing, and knowing when to simplify rather than add complexity. Grounded in real production case studies (Karpathy's HN Time Capsule, Vercel d0, Manus, Anthropic multi-agent research).

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-project-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention project development topics, or you can invoke it explicitly with `Use the agent-project-development skill to ...`.

## What's Inside

This is a single-skill plugin with two reference documents:

| Component | What It Covers |
|---|---|
| **SKILL.md** | Task-model fit recognition (LLM-suited vs LLM-unsuited characteristics tables), the manual prototype step, the acquire-prepare-process-parse-render pipeline architecture, file system state machine pattern, structured output design with format enforcement, agent-assisted development practices, cost estimation formulas, single vs multi-agent architecture decision framework, architectural reduction principles, and a five-step project planning template |
| **references/case-studies.md** | Four detailed case studies: Karpathy's HN Time Capsule (930 docs, $58, 5-stage pipeline), Vercel d0 (17 tools to 2, 80% to 100% success rate), Manus context engineering (KV-cache optimization, append-only context, file system as memory), and Anthropic multi-agent research (95% performance variance explained by three factors). Includes cross-case pattern analysis |
| **references/pipeline-patterns.md** | Implementation code for file system state management (directory structure, state checking, clean/retry), parallel execution (ThreadPoolExecutor, rate limiting, batch sizing), structured output parsing (section extraction, field extraction, graceful degradation), error handling (retry with backoff, error logging, partial success), cost estimation (token counting, batch cost calculation), CLI structure, rendering patterns, checkpoint/resume, and stage testing patterns |

## Usage Scenarios

**1. "Should I use an LLM for this task or just write code?"**
Use the task-model fit tables. If your task involves synthesis across sources, subjective judgment with rubrics, and tolerates errors -- it fits. If it requires precise computation, real-time responses, or deterministic output -- it does not. Run the manual prototype: copy one representative input into the target model. If that fails, automation will fail. If it succeeds, you have your baseline.

**2. "I need to process 10,000 documents through an LLM."**
Follow the canonical pipeline: acquire raw data, prepare prompts, process with LLM (the only non-deterministic step), parse structured output, render final results. Each stage persists output to disk per item. Re-running skips completed items. Use the cost estimation formula (`items x tokens_per_item x price_per_token + 20-30% buffer`) before starting. Use ThreadPoolExecutor with 10-15 workers for the process stage, staying within API rate limits.

**3. "My agent has 17 specialized tools but performance is declining."**
Study the Vercel d0 case study. They removed 80% of their tools and saw success rate jump from 80% to 100%, execution time drop 3.5x, and token usage fall 37%. The key question: are your tools constraining the model rather than enabling it? If your data layer is well-documented, the model may perform better with direct file system access plus standard Unix utilities instead of custom tool wrappers.

**4. "How do I estimate what this LLM project will cost before committing?"**
Use the cost estimation patterns: count tokens per item (prompt template + context), estimate output tokens (typical response length), multiply by item count, add 20-30% buffer for retries. The Karpathy project processed 930 items for $58. Track actual costs during development -- if they exceed estimates significantly, reconsider the approach before scaling.

**5. "Single agent or multi-agent architecture?"**
Use multi-agent only when you need context isolation (subtasks exceed a single context window) or parallel exploration of different aspects. The primary reason for sub-agents is fresh context windows, not role anthropomorphization. Single pipelines are simpler for batch processing where items are independent. See the Manus case study for how sub-agents with constrained output schemas provide context isolation without complexity.

## When to Use / When NOT to Use

**Use when:**
- Starting a new project that might benefit from LLM processing
- Evaluating whether a task suits agents versus traditional code
- Designing batch processing pipeline architecture
- Estimating costs and timelines for LLM-heavy projects
- Deciding between single-agent and multi-agent approaches
- Diagnosing why an over-engineered agent pipeline underperforms

**Do NOT use when:**
- Evaluating agent quality or building evaluation rubrics -- use [agent-evaluation](../agent-evaluation/) instead
- Designing multi-agent coordination, handoffs, or communication protocols -- use [multi-agent-patterns](../multi-agent-patterns/) instead
- Building the memory layer for your agent -- use [memory-systems](../memory-systems/) instead

## Related Plugins

- **[Agent Evaluation](../agent-evaluation/)** -- Rubrics, LLM-as-judge, bias mitigation for measuring agent quality
- **[BDI Mental States](../bdi-mental-states/)** -- Cognitive architecture with belief-desire-intention modeling for agents
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for background agents: sandboxes, registries, self-spawning
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Supervisor, swarm, and hierarchical patterns for multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
