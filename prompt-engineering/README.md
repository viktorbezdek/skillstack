# Prompt Engineering

> Comprehensive prompt optimization system for LLMs -- design effective AI interactions, evaluate prompt quality, and perform iterative refinement for any LLM platform.

## Overview

Most people interact with LLMs using vague, unstructured prompts and get mediocre results. The gap between a naive prompt and a well-engineered one can mean the difference between useless output and production-quality work. This skill encodes the full discipline of prompt engineering into a systematic framework that transforms how you communicate with AI.

This skill is for anyone who writes prompts -- developers building LLM-powered features, content creators working with AI, product teams designing AI interactions, or power users who want consistently better results. It covers the entire lifecycle from initial design through evaluation and iterative refinement.

Within the SkillStack collection, Prompt Engineering is a foundational meta-skill. It improves the effectiveness of every other skill by teaching you how to communicate intent clearly. It pairs especially well with the Skill Creator skill (which uses prompting principles to build skills) and any domain-specific skill where prompt quality directly affects output quality.

## What's Included

### References
- **EVALUATION.md** -- Comprehensive evaluation methodologies and rubrics for scoring prompt quality
- **PLATFORMS.md** -- Platform-specific optimization guides for Claude, ChatGPT (GPT-4), Gemini, and other LLMs
- **TECHNIQUES.md** -- Full catalog of prompting techniques with detailed examples (role assignment, chain-of-thought, few-shot, etc.)
- **TEMPLATES.md** -- Reusable prompt patterns for research, creative, technical, business, and teaching use cases

### Scripts
- **analyze_structure.py** -- Analyze the structural composition of a prompt (sections, length, technique usage)
- **diff_prompts.py** -- Compare two prompt versions side-by-side to highlight differences and improvements
- **format_prompt.py** -- Auto-format and clean up prompt text for consistency

## Key Features

- **4-D Framework**: Systematic process -- Deconstruct, Diagnose, Develop, Deliver -- for every prompt optimization task
- **Multi-mode operation**: Optimize existing prompts, create new ones from scratch, evaluate quality, or teach techniques
- **7 core techniques**: Role assignment, context layering, chain-of-thought, few-shot examples, task decomposition, constraints, and output specification
- **Evaluation scoring**: Quick 5-dimension scoring (Clarity, Specificity, Completeness, Efficiency, Robustness) plus LLM-as-Judge methodology
- **A/B testing process**: Structured approach for comparing prompt versions across test inputs
- **Platform-aware**: Tailored advice for Claude (XML tags, extended thinking), ChatGPT (system messages, function calling), and Gemini (multimodal)
- **Anti-pattern detection**: Identifies and fixes vague instructions, buried intent, kitchen-sink prompts, missing output specs, and more
- **Context enrichment**: Pulls real organizational context into prompts using available tools and integrations

## Usage Examples

Optimize an existing prompt:
```
Make this prompt better: "Write me a blog post about machine learning"
```

Design a prompt from scratch for a complex task:
```
Create a prompt for analyzing quarterly sales data and generating executive summaries with actionable recommendations.
```

Evaluate prompt quality:
```
Evaluate this system prompt I wrote for our customer support chatbot: [paste prompt]. Score it and tell me what to improve.
```

Compare two prompt versions:
```
I have two versions of my code review prompt. Run them through A/B testing to tell me which performs better and why.
```

Get platform-specific advice:
```
I'm building a prompt for Claude that needs to handle structured data extraction. What Claude-specific techniques should I use?
```

## Quick Start

1. Share the prompt you want to improve, or describe the task you need a prompt for.
2. The skill will automatically select the right mode: Optimize, Design, Evaluate, or Educate.
3. For optimization, the 4-D framework runs: Deconstruct (understand intent) -> Diagnose (score weaknesses) -> Develop (apply techniques) -> Deliver (present improved prompt with explanation).
4. Review the improved prompt, then iterate if needed -- the skill supports multiple refinement rounds.

## Related Skills

- **Skill Creator** -- Uses prompt engineering principles to build Claude Code skills
- **Creative Problem-Solving** -- Generates creative approaches that inform prompt design
- **Systems Thinking** -- Helps structure complex multi-step prompt pipelines

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/prompt-engineering` -- 34 production-grade skills for Claude Code.
