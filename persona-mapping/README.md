# Persona Mapping

> **v1.0.10** | Design & UX | 11 iterations

---

## The Problem

Knowing your users is not enough. Products succeed or fail based on stakeholder dynamics -- who has the power to approve, who has the interest to champion, who must be consulted before decisions, and who gets informed after the fact. A brilliant feature dies because the VP of Engineering was never consulted. A product launch stumbles because the customer success team -- the group most affected -- was merely informed rather than actively involved. A migration stalls because nobody mapped out which stakeholders have both the power to block and the urgency to act.

Teams that skip stakeholder analysis suffer predictable failures. They over-communicate with everyone (equal updates to 30 stakeholders, most of whom do not care) or under-communicate with the wrong people (skip the executive who has veto power). They assign accountability ambiguously -- when everything goes well, five people claim credit; when it fails, nobody was responsible. They miss latent stakeholders who emerge late with legitimate concerns and enough influence to derail the project.

The RACI matrix is the most common stakeholder tool, and the most commonly misused. Teams assign "Responsible" to three people (violating the principle of singular accountability), mark everyone as "Consulted" (creating a bottleneck of approvals), or skip "Informed" entirely (leaving key people surprised by outcomes). Without proper application of the Power-Interest matrix, RACI, and salience modeling, stakeholder management degenerates into political guesswork.

## The Solution

The Persona Mapping plugin gives Claude expertise in stakeholder analysis and persona landscape mapping. It provides the Power-Interest matrix for categorizing stakeholders by influence and engagement, RACI charts for clarifying responsibility, the Salience Model for prioritization based on power, legitimacy, and urgency, stakeholder engagement strategy templates, and the tools to map complex organizational dynamics.

The plugin is a single focused skill that activates when you need to map stakeholders across an organization, assign responsibilities, analyze influence dynamics, or design engagement strategies. It handles the organizational side of product and project work -- who matters, how much, and what you do about it.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Equal communication to all 30 stakeholders -- most ignore it, key ones miss critical info | Power-Interest matrix segments stakeholders into 4 quadrants with appropriate engagement per quadrant |
| Three people marked "Responsible" for the same decision, nobody actually owns it | RACI with single Accountable per task, clear Responsible assignment, and explicit Informed vs Consulted |
| Latent stakeholder emerges late with veto power and derails the project | Salience Model identifies stakeholders by power + legitimacy + urgency, surfacing latent threats early |
| Stakeholder engagement is the same cadence and channel for everyone | Per-stakeholder strategy with frequency, channel, and key messages tailored to their quadrant |
| Resistant stakeholders surprise the team during implementation | Attitude tracked (Supportive/Neutral/Resistant) with engagement strategy calibrated to change resistance to neutrality |
| No visibility into who blocks, who champions, who is affected but silent | Complete stakeholder map with influence, interest, attitude, and engagement plan per person |

## Context to Provide

The more you describe who is involved and what they think about the project, the more accurate the stakeholder map. Organizational dynamics are unique to every project; the skill needs your specific context, not a generic org chart.

**What information to include in your prompt:**
- **Who is involved** -- names, roles, and teams. Include both obvious stakeholders (the ones in the room) and peripheral ones (teams affected downstream, executives who may surface later).
- **Decision authority** -- who has the final say? Who can block? Who thinks they have authority but actually does not? Clarifying this upfront helps the skill place people on the Power-Interest matrix correctly.
- **Known attitudes** -- which stakeholders are supportive, neutral, or resistant? Even rough impressions help (e.g., "the VP of Sales is skeptical because she thinks this will change her team's commission structure").
- **Why you are doing this now** -- a migration, a launch, a reorg, a vendor change? The project type determines which risk categories to look for in stakeholder dynamics.
- **What went wrong before (if anything)** -- if previous efforts stalled or surprised you with unexpected blockers, describe that. These patterns often reveal stakeholders who should have been in the "Manage Closely" quadrant.

**What makes results better:**
- Describing relationships between stakeholders, not just listing individuals
- Flagging any ongoing organizational tension or competing priorities
- Indicating which phase of the project you are in (planning vs. mid-execution -- stakeholder dynamics shift)

**What makes results worse:**
- Listing people by name only with no role or context ("map stakeholders: John, Sarah, Mike")
- Providing an org chart without describing how each team relates to the project
- Treating RACI as a formality -- if responsibilities are genuinely contested, say so

**Template prompt:**
```
Map the stakeholders for [project/initiative name].

Project description: [what you are doing and why, in 2-3 sentences]

People involved:
- [Name]: [role], [team]. Attitude: [supportive/neutral/resistant]. Note: [anything unusual about their position or influence]
- [Name]: [role], [team]. Attitude: [...]

Decision-maker (who has final say): [name/role]
Known blockers or concerns: [describe any tension, competing priorities, or past issues]
Timeline: [when key decisions need to be made]

Deliverable needed: [Power-Interest matrix / RACI for specific tasks / full stakeholder engagement plan]
```

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install persona-mapping@skillstack
```

### Prerequisites

None. For creating individual user personas (demographics, goals, pain points), install `persona-definition` alongside this plugin. They complement each other: `persona-definition` for who the users are, `persona-mapping` for who the stakeholders are.

### Verify installation

After installing, test with:

```
Map the stakeholders for a platform migration from monolith to microservices. The backend team (5 engineers) does the migration work. Frontend team (4 engineers) needs to adapt to new APIs -- their lead says they were never consulted. DevOps lead has raised concerns about deployment pipeline compatibility. VP of Product is upset about roadmap delays and escalated to the CTO last week. CTO approved the project and owns budget. Timeline: 6 months, with a decision point on architecture in 4 weeks.
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I need to map stakeholders for a product launch -- we have engineering, design, marketing, sales, customer success, and executive sponsors`
3. The skill creates a Power-Interest matrix placing each stakeholder and recommends engagement levels
4. You receive a RACI chart for launch tasks and per-stakeholder engagement strategies
5. Next, try: `Our CTO is blocking the migration -- help me analyze the stakeholder dynamics and find a path forward`

---

## System Overview

```
persona-mapping/
├── .claude-plugin/
│   └── plugin.json            # Plugin manifest
└── skills/
    └── persona-mapping/
        ├── SKILL.md           # Core skill (Power-Interest, RACI, Salience Model, engagement templates)
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

A single skill with no additional references. The SKILL.md contains the complete persona mapping framework: Power-Interest matrix, RACI definitions, Salience Model, and stakeholder engagement templates.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `persona-mapping` | Skill | Power-Interest matrix, RACI charts, Salience Model, stakeholder engagement strategies |

### Component Spotlight

#### persona-mapping (skill)

**What it does:** Activates when you need to map stakeholders, assign responsibilities, or analyze influence dynamics for projects and products. Provides the Power-Interest matrix for segmentation, RACI for role clarity, the Salience Model for prioritization, and engagement strategy templates per stakeholder.

**Input -> Output:** A project or initiative with its stakeholder landscape -> Stakeholder map with Power-Interest placement, RACI chart, salience classification, and per-stakeholder engagement strategy.

**When to use:**
- Mapping stakeholders for a new project or initiative
- Assigning RACI responsibilities for cross-functional work
- Analyzing blockers and influence dynamics
- Designing engagement strategies for different stakeholder types
- Identifying latent stakeholders who could emerge as risks

**When NOT to use:**
- Creating individual user personas with demographics, goals, and empathy maps (use `persona-definition`)
- Designing user journeys across touchpoints (use `user-journey-design`)
- Prioritizing features or initiatives (use `prioritization`)
- Assessing project risks beyond stakeholder dynamics (use `risk-management`)

**Try these prompts:**

```
Map stakeholders for a company-wide migration from monolith to microservices -- engineering, product, DevOps, QA, and executive leadership are involved
```

```
Create a RACI chart for our product launch: design needs to deliver assets, marketing writes copy, engineering deploys, PM coordinates, and the VP approves
```

```
Our data science team's project keeps getting blocked by the security team. Help me analyze the power dynamics and find a resolution path.
```

```
Identify latent stakeholders for an API deprecation that affects 200 external customers -- who might emerge late to block this?
```

```
The CEO is High Power / Low Interest in our project. How do we keep them satisfied without over-communicating?
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help me with my team" | "Map stakeholders for a data platform migration affecting 4 teams with competing priorities" |
| "Who should I talk to?" | "Who are the High Power / High Interest stakeholders for our API redesign, and what's the engagement strategy for each?" |
| "Make a RACI" | "Create a RACI for a product launch: PM coordinates, 2 engineers build, design delivers assets, marketing writes copy, VP approves, support prepares" |
| "I have stakeholder problems" | "Our VP of Sales is resistant to the new pricing model. They have high influence with the CEO. How do I manage this?" |

### Structured Prompt Templates

**For stakeholder mapping:**
```
Map stakeholders for [project/initiative]. Teams involved: [list teams]. Key individuals: [names and roles if known]. Potential blockers: [known resistance or concerns]. The decision-maker is [who has final say].
```

**For RACI creation:**
```
Create a RACI chart for [set of tasks/deliverables]. People involved: [list names and roles]. Each task needs exactly one Accountable. Flag any tasks where responsibility is currently ambiguous.
```

**For influence analysis:**
```
Analyze the stakeholder dynamics around [decision or initiative]. [Person A] has [power level] and is [supportive/resistant]. [Person B] has [power level] and is [neutral]. What's the best engagement strategy to move this forward?
```

### Prompt Anti-Patterns

- **Listing people without roles or context** -- "Map stakeholders: John, Sarah, Mike" gives the skill nothing to work with; provide roles, teams, and known attitudes
- **Confusing individual personas with stakeholder mapping** -- "Create a persona for our engineering manager" is a `persona-definition` task; stakeholder mapping is about organizational dynamics, not individual user profiles
- **Assigning RACI without tasks** -- RACI is task-specific; provide the list of deliverables or decisions that need responsibility assignment

## Real-World Walkthrough

**Starting situation:** You are leading a platform migration from a monolith to microservices at a mid-size company. The project affects five teams: backend engineering (does the migration work), frontend engineering (needs to adapt to new APIs), DevOps (infrastructure changes), product management (feature timeline impact), and executive leadership (budget and strategic alignment). After two months, progress has stalled -- the frontend team claims they were never consulted, the DevOps lead says the architecture does not account for their deployment pipeline, and the VP of Product is asking why the feature roadmap is delayed.

**Step 1: Power-Interest mapping.** You ask: "Map the stakeholders for our monolith-to-microservices migration. Backend engineering is doing the work, frontend says they weren't consulted, DevOps says architecture doesn't fit their pipeline, VP of Product is upset about roadmap delays, and the CTO approved the project."

The skill places stakeholders on the Power-Interest matrix:
- **High Power, High Interest (Manage Closely):** CTO (approved, strategic owner), VP of Product (budget impact, roadmap delay), Backend Tech Lead (technical decisions, doing the work)
- **High Power, Low Interest (Keep Satisfied):** CEO (informed but not tracking details)
- **Low Power, High Interest (Keep Informed):** Frontend Tech Lead (affected but not blocking), QA Lead (testing requirements change)
- **Low Power, Low Interest (Monitor):** Marketing (eventual messaging about platform improvements)

The DevOps Lead is flagged as misplaced -- they have HIGH power (can block deployment) but were treated as low interest. This explains the stall.

**Step 2: RACI assignment.** The skill creates a RACI chart for migration tasks:

| Task | Backend Lead | Frontend Lead | DevOps Lead | VP Product | CTO |
|---|---|---|---|---|---|
| Architecture design | R | C | C | I | A |
| API contract definition | R | C | I | I | I |
| Infrastructure changes | I | I | R | I | A |
| Service decomposition | R | I | C | I | I |
| Timeline communication | I | I | I | R | I |

The skill flags the root cause: Architecture design had DevOps as "Informed" when they should have been "Consulted." Frontend was "Informed" on API contracts when they should have been "Consulted." Both teams were cut out of decisions that directly affected their work.

**Step 3: Salience analysis.** The skill applies the Salience Model:
- **Definitive (Power + Legitimacy + Urgency):** CTO, Backend Tech Lead -- both have power, legitimate stake, and urgent involvement. These are the primary decision-makers.
- **Dominant (Power + Legitimacy):** VP of Product, DevOps Lead -- power and legitimate stake, but urgency varies. Must be actively managed.
- **Dependent (Legitimacy + Urgency):** Frontend Tech Lead -- legitimate stake and affected urgently, but limited power to block. Must be given voice.
- **Latent (single attribute):** QA Lead -- legitimate stake only. Monitor and include when testing phase approaches.

**Step 4: Engagement strategy per stakeholder.** The skill designs tailored engagement:
- CTO: Weekly 15-min sync, focus on strategic alignment and blockers, decision authority on architectural conflicts
- VP of Product: Bi-weekly roadmap impact update, focus on timeline and feature tradeoffs, share revised timeline
- DevOps Lead: Immediate architectural review session (fix the consultation gap), then weekly in architecture meetings
- Frontend Tech Lead: Invited to API contract reviews, async updates on migration progress, monthly demo of new APIs
- Backend Tech Lead: Daily standups, owns technical decisions within CTO's architectural guardrails

**Step 5: Resolving the stall.** The skill identifies three actions to unstall the project:
1. Conduct an architectural review with DevOps to address deployment pipeline concerns (they were never consulted)
2. Schedule API contract review sessions with frontend before finalizing (they were never consulted)
3. Send VP of Product a revised timeline that accounts for the consultation gaps

**Final outcome:** A complete stakeholder map with Power-Interest placement, RACI chart exposing the consultation gaps, Salience Model identifying decision-maker tiers, and per-stakeholder engagement strategies. The root cause of the stall was a RACI error: two "Consult" stakeholders were marked "Inform."

**Gotchas discovered:** The DevOps Lead's placement as "Low Interest" was incorrect -- they had high interest but no voice. The Power-Interest matrix exposed this when the skill cross-checked power (ability to block deployment) against actual engagement level.

## Usage Scenarios

### Scenario 1: Product launch RACI

**Context:** You are launching a new product feature. Design, engineering, marketing, sales, customer success, and an executive sponsor are involved. Previous launches had confusion about who approved the go-live decision.

**You say:** "Create a RACI for our feature launch. Who approves go-live? Last time, three people thought they had veto power."

**The skill provides:**
- RACI chart with tasks: design delivery, engineering deployment, marketing launch content, sales enablement, customer success preparation, go-live decision
- Single Accountable for go-live: the executive sponsor (not three people)
- Clear Consulted vs Informed distinction for each team per task
- Escalation path: if any Consulted party raises a blocking concern, it escalates to the Accountable

**You end up with:** An unambiguous responsibility matrix where everyone knows their role and exactly one person makes the go-live decision.

### Scenario 2: Managing a resistant executive

**Context:** The VP of Sales opposes your new pricing model. They have high influence with the CEO and have been voicing concerns in leadership meetings. The project is at risk of being killed.

**You say:** "Our VP of Sales is resistant to the new pricing model and has the CEO's ear. How do I manage this stakeholder to avoid the project being killed?"

**The skill provides:**
- Power-Interest placement: High Power, High Interest -- requires "Manage Closely"
- Attitude: Resistant -- engagement strategy calibrated to move from resistant to neutral (not necessarily supportive)
- Tactics: understand their specific objection (revenue risk? commission impact? customer pushback?), address with data, offer a pilot that limits risk, bring them into the decision process rather than presenting a fait accompli
- Warning: do NOT escalate to CEO without first engaging the VP directly -- going around a high-power stakeholder creates an enemy

**You end up with:** A stakeholder engagement plan for a specific resistant executive, with tactics calibrated to their power level and objections.

### Scenario 3: Identifying latent stakeholders

**Context:** You are deprecating a public API that 200 customers use. You have mapped the internal stakeholders but suspect there are external stakeholders who could emerge late to block the deprecation.

**You say:** "We're deprecating an API used by 200 customers. Internal stakeholders are mapped. Who are the latent external stakeholders we might miss?"

**The skill provides:**
- Latent stakeholder identification: high-revenue customers who built critical workflows on the API, partner companies with deep integrations, developer community influencers who will publicize the deprecation
- Salience: these are "Dormant" (power only) -- they have the power to escalate via contracts, social media, or executive relationships, but no urgency until the deprecation timeline is announced
- Engagement strategy: proactive outreach to top 20 customers before public announcement, migration support plan, extended timeline for high-impact integrations
- Risk: if these stakeholders learn about the deprecation from the public announcement rather than direct outreach, they move from Dormant to Definitive instantly

**You end up with:** A list of latent external stakeholders with proactive engagement strategy to prevent late-stage project derailment.

---

## Decision Logic

**When Power-Interest vs RACI vs Salience?**

- **Power-Interest matrix** -- use at project start to categorize all stakeholders and determine engagement levels. Quick, visual, and effective for initial mapping.
- **RACI chart** -- use for specific tasks or deliverables where role clarity is needed. Most valuable when confusion exists about who decides, who does the work, and who is merely informed.
- **Salience Model** -- use when stakeholders have different combinations of power, legitimacy, and urgency. More nuanced than Power-Interest for complex organizational dynamics with evolving stakeholder salience.

Use all three for large cross-functional projects. Use Power-Interest alone for simpler initiatives.

**When this skill vs persona-definition?**

`persona-mapping` maps stakeholders and their organizational dynamics (power, interest, responsibility). `persona-definition` creates individual user profiles (goals, pain points, behaviors). Use persona-mapping for project and organizational work; use persona-definition for product and design work.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Multiple Accountables per task | Confusion about who makes the final decision; decisions are delayed or contradictory | Enforce single Accountable rule; if contested, escalate to the project sponsor to assign |
| Everyone marked Consulted | Every decision requires 8 approvals; project speed grinds to halt | Reduce Consulted to those with legitimate expertise; most stakeholders should be Informed |
| Latent stakeholders emerge late | A VP who was never mapped shows up in week 8 with veto power and new requirements | Rerun stakeholder mapping quarterly; explicitly ask "who else could be affected?" at each phase gate |
| Ignoring resistant stakeholders | Resistant stakeholder sabotages the project through back-channel influence | Engage resistant stakeholders early with their specific objections; move them to neutral, not necessarily supportive |
| Static map in a dynamic environment | Stakeholder power shifts (reorganization, new hire, departure) and the map becomes outdated | Review stakeholder map at each project milestone; update when organizational changes occur |

## Ideal For

- **Project managers** running cross-functional initiatives who need clarity on who decides, who is consulted, and who is informed
- **Product leaders** navigating organizational politics around new products, pricing changes, or platform migrations
- **Engineering leads** managing stakeholder expectations for technical projects that affect multiple teams
- **Program managers** designing communication plans calibrated to stakeholder power and interest levels
- **Founders** managing investor, board, and team dynamics during strategic decisions

## Not For

- **Individual user persona creation** -- demographics, goals, pain points, and empathy maps use `persona-definition`
- **User journey design** -- touchpoint mapping and experience flow design uses `user-journey-design`
- **Feature prioritization** -- deciding what to build first uses `prioritization`

## Related Plugins

- **persona-definition** -- complementary: persona-mapping handles organizational stakeholders, persona-definition handles product users
- **risk-management** -- stakeholder risks are one input to broader project risk assessment
- **prioritization** -- stakeholder input informs what to prioritize, but the frameworks are separate
- **outcome-orientation** -- stakeholder alignment is critical for defining outcomes that the organization will pursue

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
