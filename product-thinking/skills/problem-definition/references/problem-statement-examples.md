# Problem Statement — Good vs Bad Examples

Each example shows a problem statement at three quality levels: solution-shaped (bad), symptom-anchored (weak), and problem-sharp (good). The progression shows what it means to climb from brief to problem.

## Example 1 — B2B SaaS onboarding

### Solution-shaped (bad)

> "Users need a product tour with tooltips on every page."

Problem: this is a solution. It tells the team what to build, not why.

### Symptom-anchored (weak)

> "New users churn at 45% within 7 days."

Problem: this is the symptom, measured. It does not tell you why users churn or what job they are trying to do.

### Problem-sharp (good)

```
PROBLEM STATEMENT

Who:        New users at companies of 10-50 employees, technical role, signed up
            but have not yet invited teammates.
Context:    Within 7 days of signup, typically during their first work week
            using the product.
Job:        Evaluate whether the product solves a team problem they can champion
            to their manager and team.
Current:    They explore alone, trying to understand if the product has
            collaborative features by clicking around.
Gap:        The product surfaces no evaluation path — the value is collaborative
            but the new-user experience is single-player. They cannot form an
            opinion to take back to their team.
Why now:    Q3 competitive pressure from [competitor] that ships a guided team
            evaluation mode; our win rate in evaluations is dropping.
Assumptions: (1) Users want to champion internally, not decide individually.
            (2) The decision happens within 7 days; past that they forget.
            (3) A guided path with a teammate is more valuable than more features.
Not-goals:  - Improving single-player usability beyond current levels.
            - Replacing the existing documentation site.
            - Converting free users to paid in the trial window.
```

What's different: the statement names who, when, the job, the current behavior, the specific gap, the urgency, the assumptions, and what's out of scope. The team can evaluate proposals against it.

## Example 2 — Consumer app growth

### Solution-shaped

> "We need a referral program."

### Symptom-anchored

> "Our k-factor is 0.3, below industry average."

### Problem-sharp

```
PROBLEM STATEMENT

Who:        Users who completed ≥3 sessions and have shared content externally
            at least once (via screenshot, link share, or copy).
Context:    The moment after they share — the "hot moment" of engagement.
Job:        Invite a specific friend they want to share the experience with.
Current:    They share a screenshot or copy a URL; the recipient lands on a
            generic marketing page with no context for the shared item.
Gap:        The invite flow is not designed around the hot moment. Sharing
            today is "export the thing"; inviting a specific person is
            manual and awkward.
Why now:    Growth forecast requires k-factor ≥ 0.8 by EOY. Current rate
            projects to miss target by Q4.
Assumptions: (1) Users have specific people they'd want to invite in the hot
            moment. (2) Existing shares are a leading indicator of willingness
            to invite. (3) The friction is the flow, not the intent.
Not-goals:  - General referral rewards program for all users.
            - Redesigning the share functionality itself.
            - Monetization via referrals.
```

## Example 3 — Internal developer tool

### Solution-shaped

> "Build a CLI."

### Symptom-anchored

> "Engineers complain the GUI is slow."

### Problem-sharp

```
PROBLEM STATEMENT

Who:        Backend engineers who use the deploy dashboard 5+ times per day.
Context:    During focused work sessions — they task-switch to the dashboard to
            check status, trigger deploys, or verify configuration.
Job:        Complete a deploy-related action without breaking flow.
Current:    They open a browser tab, navigate the dashboard, wait for pages
            to load, click through multiple screens, then return to their IDE.
            Typical interaction: 45-90 seconds for an action that takes 2
            seconds of actual work.
Gap:        The interface optimizes for discovery (first-time users) and
            observability (managers). Daily users do the same 3-4 tasks
            repeatedly and pay the discovery tax every time.
Why now:    Engineering productivity survey last quarter identified the
            dashboard as the #3 context-switch pain. Mitigating #1 and #2
            are longer-term; this is the tractable one this quarter.
Assumptions: (1) Power users do a small set of repeat actions. (2) The cost
            is context-switch time, not dashboard capability. (3) Better
            keyboard / scriptable access would be adopted.
Not-goals:  - Redesigning the GUI for first-time users.
            - Making the dashboard faster (it's already within acceptable
              latency for its primary audience).
            - Building monitoring / alerting features.
```

## Common failure patterns

### Failure 1 — "users" as segment

A statement that says "users" does not specify who has the problem. Real segments are concrete: "admins of teams with 20+ members using the product for >6 months."

Fix: replace "users" with a named segment. If you can't name a segment, do more research before writing the statement.

### Failure 2 — no trigger

A problem without a context/trigger cannot be designed for at the moment of need. "Users want to understand their data" has no moment; "when opening the dashboard on Monday morning to review the weekend's traffic" does.

Fix: add the When — what triggers the job to arise?

### Failure 3 — assumptions skipped

The Assumptions line is often cut because it feels redundant. It's the most valuable. Assumptions surface what you're betting on; wrong assumptions invalidate the problem even if the problem is otherwise well-stated.

Fix: force at least 2-3 assumptions per problem statement. If you can't name any, your problem is almost certainly over-specified or relying on implicit beliefs.

### Failure 4 — no not-goals

Without not-goals, scope creep during the build is guaranteed. Every adjacent problem will pull the team.

Fix: for each problem, list 3-5 adjacent problems that are explicitly not being solved.

### Failure 5 — timeless problem

"Why now?" is missing. Without urgency, the problem competes with every other problem forever and never gets prioritized.

Fix: name the specific reason this quarter is when to act. If there is no reason, the problem probably isn't this quarter's priority.

## How to use these examples

1. Write a draft of your problem statement using the template.
2. Compare to the "problem-sharp" examples above for structural completeness.
3. Look for: named segment, specific trigger, explicit job, measurable gap, dated urgency, listed assumptions, explicit not-goals.
4. Show to someone outside the team. Can they restate it? If not, refine.
