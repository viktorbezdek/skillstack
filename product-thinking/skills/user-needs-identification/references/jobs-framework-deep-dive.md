# Jobs Framework Deep Dive

User needs live in three dimensions: functional, emotional, social. This reference expands the framework with interview protocols, scoring, and common failure modes.

## The three dimensions in detail

### Functional

The observable task. "What is the user literally doing?"

Characteristics:
- Measurable (duration, frequency, success rate).
- Externally visible.
- The easiest dimension to elicit — users describe it readily.

Signals it is well-understood:
- You can name the trigger (what causes the job to arise).
- You can name success (what "done" looks like).
- You can name the current workaround (how users cope without an ideal tool).

### Emotional

Internal state during and after the job.

Signals:
- The word "feel" or "afraid" or "confident" appears in the interview without prompting.
- The user mentions stress, shame, embarrassment, relief, pride, frustration.
- The user describes workarounds that cost more time but avoid a feeling.

Important: emotional jobs include **negative valence** (avoiding bad feelings) as much as positive. Often the bigger driver is "don't make me feel stupid" rather than "make me feel smart."

### Social

Perception by others.

Signals:
- The user names the audience ("my boss sees this", "my team will notice").
- The user modifies behavior when observed vs. unobserved.
- The user is willing to sacrifice functional efficiency for social outcome.

Social jobs are strongest in:
- Tools with visible outputs (design, PRs, dashboards).
- Expensive tools (purchase signals competence).
- Tools used in team settings (the performance is observed).

## Scoring importance

For each identified job, score on three axes. Scales are 1-5; the product of all three is the importance.

| Axis | Question | Low (1) | High (5) |
|---|---|---|---|
| Frequency | How often does the job arise? | Yearly | Many times a day |
| Pain | How much does the job cost today (time, money, emotion)? | Minor inconvenience | Blocks real work |
| Unaddressed | How poorly does the current workaround / alternative solve the job? | Adequate | Fails completely |

Importance = Frequency × Pain × Unaddressed. Jobs with importance ≥ 60 (out of 125) are high priority.

## Interview protocols

### Switch interview (for existing products)

When a user switched from an old tool to a new one, four forces act on them:

1. **Push** of the old tool — what frustrated them?
2. **Pull** of the new tool — what attracted them?
3. **Anxiety** about the new tool — what made them hesitate?
4. **Habit** of the old tool — what held them back?

Interview the user about a specific recent switch. The forces reveal which jobs were under-served and which ones mattered enough to overcome switching cost.

### First-use interview (for prospects)

For users who have not adopted, walk them through their current day:

1. When do they encounter the job? (trigger)
2. What do they currently do? (workaround)
3. What does "good enough" look like today? (satisfaction threshold)
4. What would have to be true for them to try something new? (switching threshold)

### Observation over self-report

When possible, watch users do the job rather than hearing them describe it. Self-reports under-represent micro-frustrations, emotional states, and shortcuts. A 10-minute observation often produces more job evidence than a 60-minute interview.

## Common failure modes

- **Functional-only elicitation** — the interview produces a clean functional job description with no emotional or social layer. The resulting product feels correct but lacks adoption.
- **Leading questions** — "would you want a feature that X?" elicits compliance, not need.
- **Aggregating across segments** — the job profile is averaged across user segments and no longer applies to any specific user well.
- **Mistaking want for need** — the user names a solution they imagined; the team builds exactly that and discovers the underlying need was different.
- **Ignoring workarounds** — the most useful signal (what the user does today) is missed because the interview focuses on future features.
- **Missing the trigger** — the job is described in the abstract, not tied to a specific context. Without the trigger, you cannot design for the moment of need.

## Needs vs wants ladder (applied)

When a user states a want, apply the ladder:

1. **Mirror** — "So you want X."
2. **Why** — "What does X let you do that you can't do today?"
3. **Context** — "When does this come up? What triggers the need?"
4. **Outcome** — "If X worked perfectly, what would be different for you?"
5. **Alternative** — "If I could not build X, what else would solve this?"

Step 5 is diagnostic. A user who has no alternative has anchored to a specific solution. The underlying need has not been surfaced — keep asking.

## Output: the job map

For each segment, produce a job map.

```
SEGMENT: [name]

Top jobs (by importance score):
1. [job] | F: [functional] | E: [emotional] | S: [social] | Score: XX
2. [job] | F: [...]       | E: [...]       | S: [...]   | Score: XX
3. [job] | F: [...]       | E: [...]       | S: [...]   | Score: XX

Latent jobs (workarounds, apologies, shadow tools):
- [latent job 1]
- [latent job 2]

Signals to revisit:
- [anomalies to investigate]
```

The job map is the input to value-proposition-design and the bridge from needs research to build decisions.
