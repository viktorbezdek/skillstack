# Proven Copywriting Formulas

Six formulas, each with a long track record in commercial copywriting, applied to long-form technical content. None are magic; all reward deliberate practice. The formulas are scaffolds — they show you a sequence that works, not a substitute for the substance.

## AIDA — Attention, Interest, Desire, Action

The oldest and most general. Originated by E. St. Elmo Lewis (1898). Maps to the contract structure of any persuasive long-form piece.

### Phases

| Phase | Reader's state | Move |
|---|---|---|
| **Attention** | Hasn't decided to read | Hook that creates curiosity in 30 seconds |
| **Interest** | Open to reading | Promise that ties topic to reader's situation |
| **Desire** | Reading, evaluating | Build the case — why what's coming matters to *this reader* |
| **Action** | Convinced | Specific next step |

### In long-form technical content

| AIDA phase | Article element |
|---|---|
| Attention | Hook (paragraph 1-2) |
| Interest | Promise + setup (paragraphs 3-5) |
| Desire | Development + payoff |
| Action | Close (specific next step) |

### Worked example

**Article:** "Your Postgres database has more dead rows than live ones (and it's costing you)."

```
ATTENTION: "In 2023, a Postgres database I audited had 1,247 GB on disk and 200 GB of actual
            data. The other 1,000 GB was something the database technically couldn't read."

INTEREST:  "If you've ever had a database mysteriously fill its disk faster than your data
            grew, this is likely why. Most teams don't catch it until they're paying for
            storage they can't use."

DESIRE:    [Development: how dead tuples accumulate, why VACUUM matters, the long-running
            transaction trap, the audit query you can run.]

ACTION:    "Run this query on your largest table tonight. If dead_tuples is over 20%, you have
            a problem. The fix is in the next paragraph."
```

### When AIDA fails

- The piece is reference-shaped (whitepaper, doc) — no single "Action" lands cleanly.
- The reader is already convinced — AIDA assumes you're moving them; if they're already there, it patronizes.
- The piece is exploratory (an essay rather than an argument) — AIDA forces a closing move that may not exist.

## PAS — Problem, Agitate, Solve

High-conversion direct-response. Useful in opinion, case-study, and decision-support pieces. Caveat: the agitation must be *honest*, not manufactured.

### Phases

| Phase | Move |
|---|---|
| **Problem** | Name the problem the reader has |
| **Agitate** | Surface the cost — current, ongoing, future |
| **Solve** | Present the relief |

### In long-form technical content

PAS works best in two places:

1. **As the hook + setup** (sections 1-3 of an opinion or case study).
2. **As an embedded sub-structure** within a longer piece.

### Worked example

**Article:** "Your CI is the secret tax on your team's productivity."

```
PROBLEM:  "Your CI takes 12 minutes. Each PR runs it twice on average. Your team merges 80
           PRs a week."

AGITATE:  "That's 32 hours per week. Across a year, you're spending 1,664 engineer-hours on
           waiting for CI. At a fully-loaded $200/hour cost, that's $332,800 — and it
           compounds: slow CI causes batching, and batching makes the next iteration of CI
           slower."

SOLVE:    "Most CI is slow because of three patterns we'll diagnose, each with a known fix.
           After implementing all three on a 12-minute pipeline, ours dropped to 3 minutes."
```

### Honest agitation

The cost calculation must be defensible. Inflated agitation ("This is bankrupting your company!") is salesman talk and reads as such. Calibrated agitation grounded in the reader's actual situation respects them.

| Honest | Manipulative |
|---|---|
| "1,664 engineer-hours per year" (computed from stated assumptions) | "Massive productivity loss" |
| "Compounds when batching causes more conflicts" (mechanism stated) | "You'll never recover" |
| "Most teams don't catch this until [signal]" (specific signal) | "By the time you notice, it's too late" |

## BAB — Before, After, Bridge

A gentler PAS. Tutorials and case studies use this naturally.

### Phases

| Phase | Move |
|---|---|
| **Before** | The reader's current state, named honestly |
| **After** | The state after applying this — specific, vivid |
| **Bridge** | The path from Before to After (the article's body) |

### In tutorials

```
BEFORE:  "Right now, your multi-tenant Postgres app uses application-layer authorization. Every
          query has WHERE tenant_id = $current_tenant. One forgotten WHERE clause and a
          tenant sees another tenant's data."

AFTER:   "By the end of this tutorial, RLS will enforce isolation at the database layer. The
          'forgotten WHERE clause' bug class becomes structurally impossible. Your application
          code gets simpler. Your test surface area shrinks."

BRIDGE:  [The tutorial: enabling RLS, writing policies, integrating with the connection pool,
          writing tests.]
```

### In case studies

```
BEFORE:  "We had 47 microservices. Tracing a single request touched 12. The on-call rotation
          was a horror story."

AFTER:   "After the consolidation, we have 6 services. Tracing touches 2. On-call escalations
          dropped 70% in Q1."

BRIDGE:  [The case study: how they decided what to merge, what failed, what worked, what they'd
          do differently.]
```

## Bencivenga's pyramid (skepticism gradient)

Gary Bencivenga, often called the highest-paid copywriter in history, codified this principle: every reader starts skeptical. Each claim spends credibility; each piece of evidence earns it. Sequence claims so credibility *grows* through the piece — leading with the most outlandish claim wastes it.

### The pyramid

```
                  Outlandish-sounding-but-true conclusion
                  (the payoff that wouldn't have worked early)
                              ↑
                      Mid-credibility claims
                      (with evidence; some lift required)
                              ↑
                      Easy claims
                      (verifiable, low credibility cost)
                              ↑
                      Specific verifiable observations
                      (no credibility needed; just facts)
```

Build up. Don't lead with the controversial claim — lead with the verifiable observation that *implies* the controversial claim, then build the case.

### Worked example

**Article:** "There is no such thing as microservices."

The provocative claim is the conclusion, not the opening.

```
OPENING (verifiable):     "Last year I audited 12 'microservices' architectures. In 11 of them,
                           changing one service required coordinating changes in at least three
                           others within the same release window."

EARLY (easy):              "That's not a coincidence. The 12 architectures shared a structural
                           feature: they used services as their decomposition boundary instead
                           of using bounded contexts."

MID (some lift):           "When the service boundary doesn't match the change boundary, you
                           get distributed monoliths — services that *deploy* independently but
                           must *change* together."

LATE (more lift):          "And once you have distributed monoliths, every microservices
                           benefit (independent deploys, polyglot, scale-to-team) becomes a
                           cost to be paid rather than a benefit to be earned."

PAYOFF (the provocation):  "Which is why the term 'microservices' is misleading. The teams I
                           audited didn't have microservices — they had distributed coordination
                           costs they were paying for nothing."
```

If you'd led with the provocation ("there is no such thing as microservices"), the reader would have shut down. Building from verifiable to provocative gives the reader a path.

### Bencivenga rules

- **Lead with the most-believable, most-specific claim** in the section.
- **Spend credibility deliberately.** Each "trust me on this" needs to be earned.
- **Stack evidence before generalization.** Three specifics earn one generalization.
- **Save the provocative claim for the payoff** — the reader is now ready.

## Sugarman's slippery slide

Joseph Sugarman, BluBlocker founder and copywriter: every sentence has one job — to get the reader to read the next sentence.

### Implications

| Principle | Implication |
|---|---|
| **Velocity** | Short sentences accelerate; long sentences slow |
| **Curiosity gaps** | Partial reveals pull the reader forward |
| **Visual flow** | Short paragraphs, white space, lists = grease |
| **Concrete language** | Specific images grip; abstractions wash |
| **First sentences** | The first sentence sells the second; the second sells the third |
| **Page-break risks** | Don't end a section on a question if the reader has to scroll past an ad to find the answer |

### Sugarman openers

The Sugarman opener is short, specific, and unfinished:

```
"It started with a single line of code.

Or rather, three characters: `,, `."
```

Three short sentences. A specific detail. A question hanging (what could three characters do?). The slide pulls the reader to sentence four.

Compare:

```
"In this article, we will explore an interesting issue that arose in our codebase, which had to
 do with a small but consequential code change involving certain string-handling patterns."
```

Same idea, paragraph form. The reader's eye glazes by mid-sentence.

### Sugarman applied to technical content

- **Don't pack technical setup into the opener.** Lead with the surprise; defer the setup.
- **Break paragraphs at curiosity points.** A line break after "Or rather, three characters" forces the reader to commit to scrolling.
- **Use lists where the prose is grinding.** Sugarman knew lists weren't lazy — they were the slide.

### Sugarman violations

- The 200-word paragraph wall.
- Sentences that announce what they'll do ("In this section we will discuss…").
- Closed sentences at every break ("Now you know X. Moving on.").

## Schwartz's awareness levels

Eugene Schwartz, *Breakthrough Advertising* (1966): the reader's awareness of the problem and the solution determines the right hook.

### The five levels

| Level | Reader's state | Right hook framing |
|---|---|---|
| **Unaware** | Doesn't know the problem exists | The symptom; an artifact; a story |
| **Problem-aware** | Knows the problem, doesn't know solutions | Name the problem precisely; "you've felt this" |
| **Solution-aware** | Knows solutions exist, doesn't know yours | The differentiator; "here's a different way" |
| **Product-aware** | Knows your specific solution, not convinced | Objection-handling; "here's why this is better" |
| **Most aware** | Already convinced, just needs to act | The action; "here's what to do this week" |

### In technical content

Most technical articles target Problem-aware or Solution-aware audiences. Common mismatches:

| Mistake | Symptom |
|---|---|
| Pitching to Most-aware when audience is Problem-aware | Reads as preaching to the choir; bounces casual readers |
| Pitching to Unaware when audience is Solution-aware | Reads as condescending; explains what they already know |
| Pitching to Solution-aware when audience is Unaware | Reads as confusing; the differentiation isn't visible because the problem isn't named |

### Calibration

To diagnose your audience's awareness level, ask:

1. Have they encountered this problem in their own work?
2. Have they tried solutions to it?
3. Have they tried *your* approach to it?
4. Are they convinced your approach is right?

The answer to "the lowest 'no' question" is your audience's awareness level.

### Worked frame: same article, different awareness levels

**Article topic:** "Why your CI is slow and how to fix it."

| Audience awareness | Hook |
|---|---|
| **Unaware** ("CI feels fine to me") | "The hidden cost of CI: a calculation. Your team's CI takes 12 minutes. Across a year, that's 1,664 engineer-hours." |
| **Problem-aware** ("yes, it's slow, what can I do") | "Most CI slowness comes from three patterns. Each has a known fix. Here they are, in order of impact." |
| **Solution-aware** ("I know about caching/parallelism, what's new here") | "You probably already cache and parallelize. Here's the fourth move that's underused: profiling the *test selection* layer." |
| **Product-aware** ("I've heard of test selection, not convinced it's worth it") | "Test selection sounds expensive to set up. We invested 3 days; saved 4 minutes per pipeline run. Here are the numbers." |
| **Most aware** ("convinced, ready to do it") | "Test selection setup, in 5 steps: [the tutorial]." |

Each frame respects where the reader actually is. A piece that gets the awareness level right reads as written for *the reader*; a piece that gets it wrong reads as written for someone else.

## Combining formulas

The formulas aren't mutually exclusive. A piece can be:

- AIDA-shaped overall, with a PAS opener.
- BAB-framed for the high-level promise, with Bencivenga sequencing through the body.
- Schwartz-aware in framing, with Sugarman's slippery slide running through every paragraph.

Think of the formulas as lenses. Apply the ones that fit the piece; don't force-fit all six.

## Anti-patterns

### Formula as substitute for substance

A piece using AIDA perfectly with no real claims is empty. The formula amplifies what's there; it doesn't manufacture content.

### Formula visible

The reader shouldn't be aware of the formula. "Now we agitate the problem" being visible is a sign the formula is being applied mechanically. Good formula application disappears.

### Wrong formula for the genre

PAS in a meditative essay reads as a sales pitch. AIDA in a whitepaper feels marketing-coded. Match formula to genre.

### Bencivenga without evidence

The pyramid only works if you actually have the evidence to support each rung. Stacking unsupported claims and building to a "provocative payoff" is hand-waving wearing a structure.
