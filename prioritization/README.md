# Prioritization

> **v1.0.10** | Strategic Thinking | 11 iterations

> Apply prioritization frameworks -- RICE, MoSCoW, ICE scoring, and effort-impact matrices -- to make defensible decisions about what to build next instead of letting the loudest voice win.

## The Problem

Every product team has more ideas than capacity. The backlog grows faster than the team can ship, and without a systematic way to rank items, prioritization defaults to one of four anti-patterns: HiPPO (the highest-paid person's opinion wins), recency bias (the latest request jumps to the top), squeaky wheel (the loudest customer gets their feature), or sunk cost (we already invested in this, so we must finish it).

These anti-patterns are not obvious in the moment. The VP asks for a feature in a meeting and it goes to the top of the sprint. A large customer threatens to churn and their request becomes urgent. Last quarter's half-finished project keeps getting prioritized because "we already built half of it." Each decision feels reasonable in isolation, but over a quarter the backlog becomes a random collection of pet projects, customer appeasements, and legacy commitments -- with no connection to the outcomes that actually matter.

The consequence is not just wasted engineering time. It is opportunity cost: every hour spent on a low-impact item is an hour not spent on the high-impact item that would have moved the needle. Teams that cannot prioritize systematically ship constantly but accomplish little, and struggle to explain to leadership why a year of work produced incremental improvements instead of the step-change the business needed.

## The Solution

This plugin provides four complementary prioritization frameworks, each suited to different decision contexts. RICE scoring (Reach x Impact x Confidence / Effort) gives you a single numeric score that makes items directly comparable. MoSCoW (Must/Should/Could/Won't) categorizes items by necessity for a specific release. ICE scoring (Impact + Confidence + Ease / 3) offers a lightweight alternative when RICE feels too heavy. The effort-impact matrix provides a visual quadrant model (quick wins, big bets, fill-ins, money pits) for fast triage.

You get detailed scoring scales for each framework (not just the formula but what "Impact: 3" actually means), a reusable prioritization template with scoring and rationale documentation, the explicit priority order (Quick Wins first, then Big Bets, then Fill-Ins, avoid Money Pits), and an anti-pattern catalog that names the biases so the team can recognize and resist them. The skill does not just rank items -- it produces documented decisions with transparent reasoning that survives stakeholder scrutiny.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Backlog ordered by who asked loudest | RICE/ICE scores make items directly comparable with transparent math |
| "Everything is a priority" -- no way to say no | MoSCoW categories with the 60% rule: Musts cannot exceed 60% of capacity |
| Effort estimated but impact never quantified | Impact scored on a defined scale (0.25 to 3) with explicit evidence requirements |
| Sunk cost keeps half-finished projects alive | Each item scored fresh -- prior investment is not a factor in RICE |
| Decisions made in meetings, reasoning lost by next week | Prioritization template documents score, rationale, and decision for each item |
| Quick wins and big bets treated the same way | Effort-impact matrix separates them into four quadrants with distinct strategies |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install prioritization@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Bring a prioritization problem:
   ```
   I have 15 feature requests in my backlog and need to pick 5 for next quarter. Help me RICE score them.
   ```
3. The skill walks you through scoring each item on Reach, Impact, Confidence, and Effort, producing a ranked list.
4. Challenge the ranking:
   ```
   The CEO wants feature X at the top but it scored low on RICE. How do I handle this?
   ```
5. Get a framework for having the conversation: either the scoring inputs are wrong (update them with evidence) or the item genuinely is not the highest priority (defend the data).

## What's Inside

Compact single-skill plugin focused on prioritization frameworks and decision-making.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering RICE scoring with impact scale, MoSCoW method with capacity rule, ICE scoring, effort-impact matrix with quadrant strategies, prioritization template, and anti-patterns |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### prioritization

**What it does:** Activates when you need to prioritize features, rank backlog items, score initiatives, or make decisions about what to build next. It provides four frameworks (RICE, MoSCoW, ICE, effort-impact matrix) with scoring scales, templates, and anti-pattern detection.

**Try these prompts:**

```
RICE score these 8 feature requests for our Q3 planning
```

```
We need to cut scope for the v2 launch -- help me apply MoSCoW to decide what stays and what goes
```

```
Quick comparison: should we build the notification system or the analytics dashboard first? Use effort-impact.
```

```
My backlog has 30 items and I don't know where to start. What prioritization framework should I use?
```

```
The sales team keeps pushing customer requests to the top of the backlog. How do I push back with data?
```

```
Score this initiative: we want to rebuild the search feature. It could affect 50K users but will take 3 months.
```

## Real-World Walkthrough

You are the product manager for a B2B SaaS platform with 2,000 paying customers. The engineering team has capacity for roughly 5 person-months of work next quarter. You have 12 feature requests from customers, sales, support, and leadership. Everyone thinks their request is the most important. Last quarter, the team built whatever the CEO mentioned in all-hands, and the product metrics did not move. This quarter, you are going to use data.

**Step 1: Choose the right framework.**

You start by asking which framework fits:

```
I need to prioritize 12 features for next quarter. I have customer reach data, impact estimates, and engineering sizing. Which framework should I use?
```

The skill recommends RICE because you have the data to support all four dimensions: Reach (customer count from your CRM), Impact (estimated effect on retention), Confidence (how sure you are about the impact estimate), and Effort (engineering person-months from the sizing). ICE would work for a quicker pass, but with 12 items and a quarterly commitment, RICE's rigor is worth the extra time.

**Step 2: Score the items.**

You list your top contenders and the skill walks you through scoring. Here are three of the twelve:

**Bulk import tool:**
```
Reach: 800 customers/quarter (40% of base uses spreadsheet imports)
Impact: 2 (High -- eliminates #1 support ticket category)
Confidence: 90% (clear customer demand, support data backs it)
Effort: 1.5 person-months
Score: (800 x 2 x 0.9) / 1.5 = 960
```

**AI-powered search:**
```
Reach: 2000 customers/quarter (everyone uses search)
Impact: 1 (Medium -- improves experience but search works today)
Confidence: 50% (unproven -- will users actually use AI search?)
Effort: 3 person-months
Score: (2000 x 1 x 0.5) / 3 = 333
```

**White-label branding (CEO's request):**
```
Reach: 50 customers/quarter (only enterprise tier)
Impact: 2 (High for those customers -- required for procurement)
Confidence: 80% (3 enterprise prospects said this is a blocker)
Effort: 2 person-months
Score: (50 x 2 x 0.8) / 2 = 40
```

**Step 3: Interpret the results.**

The RICE scores tell a clear story: the bulk import tool (960) has 28x the score of white-label branding (40). The CEO's pet feature is not bad -- it genuinely unblocks enterprise deals -- but it affects 50 customers while the import tool affects 800. The skill helps you frame this: white-label branding is a strategic investment in the enterprise segment, but it should not displace features that serve 16x more users unless the revenue from those 50 enterprise customers justifies it.

You ask:

```
The CEO wants white-label branding but it scored 40 vs 960 for bulk import. How do I present this?
```

The skill provides the framework for the conversation: present the RICE scores transparently, acknowledge the strategic value of enterprise features, and propose that white-label branding is included as a big bet with a longer timeline rather than displacing the quick win that serves the broader base.

**Step 4: Apply MoSCoW for scope management.**

With RICE ranking in hand, you apply MoSCoW to map items to your 5 person-month capacity:

```
Apply MoSCoW to my RICE-ranked list. I have 5 person-months of capacity.
```

- **Must (60% max = 3 PM):** Bulk import tool (1.5 PM), API rate limiting fix (1 PM) -- the two highest-RICE items that are critical for retention
- **Should (remaining capacity):** Dashboard redesign (1.5 PM) -- high RICE score, important but the old dashboard works
- **Could (if time permits):** AI search, white-label branding -- valuable but do not fit in capacity
- **Won't (not this quarter):** 7 remaining items explicitly deferred with documented reasoning

The 60% rule keeps Musts from consuming all capacity, leaving room for the Should items that keep the product improving.

**Step 5: Visualize with the effort-impact matrix.**

For the leadership presentation, you plot all 12 items on the effort-impact matrix:

- **Quick Wins (high impact, low effort):** Bulk import tool, API rate limiting fix
- **Big Bets (high impact, high effort):** Dashboard redesign, AI search
- **Fill-Ins (low impact, low effort):** CSV export improvements, notification preferences
- **Money Pits (low impact, high effort):** White-label branding (for the current user base), legacy API v1 rewrite

This visual makes the priority order intuitive: Quick Wins first, then Big Bets if the evidence supports them, Fill-Ins as time allows, and Money Pits avoided unless strategic context (enterprise revenue) justifies them.

The result: a prioritized quarterly plan backed by RICE scores, scoped with MoSCoW, and visualized on an effort-impact matrix. Every decision is documented with reasoning. When the CEO asks about white-label branding, you have the data: it scores 40 vs 960 for the top item, serving 50 customers vs 800. The conversation shifts from "I want this" to "is the enterprise revenue worth displacing features that serve 16x more users?" -- which is the right conversation to have.

## Usage Scenarios

### Scenario 1: Quarterly planning with RICE

**Context:** You are a PM preparing for quarterly planning with 20 candidate features and capacity for 6.

**You say:** "RICE score these 20 features for Q3 planning. I have user reach data from analytics and effort estimates from engineering."

**The skill provides:**
- RICE scoring template for each feature with Reach, Impact, Confidence, and Effort
- Impact scale calibration: what "Massive" vs "Medium" vs "Minimal" means for your product
- Ranked list with scores that make trade-offs transparent
- Confidence-based grouping: high-confidence items to commit, low-confidence items to validate first

**You end up with:** A ranked feature list with documented scores and rationale, ready for the planning meeting.

### Scenario 2: Scope cutting for a release

**Context:** Your v2 launch is three weeks behind schedule. You need to cut 40% of the scope to hit the deadline.

**You say:** "We need to cut scope for the v2 launch. Here are the 15 features in the release -- help me apply MoSCoW to decide what ships and what gets deferred."

**The skill provides:**
- MoSCoW categorization with the 60% rule for Musts
- Clear criteria: Must = users cannot use the product without it, Should = users will complain, Could = nice to have
- Explicit Won't list with reasoning (not just "cut" -- documented deferral)
- Risk assessment: which Should items become Musts if deferred too long

**You end up with:** A release scope that ships on time with all Musts included, a documented Won't list for post-launch, and stakeholder confidence that the cuts were deliberate.

### Scenario 3: Defending priorities against HiPPO

**Context:** An executive keeps adding features to the roadmap mid-quarter. Your team never finishes what they started.

**You say:** "My CEO keeps adding features mid-sprint. How do I use prioritization data to push back without getting fired?"

**The skill provides:**
- RICE scoring comparison: new request vs current sprint items
- Framework for the conversation: "here's how this scores relative to what we're building"
- Capacity impact analysis: what gets displaced if the new item is added
- Anti-pattern naming: HiPPO is a recognized bias, not just "the boss wants it"

**You end up with:** A data-backed response to executive interruptions that shifts the conversation from authority to evidence.

### Scenario 4: Quick triage with effort-impact

**Context:** You have a brainstorming session output of 30 ideas and need to sort them into actionable categories in 30 minutes.

**You say:** "We brainstormed 30 ideas. I need to quickly sort them into quick wins, big bets, and things to skip. Use the effort-impact matrix."

**The skill provides:**
- Effort-impact placement for each idea (quick estimate, not detailed sizing)
- Four quadrant categories with priority order: Quick Wins > Big Bets > Fill-Ins > skip Money Pits
- Top 5-10 items to investigate further with RICE scoring
- Items to explicitly kill (money pits) with reasoning

**You end up with:** A triaged idea list with clear next steps: build the quick wins, investigate the big bets, defer the fill-ins, and kill the money pits.

## Ideal For

- **Product managers doing quarterly planning** -- RICE scoring makes trade-offs transparent and decisions defensible
- **Teams cutting scope for a release** -- MoSCoW with the 60% rule ensures the most critical items ship
- **Anyone who needs to say no to feature requests** -- scoring frameworks shift conversations from opinions to evidence
- **Leaders triaging large lists of ideas** -- the effort-impact matrix sorts 30 items in 30 minutes
- **Teams suffering from HiPPO or squeaky-wheel prioritization** -- named anti-patterns make biases visible and resistible

## Not For

- **Defining OKRs or success metrics** -- use [outcome-orientation](../outcome-orientation/) for outcomes, key results, and leading/lagging indicators
- **Stakeholder management and influence mapping** -- use [persona-mapping](../persona-mapping/) for Power-Interest matrices and RACI charts
- **Risk assessment for specific initiatives** -- use [risk-management](../risk-management/) for risk identification and mitigation planning

## How It Works Under the Hood

The skill is a compact, focused knowledge base covering four prioritization frameworks. The SKILL.md provides: RICE scoring with a detailed impact scale (0.25 to 3) and formula, MoSCoW categorization with the 60% capacity rule, ICE scoring as a lightweight RICE alternative, the effort-impact matrix with four quadrants and priority order, a reusable prioritization template with scoring and decision documentation, and an anti-pattern catalog (HiPPO, recency bias, squeaky wheel, sunk cost).

There are no additional reference files -- the skill is deliberately compact so it loads fully into context and delivers immediate, actionable prioritization guidance.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates reliably on prioritization and backlog ranking queries.

## Related Plugins

- **[Outcome Orientation](../outcome-orientation/)** -- Define the outcomes that prioritized features should drive
- **[Risk Management](../risk-management/)** -- Assess risks for prioritized initiatives
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholder interests that influence prioritization
- **[Systems Thinking](../systems-thinking/)** -- Understand the systemic effects of prioritization choices

## Version History

- `1.0.10` fix(design+docs): regenerate READMEs for design and documentation plugins
- `1.0.9` fix: add standard keywords and expand READMEs to full format
- `1.0.8` fix: change author field from string to object in all plugin.json files
- `1.0.7` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
