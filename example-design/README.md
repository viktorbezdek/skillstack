# Example Design

> **v1.0.10** | Documentation | 11 iterations

> Design code examples, tutorials, and runnable samples that actually teach -- with progressive complexity and copy-paste reliability.

## The Problem

Most code examples in documentation fail the reader before they finish reading. The quickstart dumps 80 lines of production code with no context about which line matters. The tutorial omits the import statements, so the developer copy-pastes, hits an error, and loses trust in the entire doc. The API reference uses `foo`, `bar`, and `baz` as variable names, forcing the reader to mentally map meaningless tokens to real concepts while simultaneously learning a new API. None of the examples show expected output, so there is no way to verify whether the code worked.

These are not style preferences -- they are adoption blockers. Developer experience research consistently shows that the first working code example is the make-or-break moment for library adoption. If a developer cannot copy-paste and run the first example within 5 minutes, most will abandon the library and try the next alternative. Yet the majority of open-source documentation treats examples as an afterthought: written once by the library author (who does not need the imports because they know the codebase), never tested after the API changes, and organized by API surface rather than by what the developer is trying to accomplish.

The deeper problem is structural. A single code example cannot serve every audience. A beginner needs the minimal happy path; an intermediate developer needs error handling and configuration; an advanced developer needs production patterns with edge cases. When all of these are crammed into one example, it overwhelms beginners and bores experts. When they are split across separate pages with no progression, each example exists in isolation and the reader cannot see how simple usage evolves into production code.

## The Solution

This plugin gives Claude a structured methodology for designing code examples at four levels of scope (snippet, complete example, tutorial, reference app) and five levels of complexity (minimal, configured, error-handled, edge-cased, production-ready). Every example follows a four-part anatomy: context comment explaining what this does, setup with all imports and prerequisites, the core concept highlighted as the key line, and expected output showing what the reader should see.

The quality checklist catches the six most common example failures before they ship: is it runnable (copy-paste works), complete (all imports included), minimal (no unrelated code), commented (key lines explained), realistic (real-world names, not foo/bar), and tested (verified working after the last API change). The tutorial structure template adds time estimates, prerequisites, numbered steps with explanation-code-result triples, and next-steps navigation.

The progressive complexity ladder is the key structural innovation. Instead of writing one example that tries to serve everyone, you write five levels -- each building on the previous one. Level 1 is the minimal happy path in 10 lines. Level 2 adds configuration. Level 3 adds error handling. Level 4 covers edge cases. Level 5 shows the production-ready implementation. The reader enters at their level and reads forward to learn more or backward to understand fundamentals.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Examples dump 80 lines of production code with no indication of which line is the key concept | Four-part anatomy highlights the core concept and separates it from setup, context, and output |
| Developers copy-paste and hit import errors because the example omits prerequisites | Quality checklist enforces "all imports included" as a non-negotiable |
| Variable names are `foo`, `bar`, `baz` -- the reader learns nothing about real usage | Anti-pattern audit flags meaningless names and requires realistic alternatives (`createUser`, `orderTotal`) |
| No expected output -- the developer cannot tell if the code worked | Every example includes expected output showing what the reader should see |
| One example tries to serve beginners and experts, overwhelming the former and boring the latter | Five-level progressive complexity ladder lets each audience enter at their level |
| Tutorials are walls of code with occasional prose, no structure or time estimates | Tutorial template provides prerequisites, numbered steps with explanation-code-result triples, and next-steps navigation |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install example-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention code examples, tutorials, sample code, quickstart guides, or runnable examples.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your project
3. Type: `Write a code example for the createUser API method -- show progressive complexity from minimal to production-ready`
4. Claude produces a five-level example set: Level 1 minimal happy path, Level 2 with configuration, Level 3 with error handling, Level 4 with edge cases, Level 5 production-ready -- each following the four-part anatomy with context, setup, core concept, and expected output
5. Next, try: `Audit the code examples in our README for quality issues` to run the six-item checklist against existing examples

## What's Inside

Single-skill plugin shipping one SKILL.md with six structured components, 13 trigger eval cases, and 3 output eval cases. No references, hooks, or MCP dependencies.

| Component | What It Provides |
|---|---|
| **Example Types** | Four-row reference mapping snippet (5-15 lines), complete example (20-50 lines), tutorial (multi-file), and reference app (full project) to their purpose |
| **Progressive Complexity** | Five-level ladder from minimal happy path through configuration, error handling, edge cases, to production-ready |
| **Example Anatomy** | Four-part structure: context comment, setup/imports, highlighted core concept, and expected output |
| **Quality Checklist** | Six-item verification: runnable, complete, minimal, commented, realistic, tested |
| **Tutorial Structure** | Markdown template with time estimate, prerequisites, numbered steps (explanation + code + expected result), and next-steps |
| **Anti-Patterns** | Six common mistakes: foo/bar names, missing imports, outdated syntax, no expected output, untested code, wall of code |

### example-design

**What it does:** Activates when you ask about creating code examples, writing tutorials, designing quickstart guides, building sample code, or auditing existing documentation examples for quality. Applies a structured methodology that ensures every example is copy-pasteable, progressively complex, and teaches through realistic scenarios rather than abstract demonstrations.

**Try these prompts:**

```
Write a quickstart guide for our authentication SDK -- someone should be able to go from install to first authenticated request in under 5 minutes
```

```
Audit the code examples in our API documentation -- check if they're runnable, have all imports, and show expected output
```

```
Design a progressive tutorial for our GraphQL API: start with a simple query, then add variables, then mutations, then subscriptions, then error handling
```

```
Convert this wall-of-code example into a properly structured snippet with context, setup, highlighted core concept, and expected output
```

```
What type of example should I write for this feature? I have a simple use case and a complex one -- should it be a snippet, a complete example, or a full tutorial?
```

## Real-World Walkthrough

You are the lead developer of an open-source Node.js ORM library. Your GitHub stars are growing, but your Discord is full of the same question: "How do I get started?" Your current README has a single code example -- 45 lines that create a connection, define a model, run a migration, seed data, and execute a query. It works, but new users report spending 20 minutes figuring out which parts are required and which are optional.

You start by asking Claude: **"Audit this code example from our ORM README"** and paste the 45-line block.

Claude activates the example-design skill and runs the quality checklist. It flags three failures. First, **missing imports**: the example uses `createConnection` but does not show where it comes from -- `import { createConnection } from 'myorm'` is nowhere in the code. Second, **no expected output**: the example ends with `const users = await User.findAll()` but does not show what `users` looks like. Third, **wall of code**: five distinct concepts (connection, model, migration, seeding, querying) are crammed into one block with no comments explaining which line does what.

You then ask Claude: **"Redesign this as a progressive complexity tutorial -- from first query to production-ready."**

Claude applies the progressive complexity ladder and produces five levels:

**Level 1 -- First Query (8 lines).** Just the connection and a single query. Context comment: "Connect to a database and fetch all users." All imports shown. The core concept (the query) is highlighted. Expected output: `[{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }]`.

```javascript
// Connect to a database and fetch all users
import { createConnection } from 'myorm';

const db = await createConnection('sqlite://demo.db');
const users = await db.query('SELECT * FROM users');

console.log(users);
// Output: [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }]
```

**Level 2 -- Define a Model (15 lines).** Builds on Level 1 by adding a model definition with typed fields. Context: "Define a User model with validation." New concept highlighted: the `define` method with field types. Expected output: the same query result, now via `User.findAll()` instead of raw SQL.

**Level 3 -- Error Handling (22 lines).** Builds on Level 2 by wrapping the connection in try/catch, handling connection failures, and showing what happens when a query fails. New concepts highlighted: connection retry logic and error types. Expected output: both the success case and the error case.

**Level 4 -- Migrations and Seeding (35 lines).** Builds on Level 3 by adding schema migration and seed data. Context: "Set up the database from scratch." This is where the migration and seeding code from the original example belongs -- not in Level 1. Expected output: "Migration complete: users table created" then the query results.

**Level 5 -- Production-Ready (50 lines).** Builds on Level 4 by adding connection pooling, environment-based configuration, graceful shutdown, and logging. Context: "Production deployment pattern." This is the full example that advanced users need, with every line commented to explain why the production version differs from the tutorial version.

Claude also applies the tutorial structure template, producing a complete markdown document with time estimates (Level 1: 2 minutes, Level 2: 5 minutes, Level 3: 8 minutes, Level 4: 12 minutes, Level 5: 15 minutes), prerequisites (Node.js 18+, npm, SQLite), and next-steps navigation pointing to the API reference and the migrations guide.

Finally, Claude runs the anti-patterns audit on each level. It catches one issue in Level 4: a variable named `data` that should be `seedUsers` for clarity. It also suggests adding a "What you'll build" section at the top showing the final result (a working API that serves user data) so readers know where the tutorial is heading before they start.

You replace the 45-line README example with Level 1 (the 8-line quickstart) and link to the full tutorial for developers who want to go deeper. Within a week, the "How do I get started?" questions in Discord drop by half, and two community members submit PRs improving examples in other parts of the docs -- following the same progressive structure.

## Usage Scenarios

### Scenario 1: Writing a quickstart for a new open-source library

**Context:** You just published an npm package and need a README example that gets developers from install to first working result in under 5 minutes.

**You say:** "Write a quickstart example for my HTTP client library -- show how to make a GET request and handle the response"

**The skill provides:**
- A Level 1 snippet following the four-part anatomy (context, setup, core concept, expected output)
- All imports explicitly shown
- Realistic variable names and URLs
- Expected output showing the actual response shape

**You end up with:** An 8-10 line example that a developer can copy-paste, run, and verify within 2 minutes.

### Scenario 2: Auditing existing documentation for broken examples

**Context:** Your SDK documentation has 30 code examples and you have received three bug reports about examples that no longer work after the v2.0 API change.

**You say:** "Audit these code examples against the quality checklist -- check for missing imports, outdated syntax, and missing expected output"

**The skill provides:**
- A pass/fail report for each example against the six quality criteria
- Specific failures identified (e.g., "Line 3: uses deprecated `connect()`, should be `createConnection()`")
- Priority ranking by severity (broken examples first, then missing output, then style issues)

**You end up with:** A prioritized fix list that the documentation team can work through systematically.

### Scenario 3: Building a progressive tutorial for a complex feature

**Context:** Your authentication library supports API key auth (simple) and OAuth2 with refresh tokens (complex). You need documentation that serves both audiences.

**You say:** "Design a progressive tutorial for our auth library -- start with API key auth and build up to OAuth2 with token refresh"

**The skill provides:**
- Five-level progression from API key (Level 1) through OAuth2 basics (Level 2), error handling for token failures (Level 3), refresh token edge cases (Level 4), to production-ready auth middleware (Level 5)
- Tutorial template with time estimates and prerequisites for each level
- Anti-pattern audit on the resulting examples

**You end up with:** A complete tutorial document where beginners can stop at Level 1 and advanced users can jump to Level 4, with each level building cleanly on the previous one.

### Scenario 4: Deciding what type of example to write

**Context:** A PM asks for "a tutorial" for a feature that can be demonstrated in 10 lines of code. You suspect a full tutorial is overkill.

**You say:** "Should this be a snippet, a complete example, or a tutorial? The feature is a single function call with two parameters"

**The skill provides:**
- Example types table showing that a snippet (5-15 lines) is appropriate for single concepts
- Recommendation to write a snippet with full anatomy (context, setup, core, output) rather than a tutorial
- Guidelines for when to escalate to a complete example or tutorial (multiple concepts, multi-step setup, or complex configuration)

**You end up with:** A clear recommendation with rationale, preventing over-engineering of documentation.

## Ideal For

- **Open-source maintainers writing README quickstarts** -- the four-part anatomy and quality checklist produce examples that pass the "copy-paste and run" test
- **Developer advocates creating tutorials and guides** -- the progressive complexity ladder structures content for multiple skill levels without duplication
- **Documentation teams auditing existing example quality** -- the six-item checklist and anti-patterns list provide objective criteria for identifying broken or unhelpful examples
- **SDK teams shipping code samples with API docs** -- the example types table matches each documentation need to the right format and scope
- **Technical writers restructuring legacy docs** -- the anti-patterns audit systematically identifies and fixes foo/bar names, missing imports, and walls of code

## Not For

- **Generating full API reference documentation** -- this plugin is about the code examples *within* documentation, not the documentation structure itself. Use [documentation-generator](../documentation-generator/) for comprehensive docs
- **Writing production application code** -- the examples are designed for teaching, not for deploying. The Level 5 "production-ready" examples show patterns, not ship-ready implementations
- **Automated documentation from source code** -- this plugin designs hand-crafted examples, not auto-generated API docs. Use code-level documentation tools for the latter

## How It Works Under the Hood

The plugin is a single-skill architecture with no references, hooks, or MCP dependencies. The SKILL.md contains six structured sections that Claude applies based on the query:

1. **Example Types** -- Claude determines the appropriate scope (snippet, complete example, tutorial, reference app) based on the concept's complexity
2. **Progressive Complexity** -- For multi-level requests, Claude applies the five-level ladder, ensuring each level builds on the previous one
3. **Example Anatomy** -- Every code example follows the four-part structure: context comment, setup/imports, highlighted core concept, expected output
4. **Quality Checklist** -- Claude verifies each example against six criteria before delivering: runnable, complete, minimal, commented, realistic, tested
5. **Tutorial Structure** -- For tutorial-scope requests, Claude applies the markdown template with time estimates, prerequisites, and step structure
6. **Anti-Patterns** -- Claude audits for the six common mistakes and flags any that appear in the output or in existing examples being reviewed

## Related Plugins

- **[Documentation Generator](../documentation-generator/)** -- Comprehensive documentation generation for repositories of any size -- pairs with this plugin (generate the docs there, design the examples here)
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and style guides that complement example quality standards

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
