# Prompt Engineering

> **v1.1.16** | Development | 17 iterations

> Systematic prompt optimization for LLMs -- turn vague instructions into precision-engineered prompts that produce reliable, high-quality outputs across Claude, GPT-4, and Gemini.
> Single skill + 4 references + 3 scripts

## The Problem

Most prompts fail not because the model is incapable, but because the instructions are ambiguous, the context is missing, and the output format is left to chance. Teams burn hours on trial-and-error iteration: tweaking a word here, adding a sentence there, running the prompt again, and hoping for better results. Without a systematic method, prompt development is pure guesswork with expensive compute behind it.

Someone finds a prompt that "worked" in a blog post and copies it verbatim. It produces decent results for one input but falls apart on the next three. They add more instructions, making the prompt longer but not better. They try adding "Be concise" and "Be thorough" in the same prompt without noticing the contradiction. When they finally get something acceptable, they cannot explain why it works, so the next team member starts from scratch. Multiply this across a team of five, each independently discovering the same dead ends, and you have weeks of cumulative waste.

The problem compounds across platforms. A prompt tuned for Claude's XML-tag conventions produces garbled output on GPT-4. A GPT-4 prompt that relies on "You MUST" directives feels over-constrained on Claude. Cross-platform prompt migration is treated as an art rather than an engineering discipline, which means every platform switch restarts the iteration cycle from zero. There is no shared vocabulary for what makes a prompt good, no rubric to score one version against another, and no systematic process for closing the gap between "sometimes works" and "reliably delivers."

## Context to Provide

Prompt engineering is a debugging discipline -- the more context you give about what is failing and why, the faster the skill can diagnose the problem and apply the right fix.

**What information to include in your prompt:**
- **The prompt itself** -- always paste the current prompt verbatim. The skill cannot diagnose what it cannot see.
- **What output you are getting** -- describe the failure mode specifically: inconsistent format, wrong tone, missing key information, hallucinated content, too long, too short, fails on certain inputs. Generic "it doesn't work well" produces generic advice.
- **What output you want** -- describe the ideal output in concrete terms, or paste an example of good output if you have one. The skill optimizes toward a target; without one, it improvises.
- **The target platform** -- Claude, GPT-4, Gemini, or other. Platform-specific structural differences (XML tags vs. system/user separation vs. section headers) change the optimization strategy significantly.
- **The audience for the output** -- who will read it? Busy engineers, non-technical stakeholders, customers? Audience calibrates tone, format, and density.
- **Volume and consistency requirements** -- is this prompt run once or thousands of times per day? High-volume prompts need tighter output specifications because format drift compounds.

**What makes results better:**
- Showing actual examples of bad output alongside good output (the contrast is more informative than describing the gap)
- Describing specific inputs that break the prompt (edge cases, unusual phrasing, long inputs)
- Indicating which dimensions matter most: accuracy, tone, format, length, or consistency

**What makes results worse:**
- Describing the problem without pasting the prompt
- Saying "make it better" without specifying what better means
- Providing the prompt without describing what it is used for

**Template prompt (for optimizing an existing prompt):**
```
This prompt gives me inconsistent results -- help me fix it.

Platform: [Claude / GPT-4 / Gemini]
Use case: [what this prompt is for and who sees the output]

Current prompt:
[paste your prompt here]

The problem: [describe what goes wrong -- inconsistent format, wrong tone, misses key content, fails on certain inputs]

Example of bad output: [paste an example or describe what you got]
Example of good output: [paste an example or describe what you want]

Constraints: [length limits, tone requirements, output format requirements, anything the prompt must not do]
```

**Template prompt (for building a new prompt):**
```
I need a prompt for [task description].

Platform: [Claude / GPT-4 / Gemini]
Who will use it: [the role running the prompt]
Who sees the output: [the audience for the output]
Output format: [describe the structure you want -- table, bullets, numbered steps, prose, JSON, etc.]
Key requirements: [2-3 most important things the output must do]
What it must NOT do: [guardrails, off-topic areas, tone restrictions]
Example input: [a sample input the prompt will receive]
```

## The Solution

This plugin provides a structured 4-D methodology -- Deconstruct, Diagnose, Develop, Deliver -- that turns prompt optimization from guesswork into engineering. Instead of random edits, you systematically analyze what a prompt needs to accomplish, score it against five quality dimensions (Clarity, Specificity, Structure, Completeness, Efficiency), select the right techniques from a proven catalog, and produce an optimized version with clear explanations of what changed and why.

The skill operates in four modes depending on your situation: Optimize mode for fixing existing prompts, Interactive Design mode for creating new prompts from scratch, Evaluate mode for scoring and testing prompt quality, and an educational mode for learning the underlying techniques. Each mode follows the same 4-D framework but adjusts depth based on complexity -- simple tasks get a streamlined pass, complex tasks get strategic questions and multi-stage decomposition.

Platform-specific optimization is built in. The skill knows that Claude excels with XML tags and intent-first design, that GPT-4 responds to system/user message separation and explicit directives, and that Gemini works best with multimodal prompts and clear section demarcation. When you migrate a prompt between platforms, it translates the structural patterns rather than just changing words. Three utility scripts support the workflow: structural analysis, version diffing, and format normalization.

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
Help me optimize this prompt. Platform: Claude. Use case: internal knowledge base chatbot that answers HR policy questions.

Current prompt: "You are a helpful HR assistant. Answer questions about company policy based on the documents provided."

The problem: sometimes the bot makes up policies that aren't in the documents, and the format varies -- sometimes bullet points, sometimes paragraphs, sometimes numbered steps. Employees find the inconsistency confusing.

Good output looks like: a short direct answer (1-3 sentences) followed by a citation of the specific policy section.
```

The skill should activate automatically and run a diagnosis of the prompt across five quality dimensions before producing an improved version.

## Quick Start

1. **Install** the plugin using the commands above
2. **Paste an underperforming prompt** and say: `This prompt gives inconsistent results -- help me fix it`
3. The skill **diagnoses** the prompt on five dimensions (Clarity, Specificity, Structure, Completeness, Efficiency) and identifies weaknesses
4. It **applies targeted techniques** (Role Assignment, Few-Shot, Output Specification, etc.) and delivers an optimized version with a brief explanation of what changed
5. **Iterate** by saying: `Can you make the output format stricter?` or `Add chain-of-thought reasoning to this`

---

## System Overview

```
User Request
    │
    ├── Has existing prompt? ──────────── OPTIMIZE MODE
    │                                       │
    ├── Needs new prompt?                   │
    │   ├── Simple task ──── AUTO DESIGN    │
    │   └── Complex task ── INTERACTIVE     │
    │                        DESIGN         │
    ├── Quality assessment? ── EVALUATE     │
    │                          MODE         │
    └── Learning request? ──── EDUCATE      │
                               MODE         │
                                            ▼
                                    ┌───────────────┐
                                    │ 4-D Framework  │
                                    │  Deconstruct   │
                                    │  Diagnose      │
                                    │  Develop  ◄────┼── TECHNIQUES.md
                                    │  Deliver       │     (technique catalog)
                                    └───────┬───────┘
                                            │
                          ┌─────────────────┼─────────────────┐
                          │                 │                   │
                   EVALUATION.md      PLATFORMS.md        TEMPLATES.md
                   (scoring rubrics)  (Claude/GPT/Gemini) (starter prompts)
                          │                 │                   │
                          ▼                 ▼                   ▼
                   ┌──────────────────────────────────────────────┐
                   │              Utility Scripts                  │
                   │  analyze_structure.py  diff_prompts.py       │
                   │  format_prompt.py                            │
                   └──────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `prompt-engineering` | skill | Core 4-D methodology with four operating modes, three optimization patterns, evaluation framework, and platform notes |
| `TECHNIQUES.md` | reference | Full catalog of prompting techniques with detailed examples |
| `EVALUATION.md` | reference | Comprehensive evaluation methodology, scoring rubrics, and A/B testing process |
| `TEMPLATES.md` | reference | Battle-tested prompt templates across seven domains |
| `PLATFORMS.md` | reference | Platform-specific optimization for Claude, GPT-4, and Gemini |
| `analyze_structure.py` | script | Static analysis of prompt structure -- detects role, context, task, format, and examples sections |
| `diff_prompts.py` | script | Side-by-side structural diff of two prompt versions for tracking iterations |
| `format_prompt.py` | script | Normalizes prompt formatting into consistent structure (XML, Markdown, or plain) |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### prompt-engineering (skill)

**What it does:** Activates when you need to design, optimize, evaluate, or learn about prompts for any LLM platform. The skill automatically selects the right mode -- Optimize for fixing existing prompts, Interactive Design for building new ones, Evaluate for scoring quality, or Educate for learning techniques. Every task flows through the 4-D framework (Deconstruct, Diagnose, Develop, Deliver).

**Input -> Output:** A prompt (or a description of what you need) -> An optimized prompt with explanation, quality scores, technique rationale, and platform-specific advice.

**When to use:** You have a prompt that produces inconsistent results. You need to build a new prompt from scratch. You want to compare two prompt versions. You need to migrate a prompt between LLM platforms. You want to learn which prompting techniques apply to your situation.

**When NOT to use:** Building MCP servers or Claude Code plugins (use mcp-server or skill-creator). Creating few-shot examples from scratch (use Example Design). Generating the actual content a prompt would produce (this skill optimizes the prompt, not the output).

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
| `TECHNIQUES.md` | Complete prompting technique catalog -- Role Assignment, Context Layering, Chain-of-Thought, Few-Shot, Task Decomposition, Constraints, Output Specification |
| `EVALUATION.md` | Systematic evaluation methodology -- performance metrics, quality metrics, A/B testing, LLM-as-Judge scoring |
| `TEMPLATES.md` | Ready-to-use prompt templates for Analysis & Research, Creative Content, Technical Tasks, Business & Strategy, Education & Training, Data Processing, Decision Support |
| `PLATFORMS.md` | Platform-specific optimization guides for ChatGPT/GPT-4, Claude, and Gemini with structural preferences and concrete examples |

#### analyze_structure.py (script)

**CLI:** `python scripts/analyze_structure.py < prompt.txt`
**What it produces:** A structural analysis report showing which prompt components are present (role, context, task, format, examples) and which are missing.
**Typical workflow:** Run before optimization to baseline the prompt's structure, then run after to verify improvements.

#### diff_prompts.py (script)

**CLI:** `python scripts/diff_prompts.py prompt_v1.txt prompt_v2.txt`
**What it produces:** A side-by-side structural diff showing what changed between two prompt versions -- useful for tracking iteration progress.
**Typical workflow:** After the skill produces an optimized version, diff it against the original to confirm changes are targeted and intentional.

#### format_prompt.py (script)

**CLI:** `python scripts/format_prompt.py --style xml < prompt.txt`
**What it produces:** A reformatted prompt normalized to consistent structure (XML, Markdown, or plain style).
**Typical workflow:** When adopting a team-wide prompt style convention or preparing prompts for a specific platform.

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't produce consistent results) | Good (specific, produces reliable output) |
|---|---|
| "Write a blog post about AI" | "Write a 1200-word blog post for technical PMs explaining how RAG pipelines reduce hallucination in customer-facing chatbots. Include 3 concrete examples and a comparison table." |
| "Summarize this document" | "Summarize this quarterly report in 3 bullet points: key metric changes, biggest risk, and recommended action. Use the format: Metric: [change]. Risk: [description]. Action: [recommendation]." |
| "Help me with this code" | "Review this Python function for edge cases in the date parsing logic. Focus on timezone handling and leap year boundaries. Output a table: Edge Case / Current Behavior / Fix." |
| "Be a helpful assistant" | "You are a senior DevOps engineer with 10 years of Kubernetes experience. Diagnose this pod crash loop using the logs below. Structure your response as: Root Cause, Evidence, Fix, Prevention." |
| "Analyze the data" | "Analyze these 500 NPS responses. Stage 1: categorize by theme. Stage 2: score sentiment per theme (-5 to +5). Stage 3: rank themes by urgency with one recommended action each." |

### Structured Prompt Templates

**For optimizing an existing prompt:**
```
This prompt gives [describe the problem -- inconsistent results, wrong format, misses key points]:

[paste your prompt]

Help me fix it. The output should be [describe what good output looks like].
```

**For building a new prompt from scratch:**
```
I need a prompt for [task description]. The audience is [who will see the output].
The output should be structured as [format]. The key constraints are [list 2-3].
```

**For cross-platform migration:**
```
I have this [Claude/GPT-4/Gemini] prompt that works well:

[paste prompt]

I need it to work on [target platform] without losing quality. What structural
changes are needed?
```

**For A/B testing prompt versions:**
```
I have two prompts for [same task]. Help me test which one produces better results.

Version A: [paste]
Version B: [paste]

Test criteria: [accuracy, tone, completeness, format consistency -- pick what matters]
```

### Prompt Anti-Patterns

- **The kitchen sink prompt:** Adding every possible instruction to a prompt without prioritizing. The model drowns in contradictory or irrelevant directives and produces mediocre output on everything instead of excellent output on what matters. Fix: identify the 3 most important requirements and cut the rest.
- **The copycat prompt:** Grabbing a prompt from a blog post or ChatGPT gallery without understanding why it works. When your use case differs even slightly, the prompt fails and you cannot debug it because you never understood the design. Fix: use the 4-D framework to analyze why a template works before adapting it.
- **The platform-blind prompt:** Writing a prompt that works on one LLM and assuming it transfers. Claude's XML tags confuse GPT-4; GPT-4's "You MUST" directives over-constrain Claude; neither format works well on Gemini. Fix: use the platform-specific translation guide to convert structural patterns.
- **The format-free prompt:** Never specifying output structure and hoping the model guesses correctly. Each run produces a different format, making downstream processing impossible. Fix: add an explicit Output Specification section with headers, structure, and length requirements.
- **The contradiction prompt:** Including "Be concise" and "Be thorough" in the same prompt, or asking for "creative" output with "strict formatting." The model cannot satisfy both and produces inconsistent results as it oscillates between the contradictory instructions. Fix: resolve trade-offs explicitly ("Prioritize completeness over brevity" or "Be thorough on methodology, concise on examples").

## Real-World Walkthrough

You are building an AI-powered code review assistant for your engineering team. The current prompt is a single paragraph that reads: "Review this code and find bugs. Also suggest improvements and check for security issues." It works sometimes, but the output varies wildly -- some reviews are thorough, others miss obvious issues, and the format is different every time.

You open Claude Code and say:

```
This code review prompt gives inconsistent results. Some reviews are great, others miss obvious bugs. Help me fix it.
```

You paste the prompt. The skill enters **Optimize mode** and begins with the **Deconstruct** phase. It identifies that the actual goal is a structured, repeatable code review that catches bugs, security issues, and maintainability problems. The unstated assumptions include: the reviewer should prioritize by severity, the output should be scannable by busy engineers, and the review should cover both line-level issues and architectural concerns.

The **Diagnose** phase scores the prompt across five dimensions:
- **Clarity:** 2/5 -- "find bugs" is vague; what counts as a bug? Logic errors? Performance issues? Type mismatches?
- **Specificity:** 1/5 -- no output format defined, no severity levels, no categories
- **Structure:** 2/5 -- everything crammed into one sentence with no logical organization
- **Completeness:** 2/5 -- no role, no context about the codebase or language, no examples of good reviews
- **Efficiency:** 3/5 -- at least it is short, though brevity is not helping here

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

The skill references the platform-specific guide and translates the Claude-optimized XML tags into GPT-4's preferred system/user message separation pattern, adjusting directive language from intent-based ("focus on security-critical findings first") to explicit ("You MUST categorize every finding by severity before presenting it"). You now have two platform-native prompts that produce equivalent results.

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

### Scenario 5: Teaching a team prompt engineering fundamentals

**Context:** Your engineering team is starting to build LLM-powered features but nobody has formal prompt engineering knowledge. You need to bring everyone up to speed quickly.

**You say:** `Teach me the most important prompt engineering techniques. I'm building LLM features and my team needs to understand how to write good prompts.`

**The skill provides:**
- Educate mode walkthrough of the core techniques: Role Assignment, Context Layering, Chain-of-Thought, Few-Shot, Output Specification
- Concrete before/after examples for each technique showing the difference between a naive prompt and an optimized one
- The 4-D framework explained as a repeatable process anyone can follow

**You end up with:** A working mental model of prompt engineering that your team can apply immediately, plus the technique catalog as an ongoing reference.

---

## Decision Logic

**How does the skill choose which mode to use?**

The skill examines your request and routes to the appropriate mode:
- If you paste an existing prompt and describe a problem with it, **Optimize mode** activates. The 4-D framework diagnoses the prompt and applies targeted fixes.
- If you describe what you need without an existing prompt, the skill checks complexity. Simple, well-defined tasks go to **Auto Design** (the skill builds the prompt directly). Complex or ambiguous tasks go to **Interactive Design** (the skill asks 2-3 strategic questions first).
- If you explicitly ask to evaluate, score, test, or compare prompts, **Evaluate mode** activates with scoring rubrics and A/B testing.
- If you ask to learn or understand techniques, **Educate mode** activates with explanations and examples.

**When does the skill load references?**

The SKILL.md body contains the complete 4-D methodology, three optimization patterns, a quick evaluation framework, and platform notes -- enough for 80% of tasks. References load on demand:
- **TECHNIQUES.md** loads when the Develop phase needs detailed technique examples beyond the SKILL.md body
- **EVALUATION.md** loads when you request systematic testing or A/B comparisons
- **TEMPLATES.md** loads when you need a starting-point prompt for a common use case
- **PLATFORMS.md** loads when cross-platform optimization is needed

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Prompt is too vague to diagnose | The skill cannot identify a specific weakness because the prompt has no clear goal | Provide context: what the prompt is for, who sees the output, and what "good" looks like. The skill will ask clarifying questions in Interactive Design mode. |
| Platform-specific features have no equivalent | A Claude feature (e.g., extended thinking) has no direct GPT-4 equivalent and the translated prompt loses capability | The skill will flag features with no equivalent and suggest workaround patterns. Accept that some cross-platform translations involve trade-offs. |
| Over-optimized prompt is too rigid | After multiple optimization rounds, the prompt is so constrained that it cannot handle input variations | Reduce constraints to the 3-5 most important ones. Use the Diagnose phase's Efficiency dimension to identify tokens that are not earning their keep. |
| Few-shot examples bias the output | The examples are so specific that the model mimics them literally instead of generalizing the pattern | Diversify examples: use 3 examples that vary in content, length, and structure while sharing the same format pattern. The skill's technique guidance covers this. |
| Conflicting requirements produce oscillating output | The prompt asks for contradictory things (concise + thorough, creative + structured) and each run picks a different interpretation | The Diagnose phase catches contradictions. Resolve by making one requirement primary and the other secondary, or by splitting into stages. |

## Ideal For

- **Engineers building LLM-powered features** -- the systematic methodology prevents the trial-and-error spiral that wastes days of development time
- **Product managers writing prompts for AI assistants** -- Interactive Design mode asks the right strategic questions and produces production-ready prompts without requiring prompt engineering expertise
- **Teams maintaining prompts across multiple LLM platforms** -- platform-specific translation guides eliminate the "works on Claude, breaks on GPT-4" problem
- **Anyone evaluating prompt quality** -- the five-dimension scoring framework and A/B testing process replace gut feeling with measurable metrics
- **Technical writers and content teams** -- the template library and Output Specification technique produce consistent, structured content at scale

## Not For

- **Building MCP servers or Claude Code plugins** -- use [mcp-server](../mcp-server/) for MCP development and [skill-creator](../skill-creator/) for skill authoring
- **Creating few-shot examples from scratch** -- use [Example Design](../example-design/) for systematic example creation; this skill will reference it when the Few-Shot technique is selected
- **Generating creative content directly** -- this skill optimizes the prompt, not the content itself. Use [Creative Problem Solving](../creative-problem-solving/) for ideation workflows
- **Fine-tuning or training models** -- prompt engineering operates at inference time. For training-time optimization, you need different tools entirely.

## Related Plugins

- **[Skill Creator](../skill-creator/)** -- Create Claude Code skills with philosophy-first design and progressive disclosure architecture
- **[Outcome Orientation](../outcome-orientation/)** -- Define measurable outcomes to evaluate whether your prompt changes actually improve results
- **[Example Design](../example-design/)** -- Design effective few-shot examples for prompts that need input/output demonstrations
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough approaches when standard prompting techniques are not producing the results you need
- **[Context Fundamentals](../context-fundamentals/)** -- Understand how LLM context windows work to write prompts that use tokens efficiently

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
