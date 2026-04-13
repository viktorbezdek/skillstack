# Prompt Engineering

> **v1.1.15** | Development | 17 iterations

Comprehensive prompt optimization system for LLMs. Design effective AI interactions, evaluate prompt quality, and perform iterative refinement for any LLM platform.

## What Problem Does This Solve

Most prompts fail not because the LLM is incapable, but because the instruction is vague, the context is missing, or the output format is left to chance. Engineers and product teams burn hours iterating without a systematic method -- copying prompts that worked somewhere else without understanding why they worked. Different LLM platforms respond to different prompting styles, but most people use a single approach everywhere. This skill provides a structured 4-D methodology (Deconstruct, Diagnose, Develop, Deliver) for designing prompts that produce reliable, high-quality outputs across Claude, GPT-4, and Gemini.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "This prompt gives inconsistent results -- help me fix it" | OPTIMIZE mode: diagnosis across five dimensions (Clarity, Specificity, Structure, Completeness, Efficiency), then targeted technique application |
| "Write me a system prompt for a customer support agent" | INTERACTIVE DESIGN mode: 2-3 strategic questions to gather context, then a complete Role+Context+Task+Format structured prompt |
| "Is this prompt good? Score it for me" | EVALUATE mode: 1-5 scoring on five dimensions, an LLM-as-Judge evaluation template, and specific improvement suggestions |
| "My prompt works on Claude but not on GPT-4" | Platform-specific adjustment guidance -- Claude (XML tags, intent-first), GPT-4 (system/user separation, explicit directives), Gemini (multimodal, section demarcation) |
| "I need a prompt that reasons through complex decisions step by step" | Chain-of-Thought + Few-Shot combined pattern with reasoning examples and Multi-Stage Pipeline decomposition |

## When NOT to Use This Skill

- Building MCP servers -- use [mcp-server](../mcp-server/) instead
- Creating Claude Code skills -- use [skill-creator](../skill-creator/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install prompt-engineering@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the prompt-engineering skill to optimize my API extraction prompt
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `prompt engineering`
- `prompt design`
- `prompt optimization`
- `system prompt`
- `LLM optimization`

## What's Inside

This is a single-skill plugin with a rich reference layer.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core 4-D methodology, decision flow, three optimization patterns, evaluation framework, anti-patterns, and platform notes |
| `references/TECHNIQUES.md` | Full catalog of prompting techniques with detailed examples -- Role Assignment, Context Layering, Chain-of-Thought, Few-Shot, Task Decomposition, Constraints, Output Specification |
| `references/EVALUATION.md` | Comprehensive evaluation methodology -- performance metrics (accuracy, relevance, completeness, consistency), quality metrics, and systematic testing procedures |
| `references/TEMPLATES.md` | Battle-tested prompt templates for Analysis & Research, Creative Content, Technical Tasks, Business & Strategy, Education & Training, Data Processing, and Decision Support |
| `references/PLATFORMS.md` | Platform-specific optimization for ChatGPT/GPT-4, Claude, and Gemini with structural preferences, special features, and concrete examples |
| `scripts/analyze_structure.py` | Static analysis of prompt structure -- detects presence of role, context, task, format, and examples sections |
| `scripts/diff_prompts.py` | Side-by-side structural diff of two prompt versions for tracking iterations during refinement |
| `scripts/format_prompt.py` | Normalizes prompt formatting into consistent structure (XML, Markdown, or plain style) |

## Usage Scenarios

**Scenario 1 -- Fixing an inconsistent prompt.** You have a prompt that produces great results 60% of the time and garbage the rest. The skill runs the Diagnose phase, scoring the prompt on five dimensions. It identifies that the prompt lacks output specification and has contradicting requirements, then applies the Role+Context+Task+Format pattern to produce a version that constrains the output reliably.

**Scenario 2 -- Creating a prompt for a new use case.** You need a system prompt for an internal knowledge-base assistant. The skill enters Interactive Design mode, asks 2-3 strategic questions (audience, tone, failure modes), then produces a complete prompt using Context Layering and Constraints techniques, enriched with your organizational context from connected tools.

**Scenario 3 -- A/B testing prompt versions.** You have two candidate prompts for a content generation task. The skill defines 3-5 test inputs covering typical, edge, and stress cases, runs both prompts against them, applies blind LLM-as-Judge evaluation, and declares a winner with dimension scores.

**Scenario 4 -- Cross-platform migration.** Your Claude prompt needs to work on GPT-4 as well. The skill identifies Claude-specific patterns (XML tags, nuanced role descriptions) and translates them to GPT-4 equivalents (system/user message separation, explicit "You MUST" directives) using the PLATFORMS.md reference.

**Scenario 5 -- Iterating with structural diffing.** You are on your third revision of a complex prompt. The `diff_prompts.py` script shows structural changes between versions -- added sections, changed word counts, new constraints -- so you can track what actually improved and what regressed.

## Related Skills

- **[Skill Creator](../skill-creator/)** -- Create Claude Code skills with philosophy-first design and progressive disclosure architecture.
- **[Outcome Orientation](../outcome-orientation/)** -- Define measurable outcomes to evaluate whether your prompt changes actually improve results.
- **[Example Design](../example-design/)** -- Design effective few-shot examples for prompts that need input/output demonstrations.
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough approaches when standard prompting techniques are not producing the results you need.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 52 production-grade plugins for Claude Code.
