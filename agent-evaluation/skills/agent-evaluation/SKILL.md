---
name: agent-evaluation
description: This skill should be used when the user asks to "evaluate agent performance", "build test framework", "measure agent quality", "create evaluation rubrics", "implement LLM-as-judge", "compare model outputs", "mitigate evaluation bias", or mentions multi-dimensional evaluation, agent testing, quality gates, direct scoring, pairwise comparison, position bias, evaluation pipelines, or automated quality assessment for LLM agent systems. NOT for testing code or applications (use testing-framework), NOT for agent coordination or multi-agent design (use multi-agent-patterns).
---

# Evaluating LLM Agent Systems

Agent evaluation requires fundamentally different approaches than traditional software testing. Agents make dynamic decisions, are non-deterministic, and often lack single correct answers. Effective evaluation must account for these characteristics while providing actionable feedback.

**Key insight**: LLM-as-a-Judge is not a single technique but a family of approaches, each suited to different evaluation contexts. Choosing the right approach and mitigating known biases is the core competency this skill develops.

## When to Activate

- Testing agent performance systematically
- Validating context engineering choices
- Measuring improvements or catching regressions over time
- Building quality gates for agent pipelines
- Comparing different agent configurations or model outputs
- Building automated evaluation pipelines for LLM outputs
- Designing A/B tests for prompt or model changes
- Debugging evaluation systems that show inconsistent results
- Analyzing correlation between automated and human judgments

## Decision Tree: Choosing an Evaluation Approach

```
What are you evaluating?
+-- Agent outputs against known correct answers?
|   +-- Yes --> Direct Scoring (factual accuracy, format compliance, instruction following)
|   +-- No --> Are you comparing two configurations?
|       +-- Yes --> Pairwise Comparison with position-swap protocol
|       |   Criteria: tone, style, persuasiveness, creativity
|       +-- No --> Do you have reference material?
|           +-- Yes --> Reference-based evaluation (summarization, translation)
|           +-- No --> Build rubrics first, then choose approach per dimension
```

## Fundamentals

### Why Agent Evaluation Is Different

**Non-Determinism and Multiple Valid Paths**: Agents may take different valid paths to reach goals. One agent searches three sources while another searches ten. Evaluate outcomes, not specific steps.

**Context-Dependent Failures**: Agent failures often depend on context in subtle ways. An agent might succeed on simple queries but fail on complex ones. Evaluation must cover a range of complexity levels.

**Composite Quality Dimensions**: Agent quality spans factual accuracy, completeness, coherence, tool efficiency, and process quality. Single-metric evaluation hides dimension-specific failures.

### Performance Drivers: The 95% Finding

Research on the BrowseComp evaluation found that three factors explain 95% of performance variance:

| Factor | Variance Explained | Implication |
|--------|-------------------|-------------|
| Token usage | 80% | More tokens = better performance |
| Number of tool calls | ~10% | More exploration helps |
| Model choice | ~5% | Better models multiply efficiency |

Implications: Evaluate agents with realistic token budgets, not unlimited resources. Model upgrades beat token increases. Multi-agent architectures get validated by distributing work across separate context windows.

### The Evaluation Taxonomy

**Direct Scoring**: A single LLM rates one response on a defined scale.
- Best for: Objective criteria (factual accuracy, instruction following, toxicity)
- Failure mode: Score calibration drift, inconsistent scale interpretation

**Pairwise Comparison**: An LLM compares two responses and selects the better one.
- Best for: Subjective preferences (tone, style, persuasiveness)
- Failure mode: Position bias, length bias

Research (Zheng et al., 2023) establishes that pairwise comparison achieves higher agreement with human judges than direct scoring for preference-based evaluation, while direct scoring remains appropriate for objective criteria.

**End-State Evaluation**: For agents that mutate persistent state, evaluate whether the final state matches expectations rather than how the agent got there.

### Metric Selection Framework

| Task Type | Primary Metrics | Secondary Metrics |
|-----------|-----------------|-------------------|
| Binary classification (pass/fail) | Recall, Precision, F1 | Cohen's kappa |
| Ordinal scale (1-5 rating) | Spearman's rho, Kendall's tau | Cohen's kappa (weighted) |
| Pairwise preference | Agreement rate, Position consistency | Confidence calibration |
| Multi-label | Macro-F1, Micro-F1 | Per-label precision/recall |

Critical insight: High absolute agreement matters less than systematic disagreement patterns.

## Rubric Design

### Multi-Dimensional Rubric

Effective rubrics cover key dimensions with descriptive levels. Well-defined rubrics reduce evaluation variance by 40-60% compared to open-ended scoring.

**Rubric Components**:
1. **Level descriptions**: Clear boundaries for each score level
2. **Characteristics**: Observable features that define each level
3. **Examples**: Representative text for each level (optional but valuable)
4. **Edge cases**: Guidance for ambiguous situations
5. **Scoring guidelines**: General principles for consistent application

### Scale Calibration

- **1-3 scales**: Binary with neutral option, lowest cognitive load
- **1-5 scales**: Standard Likert, good balance of granularity and reliability
- **1-10 scales**: High granularity but harder to calibrate, use only with detailed rubrics

### Strictness Calibration

- **Lenient**: Lower bar, appropriate for encouraging iteration
- **Balanced**: Typical expectations for production use
- **Strict**: High standards, appropriate for safety-critical evaluation

### Domain Adaptation

Rubrics should use domain-specific terminology. A "code readability" rubric mentions variables, functions, and comments. A "medical accuracy" rubric references clinical terminology. Generic rubrics produce generic evaluations.

## The Bias Landscape

LLM judges exhibit systematic biases that must be actively mitigated:

| Bias | Symptom | Mitigation |
|------|---------|------------|
| **Position Bias** | First-position responses win disproportionately | Evaluate twice with swapped positions; inconsistent pairs become TIEs |
| **Length Bias** | Longer responses rated higher regardless of quality | Explicit prompting to ignore length; length-normalized scoring |
| **Self-Enhancement** | Models rate their own outputs higher | Use different model for generation and evaluation |
| **Verbosity Bias** | Detailed explanations scored higher even when unnecessary | Criteria-specific rubrics that penalize irrelevant detail |
| **Authority Bias** | Confident, authoritative tone rated higher regardless of accuracy | Require evidence citation; fact-checking layer |

## Evaluation Approaches in Detail

### Direct Scoring Implementation

**Prompt Structure for Direct Scoring**:
```
You are an expert evaluator assessing response quality.

## Task
Evaluate the following response against each criterion.

## Original Prompt
{prompt}

## Response to Evaluate
{response}

## Criteria
{for each criterion: name, description, weight}

## Instructions
For each criterion:
1. Find specific evidence in the response
2. Score according to the rubric (1-{max} scale)
3. Justify your score with evidence
4. Suggest one specific improvement

## Output Format
Respond with structured JSON containing scores, justifications, and summary.
```

**Chain-of-Thought Requirement**: All scoring prompts must require justification before the score. This improves reliability by 15-25% compared to score-first approaches.

### Pairwise Comparison Implementation

**Position Bias Mitigation Protocol**:
1. First pass: Response A in first position, Response B in second
2. Second pass: Response B in first position, Response A in second
3. Consistency check: If passes disagree, return TIE with reduced confidence
4. Final verdict: Consistent winner with averaged confidence

**Prompt Structure for Pairwise Comparison**:
```
You are an expert evaluator comparing two AI responses.

## Critical Instructions
- Do NOT prefer responses because they are longer
- Do NOT prefer responses based on position (first vs second)
- Focus ONLY on quality according to the specified criteria
- Ties are acceptable when responses are genuinely equivalent

## Original Prompt
{prompt}

## Response A
{response_a}

## Response B
{response_b}

## Comparison Criteria
{criteria list}

## Instructions
1. Analyze each response independently first
2. Compare them on each criterion
3. Determine overall winner with confidence level

## Output Format
JSON with per-criterion comparison, overall winner, confidence (0-1), and reasoning.
```

**Confidence Calibration**: Both passes agree = average confidences. Passes disagree = 0.5 confidence, verdict = TIE.

### Human Evaluation

Human evaluation catches what automation misses: hallucinated answers on unusual queries, system failures, and subtle biases. Use human evaluation to validate and calibrate automated systems.

## Test Set Design

### Sample Selection

Start with small samples during development. Early in agent development, changes have dramatic impacts because there is abundant low-hanging fruit. Sample from real usage patterns. Add known edge cases. Ensure coverage across complexity levels.

### Complexity Stratification

| Level | Description | Tool Calls | Example |
|-------|-------------|------------|---------|
| Simple | Single fact lookup | 1 | "What is the capital of France?" |
| Medium | Multiple sources, comparison | 2-5 | "Compare Apple and Microsoft revenue" |
| Complex | Aggregation, analysis, reasoning | 5-10 | "Analyze Q1-Q4 sales trends and summarize" |
| Very Complex | Extended interaction, synthesis | 10+ | "Research emerging AI tech and recommend strategy" |

## Production Pipeline Design

### Evaluation Pipeline Architecture

```
Input: Response + Prompt + Context
         |
         v
+---------------------+
|   Criteria Loader   | <-- Rubrics, weights
+----------+----------+
           |
           v
+---------------------+
|   Primary Scorer    | <-- Direct or Pairwise
+----------+----------+
           |
           v
+---------------------+
|   Bias Mitigation   | <-- Position swap, etc.
+----------+----------+
           |
           v
+---------------------+
| Confidence Scoring  | <-- Calibration
+----------+----------+
           |
           v
Output: Scores + Justifications + Confidence
```

### Scaling Evaluation

| Strategy | How | Best For |
|----------|-----|----------|
| **Panel of LLMs (PoLL)** | Multiple models as judges, aggregate votes | High-stakes decisions, reducing individual model bias |
| **Hierarchical evaluation** | Fast cheap model screens, expensive model reviews edge cases | Cost-effective large volumes |
| **Human-in-the-loop** | Automated for clear cases, human review for low-confidence | Critical applications, best reliability |

### Continuous Evaluation

Build pipelines that run automatically on agent changes. Track results over time. Compare versions to identify regressions. Sample production interactions randomly. Set alerts for quality drops.

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Scoring without justification | Scores lack grounding; difficult to debug | Always require evidence-based justification before score |
| Single-pass pairwise comparison | Position bias corrupts results | Always swap positions and check consistency |
| Overloaded criteria | Criteria measuring multiple things are unreliable | One criterion = one measurable aspect |
| Missing edge case guidance | Evaluators handle ambiguous cases inconsistently | Include edge cases in rubrics with explicit guidance |
| Ignoring confidence calibration | High-confidence wrong judgments are worse than low-confidence | Calibrate confidence to position consistency and evidence strength |
| Overfitting to specific paths | Evaluating exact steps rather than outcome | Evaluate outcomes, not execution paths |
| Single-metric obsession | Optimizing one number while other dimensions degrade | Use multi-dimensional rubrics |
| Neglecting context effects | Tests pass in isolation but fail with realistic context | Test with realistic context sizes and histories |
| Skipping human evaluation | Automated evaluation misses subtle issues | Supplement LLM evaluation with human review |
| Same model for generation and evaluation | Self-enhancement bias inflates scores | Use different models for generation and evaluation |

## Examples

### Example 1: Direct Scoring Output

**Input**: Prompt: "What causes seasons on Earth?" Response correctly identifies axial tilt. Criterion: Factual Accuracy. Scale: 1-5.

```json
{
  "criterion": "Factual Accuracy",
  "score": 5,
  "evidence": ["Correctly identifies axial tilt as primary cause", "Correctly explains differential sunlight by hemisphere"],
  "justification": "Response accurately explains the cause of seasons with correct scientific reasoning.",
  "improvement": "Could add the specific tilt angle (23.5 degrees) for completeness."
}
```

### Example 2: Pairwise Comparison with Position Swap

First pass (A first): `{ "winner": "B", "confidence": 0.8 }`
Second pass (B first): `{ "winner": "A", "confidence": 0.6 }` → Mapped: `{ "winner": "B", "confidence": 0.6 }`

Final: `{ "winner": "B", "confidence": 0.7, "positionConsistency": { "consistent": true } }`

If passes disagree → `{ "winner": "TIE", "confidence": 0.5 }`

## Guidelines

1. Use multi-dimensional rubrics, not single metrics
2. Evaluate outcomes, not specific execution paths
3. Always require justification before scores (15-25% reliability improvement)
4. Always swap positions in pairwise comparison
5. Match scale granularity to rubric specificity
6. Separate objective criteria (direct scoring) from subjective (pairwise)
7. Include confidence scores calibrated to position consistency
8. Define edge cases explicitly in rubrics
9. Use domain-specific rubric terminology
10. Cover complexity levels from simple to very complex
11. Test with realistic context sizes
12. Run evaluations continuously, not just before release
13. Supplement LLM evaluation with human review
14. Validate against human judgments
15. Monitor for systematic bias by criterion, response type, and model

## Building an Evaluation Framework: Step by Step

1. Define quality dimensions relevant to your use case
2. Create rubrics with clear level descriptions and edge cases
3. Choose evaluation approach per dimension (direct vs. pairwise)
4. Build test sets from real usage, stratified by complexity
5. Implement automated evaluation pipelines with bias mitigation
6. Establish baseline metrics before making changes
7. Run evaluations on all significant changes
8. Track metrics over time for trend analysis
9. Supplement with human review
10. Feed disagreements back to improve rubrics

## Integration

- **context-fundamentals** - Evaluating context usage; evaluation prompts require effective context structure
- **context-degradation** - Detecting and measuring degradation effects
- **context-optimization** - Measuring optimization effectiveness
- **multi-agent-patterns** - Evaluating coordination across agents
- **tool-design** - Evaluating tool effectiveness

## References

External research:
- [Eugene Yan: Evaluating the Effectiveness of LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/)
- [Judging LLM-as-a-Judge (Zheng et al., 2023)](https://arxiv.org/abs/2306.05685)
- [G-Eval: NLG Evaluation using GPT-4 (Liu et al., 2023)](https://arxiv.org/abs/2303.16634)
- [Large Language Models are not Fair Evaluators (Wang et al., 2023)](https://arxiv.org/abs/2305.17926)

---

## Skill Metadata

**Created**: 2024-12-20
**Last Updated**: 2026-04-18
**Authors**: Agent Skills for Context Engineering Contributors, Muratcan Koylan
**Version**: 2.1.0
