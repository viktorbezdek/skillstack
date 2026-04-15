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

- **Feature-as-need** — "users need notifications" is a feature, not a need. The need is "I want to know when X happens without having to check."
- **Ignoring the emotional layer** — everything is measured in minutes saved, not in anxiety reduced. Emotional needs drive retention.
- **Projecting needs** — team imagines what users need without evidence. Build on observed behavior, not on team intuition.
- **Averaging needs** — aggregating needs across segments produces a product that serves nobody well. Segment first, then identify needs per segment.
- **Stopping at the functional** — functional jobs are the easiest to elicit, so teams stop there and miss the emotional and social drivers that actually determine adoption.

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
