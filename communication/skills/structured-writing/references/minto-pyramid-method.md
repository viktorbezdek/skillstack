# The Minto Pyramid Method

Barbara Minto's pyramid is the discipline behind McKinsey-style business writing. Every document has one governing thought, supported by 3-5 grouped arguments, each supported by evidence. The reader gets the main idea first; they dive deeper only when they want to.

## The single governing thought

The top of the pyramid is one sentence: the answer to the reader's primary question. Everything below it exists to support or explain it.

### What makes a strong governing thought

- **States a claim, not a topic.** "Our pricing strategy" is a topic. "We should move to usage-based pricing in Q3" is a claim.
- **Takes a position.** A claim you could disagree with.
- **Compresses the message.** If the reader understands only this sentence, they have the message.
- **Invites predictable questions.** A good claim raises "why?" or "how?" that the pyramid then answers.

### Test the governing thought

Before writing, write the governing thought in one sentence. Then ask:

1. **Can a reader disagree with this?** (If no, it's too bland to matter.)
2. **Does it state what I want the reader to do/believe?** (If no, refine.)
3. **Can the rest of the document support this claim?** (If no, the claim is too ambitious.)
4. **Does it raise a predictable question?** (If no, you have a fact, not an argument.)

If any answer is no, the pyramid is not yet buildable.

## Grouped arguments (MECE)

The next level down contains 3-5 arguments that support the governing thought. These must be **MECE** — Mutually Exclusive, Collectively Exhaustive.

### Mutually Exclusive

Arguments at the same level do not overlap. If Argument 1 is "cost savings" and Argument 2 is "operational efficiency," they overlap (efficiency includes cost). Split or merge until each argument owns its space.

### Collectively Exhaustive

Together, the arguments cover the full support for the governing thought. If you left out a major reason, the argument feels incomplete and a reader will notice.

### The question test

Each argument at level 2 should answer a specific "why" or "how" question raised by the governing thought:

```
Governing thought: "We should move to usage-based pricing in Q3."
  Raises: "Why?" and "Why Q3?"

Arguments:
  1. Because per-seat pricing is penalizing high-usage customers. (WHY)
  2. Because we have six months of data showing it. (SUPPORTS #1)
  3. Because Q3 aligns with contract renewal cycles. (WHY Q3)
```

If an argument does not answer a predictable question, it does not belong at that level — either raise the governing thought to raise the question, or demote the argument.

## Evidence at the bottom

Each argument is supported by evidence: numbers, quotes, references, cases. Evidence is the bottom of the pyramid; it is what makes the argument credible.

### Strong evidence

- Specific numbers with source
- Named examples (customer X did Y)
- Direct quotes from primary sources
- References to prior decisions or documents

### Weak evidence

- "Industry best practice"
- "Many customers tell us"
- Unnamed polls or "some analysts believe"

Replace weak evidence. If you cannot, downgrade the argument it supports.

## The SCQ introduction

Minto's introduction format: Situation → Complication → Question → (Answer, which is the governing thought).

```
Situation: [Shared understanding. Uncontroversial.]
Complication: [What changed. The reason this document exists.]
Question: [What does the reader want to know now?]
Answer: [Governing thought.]
```

Worked example:

> **Situation:** We have used per-seat pricing for three years. Revenue has grown 40% year-over-year and the model is straightforward for sales.
>
> **Complication:** Q2 data shows our top 20% of customers by API volume are converting at half the rate of the bottom 80%. Exit interviews indicate the per-seat model does not match how they value the product.
>
> **Question:** Should we change the pricing model — and if so, to what?
>
> **Answer (governing thought):** We should move to usage-based pricing in Q3, piloted with 10% of new signups, with existing customers grandfathered.

The SCQ makes the pyramid testable — the governing thought is the *answer* to a specific question grounded in a specific situation.

## Building the pyramid

### Step 1 — write the governing thought

One sentence. Refine until it passes the four tests.

### Step 2 — list the questions the governing thought raises

- Why?
- Why now?
- How?
- What does it cost?
- What are we giving up?

Write all that apply. The ones worth answering become your level-2 arguments.

### Step 3 — group the questions into 3-5 arguments

Arguments should be MECE. Each argument answers one question-cluster.

### Step 4 — gather evidence for each argument

For each argument, list the evidence you have. If evidence is thin, the argument is thin; either gather more or weaken the argument.

### Step 5 — write the SCQ intro

Establish shared context, name the complication, state the question, land on the governing thought.

### Step 6 — write the body

Each argument gets a section. The first sentence of each section states the argument; the rest supports it with evidence.

### Step 7 — skim-test

Read only the governing thought and the first sentence of each section. Does the message still come through? If yes, the pyramid works.

## Worked example — full pyramid

### Governing thought
We should move to usage-based pricing in Q3, piloted with 10% of new signups, with existing customers grandfathered.

### Level 2 arguments
1. Per-seat pricing is mis-aligned with how our top customers value the product.
2. Usage-based pricing grows revenue faster without harming small-account economics.
3. Q3 minimizes disruption because it aligns with contract renewal cycles.

### Level 3 evidence

**Argument 1:** Per-seat pricing is mis-aligned.
- Top 20% by API volume convert at half the rate of bottom 80% (Q2 data, N=240).
- Exit interviews (n=18) cite "pricing does not reflect value" as the top reason.
- Competitor X moved to usage-based in 2024 and reported similar cohort behavior pre-move.

**Argument 2:** Usage-based grows revenue faster.
- Modeling shows 18% ARR lift at similar conversion, 32% at improved conversion.
- Small accounts see no pricing change at projected usage.
- Downside: 6% of current accounts (light users of paid tier) would pay less; offset by lower churn.

**Argument 3:** Q3 minimizes disruption.
- 72% of contracts renew in Q3 or Q4 — aligning the change with a natural touchpoint.
- Sales team prefers Q3: Q4 is pipeline-closing season.
- Billing system has feature-flag infrastructure to run both models simultaneously.

## Common mistakes

- **Governing thought is a topic, not a claim.** "Our pricing situation" instead of "We should move to usage-based pricing."
- **Arguments overlap.** "Lower cost" and "better efficiency" are the same argument said two ways.
- **Missing arguments.** The pyramid covers 60% of the case; readers notice the missing 40%.
- **Evidence dumping.** Numbers and charts with no argument they support.
- **Chronological narrative instead of pyramid.** "Here's what we did, then what we learned, then what we decided." Invert — decision first, then evidence.
- **Over-arguing.** Three levels when two would do. Pyramid depth should match reader interest.
- **No SCQ intro.** Jumping straight to the governing thought without establishing why the question is being asked.

## When the pyramid is the wrong tool

- **Narrative pieces** — blog posts, essays, personal reflections.
- **Announcements** — inverted pyramid is better.
- **Short messages** — BLUF is the compressed pyramid; use it.
- **Open-ended exploration** — when you genuinely do not have a governing thought yet.

The pyramid is for documents that must **make a case**. For documents that just share information, other structures serve better.
