# When to Fork (Canonical vs Custom)

Decision tree for when to brief a canonical persona with extra context vs design a new custom persona.

## The decision tree

```
Topic needs a perspective. Does one of the canonical 12 cover it?

├── YES, well → use the canonical persona, standard prompt
├── YES, partially → brief the canonical with EXTRA CONTEXT
└── NO → design a custom persona
```

## "Brief with extra context" — the middle path

Often you don't need a custom persona — you need to *brief* a canonical persona with domain-specific context.

### Examples

**Topic: a fintech compliance question**
- Canonical Operator handles security/reliability, but not financial regulation
- Don't design a "Compliance Officer" persona for this one question
- Instead: brief the canonical Operator with extra context:

```
Topic: [fintech compliance question]
Context: [normal context]
+ Additional context: This product is regulated under [specific reg]. The
  Operator perspective should specifically attend to: audit trail requirements,
  encryption-in-transit and -at-rest requirements, segregation of duties for
  financial operations, the [specific compliance program] checklist.
```

The Operator brings security+production-reliability rigor, augmented with the regulatory specifics. Often this is enough.

**Topic: a healthcare app feature**
- Canonical User Advocate handles "user perspective", but not clinical workflow
- Brief instead of forking:

```
Topic: [healthcare feature]
Context: [normal]
+ Additional context: Users include nurses doing 12-hour shifts and physicians
  who get 5 minutes per patient. The User Advocate perspective should
  consider: cognitive load during high-stress shifts, charting burden,
  interruption tolerance, EHR integration patterns.
```

The User Advocate brings the user-centric voice; the brief tightens it to the specific clinical context.

### When to brief vs fork

| Situation | Approach |
|---|---|
| Canonical handles 80% of the topic | Brief with context |
| Canonical handles 50% | Probably fork, depends on the missing 50% |
| Canonical handles < 30% | Fork |
| Brainstorm has 3+ topics in the missing domain | Fork (the custom persona pays back across topics) |
| Brainstorm has 1 topic in the missing domain | Brief the canonical |

## When to fork (design custom)

Fork when:

1. **The missing perspective is load-bearing** for the brainstorm
2. **The canonical persona's voice would be inappropriate** in the missing domain (e.g. forcing PM voice into a medical-legal question)
3. **The missing perspective recurs** across multiple brainstorms in this domain
4. **The expertise needed is genuinely specialized** (lawyer, security researcher, physician, economist)

## When NOT to fork

Don't fork for:

1. **Voice variations** — "I want a more enthusiastic Skeptic" is not a custom persona; it's a tone request, fix the brief
2. **Combining canonicals** — "PM + Engineer combined" is not a custom persona; spawn both canonicals
3. **Over-specialization** — "Senior Engineer specifically for Postgres" is too narrow; brief the canonical Engineer with Postgres context
4. **Persona-as-stand-in for the user's view** — "Visionary Founder" persona that just says what the orchestrator wants to hear

## Domain-fork patterns

Domains where forking is consistently justified:

| Domain | Fork-worthy custom persona | Why |
|---|---|---|
| **Finance / fintech** | CFO, Compliance Officer | regulatory specifics canonical doesn't carry |
| **Healthcare** | Clinician, Healthcare Admin, Privacy Officer | clinical workflow + HIPAA + medical liability |
| **Defense / govtech** | FedRAMP Specialist, ATO Reviewer | accreditation specifics |
| **EdTech** | Teacher, Student Privacy Officer, District IT | classroom workflow + FERPA |
| **B2B sales-led** | Enterprise Sales Lead, RevOps, CS Lead | deal mechanics + retention |
| **B2C consumer** | Growth Marketer, Lifecycle Marketer | consumer psych + acquisition channels |
| **Hardware** | Mechanical Engineer, Manufacturing Lead | physical-world constraints |
| **AI / ML** | ML Engineer, Eval Specialist, Safety Researcher | model-specific concerns canonical Engineer doesn't carry |

## Domains where canonical usually suffices

Most general SaaS, web, mobile, dev-tools, internal tooling. The canonical 12 cover the common ground. Brief them with topic context; resist the urge to invent custom personas.

## The "this is just a tone variation" check

A common mistake: thinking you need a custom persona when you actually need a tone variation.

| Thought | Better fix |
|---|---|
| "I want a more aggressive Skeptic" | Brief Skeptic with: "Be direct; don't soften. Take the hardest line." |
| "I want PM but more strategic" | Brief PM with: "Frame this as a strategic decision; consider 12-month implications." |
| "I want Engineer but for staff-level" | Brief Engineer with: "Consider this from a staff-engineer perspective: trade-offs across teams, technical debt implications, hiring market." |

If the change you want is in voice/tone/altitude, brief the canonical. Don't fork.

## Workflow for deciding

1. **Read the topic.** What perspectives would actually help?
2. **List the canonicals that fit.** Which of the 12 cover this?
3. **Identify the gap.** What perspective is genuinely missing?
4. **Ask: brief or fork?**
   - If briefing the canonical with context fills the gap → brief it
   - If a custom persona is needed → design it
5. **If forking, sanity-check.** Would the custom persona contribute something a briefed canonical wouldn't? If no, fall back to briefing.

## When to ship the custom persona as a saved subagent

If a custom persona recurs (you find yourself designing the same one repeatedly), promote it to a saved subagent in `agents/`. This:

- Removes the per-brainstorm prompt construction work
- Lets others invoke the persona too
- Treats the custom persona like a canonical

The threshold: if you've designed the same custom persona 3+ times, ship it.

## Recurring custom personas worth shipping

Track which custom personas you build repeatedly. Common candidates that have proven worth shipping in production swarms (consider promoting if your domain calls for them):

- CFO (financial decisions)
- General Counsel (legal/compliance)
- Security Engineer (deeper than Operator)
- Sales Lead (B2B deal floor)
- Marketing Lead (positioning + launch)
- Customer Success Lead (B2B retention)
- Data Scientist (measurement + experiments)
- Hiring Manager (team-impact decisions)

The brainstorm-swarm plugin ships only the canonical 12. The others are inline customs. If your team brainstorms in a domain that's a good fit for a custom persona, design + save it locally; promote it via PR if it generalizes.
