---
name: agent-evaluation
description: This skill should be used when the user asks to "evaluate agent performance", "build test framework", "measure agent quality", "create evaluation rubrics", "implement LLM-as-judge", "compare model outputs", "mitigate evaluation bias", or mentions multi-dimensional evaluation, agent testing, quality gates, direct scoring, pairwise comparison, position bias, evaluation pipelines, or automated quality assessment for LLM agent systems.
---

# Evaluating LLM Agent Systems

Evaluation of agent systems requires fundamentally different approaches than traditional software testing or standard language model benchmarking. Agents make dynamic decisions, are non-deterministic between runs, and often lack single correct answers. Effective evaluation must account for these characteristics while providing actionable feedback.

This skill is the definitive resource for agent evaluation. It covers foundational concepts (rubric design, test sets, outcome-focused assessment), advanced techniques (LLM-as-judge, pairwise comparison, bias mitigation), and production-grade pipeline design. A robust evaluation framework enables continuous improvement, catches regressions, and validates that context engineering choices achieve intended effects.

**Key insight**: LLM-as-a-Judge is not a single technique but a family of approaches, each suited to different evaluation contexts. Choosing the right approach and mitigating known biases is the core competency this skill develops.

## When to Activate

Activate this skill when:

- Testing agent performance systematically
- Validating context engineering choices
- Measuring improvements or catching regressions over time
- Building quality gates for agent pipelines
- Comparing different agent configurations or model outputs
- Building automated evaluation pipelines for LLM outputs
- Designing A/B tests for prompt or model changes
- Creating rubrics for human or automated evaluation
- Debugging evaluation systems that show inconsistent results
- Analyzing correlation between automated and human judgments
- Evaluating production systems continuously

## Fundamentals

### Why Agent Evaluation Is Different

**Non-Determinism and Multiple Valid Paths**
Agents may take completely different valid paths to reach goals. One agent might search three sources while another searches ten. They might use different tools to find the same answer. Traditional evaluations that check for specific steps fail in this context. The solution is outcome-focused evaluation that judges whether agents achieve right outcomes while following reasonable processes.

**Context-Dependent Failures**
Agent failures often depend on context in subtle ways. An agent might succeed on simple queries but fail on complex ones. It might work well with one tool set but fail with another. Failures may emerge only after extended interaction when context accumulates. Evaluation must cover a range of complexity levels and test extended interactions, not just isolated queries.

**Composite Quality Dimensions**
Agent quality is not a single dimension. It includes factual accuracy, completeness, coherence, tool efficiency, and process quality. An agent might score high on accuracy but low in efficiency, or vice versa. Evaluation rubrics must capture multiple dimensions with appropriate weighting for the use case.

### Performance Drivers: The 95% Finding

Research on the BrowseComp evaluation (which tests browsing agents' ability to locate hard-to-find information) found that three factors explain 95% of performance variance:

| Factor | Variance Explained | Implication |
|--------|-------------------|-------------|
| Token usage | 80% | More tokens = better performance |
| Number of tool calls | ~10% | More exploration helps |
| Model choice | ~5% | Better models multiply efficiency |

This finding has significant implications for evaluation design:
- **Token budgets matter**: Evaluate agents with realistic token budgets, not unlimited resources
- **Model upgrades beat token increases**: Upgrading model generations provides larger gains than doubling token budgets on previous versions
- **Multi-agent validation**: The finding validates architectures that distribute work across agents with separate context windows

### The Evaluation Taxonomy

Evaluation approaches fall into two primary categories with distinct reliability profiles:

**Direct Scoring**: A single LLM rates one response on a defined scale.
- Best for: Objective criteria (factual accuracy, instruction following, toxicity)
- Reliability: Moderate to high for well-defined criteria
- Failure mode: Score calibration drift, inconsistent scale interpretation

**Pairwise Comparison**: An LLM compares two responses and selects the better one.
- Best for: Subjective preferences (tone, style, persuasiveness)
- Reliability: Higher than direct scoring for preferences
- Failure mode: Position bias, length bias

Research from the MT-Bench paper (Zheng et al., 2023) establishes that pairwise comparison achieves higher agreement with human judges than direct scoring for preference-based evaluation, while direct scoring remains appropriate for objective criteria with clear ground truth.

**End-State Evaluation**: For agents that mutate persistent state, end-state evaluation focuses on whether the final state matches expectations rather than how the agent got there.

### Decision Framework: Direct vs. Pairwise

```
Is there an objective ground truth?
+-- Yes --> Direct Scoring
|   Examples: factual accuracy, instruction following, format compliance
|
+-- No --> Is it a preference or quality judgment?
    +-- Yes --> Pairwise Comparison
    |   Examples: tone, style, persuasiveness, creativity
    |
    +-- No --> Consider reference-based evaluation
        Examples: summarization (compare to source), translation (compare to reference)
```

### Metric Selection Framework

Choose metrics based on the evaluation task structure:

| Task Type | Primary Metrics | Secondary Metrics |
|-----------|-----------------|-------------------|
| Binary classification (pass/fail) | Recall, Precision, F1 | Cohen's kappa |
| Ordinal scale (1-5 rating) | Spearman's rho, Kendall's tau | Cohen's kappa (weighted) |
| Pairwise preference | Agreement rate, Position consistency | Confidence calibration |
| Multi-label | Macro-F1, Micro-F1 | Per-label precision/recall |

The critical insight: High absolute agreement matters less than systematic disagreement patterns. A judge that consistently disagrees with humans on specific criteria is more problematic than one with random noise.

## Rubric Design

### Multi-Dimensional Rubric

Effective rubrics cover key dimensions with descriptive levels:

- **Factual accuracy**: Claims match ground truth (excellent to failed)
- **Completeness**: Output covers requested aspects (excellent to failed)
- **Citation accuracy**: Citations match claimed sources (excellent to failed)
- **Source quality**: Uses appropriate primary sources (excellent to failed)
- **Tool efficiency**: Uses right tools reasonable number of times (excellent to failed)

Convert dimension assessments to numeric scores (0.0 to 1.0) with appropriate weighting. Calculate weighted overall scores. Determine passing threshold based on use case requirements.

### Rubric Components

Well-defined rubrics reduce evaluation variance by 40-60% compared to open-ended scoring.

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

- **Lenient**: Lower bar for passing scores, appropriate for encouraging iteration
- **Balanced**: Fair, typical expectations for production use
- **Strict**: High standards, appropriate for safety-critical or high-stakes evaluation

### Domain Adaptation

Rubrics should use domain-specific terminology. A "code readability" rubric mentions variables, functions, and comments. A "medical accuracy" rubric references clinical terminology and evidence standards. Generic rubrics produce generic (less useful) evaluations.

## The Bias Landscape

LLM judges exhibit systematic biases that must be actively mitigated:

**Position Bias**: First-position responses receive preferential treatment in pairwise comparison. Mitigation: Evaluate twice with swapped positions, use majority vote or consistency check.

**Length Bias**: Longer responses are rated higher regardless of quality. Mitigation: Explicit prompting to ignore length, length-normalized scoring.

**Self-Enhancement Bias**: Models rate their own outputs higher. Mitigation: Use different models for generation and evaluation, or acknowledge limitation.

**Verbosity Bias**: Detailed explanations receive higher scores even when unnecessary. Mitigation: Criteria-specific rubrics that penalize irrelevant detail.

**Authority Bias**: Confident, authoritative tone rated higher regardless of accuracy. Mitigation: Require evidence citation, fact-checking layer.

## Evaluation Approaches in Detail

### Direct Scoring Implementation

Direct scoring requires three components: clear criteria, a calibrated scale, and structured output format.

**Criteria Definition Pattern**:
```
Criterion: [Name]
Description: [What this criterion measures]
Weight: [Relative importance, 0-1]
```

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

**Chain-of-Thought Requirement**: All scoring prompts must require justification before the score. Research shows this improves reliability by 15-25% compared to score-first approaches.

### Pairwise Comparison Implementation

Pairwise comparison is inherently more reliable for preference-based evaluation but requires bias mitigation.

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

**Confidence Calibration**: Confidence scores should reflect position consistency:
- Both passes agree: confidence = average of individual confidences
- Passes disagree: confidence = 0.5, verdict = TIE

### Human Evaluation

Human evaluation catches what automation misses. Humans notice hallucinated answers on unusual queries, system failures, and subtle biases that automated evaluation misses.

Effective human evaluation covers edge cases, samples systematically, tracks patterns, and provides contextual understanding. Use human evaluation to validate and calibrate automated systems.

## Test Set Design

### Sample Selection

Start with small samples during development. Early in agent development, changes have dramatic impacts because there is abundant low-hanging fruit. Small test sets reveal large effects.

Sample from real usage patterns. Add known edge cases. Ensure coverage across complexity levels.

### Complexity Stratification

Test sets should span complexity levels: simple (single tool call), medium (multiple tool calls), complex (many tool calls, significant ambiguity), and very complex (extended interaction, deep reasoning).

## Context Engineering Evaluation

### Testing Context Strategies

Context engineering choices should be validated through systematic evaluation. Run agents with different context strategies on the same test set. Compare quality scores, token usage, and efficiency metrics.

### Degradation Testing

Test how context degradation affects performance by running agents at different context sizes. Identify performance cliffs where context becomes problematic. Establish safe operating limits.

## Production Pipeline Design

### Evaluation Pipeline Architecture

Production evaluation systems require multiple layers:

```
+-------------------------------------------------+
|                 Evaluation Pipeline              |
+-------------------------------------------------+
|                                                  |
|  Input: Response + Prompt + Context              |
|           |                                      |
|           v                                      |
|  +---------------------+                        |
|  |   Criteria Loader   | <-- Rubrics, weights   |
|  +----------+----------+                        |
|             |                                    |
|             v                                    |
|  +---------------------+                        |
|  |   Primary Scorer    | <-- Direct or Pairwise |
|  +----------+----------+                        |
|             |                                    |
|             v                                    |
|  +---------------------+                        |
|  |   Bias Mitigation   | <-- Position swap, etc.|
|  +----------+----------+                        |
|             |                                    |
|             v                                    |
|  +---------------------+                        |
|  | Confidence Scoring  | <-- Calibration        |
|  +----------+----------+                        |
|             |                                    |
|             v                                    |
|  Output: Scores + Justifications + Confidence    |
|                                                  |
+-------------------------------------------------+
```

### Continuous Evaluation

Build evaluation pipelines that run automatically on agent changes. Track results over time. Compare versions to identify improvements or regressions.

### Production Monitoring

Track evaluation metrics in production by sampling interactions and evaluating randomly. Set alerts for quality drops. Maintain dashboards for trend analysis.

### Scaling Evaluation

For high-volume evaluation:

1. **Panel of LLMs (PoLL)**: Use multiple models as judges, aggregate votes
   - Reduces individual model bias
   - More expensive but more reliable for high-stakes decisions

2. **Hierarchical evaluation**: Fast cheap model for screening, expensive model for edge cases
   - Cost-effective for large volumes
   - Requires calibration of screening threshold

3. **Human-in-the-loop**: Automated evaluation for clear cases, human review for low-confidence
   - Best reliability for critical applications
   - Design feedback loop to improve automated evaluation

## Anti-Patterns

**Scoring without justification**
- Problem: Scores lack grounding, difficult to debug or improve
- Solution: Always require evidence-based justification before score

**Single-pass pairwise comparison**
- Problem: Position bias corrupts results
- Solution: Always swap positions and check consistency

**Overloaded criteria**
- Problem: Criteria measuring multiple things are unreliable
- Solution: One criterion = one measurable aspect

**Missing edge case guidance**
- Problem: Evaluators handle ambiguous cases inconsistently
- Solution: Include edge cases in rubrics with explicit guidance

**Ignoring confidence calibration**
- Problem: High-confidence wrong judgments are worse than low-confidence
- Solution: Calibrate confidence to position consistency and evidence strength

**Overfitting to specific paths**
- Problem: Evaluating the exact steps rather than the outcome
- Solution: Evaluate outcomes, not specific execution paths

**Single-metric obsession**
- Problem: Optimizing one number while other dimensions degrade
- Solution: Use multi-dimensional rubrics

**Neglecting context effects**
- Problem: Tests pass in isolation but fail with realistic context
- Solution: Test with realistic context sizes and histories

**Skipping human evaluation**
- Problem: Automated evaluation misses subtle issues
- Solution: Supplement LLM evaluation with human review

## Examples

### Example 1: Simple Evaluation Function

```python
def evaluate_agent_response(response, expected):
    rubric = load_rubric()
    scores = {}
    for dimension, config in rubric.items():
        scores[dimension] = assess_dimension(response, expected, dimension)
    overall = weighted_average(scores, config["weights"])
    return {"passed": overall >= 0.7, "scores": scores}
```

### Example 2: Test Set Structure

Test sets should span multiple complexity levels to ensure comprehensive evaluation:

```python
test_set = [
    {
        "name": "simple_lookup",
        "input": "What is the capital of France?",
        "expected": {"type": "fact", "answer": "Paris"},
        "complexity": "simple",
        "description": "Single tool call, factual lookup"
    },
    {
        "name": "medium_query",
        "input": "Compare the revenue of Apple and Microsoft last quarter",
        "complexity": "medium",
        "description": "Multiple tool calls, comparison logic"
    },
    {
        "name": "multi_step_reasoning",
        "input": "Analyze sales data from Q1-Q4 and create a summary report with trends",
        "complexity": "complex",
        "description": "Many tool calls, aggregation, analysis"
    },
    {
        "name": "research_synthesis",
        "input": "Research emerging AI technologies, evaluate their potential impact, and recommend adoption strategy",
        "complexity": "very_complex",
        "description": "Extended interaction, deep reasoning, synthesis"
    }
]
```

### Example 3: Direct Scoring for Accuracy

**Input**:
```
Prompt: "What causes seasons on Earth?"
Response: "Seasons are caused by Earth's tilted axis. As Earth orbits the Sun,
different hemispheres receive more direct sunlight at different times of year."
Criterion: Factual Accuracy (weight: 1.0)
Scale: 1-5
```

**Output**:
```json
{
  "criterion": "Factual Accuracy",
  "score": 5,
  "evidence": [
    "Correctly identifies axial tilt as primary cause",
    "Correctly explains differential sunlight by hemisphere",
    "No factual errors present"
  ],
  "justification": "Response accurately explains the cause of seasons with correct
scientific reasoning. Both the axial tilt and its effect on sunlight distribution
are correctly described.",
  "improvement": "Could add the specific tilt angle (23.5 degrees) for completeness."
}
```

### Example 4: Pairwise Comparison with Position Swap

**Input**:
```
Prompt: "Explain machine learning to a beginner"
Response A: [Technical explanation with jargon]
Response B: [Simple analogy-based explanation]
Criteria: ["clarity", "accessibility"]
```

**First Pass (A first)**:
```json
{ "winner": "B", "confidence": 0.8 }
```

**Second Pass (B first)**:
```json
{ "winner": "A", "confidence": 0.6 }
```
(Note: Winner is A because B was in first position)

**Mapped Second Pass**:
```json
{ "winner": "B", "confidence": 0.6 }
```

**Final Result**:
```json
{
  "winner": "B",
  "confidence": 0.7,
  "positionConsistency": {
    "consistent": true,
    "firstPassWinner": "B",
    "secondPassWinner": "B"
  }
}
```

### Example 5: Rubric Generation

**Input**:
```
criterionName: "Code Readability"
criterionDescription: "How easy the code is to understand and maintain"
domain: "software engineering"
scale: "1-5"
strictness: "balanced"
```

**Output** (abbreviated):
```json
{
  "levels": [
    {
      "score": 1,
      "label": "Poor",
      "description": "Code is difficult to understand without significant effort",
      "characteristics": [
        "No meaningful variable or function names",
        "No comments or documentation",
        "Deeply nested or convoluted logic"
      ]
    },
    {
      "score": 3,
      "label": "Adequate",
      "description": "Code is understandable with some effort",
      "characteristics": [
        "Most variables have meaningful names",
        "Basic comments present for complex sections",
        "Logic is followable but could be cleaner"
      ]
    },
    {
      "score": 5,
      "label": "Excellent",
      "description": "Code is immediately clear and maintainable",
      "characteristics": [
        "All names are descriptive and consistent",
        "Comprehensive documentation",
        "Clean, modular structure"
      ]
    }
  ],
  "edgeCases": [
    {
      "situation": "Code is well-structured but uses domain-specific abbreviations",
      "guidance": "Score based on readability for domain experts, not general audience"
    }
  ]
}
```

## Guidelines

1. **Use multi-dimensional rubrics, not single metrics** - Agent quality spans many dimensions
2. **Evaluate outcomes, not specific execution paths** - Agents may find alternative valid paths
3. **Always require justification before scores** - Chain-of-thought prompting improves reliability by 15-25%
4. **Always swap positions in pairwise comparison** - Single-pass comparison is corrupted by position bias
5. **Match scale granularity to rubric specificity** - Do not use 1-10 without detailed level descriptions
6. **Separate objective and subjective criteria** - Use direct scoring for objective, pairwise for subjective
7. **Include confidence scores** - Calibrate to position consistency and evidence strength
8. **Define edge cases explicitly** - Ambiguous situations cause the most evaluation variance
9. **Use domain-specific rubrics** - Generic rubrics produce generic (less useful) evaluations
10. **Cover complexity levels from simple to very complex** - Stratify test sets accordingly
11. **Test with realistic context sizes and histories** - Context effects matter
12. **Run evaluations continuously, not just before release** - Catch regressions early
13. **Supplement LLM evaluation with human review** - Automated evaluation misses subtle issues
14. **Validate against human judgments** - Automated evaluation is only valuable if it correlates with human assessment
15. **Monitor for systematic bias** - Track disagreement patterns by criterion, response type, model
16. **Design for iteration** - Evaluation systems improve with feedback loops
17. **Set clear pass/fail thresholds based on use case** - Ambiguous standards produce ambiguous results
18. **Track metrics over time for trend detection** - Point-in-time snapshots miss drift

## Building an Evaluation Framework: Step by Step

1. Define quality dimensions relevant to your use case
2. Create rubrics with clear, actionable level descriptions and edge cases
3. Choose evaluation approach per dimension (direct scoring vs. pairwise)
4. Build test sets from real usage patterns and edge cases, stratified by complexity
5. Implement automated evaluation pipelines with bias mitigation
6. Establish baseline metrics before making changes
7. Run evaluations on all significant changes
8. Track metrics over time for trend analysis
9. Supplement automated evaluation with human review
10. Feed disagreements back to improve rubrics and prompts

## Integration

This skill connects to all other skills as a cross-cutting concern:

- **context-fundamentals** - Evaluating context usage; evaluation prompts require effective context structure
- **context-degradation** - Detecting and measuring degradation effects
- **context-optimization** - Measuring optimization effectiveness; evaluation prompts can be optimized for token efficiency
- **multi-agent-patterns** - Evaluating coordination across agents
- **tool-design** - Evaluating tool effectiveness; evaluation tools need proper schemas and error handling
- **memory-systems** - Evaluating memory quality and recall

## References

External research:
- [Eugene Yan: Evaluating the Effectiveness of LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/)
- [Judging LLM-as-a-Judge (Zheng et al., 2023)](https://arxiv.org/abs/2306.05685)
- [G-Eval: NLG Evaluation using GPT-4 (Liu et al., 2023)](https://arxiv.org/abs/2303.16634)
- [Large Language Models are not Fair Evaluators (Wang et al., 2023)](https://arxiv.org/abs/2305.17926)
- LLM evaluation benchmarks and agent evaluation research

---

## Skill Metadata

**Created**: 2024-12-20
**Last Updated**: 2026-03-14
**Authors**: Agent Skills for Context Engineering Contributors, Muratcan Koylan
**Version**: 2.0.0
