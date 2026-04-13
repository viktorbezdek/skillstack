# Persona Mapping

> **v1.0.10** | Design & UX | 11 iterations

> Map stakeholders by influence, interest, and responsibility using Power-Interest matrices, RACI charts, and salience models -- know who matters, who decides, and who blocks.

## The Problem

Every project has stakeholders, and most teams manage them badly. The VP of Engineering has strong opinions about the tech stack but no formal role on the project. The compliance team can block the launch but nobody told them about the timeline. The product designer is listed as "responsible" for the UX but three different directors have sign-off authority. Without explicit stakeholder mapping, teams discover these dynamics through painful surprises: a launch blocked by a stakeholder nobody consulted, a feature redesigned because the wrong person was treated as the decision-maker, or a meeting that drags on because everyone thinks they are accountable.

The RACI matrix is supposed to solve this, but most teams create one at the project kickoff and never look at it again. Worse, they assign RACI roles based on org chart titles rather than actual influence. The person with the "Director" title gets marked as Accountable, but the senior IC with 10 years of domain expertise is the one whose opinion actually determines the outcome. Power and interest do not follow org charts, and stakeholder mapping that ignores this reality is worse than no mapping at all -- it gives false confidence.

The result: communication goes to the wrong people, decisions stall because the actual decision-maker was not in the room, and resistant stakeholders become blockers late in the project when changes are expensive. Teams spend more time navigating politics than they would have spent mapping the landscape upfront.

## The Solution

This plugin provides a structured toolkit for stakeholder analysis that goes beyond simple RACI assignments. It combines three complementary frameworks: the Power-Interest matrix for prioritizing engagement (manage closely vs. keep informed vs. monitor), the RACI matrix for clarifying roles per deliverable, and the salience model for triaging stakeholders by power, legitimacy, and urgency.

You get a stakeholder template that captures not just role and responsibility but attitude (supportive/neutral/resistant) and engagement strategy (frequency, channel, key messages). This turns stakeholder mapping from a one-time exercise into an actionable communication plan. The skill produces explicit engagement strategies: who to manage closely, who to keep satisfied, who to keep informed, and who to simply monitor.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Stakeholders discovered mid-project when they block progress | Power-Interest matrix identifies all stakeholders and their influence upfront |
| Everyone thinks they are the decision-maker; decisions stall | RACI assigns exactly one Accountable per deliverable |
| Communicate the same way to everyone (all-hands email) | Tailored engagement strategies by stakeholder quadrant |
| Resistant stakeholders surface objections at launch time | Attitude mapping (supportive/neutral/resistant) with early engagement plans |
| Org chart titles drive role assignment, not actual influence | Salience model maps real power, legitimacy, and urgency regardless of title |
| Stakeholder analysis done once at kickoff and never updated | Living stakeholder map with engagement cadence and update triggers |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install persona-mapping@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your project and stakeholder landscape:
   ```
   Map the stakeholders for a platform migration project -- we're moving from a monolith to microservices and it affects engineering, product, QA, DevOps, and the CTO's office
   ```
3. The skill produces a Power-Interest matrix, RACI chart for key deliverables, and engagement strategies for each stakeholder group.
4. Drill into specific stakeholder dynamics:
   ```
   The VP of Infrastructure is resistant to the migration -- how should I manage this stakeholder?
   ```
5. Get an engagement strategy with frequency, channel, key messages, and tactics for converting resistance.

## What's Inside

Compact single-skill plugin focused on stakeholder analysis and organizational mapping.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering Power-Interest matrix, RACI matrix with role definitions, stakeholder template with engagement strategy, and salience model (power/legitimacy/urgency) |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### persona-mapping

**What it does:** Activates when you need to map stakeholders, create RACI charts, analyze influence dynamics, prioritize communication, or understand organizational power structures for a project. It provides three complementary frameworks (Power-Interest, RACI, salience model) and produces actionable engagement plans for each stakeholder.

**Try these prompts:**

```
Create a RACI matrix for our product launch -- the deliverables are feature spec, design, implementation, QA, and go-to-market
```

```
Map the stakeholders for our API redesign project using a Power-Interest matrix
```

```
I have 15 stakeholders for this initiative and I don't know who to prioritize. Help me use the salience model to triage them.
```

```
The legal team keeps blocking our releases with last-minute reviews. How do I map and manage this stakeholder?
```

```
Design an engagement strategy for a platform migration that spans 4 teams and 3 VPs with competing priorities
```

```
Our RACI has 5 people marked as Accountable for the same deliverable. Fix this.
```

## Real-World Walkthrough

You are leading a company-wide data platform migration at a 500-person fintech company. The project replaces the legacy data warehouse with a modern lakehouse architecture. It touches every team that uses data -- analytics, data science, product, finance, compliance, and engineering infrastructure. You have been told to "just coordinate with stakeholders" but nobody has defined who those stakeholders are or what "coordinate" means.

**Step 1: Identify and map stakeholders.**

You describe the situation:

```
Map the stakeholders for a data platform migration at a fintech company. Teams affected: data engineering (owns the old warehouse), analytics (daily users), data science (ML pipelines), product (dashboards), finance (regulatory reporting), compliance (audit trails), and infrastructure (hosting). Executives: CTO, VP Data, VP Product.
```

The skill produces a Power-Interest matrix with all stakeholders placed:

**High Power, High Interest (Manage Closely):**
- VP Data -- owns the budget and the migration timeline
- Data Engineering lead -- team doing the migration work
- Compliance director -- regulatory requirements are non-negotiable

**High Power, Low Interest (Keep Satisfied):**
- CTO -- cares about outcome, not daily decisions
- VP Product -- affected by dashboard downtime during migration

**Low Power, High Interest (Keep Informed):**
- Analytics team -- heavy daily users worried about disruption
- Data scientists -- ML pipelines need to migrate without breaking models
- Finance team -- regulatory reports must continue uninterrupted

**Low Power, Low Interest (Monitor):**
- Infrastructure team -- affected only by hosting changes
- Product managers -- indirect impact through dashboard changes

**Step 2: Build the RACI matrix.**

You ask for role clarity:

```
Create a RACI chart for the migration with these deliverables: migration plan, data model redesign, pipeline migration, testing, cutover, and stakeholder communication
```

The skill produces a RACI matrix:

| Deliverable | VP Data | DE Lead | Analytics | Compliance | CTO |
|-------------|---------|---------|-----------|------------|-----|
| Migration plan | A | R | C | C | I |
| Data model redesign | I | A, R | C | C | I |
| Pipeline migration | I | A, R | I | I | I |
| Testing | I | R | R | A | I |
| Cutover | A | R | I | C | I |
| Stakeholder comms | A | R | I | I | I |

The skill flags that Testing has compliance as Accountable -- they have sign-off authority on data integrity for regulatory reporting. If the DE lead were Accountable for testing, compliance could still block the cutover, creating a hidden governance gap. Making compliance explicitly Accountable for testing ensures they are involved early, not as a last-minute gate.

**Step 3: Apply the salience model.**

You need to prioritize among 12 stakeholders for your limited communication bandwidth. You ask:

```
Use the salience model to triage my 12 stakeholders. I can't give everyone the same attention.
```

The skill applies the three-attribute salience model:

- **Definitive (Power + Legitimacy + Urgency):** VP Data, Compliance director -- these stakeholders can act immediately, have legitimate claims, and care about the timeline. They get weekly 1:1 updates.
- **Dominant (Power + Legitimacy):** CTO, VP Product -- they have authority and legitimate interest but are not urgent. Monthly executive summaries.
- **Dependent (Legitimacy + Urgency):** Analytics team, Finance team -- they have urgent needs and legitimate concerns but no power to change the project. Weekly status emails with FAQ.
- **Latent (Single attribute):** Infrastructure team -- they have some power but no urgency or strong interest. Notify before changes.

**Step 4: Design engagement strategies for resistant stakeholders.**

The analytics team lead is vocally resistant to the migration because the last platform change broke their dashboards for two weeks. You ask:

```
The analytics lead is resistant -- they don't trust that the migration won't break their dashboards again. Design an engagement strategy.
```

The skill produces a targeted engagement plan:

- **Attitude:** Resistant (based on past experience, not irrational)
- **Frequency:** Bi-weekly 1:1 meetings during migration planning, weekly during cutover
- **Channel:** Direct meetings, not email (resistance needs dialogue, not broadcasts)
- **Key messages:** Emphasize what is different this time (parallel running, rollback plan, their team involved in testing)
- **Conversion tactic:** Give the analytics team a role in the testing phase. People who test the migration trust the migration.

**Step 5: Create the stakeholder communication plan.**

With all mapping complete, the skill produces a consolidated communication plan:

| Stakeholder | Cadence | Channel | Content |
|-------------|---------|---------|---------|
| VP Data | Weekly 1:1 | In-person | Risks, decisions needed, budget status |
| Compliance | Weekly report | Email + meeting | Data integrity tests, audit trail status |
| CTO | Monthly summary | Slide deck | Progress, timeline, ROI |
| Analytics team | Bi-weekly | Stand-up | Migration timeline, testing participation |
| Data scientists | Weekly email | Slack + email | Pipeline migration schedule, breaking changes |

The result: a complete stakeholder landscape mapped by power, interest, and salience, with a RACI chart that clarifies who decides what, engagement strategies tailored to each stakeholder's attitude and influence, and a communication plan that ensures the right people get the right information at the right frequency. The analytics lead's resistance is addressed through involvement rather than broadcast communication, and compliance is embedded in testing rather than surfacing as a last-minute blocker.

## Usage Scenarios

### Scenario 1: Creating a RACI for a new project

**Context:** You are kicking off a product launch with design, engineering, marketing, and executive stakeholders. Nobody is clear on who decides what.

**You say:** "Create a RACI matrix for our product launch. Deliverables: PRD, design specs, implementation, QA sign-off, marketing plan, and launch decision."

**The skill provides:**
- RACI matrix with exactly one Accountable per deliverable
- Identification of where multiple Accountables would create conflicts
- Recommendations for where to add Consulted roles to prevent surprises
- Governance gaps where no one is Accountable

**You end up with:** A clear responsibility matrix that prevents "I thought you were handling that" conversations and ensures every deliverable has a single decision-maker.

### Scenario 2: Managing executive stakeholders

**Context:** Your project has three VP-level sponsors with different priorities. They each think they are the most important stakeholder.

**You say:** "I have three VPs involved in this project and they all want different things. How do I map their influence and manage the conflicts?"

**The skill provides:**
- Power-Interest placement for each VP
- Salience model analysis: which VP has power + legitimacy + urgency (definitive)
- Engagement strategy per VP with tailored messaging
- Conflict resolution approach when priorities clash

**You end up with:** A stakeholder hierarchy that clarifies which VP's priorities take precedence, with engagement strategies that keep all three satisfied without letting any one dominate.

### Scenario 3: Fixing a broken RACI

**Context:** Your existing RACI has every senior person marked as Accountable, multiple Responsibles with no clear lead, and no one Consulted from the compliance team.

**You say:** "Our RACI is a mess -- 4 people are Accountable for the design spec and compliance isn't listed anywhere. Fix it."

**The skill provides:**
- Diagnosis: multiple Accountables means no one is accountable; missing compliance creates a hidden blocker
- Fixed RACI with single Accountable per deliverable
- Added compliance as Consulted on deliverables that affect regulated data
- Escalation path for when the Accountable person is unavailable

**You end up with:** A working RACI that resolves decision-making paralysis and prevents compliance from becoming a last-minute blocker.

## Ideal For

- **Project managers coordinating across multiple teams** -- Power-Interest matrices and RACI charts prevent the stakeholder surprises that derail timelines
- **Technical leads navigating organizational politics** -- salience model identifies who actually has influence, regardless of org chart titles
- **Product managers managing executive stakeholders** -- engagement strategies tailored to each stakeholder's power, interest, and attitude
- **Anyone whose RACI chart has more than one Accountable** -- the skill enforces the one-A rule that prevents decision paralysis
- **Change managers driving adoption of new tools or processes** -- resistance mapping and conversion tactics address skeptics before they become blockers

## Not For

- **Creating individual user personas or customer archetypes** -- use [persona-definition](../persona-definition/) for demographics, goals, pain points, and empathy maps
- **Designing user journeys and touchpoint maps** -- use [user-journey-design](../user-journey-design/) for end-to-end experience flows
- **Prioritizing features or backlog items** -- use [prioritization](../prioritization/) for RICE, MoSCoW, and effort-impact frameworks

## How It Works Under the Hood

The skill is a compact, focused knowledge base covering three complementary stakeholder analysis frameworks. The SKILL.md provides: the Power-Interest matrix with four quadrants (manage closely, keep satisfied, keep informed, monitor), the RACI matrix with strict role definitions and the one-Accountable rule, a stakeholder template capturing influence, interest, attitude, and engagement strategy, and the salience model (power/legitimacy/urgency) for stakeholder triaging.

There are no additional reference files -- the skill is deliberately compact so it loads fully into context and delivers immediate, actionable stakeholder analysis.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates reliably on stakeholder mapping and organizational analysis queries.

## Related Plugins

- **[Persona Definition](../persona-definition/)** -- Create individual user personas with demographics, goals, and empathy maps
- **[Risk Management](../risk-management/)** -- Identify and mitigate risks from stakeholder dynamics
- **[Outcome Orientation](../outcome-orientation/)** -- Connect stakeholder alignment to measurable business outcomes
- **[Prioritization](../prioritization/)** -- Prioritize work across competing stakeholder interests

## Version History

- `1.0.10` fix(design+docs): regenerate READMEs for design and documentation plugins
- `1.0.9` fix: add standard keywords and expand READMEs to full format
- `1.0.8` fix: change author field from string to object in all plugin.json files
- `1.0.7` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
