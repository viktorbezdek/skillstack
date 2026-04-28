---
name: custom-personas
description: >-
  Design ad-hoc personas for niche domains when the canonical 12 brainstorm-
  swarm personas don't fit. Covers: when a custom persona is justified (vs
  forcing canonical to fit), the persona-design template (voice, contribution
  shape, output format), anti-patterns (too-narrow personas, redundant
  personas, sock-puppet personas), and how to invoke a custom persona inline
  via Task() with a tailored prompt rather than a saved subagent definition.
  Use when running a brainstorm-swarm and the topic calls for a CFO,
  Security Engineer, Lawyer, Marketing, Customer Success, or other domain-
  specific perspective not in the canonical 12. NOT for the canonical
  personas (use swarm-protocol). NOT for the orchestration mechanics (use
  swarm-protocol). NOT for the synthesis output (use swarm-synthesis). NOT
  for product personas as artifacts (use persona-definition).
---

# Custom Personas

> The canonical 12 cover most decisions. They don't cover every domain. When you need a CFO for a budget brainstorm or a security engineer for threat modeling, design the persona — don't force a canonical to fit.

This skill covers the design discipline for ad-hoc personas: when a custom is justified, how to write the persona prompt, how to invoke it inline (without shipping a new subagent file).

## Core principle

**A custom persona is a tool, not a feature.** Design one when the canonical 12 demonstrably don't cover the domain. Don't design custom personas to "be thorough" or to feel comprehensive — that produces sock-puppet personas that contribute generic content.

## When a custom persona is justified

A custom persona is justified when:

1. The domain has specialized knowledge that the canonical personas don't have (e.g. tax law, regulatory compliance, hardware reliability, biotech)
2. The decision affects a specific stakeholder group with a distinct perspective (e.g. enterprise procurement, customer success at scale, sales at a specific deal size)
3. The framing requires expertise the canonical personas wouldn't bring (e.g. economist for pricing strategy, behavioral psychologist for engagement design)
4. The brainstorm is industry-specific (e.g. healthcare, finance, defense, EdTech)

A custom persona is NOT justified when:

1. The canonical personas would cover it adequately if you tightened their prompts
2. You're trying to "represent everyone" — the swarm is illustrative, not exhaustive
3. You want a "voice" persona (poet, philosopher, etc.) that doesn't carry domain expertise
4. The custom persona's contribution would substantially overlap with a canonical one

## Common custom persona archetypes

| Domain | Custom persona | What they bring |
|---|---|---|
| Budget / finance | **CFO** | ROI rigor, capital allocation framing, runway implications |
| Legal / compliance | **General Counsel** | regulatory risk, contract implications, IP concerns |
| Security | **Security Engineer** | threat modeling beyond what Operator covers, attack surface |
| Sales | **Sales Lead** | what closes deals, what blocks them, win/loss patterns |
| Customer Success | **CS Lead** | renewal risk, expansion opportunity, support burden |
| Marketing | **Head of Marketing** | positioning, launch strategy, channel implications |
| Data | **Data Scientist** | what's measurable, what data we have, what we can learn |
| HR / People | **People Operations** | culture impact, hiring implications, team dynamics |
| Industry-specific | **[Domain] Expert** | regulatory specifics, industry conventions, domain risks |
| Stakeholder voice | **The [specific stakeholder]** | the actual voice of an affected party (enterprise CTO, hospital admin, school principal) |

## The custom persona template

When you need a custom persona, design it inline using this template:

```
You are a [role] participating in a multi-perspective brainstorm. Your job is
NOT to [thing the canonical handles]. Your job is to bring [the specific
perspective only this role brings].

## Your voice
- [3-5 voice characteristics, specific to the role]

## Your job in the swarm

When the orchestrator gives you a topic, contribute a focused perspective covering:

### 1. [First contribution slot]
[3 of something specific to this role]

### 2. [Second contribution slot]
[2 concerns or observations]

### 3. [Third contribution slot]
[1 reframe or specific recommendation]

### 4. [Fourth contribution slot]
[The single most important question or warning from this role]

## Discipline
- DO NOT play other personas
- DO use specific terminology from your domain
- DO commit to specific positions when asked
- DO NOT [specific failure mode for this role]

## Output format
[Markdown structure mirroring the canonical persona format]

Length: under 400 words.
```

The persona prompt mirrors the canonical structure — voice + 4 contribution slots + discipline + output format.

## How to invoke a custom persona

Custom personas don't have saved subagent files. You invoke them by spawning a `general-purpose` Task() with the custom persona prompt as the subagent's instructions:

```python
Task(
    subagent_type="general-purpose",
    description="CFO perspective on pricing change",
    prompt="""[CUSTOM PERSONA SYSTEM PROMPT — use the template above]

Topic: [the brainstorm topic]
Context: [the brainstorm context]

Your job: Contribute your perspective in your characteristic voice, following the output format.
"""
)
```

The custom persona's voice is loaded into the prompt directly. The general-purpose subagent runs with that prompt as its instruction set.

## Worked example: designing the CFO persona

Suppose the brainstorm topic is "should we lower our entry-level price by 30%?" — clearly a topic where a CFO perspective adds value.

Custom persona prompt:

```
You are a CFO participating in a multi-perspective brainstorm. Your job is NOT to
do the product strategy work (PM handles that). Your job is to bring financial
rigor — unit economics, cash impact, runway implications.

## Your voice
- Direct, numerate, slightly impatient with hand-waved financial claims
- You think in unit economics, gross margin, payback period, runway months
- You name specific numbers — "if CAC is $X and LTV is $Y, payback is Z months"
- You distinguish between accounting profit and cash impact
- You're not anti-growth; you're pro-economics that work

## Your job

When the orchestrator gives you a topic, contribute:

### 1. Three financial questions
The questions a CFO would ask in a pricing discussion. Examples:
- "What's our current LTV at the new price? What's the elasticity assumption?"
- "If conversion goes up 30% but ACV drops 30%, are we cash neutral or cash worse?"
- "What's the runway impact in months under three demand scenarios?"

### 2. Two financial concerns
What worries the CFO. Examples:
- "Lowering price for new customers creates a perceived-value problem with existing customers paying the higher price."
- "If we hit the upside case, gross margin still drops because [reason]."

### 3. One financial reframe
The CFO's move: reshape the proposal to be more financially honest. Examples:
- "Don't lower the price; create a lower-tier with reduced features. Preserves the price ladder."

### 4. The veto question
The CFO's hardest question. Example:
- "Show me the model. I don't trust intuitions about pricing — I trust the LTV and CAC calculations."

## Discipline
- DO commit to specific numbers (even rough ones) rather than hedge
- DO NOT play other personas
- DO be direct — CFO voice is impatient with hand-waving

## Output format

```markdown
## CFO perspective

### Financial questions
1. [Q]
2. [Q]
3. [Q]

### Concerns
- [Concern with specific financial mechanism]
- [Concern with specific financial mechanism]

### Financial reframe
- [Specific alternative]

### Veto question
- [The CFO's hardest question]
```

Length: under 400 words.
```

This custom persona is now a fully-defined agent for THIS brainstorm. Invoke via:

```python
Task(
    subagent_type="general-purpose",
    description="CFO perspective on 30% price cut",
    prompt="[the prompt above + topic + context]"
)
```

See `references/persona-design.md` for more worked examples.

## ✅ Use for

- Designing a custom persona when canonical 12 don't fit
- Inventing a domain-specific persona inline (CFO, Security Engineer, Lawyer, etc.)
- Representing a specific stakeholder in the brainstorm (enterprise CTO, customer success manager, etc.)
- Building a persona for an industry-specific brainstorm (healthcare, fintech, defense)

## ❌ NOT for

- The canonical 12 personas — use `swarm-protocol`
- The orchestration mechanics (parallel spawn, prompt template) — use `swarm-protocol`
- The synthesis output format — use `swarm-synthesis`
- Product personas as artifacts (user personas for UX research) — use `persona-definition` (skillstack)
- Stakeholder mapping (Power-Interest matrices, RACI) — use `persona-mapping` (skillstack)

## Anti-patterns

### Sock-puppet persona

**What it looks like:** designing a "Visionary CEO" persona that's really just an excuse to inject the user's own preferred direction.

**Why it's wrong:** the persona produces what the orchestrator already wanted. No actual perspective, just confirmation.

**What to do instead:** if you want the CEO's view, design it from the role honestly — not as a stand-in for your own opinion. The CEO has different priorities than the orchestrator (capital allocation, board narrative, exec-team dynamics).

### Too-narrow persona

**What it looks like:** "Senior Backend Engineer specifically for Postgres performance issues." So narrow it can only contribute on one type of question.

**Why it's wrong:** breaks down outside the narrow domain; can't engage the broader brainstorm.

**What to do instead:** if Postgres performance is the topic, just brief the Engineer canonical with that context. Don't build a hyper-specific custom persona unless the brainstorm is genuinely focused on that one thing.

### Redundant persona

**What it looks like:** "Strategic Thinker" persona that overlaps with First-Principles Thinker.

**Why it's wrong:** adds noise; the contribution overlaps with a canonical persona.

**What to do instead:** check the canonical 12 first. If a canonical persona would cover it, use that. Custom personas are for genuine gaps.

### Persona-as-monologue

**What it looks like:** the custom persona's prompt is so prescriptive that it produces the exact output the orchestrator already had in mind.

**Why it's wrong:** the persona isn't contributing; it's parroting.

**What to do instead:** keep the persona's voice + contribution-shape; let the persona reach its own conclusions. The output should sometimes surprise the orchestrator.

### Forced inclusion

**What it looks like:** spawning a CFO persona for a "should we add a button" brainstorm.

**Why it's wrong:** the topic doesn't justify the persona; the contribution will be either forced or generic.

**What to do instead:** custom personas are for topics where their domain is genuinely load-bearing. If the topic doesn't touch finance, skip the CFO.

## Workflow

1. **Confirm the canonical 12 don't cover.** Walk through the catalog; ask "would [canonical persona] handle this?". If yes, use that.
2. **Identify the role.** What specific role brings the missing perspective?
3. **Draft the persona prompt.** Use the template — voice + 4 contribution slots + discipline + output format.
4. **Sanity-check.** Would this persona actually contribute something a canonical wouldn't? If no, drop it.
5. **Invoke inline.** Spawn via `Task(subagent_type="general-purpose", prompt=<custom persona + topic + context>)`.
6. **Treat the contribution like a canonical's.** Hand off to `swarm-synthesis` along with the canonical contributions.

## References

| File | Contents |
|---|---|
| `references/persona-design.md` | The persona-design template; 5+ worked examples (CFO, Security Engineer, Lawyer, Healthcare Admin, Sales Lead); voice calibration |
| `references/when-to-fork.md` | Decision tree for canonical-vs-custom; when to brief a canonical with context vs design a new persona |

## Related skills

- **swarm-protocol** — uses these custom personas in the parallel spawn
- **interview-facilitation** — structures the interview that includes custom personas
- **swarm-synthesis** — synthesizes custom + canonical persona outputs together
- **persona-definition** (skillstack) — for product personas as artifacts (different domain)
- **persona-mapping** (skillstack) — for stakeholder mapping (different domain)
