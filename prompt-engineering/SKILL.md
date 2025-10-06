---
name: prompt-engineering
description: >
  Comprehensive prompt optimization system for LLMs. Use when users need to optimize prompts,
  design effective AI interactions, evaluate prompt quality, or perform iterative refinement.
  Trigger this skill whenever the user mentions prompt engineering, prompt design, prompt optimization,
  LLM optimization, "improve this prompt", "make this prompt better", "write a system prompt",
  "create a prompt for", or asks about best practices for prompting AI models. Also trigger when
  the user wants to create reusable prompt templates, evaluate prompt quality, A/B test prompts,
  or build system prompts for any LLM (Claude, ChatGPT, Gemini, Llama, etc.). Even if the user
  doesn't use the word "prompt" — if they're crafting instructions for an AI model, use this skill.
---

# Prompt Engineering Skill

## Overview

Transform vague AI instructions into precision-engineered prompts that reliably produce
high-quality outputs. This skill combines proven techniques, systematic evaluation, and
iterative refinement to create prompts for any LLM platform.

## Decision Flow

Assess the request and pick the right mode:

```
User request arrives
  │
  ├─ "Make this prompt better" / has existing prompt
  │   └─ OPTIMIZE MODE: Analyze → Apply techniques → Deliver improved prompt
  │
  ├─ "Create a prompt for X" / needs new prompt from scratch
  │   ├─ Simple task → AUTO DESIGN: Apply techniques → Deliver
  │   └─ Complex task → INTERACTIVE DESIGN: Ask 2-3 questions → Design → Test
  │
  ├─ "Evaluate/test this prompt" / quality assessment
  │   └─ EVALUATE MODE: Score → Identify weaknesses → Suggest improvements
  │
  └─ "Help me understand prompt engineering" / learning
      └─ EDUCATE: Teach relevant techniques with examples
```

## Core Process: The 4-D Framework

Apply this framework for every prompt optimization task.

### 1. DECONSTRUCT — Understand What's Really Being Asked

Read the prompt (or request) and answer:
- What is the actual goal? (Often different from what's literally stated)
- What assumptions are unstated?
- What information is missing that the LLM will need?
- Who is the audience for the output?

### 2. DIAGNOSE — Identify What's Wrong or Missing

Score the prompt against these dimensions:
- **Clarity**: Is it unambiguous? Could the LLM interpret it differently than intended?
- **Specificity**: Are outputs constrained enough to be useful?
- **Structure**: Is information organized logically?
- **Completeness**: Does it include role, context, constraints, format, examples?
- **Efficiency**: Is every token earning its keep, or is there bloat?

### 3. DEVELOP — Apply the Right Techniques

Select techniques based on what the diagnosis reveals. Here are the core techniques
(see `references/TECHNIQUES.md` for the full catalog with detailed examples):

**Role Assignment** — Give the LLM a specific expert identity with credentials and methodology.
Use when domain expertise matters. The more specific the role, the better the output quality.

**Context Layering** — Provide essential background in a structured format:
Background → Goal → Constraints → Output Format. Remove anything the LLM doesn't need.

**Chain-of-Thought** — Ask the LLM to reason step by step. Critical for complex analytical,
mathematical, or multi-factor reasoning tasks. Without this, LLMs often skip to conclusions.

**Few-Shot Examples** — Show 2-3 input→output pairs that demonstrate the pattern you want.
This is the single most powerful technique for controlling output format and style.

**Task Decomposition** — Break complex tasks into sequential stages where each stage feeds
the next. Prevents the LLM from trying to do everything at once and dropping quality.

**Constraints & Guardrails** — Define what NOT to do, set length limits, specify format
requirements. LLMs perform better with clear boundaries than with open-ended freedom.

**Output Specification** — Define the exact structure, format, and content requirements
of the output. Be explicit: headers, sections, length, style, tone.

### 4. DELIVER — Present the Optimized Prompt

When delivering:
- Show the complete optimized prompt in a code block or artifact
- Briefly explain the key improvements (2-3 sentences, not a lecture)
- Note which techniques were applied and why
- If relevant, provide platform-specific tips (see `references/PLATFORMS.md`)
- Offer to iterate if the user wants refinements

## Optimization Patterns

### Pattern: Role + Context + Task + Format

The most common pattern. Works for 80% of prompt optimization needs.

```
You are a [SPECIFIC EXPERT] with expertise in [DOMAIN].

Context:
[ESSENTIAL BACKGROUND — 2-4 lines max]

Task:
[CLEAR, SPECIFIC OBJECTIVE]

Requirements:
- [CONSTRAINT 1]
- [CONSTRAINT 2]

Output format:
[EXACT STRUCTURE EXPECTED]
```

### Pattern: Few-Shot + Chain-of-Thought

Use for tasks requiring consistent format AND complex reasoning.

```
[ROLE AND CONTEXT]

Here are examples of the expected analysis:

Example 1:
Input: [SAMPLE]
Reasoning: [STEP-BY-STEP THOUGHT PROCESS]
Output: [RESULT]

Example 2:
Input: [SAMPLE]
Reasoning: [STEP-BY-STEP THOUGHT PROCESS]
Output: [RESULT]

Now analyze the following. Think through your reasoning step by step before
providing your final output.

Input: [ACTUAL TASK]
```

### Pattern: Multi-Stage Pipeline

Use for complex tasks that benefit from decomposition.

```
Complete this analysis in three stages:

Stage 1 — Research:
[GATHER AND ORGANIZE INFORMATION]
Present findings as: [FORMAT]

Stage 2 — Analysis:
Using the research from Stage 1, [ANALYZE SPECIFIC ASPECTS]
Present analysis as: [FORMAT]

Stage 3 — Synthesis:
Based on your analysis, [PRODUCE FINAL DELIVERABLE]
Format: [FINAL OUTPUT SPECIFICATION]
```

## Context Enrichment

When the user's prompt references specific company data, projects, documents, or internal
information, enrich the prompt with real context before optimizing.

**When to enrich:**
- User mentions "our company/team/project/product"
- References specific documents, emails, or meetings
- Uses domain terminology suggesting organizational context
- Mentions temporal markers like "Q3", "this sprint", "last month"

**How to enrich:**
Use available tools (web search, connected integrations like Google Drive, Asana, Jira,
Confluence, Slack, etc.) to pull relevant context. Synthesize the key facts — goals,
metrics, stakeholders, constraints, timelines — and inject them into the prompt's
context section.

The goal is to transform a generic prompt into one grounded in the user's actual situation.
Don't dump raw data — distill what the LLM actually needs to produce a useful output.

## Evaluation Framework

When asked to evaluate a prompt (or when testing an optimized prompt), assess across
these dimensions. See `references/EVALUATION.md` for the full methodology.

### Quick Evaluation (Score 1-5 each)

| Dimension | What to Check |
|-----------|--------------|
| **Clarity** | Could this be misinterpreted? Vague terms? Ambiguity? |
| **Specificity** | Are outputs constrained enough? Format defined? |
| **Completeness** | Role + Context + Task + Format + Examples present? |
| **Efficiency** | Token-efficient? No redundancy? Every line earns its place? |
| **Robustness** | Will it work across input variations? Edge cases handled? |

### LLM-as-Judge Evaluation

For systematic testing, use the LLM itself as an evaluator:

```
Evaluate the following response against these criteria.
Score each 1-5 with brief justification.

Criteria:
1. Accuracy — factual correctness
2. Relevance — addresses the actual question
3. Completeness — covers all aspects
4. Clarity — well-organized and readable

Response to evaluate:
[PASTE RESPONSE]

For each criterion: Score (1-5) | Evidence | Improvement suggestion
Overall: __/20
```

### A/B Testing Process

When comparing two prompt versions:
1. Define 3-5 test inputs covering typical, edge, and stress cases
2. Run both prompts against each test input
3. Blind-evaluate outputs (don't look at which prompt produced which)
4. Score on the relevant dimensions
5. Declare winner with reasoning

## Platform-Specific Notes

Different LLMs respond to different prompting styles. Key differences:

- **Claude**: Excels with XML tags for structure, responds well to nuanced role
  descriptions, supports extended thinking. Avoid over-constraining — Claude performs
  better with clear intent than rigid rules.
- **ChatGPT (GPT-4)**: Responds well to system/user message separation, function calling
  patterns, and explicit instruction following. Benefits from "You MUST" directives.
- **Gemini**: Strong with multimodal prompts, benefits from clear section demarcation.

See `references/PLATFORMS.md` for detailed platform optimization guides.

## Templates

Reusable prompt templates for common use cases are in `references/TEMPLATES.md`:
- Research & Analysis
- Creative & Content
- Technical & Code
- Business & Strategy
- Teaching & Explanation

## Anti-Patterns to Fix

When optimizing, watch for and fix these common problems:

**Vague instructions** → Add specificity: who, what, how, format, length, audience
**No examples** → Add 2-3 few-shot examples showing desired output pattern
**Buried intent** → Move the actual task to the top; context supports, doesn't obscure
**Kitchen sink** → Remove requirements that don't serve the core goal
**No output spec** → Define exact format, structure, and length expectations
**Assumed knowledge** → Add necessary context the LLM wouldn't have
**Contradictions** → Resolve conflicting requirements; flag trade-offs
**Over-engineering** → Simple tasks need simple prompts. Don't add complexity for its own sake.

## Reference Files

Load these as needed for deeper guidance:

| File | When to Read |
|------|-------------|
| `references/TECHNIQUES.md` | Full technique catalog with detailed examples |
| `references/EVALUATION.md` | Comprehensive evaluation methodologies and rubrics |
| `references/TEMPLATES.md` | Reusable prompt patterns for common use cases |
| `references/PLATFORMS.md` | Platform-specific optimization (Claude, GPT, Gemini) |

## Best Practices

- Focus on user intent, not their exact wording — understand what they actually need
- Ask 2-3 strategic questions for complex cases; don't interrogate
- Test professionally-used prompts before deploying
- Explain significant changes briefly — don't lecture
- Keep prompts as concise as possible while being complete
- Consider the target platform's strengths and quirks
- Iterate: first draft → test → refine → test again
