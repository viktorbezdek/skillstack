# Prompt Engineering

> **v1.1.15** | Development | 17 iterations

> Systematic prompt optimization for LLMs -- turn vague instructions into precision-engineered prompts that produce reliable, high-quality outputs across Claude, GPT-4, and Gemini.

## The Problem

Most prompts fail not because the model is incapable, but because the instructions are ambiguous, the context is missing, and the output format is left to chance. Teams burn hours on trial-and-error iteration: tweaking a word here, adding a sentence there, running the prompt again, and hoping for better results. Without a systematic method, prompt development looks like this:

Someone finds a prompt that "worked" in a blog post and copies it verbatim. It produces decent results for one input but falls apart on the next three. They add more instructions, making the prompt longer but not better. They try adding "Be concise" and "Be thorough" in the same prompt without noticing the contradiction. When they finally get something acceptable, they cannot explain why it works, so the next team member starts from scratch.

The problem gets worse across platforms. A prompt tuned for Claude's XML-tag conventions produces garbled output on GPT-4. A GPT-4 prompt that relies on "You MUST" directives feels over-constrained on Claude. Cross-platform prompt migration is treated as an art rather than an engineering discipline, which means every platform switch restarts the iteration cycle from zero.

## The Solution

This plugin provides a structured 4-D methodology -- Deconstruct, Diagnose, Develop, Deliver -- that turns prompt optimization from guesswork into engineering. Instead of random edits, you systematically analyze what a prompt needs to accomplish, score it against five quality dimensions (Clarity, Specificity, Structure, Completeness, Efficiency), select the right techniques from a proven catalog, and produce an optimized version with clear explanations of what changed and why.

The skill operates in four modes depending on your situation: Optimize mode for fixing existing prompts, Interactive Design mode for creating new prompts from scratch, Evaluate mode for scoring and testing prompt quality, and an educational mode for learning the underlying techniques. Each mode follows the same 4-D framework but adjusts depth based on complexity -- simple tasks get a streamlined pass, complex tasks get strategic questions and multi-stage decomposition.

Platform-specific optimization is built in. The skill knows that Claude excels with XML tags and intent-first design, that GPT-4 responds to system/user message separation and explicit directives, and that Gemini works best with multimodal prompts and clear section demarcation. When you migrate a prompt between platforms, it translates the structural patterns rather than just changing words.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Trial-and-error iteration with no systematic method -- hours of tweaking with unpredictable results | Structured 4-D methodology: diagnose the problem, apply the right technique, deliver with explanation |
| Prompts that work 60% of the time and produce garbage the rest | Five-dimension quality scoring identifies exactly why output is inconsistent, then targeted fixes close the gaps |
| Copying prompts from blog posts without understanding why they work | Technique catalog (Role Assignment, Chain-of-Thought, Few-Shot, etc.) with clear guidelines on when each applies |
| Cross-platform migration restarts prompt development from scratch | Platform-specific translation guides convert structural patterns between Claude, GPT-4, and Gemini |
| No way to compare prompt versions or track what improved | Structural diffing script shows exactly what changed between revisions and whether changes helped |
| Output format left to chance -- the LLM decides how to structure its response | Output Specification technique defines exact structure, headers, length, and style expectations |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install prompt-engineering@skillstack
```

### Verify installation

After installing, test with:

```
Help me optimize this prompt: "Write a good blog post about AI"
```

The skill should activate automatically and run a diagnosis of the prompt across five quality dimensions before producing an improved version.

## Quick Start

1. **Install** the plugin using the commands above
2. **Paste an underperforming prompt** and say: `This prompt gives inconsistent results -- help me fix it`
3. The skill **diagnoses** the prompt on five dimensions (Clarity, Specificity, Structure, Completeness, Efficiency) and identifies weaknesses
4. It **applies targeted techniques** (Role Assignment, Few-Shot, Output Specification, etc.) and delivers an optimized version with a brief explanation of what changed
5. **Iterate** by saying: `Can you make the output format stricter?` or `Add chain-of-thought reasoning to this`

## What's Inside

This is a single-skill plugin with a rich reference layer and three utility scripts.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core 4-D methodology, decision flow, three optimization patterns (Role+Context+Task+Format, Few-Shot+CoT, Multi-Stage Pipeline), evaluation framework, anti-patterns, and platform notes |
| `references/TECHNIQUES.md` | Full catalog of prompting techniques with detailed examples -- Role Assignment, Context Layering, Chain-of-Thought, Few-Shot, Task Decomposition, Constraints, Output Specification |
| `references/EVALUATION.md` | Comprehensive evaluation methodology -- performance metrics (accuracy, relevance, completeness, consistency), quality metrics, and systematic testing procedures |
| `references/TEMPLATES.md` | Battle-tested prompt templates for Analysis & Research, Creative Content, Technical Tasks, Business & Strategy, Education & Training, Data Processing, and Decision Support |
| `references/PLATFORMS.md` | Platform-specific optimization for ChatGPT/GPT-4, Claude, and Gemini with structural preferences, special features, and concrete examples |
| `scripts/analyze_structure.py` | Static analysis of prompt structure -- detects presence of role, context, task, format, and examples sections |
| `scripts/diff_prompts.py` | Side-by-side structural diff of two prompt versions for tracking iterations during refinement |
| `scripts/format_prompt.py` | Normalizes prompt formatting into consistent structure (XML, Markdown, or plain style) |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### prompt-engineering

**What it does:** Activates when you need to design, optimize, evaluate, or learn about prompts for any LLM platform. The skill automatically selects the right mode -- Optimize for fixing existing prompts, Interactive Design for building new ones, Evaluate for scoring quality, or Educate for learning techniques. It applies the 4-D framework (Deconstruct, Diagnose, Develop, Deliver) to every task.

**Try these prompts:**

```
This prompt gives me different results every time -- help me make it consistent
```

```
Write me a system prompt for an internal customer support chatbot that handles refund requests
```

```
Score this prompt on a scale of 1-5 and tell me what's wrong with it: "Summarize the document and highlight key points"
```

```
My Claude prompt uses XML tags but I need it to work on GPT-4 too -- how do I adapt it?
```

```
I need a prompt that walks the model through complex financial analysis step by step before giving a recommendation
```

```
Compare these two prompt versions and tell me which one is better for generating product descriptions
```

**Key references:**

| Reference | Topic |
|---|---|
| `TECHNIQUES.md` | Complete prompting technique catalog with examples for each technique |
| `EVALUATION.md` | Systematic evaluation methodology, scoring rubrics, and A/B testing process |
| `TEMPLATES.md` | Ready-to-use prompt templates across seven domains |
| `PLATFORMS.md` | Platform-specific optimization guides for Claude, GPT-4, and Gemini |

## Real-World Walkthrough

You are building an AI-powered code review assistant for your engineering team. The current prompt is a single paragraph that reads: "Review this code and find bugs. Also suggest improvements and check for security issues." It works sometimes, but the output varies wildly -- some reviews are thorough, others miss obvious issues, and the format is different every time.

You open Claude Code and say:

```
This code review prompt gives inconsistent results. Some reviews are great, others miss obvious bugs. Help me fix it.
```

You paste the prompt. The skill enters **Optimize mode** and begins with the **Deconstruct** phase. It identifies that the actual goal is a structured, repeatable code review that catches bugs, security issues, and maintainability problems. The unstated assumptions include: the reviewer should prioritize by severity, the output should be scannable by busy engineers, and the review should cover both line-level issues and architectural concerns.

The **Diagnose** phase scores the prompt:
- **Clarity:** 2/5 -- "find bugs" is vague; what counts as a bug? Logic errors? Performance issues? Type mismatches?
- **Specificity:** 1/5 -- no output format defined, no severity levels, no categories
- **Structure:** 2/5 -- everything crammed into one sentence
- **Completeness:** 2/5 -- no role, no context about the codebase or language, no examples of good reviews
- **Efficiency:** 3/5 -- at least it's short, though brevity isn't helping here

The skill moves to the **Develop** phase and selects techniques based on the diagnosis. It applies **Role Assignment** to give the model a specific identity ("Senior software engineer with 10+ years of experience conducting code reviews at FAANG companies"). It uses **Context Layering** to structure background information (language, framework, team standards). It applies **Output Specification** to define a consistent format with severity levels (Critical, Warning, Suggestion), categories (Bug, Security, Performance, Maintainability), and a summary section. Finally, it adds a **Few-Shot Example** showing one well-formatted review finding so the model knows exactly what each entry should look like.

The **Deliver** phase presents the optimized prompt in a code block. It is structured as Role, Context, Task, Categories, Output Format, and Example -- following the Role+Context+Task+Format pattern. The skill explains the three key changes: (1) the role assignment focuses the model's expertise, (2) the output specification eliminates format inconsistency, and (3) the severity levels help engineers prioritize which findings to address first.

You test the new prompt against three code samples: a simple utility function, a complex API endpoint with authentication, and a database migration script. The output is now consistent -- every review follows the same format, categorizes findings by type and severity, and includes a summary with the total finding count. The complex API endpoint review correctly identifies an SQL injection risk that the original prompt missed entirely.

But you notice the reviews are verbose. You say:

```
The reviews are too long for quick scanning. Can you make the individual findings more concise -- one line per finding with a separate details section?
```

The skill iterates on the output specification, restructuring it into a compact summary table (one row per finding: Severity | Category | Line | One-line description) followed by an expandable details section. You run the `diff_prompts.py` script to compare the two versions structurally -- the diff shows that the output format section changed but the role, context, and task sections remained identical, confirming you only changed what needed changing.

After two iterations, you have a production-ready code review prompt that produces consistent, scannable output across any codebase. You then ask:

```
I need this to work on GPT-4 too -- my team uses both Claude and ChatGPT
```

The skill references the platform-specific guide and translates the Claude-optimized XML tags into GPT-4's preferred system/user message separation pattern, adjusting directive language from intent-based ("focus on security-critical findings first") to explicit ("You MUST categorize every finding by severity before presenting it").

## Usage Scenarios

### Scenario 1: Fixing a flaky customer support prompt

**Context:** You manage an AI-powered customer support system. The prompt generates helpful responses 70% of the time, but occasionally produces overly casual tone or misses the customer's actual question.

**You say:** `This customer support prompt is inconsistent -- sometimes the tone is too casual and it misses what the customer is actually asking. Here's the prompt: [paste]`

**The skill provides:**
- Five-dimension diagnosis identifying that the prompt lacks tone constraints and has no instruction to paraphrase the customer's question before responding
- Role Assignment technique to set a specific support persona with tone guidelines
- Output Specification requiring the response to start with a paraphrase of the customer's issue
- Constraints & Guardrails defining what tone is acceptable and what is not

**You end up with:** An optimized prompt that consistently produces professional, on-topic responses by anchoring every reply to a restated understanding of the customer's question.

### Scenario 2: Building a data analysis prompt from scratch

**Context:** You are a product manager who needs an LLM to analyze user feedback surveys and extract actionable insights, but you have never written a serious prompt before.

**You say:** `I need a prompt that can analyze user survey responses and tell me what to fix in my product. I have about 500 free-text responses.`

**The skill provides:**
- Interactive Design mode with 2-3 strategic questions (What product? What decisions will this inform? What format does your team consume?)
- A Multi-Stage Pipeline prompt: Stage 1 categorizes responses by theme, Stage 2 quantifies sentiment per theme, Stage 3 produces prioritized recommendations
- Few-Shot examples showing how one survey response gets categorized and scored

**You end up with:** A three-stage analysis prompt that transforms raw survey text into a prioritized action list, ready to paste into a team document.

### Scenario 3: A/B testing prompt versions for content generation

**Context:** Your marketing team has two candidate prompts for generating product descriptions. Neither team member can agree on which is better, and they have been going back and forth based on gut feeling.

**You say:** `We have two prompts for generating product descriptions. Help me test which one actually produces better results.`

**The skill provides:**
- A structured A/B testing process: 5 test products covering simple, complex, and edge cases
- Blind LLM-as-Judge evaluation scoring both outputs on accuracy, tone, completeness, and persuasiveness
- A winner declaration with dimension-by-dimension reasoning

**You end up with:** An evidence-based recommendation with scores, not opinions -- and a reusable testing template for future prompt comparisons.

### Scenario 4: Migrating a Claude prompt to GPT-4

**Context:** Your team standardized on Claude for prompt development but a client requires GPT-4 compatibility. The prompts use Claude-specific XML tags and nuanced role descriptions.

**You say:** `I have 3 Claude prompts that use XML tags and extended thinking. I need them to work on GPT-4 without losing quality.`

**The skill provides:**
- Platform-specific translation mapping XML tags to GPT-4 system/user separation
- Directive style conversion from intent-based to explicit "You MUST" format
- Identification of features with no direct equivalent (extended thinking) and workaround patterns

**You end up with:** Three GPT-4-compatible prompts that preserve the original behavior using platform-native conventions, plus notes on where behavior may differ.

## Ideal For

- **Engineers building LLM-powered features** -- the systematic methodology prevents the trial-and-error spiral that wastes days of development time
- **Product managers writing prompts for AI assistants** -- Interactive Design mode asks the right strategic questions and produces production-ready prompts without requiring prompt engineering expertise
- **Teams maintaining prompts across multiple LLM platforms** -- platform-specific translation guides eliminate the "works on Claude, breaks on GPT-4" problem
- **Anyone evaluating prompt quality** -- the five-dimension scoring framework and A/B testing process replace gut feeling with measurable metrics

## Not For

- **Building MCP servers or Claude Code plugins** -- use [mcp-server](../mcp-server/) for MCP development and [skill-forge](../skill-forge/) for skill authoring
- **Creating few-shot examples from scratch** -- use [Example Design](../example-design/) for systematic example creation; this skill will reference it when Few-Shot technique is selected
- **Generating creative content directly** -- this skill optimizes the prompt, not the content itself. Use [Creative Problem Solving](../creative-problem-solving/) for ideation workflows

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through four reference files. The SKILL.md body contains the complete 4-D methodology, three optimization patterns, a quick evaluation framework, and platform notes -- enough for 80% of prompt optimization tasks. When deeper guidance is needed, the skill loads references on demand:

- **TECHNIQUES.md** is loaded when the Develop phase needs detailed technique examples beyond what the SKILL.md body provides
- **EVALUATION.md** is loaded when the user requests systematic testing or A/B comparisons
- **TEMPLATES.md** is loaded when the user needs a starting-point prompt for a common use case
- **PLATFORMS.md** is loaded when cross-platform optimization is needed

Three Python utility scripts support the workflow: `analyze_structure.py` for static analysis of prompt components, `diff_prompts.py` for tracking structural changes between prompt versions, and `format_prompt.py` for normalizing prompt formatting across XML, Markdown, and plain styles.

## Related Plugins

- **[Skill Creator](../skill-forge/)** -- Create Claude Code skills with philosophy-first design and progressive disclosure architecture
- **[Outcome Orientation](../outcome-orientation/)** -- Define measurable outcomes to evaluate whether your prompt changes actually improve results
- **[Example Design](../example-design/)** -- Design effective few-shot examples for prompts that need input/output demonstrations
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough approaches when standard prompting techniques are not producing the results you need
- **[Context Fundamentals](../context-fundamentals/)** -- Understand how LLM context windows work to write prompts that use tokens efficiently

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
