# Agent Evaluation

> **v1.0.4** | Agent Architecture | 5 iterations

Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, direct scoring, confidence calibration, and continuous monitoring.

## What Problem Does This Solve

Agent systems are non-deterministic -- they can take multiple valid paths to the same goal and produce outputs where no single "correct" answer exists. Traditional unit tests cannot measure whether a prompt change made an agent better or worse, whether evaluation scores correlate with human judgment, or whether a specific quality dimension (accuracy, completeness, efficiency) is regressing over time. Teams iterating on prompts, context strategies, or model versions need systematic evaluation that catches regressions, validates improvements, and produces results humans can trust.

This skill provides the rubric designs, bias mitigation protocols, scoring approaches, test set strategies, and production pipeline patterns to build evaluation systems that actually correlate with human judgment -- not just produce numbers.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-evaluation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention evaluation-related topics, or you can invoke it explicitly with `Use the agent-evaluation skill to ...`.

## What's Inside

This is a single-skill plugin with four reference documents:

| Component | What It Covers |
|---|---|
| **SKILL.md** | Foundational concepts (why agent eval differs from testing, the 95% performance variance finding), rubric design (multi-dimensional scoring, scale calibration, strictness levels), the bias landscape (position, length, self-enhancement, verbosity, authority), evaluation approaches (direct scoring prompts, pairwise comparison with position swap), test set design (complexity stratification, context degradation testing), production pipeline architecture, and 18 actionable guidelines |
| **references/bias-mitigation.md** | Implementation code for position swap protocol, multi-shuffle comparison, length-normalized scoring, cross-model evaluation, blind evaluation, relevance-weighted scoring, fact-checking layer, and aggregate bias monitoring with z-score detection |
| **references/implementation-patterns.md** | Five production patterns: structured evaluation pipeline (input validation through output formatting), hierarchical evaluation (cheap screening then expensive model), Panel of LLM Judges (PoLL), confidence calibration, and structured output formatting with error handling and retry logic |
| **references/metrics-guide.md** | Metric selection guide covering classification metrics (precision, recall, F1), agreement metrics (Cohen's kappa, weighted kappa), correlation metrics (Spearman's rho, Kendall's tau, Pearson's r), pairwise comparison metrics, and a decision tree for choosing the right metric by task type |
| **references/metrics.md** | Rubric implementation code with five evaluation dimensions (factual accuracy, completeness, citation accuracy, source quality, tool efficiency), weighted scoring calculations, test set management class, evaluation runner class, and production monitoring with alert thresholds |

## Usage Scenarios

**1. "My prompt change looks good subjectively, but I need data."**
Start with the evaluation taxonomy to pick the right approach: direct scoring for objective criteria like factual accuracy, pairwise comparison for subjective qualities like tone. Use the test set design patterns to build a representative sample stratified by complexity (simple single-tool-call through complex multi-step reasoning). Run both versions through the pipeline and compare weighted scores.

**2. "Our LLM judge scores don't match what human reviewers think."**
Use the metrics guide to calculate Spearman's rho between automated and human scores -- anything below 0.6 indicates a calibration problem. Check the bias landscape: if longer responses consistently score higher, apply the length-normalized scoring pattern. If position matters in pairwise comparison, implement the position swap protocol. Use the aggregate bias monitor to detect systematic issues.

**3. "We need to add evaluation to our agent's CI pipeline."**
Follow the production pipeline architecture: criteria loader, primary scorer, bias mitigation layer, confidence scoring, then structured output. Use the hierarchical evaluation pattern for cost efficiency -- cheap model screens obvious cases, expensive model handles borderline items. Set quality gate thresholds based on weighted dimension scores and alert on drops below baseline.

**4. "I want to evaluate accuracy, completeness, and efficiency as separate dimensions."**
Use the multi-dimensional rubric with the five built-in dimensions (or customize). Each dimension has five levels from "failed" (0.0) to "excellent" (1.0) with explicit characteristics at each level. Apply domain-specific language in your rubric descriptions -- a "code readability" rubric should mention variables and function names, not generic quality terms. The weighted scoring formula combines dimensions based on what matters most for your use case.

**5. "I need to compare two models (or two prompt versions) head-to-head."**
Use pairwise comparison with the position swap protocol: run comparison twice with responses swapped, check for consistency. If both passes agree, average the confidence scores. If they disagree, the result is a tie with 0.5 confidence -- position bias was a factor. For higher stakes, use the multi-shuffle variant with majority vote across 3+ orderings.

## When to Use / When NOT to Use

**Use when:**
- Measuring whether a prompt, context strategy, or model change improved agent quality
- Building automated evaluation pipelines with quality gates
- Designing rubrics for human or LLM-as-judge evaluation
- Debugging evaluation systems that produce inconsistent or biased results
- Comparing model outputs across multiple quality dimensions

**Do NOT use when:**
- Testing code or applications -- use [testing-framework](../testing-framework/) instead
- Coordinating multiple agents or designing handoff patterns -- use [multi-agent-patterns](../multi-agent-patterns/) instead
- Building the agent itself -- use [agent-project-development](../agent-project-development/) instead

## Related Plugins

- **[Agent Project Development](../agent-project-development/)** -- Methodology for starting LLM projects: task-model fit, pipeline architecture, cost estimation
- **[BDI Mental States](../bdi-mental-states/)** -- Cognitive architecture for agents with formal belief-desire-intention modeling
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for background agents: sandboxes, registries, self-spawning
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep/Graphiti, Letta, Cognee, LangMem
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Architecture patterns for supervisor, swarm, and hierarchical multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
