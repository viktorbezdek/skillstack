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

## When to Use

- A brief or feature request needs to be unpacked into the underlying problem
- You suspect the team is solving the wrong problem
- You need to separate symptoms from root causes
- You want to apply 5-whys to a product or organizational issue
- You need to write a problem statement with assumptions and not-goals
- You want to surface hidden assumptions about what's being solved

## When NOT to Use

- Ideating or brainstorming candidate solutions (use creative-problem-solving)
- Diagnosing code, test, or CI bugs (use debugging)
- Ranking problems by priority (use prioritization)
- Writing a value proposition (use value-proposition-design)
- Identifying user needs (use user-needs-identification)

## Decision Tree

```
What problem framing problem do you have?
│
├─ Brief says "build X" — is X the problem?
│  ├─ X names a feature? → It's a solution, not a problem; apply JTBD
│  ├─ X names a metric? → It's a symptom; apply 5-whys
│  └─ X names a situation? → Closer; check for who/what/why-now gaps
│
├─ Symptom vs problem confusion
│  ├─ "Users churn in week one" → Symptom; 5-whys to find root cause
│  ├─ "Users can't get a working result in first session" → Problem ✅
│  └─ "Need a dashboard" → Solution in disguise; extract the job
│
├─ Writing a problem statement
│  ├─ Can't name a specific segment? → "Users" is too broad; narrow it
│  ├─ No current workaround documented? → You don't know how they cope yet
│  └─ No "why now" answer? → The problem may not be urgent enough to solve
│
└─ Validating an existing problem statement
   ├─ Names a feature as the problem? → Reframe as a job to be done
   ├─ Segment is "everyone"? → Too broad; narrow to a specific group
   └─ No assumptions listed? → Add 2-3 beliefs that, if wrong, invalidate the problem
```

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

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Solutioning the brief | Brief says "build X"; the problem behind X is never stated | Reframe: what job is X being hired for? What constraint makes X necessary? |
| Problem-as-feature | "Users need Slack integration" is a solution; the problem is a workflow broken by app-switching | Extract the job: "When I'm in my workflow, I want to notify the team, so I can..." |
| Segment of one | Problem defined around a single user interview and generalized without evidence | Validate with 3-5 more data points before committing resources |
| Symptom persistence | Problem statement names a metric ("reduce churn") instead of the underlying user situation | 5-whys from metric to root cause; restate as a job |
| Frozen not-goals | Not-goals never change as understanding improves | Revisit not-goals each iteration; they should evolve with understanding |
| No assumptions listed | Team proceeds without surfacing what they're betting on | List 2-3 assumptions; design a test for each |
| Skipping the current workaround | You don't know how users cope today, so you can't measure improvement | Document the workaround; the gap between workaround and ideal IS the problem |

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
