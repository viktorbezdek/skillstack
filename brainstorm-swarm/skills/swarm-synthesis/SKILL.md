---
name: swarm-synthesis
description: >-
  Combine a parallel persona-swarm's outputs into an actionable artifact —
  consensus matrix (what every persona agreed on), dissent log (where personas
  disagreed and why), open questions (what nobody could answer), recommended
  next move (synthesized decision). Preserves dissent rather than forcing
  consensus. Use when running a brainstorm-swarm and the swarm-protocol skill
  has collected the persona outputs — this skill produces the synthesis
  artifact. NOT for orchestrating the spawn (use swarm-protocol). NOT for
  designing the interview arc (use interview-facilitation). NOT for designing
  custom personas (use custom-personas). NOT for short-form structured
  writing like BLUF or Pyramid (use communication/structured-writing).
---

# Swarm Synthesis

> The swarm's value is in the dissent. Synthesis that hides disagreement to "give a clear answer" loses what the multi-perspective brainstorm bought you.

This skill turns a pile of persona contributions into an actionable artifact. The artifact preserves dissent explicitly, surfaces consensus where it exists, names the open questions, and proposes a synthesized next move — without flattening the perspectives.

## Core principle

**Synthesis is curation, not consensus.** The synthesizer's job is to make the swarm's structure visible to the user — not to decide who's right. Disagreement is data; preserve it.

Secondary principle: **end with a recommended next move.** A synthesis that ends in "well, perspectives differ" puts the burden on the user. A synthesis that ends with "given the disagreement, the next move is to gather X evidence" is actionable.

## The synthesis artifact

Standard format:

```markdown
## Brainstorm: [topic]

[1-2 sentence framing — what was being brainstormed]

### Personas in the swarm
[List of 4-8 personas spawned + 1-line rationale per inclusion]

### Consensus
- [Point all personas (or near-all) agreed on, with attribution to who raised it first]
- [Another consensus point]
[3-5 items, ordered by importance]

### Dissent
- **[Topic of disagreement]**: PM said [position]; Skeptic said [opposing position]; the underlying disagreement is [the real question, not the surface position]
- **[Topic of disagreement]**: ...
[2-4 items, each naming the substantive disagreement, not just the surface clash]

### Open questions (nobody could answer)
- [Question that surfaced but no persona could resolve]
- [Question]
[1-3 items, ideally with "what evidence would resolve this"]

### Recommended next move
- [Synthesized direction with reasoning]
- [Alternative if the recommended move is rejected]

### Per-persona contributions (collapsed)
<details>
<summary>PM perspective</summary>
[Full PM output]
</details>
<details>
<summary>Engineer perspective</summary>
[Full Engineer output]
</details>
[etc.]
```

The collapsed per-persona section preserves the originals for users who want to read individual takes.

## How to extract consensus

Consensus = same core point from 3+ personas, possibly worded differently.

### What counts as consensus

- All personas raised the same risk (e.g. "scope is too big")
- 4+ personas independently asked the same question
- All personas implicitly assumed the same thing (which itself becomes a consensus point about a hidden assumption)

### What doesn't count as consensus

- A point made by only one persona, even if true
- Generic agreement on platitudes ("user experience matters") — too abstract to be a consensus point
- Apparent agreement that turns out to be different things on inspection (e.g. PM and Engineer both say "this is risky" but mean different risks)

### Attribution

When listing a consensus point, name who raised it most clearly:

```markdown
- **The single enterprise customer doesn't justify the eng cost.**
  Raised most clearly by PM; echoed by Skeptic ("inventing demand")
  and Constraint-Setter ("scope grows from one request").
```

This shows the user the convergence without losing the persona texture.

## How to extract dissent

Dissent = two or more personas in substantive opposition, not just word-level disagreement.

### Surface dissent

```markdown
- **PM** said: "Don't build it."
- **User Advocate** said: "Build it."
```

This is the surface. Don't stop here — find the underlying disagreement.

### Substantive dissent

```markdown
- **Underlying disagreement**: how to interpret the demand signal.
  PM treats "one enterprise request" as the whole signal (build for the median
  user, not the loudest). User Advocate treats it as the visible tip of an
  iceberg (the enterprise customer voices what the cellular cohort silently
  experiences).
  This isn't a values disagreement; it's an empirical disagreement about
  whether the cellular cohort exists and shares the pain.
```

The substantive dissent surfaces what the user actually has to decide. It's also more actionable: "we need to learn whether the cellular cohort hits offline issues."

### Preserve dissent honestly

Don't collapse to "personas disagree, more research needed" — that's a non-synthesis. Name the disagreement specifically. Name what would resolve it.

## How to extract open questions

Open questions = topics raised by personas that no persona could answer.

Examples:
- "How many customers actually need offline mode?" (raised by Skeptic + User Advocate, no persona has the data)
- "What's the engineering cost of bidirectional sync vs read-only?" (raised by Engineer, requires actual estimation work)
- "What's our enterprise SLA commitment?" (raised by Operator, requires looking up the contract)

For each open question, ideally identify what evidence would resolve it:

```markdown
- **How many customers actually need offline mode?**
  Resolution: query for sessions with connectivity errors over the last 90 days;
  segment by customer type. (Estimated 30 min of analytics work.)
```

This makes the open questions actionable, not just lists.

## How to recommend a next move

The recommended next move is the synthesizer's contribution — it integrates the swarm's perspectives and names the action that best fits.

### Patterns

| When the swarm produced... | Recommended next move pattern |
|---|---|
| Strong consensus on a direction | "Direction is clear: [X]. Next move: build the smallest version, ship to [audience], measure [metric]." |
| Dissent that hinges on missing data | "The disagreement is empirical. Next move: gather [evidence] to resolve it before deciding." |
| Many open questions | "We're not ready to decide. Next move: answer [question 1] and [question 2] before re-running the brainstorm." |
| Consensus on a constraint, dissent on path | "Consensus: [constraint]. Within that, two paths emerged: [A] and [B]. Recommend prototype both for 1 week, decide based on what we learn." |
| Strong skeptic-heavy "don't do this" | "Pre-mortem and Skeptic surfaced critical risk. Recommend NOT proceeding without first [mitigation]. If mitigation works, re-run the brainstorm." |

### What NOT to do

- Don't average the perspectives — that produces mush
- Don't side with one persona — the user can do that themselves; your job is to integrate
- Don't recommend "more discussion" — that's a cop-out; recommend a specific next action
- Don't over-recommend — one recommended move + one alternative is enough

## ✅ Use for

- Synthesizing a parallel swarm's outputs into an actionable artifact
- Identifying consensus vs dissent vs open questions
- Naming the recommended next move with reasoning
- Preserving dissent rather than forcing consensus
- Producing the final deliverable of a brainstorm-swarm session

## ❌ NOT for

- Orchestrating the spawn — use `swarm-protocol`
- Designing the interview arc — use `interview-facilitation`
- Designing custom personas — use `custom-personas`
- Short-form structured writing (BLUF, Pyramid) — use `communication/structured-writing`
- Writing PRDs from the synthesis — use `prd` (skillstack)

## Anti-patterns

### Forced consensus

**What it looks like:** synthesis hides disagreement to "give a clear answer."

**Why it's wrong:** the swarm's value is in the dissent. Hiding it loses the swarm's contribution.

**What to do instead:** explicit Dissent section. Name the disagreement; identify the substantive question underneath; propose what would resolve it.

### Average-the-perspectives

**What it looks like:** "PM said maybe build, Engineer said maybe complex, Skeptic said maybe risky. Synthesis: it's a moderate-complexity feature with risks."

**Why it's wrong:** flat compromise that loses the texture of each contribution. The user could have generated this themselves.

**What to do instead:** preserve the texture. Show what each persona specifically said. Then synthesize what the cross-persona pattern means.

### Wall of text

**What it looks like:** synthesis is 3000 words because it tries to capture everything.

**Why it's wrong:** the user has to do the synthesis themselves to extract action.

**What to do instead:** lead with consensus / dissent / open questions / next move. Put the full per-persona contributions in collapsed sections for those who want depth.

### Burying the next move

**What it looks like:** synthesis ends with "many considerations to weigh."

**Why it's wrong:** doesn't help the user decide. Punts the brainstorm's value to the user's own integration work.

**What to do instead:** end with a specific recommended next move + alternative. The user can override; that's fine. But the synthesizer's job is to propose.

### Treating dissent as a problem

**What it looks like:** synthesis presents dissent apologetically — "personas couldn't agree on..."

**Why it's wrong:** dissent is the swarm's main value. Apologizing for it inverts the framing.

**What to do instead:** present dissent as substantive — "the swarm surfaced these substantive disagreements, each one a decision the user has to make."

## Workflow

After the orchestrator collects all persona contributions:

1. **Read all contributions.** Don't skim. The synthesis depends on actually understanding each.
2. **Extract consensus.** What did 3+ personas raise? Group similar points. Attribute who raised most clearly.
3. **Extract dissent.** Where do personas substantively oppose each other? What's the underlying disagreement (not just the surface position)?
4. **Extract open questions.** What did personas raise that nobody could answer? For each, propose what evidence would resolve.
5. **Form the recommended next move.** Based on consensus + dissent + open questions, what's the best next action?
6. **Write the artifact.** Use the standard format. Preserve dissent. Lead with action.
7. **Hand to user.** If the user wants to deepen specific dissent → second round (back to swarm-protocol + interview-facilitation).

## References

| File | Contents |
|---|---|
| `references/synthesis-frameworks.md` | The standard artifact structure; consensus matrix; dissent log; alternative formats |
| `references/decision-frameworks.md` | How to recommend a next move based on the brainstorm shape |
| `references/output-formats.md` | When to produce a doc, a decision matrix, a one-pager, a slide |

## Related skills

- **swarm-protocol** — spawns the personas; this skill consumes the outputs
- **interview-facilitation** — structures the interview; this skill produces the artifact at each phase
- **custom-personas** — when canonical personas don't fit
- **communication/structured-writing** (skillstack) — for short-form structure (BLUF, Pyramid) — different domain
- **prd** (skillstack) — when the synthesis becomes a full PRD
