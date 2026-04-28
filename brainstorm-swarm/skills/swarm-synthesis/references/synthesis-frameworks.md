# Synthesis Frameworks

The standard artifact structure for a brainstorm-swarm synthesis, plus alternative formats for different needs.

## The standard artifact

Used for most brainstorms. Sections in order:

```markdown
## Brainstorm: [topic]

[1-2 sentence framing]

### Personas in the swarm
- [Persona] — [why included]
[4-8 personas total]

### Consensus
- [Point] — raised by [primary persona]; echoed by [others]
[3-5 items, ordered by importance]

### Dissent
- **[Topic of disagreement]**
  - [Persona A] said: [position]
  - [Persona B] said: [opposing position]
  - **Underlying disagreement**: [the substantive question]
[2-4 items]

### Open questions
- **[Question]**
  - Resolution: [what evidence would settle this]
[1-3 items]

### Recommended next move
- [Specific action with reasoning]
- Alternative: [if recommended is rejected]

### Per-persona contributions
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

## When to use the standard artifact

- Most brainstorms (any arc, any topic)
- The user wants the full picture
- The output will be referenced later for the decision rationale

## Alternative format 1: Consensus Matrix

When consensus and dissent are the headline, render as a matrix.

```markdown
## Brainstorm: [topic]

### Where personas agreed (consensus matrix)

| Point | PM | Eng | Designer | Skeptic | UA | Pre-Mortem |
|---|---|---|---|---|---|---|
| Scope is too big | ✓ | ✓ | — | ✓ | — | ✓ |
| Need user research first | — | — | ✓ | ✓ | ✓ | — |
| Production complexity high | — | ✓ | — | — | — | ✓ |

### Where personas disagreed
[Standard dissent section]
```

**When to use:** the swarm is large (8+ personas) and the convergence pattern is itself the insight.

## Alternative format 2: Decision One-Pager

For when the brainstorm produced a clear direction and you need a short artifact for stakeholders.

```markdown
## Decision Brief: [topic]

**Direction**: [one-sentence proposed decision]

**Why**: [paragraph synthesizing the consensus reasoning]

**Risks acknowledged** (from dissent + pre-mortem):
- [Risk 1] — mitigation: [planned action]
- [Risk 2] — mitigation: [planned action]

**Open question** (resolve before commit):
- [Question + planned resolution]

**Alternative considered**: [the runner-up direction; why not chosen]

**Inputs**: brainstorm-swarm with [N] personas: [list]
```

**When to use:** the brainstorm reached a clear direction; the user needs a doc to share / decide on / file.

## Alternative format 3: Dissent Log

For when the brainstorm's main output is *what to research / decide between*.

```markdown
## Open Questions from Brainstorm: [topic]

### Question 1: [the question]

- **PM** said: [their take]
- **Engineer** said: [their take]
- **Skeptic** said: [their take]
- **The substantive disagreement**: [the underlying question]
- **What would resolve this**: [evidence type, who can gather it, estimated effort]

### Question 2: [the question]
[same structure]

[...]

### Recommended sequence
1. Resolve Question 1 first ([reason])
2. Then re-examine the brainstorm with new evidence
```

**When to use:** the brainstorm exposed that the team isn't ready to decide and needs to do research first.

## Alternative format 4: Per-Persona Highlights

For when each persona's contribution stands well alone and the user wants to read them as separate voices, not synthesized.

```markdown
## Brainstorm: [topic]

### Headline
[1-2 sentence summary of what every persona was thinking]

### Voices

#### PM
[Full PM contribution, edited for readability]

#### Engineer
[Full Engineer contribution]

[...]

### Where they agreed
[short consensus list, no need for full Dissent / Open Questions structure]
```

**When to use:** the user values reading the persona texture; the synthesis would lose the voice; perspectives don't deeply conflict (so dissent isn't the headline).

## Alternative format 5: Decision Matrix

When the brainstorm has clearly produced 2-3 candidate directions to choose between.

```markdown
## Brainstorm: [topic]

### Three candidate directions emerged

|  | Option A: [name] | Option B: [name] | Option C: [name] |
|---|---|---|---|
| **Description** | [one line] | [one line] | [one line] |
| **PM view** | [supports/skeptical/neutral] — reason | ... | ... |
| **Eng view** | ... | ... | ... |
| **Skeptic view** | ... | ... | ... |
| **User Advocate** | ... | ... | ... |
| **Pre-Mortem** | ... | ... | ... |
| **Cost** | [rough estimate] | ... | ... |
| **Risk** | [primary risk] | ... | ... |

### Recommended: Option [X]
[Reasoning]

### Why not [Option Y]: [reason]
### Why not [Option Z]: [reason]
```

**When to use:** the brainstorm produced clean alternatives; user is comparing options; output will be a decision doc.

## Picking the right format

```
What did the brainstorm produce?

- Mostly consensus + clear direction        → Decision One-Pager
- Mostly dissent + need for research        → Dissent Log
- 2-3 distinct alternatives                 → Decision Matrix
- Many personas, mixed convergence         → Consensus Matrix
- Diverse perspectives worth preserving     → Per-Persona Highlights
- Standard mix                             → Standard Artifact
```

## Length guidance

| Format | Target length |
|---|---|
| Standard Artifact | 600-1200 words (excluding collapsed per-persona) |
| Consensus Matrix | 300-600 words + the matrix |
| Decision One-Pager | 250-400 words (ONE PAGE) |
| Dissent Log | 400-800 words |
| Per-Persona Highlights | 200 words intro + per-persona contributions |
| Decision Matrix | 300-500 words + the matrix |

Synthesis longer than 1500 words is failing. The user can't act on a 3000-word document; they have to do their own synthesis.

## Headers and emphasis

Use bold and structure to make the artifact scannable:

```markdown
- **Bold the underlying disagreement** when listing dissent (not the surface positions)
- ✓ Bullet the consensus points with their primary attribution
- > Use blockquote for direct persona quotes when the wording matters
```

## Voice

The synthesizer's voice is **neutral integrator**, not commentator:

- Don't say "I agree with PM"
- Don't say "the right answer is clearly..."
- Don't editorialize on personas ("the Skeptic, as usual, was contrarian")

DO use crisp third-person:
- "Three personas converged on [point]"
- "PM and Engineer disagreed substantively on [issue]"
- "No persona could answer [question]; resolution requires [evidence]"

The recommended next move is the only place where the synthesizer takes a position — and it's framed as recommendation, not pronouncement.

## When the synthesis fails

Sometimes the swarm produces output the synthesizer can't integrate. Symptoms:
- 6 personas, 6 different topics — no consensus, no dissent, just six monologues
- Everyone produced similar generic content (single-message rule probably violated)
- One persona dominated (their contribution was 2000 words, others were 200)

In each case, the synthesis can't carry. Be honest:

```markdown
## Brainstorm: [topic]

**Note: this synthesis is incomplete because [the swarm produced X / the
spawn was sequential / one persona dominated]. Recommend re-running with
[fix].**

[Best-effort synthesis follows]
```

Better to flag the issue than produce a misleading polished synthesis.
