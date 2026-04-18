---
name: agent-project-development
description: This skill should be used when the user asks to "start an LLM project", "design batch pipeline", "evaluate task-model fit", "structure agent project", or mentions pipeline architecture, agent-assisted development, cost estimation, or choosing between LLM and traditional approaches. NOT for evaluating agent quality or building evaluation rubrics (use agent-evaluation), NOT for multi-agent coordination or agent handoffs (use multi-agent-patterns).
---

# Project Development Methodology

Principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development. Applies whether building a batch processing pipeline, a multi-agent research system, or an interactive agent application.

## When to Activate

- Starting a new project that might benefit from LLM processing
- Evaluating whether a task is well-suited for agents versus traditional code
- Designing the architecture for an LLM-powered application
- Planning a batch processing pipeline with structured outputs
- Choosing between single-agent and multi-agent approaches
- Estimating costs and timelines for LLM-heavy projects

## Decision Tree: Task-Model Fit

```
Should you use LLM processing for this task?
+-- Does it require synthesis across sources? --> Likely YES
+-- Does it involve subjective judgment with rubrics? --> Likely YES
+-- Is natural language the desired output? --> Likely YES
+-- Is there tolerance for individual errors? --> Likely YES
+-- Is the domain knowledge in the model's training? --> Likely YES
|
+-- Does it require precise computation? --> Likely NO (use traditional code)
+-- Does it need real-time sub-second responses? --> Likely NO
+-- Does it require perfect accuracy? --> Likely NO (hallucination risk)
+-- Does it depend on proprietary data the model lacks? --> Likely NO
+-- Must same input produce identical output? --> Likely NO
|
+-- Mixed? --> Manual prototype first (5 minutes saves weeks)
```

## Core Concepts

### The Manual Prototype Step

Before investing in automation, validate task-model fit with a manual test. Copy one representative input into the model interface. Evaluate the output quality. This takes minutes and prevents hours of wasted development.

If the manual prototype fails, the automated system will fail. If it succeeds, you have a baseline and a template for prompt design.

### Pipeline Architecture

LLM projects benefit from staged pipeline architectures where each stage is:
- **Discrete**: Clear boundaries between stages
- **Idempotent**: Re-running produces the same result
- **Cacheable**: Intermediate results persist to disk
- **Independent**: Each stage can run separately

**The canonical pipeline structure:**

```
acquire → prepare → process → parse → render
```

1. **Acquire**: Fetch raw data from sources (APIs, files, databases)
2. **Prepare**: Transform data into prompt format
3. **Process**: Execute LLM calls (the expensive, non-deterministic step)
4. **Parse**: Extract structured data from LLM outputs
5. **Render**: Generate final outputs (reports, files, visualizations)

Stages 1, 2, 4, and 5 are deterministic. Stage 3 is non-deterministic and expensive. This separation allows re-running only the expensive LLM stage when necessary.

### File System as State Machine

Use the file system to track pipeline state rather than databases. Each processing unit gets a directory. Each stage completion is marked by file existence.

```
data/{id}/
├── raw.json         # acquire stage complete
├── prompt.md        # prepare stage complete
├── response.md      # process stage complete
├── parsed.json      # parse stage complete
```

This provides natural idempotency, easy debugging (all state is human-readable), simple parallelization (each directory is independent), and trivial caching.

### Structured Output Design

When LLM outputs must be parsed programmatically:

1. **Section markers**: Explicit headers or prefixes for parsing
2. **Format examples**: Show exactly what output should look like
3. **Rationale disclosure**: "I will be parsing this programmatically"
4. **Constrained values**: Enumerated options, score ranges, formats

**Example prompt structure:**
```
Analyze the following and provide your response in exactly this format:

## Summary
[Your summary here]

## Score
Rating: [1-10]

Follow this format exactly because I will be parsing it programmatically.
```

Build parsers that use flexible regex patterns, provide sensible defaults for missing sections, and log parsing failures rather than crashing.

### Agent-Assisted Development

The pattern: describe the goal and constraints → agent generates initial implementation → test and iterate on specific failures → refine based on results. The agent handles boilerplate and initial structure while you focus on domain-specific requirements and edge cases.

### Cost and Scale Estimation

```
Total cost = (items × tokens_per_item × price_per_token) + API overhead
```

For batch processing: estimate input/output tokens per item, multiply by item count, add 20-30% buffer for retries and failures. Track actual costs during development. If costs exceed estimates significantly, re-evaluate the approach.

## Decision Tree: Single vs Multi-Agent Architecture

```
Are items independent with no cross-item dependencies?
+-- Yes --> Single-agent pipeline
|   Simpler cost/complexity management
|
+-- No --> Does the task exceed one context window?
    +-- Yes --> Multi-agent with context isolation
    |   Each sub-agent gets fresh context for focused subtasks
    |
    +-- No --> Do specialized sub-agents measurably improve quality?
        +-- Yes --> Multi-agent
        +-- No --> Single-agent (default)
```

**Key insight**: The primary reason for multi-agent is context isolation, not role anthropomorphization.

## Architectural Reduction

Start with minimal architecture. Add complexity only when proven necessary.

**Vercel's d0 agent**: Reduced from 17 specialized tools to 2 primitives (bash + SQL), going from 80% to 100% success rate and 274s to 77s execution time.

**When reduction outperforms complexity:**
- Your data layer is well-documented and consistently structured
- The model has sufficient reasoning capability
- Your specialized tools were constraining rather than enabling
- You are spending more time maintaining scaffolding than improving outcomes

**When complexity is necessary:**
- Your underlying data is messy, inconsistent, or poorly documented
- The domain requires specialized knowledge the model lacks
- Safety constraints require limiting agent capabilities
- Operations are truly complex and benefit from structured workflows

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Skipping manual validation | Building automation for a task the model cannot do | Test one example manually first; 5 minutes saves weeks |
| Monolithic pipelines | Re-running all LLM calls ($30+) when parsing breaks | Separate stages with persistent intermediate outputs |
| Over-constraining the model | Guardrails that the model could handle on its own | Test whether your scaffolding helps or hurts |
| Ignoring costs until production | Token costs compound quickly at scale | Estimate and track from the beginning |
| Perfect parsing requirements | LLMs do not follow format instructions perfectly | Build robust parsers that handle variations |
| Premature optimization | Caching/parallelization before basic pipeline works | Get it working first, optimize second |
| Default to multi-agent | Adds complexity without proven benefit | Use single-agent unless context isolation is needed |
| Over-engineered tool suites | Many tools, low success rate | Apply architectural reduction: test with primitives first |

## Examples

**Example 1: Batch Analysis Pipeline (Karpathy's HN Time Capsule)**

Task: Analyze 930 HN discussions from 10 years ago with hindsight grading.
Architecture: 5-stage pipeline, file system state, structured output, 15 parallel workers.
Results: $58 total cost, ~1 hour execution, static HTML output.

**Example 2: Architectural Reduction (Vercel d0)**

Task: Text-to-SQL agent for internal analytics.
Before: 17 specialized tools, 80% success rate, 274s average.
After: 2 tools (bash + SQL), 100% success rate, 77s average.

See [Case Studies](./references/case-studies.md) for detailed analysis.

## Project Planning Template

1. **Task Analysis**: What is the input/output? Is this synthesis, generation, classification? Error tolerance? Value per success?
2. **Manual Validation**: Test one example with target model. Evaluate quality and format. Identify failure modes. Estimate tokens.
3. **Architecture Selection**: Single pipeline vs multi-agent. Required tools and data sources. Storage and caching strategy. Parallelization.
4. **Cost Estimation**: Items × tokens × price + 20-30% buffer. Development time. Infrastructure. Ongoing operational costs.
5. **Development Plan**: Stage-by-stage implementation. Testing per stage. Iteration milestones. Deployment approach.

## Guidelines

1. Validate task-model fit with manual prototyping before building automation
2. Structure pipelines as discrete, idempotent, cacheable stages
3. Use the file system for state management and debugging
4. Design prompts for structured, parseable outputs with explicit format examples
5. Start with minimal architecture; add complexity only when proven necessary
6. Estimate costs early and track throughout development
7. Build robust parsers that handle LLM output variations
8. Expect and plan for multiple architectural iterations
9. Test whether scaffolding helps or constrains model performance
10. Use agent-assisted development for rapid iteration on implementation

## Integration

- context-fundamentals - Understanding context constraints for prompt design
- tool-design - Designing tools for agent systems within pipelines
- multi-agent-patterns - When to use multi-agent versus single pipelines
- evaluation - Evaluating pipeline outputs and agent performance
- context-compression - Managing context when pipelines exceed limits

## References

Internal references:
- [Case Studies](./references/case-studies.md) - Karpathy HN Capsule, Vercel d0, Manus patterns
- [Pipeline Patterns](./references/pipeline-patterns.md) - Detailed pipeline architecture guidance

External resources:
- Karpathy's HN Time Capsule project: https://github.com/karpathy/hn-time-capsule
- Vercel d0 architectural reduction: https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
- Anthropic multi-agent research: How we built our multi-agent research system

---

## Skill Metadata

**Created**: 2025-12-25
**Last Updated**: 2026-04-18
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.1.0
