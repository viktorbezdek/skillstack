---
name: prompt-engineering
description: >-
  Design, evaluate, and iteratively improve prompts for LLMs — system prompts, few-shot
  examples, chain-of-thought structures, and instruction templates. Use when the user
  asks to improve a prompt, write a system prompt, optimize LLM instructions, reduce
  hallucinations through prompt structure, test prompt variants, or apply prompting
  techniques (CoT, ReAct, few-shot, structured output). NOT for building MCP tools
  or server implementation (use mcp-server). NOT for creating Claude Code SKILL.md
  files (use skill-foundry). NOT for building a full agent (use build-ai-agent workflow).
---

# Prompt Engineering Skill

## When to Use

Activate this skill when:
- Optimizing an existing prompt that produces inconsistent or low-quality output
- Creating a new prompt from scratch (system prompt, instruction template, few-shot)
- Evaluating prompt quality across dimensions (clarity, specificity, structure)
- A/B testing prompt variants for measurable improvement
- Migrating a prompt between LLM platforms (Claude ↔ GPT-4 ↔ Gemini)
- Applying specific techniques: Chain-of-Thought, Few-Shot, Role Assignment, Output Specification
- Reducing hallucinations through prompt structure and constraints
- Designing multi-stage prompt pipelines

## When NOT to Use

- **Building MCP servers or implementing MCP protocol** → use `mcp-server`
- **Creating Claude Code SKILL.md files** → use `skill-foundry`
- **Building a full agent system** → use agent-project-development workflow
- **Generating creative content directly** → this skill optimizes the prompt, not the output
- **Fine-tuning or training models** → prompt engineering operates at inference time

## Decision Flow

Assess the request and pick the right mode:

```
User request arrives
  │
  ├─ Has existing prompt + describes problem?
  │   └─ OPTIMIZE MODE
  │       1. Deconstruct: What's really being asked?
  │       2. Diagnose: Score on 5 dimensions (see below)
  │       3. Develop: Apply targeted techniques
  │       4. Deliver: Improved prompt + brief explanation
  │
  ├─ Needs new prompt from scratch?
  │   ├─ Simple, well-defined task → AUTO DESIGN: Build directly
  │   └─ Complex or ambiguous task → INTERACTIVE DESIGN: Ask 2-3 questions first
  │
  ├─ Quality assessment / comparison request?
  │   └─ EVALUATE MODE
  │       1. Score each dimension 1-5
  │       2. Identify specific weaknesses
  │       3. Suggest targeted improvements
  │
  └─ Learning / understanding request?
      └─ EDUCATE: Teach relevant techniques with before/after examples
```

### Technique Selection Decision Tree

```
Diagnosis reveals the problem:
  │
  ├─ No domain expertise → Role Assignment
  │   └─ Give LLM a specific expert identity with credentials
  │
  ├─ Missing background / LLM lacks context → Context Layering
  │   └─ Background → Goal → Constraints → Output Format
  │
  ├─ Complex reasoning, math, multi-factor analysis → Chain-of-Thought
  │   └─ Ask LLM to reason step by step before answering
  │
  ├─ Output format inconsistent → Few-Shot Examples + Output Specification
  │   └─ Show 2-3 input→output pairs + define exact structure
  │
  ├─ Task too large for single pass → Task Decomposition
  │   └─ Break into sequential stages; each feeds the next
  │
  ├─ No boundaries defined → Constraints & Guardrails
  │   └─ Define what NOT to do, length limits, format requirements
  │
  └─ Output structure undefined → Output Specification
      └─ Define headers, sections, length, style, tone explicitly
```

## Core Process: The 4-D Framework

Apply this framework for every prompt optimization task.

### 1. DECONSTRUCT — Understand What's Really Being Asked

- What is the actual goal? (Often different from what's literally stated)
- What assumptions are unstated?
- What information is missing that the LLM will need?
- Who is the audience for the output?

### 2. DIAGNOSE — Identify What's Wrong or Missing

Score the prompt against these dimensions:

| Dimension | What to Check | Red Flag |
|-----------|--------------|----------|
| **Clarity** | Could this be misinterpreted? Vague terms? | Score ≤ 2: Rewrite with precise language |
| **Specificity** | Are outputs constrained enough? Format defined? | Score ≤ 2: Add Output Specification |
| **Structure** | Information organized logically? | Score ≤ 2: Apply Context Layering |
| **Completeness** | Role + Context + Task + Format + Examples present? | Score ≤ 2: Add missing components |
| **Efficiency** | Every token earns its keep? No redundancy? | Score ≤ 2: Cut bloat |

### 3. DEVELOP — Apply the Right Techniques

Select techniques based on diagnosis (see Technique Selection Decision Tree above).
For detailed examples, see `references/TECHNIQUES.md`.

**Role Assignment** — Give the LLM a specific expert identity with credentials and methodology.
Use when domain expertise matters. The more specific the role, the better the output quality.

**Context Layering** — Provide essential background in structured format:
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

- Show the complete optimized prompt in a code block or artifact
- Briefly explain key improvements (2-3 sentences, not a lecture)
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

## Anti-Patterns to Fix

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Kitchen sink prompt** | Every possible instruction crammed in; model drowns in contradictory directives | Identify the 3 most important requirements. Cut the rest. Each instruction must earn its tokens. |
| **Copycat prompt** | Copied from a blog post without understanding why it works; fails when use case differs slightly | Use the 4-D framework to analyze why a template works before adapting it. Understand the technique, not just the words. |
| **Platform-blind prompt** | Written for one LLM and assumed to transfer; Claude XML tags confuse GPT-4, "You MUST" over-constrains Claude | Use platform-specific translation (see `references/PLATFORMS.md`). Convert structural patterns, don't just change words. |
| **Format-free prompt** | No output structure specified; each run produces different format, breaking downstream processing | Add explicit Output Specification with headers, structure, and length requirements. |
| **Contradiction prompt** | "Be concise" AND "Be thorough" in same prompt; model oscillates between contradictory instructions | Resolve trade-offs explicitly: "Prioritize completeness over brevity" or "Be thorough on methodology, concise on examples." |
| **Vague instructions** | "Analyze the data" — no format, scope, or audience defined | Add specificity: who, what, how, format, length, audience |
| **Buried intent** | The actual task is buried under paragraphs of context | Move the task to the top; context supports, doesn't obscure |
| **Assumed knowledge** | LLM expected to know company-specific or domain-specific facts | Add necessary context the LLM wouldn't have |
| **No examples** | LLM must infer expected output format from description alone | Add 2-3 few-shot examples showing desired output pattern |
| **Over-engineering** | Simple task gets a complex multi-stage prompt with unnecessary techniques | Simple tasks need simple prompts. Don't add complexity for its own sake. |

## Context Enrichment

When the user's prompt references specific company data, projects, documents, or internal
information, enrich the prompt with real context before optimizing.

**When to enrich:**
- User mentions "our company/team/project/product"
- References specific documents, emails, or meetings
- Uses domain terminology suggesting organizational context
- Mentions temporal markers like "Q3", "this sprint", "last month"

**How to enrich:**
Use available tools (web search, connected integrations) to pull relevant context.
Synthesize the key facts — goals, metrics, stakeholders, constraints, timelines — and
inject them into the prompt's context section. Don't dump raw data — distill what the
LLM actually needs to produce a useful output.

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

### A/B Testing Process

When comparing two prompt versions:
1. Define 3-5 test inputs covering typical, edge, and stress cases
2. Run both prompts against each test input
3. Blind-evaluate outputs (don't look at which prompt produced which)
4. Score on the relevant dimensions
5. Declare winner with reasoning

## Platform-Specific Notes

| Platform | Strengths | Avoid |
|----------|----------|-------|
| **Claude** | XML tags for structure, nuanced role descriptions, extended thinking | Over-constraining with rigid rules; Claude performs better with clear intent |
| **GPT-4** | System/user message separation, function calling, "You MUST" directives | Assuming XML tags work; use explicit directives instead |
| **Gemini** | Multimodal prompts, clear section demarcation | Ambiguous section boundaries |

See `references/PLATFORMS.md` for detailed platform optimization guides.

## Reference Files

Load these as needed for deeper guidance:

| File | When to Read |
|------|-------------|
| `references/TECHNIQUES.md` | Full technique catalog with detailed examples |
| `references/EVALUATION.md` | Comprehensive evaluation methodologies and rubrics |
| `references/TEMPLATES.md` | Reusable prompt patterns for common use cases |
| `references/PLATFORMS.md` | Platform-specific optimization (Claude, GPT, Gemini) |
