# The 5-Whys — Technique, Pitfalls, When to Stop

5-whys is a root-cause elicitation technique: start with an observed symptom, ask "why?" five times, each answer triggering the next question. Done well, it climbs from symptom to structural cause. Done badly, it rationalizes a predetermined conclusion.

## The technique

```
Observation:  [what you observe]
Why 1:        [why does the observation happen?]
Why 2:        [why does why-1's answer happen?]
Why 3:        [why does why-2's answer happen?]
Why 4:        [why does why-3's answer happen?]
Why 5:        [why does why-4's answer happen?]

Root cause:   [the answer to why-5, usually structural]
```

Each "why" should reveal a deeper constraint — not a synonym, not a restatement, not a person to blame.

## Worked example — good

**Observation**: Users abandon the signup flow at step 3.

1. **Why?** Because step 3 asks for a credit card before trial starts.
2. **Why?** Because marketing requested it to improve lead quality.
3. **Why?** Because the sales team complains about low-quality leads.
4. **Why?** Because lead scoring in CRM doesn't filter for intent well.
5. **Why?** Because the CRM uses generic scoring and was never tuned for our funnel.

Root cause: **CRM lead scoring is generic, not tuned for our funnel** — changing this resolves the cascade. Moving credit card to step 3 (the original complaint) was a symptom of bad lead scoring.

## Worked example — bad

**Observation**: Users abandon the signup flow at step 3.

1. **Why?** Because step 3 is too long.
2. **Why?** Because there are too many fields.
3. **Why?** Because we didn't design it well.
4. **Why?** Because we didn't have time to iterate.
5. **Why?** Because the deadline was tight.

Root cause: "tight deadlines" — dead end. Every "why" restates the previous one. No constraint is surfaced; the answer is a vague feeling.

## Pitfalls

### 1. Synonym walks

Each "why" is a rephrasing of the previous answer. Symptom: the answers sound identical in different words. Fix: if the answer does not name a new actor, constraint, or mechanism, re-ask.

### 2. Person-blame

Each "why" eventually lands on a person. "Because the intern didn't know." Symptom: root cause names an individual. Fix: ask "what made it possible for this person to not know?" — the real cause is usually the system that allowed the error, not the person who made it.

### 3. Stopping too early

The first satisfying answer is accepted as root cause. Symptom: the team stops at why-2 or why-3 because the answer is convenient. Fix: explicitly count — require five whys, not fewer.

### 4. Going past the actionable

The root cause is "because capitalism" or "because the universe is entropic." Symptom: the answer is outside the team's influence. Fix: stop at the deepest cause within your influence.

### 5. Cherry-picked branches

At each "why" there are multiple valid answers. The team picks the one that supports the conclusion they already had. Fix: at each step, list 2-3 possible answers and investigate the most likely, not the most convenient.

### 6. Single-path assumption

5-whys assumes a single causal chain. Real systems have multiple contributing causes. Fix: consider running 5-whys on 2-3 parallel branches and see whether they converge on one structural cause.

## When to stop

Stop climbing when one of these is true:

1. **You hit a structural cause** — an organizational policy, an incentive, a process, a technical design. Something you can name and act on.
2. **The next "why" goes outside your influence** — market conditions, industry regulation, physics.
3. **The next "why" returns to a synonym** — you've exhausted the chain; what you have is the root.

Do not stop when:

- You've hit an easy fix (fix the easy thing AND keep climbing to see if something deeper is also causing it).
- The answer is embarrassing (that's often the signal you're close to truth).
- You've reached "personal" — the person's actions are an effect, not a cause.

## Stopping conditions — quick reference

| Signal | Stop? |
|---|---|
| Organizational policy named | ✅ Stop |
| Process gap named | ✅ Stop |
| Incentive misalignment named | ✅ Stop |
| Technical design constraint named | ✅ Stop |
| "We didn't prioritize it" | ❌ Keep climbing — why? |
| A person's name | ❌ Keep climbing — what system allowed this? |
| "Because the market demands it" | ❌ Outside your control — back up one |
| "Because physics" | ❌ Outside your control — back up one |

## When 5-whys is the wrong tool

- **Multi-cause incidents** — use a fishbone diagram (Ishikawa) to capture multiple parallel causes.
- **Complex adaptive systems** — use systems-thinking with feedback loops; 5-whys assumes linear causation.
- **Ambiguous observations** — confirm the observation is real before running 5-whys (the symptom might be measurement error).
- **Non-technical, non-organizational problems** — 5-whys works best when the chain passes through systems you control.

## Integration with problem-definition

Use 5-whys after you have identified a symptom but before you write the problem statement. The root cause becomes the problem; the symptoms become the motivating evidence. Without 5-whys, problem statements often anchor at the symptom layer and the team solves the wrong problem.
