# Prompt Engineering

> **v1.1.15** | Development | 17 iterations

Comprehensive prompt optimization system for LLMs. Design effective AI interactions, evaluate prompt quality, and perform iterative refinement for any LLM platform.

## What Problem Does This Solve

Most prompts fail not because the LLM is incapable, but because the instruction is ambiguous, missing context, or specifying the wrong output format. Engineers and product teams waste hours iterating on prompts with no systematic method, copying examples that worked elsewhere without understanding why. This skill provides a structured 4-D methodology (Deconstruct, Diagnose, Develop, Deliver) for designing prompts that produce reliable, high-quality outputs across any LLM platform.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "This prompt gives inconsistent results — help me fix it" | OPTIMIZE mode: diagnosis across Clarity, Specificity, Structure, Completeness, and Efficiency dimensions, then targeted improvements |
| "Write me a system prompt for a customer support agent" | INTERACTIVE DESIGN mode: 2-3 strategic questions to gather context, then a complete Role+Context+Task+Format structured prompt |
| "Is this prompt good? Score it for me" | EVALUATE mode: 1-5 scoring on 5 dimensions with an LLM-as-Judge template and specific improvement suggestions |
| "My prompt works on Claude but not on GPT-4" | Platform-specific guidance for Claude (XML tags, intent-first), GPT-4 (system/user separation, "You MUST" directives), and Gemini |
| "I need a prompt that reasons through complex decisions step by step" | Chain-of-Thought + Few-Shot pattern with reasoning examples and multi-stage pipeline decomposition |
| "Help me A/B test two versions of this prompt" | A/B testing process: define test inputs, run blind evaluation, score on dimensions, declare winner with reasoning |

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
Use the prompt-engineering skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `prompts`
- `llm`
- `optimization`
- `evaluation`

## What's Inside

- **Decision Flow** -- Routes incoming requests to the correct mode: Optimize, Auto Design, Interactive Design, Evaluate, or Educate based on what the user brings.
- **Core Process: The 4-D Framework** -- Four-phase methodology (Deconstruct, Diagnose, Develop, Deliver) applied to every prompt optimization task.
- **Optimization Patterns** -- Three reusable prompt structures: Role+Context+Task+Format (80% of cases), Few-Shot+Chain-of-Thought (format + reasoning), and Multi-Stage Pipeline (complex decomposed tasks).
- **Context Enrichment** -- Guidance for grounding prompts in real organizational context using connected tools (Google Drive, Asana, Slack, etc.) when users reference internal information.
- **Evaluation Framework** -- Quick 1-5 scoring rubric across five dimensions, LLM-as-Judge evaluation template, and a structured A/B testing process.
- **Platform-Specific Notes** -- Key behavioral differences between Claude, GPT-4, and Gemini with concrete prompting adjustments for each.
- **Templates** -- Reusable prompt patterns for Research & Analysis, Creative & Content, Technical & Code, Business & Strategy, and Teaching & Explanation use cases.

## Key Capabilities

- **Clarity**
- **Specificity**
- **Structure**
- **Completeness**
- **Efficiency**
- **Claude**

## Version History

- `1.1.15` fix(meta): optimize descriptions for prompt-engineering and skill-creator (a9056e6)
- `1.1.14` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.13` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.12` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.11` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.10` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.9` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.8` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.7` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.1.6` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
