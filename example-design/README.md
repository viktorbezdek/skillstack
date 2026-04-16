# Example Design

> **v1.0.10** | Documentation | 11 iterations

> Design code examples, tutorials, and runnable samples that actually teach -- with progressive complexity, realistic naming, and copy-paste reliability.

## The Problem

Most code examples fail at their primary job: teaching. They use `foo` and `bar` as variable names, omit imports, skip error handling, and present a wall of uncommented code that the reader must reverse-engineer. The result is that developers copy-paste examples, discover they don't run, spend 20 minutes fixing missing dependencies, and still don't understand the concept the example was supposed to demonstrate.

The problem is worse at scale. A library with 50 API methods needs 50+ examples, each at multiple complexity levels (minimal, configured, production-ready). Without a framework, example quality varies wildly across the documentation: some are runnable and well-commented, others are pseudocode fragments that have never been tested. Tutorials jump from trivial to advanced without intermediate steps, losing readers who needed the middle complexity level. Quickstart guides assume knowledge they don't teach, creating a gap between "hello world" and "real project" that new users fall through.

The cost is measured in adoption. Developers evaluate libraries by trying the first example. If it doesn't run in under 2 minutes, they move to the next option. Studies of developer documentation consistently find that runnable, copy-pasteable examples are the single strongest predictor of library adoption -- more than API completeness, more than performance benchmarks, more than community size. Bad examples directly cost users.

## The Solution

This plugin gives Claude a structured methodology for designing code examples that teach effectively through progressive complexity. Instead of generating a single code block, Claude applies a four-level complexity ladder (minimal happy path, add configuration, add error handling, add edge cases, production-ready) and a quality checklist that enforces runnability, completeness, minimality, commenting, and realistic naming.

The skill provides four distinct example types (snippet, complete example, tutorial, reference app) with specific templates for each. Every example follows a four-part anatomy: context (what this does), setup (prerequisites), core (the key concept, highlighted), and result (expected output). Tutorials get a structured template with time estimate, prerequisites, step-by-step progression, and next steps. Anti-patterns are explicitly flagged: foo/bar variables, missing imports, outdated syntax, no expected output, untested code, and wall-of-code formatting.

The plugin ships a single SKILL.md with all templates and checklists, 13 trigger eval cases, and 3 output quality eval cases.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Examples use `foo`, `bar`, `baz` as variable names, teaching nothing about real usage | Realistic naming convention enforced: `user`, `order`, `paymentResult` -- variables that map to real domains |
| Missing imports mean copy-paste fails immediately | All imports included; quality checklist verifies the example runs as-is |
| Single code block with no explanation | Four-part anatomy: context comment, setup, highlighted core concept, expected output |
| One complexity level (either too simple or too complex) | Five-level progressive complexity: minimal -> configured -> error handling -> edge cases -> production |
| Tutorials jump from trivial to advanced with no intermediate steps | Structured tutorial template with time estimate, prerequisites, and step-by-step progression |
| No expected output -- reader cannot verify if their result is correct | Every example includes an expected output comment showing what success looks like |

## Context to Provide

Example quality is directly proportional to how much context the skill knows about the target reader, the concept being taught, and the realistic domain the code operates in. Generic "show me an example" produces generic examples with placeholder names. Specific context produces examples that a developer can copy, run, and immediately understand in the context of their real work.

**What to include in your prompt:**
- **The specific concept, API method, or feature to demonstrate** -- name it exactly; "authentication" is too broad, "JWT token refresh with automatic retry on 401" is specific enough to produce a focused example
- **The language and framework version** (Python 3.11 with FastAPI 0.104, TypeScript with Express 4.x, Node.js 20 with the AWS SDK v3)
- **The audience's experience level** (intermediate Python developer who knows HTTP but not our SDK; senior TypeScript developer unfamiliar with our authentication model)
- **The realistic domain** -- if the code is for an e-commerce platform, use order/product/customer variables, not foo/bar
- **The complexity level you need** -- minimal snippet, working example, or full progressive set (minimal through production-ready)
- **Expected output** -- what should the user see when the example runs successfully?

**What makes results better:**
- Providing the actual API signature or method you want demonstrated -- the skill names variables after real parameters
- Describing what typically goes wrong so the example can show the common error and how to handle it
- Saying which prerequisite knowledge can be assumed (e.g., "they have already authenticated, show them the next step")
- For tutorials: stating the concrete end result ("deploy their first endpoint" or "process their first webhook")

**What makes results worse:**
- Asking for examples in a vacuum without language or framework -- produces pseudocode that cannot be run
- Requesting production application code -- this skill designs *teaching* code optimized for clarity; use language-specific skills for production code
- Asking for a "complete application example" without specifying which concept each section should teach -- produces a wall of code with no clear focal point

**Template prompt:**
```
Create a [progressive set of / single / tutorial for] example(s) showing how to [specific concept/API]. Language: [language version]. Framework: [framework version]. Target audience: [experience level, what they know, what they don't]. Domain: [the realistic domain for variable names, e.g., "e-commerce: orders, products, customers"]. Complexity: [minimal only / minimal through error handling / full 5-level progression]. Expected output when it runs: [what success looks like].
```

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install example-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention code examples, tutorials, quickstart guides, sample code, runnable examples, or progressive complexity.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your project
3. Type: `Create a progressive example showing how to use our authentication API -- from minimal to production-ready`
4. Claude produces a five-level example set: basic happy path, with configuration, with error handling, with edge cases, and production-ready with retry logic and logging
5. Next, try: `Write a 10-minute tutorial for first-time users of this library`

---

## System Overview

```
User prompt (create example / write tutorial / design quickstart)
        |
        v
+------------------+
|  example-design  |
|  skill (SKILL.md)|
+------------------+
        |
        +---> Example Type Selection
        |     (snippet / complete / tutorial / reference app)
        |
        +---> Progressive Complexity Ladder
        |     Level 1: Minimal (happy path)
        |     Level 2: Add configuration
        |     Level 3: Add error handling
        |     Level 4: Add edge cases
        |     Level 5: Production-ready
        |
        +---> Example Anatomy (per example)
        |     1. Context comment
        |     2. Setup (imports/prerequisites)
        |     3. Core concept (highlighted)
        |     4. Expected output
        |
        +---> Quality Checklist
        |     Runnable / Complete / Minimal / Commented / Realistic / Tested
        |
        +---> Anti-Pattern Audit
              foo/bar vars / missing imports / outdated syntax / no output / untested / wall of code
```

Single-skill plugin with no references, hooks, or MCP dependencies. The skill contains structured templates for four example types and a five-level complexity ladder.

## What's Inside

| Component | Type | What It Provides |
|---|---|---|
| **example-design** | Skill | Templates for 4 example types, 5-level complexity ladder, quality checklist, anti-pattern list |
| **trigger-evals** | Eval | 13 trigger eval cases (8 positive, 5 negative) |
| **output-evals** | Eval | 3 output quality eval cases |

### Component Spotlight

#### example-design (skill)

**What it does:** Activates when you ask about creating code examples, tutorials, quickstart guides, sample code, or runnable demonstrations. Applies a progressive complexity framework and structured templates to produce examples that teach effectively and run correctly on first try.

**Input -> Output:** You provide a concept, API, or library to demonstrate -> The skill produces structured examples at appropriate complexity levels with realistic naming, complete imports, highlighted core concepts, and expected output.

**When to use:**
- Writing documentation examples for a library or API
- Creating a quickstart guide for new users
- Building a step-by-step tutorial with progressive complexity
- Designing a reference application that demonstrates production patterns
- Reviewing existing examples for quality (runnability, completeness, clarity)

**When NOT to use:**
- Generating full documentation (API reference, architecture guides) -> use [documentation-generator](../documentation-generator/)
- Writing production application code -> this skill designs *teaching* code, not production code
- Creating test cases -> use [test-driven-development](../test-driven-development/) or [testing-framework](../testing-framework/)

**Try these prompts:**

```
Create a progressive example set (minimal through production-ready) showing how to use our REST API client to fetch paginated user records. Language: Python 3.11. Target audience: intermediate Python developers who know requests but not our SDK. Domain: user management (users, accounts, roles). The final level should include retry logic and structured error handling.
```

```
Write a 10-minute tutorial that takes a Node.js developer from npm install to their first successful webhook delivery and verification. They know Express but have never used our SDK. Each step should show the exact command to run and the expected output so they know if something went wrong.
```

```
Review these three code examples from our Python SDK documentation. Check each for: missing imports, placeholder variable names (foo/bar/data), expected output, and whether a beginner could run them without modification.

[paste the three examples]
```

```
Design a reference todo application that demonstrates our TypeScript framework's four core concepts: routing, PostgreSQL persistence, JWT authentication, and centralized error handling. Each concept should be isolated in its own file so a developer can read just one file to learn that concept.
```

```
Our CLI quickstart drops off between step 3 (configure credentials) and step 4 (run first command). Step 3 shows the config file but doesn't show what success looks like, so users don't know if they configured it correctly before continuing. Redesign steps 3 and 4 to show expected output at each step.
```

**Key components in the skill:**

| Component | What It Covers |
|---|---|
| Example Types | Snippet (5-15 lines), complete example (20-50 lines), tutorial (multi-file), reference app (full project) |
| Progressive Complexity | 5-level ladder: minimal -> configured -> error handling -> edge cases -> production-ready |
| Example Anatomy | 4-part structure: context, setup, core (highlighted), expected output |
| Quality Checklist | 6 criteria: runnable, complete, minimal, commented, realistic, tested |
| Tutorial Template | Structured format: goal, time estimate, prerequisites, step-by-step, next steps |
| Anti-Patterns | 6 common mistakes: foo/bar variables, missing imports, outdated syntax, no output, untested, wall of code |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Show me how to use this" | "Create a progressive example showing how to connect to Redis -- from basic get/set to production-ready with connection pooling" |
| "Write some code samples" | "Write runnable examples for each of our 5 SDK methods, with realistic variable names and expected output" |
| "Make a tutorial" | "Write a 10-minute tutorial that takes a Python developer from pip install to their first webhook handler" |
| "Document this API" | "Design examples for our pagination API at three complexity levels: basic list, with cursor, with error handling and retry" |
| "Give me an example" | "Show me a complete working example of file upload with progress tracking, including all imports and expected console output" |

### Structured Prompt Templates

**For progressive example sets:**
```
Create a progressive example set for [concept/API/method]. Start with the minimal happy path and build up through: configuration options, error handling, edge cases, and production-ready patterns. Language: [language]. Target audience: [beginner/intermediate/advanced].
```

**For tutorials:**
```
Write a [duration]-minute tutorial for [audience]. Goal: [what they'll build/learn]. Prerequisites: [what they need installed/known]. The tutorial should go from [starting point] to [end result] in [number] steps.
```

**For example review:**
```
Review these code examples for [quality issues / runnability / progressive complexity]. Flag any that use placeholder names, miss imports, or lack expected output. Suggest specific fixes.
```

### Prompt Anti-Patterns

- **No target audience specified:** "Write examples for our API" -- beginner examples look very different from advanced examples. Specify who will read them.
- **Asking for examples without context:** "Show me an example of caching" -- caching in what framework? With what data? For what use case? The more context, the more realistic the example.
- **Requesting a wall of code:** "Give me a complete application example" without specifying which concepts to highlight -- the skill will produce a reference app, but it works best when you specify which concepts each section should teach.

## Real-World Walkthrough

You are writing documentation for a new Python HTTP client library. The library is a wrapper around `httpx` with automatic retry, circuit breaking, and structured logging. Your current documentation has one example: a 200-line script that demonstrates everything at once. New users are confused because they can't tell which parts are the library and which parts are their application code.

**Step 1: Scoping the example set.** You ask Claude: **"Design a progressive example set for our HTTP client library. The key features are: basic requests, retry configuration, circuit breaking, and structured logging. Target audience is intermediate Python developers."**

Claude activates the example-design skill and proposes a five-level progression:

**Level 1 (Minimal, 8 lines):** Import the client, make a GET request, print the response. No configuration, no error handling. Just the "hello world" that proves the library works:

```python
"""Make your first request with our HTTP client."""
from mylib import Client

client = Client(base_url="https://api.example.com")
response = client.get("/users/1")
print(response.json())  # Output: {"id": 1, "name": "Alice"}
```

Every line is commented. The import is explicit. The output shows what success looks like.

**Level 2 (Configured, 15 lines):** Add retry configuration. The diff from Level 1 is exactly 3 lines -- the reader can see what changed:

```python
"""Configure automatic retry for transient failures."""
from mylib import Client, RetryConfig

retry = RetryConfig(max_attempts=3, backoff_factor=0.5)
client = Client(base_url="https://api.example.com", retry=retry)
# ... same request as Level 1
```

**Step 2: Tutorial design.** You then ask: **"Now write a 15-minute tutorial that takes a new user from pip install to a working retry-enabled client."**

Claude produces a structured tutorial with time estimate, prerequisites (Python 3.9+, pip), and 5 steps. Each step has exactly one concept, one code block, and one expected result. The tutorial explicitly calls out what to look for: "Run this. You should see a 200 status code. If you see a ConnectionError, check that the URL is reachable."

**Step 3: Quality audit.** You paste your existing 200-line example and ask: **"Review this example for quality issues."**

Claude flags: 3 uses of `data` as a variable name (ambiguous -- is it request data? response data? parsed data?), 2 missing imports that only work because of a wildcard import at the top, no expected output for any code block, and a jump from "basic request" to "circuit breaking" with no intermediate step. It suggests splitting the single example into the five-level progression designed in Step 1.

**Step 4: Anti-pattern cleanup.** Claude identifies that the original example uses `temp`, `result`, and `x` as variable names. It replaces them with `user_response`, `retry_count`, and `health_check` -- names that teach what the code does, not just what the syntax is.

You now have a five-level example set, a structured tutorial, and a cleaned-up reference example -- all designed to get a new user from installation to productive usage in under 15 minutes.

## Usage Scenarios

### Scenario 1: Writing SDK documentation examples

**Context:** You are documenting a JavaScript SDK with 12 methods. Each method needs at least one example, and the key methods need examples at multiple complexity levels.

**You say:** "Design examples for each of our 12 SDK methods. For the 4 core methods (create, read, update, delete), provide examples at 3 complexity levels. For the rest, provide a single runnable example with expected output."

**The skill provides:**
- 12 complete examples with realistic variable names, all imports, and expected output
- 4 three-level progressive examples for core methods (minimal, with options, with error handling)
- Quality checklist verification for each example (runnable, complete, minimal, commented)
- Consistent naming conventions across all 12 examples

**You end up with:** A complete set of documentation examples that a developer can copy-paste and run immediately, with progressive depth for the methods that need it.

### Scenario 2: Designing a quickstart guide for a CLI tool

**Context:** Your CLI tool has a 5-minute quickstart guide but users drop off between installation and their first successful command. The current guide has 8 steps with no expected output shown.

**You say:** "Redesign our CLI quickstart to show expected output at every step. Users should go from install to their first meaningful result in under 5 minutes."

**The skill provides:**
- Restructured 5-step quickstart with expected output after every command
- Progressive complexity: step 1 is the simplest possible command, step 5 is a realistic workflow
- Troubleshooting hints embedded inline ("If you see X, run Y to fix it")
- Time estimates per step so users know if they are on track

**You end up with:** A quickstart guide where users can verify success at every step, reducing the drop-off point from step 3 to zero.

### Scenario 3: Creating a reference application

**Context:** Your framework needs a "todo app" reference implementation that demonstrates routing, data persistence, authentication, and error handling in a realistic context.

**You say:** "Design a reference todo application for our framework. It should demonstrate the 4 core concepts (routing, persistence, auth, errors) with realistic code, not toy examples."

**The skill provides:**
- Multi-file reference application with clear separation of concerns
- Each file focused on teaching one concept (router.ts teaches routing, auth.ts teaches authentication)
- Progressive complexity within the app: basic CRUD first, then auth middleware, then error handling
- README with architecture diagram and "start here" guidance

**You end up with:** A reference application that developers can clone, run, and learn from -- with each file teaching one concept clearly.

---

## Decision Logic

This is a single-skill plugin with no component-selection logic. The skill activates when your prompt mentions code examples, tutorials, quickstart guides, sample code, or runnable examples. Once activated, Claude selects the appropriate example type and complexity level based on your request:

| You ask for... | Example type | Complexity levels |
|---|---|---|
| A quick code snippet | Snippet (5-15 lines) | Level 1 only |
| A working example | Complete example (20-50 lines) | Level 1-3 |
| A step-by-step guide | Tutorial (multi-file) | Levels 1-5 progressive |
| A full demo project | Reference app (full project) | Level 5 (production-ready) |
| Progressive examples | Complete examples at each level | All 5 levels |

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| No language or framework specified | Skill produces generic pseudocode instead of runnable examples | Specify the language and framework: "Python with FastAPI" or "TypeScript with Express" |
| Audience level unclear | Examples are too simple for advanced users or too complex for beginners | Specify the audience: "intermediate Python developers who know HTTP but not our library" |
| Example scope too broad | 200-line wall of code that tries to demonstrate everything | Scope to one concept per example: "just show retry configuration" or split into a progressive example set |
| Expected output depends on external state | Output section says "varies" instead of showing a concrete result | Use deterministic examples or mock the external dependency so the expected output is consistent |
| Framework/library version mismatch | Example uses deprecated API from an older version | Specify the version in your prompt: "examples for v3.x of our SDK" |

## Ideal For

- **Library and SDK authors** who need documentation examples that run correctly and teach effectively
- **Developer advocates** writing quickstart guides, tutorials, and getting-started content
- **Technical writers** who need to audit existing examples for quality (runnability, completeness, clarity)
- **Team leads** establishing example code standards across a documentation set
- **Open source maintainers** whose README examples are the primary driver of adoption

## Not For

- **Full documentation generation** -- this skill designs examples and tutorials, not complete API references or architecture guides. Use [documentation-generator](../documentation-generator/) for that.
- **Production application code** -- the skill optimizes for teaching clarity, not production performance. Use language-specific development skills for production code.
- **Test case generation** -- use [test-driven-development](../test-driven-development/) or [testing-framework](../testing-framework/) for writing tests.

## Related Plugins

- **[Documentation Generator](../documentation-generator/)** -- Generate comprehensive documentation for repositories of any size
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and style guides for uniform examples across a documentation set
- **[API Design](../api-design/)** -- Design the APIs that examples demonstrate
- **[Frontend Design](../frontend-design/)** -- When examples need UI component demonstrations
- **[Prompt Engineering](../prompt-engineering/)** -- When examples are for LLM prompt templates rather than code

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
