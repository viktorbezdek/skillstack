# Agent Evaluation

> **v1.0.5** | Comprehensive evaluation framework for LLM agent systems -- multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, and continuous monitoring.
> 1 skill | 4 references | 15 trigger evals, 3 output evals

## The Problem

Evaluating LLM agents is nothing like testing traditional software. You cannot write a unit test that asserts a single correct answer because agents take different valid paths to reach the same goal. One agent searches three sources, another searches ten, and both produce correct results -- but a naive test that checks for specific steps flags one as failing. Teams that try to apply conventional testing frameworks to agents waste weeks building brittle harnesses that break every time the model takes a slightly different approach.

The consequences compound fast. Without proper evaluation, teams ship agents that score well on cherry-picked demos but fail on real user queries. Regressions sneak in because nobody measured the baseline. Prompt changes that improve one dimension (accuracy) silently degrade another (efficiency). And when someone finally notices quality has dropped, there is no data to pinpoint when or why it happened.

The worst outcome is invisible: teams that lack evaluation methodology never discover that their agents are mediocre. They optimize blindly -- changing prompts, swapping models, adding tools -- with no systematic way to know if anything actually improved. Every change is a coin flip dressed up as engineering.

## The Solution

This plugin provides a complete evaluation methodology purpose-built for LLM agent systems. It covers rubric design with multi-dimensional scoring, two distinct evaluation approaches (direct scoring for objective criteria, pairwise comparison for subjective preferences), systematic bias mitigation protocols, confidence calibration, and production pipeline architecture for continuous evaluation.

The skill teaches you to build evaluation systems that account for agent-specific challenges: non-determinism, multiple valid paths, composite quality dimensions, and context-dependent failures. It provides concrete prompt templates for both direct scoring and pairwise comparison, protocols for mitigating position bias and length bias, and frameworks for test set design stratified by complexity.

The result is an evaluation pipeline that runs automatically on agent changes, tracks quality metrics over time, catches regressions early, and gives you the data to make informed decisions about prompt engineering, model selection, and architecture changes.

## Context to Provide

The more specific you are about what you are evaluating, the more precise the rubrics, evaluation prompts, and pipeline architecture will be.

**What information to include in your prompt:**

- **Agent description**: What does your agent do? (e.g., "RAG agent that answers legal questions from a document corpus")
- **Task type**: What kind of task does it perform? (question answering, code generation, summarization, classification, creative writing)
- **Quality dimensions you care about**: Which aspects matter most? (accuracy, completeness, efficiency, citation correctness, tone, format compliance)
- **Evaluation context**: Are you comparing two configurations (A/B), tracking quality over time (regression testing), or doing a one-time audit?
- **Ground truth availability**: Do you have correct reference answers, or is evaluation preference-based with no single correct answer?
- **Scale**: How many test cases? How often will you run the evaluation? What is your latency and cost budget?
- **Known failure modes**: What specific problems have users or testers already reported?

**What makes results better:**
- Describing a real quality problem ("users say answers are too long and sometimes miss the point") produces actionable rubrics tuned to your failure mode
- Specifying exact dimensions (accuracy, relevance, conciseness) rather than asking for "quality" produces measurable rubrics with level descriptions
- Sharing a few example agent outputs, even just one good and one bad, anchors the rubric calibration
- Mentioning which models you are comparing (Claude Sonnet vs GPT-4o) enables bias mitigation configuration specific to your setup

**What makes results worse:**
- Asking to "test my agent" without describing what the agent does
- Requesting a single overall quality score (single scores hide dimension-specific failures)
- Omitting whether you have ground truth (determines whether to use direct scoring or pairwise comparison)

**Template prompt:**
```
I need to evaluate my [agent type] that [what it does]. The inputs are [describe input type] and the expected outputs are [describe what good looks like]. I care most about [list 2-4 dimensions]. I [do / do not] have verified correct answers to compare against. My evaluation goal is [catch regressions / compare two configurations / one-time quality audit]. Known problems: [describe user complaints or observed failures].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Cherry-picked demos masquerade as evaluation | Multi-dimensional rubrics score accuracy, completeness, efficiency, and process quality independently |
| Regressions go undetected for weeks | Continuous evaluation pipeline catches quality drops on every change |
| Prompt changes are coin flips -- no data on what improved or degraded | Before/after comparison with statistical confidence across stratified test sets |
| Single "it works" metric hides dimension-specific failures | Weighted multi-dimensional scores reveal that accuracy improved but efficiency dropped |
| Position bias in pairwise comparison corrupts A/B test results | Automatic position-swap protocol with consistency checks eliminates first-position preference |
| No baseline means no way to measure progress | Baseline metrics established before changes, tracked over time with trend analysis |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-evaluation@skillstack
```

### Verify installation

After installing, test with:

```
Help me build an evaluation framework for my customer support agent
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I need to evaluate whether my coding agent produces correct solutions -- help me design rubrics`
3. The skill walks you through multi-dimensional rubric design with scoring scales, level descriptions, and edge case guidance
4. Apply the rubrics by asking: `Now help me build an automated evaluation pipeline that runs these rubrics on every agent change`
5. Iterate by asking: `My evaluation shows position bias in pairwise comparisons -- how do I fix that?`

---

## System Overview

```
                        +---------------------------+
                        |     Agent Evaluation       |
                        |         Skill              |
                        +---------------------------+
                                    |
            +-----------+-----------+-----------+
            |           |           |           |
     +-----------+ +-----------+ +-----------+ +-----------+
     |  Rubric   | |  Direct   | | Pairwise  | |  Bias     |
     |  Design   | |  Scoring  | | Comparison| | Mitigation|
     +-----------+ +-----------+ +-----------+ +-----------+
            |           |           |           |
            +-----+-----+-----+-----+----------+
                  |           |
          +-------------+ +------------------+
          | Test Set     | | Production       |
          | Design       | | Pipeline         |
          +-------------+ +------------------+
```

The skill operates as a single comprehensive unit that covers the full evaluation lifecycle: designing rubrics, choosing and implementing evaluation approaches, mitigating systematic biases, building test sets, and running production evaluation pipelines.

## What's Inside

| Component | Type | Description |
|---|---|---|
| `agent-evaluation` | Skill | Core evaluation methodology covering rubrics, scoring, comparison, bias mitigation, and pipeline design |
| `bias-mitigation.md` | Reference | Techniques for mitigating position, length, self-enhancement, verbosity, and authority biases |
| `implementation-patterns.md` | Reference | Production-grade patterns for building LLM evaluation systems |
| `metrics-guide.md` | Reference | Guidance on selecting appropriate metrics for different evaluation scenarios |
| `metrics.md` | Reference | Core metric definitions and implementation details |

### Component Spotlights

#### agent-evaluation (skill)

**What it does:** Activates when you need to evaluate LLM agent performance, build evaluation frameworks, design rubrics, implement LLM-as-judge systems, or compare model outputs. Provides a structured methodology covering rubric design, two evaluation approaches (direct scoring and pairwise comparison), bias mitigation, test set design, and production pipeline architecture.

**Input -> Output:** A description of what you need to evaluate -> Multi-dimensional rubrics, evaluation prompts, bias mitigation protocols, test set structure, and pipeline architecture.

**When to use:**
- Building a new evaluation framework for an agent system
- Designing rubrics for scoring agent outputs
- Comparing two agent configurations or model versions
- Setting up continuous evaluation in a production pipeline
- Debugging inconsistent evaluation results

**When NOT to use:**
- Testing traditional software code -> use `testing-framework`
- Coordinating multiple agents -> use `multi-agent-patterns`
- Evaluating Claude Code plugin activation quality -> use `plugin-evaluation`

**Try these prompts:**

```
Help me design evaluation rubrics for my research agent that synthesizes information from multiple sources. The agent searches 3-5 documents per query and produces 200-400 word answers. Users complain that answers sometimes miss key details even when technically accurate. I need to measure accuracy, completeness, and citation quality.
```

```
I'm comparing GPT-4o vs Claude Sonnet for our customer support agent -- set up a pairwise comparison with bias mitigation. The agent handles billing and technical questions. I want to measure empathy, accuracy, and resolution rate. I suspect GPT-4o is winning because it's always in position A.
```

```
My evaluation pipeline shows inconsistent results between runs on the same test cases -- scores vary by 0.2 or more. The rubric says "assess answer quality" without level descriptions. Help me diagnose and fix the inconsistency.
```

```
Build me a test set for our coding agent that covers simple (single-function), medium (multi-file refactor), and complex (architectural) tasks with realistic token budgets. The agent uses Claude Sonnet. I want 30 cases for development.
```

```
I need to add continuous evaluation to our agent pipeline -- we deploy prompt changes weekly and regressions slip through. The agent classifies support tickets. I want to track accuracy, false positive rate, and latency. Alert me when any metric drops more than 5%.
```

**Key references:**

| Reference | Topic |
|---|---|
| `bias-mitigation.md` | Position bias, length bias, self-enhancement bias, verbosity bias -- specific mitigation techniques for each |
| `implementation-patterns.md` | Structured evaluation pipeline, hierarchical evaluation, Panel of LLMs (PoLL), human-in-the-loop patterns |
| `metrics-guide.md` | Metric selection by task type: binary, ordinal, pairwise, multi-label |
| `metrics.md` | Core metric definitions: F1, Cohen's kappa, Spearman's rho, agreement rates |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Test my agent" | "Help me design evaluation rubrics for my RAG agent that answers legal questions" |
| "Is my agent good?" | "Set up a pairwise comparison between our current and new prompt -- the agent summarizes financial reports" |
| "Use agent-evaluation to check quality" | "My agent evaluation shows 80% accuracy but users complain about incomplete answers -- help me add completeness and citation dimensions" |
| "Evaluate something" | "Build a production evaluation pipeline that runs on every commit and alerts when quality drops below 0.7" |

### Structured Prompt Templates

**For rubric design:**
```
Design a multi-dimensional evaluation rubric for [agent type] that scores [dimension 1], [dimension 2], and [dimension 3]. The agent handles [task description] and needs to be [strict/balanced/lenient] because [reason].
```

**For A/B comparison:**
```
I'm comparing [config A] vs [config B] for [agent purpose]. Set up a pairwise evaluation with position bias mitigation. The key criteria are [list criteria]. Show me the prompt templates and the consistency check protocol.
```

**For pipeline setup:**
```
Build an automated evaluation pipeline for [agent name]. It should run [frequency], track [metrics], and alert when [threshold condition]. We have [N] test cases stratified by [complexity levels].
```

### Prompt Anti-Patterns

- **Asking for a single score**: "Rate my agent 1-10" -- agents have multiple quality dimensions. A single score hides that accuracy is great but efficiency is terrible. Always use multi-dimensional rubrics.
- **Skipping rubric design**: "Just compare the two outputs and tell me which is better" -- without explicit criteria and level descriptions, the evaluator's judgment is uncalibrated and unreproducible. Define rubrics first.
- **Evaluating specific execution steps**: "Check that my agent called the search tool exactly twice" -- agents take different valid paths. Evaluate outcomes, not specific steps.

## Real-World Walkthrough

**Starting situation:** You run a customer support agent that answers questions about your SaaS product. Users have been complaining that answers are sometimes wrong, often too long, and occasionally miss the point entirely. You have no evaluation system -- quality feedback comes from sporadic user complaints.

**Step 1: Rubric design.** You start by asking: "Help me design evaluation rubrics for a customer support agent that answers product questions. I need to measure factual accuracy, answer relevance, conciseness, and tone appropriateness."

The skill produces a four-dimension rubric with 1-5 scoring scales for each. Factual accuracy gets the highest weight (0.4) because wrong answers erode trust. Each level has descriptive characteristics -- for example, a score of 3 on conciseness means "answer addresses the question but includes some unnecessary detail or preamble." Edge cases are documented: when the question is ambiguous, accuracy should be scored based on whether the agent asked for clarification rather than guessing.

**Step 2: Test set construction.** Next you ask: "Build me a test set from our real support tickets -- I have 500 historical tickets with verified correct answers." The skill guides you to stratify by complexity: 10 simple tickets (single-fact lookups), 10 medium tickets (require combining information from multiple docs), 5 complex tickets (ambiguous questions or multi-step procedures), and 5 edge cases (questions about features that don't exist, unclear product versions). Starting with 30 cases is sufficient for development -- you add more later.

**Step 3: Direct scoring implementation.** You ask: "Implement direct scoring for the accuracy and relevance dimensions -- these have objective ground truth." The skill provides prompt templates that require chain-of-thought justification before each score, structured JSON output, and specific instructions to find evidence in the response before scoring. Research shows this improves reliability by 15-25% compared to score-first approaches.

**Step 4: Pairwise comparison for subjective dimensions.** For conciseness and tone, you ask: "Set up pairwise comparison with bias mitigation for the subjective dimensions." The skill implements a position-swap protocol: each pair of responses is evaluated twice with positions swapped. If both passes agree, confidence is the average. If they disagree, the result is a TIE with 0.5 confidence. This eliminates the systematic first-position preference that LLM judges exhibit.

**Step 5: Baseline measurement.** You run the evaluation on your current agent and discover: accuracy 0.78, relevance 0.82, conciseness 0.61, tone 0.73. The low conciseness score confirms user complaints about verbose answers. Now you have a baseline.

**Step 6: Continuous pipeline.** Finally you ask: "Set up this evaluation to run on every prompt change with alerting." The skill designs a pipeline that runs the 30-case test set on every commit to the prompt repository, tracks all four dimensions over time, and alerts when any dimension drops more than 0.05 from the rolling average. After three months, you expand the test set to 100 cases and add a human review loop for low-confidence evaluations.

**Gotchas discovered:** The initial rubric for "tone" was too vague -- "appropriate tone" means different things for billing complaints versus feature questions. The skill recommended splitting it into "empathy" and "professionalism" as separate dimensions with domain-specific rubrics. Also, test cases from three months ago referenced a deprecated feature, producing false accuracy failures -- the skill recommended a quarterly test set review cadence.

## Usage Scenarios

### Scenario 1: Evaluating a RAG pipeline after retrieval changes

**Context:** You changed the retrieval strategy in your RAG agent from keyword search to hybrid search. You need to know if answer quality improved without regressing on any dimension.

**You say:** "I changed my RAG retrieval from BM25 to hybrid BM25+vector. Help me evaluate whether answer quality improved. I care about factual accuracy, citation correctness, and completeness."

**The skill provides:**
- Three-dimension rubric with weighted scoring
- Test set design stratified by query complexity
- Before/after comparison framework with statistical significance
- Confidence intervals for each dimension score

**You end up with:** A structured comparison showing that accuracy improved from 0.81 to 0.87, citation correctness improved from 0.72 to 0.85, but completeness dropped slightly from 0.79 to 0.76 because the new retriever sometimes returns fewer but more relevant documents.

### Scenario 2: Building quality gates for an agent deployment pipeline

**Context:** Your team deploys agent updates weekly and occasionally ships regressions. You need automated quality gates that block deploys when quality drops.

**You say:** "Set up quality gates for our weekly agent deploy. Block the deploy if any quality dimension drops below threshold."

**The skill provides:**
- Per-dimension pass/fail thresholds calibrated to your use case
- Pipeline architecture with fast screening (cheap model) and edge case review (expensive model)
- Alert routing for different failure modes (regression vs. flaky test)
- Dashboard metrics for trend analysis

**You end up with:** A CI pipeline stage that runs evaluation on every release candidate and blocks deployment if accuracy drops below 0.75 or any other dimension drops below 0.65.

### Scenario 3: Mitigating bias in model comparison

**Context:** You are comparing Claude Sonnet vs GPT-4o for your coding agent. Initial results show GPT-4o winning 70% of comparisons, but you suspect position bias.

**You say:** "My A/B comparison might be biased -- GPT-4o is always in position A. How do I check and fix this?"

**The skill provides:**
- Position-swap protocol implementation
- Consistency analysis between first-pass and second-pass results
- Length normalization to control for verbosity bias
- Confidence calibration based on inter-pass agreement

**You end up with:** After position swapping, the real winner ratio is 55/45 in favor of GPT-4o (not 70/30), with 20% of comparisons being genuine ties that were artificially broken by position bias.

### Scenario 4: Designing rubrics for a creative writing agent

**Context:** You built an agent that generates marketing copy and need to evaluate quality, but "good copy" is subjective and there is no single correct answer.

**You say:** "Help me evaluate my marketing copy agent. There's no ground truth -- I need to assess creativity, brand voice alignment, and persuasiveness."

**The skill provides:**
- Pairwise comparison setup (not direct scoring) because the criteria are subjective
- Domain-specific rubrics with concrete examples for each score level
- Human evaluation protocol to validate automated judgments
- Correlation analysis between automated and human scores

**You end up with:** An evaluation system where pairwise comparison achieves 78% agreement with human raters, validated quarterly with a 50-case human evaluation sample.

---

## Decision Logic

**When does direct scoring activate vs pairwise comparison?**

The skill uses a clear decision tree: if there is an objective ground truth (factual accuracy, format compliance, instruction following), use direct scoring. If the evaluation is preference-based (tone, style, creativity, persuasiveness), use pairwise comparison. If you are comparing summaries against a source document, consider reference-based evaluation. When in doubt, the skill asks about your criteria to route correctly.

**What happens when evaluation results are inconsistent?**

The skill diagnoses inconsistency through several checks: position consistency in pairwise comparisons (disagree = TIE), confidence calibration (low evidence = low confidence), and rubric ambiguity analysis (vague level descriptions cause inter-rater disagreement). Recovery involves tightening rubric definitions, adding edge case guidance, and increasing the evaluation panel size.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Position bias corrupting pairwise results | One position wins disproportionately regardless of content | Implement position-swap protocol with consistency check; inconsistent pairs become TIEs |
| Rubric too vague | High variance between evaluation runs on the same response | Add concrete level descriptions with observable characteristics and edge case guidance; reduce scoring variance by 40-60% |
| Test set not representative | High eval scores but poor user satisfaction | Stratify test set by complexity; add cases from real user failures; review quarterly |
| Evaluator model rating its own outputs higher | Self-generated responses score 0.2+ higher than competitors | Use a different model for evaluation than for generation; document this limitation |
| Single-metric obsession | Optimizing accuracy while completeness and efficiency degrade silently | Use multi-dimensional rubrics with per-dimension thresholds and alerting |

## Ideal For

- **ML engineers building agent systems** who need to measure and improve quality systematically rather than relying on spot-checks and user complaints
- **Teams comparing model providers** (Claude vs GPT vs Gemini) who need unbiased A/B evaluation with statistical rigor rather than subjective impressions
- **Platform engineers setting up quality gates** who need automated evaluation pipelines that block bad deploys and catch regressions before users do
- **Research teams running experiments** who need reproducible evaluation methodology with tracked baselines, confidence intervals, and bias mitigation

## Not For

- **Testing traditional software** -- code that has deterministic correct outputs needs unit tests and integration tests, not LLM-as-judge. Use `testing-framework`.
- **Coordinating multiple agents** -- if your problem is agent handoffs, task routing, or multi-agent orchestration, evaluation is a cross-cutting concern but not the primary tool. Use `multi-agent-patterns`.
- **Evaluating Claude Code plugin activation** -- whether a skill triggers on the right queries is a different evaluation problem with its own methodology. Use `plugin-evaluation`.

## Related Plugins

- **agent-project-development** -- Design the agent pipeline that this plugin evaluates
- **multi-agent-patterns** -- Evaluate coordination quality across multi-agent systems
- **prompt-engineering** -- Improve the prompts that evaluation identifies as underperforming
- **context-optimization** -- Measure and improve context efficiency that evaluation reveals as wasteful
- **testing-framework** -- Complement agent evaluation with traditional software testing for deterministic components

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
