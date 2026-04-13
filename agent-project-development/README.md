# Agent Project Development

> **v1.0.4** | Agent Architecture | 5 iterations

> A structured methodology for starting LLM projects right -- task-model fit validation, pipeline architecture, file system state machines, cost estimation, and knowing when to simplify.

## The Problem

Engineers starting LLM-powered projects routinely make the same expensive mistakes. They spend days building a full automation pipeline before checking whether the model can actually handle the task -- then discover the approach is fundamentally flawed. They build monolithic scripts that mix deterministic data fetching with non-deterministic LLM calls, making it impossible to iterate on prompts without re-running the entire pipeline. They scale to 10,000 items without estimating costs, then get a four-figure API bill they did not budget for.

Even teams that avoid these traps struggle with architecture decisions. Should this be one agent or three? Do I need 17 specialized tools or can the model work with bash and file access? When my pipeline fails on item 847 of 2,000, do I need to re-run everything from scratch? These questions do not have generic answers -- they depend on task characteristics, model capabilities, and cost constraints that need systematic evaluation.

The result is wasted development time, unexpectedly high costs, over-engineered architectures that constrain model performance, and pipelines that cannot be debugged or iterated on efficiently. The knowledge to avoid these mistakes exists in production case studies, but it is scattered across blog posts and conference talks rather than structured into an actionable methodology.

## The Solution

This plugin provides a complete project development methodology grounded in production case studies from Karpathy (HN Time Capsule, 930 docs for $58), Vercel (d0 agent, 17 tools reduced to 2 with 80% to 100% success rate), Manus (KV-cache optimization, file system as memory), and Anthropic (multi-agent research, 95% variance from three factors).

The skill starts with task-model fit evaluation -- a structured comparison of your task characteristics against LLM strengths and weaknesses, followed by a manual prototype step that takes minutes and prevents hours of wasted automation. It then guides pipeline architecture using the acquire-prepare-process-parse-render pattern where only the LLM call is non-deterministic, with file system state machines that provide natural idempotency, easy debugging, and trivial caching. Cost estimation happens before you commit, not after the bill arrives. And the architectural reduction framework helps you decide when simplifying (fewer tools, simpler architecture) actually improves performance.

You end up with a validated project plan, a pipeline architecture that can be debugged and iterated stage by stage, cost estimates grounded in real token measurements, and an architecture right-sized for your actual needs.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Building full automation before validating the model can do the task | Manual prototype in minutes validates task-model fit before writing code |
| Monolithic scripts where prompt iteration requires re-running everything | Staged pipeline where you re-run only the LLM call stage, preserving all other work |
| No idea what 10,000 items will cost until the bill arrives | Cost estimation formula with 20-30% buffer calculated before committing |
| 17 specialized tools that constrain rather than enable the model | Architectural reduction framework -- fewer tools can mean higher success rates |
| Pipeline fails on item 847 and you re-run all 2,000 from scratch | File system state machine where each item's progress persists independently |
| Guessing whether to use single-agent or multi-agent | Decision framework based on context isolation needs, not role anthropomorphization |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-project-development@skillstack
```

### Verify Installation

After installing, test with:

```
I'm starting a project to analyze customer reviews with an LLM -- help me plan the architecture
```

The skill activates automatically when you mention LLM project development topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your project idea:
   ```
   Should I use an LLM to classify and summarize 5,000 support tickets, or should I just write rules?
   ```
3. The skill evaluates task-model fit, walks you through a manual prototype, and recommends an approach.
4. If the fit is good, you get a staged pipeline architecture with cost estimates:
   ```
   Design the pipeline architecture for processing these 5,000 tickets with structured output
   ```
5. You end up with a file system state machine, parallel execution plan, and cost projection before writing a line of production code.

## What's Inside

This is a single-skill plugin backed by two detailed reference documents and a comprehensive eval suite.

| Component | Purpose |
|---|---|
| **agent-project-development** skill | Core methodology: task-model fit tables, manual prototype step, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, structured output design, cost estimation, single vs multi-agent decision framework, architectural reduction, 10 guidelines |
| **case-studies.md** | Four production case studies: Karpathy HN Time Capsule (930 docs, $58, 5-stage pipeline), Vercel d0 (17 tools to 2, 80% to 100% success), Manus context engineering (KV-cache, append-only context), Anthropic multi-agent research (95% variance from three factors). Cross-case pattern analysis |
| **pipeline-patterns.md** | Implementation code: file system state management, parallel execution (ThreadPoolExecutor, rate limiting), structured output parsing with graceful degradation, error handling with retry/backoff, cost estimation, CLI structure, checkpoint/resume, stage testing |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: agent-project-development

**What it does:** Guides you from "I have an idea for an LLM project" through task validation, architecture design, cost estimation, and implementation planning. Activates when you are starting a new LLM project, evaluating task-model fit, designing batch pipelines, estimating costs, choosing between single and multi-agent approaches, or diagnosing over-engineered agent systems.

**Try these prompts:**

```
I want to process 10,000 product descriptions through an LLM to generate SEO metadata -- is this a good fit and how should I architect it?
```

```
My agent has 12 specialized tools but keeps failing on complex queries -- should I simplify?
```

```
Help me estimate how much it will cost to run 50,000 customer reviews through Claude for sentiment analysis and summarization
```

```
I have a batch pipeline that fails halfway through and I have to restart from scratch -- how do I fix this?
```

```
Should I use a single agent or break this into multiple specialized agents? The task is research synthesis across 20+ sources.
```

**Key references:**

| Reference | Topic |
|---|---|
| `case-studies.md` | Karpathy HN Time Capsule ($58 for 930 docs), Vercel d0 (17 tools to 2), Manus context engineering, Anthropic multi-agent research |
| `pipeline-patterns.md` | File system state management, parallel execution, structured output parsing, error handling, cost estimation, checkpoint/resume |

## Real-World Walkthrough

Your team wants to analyze 2,000 competitor product listings to extract pricing patterns, feature comparisons, and market positioning insights. Nobody has done this before, and the VP wants a cost estimate by Friday.

You start by checking task-model fit:

```
We have 2,000 competitor product listings scraped as HTML. We want to extract pricing, features, and positioning for each. Is this a good fit for LLM processing?
```

The skill evaluates your task against the fit tables. Synthesis across structured and unstructured sources -- good fit. Subjective judgment needed for "positioning" classification -- good fit. Error tolerance (a few misclassified products will not break the analysis) -- good fit. No real-time requirements -- good fit. The skill recommends proceeding but flags that pricing extraction might work better with traditional parsing if the HTML is consistent. You decide to test both approaches.

Next, the manual prototype. You copy one product listing HTML into Claude and ask for the structured output you need. The response correctly extracts price ($299/year), identifies five features, and classifies the positioning as "enterprise mid-market." This took three minutes and confirmed the model can do the task. You also notice the output format needs adjustment -- the model includes explanations you do not need. You refine the prompt template.

Now the architecture:

```
Design the pipeline for processing 2,000 product listings -- I need it to be resumable if it fails partway through
```

The skill produces the canonical five-stage pipeline: **acquire** (read HTML files from the scraper output directory), **prepare** (strip HTML to relevant sections and build the prompt with your template), **process** (send to Claude API with structured output requirements), **parse** (extract pricing, features, and positioning from the response), **render** (generate the comparison spreadsheet and summary report).

The file system state machine puts each product in `data/{product_id}/` with `raw.html`, `prompt.md`, `response.md`, and `parsed.json` marking each stage's completion. If the pipeline crashes on item 1,247, you re-run and it skips the 1,246 already-completed items automatically. No database needed -- file existence is the state.

Cost estimation comes next:

```
Estimate the cost for 2,000 items -- each HTML page is about 15KB, and I need roughly 500 tokens of structured output per item
```

The skill calculates: input tokens per item (roughly 4,000 tokens for 15KB of HTML context plus prompt template), output tokens per item (500), total tokens (2,000 items times 4,500 tokens), API cost at Claude Sonnet pricing, plus 25% buffer for retries. The estimate comes to approximately $12-18 -- well within budget. You report this to the VP with confidence.

For the process stage, the skill recommends ThreadPoolExecutor with 10 workers to stay within API rate limits, with exponential backoff on failures. Each worker processes one product directory independently, writes the response file, and moves to the next item. The parallel execution cuts wall-clock time from 6 hours to under 40 minutes.

You build the pipeline in a day, run it overnight, and find that 1,847 of 2,000 items parsed cleanly. The 153 failures are logged with their error details. You examine a few -- mostly unusual HTML structures the prompt did not anticipate. You adjust the prepare stage to handle these edge cases, delete only the failed items' `response.md` files, and re-run. The pipeline processes only the 153 items, and 149 succeed. Four genuinely malformed listings are flagged for manual review.

Total cost: $14.50. Total time: about 5 hours of development plus 40 minutes of execution. The VP gets the competitive analysis report on Thursday, a day ahead of schedule.

## Usage Scenarios

### Scenario 1: Evaluating task-model fit before committing

**Context:** Your team wants to use an LLM to auto-generate release notes from git commit histories. Nobody has tested whether this actually works well enough to ship.

**You say:** "We want to generate customer-facing release notes from git commits -- is this a good task for an LLM or should we just write templates?"

**The skill provides:**
- Task-model fit evaluation against the characteristics tables
- Manual prototype instructions (copy 10 commits into Claude, evaluate the output)
- Identification of edge cases (merge commits, dependency updates, security fixes)
- Recommendation on hybrid approach (LLM for narrative, templates for structured sections)

**You end up with:** A validated decision on whether to proceed, with a manual prototype proving the approach works before any automation is built.

### Scenario 2: Designing a resumable batch pipeline

**Context:** You need to process 50,000 documents through an LLM but your last attempt crashed at item 23,000 and you had to start over, burning $200 in API costs.

**You say:** "I have a batch pipeline that keeps failing halfway through -- how do I make it resumable so I don't waste money re-processing items?"

**The skill provides:**
- File system state machine pattern with per-item directories
- Stage completion markers (file existence = done)
- Idempotent re-run logic (skip items with existing output files)
- Checkpoint/resume implementation code
- Error logging per item for post-run analysis

**You end up with:** A pipeline architecture where crashes only lose the single in-progress item, and re-running automatically resumes from where it left off.

### Scenario 3: Deciding on architectural simplification

**Context:** Your agent has 15 specialized tools (search, summarize, classify, extract, validate, format, etc.) but performance has been declining as you add more tools. Complex queries that used to work now fail.

**You say:** "My agent has 15 tools but performance is getting worse -- the Vercel team improved by removing tools. Should I do the same?"

**The skill provides:**
- The Vercel d0 case study (17 tools to 2, 80% to 100% success rate, 3.5x faster)
- Decision framework for when reduction outperforms complexity
- Analysis of whether your tools are constraining vs. enabling the model
- Reduction strategy: identify which tools duplicate file system capabilities

**You end up with:** A concrete reduction plan identifying which tools to remove, with the d0 case study as evidence that fewer tools can mean dramatically better performance.

### Scenario 4: Estimating costs before committing

**Context:** The product team wants to run an LLM analysis on your entire customer feedback database (100,000 entries). Leadership wants a cost estimate before approving the project.

**You say:** "Estimate how much it will cost to process 100,000 customer feedback entries through Claude for sentiment, topic classification, and summary generation"

**The skill provides:**
- Token estimation methodology (input context + prompt template + output per item)
- Cost formula with the 20-30% retry buffer
- Comparison of model tiers (Haiku for classification, Sonnet for summaries)
- Hierarchical processing strategy (cheap model for simple items, expensive model for complex ones)
- Reference to the Karpathy case study ($58 for 930 items) for calibration

**You end up with:** A defensible cost estimate with confidence intervals, a recommended model-tier strategy, and a phased rollout plan (start with 1,000 items to validate estimates).

## Ideal For

- **Engineers starting their first LLM project** -- the task-model fit evaluation and manual prototype step prevent the most common costly mistake: building automation before validating the model can do the task
- **Teams building batch processing pipelines** -- the staged pipeline architecture with file system state machines provides resumability, debuggability, and fast iteration out of the box
- **Technical leads estimating LLM project costs** -- the cost estimation framework with real case study calibration points ($58 for 930 items) produces defensible numbers for leadership
- **Anyone with an over-engineered agent** -- the architectural reduction framework, backed by the Vercel d0 case study, provides evidence-based guidance on when simplifying improves performance
- **Developers choosing between single and multi-agent architectures** -- the decision framework based on context isolation needs (not role anthropomorphization) prevents unnecessary complexity

## Not For

- **Evaluating agent quality or building scoring rubrics** -- use [agent-evaluation](../agent-evaluation/) for LLM-as-judge, bias mitigation, and evaluation pipelines
- **Designing multi-agent coordination and handoff protocols** -- use [multi-agent-patterns](../multi-agent-patterns/) for supervisor, swarm, and hierarchical architectures
- **Building agent memory systems** -- use [memory-systems](../memory-systems/) for production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through two reference documents.

The **SKILL.md** body covers the full project development methodology: task-model fit recognition tables, the manual prototype validation step, the acquire-prepare-process-parse-render pipeline architecture, file system state machine patterns, structured output design with format enforcement, agent-assisted development practices, cost estimation formulas, single vs. multi-agent decision framework, architectural reduction principles, anti-patterns to avoid, and a five-step project planning template.

When deeper implementation detail is needed, Claude draws from the references:

- **case-studies.md** provides four detailed production case studies with concrete numbers (Karpathy's $58 for 930 documents, Vercel's 80% to 100% success rate improvement). These ground the methodology in real-world evidence rather than theoretical advice.
- **pipeline-patterns.md** provides implementation code for file system state management, parallel execution with ThreadPoolExecutor and rate limiting, structured output parsing with graceful degradation, error handling with retry/backoff, cost estimation calculations, and checkpoint/resume logic.

Simple questions ("should I use an LLM for this?") are answered from the core skill's task-model fit tables. Architecture design pulls from both the skill body and the pipeline patterns reference. "Show me how Vercel improved by removing tools" pulls from the case studies reference.

## Related Plugins

- **[Agent Evaluation](../agent-evaluation/)** -- Rubrics, LLM-as-judge, bias mitigation for measuring agent quality
- **[BDI Mental States](../bdi-mental-states/)** -- Cognitive architecture with belief-desire-intention modeling for agents
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for background agents: sandboxes, registries, self-spawning
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Supervisor, swarm, and hierarchical patterns for multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
