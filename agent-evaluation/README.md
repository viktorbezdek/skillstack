# Agent Evaluation

> **v1.0.4** | Agent Architecture | 5 iterations

> Build evaluation systems for LLM agents that actually correlate with human judgment -- rubrics, bias mitigation, scoring pipelines, and production monitoring.

## The Problem

You changed a prompt and the agent "feels" better. But you have no data. You run the same query five times and get five different quality levels, and there is no systematic way to tell whether version A outperforms version B. Traditional unit tests are useless here -- agent outputs are non-deterministic, multiple valid paths exist for any task, and there is no single "correct" answer to compare against.

Teams building with LLMs discover this the hard way. They ship a prompt change that looks great on three hand-picked examples, only to find it regressed on edge cases nobody tested. Or they build an automated evaluation pipeline using LLM-as-judge, but the scores do not match what human reviewers think -- because position bias, length bias, and self-enhancement bias are silently corrupting every result. Debugging why an evaluation system disagrees with humans requires understanding which bias is at play and how to mitigate it.

The gap is not "evaluation is hard" -- it is that building a trustworthy evaluation system requires rubric design, bias mitigation protocols, metric selection, test set stratification, and production pipeline architecture, all working together. Most teams get one or two of these right and wonder why their numbers are unreliable.

## The Solution

This plugin provides the complete evaluation toolkit: multi-dimensional rubrics with calibrated scoring scales, five documented bias types with concrete mitigation techniques (position swap protocol, length-normalized scoring, cross-model evaluation), both direct scoring and pairwise comparison approaches with decision frameworks for choosing between them, test set design stratified by complexity, and production pipeline architecture from criteria loading through confidence scoring.

The skill walks you through designing rubrics that reduce evaluation variance by 40-60%, implementing position swap protocols that catch position bias before it corrupts your results, choosing the right metric for your task type (Spearman's rho for ordinal scales, Cohen's kappa for classification, agreement rate for pairwise), and building CI-integrated evaluation pipelines with quality gates. It includes the 95% performance variance finding from BrowseComp research (80% token usage, 10% tool calls, 5% model choice) so you know where to focus optimization efforts.

You end up with evaluation systems that produce numbers you can trust, catch regressions before they ship, and improve through feedback loops between automated and human judgment.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Eyeballing agent quality on 3 hand-picked examples | Systematic evaluation across complexity-stratified test sets |
| LLM-as-judge scores that silently suffer from position and length bias | Position swap protocol and length-normalized scoring catching bias before it corrupts results |
| Single "quality score" that hides dimension-specific regressions | Multi-dimensional rubrics scoring accuracy, completeness, efficiency, and more independently |
| No data on whether a prompt change helped or hurt | Automated pipeline comparing versions with statistical metrics (Spearman's rho, Cohen's kappa) |
| Evaluation scores that do not match human judgment | Calibrated scoring with confidence levels and human-in-the-loop validation |
| Ad hoc evaluation before releases only | Continuous evaluation in CI with alert thresholds for quality drops |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-evaluation@skillstack
```

### Verify Installation

After installing, test with:

```
Help me design an evaluation rubric for my customer support agent
```

The skill activates automatically when you mention evaluation-related topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your evaluation need:
   ```
   I need to measure whether my prompt changes are actually improving my agent's accuracy
   ```
3. The skill guides you through rubric design -- choosing dimensions, calibrating scales, and defining level descriptions with domain-specific language.
4. You get a multi-dimensional rubric, a test set structure stratified by complexity, and a scoring pipeline with bias mitigation built in.
5. Next, build continuous evaluation:
   ```
   Help me add this evaluation as a quality gate in my CI pipeline
   ```

## What's Inside

This is a single-skill plugin backed by four deep reference documents and a comprehensive eval suite.

| Component | Purpose |
|---|---|
| **agent-evaluation** skill | Core methodology: rubric design, bias landscape, evaluation taxonomy, pipeline architecture, 18 actionable guidelines |
| **bias-mitigation.md** | Implementation code for position swap, multi-shuffle comparison, length-normalized scoring, cross-model evaluation, blind evaluation, aggregate bias monitoring |
| **implementation-patterns.md** | Five production patterns: structured pipeline, hierarchical evaluation, Panel of LLM Judges (PoLL), confidence calibration, structured output formatting |
| **metrics-guide.md** | Metric selection guide: classification metrics, agreement metrics, correlation metrics, pairwise comparison metrics, decision tree by task type |
| **metrics.md** | Rubric implementation code: five evaluation dimensions, weighted scoring, test set management, evaluation runner, production monitoring with alert thresholds |

**Eval coverage:** 15 trigger eval cases + 3 output eval cases.

### How to Use: agent-evaluation

**What it does:** Guides you through designing, implementing, and operating evaluation systems for LLM agents. Activates when you need to measure agent quality, build rubrics, compare model outputs, set up evaluation pipelines, or debug bias in existing evaluation systems. Covers the full spectrum from rubric design through production monitoring.

**Try these prompts:**

```
Help me design an evaluation rubric for a code review agent that checks for security issues, code style, and test coverage
```

```
My LLM-as-judge scores don't correlate with what our human reviewers think -- how do I debug this?
```

```
I need to compare two prompt versions head-to-head for my customer support agent -- what approach should I use?
```

```
Set up a production evaluation pipeline with quality gates for our RAG agent that runs on every prompt change
```

```
How should I build my test set? I have a search agent that handles everything from simple lookups to multi-step research tasks
```

**Key references:**

| Reference | Topic |
|---|---|
| `bias-mitigation.md` | Position swap protocol, length-normalized scoring, cross-model evaluation, aggregate bias monitoring with z-score detection |
| `implementation-patterns.md` | Structured pipeline, hierarchical evaluation, Panel of LLM Judges, confidence calibration, retry logic |
| `metrics-guide.md` | Metric selection by task type: precision/recall for classification, Spearman's rho for ordinal, agreement rate for pairwise |
| `metrics.md` | Rubric implementation with five dimensions, weighted scoring, test set management class, evaluation runner, production alerts |

## Real-World Walkthrough

You are building a research agent that searches the web, synthesizes information from multiple sources, and produces summary reports. The agent has been running for a month, and your team has iterated on the prompt three times. Each time, someone says "this version feels better" but nobody has data. Last week, a customer complained that the agent cited a source that did not actually support the claim it was making -- a hallucination that your ad hoc testing missed.

You start by asking Claude:

```
I have a research agent that synthesizes web sources into reports. I need to evaluate it systematically -- we've had hallucination issues and I want to catch them before customers do.
```

The skill begins with rubric design. For a research agent, it recommends five dimensions: factual accuracy (weight 0.3), citation accuracy (weight 0.25), completeness (weight 0.2), source quality (weight 0.15), and coherence (weight 0.1). Each dimension gets a 1-5 scale with domain-specific level descriptions. For citation accuracy, level 1 is "citations do not match claimed sources" and level 5 is "every claim links to the correct source passage." This is not a generic quality rubric -- it targets exactly the failure mode your customer reported.

Next, you build the test set:

```
Help me design a test set that covers simple lookups through complex multi-source synthesis
```

The skill structures your test set into four complexity tiers: simple (single-source factual lookup, 5 cases), medium (two-source comparison, 5 cases), complex (multi-source synthesis with conflicting information, 5 cases), and very complex (research requiring chain-of-reasoning across 5+ sources, 5 cases). Each case includes the query, expected source types, and known ground truth where available. The skill emphasizes including cases where sources contradict each other -- this is where hallucination is most likely.

Now the evaluation approach. Factual accuracy and citation accuracy have objective ground truth, so they use direct scoring. Coherence is subjective, so it uses pairwise comparison between the current and previous prompt versions. You implement the position swap protocol for the pairwise evaluations -- running each comparison twice with responses in swapped positions and checking for consistency.

You wire the evaluation into your CI pipeline:

```
Now help me build this into a pipeline that runs automatically when we change the prompt
```

The skill produces a pipeline architecture: criteria loader pulls the rubric, primary scorer runs direct scoring on each dimension, bias mitigation layer applies length-normalized scoring (your agent's longer responses were scoring artificially higher), and confidence scoring calibrates based on evidence strength. The pipeline outputs per-dimension scores, an overall weighted score, confidence levels, and specific justifications. A quality gate blocks prompt changes if the overall score drops below 0.7 or if any single dimension drops below 0.5.

After running the pipeline on your three historical prompt versions, you discover that version 2 actually regressed on citation accuracy (from 0.78 to 0.61) even though it improved coherence (from 0.65 to 0.82). The "feels better" judgment was tracking coherence while ignoring the hallucination regression. With the multi-dimensional rubric, you would have caught this immediately.

You also find that your evaluation scores for longer responses were inflated by 15% due to length bias. After applying length-normalized scoring, the rankings change -- a concise version that was ranked third actually produces the most accurate citations. This is the kind of insight that only a properly debiased evaluation system reveals.

The pipeline now runs on every prompt change, tracks metrics over time, and alerts when any dimension drops below threshold. Your hallucination problem has a systematic defense, not just a hope that someone will notice.

## Usage Scenarios

### Scenario 1: Validating a prompt change with data

**Context:** You rewrote your agent's system prompt to improve response quality. It looks better on the few examples you tested manually, but you need to know if it actually improved across the board before shipping to production.

**You say:** "I changed my agent's system prompt and need to validate it didn't regress -- help me set up a before/after comparison"

**The skill provides:**
- Decision framework for choosing direct scoring vs. pairwise comparison per quality dimension
- Test set design stratified by complexity so edge cases are covered
- Position swap protocol to prevent bias from corrupting the comparison
- Statistical metrics (Spearman's rho, weighted kappa) for quantifying the difference
- Quality gate thresholds for deciding ship vs. no-ship

**You end up with:** A data-backed comparison showing per-dimension scores for both prompt versions, statistical confidence in the difference, and a clear ship/no-ship recommendation.

### Scenario 2: Debugging an unreliable LLM-as-judge

**Context:** You built an automated evaluation system, but when you compare its scores to human reviewer judgments, the correlation is only 0.45. You need to figure out why the automated judge disagrees with humans and fix it.

**You say:** "My automated evaluation scores have low correlation with human reviewers -- what's going wrong and how do I fix it?"

**The skill provides:**
- Systematic diagnosis through the five bias types (position, length, self-enhancement, verbosity, authority)
- Metric selection for measuring human-automated agreement (Spearman's rho, Cohen's kappa)
- Specific mitigation implementations for each identified bias
- Aggregate bias monitoring with z-score detection for ongoing tracking
- Confidence calibration to flag low-confidence judgments for human review

**You end up with:** An identified root cause (e.g., length bias inflating scores for verbose responses), a concrete fix (length-normalized scoring), and improved human-automated correlation above 0.7.

### Scenario 3: Building evaluation into CI/CD

**Context:** Your team iterates on an agent weekly. Changes ship without systematic quality checks because nobody has time to manually evaluate. You need automated quality gates.

**You say:** "Set up a production evaluation pipeline with quality gates for our agent that runs on every prompt change in CI"

**The skill provides:**
- Pipeline architecture: criteria loader, primary scorer, bias mitigation, confidence scoring
- Hierarchical evaluation pattern for cost efficiency (cheap model screens, expensive model handles edge cases)
- Quality gate configuration with per-dimension thresholds
- Production monitoring with alert thresholds and trend tracking
- Panel of LLM Judges (PoLL) pattern for high-stakes evaluations

**You end up with:** A CI-integrated evaluation pipeline that blocks prompt changes when quality drops below threshold, with cost-efficient hierarchical scoring and production dashboards tracking quality trends over time.

### Scenario 4: Comparing two models head-to-head

**Context:** You are deciding between GPT-4o and Claude for your agent's backbone. You need a fair comparison that accounts for the biases inherent in having one LLM judge another.

**You say:** "I need to compare GPT-4o and Claude for my research agent -- how do I run a fair head-to-head evaluation?"

**The skill provides:**
- Cross-model evaluation setup to avoid self-enhancement bias
- Pairwise comparison with position swap protocol
- Multi-shuffle variant with majority vote for high-stakes decisions
- Blind evaluation where the judge does not know which model produced which response
- Dimension-specific scoring so you see where each model excels

**You end up with:** A bias-mitigated head-to-head comparison with per-dimension breakdowns, confidence scores, and a justified recommendation for which model fits your use case.

## Ideal For

- **Teams iterating on agent prompts** -- the evaluation framework catches regressions that "feels better" testing misses, using systematic comparison with statistical metrics
- **Engineers building LLM-as-judge systems** -- the bias mitigation protocols (position swap, length normalization, cross-model) prevent the five most common failure modes
- **Organizations adding quality gates to agent CI/CD** -- the production pipeline patterns and hierarchical evaluation strategy balance thoroughness with cost
- **Anyone debugging evaluation reliability** -- the metric selection framework and human-automated correlation analysis pinpoint exactly why scores diverge from human judgment
- **Researchers benchmarking agent performance** -- the test set stratification by complexity and multi-dimensional rubrics provide publishable evaluation methodology

## Not For

- **Testing application code or APIs** -- use [testing-framework](../testing-framework/) for unit, integration, and E2E test design
- **Designing or coordinating multi-agent systems** -- use [multi-agent-patterns](../multi-agent-patterns/) for supervisor, swarm, and hierarchical architectures
- **Building the agent itself** -- use [agent-project-development](../agent-project-development/) for task-model fit, pipeline architecture, and cost estimation

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through four reference documents.

The **SKILL.md** body provides the conceptual framework: why agent evaluation differs from traditional testing (non-determinism, multiple valid paths, composite quality dimensions), the evaluation taxonomy (direct scoring vs. pairwise comparison), rubric design methodology (multi-dimensional, scale-calibrated, domain-adapted), the five bias types and their mitigations, and production pipeline architecture. It includes 18 actionable guidelines and a 10-step framework for building evaluation systems from scratch.

When deeper implementation detail is needed, Claude draws from the reference documents:

- **bias-mitigation.md** activates when you need concrete code for position swap protocols, length normalization, or aggregate bias monitoring
- **implementation-patterns.md** activates for production pipeline construction -- structured evaluation, hierarchical evaluation, Panel of LLM Judges, and confidence calibration
- **metrics-guide.md** activates when choosing between metrics -- the decision tree routes from task type (binary, ordinal, pairwise, multi-label) to appropriate primary and secondary metrics
- **metrics.md** activates for rubric implementation code, including the evaluation runner class and production monitoring with alert thresholds

This layered structure means simple questions ("what evaluation approach should I use?") get answered from the core skill, while deep implementation questions ("show me the position swap protocol code") pull from the right reference automatically.

## Related Plugins

- **[Agent Project Development](../agent-project-development/)** -- Methodology for starting LLM projects: task-model fit, pipeline architecture, cost estimation
- **[BDI Mental States](../bdi-mental-states/)** -- Cognitive architecture for agents with formal belief-desire-intention modeling
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for background agents: sandboxes, registries, self-spawning
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for supervisor, swarm, and hierarchical multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
