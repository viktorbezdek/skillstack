# Persona Definition

> **v1.0.10** | Design & UX | 11 iterations

---

## The Problem

Products built for "everyone" satisfy no one. Without defined user personas, teams make design decisions based on assumptions, internal preferences, and whoever is loudest in the room. The developer builds for developers. The designer builds for designers. The PM builds for the CEO. Each stakeholder imagines a different user, and the product reflects this fragmentation -- inconsistent complexity levels, conflicting feature priorities, and documentation that speaks to no one specifically.

The consequences are measurable. Onboarding flows assume expert knowledge because the team forgot about beginners. Features accumulate without a clear mental model of who needs them and why. Marketing messages try to appeal to everyone and resonate with no one. Customer support handles the same confusion repeatedly because the product was designed for an imaginary user who does not match any real customer segment.

Most teams that attempt persona work either skip it entirely ("we know our users") or produce unusable artifacts. Demographic-only personas ("Sarah, 32, marketing manager") provide no actionable guidance because they describe who the user is but not what they need, what frustrates them, or how they make decisions. Aspirational personas describe the users the team wishes they had rather than the users they actually serve. Teams create 12 personas and use none of them because the set is too large to remember and too vague to apply.

## The Solution

The Persona Definition plugin gives Claude expertise in creating research-backed user personas that drive product, design, and documentation decisions. It covers three persona types matched to project stage (proto-persona for quick alignment, lean persona for agile MVPs, full persona for strategic decisions), five core components (demographics, goals, pain points, behaviors, context), empathy mapping, and a structured persona template.

The plugin provides a single focused skill that activates when you need to define target users, create customer archetypes, or build empathy maps. It enforces the critical distinctions that make personas useful: goals over demographics, pain points over features, behaviors over assumptions, and a manageable set (3-5) over an exhaustive catalog.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Design decisions based on whoever is loudest in the room | Decisions anchored to defined personas with documented goals and pain points |
| Personas are demographic-only: "Sarah, 32, marketing manager" with no actionable guidance | Five-component personas: demographics, goals, pain points, behaviors, and context |
| 12 personas created, none used -- too many to remember | 3-5 focused personas matched to actual user segments with clear differentiation |
| Aspirational personas describe wished-for users, not actual ones | Research-backed personas grounded in real user behavior and evidence |
| No empathy mapping -- team cannot articulate what users think vs feel vs do | Structured empathy map: Says, Thinks, Does, Feels quadrants per persona |
| Personas created once and never updated as the product and user base evolve | Anti-pattern awareness: static personas flagged as a known failure mode |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install persona-definition@skillstack
```

### Prerequisites

None. For mapping personas across stakeholder landscapes, also install `persona-mapping`. For designing journeys for defined personas, also install `user-journey-design`.

### Verify installation

After installing, test with:

```
Create personas for a developer documentation platform used by junior developers, senior architects, and DevOps engineers
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I need to define the target users for our new API management product -- we serve individual developers and enterprise platform teams`
3. The skill creates differentiated personas for each user segment with goals, pain points, and behaviors
4. You receive structured persona documents with empathy maps and documentation needs
5. Next, try: `Our onboarding flow assumes expert knowledge -- help me create a beginner persona so we can redesign it`

---

## System Overview

```
persona-definition/
├── .claude-plugin/
│   └── plugin.json            # Plugin manifest
└── skills/
    └── persona-definition/
        ├── SKILL.md           # Core skill (persona types, components, empathy map, templates, anti-patterns)
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

A single skill with no additional references. The SKILL.md contains the complete persona definition framework: three persona types, five core components, empathy map structure, the persona template, and anti-patterns.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `persona-definition` | Skill | Persona types, core components, empathy mapping, persona template, anti-pattern detection |

### Component Spotlight

#### persona-definition (skill)

**What it does:** Activates when you need to create user personas, define target audiences, or build empathy maps. Provides three persona types matched to project stage, five core components for each persona, the empathy map framework (Says/Thinks/Does/Feels), a structured template, and anti-pattern detection.

**Input -> Output:** A description of your product and user segments -> Structured personas with demographics, goals, pain points, behaviors, context, and empathy maps, sized appropriately (proto, lean, or full).

**When to use:**
- Defining target users for a new product or feature
- Creating customer archetypes for marketing and positioning
- Building empathy maps to understand user motivations
- Reviewing existing personas that feel stale or unusable
- Aligning a team around who they are building for

**When NOT to use:**
- Mapping stakeholders across an organization with influence and power analysis (use `persona-mapping`)
- Designing user journeys and touchpoints (use `user-journey-design`)
- Writing user-facing copy and microcopy (use `ux-writing`)
- Prioritizing which persona to serve first (use `prioritization`)

**Try these prompts:**

```
Create personas for a project management tool used by freelancers, small agency teams, and enterprise PMOs
```

```
Build an empathy map for a first-time user of our developer CLI tool -- they just installed it and don't know where to start
```

```
Our current personas are just demographics (name, age, job title). Help me add goals, pain points, and behaviors to make them actionable.
```

```
I need a quick proto-persona for a hackathon project -- we're building a meeting summarizer for remote teams
```

```
Review our 8 personas -- we suspect there's overlap and the set is too large to be useful
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "I need users" | "Create 3 personas for a B2B analytics dashboard used by data analysts, engineering managers, and C-suite executives" |
| "Who is our target audience?" | "Define the target user for a code review tool -- primarily senior engineers at mid-size startups, but also used by junior developers" |
| "Make me a persona" | "Build a full persona for a DevOps engineer who evaluates and adopts monitoring tools for their team" |
| "Help with empathy mapping" | "Create an empathy map for a non-technical product manager who uses our API documentation to understand integrations" |

### Structured Prompt Templates

**For new persona creation:**
```
Create [proto/lean/full] personas for [product type]. User segments: [segment 1, segment 2, segment 3]. Each persona needs: goals (what they want to achieve), pain points (what blocks them), and behaviors (how they work today). Product context: [what the product does].
```

**For empathy mapping:**
```
Build an empathy map for [persona type] using [product]. They are trying to [task]. Their experience level with [domain] is [beginner/intermediate/expert]. Focus on the gap between what they say they want and what they actually do.
```

**For persona review:**
```
Review these personas: [list or paste existing personas]. Check for: overlap between personas, missing goals/pain points, demographic-only definition, aspirational bias. Recommend consolidation or enhancement.
```

### Prompt Anti-Patterns

- **Describing features instead of users** -- "I need a persona for someone who uses our dashboard filters" describes a feature, not a user; describe the person's role, goals, and context instead
- **Requesting only demographics** -- age, job title, and location are insufficient; always ask for goals, pain points, and behaviors
- **Creating too many personas** -- 3-5 is the practical maximum; more than 5 means segments overlap or are too granular
- **Building aspirational personas** -- describe users as they ARE, not as you wish they were; if you want expert users but serve beginners, the persona should reflect beginners

## Real-World Walkthrough

**Starting situation:** You are building a cloud cost optimization platform. The sales team says "our users are DevOps engineers," but the product team suspects there are multiple distinct user types with different needs. Support tickets show confusion from both technical and non-technical users, and the onboarding flow assumes deep cloud infrastructure knowledge.

**Step 1: Identifying segments.** You ask: "Help me define personas for a cloud cost optimization platform. Sales says 'DevOps engineers' but support tickets show both deeply technical and non-technical users struggling."

The skill identifies three likely segments from the description: (1) the DevOps/platform engineer who implements and operates the tool, (2) the engineering manager who uses reports to make staffing and architecture decisions, and (3) the finance/FinOps analyst who needs cost data without infrastructure knowledge. These are differentiated by goals, technical depth, and decision authority.

**Step 2: Building the first persona.** The skill creates a full persona for the platform engineer:

"Alex, Platform Engineer" -- Tech Savvy: 5/5 -- Primary goal: reduce cloud spend without sacrificing reliability or development velocity. Pain points: cost dashboards show raw data but no actionable recommendations, alerts fire too late (after the bill is generated), and implementing changes requires understanding 3 different cloud provider consoles. Behaviors: checks costs weekly, responds to alerts reactively, prefers CLI and API access over dashboards, evaluates tools by trying free tiers before involving procurement.

**Step 3: Empathy mapping.** The skill constructs the empathy map for Alex:
- Says: "I need to cut our cloud bill by 20% this quarter"
- Thinks: "If I resize these instances I might break the deployment pipeline -- is it worth the risk?"
- Does: Checks spot instance pricing manually, creates spreadsheets to track savings, avoids changes before release cycles
- Feels: Pressure from management to cut costs, anxiety about causing outages, frustration that cost tools don't understand their deployment patterns

The gap between Says and Does is revealing: Alex says they want to cut costs but avoids making changes due to reliability anxiety. The product needs to address the risk-of-change fear, not just show cost data.

**Step 4: Second persona -- the manager.** "Jordan, Engineering Manager" -- Tech Savvy: 3/5 -- Primary goal: understand where money is going and justify infrastructure decisions to leadership. Pain points: cost reports are too granular (instance-level) when they need team-level and service-level views, cannot correlate cost increases with specific product decisions, reports need manual export for executive presentations. Behaviors: reviews costs monthly, delegates implementation to platform team, makes decisions based on trends not real-time data.

**Step 5: Third persona -- the FinOps analyst.** "Morgan, FinOps Analyst" -- Tech Savvy: 2/5 -- Primary goal: allocate cloud costs to business units and forecast monthly spend. Pain points: tagging is inconsistent so cost allocation is manual, no understanding of what a "t3.xlarge" is or why it costs what it does, needs to produce reports for finance that translate technical resources into business cost centers. Behaviors: works in spreadsheets, requests data from engineering rather than self-serving, evaluates tools by reporting capabilities.

**Step 6: Anti-pattern review.** The skill checks the persona set:
- Not aspirational? Confirmed -- each persona reflects real segments observed in support tickets
- 3-5 personas? Yes -- 3 personas with clear differentiation
- More than demographics? Yes -- each has goals, pain points, behaviors, and context
- Static risk? Flagged -- these should be updated quarterly as the product evolves and user base shifts

**Final outcome:** Three differentiated personas with empathy maps, covering the technical implementer, the management decision-maker, and the non-technical analyst. Each persona provides clear guidance for feature prioritization (Alex needs CLI/API, Jordan needs team-level views, Morgan needs business-unit reports), onboarding design (three different paths by technical depth), and documentation strategy (three different content levels).

**Gotchas discovered:** The empathy map revealed that the platform engineer's core blocker is reliability anxiety, not lack of cost data. This insight redirects product strategy from "better dashboards" to "safe, reversible cost optimization with rollback."

## Usage Scenarios

### Scenario 1: Quick alignment for a hackathon project

**Context:** You have 48 hours to build a meeting summarizer for remote teams. You need a proto-persona to align the team quickly without extensive research.

**You say:** "I need a quick proto-persona for a meeting summarizer product -- our target is remote team leads who have too many meetings."

**The skill provides:**
- Proto-persona (low detail, high speed): "Taylor, Remote Team Lead" -- 10+ meetings/week, primary goal is to stop attending meetings just for the notes, pain point is missing action items from meetings they skip
- Key behavioral insight: Taylor forwards meeting recordings to junior team members and asks for summaries -- they're already working around the problem manually
- Documentation preference: bullet-point summaries with action items highlighted, not transcripts

**You end up with:** An aligned team vision in 5 minutes -- everyone knows who Taylor is and what Taylor needs.

### Scenario 2: Making existing personas actionable

**Context:** Your team has 6 personas that are just demographic profiles: name, age, job title, company size. Nobody uses them because they don't inform any decisions.

**You say:** "Enhance these demographic-only personas with goals, pain points, and behaviors. Here are the 6: [names and titles]."

**The skill provides:**
- Review finding: 2 of the 6 personas overlap significantly (same goals, same pain points, different demographics)
- Recommendation: consolidate to 4 personas
- For each: added primary and secondary goals, 3 specific pain points, key behaviors, and documentation needs
- Empathy maps highlighting the gap between what each persona says vs does

**You end up with:** 4 actionable personas with clear decision-guiding content, down from 6 demographic-only profiles nobody used.

### Scenario 3: Designing for a persona you forgot

**Context:** Your product's onboarding has a 30% completion rate. You realize the onboarding was designed for expert users, but most signups are beginners trying the product for the first time.

**You say:** "Our onboarding assumes expertise but most new signups are beginners. Help me create a beginner persona so we can redesign the flow."

**The skill provides:**
- Beginner persona: "Sam, Curious Evaluator" -- Tech Savvy: 2/5 -- heard about the product from a colleague, has no domain expertise, evaluating against 3 competitors
- Pain points: onboarding uses jargon without explanation, first-value takes 20 minutes (competitors show value in 3), cannot tell if the product is "for people like me"
- Key behavior: abandons at step 3 (configuration), never reaches the core feature
- Empathy map: Says "this looks powerful" / Thinks "I don't even know where to start" / Does clicks the first button and gets lost / Feels overwhelmed and considers switching to competitor

**You end up with:** A beginner persona that explains the 30% completion rate and provides specific guidance for redesigning the onboarding flow.

---

## Decision Logic

**Which persona type to use?**

- **Proto-persona** (low detail) -- when you need quick team alignment without research investment. Hackathons, early-stage startups, initial brainstorming. Replace with lean/full personas when real data becomes available.
- **Lean persona** (medium detail) -- when you are building an MVP or running an agile process that needs actionable personas without exhaustive research. Startups, small teams, rapid iteration.
- **Full persona** (high detail) -- when making strategic decisions: product positioning, major redesigns, enterprise sales strategy, multi-year roadmaps. Requires real user research data.

**How many personas?**

3-5 for most products. Fewer than 3 usually means you have not differentiated your segments. More than 5 usually means segments overlap and should be consolidated. Test: if two personas would make the same decision in every product scenario, they are the same persona.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Aspirational personas | Personas describe expert power users but product serves mostly beginners | Rebuild from actual user data: support tickets, usage analytics, interview transcripts |
| Too many personas | 8+ personas, team cannot remember or apply them | Consolidate by merging personas with the same goals/pain points; target 3-5 |
| Demographic-only | Persona has name, age, title but no goals, pain points, or behaviors | Add the five core components: demographics, goals, pain points, behaviors, context |
| Static personas | Personas created 2 years ago, never updated as product and users evolved | Schedule quarterly reviews; update when user segments shift or new segments emerge |
| No differentiation | All personas want the same thing, experience the same pain points | Reevaluate segmentation criteria; differentiate by goals and constraints, not just job title |

## Ideal For

- **Product managers** defining target users to guide feature prioritization and roadmap decisions
- **Designers** building empathy maps and user understanding before designing interfaces
- **Marketing teams** creating customer archetypes for positioning, messaging, and content strategy
- **Founders** aligning the team around who the product serves in early-stage development
- **Documentation teams** understanding audience technical levels to calibrate content depth

## Not For

- **Stakeholder mapping across organizations** -- influence analysis, RACI charts, and power-interest matrices use `persona-mapping`
- **User journey mapping** -- designing touchpoints and experience flows for defined personas uses `user-journey-design`
- **UX copy and microcopy** -- writing persona-appropriate interface text uses `ux-writing`

## Related Plugins

- **persona-mapping** -- mapping personas and stakeholders across organizational power structures
- **user-journey-design** -- designing experience journeys for defined personas
- **ux-writing** -- writing interface text calibrated to persona technical level
- **outcome-orientation** -- defining outcomes that matter to each persona
- **prioritization** -- deciding which persona's needs to address first

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
