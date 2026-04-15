---
name: problem-definition
description: >-
  Frame the real user or business problem (not a code/test bug) using
  Jobs-To-Be-Done, the 5-whys ladder, and problem-vs-symptom separation. Use
  when the user asks "are we solving the right problem", wants to write a
  problem statement, needs to separate problems from symptoms, wants to apply
  5-whys to a product or organizational issue, suspects a brief conflates a
  feature with a problem, or wants to surface assumptions about what problem
  is actually being solved. NOT for ideating or brainstorming candidate
  solutions (use creative-problem-solving). NOT for diagnosing code, test, or
  CI bugs (use debugging). NOT for ranking problems by priority (use
  prioritization).
---

# Problem Definition

Most products fail not because the solution was wrong, but because the problem was never sharpened. Teams jump from brief to build, skipping the step where they ask what problem they are actually solving, for whom, and why now.

## The three questions

Every well-defined problem answers these in one breath:

1. **Who** has the problem? (A specific segment, not "users.")
2. **What** are they trying to get done? (A job, not a feature.)
3. **Why** is it unsolved today? (Constraint, not just "nobody built it.")

If any of the three is missing or generic, stop and re-scope.

## Problem vs symptom vs solution

| Layer | Example |
|---|---|
| Symptom | "Users churn in the first week." |
| Problem | "New users cannot get a working result in their first session because setup requires three external accounts they do not have." |
| Solution | "Remove the account requirement for the first session." |

Teams debate solutions for weeks while the problem stays at the symptom layer. Force the climb from symptom to problem before discussing any solution.

## Jobs-To-Be-Done framing

A Job is what a user is hiring the product to do. Format:

> **When** [context / trigger], **I want to** [motivation], **so I can** [outcome].

Example:
> **When** I am onboarding a new hire, **I want to** give them a production-safe sandbox in one click, **so I can** unblock them without giving them prod credentials.

This framing separates the user's situation (context), motivation (what they are pulling toward), and expected outcome (success measure).

Three job dimensions exist and must be named separately — see `references/jtbd-framework.md`.

## The 5-whys ladder

Walk from stated problem to root problem by asking "why" five times. Each "why" should reveal a deeper constraint, not a synonym.

Example:

1. Users abandon the signup flow — **why?**
2. Because the email verification email is slow — **why?**
3. Because our queue worker is overloaded — **why?**
4. Because every signup triggers 12 side-effect emails — **why?**
5. Because marketing and product stacked their emails independently — **root problem: no shared transactional email policy.**

Stop when the next "why" becomes organizational ("because that's how it's always been") — that's the root cause. Full guidance in `references/five-whys-guide.md`.

## Problem statement template

```
PROBLEM STATEMENT

Who:        [specific segment]
Context:    [situation / trigger]
Job:        [what they are trying to get done]
Current:    [how they attempt it today]
Gap:        [where current fails — measurable]
Why now:    [reason this matters this quarter, not next]
Assumptions: [the 2-3 beliefs that, if wrong, invalidate the problem]
Not-goals:  [the adjacent problems we are explicitly not solving]
```

The `Assumptions` and `Not-goals` lines are the most often skipped and the most valuable. Assumptions surface what you are betting on; Not-goals prevent scope creep.

## Red flags — the problem is not yet defined

- The problem statement names a feature ("users need a dashboard").
- The affected segment is "users" or "everyone."
- The current workaround is not documented — you don't yet know how people cope without your product.
- The symptom and problem are not separated.
- Nobody can articulate why this matters this quarter.

If two or more of these are true, you do not yet have a problem — you have a brief. Go back to discovery.

## Workflow

1. **Restate the brief** in one paragraph without using the words "solution", "feature", or any proposed implementation.
2. **Identify the symptom** — the observable pain that triggered the conversation.
3. **Climb** with 5-whys until you hit a constraint you can name.
4. **Reframe as a Job** using the When/I-want-to/So-I-can template.
5. **Fill the template** including Assumptions and Not-goals.
6. **Challenge:** show the statement to someone outside the team and ask them to restate it. If they can't, it's not sharp enough.

## Anti-patterns

- **Solutioning the brief** — a brief says "build X"; the problem behind X is never stated, and the team accepts X as the problem.
- **Problem-as-feature** — "users need Slack integration" is a solution; the problem is a workflow broken by app-switching.
- **Segment of one** — the problem is defined around a single user interview and generalized without evidence.
- **Symptom persistence** — the problem statement names a metric ("reduce churn") instead of the underlying user situation that causes the metric to move.
- **Frozen not-goals** — not-goals that never change as understanding improves; they should be revisited each iteration.

## References

| File | Contents |
|---|---|
| `references/jtbd-framework.md` | Functional/emotional/social jobs, job hierarchy, interview prompts |
| `references/five-whys-guide.md` | 5-whys technique with worked examples, pitfalls, when to stop |
| `references/problem-statement-examples.md` | Good vs bad problem statements across SaaS, consumer, and internal tools |

## Related skills

- **user-needs-identification** — once the problem is framed, identify the jobs/needs behind it.
- **value-proposition-design** — once needs are understood, design the value proposition.
- **trade-off-analysis** — evaluate whether solving this problem is worth the cost of not solving others.
- **creative-problem-solving** — ideate solutions once the problem is defined.
