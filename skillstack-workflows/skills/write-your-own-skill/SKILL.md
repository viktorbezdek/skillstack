---
name: write-your-own-skill
description: Meta-workflow for creating your own Claude Code skill that actually activates when needed and delivers genuine value. Starts with skill-creator as the canonical starting point, adds elicitation frameworks when the skill is for a human/domain area (interviewing, research, therapy-adjacent), designs the examples that will illustrate the skill (example-design), aligns with repo conventions (consistency-standards), writes structural validation tests before the content (test-driven-development), audits the draft against anti-patterns (critical-intuition), and generates the README with scenario tables (documentation-generator). Use when creating any new Claude Code skill that you want to be activation-reliable, well-scoped, and maintainable. NOT for quick-and-dirty prompts — use prompt-engineering directly.
---

# Write Your Own Skill

> The difference between a skill that activates reliably and one that sits unused is almost always the frontmatter description. The difference between a skill that delivers value and one that doesn't is almost always whether anti-patterns were audited before shipping. This workflow enforces both.

Creating a Claude Code skill looks easy — write a markdown file with some frontmatter. Creating a GOOD skill requires discipline: clear activation boundaries, progressive disclosure, concrete examples, anti-pattern awareness, and validation. This workflow makes the discipline concrete.

---

## When to use this workflow

- Creating a new Claude Code skill from scratch
- Rewriting a skill that doesn't activate reliably
- Adding a skill to a repo that enforces a plugin contract (like skillstack)
- Extracting a workflow pattern you've used repeatedly into a reusable skill
- Teaching someone else how to build skills well

## When NOT to use this workflow

- **Quick-and-dirty prompts** — use `prompt-engineering` directly
- **One-off scripts or automation** — skills are for reusable knowledge, not one-time work
- **Things that should be tools, not knowledge** — if the "skill" is really a function that does something, build it as an MCP server (use the `mcp-server` skill)
- **Things that should be entire plugins** — if your skill is 40+ reference files, you're building a plugin, which this workflow still covers, but know the scope before starting

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install skill-foundry@skillstack
/plugin install elicitation@skillstack
/plugin install example-design@skillstack
/plugin install consistency-standards@skillstack
/plugin install test-driven-development@skillstack
/plugin install critical-intuition@skillstack
/plugin install documentation-generator@skillstack
```

---

## Core principle

**A skill is not a document — it's an instruction to Claude.** The audience is Claude, not humans browsing GitHub. Every word in SKILL.md is evaluated for whether it makes Claude's behavior better when the skill activates. Decorative prose, aspirational framings, and encyclopedia content all hurt. Concrete guidance, when-to-use boundaries, and decision tables help.

Secondary principle: **the frontmatter description is the whole game for activation.** Claude decides whether to load a skill based on its description. A description that says "comprehensive framework for X" tells Claude nothing about when to use it. A description that says "use when the user mentions A, B, or C; not for D or E" tells Claude exactly when to activate.

Third principle: **progressive disclosure is non-negotiable.** A skill that dumps 5,000 lines of content into Claude's context on activation burns tokens and degrades quality. Lean SKILL.md (≤200 lines), focused references loaded on demand, and explicit routing are the pattern that scales.

---

## The phases

### Phase 1 — starting point (skill-creator)

Load the `skill-foundry` skill. It knows the current conventions for well-formed skills and will catch mistakes that would take you weeks to diagnose on your own.

Use its guidance to answer:

- **What is this skill for?** One sentence. If you can't, you don't know yet — keep thinking.
- **Who is the audience?** Claude, yes, but also: which kind of query should trigger it? Write 3-5 example queries you want the skill to catch.
- **What's the output?** What behavior change should activating this skill produce?
- **What's in scope?** A skill that tries to cover everything covers nothing.
- **What's explicitly out of scope?** The negation matters as much as the positive. Skills with no "when NOT to use" sections tend to over-activate.

Output: a one-page spec of the skill before any markdown is written.

### Phase 2 — elicit the domain depth (elicitation, if applicable)

Load the `elicitation` skill IF your skill is about a domain involving humans (interviewing, research, therapy-adjacent, user-facing design, communication).

Most skill authors don't know what "depth" looks like in domains they're writing about. You think you understand what a user interview is until you read `elicitation` and realize you were designing interrogations. The `elicitation` skill's frameworks (OARS, narrative identity, values elicitation, schema detection, anti-patterns) are meta-tools for thinking about depth in other domains.

Specifically, when writing a skill:

- **Interview a practitioner** who actually does the thing your skill is about. Not a colleague who's read about it — someone who practices it daily. Use the `elicitation` skill's frames to get real depth, not surface summaries.
- **Look for what's NOT in the textbook** — the things practitioners do that aren't in any reference but that matter. These are the moves that make real expertise.
- **Distinguish the common case from the edge case** — skill content should privilege the common case and flag edge cases as edge cases.

Skip this phase if your skill is purely technical (e.g., "how to write a TypeScript class") — no elicitation needed.

Output: a notebook of practitioner wisdom that the skill will encode.

### Phase 3 — design the examples (example-design)

Load the `example-design` skill.

The examples in a skill are often read before the prose. If the examples are bad, the skill is bad regardless of what the prose says. Examples should:

- **Start minimal** — the smallest possible case that illustrates the concept. Not production-ready. Not comprehensive. Minimal.
- **Progress in complexity** — add one concern at a time. The second example adds one more thing. The third adds one more.
- **Be runnable and copy-pasteable** — for code skills, every example should work when pasted. For process skills, every example should be followable.
- **Include anti-examples** — sometimes showing what NOT to do is more effective than showing what to do
- **Be specific, not generic** — "process user data" is not an example. "Validate that a POST body has required fields 'email' and 'password' and returns 400 with a specific error if missing" is an example.

Design the examples BEFORE writing the skill prose. The examples will tell you what the prose needs to cover and what it doesn't.

Output: 5-15 designed examples covering the common cases and key edge cases.

### Phase 4 — align with repo conventions (consistency-standards)

Load the `consistency-standards` skill.

Check:

- **Naming** — does the skill name fit the repo's conventions? skillstack uses `kebab-case`. Other repos may differ.
- **File structure** — single-skill plugin (`skills/{name}/SKILL.md`) vs multi-skill plugin (`skills/{sub-name}/SKILL.md` under one plugin root)
- **Frontmatter fields** — what's required? what's optional? mismatches get caught by validation
- **Footer format** — attribution, license
- **README structure** — for skillstack: scenario table, when-not-to-use, installation, how-to-use, what's-inside
- **Reference file layout** — `references/` directory, one concept per file, each file opens with a blockquote scope statement

Failing to check this step is how skills end up getting rejected by CI validation (in skillstack's case) or sitting broken in other repos.

Output: a conformance checklist for your skill.

### Phase 5 — write structural tests first (test-driven-development)

Load the `test-driven-development` skill.

Yes — TDD for a skill. The structural tests are:

- **Frontmatter validity** — name, description, any other required fields present
- **Frontmatter name matches directory** — for plugin repos with validators
- **Required sections present** — if your repo has a README contract (like skillstack), check for each section
- **References exist on disk** — every reference cited from SKILL.md has a corresponding file
- **Footer present** — license/attribution line

Write these tests before writing the skill content. When the tests pass, you have a structurally correct skill. Then you focus on content quality.

For skillstack specifically, the plugin validator at `.github/scripts/validate_plugins.py` does this automatically. Run it locally before committing.

Output: a passing test suite for the structural properties of your skill.

### Phase 6 — draft the SKILL.md

NOW you write the skill. You have:

- A spec (Phase 1)
- Practitioner wisdom if applicable (Phase 2)
- Examples (Phase 3)
- A style/structure checklist (Phase 4)
- Structural tests you must pass (Phase 5)

Writing the SKILL.md:

**Frontmatter description** — this is the single most important sentence in the skill. Include:

- When to activate (specific query patterns, domain keywords)
- When NOT to activate (adjacent domains that belong to other skills)
- Key capabilities (what the skill will deliver, in 2-3 concrete terms)
- The "NOT for X, use Y instead" pattern

A bad description: *"Comprehensive framework for database design."*
A good description: *"PostgreSQL schema design and optimization. Use for creating schemas, normalizing tables, choosing indexes, auditing migrations, debugging query performance. NOT for MongoDB/Redis/other NoSQL (use nosql-databases), NOT for ORM-specific questions (use the language/framework skill)."*

**Body structure** — follow the lean pattern:

- Opening blockquote establishing scope and core principle
- "When to use this skill" — scenario list
- "When NOT to use this skill" — the negation, with pointers to alternatives
- "Core principle(s)" — the non-negotiable rules
- "The phases" or "Domain routing table" — the main body
- "Gates and failure modes" — what stops the workflow or what to avoid
- "Output artifacts" — what a successful run produces
- "Related workflows and skills" — cross-references
- Footer

Keep the SKILL.md under ~200 lines. If you're going longer, extract sections into reference files and route to them.

**References** — if you have more than ~200 lines of content, extract focused references. Each reference:

- Covers one concept
- Opens with a blockquote explaining scope
- Has actionable content, not theory
- Ends with "Further reading" and the footer
- 150-350 lines is typical

**Examples throughout** — insert the designed examples from Phase 3 into the prose, not in a separate "examples" section. Examples in context teach better than examples in an appendix.

### Phase 7 — audit against anti-patterns (critical-intuition)

Load the `critical-intuition` skill.

Before shipping, self-audit the skill:

**Activation anti-patterns:**
- **Vague description** — the frontmatter description doesn't tell Claude when to use this
- **Overbroad description** — the description claims the skill applies to queries it doesn't actually handle well
- **Missing negation** — no "when NOT to use" makes the skill over-activate
- **Keyword stuffing** — the description lists 40 keywords trying to catch every possible query, which actually reduces activation accuracy

**Content anti-patterns:**
- **Encyclopedia mode** — the skill summarizes a field rather than telling Claude how to act in the field
- **Aspirational framing** — "achieve 10/10", "be the best at X" instead of concrete behavior guidance
- **Missing examples** — prose only, no concrete cases
- **Context bloat** — single-file skill over 300 lines, no progressive disclosure
- **Dangling references** — cites `references/X.md` that doesn't exist
- **Mission creep** — the skill covers three adjacent domains instead of one
- **Cargo-cult structure** — the skill has all the right section headers but the content inside them is vague

**Quality anti-patterns:**
- **No concrete output** — the skill describes what to think about but never what to produce
- **Missing boundary with neighbors** — no cross-references to related skills, so users don't know which skill to use when
- **Unchecked validation** — the skill hasn't been run through whatever validator the target repo uses

For each anti-pattern you find, fix it specifically. Don't generalize "this could be better" — name the anti-pattern and apply the concrete fix.

### Phase 8 — write the README (documentation-generator)

Load the `documentation-generator` skill.

The README is for humans browsing GitHub. It's not the skill content — it's marketing for the skill. It should:

- **Open with what the skill solves** — not "this is a comprehensive skill for X" but "X fails in these specific ways and this skill prevents them"
- **Have a "When to use" section** — scenario table mapping queries the user might have to what the skill delivers ("You say... / The skill provides...")
- **Have a "When NOT to use" section** — with pointers to alternatives
- **Have installation instructions** — including the exact commands (verified!)
- **Have a "What's inside" section** — list every reference file with its contents in one sentence
- **Have a version history** — so users know what changed
- **Have cross-references** — to related skills and workflows
- **Have proper attribution** — author, license, acknowledgments

The README is usually where you'll notice gaps in your own skill. Writing the README often reveals that you didn't fully think through who the skill is for.

### Phase 9 — validate and ship

- Run the validator (for skillstack: `python3 .github/scripts/validate_plugins.py`)
- Run the structural tests from Phase 5
- Try activating the skill with 3 queries — does it activate reliably? If not, the frontmatter description needs work
- Test with 2-3 queries the skill SHOULDN'T handle — does it stay silent? If not, the description is overbroad
- Commit with a clear message describing what the skill does
- Publish to the marketplace / catalog with the required metadata

---

## Gates and failure modes

**Gate 1: the spec gate.** Phase 3 cannot start until Phase 1's one-page spec exists. Skills written without a clear spec end up as encyclopedias.

**Gate 2: the example gate.** Phase 6 (drafting) cannot start until Phase 3's examples are designed. Writing prose before examples is backwards — prose ends up abstract.

**Gate 3: the audit gate.** Phase 9 (ship) cannot start until Phase 7's anti-pattern audit is complete. Shipping without audit almost always ships an anti-pattern.

**Failure mode: "I'll just write it and polish later".** The polish never happens. The skill ships with vague description, no examples, bloated content. Mitigation: follow the phase order.

**Failure mode: skill as knowledge dump.** The author knows a lot about the domain and tries to include everything. The skill is 800 lines. Claude won't load it reliably, and if it does, the content dilutes. Mitigation: progressive disclosure — lean SKILL.md + references.

**Failure mode: ambition mismatch.** The author wants to write "the definitive skill about X". X is a huge field. The skill tries to cover it all, fails at all of it. Mitigation: scope ruthlessly in Phase 1. "The skill for PostgreSQL schema design" is scoped. "The skill for databases" is not.

**Failure mode: copy-paste from a source.** The author copies content from a book, paper, or external doc. The skill reads like an article, not an instruction to Claude. Mitigation: Phase 1's "behavior change" question. A skill should change Claude's behavior, not summarize a reference.

**Failure mode: missing negation.** No "when NOT to use" section. The skill over-activates on adjacent queries, producing mediocre responses. Mitigation: Phase 1 + Phase 6 both require the negation.

**Failure mode: content without context.** The skill has great content but no concrete examples. Claude understands the principles but doesn't know how to apply them. Mitigation: Phase 3's example-first approach.

---

## Output artifacts

A completed skill produces:

1. **plugin.json** (or equivalent manifest for non-Claude-Code platforms)
2. **SKILL.md** — lean, scoped, with examples and cross-references
3. **references/** — focused domain content loaded on demand
4. **README.md** — human-facing documentation
5. **A passing structural test suite** — from Phase 5
6. **Activation evidence** — 3 queries that reliably activate the skill, 3 that don't
7. **A version history entry** — semantic version, what changed

---

## Related workflows and skills

- For managing the full plugin bundle (not just one skill), use the skillstack repo's `skill-foundry` plugin directly
- For presenting your new skill to others, use the `pitch-sprint` workflow
- For debugging why your skill isn't activating, use the `debug-complex-issue` workflow
- For the theory behind progressive disclosure and context efficiency, use the `context-fundamentals` and `context-optimization` skills

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
