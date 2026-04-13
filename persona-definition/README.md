# Persona Definition

> **v1.0.10** | Design & UX | 11 iterations

> Create research-backed user personas with demographics, goals, pain points, behaviors, and empathy maps that drive real product decisions instead of collecting dust in a slide deck.

## The Problem

Most product teams design for a vague idea of "the user." When pressed, different team members imagine different people -- the engineer pictures a power user comfortable with CLIs, the designer imagines a non-technical manager, the PM thinks about the buyer who is not even the end user. Without explicit personas, every design discussion becomes a proxy war between these unspoken assumptions.

Teams that do create personas often make them wrong. They build aspirational personas -- the user they wish they had, not the one they actually have. They load personas with demographics (age 32, lives in San Francisco, owns a dog) while leaving out the parts that actually drive product decisions: goals, pain points, behaviors, and context. They create 12 personas because every stakeholder wants their favorite user type represented, diluting the focus until the personas are too numerous to remember and too generic to be useful.

The result is a set of persona documents that nobody references after the initial workshop. Design decisions revert to "I think the user would..." based on individual intuition. Features ship without a clear answer to "which persona does this serve?" and "what pain point does it address?" The personas become artifacts of the process, not tools that shape it.

## The Solution

This plugin provides a structured methodology for creating personas that actually influence decisions. It starts with three persona types (proto-persona for quick alignment, lean persona for agile/MVP work, full persona for strategic decisions) so you invest the right amount of effort for your stage. Each persona captures the five components that matter: demographics, goals, pain points, behaviors, and context.

You get an empathy map framework (Says/Thinks/Does/Feels) for getting beneath surface-level demographics, a reusable persona template that captures goals, pain points, and documentation needs, and an anti-pattern catalog that catches the most common mistakes -- aspirational personas, too many personas, demographic-only personas, and static personas that are never updated. The skill limits you to 3-5 personas and pushes you to define goals and behaviors first, demographics second.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| "The user" is a different person in every team member's head | 3-5 explicit personas that the whole team references by name |
| Personas are demographics-only (age, location, job title) | Full persona with goals, pain points, behaviors, context, and empathy map |
| 12 personas that nobody remembers or uses | Constrained to 3-5 personas that are specific enough to drive decisions |
| Aspirational personas describe users you wish you had | Research-backed personas describe users you actually have |
| Persona documents created once and never updated | Living personas with update triggers and validation patterns |
| Features ship without clarity on which user they serve | Every design decision traceable to a specific persona and pain point |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install persona-definition@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe the product and its users:
   ```
   Create user personas for a developer documentation platform -- our users range from junior developers learning their first framework to senior architects evaluating tools
   ```
3. The skill produces 3-4 distinct personas with goals, pain points, behaviors, and documentation preferences.
4. Deep-dive into a specific persona:
   ```
   Build an empathy map for the junior developer persona -- what do they say, think, do, and feel when trying to learn a new API?
   ```
5. Get a four-quadrant empathy map that reveals motivations and frustrations beneath the surface-level description.

## What's Inside

Compact single-skill plugin focused on user persona creation and audience definition.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering persona types (proto, lean, full), five core components, empathy map framework, persona template, and anti-patterns |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### persona-definition

**What it does:** Activates when you need to create user personas, define target audiences, build customer archetypes, or understand user goals and pain points. It provides a structured methodology for creating personas at three levels of detail, with empathy maps for deeper behavioral insight and anti-pattern detection to prevent common mistakes.

**Try these prompts:**

```
Create user personas for a B2B project management tool -- our customers are mid-size agencies with PMs, designers, and developers
```

```
I need a quick proto-persona for our MVP -- we're building a budgeting app for freelancers
```

```
Build an empathy map for a first-time user of our CLI tool who comes from a GUI background
```

```
Review our existing personas -- I think they're too aspirational and don't match our actual users
```

```
We have 8 personas and nobody can remember them. Help me consolidate to a manageable set.
```

```
What persona components am I missing? I have demographics and job titles but the personas feel shallow.
```

## Real-World Walkthrough

You are the product lead for a developer tools company launching a new API testing platform. The platform targets developers who currently use Postman, curl, or custom scripts to test APIs. You need personas to guide the product roadmap, documentation strategy, and onboarding flow.

**Step 1: Choose the right persona type.**

You are past the MVP stage and making strategic decisions about the product direction. You ask:

```
We're building an API testing platform competing with Postman. We need personas to guide our product roadmap and docs strategy. We have 2,000 beta users and survey data. What persona type should I use?
```

The skill recommends full personas because you have real user data and are making strategic decisions. Proto-personas would be too shallow for roadmap planning. Lean personas would work for a single sprint's worth of decisions, but you need personas that last across quarters.

**Step 2: Define the persona set.**

Based on your description of the user base, the skill produces three personas:

**Alex, the API-First Developer** (Tech Savvy: 5/5)
- Role: Backend developer at a startup
- Primary goal: Test APIs as part of the development workflow, not as a separate step
- Pain point: Switching between IDE and Postman breaks flow; wants everything in the terminal
- Behavior: Prefers CLI tools, automates everything, writes tests before manual checking
- Context: Uses VS Code, works in TypeScript/Python, deploys multiple times per day

**Maya, the QA Engineer** (Tech Savvy: 3/5)
- Role: QA lead at a mid-size company
- Primary goal: Create comprehensive test suites for API contracts that run in CI
- Pain point: Postman collections are hard to version control and share with the team
- Behavior: Methodical, documents every test case, needs to report results to stakeholders
- Context: Works across multiple projects, needs to hand off tests to other QA team members

**Jordan, the Technical Lead** (Tech Savvy: 4/5)
- Role: Engineering manager evaluating tools for the team
- Primary goal: Standardize API testing across 5 backend teams
- Pain point: Every team uses different tools; no consistency in how APIs are tested
- Behavior: Decision-maker, evaluates tools on team adoption and maintainability, not just features
- Context: Manages 20+ developers, needs pricing transparency, cares about onboarding time

The skill keeps it to three personas and ensures each represents a distinct decision-making pattern, not just a different job title.

**Step 3: Build empathy maps.**

You want to understand Alex more deeply to design the CLI experience. You ask:

```
Build an empathy map for Alex, the API-first developer
```

The skill produces the four-quadrant empathy map:

| SAYS | THINKS |
|------|--------|
| "I just want to test this endpoint real quick" | "Why do I need a GUI for something curl can do?" |
| "Can I run this from my CI pipeline?" | "If I have to leave my terminal, I'll just use curl" |

| DOES | FEELS |
|------|-------|
| Writes bash scripts to test APIs | Frustrated by context-switching between IDE and GUI tools |
| Avoids tools that require mouse interaction | Proud of automated workflows; annoyed by manual steps |

This reveals that Alex's adoption hinges on terminal integration, not on feature parity with Postman. The onboarding flow for Alex should start with a CLI command, not a web dashboard.

**Step 4: Validate against anti-patterns.**

You run the personas through the anti-pattern checklist:

```
Check these three personas for anti-patterns. Are they aspirational? Too demographic-focused? Am I missing anything?
```

The skill catches one issue: Jordan's persona has solid demographics and goals but weak behavioral detail. What does Jordan actually do when evaluating a tool? The fix: add the evaluation behavior -- Jordan installs the tool, tries the onboarding in under 15 minutes, checks documentation quality, and asks two team members to try it independently. This behavioral detail directly informs the onboarding design: the first 15 minutes must demonstrate value to Jordan, or the deal is lost.

**Step 5: Connect personas to product decisions.**

With personas defined, you start making decisions. The documentation strategy now maps directly to personas: Alex gets a CLI quickstart guide (5 minutes to first API call from terminal), Maya gets a test suite tutorial (building a comprehensive collection), Jordan gets an evaluation guide (team rollout plan with ROI). The onboarding flow splits by persona: CLI-first path for Alex, guided wizard for Maya, team admin setup for Jordan.

The result: three research-backed personas that the entire team references by name. Feature prioritization debates shift from "I think the user wants..." to "This serves Alex's workflow, but what about Maya?" Documentation covers all three learning styles and use cases. The personas are not artifacts from a workshop -- they are active tools that shape every product decision.

## Usage Scenarios

### Scenario 1: Creating personas for a new product

**Context:** You are launching a fitness app and need to understand your target users before designing the first features.

**You say:** "Create user personas for a fitness tracking app targeting people who want to start exercising but find existing apps intimidating."

**The skill provides:**
- 3-4 personas spanning the motivation spectrum (health anxiety, social accountability, habit formation)
- Goals and pain points specific to fitness beginners (not gym regulars)
- Behavioral patterns: when they exercise, what triggers quitting, what keeps them going
- Anti-pattern check: ensures personas are not aspirational athletes

**You end up with:** Personas that represent your actual target users (beginners), not the users you wish you had (fitness enthusiasts), directly informing a beginner-friendly feature set.

### Scenario 2: Consolidating too many personas

**Context:** Over two years, your team accumulated 9 personas. Nobody remembers them and they contradict each other in feature prioritization.

**You say:** "We have 9 personas and they're not useful anymore. Help me consolidate to 3-4 that cover our actual user base."

**The skill provides:**
- Analysis of overlap between existing personas (which ones share goals and behaviors?)
- Consolidation strategy: merge similar personas, retire edge cases
- Validation criteria for the reduced set: does each persona represent a distinct decision-making pattern?
- Migration plan for existing documents that reference old persona names

**You end up with:** 3-4 consolidated personas that cover the full user base, are distinct enough to drive different design decisions, and are memorable enough that the team actually uses them.

### Scenario 3: Making shallow personas actionable

**Context:** Your personas are just demographics and job titles. They do not drive any product decisions.

**You say:** "Our personas have name, age, job title, and a generic quote. They feel useless. How do I make them drive actual product decisions?"

**The skill provides:**
- Gap analysis: what is missing (goals, pain points, behaviors, context)
- Empathy map exercise for each persona to uncover Says/Thinks/Does/Feels
- Goal hierarchy: primary goals, secondary goals, experience goals, prevention goals
- Decision test: for each persona, one product decision that would be different because of this persona

**You end up with:** Enriched personas with behavioral depth, plus a concrete example of how each persona changes a specific product decision.

## Ideal For

- **Product managers starting a new product** -- personas built before features prevent designing for imaginary users
- **UX designers planning research and usability tests** -- personas define who to recruit and what scenarios to test
- **Documentation teams tailoring content** -- persona documentation needs (format, detail level, learning style) directly shape the docs strategy
- **Teams with too many or too shallow personas** -- consolidation and enrichment patterns make existing personas useful again
- **Founders validating product-market fit** -- proto-personas test assumptions about who the user is before investing in full research

## Not For

- **Mapping stakeholders across organizations** -- use [persona-mapping](../persona-mapping/) for Power-Interest matrices, RACI charts, and influence analysis
- **Designing user journeys and touchpoint maps** -- use [user-journey-design](../user-journey-design/) for mapping the end-to-end experience
- **Defining OKRs and success metrics** -- use [outcome-orientation](../outcome-orientation/) for connecting user outcomes to business goals

## How It Works Under the Hood

The skill is a compact, focused knowledge base covering the core discipline of user persona design. The SKILL.md provides the complete framework: three persona types (proto, lean, full) with detail levels, five core components (demographics, goals, pain points, behaviors, context), the empathy map framework (Says/Thinks/Does/Feels), a reusable persona template with goals, pain points, and documentation needs, and an anti-pattern catalog (aspirational personas, too many personas, demographic-only, static personas).

There are no additional reference files -- the skill is deliberately compact so it loads fully into context and delivers immediate, actionable persona design guidance.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates reliably on persona and audience definition queries.

## Related Plugins

- **[Persona Mapping](../persona-mapping/)** -- Maps stakeholders across organizations with Power-Interest matrices and RACI charts
- **[User Journey Design](../user-journey-design/)** -- Maps the end-to-end journey for each persona across touchpoints
- **[Outcome Orientation](../outcome-orientation/)** -- Connects persona goals to measurable business outcomes
- **[UX Writing](../ux-writing/)** -- Crafts microcopy tailored to each persona's language and comprehension level

## Version History

- `1.0.10` fix(design+docs): regenerate READMEs for design and documentation plugins
- `1.0.9` fix: add standard keywords and expand READMEs to full format
- `1.0.8` fix: change author field from string to object in all plugin.json files
- `1.0.7` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
