# Prompt Evaluation Framework

Comprehensive guide for systematic prompt evaluation, testing, and quality assessment.

## Evaluation Dimensions

### 1. Performance Metrics

**Accuracy**
- Definition: Factual correctness and precision
- Measurement:
  ```
  accuracy_score = correct_facts / total_facts
  hallucination_rate = false_claims / total_claims
  ```
- Testing: Compare against ground truth, expert validation

**Relevance**
- Definition: Alignment with query requirements and goals
- Measurement:
  ```
  relevance_score = relevant_info / total_info
  off_topic_rate = off_topic_content / total_content
  ```
- Testing: Human judgment, semantic similarity

**Completeness**
- Definition: Comprehensive coverage of requirements
- Measurement:
  ```
  completeness_score = requirements_met / total_requirements
  coverage_depth = detail_level (1-5 scale)
  ```
- Testing: Checklist validation, requirement mapping

**Consistency**
- Definition: Stable outputs across multiple runs
- Measurement:
  ```
  consistency_score = similar_responses / total_runs
  variance = std_dev(response_quality)
  ```
- Testing: Run same prompt 5-10 times, compare outputs

### 2. Quality Metrics

**Clarity**
- Unambiguous instructions
- Clear structure and flow
- Appropriate language level
- Measurement: Human readability scores, ambiguity detection

**Specificity**
- Concrete vs. vague language
- Detailed requirements
- Precise constraints
- Measurement: Specificity ratio, constraint completeness

**Actionability**
- Clear next steps
- Practical recommendations
- Implementation guidance
- Measurement: Actionable items per response

**Coherence**
- Logical flow
- Internal consistency
- Proper argumentation
- Measurement: Coherence scoring (1-5), logic validation

### 3. Efficiency Metrics

**Token Usage**
- Prompt length (input tokens)
- Response length (output tokens)
- Total cost per query
- Measurement: Direct token counting

**Response Time**
- Latency (time to first token)
- Total generation time
- Throughput (queries per second)
- Measurement: Direct timing

**Cost Effectiveness**
- Value per dollar spent
- Quality-cost ratio
- ROI calculation
- Measurement: quality_score / (tokens × cost_per_token)

## Evaluation Methods

### 1. Automated Evaluation

**Rule-Based Checks**
```python
def evaluate_prompt_basic(prompt):
    scores = {
        'has_role': check_role_assignment(prompt),
        'has_constraints': check_constraints(prompt),
        'has_examples': check_examples(prompt),
        'has_output_spec': check_output_format(prompt),
        'length_appropriate': check_length(prompt, min=50, max=1000)
    }
    return scores

def check_role_assignment(prompt):
    role_indicators = ['you are', 'act as', 'as a', 'expert in']
    return any(ind in prompt.lower() for ind in role_indicators)

def check_constraints(prompt):
    constraint_words = ['must', 'should', 'constraint', 'requirement']
    return sum(word in prompt.lower() for word in constraint_words) >= 2

def check_output_format(prompt):
    format_indicators = ['format', 'structure', 'organize', 'section']
    return any(ind in prompt.lower() for ind in format_indicators)
```

**Metrics-Based Evaluation**
```python
def evaluate_response_metrics(response, ground_truth=None):
    metrics = {}
    
    # Length metrics
    metrics['word_count'] = len(response.split())
    metrics['sentence_count'] = len(response.split('.'))
    metrics['avg_sentence_length'] = metrics['word_count'] / max(metrics['sentence_count'], 1)
    
    # Readability
    metrics['flesch_reading_ease'] = calculate_flesch(response)
    
    # If ground truth available
    if ground_truth:
        metrics['bleu_score'] = calculate_bleu(response, ground_truth)
        metrics['rouge_scores'] = calculate_rouge(response, ground_truth)
        metrics['semantic_similarity'] = calculate_bert_score(response, ground_truth)
    
    return metrics
```

### 2. LLM-as-Judge Evaluation

**G-Eval Framework**
```
You are an expert evaluator. Assess this LLM response comprehensively.

QUERY: {original_query}
RESPONSE: {llm_response}

Evaluate on these dimensions (1-5 scale):

## 1. Accuracy
Score: __/5
Reasoning:
- Are facts correct?
- Any hallucinations?
- Sources reliable?

Evidence:
[Specific examples from response]

## 2. Relevance  
Score: __/5
Reasoning:
- Addresses the query?
- Stays on topic?
- Appropriate scope?

Evidence:
[Specific examples]

## 3. Clarity
Score: __/5
Reasoning:
- Easy to understand?
- Well structured?
- Appropriate language?

Evidence:
[Specific examples]

## 4. Completeness
Score: __/5
Reasoning:
- Covers all aspects?
- Sufficient depth?
- Nothing missing?

Evidence:
[Specific examples]

## Overall Assessment
Total: __/20

Strengths:
1. [Specific strength]
2. [Specific strength]

Weaknesses:
1. [Specific weakness]
2. [Specific weakness]

Improvements:
1. [Specific suggestion]
2. [Specific suggestion]
```

**Pairwise Comparison**
```
Compare these two responses and select the better one:

QUERY: {query}

RESPONSE A: {response_a}
RESPONSE B: {response_b}

For each criterion, select the better response (A/B/Tie):

1. Accuracy: __ because [reasoning]
2. Relevance: __ because [reasoning]
3. Clarity: __ because [reasoning]
4. Completeness: __ because [reasoning]
5. Overall: __ 

Justification:
[Detailed reasoning for overall choice]
```

### 3. Human Evaluation

**Expert Review Protocol**
```
Evaluator: [Name/Expertise]
Date: [Date]
Prompt ID: [ID]

Rating Scale: 1-5 (1=Poor, 5=Excellent)

1. Technical Accuracy: __/5
   Notes: [Specific feedback]

2. Relevance to Task: __/5
   Notes: [Specific feedback]

3. Clarity of Expression: __/5
   Notes: [Specific feedback]

4. Completeness: __/5
   Notes: [Specific feedback]

5. Practical Utility: __/5
   Notes: [Specific feedback]

Overall Score: __/25

Qualitative Feedback:
- What worked well:
- What needs improvement:
- Suggested changes:
- Edge cases identified:
```

**User Acceptance Testing**
```
User: [Role/Department]
Task: [What they were trying to accomplish]

Questions:
1. Did the response meet your needs? (Yes/No/Partially)
2. What would you change?
3. Rate usefulness (1-5): __
4. Would you use this prompt again? (Yes/No)
5. Time saved vs. manual approach: __ minutes

Follow-up:
- Any confusion or unclear parts?
- Missing information?
- Unexpected results?
```

## Testing Strategies

### 1. Test Case Generation

**Variation Types**
```python
test_case_types = {
    'typical': {
        'description': 'Standard use case',
        'purpose': 'Baseline performance',
        'examples': [
            'Normal complexity',
            'Average length input',
            'Common scenario'
        ]
    },
    'edge_cases': {
        'description': 'Boundary conditions',
        'purpose': 'Robustness testing',
        'examples': [
            'Empty input',
            'Very long input (>10K words)',
            'Ambiguous request',
            'Contradictory requirements'
        ]
    },
    'stress_tests': {
        'description': 'Extreme scenarios',
        'purpose': 'Failure mode analysis',
        'examples': [
            'Maximum complexity',
            'Multiple constraints',
            'Conflicting goals',
            'Minimal information'
        ]
    },
    'negative_tests': {
        'description': 'Invalid inputs',
        'purpose': 'Error handling',
        'examples': [
            'Off-topic requests',
            'Malformed input',
            'Inappropriate content',
            'Out-of-scope tasks'
        ]
    }
}
```

**Systematic Test Generation**
```python
def generate_test_suite(prompt_template, num_tests=20):
    """Generate comprehensive test suite"""
    
    tests = []
    
    # Typical cases (50%)
    for i in range(num_tests // 2):
        tests.append(generate_typical_case(prompt_template, i))
    
    # Edge cases (30%)
    for i in range(int(num_tests * 0.3)):
        tests.append(generate_edge_case(prompt_template, i))
    
    # Stress tests (15%)
    for i in range(int(num_tests * 0.15)):
        tests.append(generate_stress_test(prompt_template, i))
    
    # Negative tests (5%)
    for i in range(max(1, num_tests // 20)):
        tests.append(generate_negative_test(prompt_template, i))
    
    return tests

def generate_typical_case(template, seed):
    """Generate realistic, common scenario"""
    return {
        'input': create_realistic_input(template, complexity='medium', seed=seed),
        'expected_type': 'comprehensive_response',
        'validation': 'standard_metrics'
    }

def generate_edge_case(template, seed):
    """Generate boundary condition"""
    edge_types = ['minimal_info', 'maximal_info', 'ambiguous', 'unusual_format']
    edge_type = edge_types[seed % len(edge_types)]
    return {
        'input': create_edge_input(template, edge_type=edge_type),
        'expected_type': 'graceful_handling',
        'validation': 'robustness_check'
    }
```

### 2. A/B Testing

**Comparison Framework**
```python
def ab_test_prompts(prompt_a, prompt_b, test_cases, metrics):
    """
    Compare two prompt versions
    
    Returns:
        Statistical comparison results
    """
    results_a = []
    results_b = []
    
    for test_case in test_cases:
        # Run both prompts
        response_a = run_llm(prompt_a, test_case['input'])
        response_b = run_llm(prompt_b, test_case['input'])
        
        # Evaluate both
        score_a = evaluate(response_a, metrics)
        score_b = evaluate(response_b, metrics)
        
        results_a.append(score_a)
        results_b.append(score_b)
    
    # Statistical analysis
    comparison = {
        'prompt_a_mean': mean(results_a),
        'prompt_b_mean': mean(results_b),
        'difference': mean(results_b) - mean(results_a),
        'p_value': t_test(results_a, results_b),
        'confidence_interval': confidence_interval(results_a, results_b),
        'winner': determine_winner(results_a, results_b)
    }
    
    return comparison
```

**Statistical Significance**
```python
def determine_significance(results_a, results_b, alpha=0.05):
    """
    Determine if difference is statistically significant
    """
    from scipy import stats
    
    # Perform t-test
    t_stat, p_value = stats.ttest_ind(results_a, results_b)
    
    # Calculate effect size (Cohen's d)
    mean_a, mean_b = mean(results_a), mean(results_b)
    pooled_std = sqrt((std(results_a)**2 + std(results_b)**2) / 2)
    cohens_d = (mean_b - mean_a) / pooled_std
    
    return {
        'significant': p_value < alpha,
        'p_value': p_value,
        'effect_size': cohens_d,
        'interpretation': interpret_effect_size(cohens_d)
    }

def interpret_effect_size(d):
    """Cohen's d interpretation"""
    if abs(d) < 0.2:
        return 'negligible'
    elif abs(d) < 0.5:
        return 'small'
    elif abs(d) < 0.8:
        return 'medium'
    else:
        return 'large'
```

### 3. Regression Testing

**Versioning and Comparison**
```python
class PromptVersionManager:
    def __init__(self):
        self.versions = {}
        self.test_suite = []
        self.baseline_scores = {}
    
    def add_version(self, version_id, prompt, description):
        """Add new prompt version"""
        self.versions[version_id] = {
            'prompt': prompt,
            'description': description,
            'timestamp': datetime.now(),
            'scores': None
        }
    
    def run_regression_test(self, version_id):
        """Test new version against baseline"""
        prompt = self.versions[version_id]['prompt']
        
        scores = []
        for test_case in self.test_suite:
            response = run_llm(prompt, test_case['input'])
            score = evaluate(response, test_case['metrics'])
            scores.append(score)
        
        # Compare to baseline
        regression_detected = self.check_regression(scores)
        
        self.versions[version_id]['scores'] = scores
        
        return {
            'version': version_id,
            'scores': scores,
            'mean_score': mean(scores),
            'vs_baseline': mean(scores) - self.baseline_scores['mean'],
            'regression_detected': regression_detected,
            'failing_tests': self.identify_failures(scores)
        }
    
    def check_regression(self, new_scores, threshold=0.05):
        """Check if performance degraded significantly"""
        baseline_mean = self.baseline_scores['mean']
        new_mean = mean(new_scores)
        
        # Performance dropped by more than threshold
        return (baseline_mean - new_mean) / baseline_mean > threshold
```

## Evaluation Workflows

### Comprehensive Evaluation Pipeline

```python
def comprehensive_evaluation(prompt, test_suite):
    """
    Full evaluation pipeline
    
    Steps:
    1. Automated checks
    2. Test case execution  
    3. Metrics calculation
    4. LLM-as-judge evaluation
    5. Statistical analysis
    6. Report generation
    """
    
    results = {
        'prompt_analysis': {},
        'test_results': [],
        'metrics': {},
        'llm_judge_scores': [],
        'recommendations': []
    }
    
    # Step 1: Analyze prompt structure
    results['prompt_analysis'] = analyze_prompt_structure(prompt)
    
    # Step 2: Run test cases
    for test_case in test_suite:
        response = run_llm(prompt, test_case['input'])
        test_result = {
            'test_id': test_case['id'],
            'input': test_case['input'],
            'response': response,
            'metrics': calculate_metrics(response, test_case),
            'passed': validate_response(response, test_case['expected'])
        }
        results['test_results'].append(test_result)
    
    # Step 3: Aggregate metrics
    results['metrics'] = aggregate_metrics(results['test_results'])
    
    # Step 4: LLM-as-judge evaluation (sample)
    sample_tests = random.sample(results['test_results'], min(5, len(results['test_results'])))
    for test in sample_tests:
        judge_score = llm_judge_evaluate(test['input'], test['response'])
        results['llm_judge_scores'].append(judge_score)
    
    # Step 5: Generate recommendations
    results['recommendations'] = generate_recommendations(results)
    
    # Step 6: Create report
    report = create_evaluation_report(results)
    
    return report

def generate_recommendations(results):
    """Generate actionable improvement recommendations"""
    recommendations = []
    
    metrics = results['metrics']
    
    # Check accuracy
    if metrics['accuracy'] < 0.8:
        recommendations.append({
            'priority': 'high',
            'area': 'accuracy',
            'issue': 'Low factual accuracy detected',
            'suggestion': 'Add explicit accuracy requirements and fact-checking instructions'
        })
    
    # Check consistency
    if metrics['consistency_score'] < 0.7:
        recommendations.append({
            'priority': 'high',
            'area': 'consistency',
            'issue': 'High variance across runs',
            'suggestion': 'Add more specific constraints and examples to reduce variability'
        })
    
    # Check completeness
    if metrics['completeness'] < 0.9:
        recommendations.append({
            'priority': 'medium',
            'area': 'completeness',
            'issue': 'Some requirements not consistently met',
            'suggestion': 'Make requirements more explicit with checklist format'
        })
    
    # Token efficiency
    if metrics['avg_tokens'] > 1000 and metrics['quality_score'] < 0.9:
        recommendations.append({
            'priority': 'medium',
            'area': 'efficiency',
            'issue': 'High token usage without proportional quality',
            'suggestion': 'Simplify prompt or add length constraints'
        })
    
    return sorted(recommendations, key=lambda x: x['priority'], reverse=True)
```

### Iterative Improvement Workflow

```
1. Initial Evaluation
   ├─> Run test suite
   ├─> Calculate baseline metrics
   └─> Identify top 3 issues

2. Targeted Refinement
   ├─> Address highest priority issue
   ├─> Make minimal, focused changes
   └─> Document change rationale

3. Re-evaluation
   ├─> Run same test suite
   ├─> Compare to baseline
   └─> Verify improvement

4. Regression Check
   ├─> Ensure other metrics didn't degrade
   ├─> Check for unintended side effects
   └─> Validate on edge cases

5. Repeat or Accept
   ├─> If score < target: Return to step 2
   └─> If score ≥ target: Finalize and document

6. Production Validation
   ├─> Monitor real usage
   ├─> Collect user feedback
   └─> Plan next iteration
```

## Reporting

### Evaluation Report Template

```markdown
# Prompt Evaluation Report

## Summary
- Prompt ID: [ID]
- Version: [VERSION]
- Evaluation Date: [DATE]
- Evaluator: [NAME/SYSTEM]

## Overall Score: __/100

## Detailed Metrics

### Performance (40 points)
| Metric | Score | Target | Status |
|--------|-------|--------|--------|
| Accuracy | __/10 | >8 | ✓/✗ |
| Relevance | __/10 | >8 | ✓/✗ |
| Completeness | __/10 | >8 | ✓/✗ |
| Consistency | __/10 | >7 | ✓/✗ |

### Quality (30 points)
| Metric | Score | Target | Status |
|--------|-------|--------|--------|
| Clarity | __/10 | >8 | ✓/✗ |
| Structure | __/10 | >7 | ✓/✗ |
| Actionability | __/10 | >7 | ✓/✗ |

### Efficiency (30 points)
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Avg tokens | __ | <800 | ✓/✗ |
| Cost per query | $__ | <$0.10 | ✓/✗ |
| Response time | __s | <5s | ✓/✗ |

## Test Results
- Total tests: __
- Passed: __ (__%)
- Failed: __ (__%)
- Edge cases passed: __/__

## Key Findings

### Strengths
1. [Specific strength with evidence]
2. [Specific strength with evidence]
3. [Specific strength with evidence]

### Weaknesses
1. [Specific weakness with impact]
2. [Specific weakness with impact]
3. [Specific weakness with impact]

## Recommendations

### High Priority
1. [Action item with expected impact]
2. [Action item with expected impact]

### Medium Priority
1. [Action item with expected impact]
2. [Action item with expected impact]

### Low Priority
1. [Nice-to-have improvement]

## Next Steps
1. [Immediate action]
2. [Follow-up testing needed]
3. [Long-term monitoring plan]

## Appendix
- Full test case results
- Statistical analysis details
- Comparison to previous versions
```

## Best Practices

### Do ✓
- Test with diverse, realistic inputs
- Use multiple evaluation methods (automated + human + LLM-judge)
- Track metrics over time
- Document all changes and rationale
- Include edge cases in test suite
- Get domain expert validation for critical use cases
- Maintain version history
- Use statistical significance testing for comparisons

### Don't ✗
- Rely on single evaluation method
- Test only on typical cases
- Ignore statistical significance
- Make multiple changes at once (can't isolate impact)
- Skip documentation
- Over-optimize for test set (overfitting)
- Ignore user feedback
- Deploy without baseline metrics
