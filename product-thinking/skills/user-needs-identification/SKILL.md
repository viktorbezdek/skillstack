---
name: user-needs-identification
description: >-
  Identify what users actually need using functional/emotional/social jobs,
  needs-vs-wants laddering, latent-need surfacing, and job statements. Use
  when the user asks what users truly need, wants to write a job statement
  (When/I-want-to/So-I-can), wants to move past stated wants to underlying
  needs, needs to separate functional jobs from emotional or social ones, or
  wants to spot latent needs the user cannot articulate. NOT for persona
  demographics (use persona-definition). NOT for stakeholder power maps (use
  persona-mapping). NOT for interview scripting (use elicitation).
---

# User Needs Identification

Users tell you what they want. They rarely tell you what they need. The two are different and treating them as the same is the fastest way to build a feature that gets used once and never again.

## When to Use

- Moving past stated wants to underlying needs
- Writing job statements (When/I-want-to/So-I-can)
- Separating functional jobs from emotional or social ones
- Surfacing latent needs users cannot articulate
- Identifying workarounds, apologies, and shadow tools that signal unmet needs

## When NOT to Use

- Persona demographics (use persona-definition)
- Stakeholder power maps (use persona-mapping)
- Interview scripting (use elicitation)
- Writing value propositions (use value-proposition-design)
- Problem framing (use problem-definition — do that first)

## Decision Tree

```
What needs identification problem do you have?
│
├─ User said "I want X" — is X a need or a want?
│  ├─ X names a specific solution? → It's a want; run needs-vs-wants ladder
│  ├─ X names a goal/outcome? → It's closer to a need; extract the job
│  └─ X names a feeling? → It's an emotional job; name it explicitly
│
├─ Have wants, need to find needs
│  ├─ User described a dashboard/feature? → Run the 5-step ladder (Mirror → Why → Context → Outcome → Alternative)
│  ├─ User described a pain? → Pain = functional job gap; what job is blocked?
│  └─ User described a behavior? → Workaround = latent need signal
│
├─ Which job dimensions matter?
│  ├─ Task-oriented? → Functional job (what they're literally trying to do)
│  ├─ Feeling-oriented? → Emotional job (how they want to feel)
│  └─ Perception-oriented? → Social job (how they want to be seen)
│
└─ Finding latent needs
   ├─ Users have workarounds? → Unmet need (product didn't intend the workaround)
   ├─ Users apologize for using alternatives? → Unmet need (main tool doesn't cover it)
   ├─ Users pay for shadow tools? → Misaligned need (official tool doesn't serve them)
   └─ Same question repeated in support? → Unmet need (UI doesn't address it)
```

## Wants vs needs vs jobs

| Layer | What the user says | What it actually is |
|---|---|---|
| Want | "I want a dashboard with 12 widgets." | A solution they imagined. |
| Need | "I need to know at a glance whether the system is healthy." | The underlying requirement. |
| Job | "When I start my shift, I want to verify nothing burned down overnight so I can triage before standup." | The situation + motivation + outcome. |

Build for the job, not the want. The want is usually wrong about the how. The job is usually right about the why.

## Three job dimensions

Every job a user hires a product to do has three facets. Name all three or you are optimizing for one and ignoring the others.

### Functional jobs

What the user is literally trying to accomplish. "Send an invoice." "Deploy a service." "Split a bill." Measurable, observable, the easiest to elicit.

### Emotional jobs

How the user wants to feel — or avoid feeling — while doing the functional job.

| Functional job | Emotional job |
|---|---|
| Deploy a service | Not feel like I am about to break production |
| Submit expenses | Not feel micromanaged |
| Learn a new tool | Not feel stupid |

Emotional jobs explain why two tools with identical features get radically different adoption.

### Social jobs

How the user wants to be perceived by others while doing the job.

| Functional | Social |
|---|---|
| Post a status update | Appear productive to my manager |
| Choose an IDE | Signal that I am a serious developer |
| File a bug | Not look like the person who broke it |

Social jobs drive tool choice in organizations more than teams admit. Missing them produces features that are "technically correct" and politically dead.

See `references/jobs-framework-deep-dive.md` for the full taxonomy.

## Needs-vs-wants extraction technique

When a user gives you a want, run this ladder:

1. **Mirror** — "You want a dashboard with 12 widgets."
2. **Why** — "What would the dashboard let you do that you can't do today?"
3. **Context** — "When would you use it? What triggers the need?"
4. **Outcome** — "If the dashboard worked perfectly, what would be different for you?"
5. **Alternative** — "If I could not build a dashboard, what else would solve this?"

Step 5 is the diagnostic — if the user has no alternative in mind, the want is anchored to a solution they already imagined, and the underlying need is unstated. Re-ask until you surface the job.

## Latent needs — what users cannot articulate

Some needs are invisible to the user because they are habituated. They work around the pain so effectively they don't know it is pain. Four signals:

1. **Workarounds** — the user does a thing the product did not intend. The workaround points to an unmet need.
2. **Apologies** — "Sorry, I still use a spreadsheet for this." The apology flags a job the main product is not doing.
3. **Shadow tools** — people pay out-of-pocket for tools that duplicate official tooling. Shadow = misaligned need.
4. **Repeated questions** — the same question in support / forums / Slack means the product leaves the need unaddressed in the UI.

Full latent-need surfacing techniques in `references/latent-needs-techniques.md`.

## The needs discovery workflow

1. **Collect wants.** Ask what the user wants. Record verbatim.
2. **Extract jobs.** For each want, run the needs-vs-wants ladder. Stop at the functional job.
3. **Layer emotional and social.** For each functional job, ask "how do you want to feel while doing this?" and "who sees you doing this?"
4. **Surface latent needs.** Look for workarounds, apologies, shadow tools, repeated questions.
5. **Rank by frequency and pain.** Not all needs are equal — which hit daily and cost the most?
6. **Write job statements.** Use the template below.

## Job statement template

```
JOB STATEMENT

Functional:  When [context], I want to [motivation], so I can [outcome].
Emotional:   I want to feel [emotion] / avoid feeling [emotion] while doing this.
Social:      I want to be perceived as [perception] by [audience].
Frequency:   [how often this job arises]
Pain today:  [what currently prevents or degrades the job — measurable]
Workaround:  [how the user copes without the ideal solution]
```

## Anti-patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Feature-as-need | "Users need notifications" is a feature, not a need | Reframe: "I want to know when X happens without having to check" |
| Ignoring the emotional layer | Everything measured in minutes saved, not anxiety reduced | Name emotional jobs explicitly; they drive retention more than functional ones |
| Projecting needs | Team imagines what users need without evidence | Build on observed behavior, not team intuition; interview and watch, don't guess |
| Averaging needs | Aggregating across segments produces a product that serves nobody well | Segment first, then identify needs per segment |
| Stopping at the functional | Functional jobs are easiest to elicit, so teams stop there | Always ask emotional and social layers; they determine adoption |
| Taking wants at face value | Building the dashboard with 12 widgets because users asked for it | Run the needs-vs-wants ladder on every want before building |
| Missing latent needs | Only looking at what users say, not what they do | Audit for workarounds, apologies, shadow tools, and repeated support questions |

## References

| File | Contents |
|---|---|
| `references/jobs-framework-deep-dive.md` | Functional/emotional/social jobs with interview prompts and scoring |
| `references/latent-needs-techniques.md` | Workaround-spotting, shadow-tool audits, apology mining |
| `references/needs-discovery-examples.md` | Before/after job statements across B2B SaaS, consumer, internal tools |

## Related skills

- **problem-definition** — frame the problem before identifying the needs within it.
- **persona-definition** — define the user segment for whom you identify needs.
- **persona-mapping** — map stakeholders and power dynamics around the user.
- **elicitation** — design the interview protocol that surfaces needs.
- **value-proposition-design** — turn identified needs into a value proposition.
