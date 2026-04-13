# Agent Project Development

> **v1.0.4** | Methodology for LLM-powered project development -- task-model fit analysis, pipeline architecture, file system state machines, cost estimation, and architectural reduction.
> 1 skill | 2 references | 13 trigger evals, 3 output evals

## The Problem

Starting an LLM-powered project without methodology leads to a predictable sequence of failures. Teams jump straight into building automation around a task the model cannot actually do well, burning weeks before discovering that the fundamental approach is flawed. A developer spends three days building a batch processing pipeline, only to find that the model hallucinates on 30% of inputs -- something a five-minute manual test would have revealed.

Even when the task is well-suited to LLM processing, teams build monolithic pipelines where the expensive LLM call, the fragile output parsing, and the deterministic rendering are all tangled together in a single script. When the parsing breaks (and it will -- LLMs do not follow format instructions perfectly), the only option is to re-run the entire pipeline, including all the LLM calls at $0.03 per item. At 1,000 items, that is $30 per debugging cycle.

Architecture decisions compound the problem. Teams add 17 specialized tools when the model only needs two. They build complex multi-agent orchestrations when a simple batch pipeline would suffice. They skip cost estimation and discover a $500 surprise bill after their first production run. Without a structured methodology, every LLM project is an expensive experiment that teams repeat from scratch each time.

## The Solution

This plugin provides a complete methodology for LLM-powered project development, from initial task-model fit assessment through production pipeline architecture. It starts with the most important step most teams skip: manually testing one example with the target model before writing any code. This five-minute validation prevents weeks of wasted development.

The core architecture is a five-stage pipeline -- acquire, prepare, process, parse, render -- where each stage is discrete, idempotent, and cacheable. The expensive non-deterministic LLM call (stage 3) is isolated from the deterministic stages, so you can iterate on parsing and rendering without re-running LLM calls. The file system serves as the state machine: each processing unit gets a directory, and stage completion is marked by file existence.

The skill also covers task-model fit recognition (which problems benefit from LLMs and which do not), cost estimation formulas, architectural reduction (when removing tools improves performance), and the decision framework for single-agent vs multi-agent approaches. Real case studies ground the methodology: Karpathy's HN Time Capsule ($58 for 930 items) and Vercel's d0 agent (80% to 100% success rate by reducing from 17 tools to 2).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Build automation first, discover the model cannot do the task weeks later | Manual prototype in 5 minutes validates task-model fit before any code |
| Monolithic pipeline re-runs all LLM calls ($30+) when parsing breaks | Staged pipeline isolates LLM calls; iterate on parsing for free |
| No cost estimate until the bill arrives | Formula-based estimation before development: items x tokens x price + 20-30% buffer |
| 17 specialized tools, 80% success rate | Architectural reduction to 2 primitives, 100% success rate (Vercel d0 pattern) |
| Debug by reading logs and guessing | File system state machine: every intermediate result is a human-readable file |
| Default to multi-agent because it sounds sophisticated | Decision framework: single-agent for independent items, multi-agent only when context isolation is necessary |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-project-development@skillstack
```

### Verify installation

After installing, test with:

```
I want to build a batch pipeline that analyzes 500 customer reviews with LLMs -- help me plan the architecture
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I have an idea for an LLM project -- help me figure out if it's worth building`
3. The skill walks you through task-model fit analysis: characteristics that match vs. don't match LLM strengths
4. Once validated, ask: `Design the pipeline architecture for this project`
5. The skill produces a staged pipeline with file system state management, cost estimate, and development plan

---

## System Overview

```
Task Idea
    |
    v
+-------------------+
| Task-Model Fit    |  <-- Manual prototype validation
| Assessment        |
+-------------------+
    |
    v
+-------------------+     +-----------------------+
| Pipeline Design   | --> | acquire -> prepare -> |
| (5-stage)         |     | process -> parse ->   |
|                   |     | render                |
+-------------------+     +-----------------------+
    |                              |
    v                              v
+-------------------+     +-------------------+
| Cost Estimation   |     | File System State |
| items x tokens    |     | data/{id}/        |
| x price           |     | raw.json          |
+-------------------+     | prompt.md         |
    |                     | response.md       |
    v                     | parsed.json       |
+-------------------+     +-------------------+
| Architecture      |
| Decision          |
| single vs multi   |
+-------------------+
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `agent-project-development` | Skill | Complete methodology for LLM project planning, architecture, and development |
| `case-studies.md` | Reference | Detailed analysis of production LLM projects: Karpathy HN Capsule, Vercel d0, Manus patterns |
| `pipeline-patterns.md` | Reference | Detailed pipeline architecture patterns for batch processing, data analysis, and content generation |

### Component Spotlights

#### agent-project-development (skill)

**What it does:** Activates when you are starting an LLM-powered project, evaluating task-model fit, designing pipeline architecture, estimating costs, or deciding between single-agent and multi-agent approaches. Provides a structured methodology that starts with manual validation and progresses through staged pipeline design.

**Input -> Output:** A project idea or requirement description -> Task-model fit assessment, pipeline architecture, cost estimate, development plan, and architectural decision rationale.

**When to use:**
- Starting a new project that might benefit from LLM processing
- Designing a batch processing pipeline for structured outputs
- Estimating costs and feasibility before committing development time
- Deciding between single-agent and multi-agent approaches
- Refactoring an existing LLM pipeline that is too complex or expensive

**When NOT to use:**
- Evaluating agent quality or building evaluation rubrics -> use `agent-evaluation`
- Designing multi-agent coordination, handoffs, or routing -> use `multi-agent-patterns`
- Building the actual tools for your agent -> use `tool-design`

**Try these prompts:**

```
I want to use an LLM to classify 10,000 support tickets by category and urgency -- is this a good fit?
```

```
Design a batch pipeline that takes company 10-K filings and produces structured financial summaries
```

```
My LLM pipeline costs $200 per run and takes 4 hours -- help me optimize the architecture
```

```
Should I use a single agent or multi-agent setup for my research synthesis project?
```

**Key references:**

| Reference | Topic |
|---|---|
| `case-studies.md` | Karpathy's HN Time Capsule (930 items, $58), Vercel d0 (17 tools to 2), Manus refactoring patterns |
| `pipeline-patterns.md` | Acquire-prepare-process-parse-render pipeline, file system state machines, structured output design, parallelization |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Build me an AI app" | "I want to analyze 500 product reviews and extract sentiment, key themes, and improvement suggestions -- help me plan the pipeline" |
| "Should I use agents?" | "I have a data enrichment task: take company names and produce structured profiles. Is this suited for LLM processing or should I use APIs?" |
| "Make it faster" | "My batch pipeline processes 1000 items but re-runs all LLM calls when parsing fails. How do I restructure it?" |
| "Use agent-project-development" | "Estimate the cost of running Claude Sonnet on 5,000 research papers with 4K token prompts and 2K token outputs" |

### Structured Prompt Templates

**For task-model fit assessment:**
```
I want to use an LLM to [task description]. The inputs are [input type and size]. The outputs need to be [output format]. Error tolerance is [high/low]. Help me assess whether this is a good fit for LLM processing.
```

**For pipeline design:**
```
Design a batch processing pipeline for [task]. I have [N] items, each is [item description]. I need [output format]. Show me the stage breakdown, file system structure, and parallelization approach.
```

**For cost estimation:**
```
Estimate the cost of processing [N] [items] with [model name]. Each item has approximately [N] input tokens and I expect [N] output tokens. Include a buffer for retries.
```

### Prompt Anti-Patterns

- **Skipping manual validation**: "Build the full pipeline for analyzing legal contracts" -- without first testing one contract manually, you risk building automation around a task the model cannot do. Always start with "test one example first."
- **Requesting multi-agent by default**: "I need a multi-agent system with a coordinator, researcher, and writer" -- multi-agent adds complexity. The skill will help you determine if your task actually needs context isolation across agents or if a simple pipeline suffices.
- **Ignoring costs**: "Process all 100K items in one run" -- token costs compound. The skill estimates costs before execution and recommends staging approaches (start with 100 items, validate quality, then scale).

## Real-World Walkthrough

**Starting situation:** You work at a fintech company with 5,000 quarterly earnings call transcripts. You need to extract structured data -- revenue figures, guidance changes, risk factors, and sentiment -- from each transcript and produce a searchable database. The transcripts average 15,000 words each.

**Step 1: Task-model fit assessment.** You ask: "Is extracting structured financial data from earnings call transcripts a good fit for LLM processing?" The skill walks through the fit criteria: synthesis across sources (yes -- each transcript is a single source, but the extraction requires understanding financial context), subjective judgment with rubrics (partially -- revenue figures are objective, but "risk factor significance" is subjective), error tolerance (moderate -- a few missed data points are acceptable, but fabricated revenue numbers are not). The skill identifies a key risk: hallucinated numbers. Recommendation: proceed with validation, but add a post-processing verification step for numerical claims.

**Step 2: Manual prototype.** You test one transcript manually. You paste it into Claude with a structured prompt requesting JSON output. The result is promising: revenue figures are correct, guidance changes are captured, risk factors are reasonable. Output tokens average 800 per transcript. Estimated input tokens: ~5,000 per transcript (after truncating non-essential sections like operator instructions).

**Step 3: Cost estimation.** You ask: "Estimate the cost for 5,000 transcripts with Claude Sonnet." The skill calculates: 5,000 items x (5,000 input + 800 output tokens) x pricing = approximately $195 base cost. With 25% retry buffer: ~$245 total. Wall-clock time with 15 parallel workers: approximately 2.5 hours. This is feasible for a quarterly run.

**Step 4: Pipeline architecture.** You ask: "Design the pipeline." The skill produces a five-stage architecture:
- **Acquire**: Download transcripts from SEC EDGAR API into `data/{ticker}_{date}/raw.txt`
- **Prepare**: Truncate to relevant sections, format as prompt with structured output template, write to `data/{ticker}_{date}/prompt.md`
- **Process**: Run LLM calls with 15 parallel workers, write responses to `data/{ticker}_{date}/response.md`
- **Parse**: Extract JSON from markdown response, validate numerical fields against regex patterns, write to `data/{ticker}_{date}/parsed.json`
- **Render**: Aggregate all parsed.json files into SQLite database and generate summary report

Each stage checks for output file existence before running, making the pipeline idempotent and resumable.

**Step 5: Architectural decision.** You consider whether to split extraction into specialized sub-agents (one for revenue, one for risk factors). The skill recommends against it: the transcript is a single document that fits in one context window, the extraction task does not exceed context limits, and a single prompt with multiple extraction targets is simpler and cheaper than coordinating multiple agents. Multi-agent would make sense if transcripts were 100K+ tokens or if different extraction tasks required different tools.

**Step 6: Iteration.** After the first run of 100 transcripts, parsing fails on 12% of items due to the model occasionally using different section headers. You fix the parser to handle variations (the skill warned about this) and re-run only the parse and render stages -- no LLM calls needed. Total cost of debugging: $0.

**Gotchas discovered:** The prepare stage needed to strip boilerplate sections (operator introductions, safe harbor disclaimers) to keep input tokens under 5,000. The skill recommended building a section-detection heuristic in the prepare stage rather than asking the LLM to ignore irrelevant content, saving ~30% on token costs.

## Usage Scenarios

### Scenario 1: Evaluating whether a task fits LLM processing

**Context:** Your PM wants to use AI to auto-generate personalized onboarding emails for new users based on their signup data. You are not sure if this is actually a good use of LLMs versus template-based generation.

**You say:** "We want to generate personalized onboarding emails from user signup data -- name, industry, use case. Should we use an LLM or stick with templates?"

**The skill provides:**
- Task-model fit analysis against six suitability criteria
- Identification that this is a natural language output task with synthesis (good fit) but has deterministic personalization needs (templates might suffice)
- Decision framework: if emails need to vary significantly by industry context, use LLM; if it is slot-filling with fixed structure, use templates
- Manual prototype instructions to test one email with the target model

**You end up with:** A clear recommendation with rationale, and one manually-generated example email to compare against your current template output.

### Scenario 2: Designing a batch content analysis pipeline

**Context:** Your content team has 2,000 blog posts and needs to categorize each by topic, extract key takeaways, and score readability. This needs to run monthly on new content.

**You say:** "Design a batch pipeline to analyze 2,000 blog posts for topic, takeaways, and readability score. It runs monthly."

**The skill provides:**
- Five-stage pipeline with file system state management
- Cost estimate ($40-60 per monthly run with Claude Haiku)
- Structured output prompt template with explicit format requirements
- Parallelization strategy (20 workers) and error handling
- Incremental processing: only analyze new/modified posts each month

**You end up with:** A production-ready pipeline architecture document with cost projections, directory structure, and implementation milestones.

### Scenario 3: Reducing an over-engineered agent system

**Context:** Your agent has 12 specialized tools for data analysis, but success rate is only 65%. Adding more tools and examples has not helped.

**You say:** "My data analysis agent has 12 tools and only succeeds 65% of the time. More tools don't seem to help. What's wrong?"

**The skill provides:**
- Architectural reduction analysis following the Vercel d0 pattern
- Identification that specialized tools may be constraining rather than enabling
- Recommendation to test with 2-3 primitive tools (bash, SQL, file read) instead
- Before/after comparison framework to measure improvement

**You end up with:** A reduction plan that removes 9 tools and replaces them with direct file access, with a test protocol to validate that simpler architecture actually improves success rate.

---

## Decision Logic

**When does this skill recommend single-agent vs multi-agent?**

Single-agent is the default recommendation when items are independent (no cross-item dependencies), context fits in one window, and the task does not require specialized sub-tools that would benefit from isolated context. Multi-agent is recommended when context isolation is needed (tasks exceed one context window), when specialized sub-agents measurably improve quality on specific subtasks, or when parallel exploration of different aspects is required. The primary reason for multi-agent is context isolation, not role anthropomorphization.

**When does architectural reduction apply?**

Reduction is recommended when success rate plateaus or declines as tools are added, when the data layer is well-documented and consistently structured (the model can navigate it directly), and when teams spend more time maintaining scaffolding than improving outcomes. The skill points to the Vercel d0 case study as evidence.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Skipped manual validation | Pipeline built on a task the model hallucinates on consistently | Stop. Test one example manually. If it fails, the task is not suited for LLM processing. |
| Monolithic pipeline | Debugging requires re-running all LLM calls; costs escalate | Refactor into five discrete stages with file system checkpoints between each |
| Cost overrun | Bill 5x higher than expected | Re-estimate with actual token counts from first 100 items; add retry buffer; consider cheaper model tier for simple items |
| Over-engineered architecture | Many tools, low success rate, high maintenance | Apply architectural reduction: test with 2-3 primitive tools; measure before/after |
| Parsing fragility | LLM output format varies; parser breaks on 10%+ of items | Build flexible regex parsers, add format enforcement in prompt, log failures for review |

## Ideal For

- **Engineers starting their first LLM-powered project** who need a structured methodology instead of trial-and-error
- **Data teams building batch processing pipelines** who need cost-effective, resumable, debuggable architectures
- **Technical leads evaluating project feasibility** who need task-model fit analysis and cost estimates before committing resources
- **Teams with over-engineered agent systems** who need to simplify architecture to improve success rates

## Not For

- **Evaluating agent quality after building** -- once the pipeline is running, use `agent-evaluation` for systematic quality measurement
- **Designing multi-agent coordination** -- if you already know you need multiple agents, use `multi-agent-patterns` for handoff protocols, routing, and orchestration
- **Building specific agent tools** -- for tool schema design and error handling patterns, use `tool-design`

## Related Plugins

- **agent-evaluation** -- Evaluate the outputs of the pipelines this skill helps you build
- **multi-agent-patterns** -- When your project outgrows single-agent architecture
- **tool-design** -- Design the tools your agent pipeline uses
- **context-optimization** -- Manage context efficiently in long-running agent tasks
- **prompt-engineering** -- Optimize the prompts within your pipeline stages

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
