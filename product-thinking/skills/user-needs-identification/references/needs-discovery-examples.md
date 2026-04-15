# Needs Discovery — Before/After Examples

The gap between a stated want and the underlying need is where product decisions go wrong. These examples show user wants transformed into full three-dimension job statements.

## Example 1 — B2B SaaS notifications

### Stated want
> "I want real-time push notifications for every event in our system."

### Wants-vs-needs ladder

1. **Mirror**: "Real-time notifications for every event."
2. **Why**: "So I don't miss anything important."
3. **Context**: "When a customer escalates, or when a service degrades."
4. **Outcome**: "I find out within 5 minutes and can respond before the customer calls."
5. **Alternative**: "Today I watch dashboards. It's exhausting. Or I rely on my team to Slack me, but they miss things too."

### Job statement

```
JOB STATEMENT

Functional:  When a customer-impacting event occurs in our system, I want to
             know within 5 minutes so I can respond before the customer escalates.
Emotional:   I want to feel confident nothing is silently failing. I want to
             avoid the feeling of being blindsided by a customer escalation
             I didn't know about.
Social:      I want my team and my boss to see me as the person who spots
             issues before they explode.
Frequency:   Several times per week.
Pain today:  Watching dashboards is exhausting; relying on team to notify is
             unreliable; customer escalations still surprise me 1-2 times/month.
Workaround:  Multiple browser tabs + custom Slack channels + a personal Notion
             page tracking suspicious patterns.
```

What changed: the stated want ("push notifications for every event") was a solution. The need is "know within 5 minutes about customer-impacting events" — which is served by intelligent filtering and prioritization, not by notifying every event. The emotional layer (not being blindsided) and social layer (being the spotter) shape which notifications matter most.

## Example 2 — Consumer fitness app

### Stated want
> "I want detailed charts of my workout progress over time."

### Ladder

1. Mirror: "Detailed progress charts."
2. Why: "To see if I'm actually improving."
3. Context: "Mostly Sunday evening, planning the next week."
4. Outcome: "Feel like the effort is paying off and know what to focus on."
5. Alternative: "I could ask a trainer, but that's expensive. I could journal, but I don't."

### Job statement

```
JOB STATEMENT

Functional:  When planning next week's workouts on Sunday, I want to see what
             has been working and what hasn't so I can choose the right mix.
Emotional:   I want to feel that the time I'm spending is producing results.
             I want to avoid the feeling of "am I wasting my time on this?"
Social:      Not strongly social — solo activity for this user. But partly
             tied to posting progress occasionally to a friend.
Frequency:   Weekly, Sunday evening.
Pain today:  Progress feels invisible week-to-week; motivation dips when I
             can't see movement.
Workaround:  Nothing — gives up on tracking or forgets entirely.
```

What changed: the stated want (detailed charts) was oriented toward analysis. The underlying need is emotional — "feel that effort is paying off." A product that just shows charts may not solve this; a product that shows *evidence of meaningful change* (even weekly) would. The Sunday-evening trigger and planning context are critical — detailed charts delivered in the middle of a workout would be wrong.

## Example 3 — Developer tool

### Stated want
> "I want a keyboard shortcut for the search function."

### Ladder

1. Mirror: "Keyboard shortcut for search."
2. Why: "The mouse interrupts my flow."
3. Context: "While I'm coding, I switch to your tool multiple times to look something up."
4. Outcome: "Look up a thing and return to my IDE without losing my train of thought."
5. Alternative: "I copy and paste into a terminal sometimes."

### Job statement

```
JOB STATEMENT

Functional:  When I am mid-thought in code and need to look up a reference in
             your product, I want to find it and return to my IDE without
             losing cognitive context.
Emotional:   I want to feel in flow, not fragmented. I want to avoid the
             feeling of "now I've lost what I was doing."
Social:      Weakly — signaling to peers who watch me work that I'm efficient
             and don't break flow for small tasks.
Frequency:   Many times per day.
Pain today:  Each lookup costs 15-30 seconds of context restoration; over
             a day that is real time and measurable frustration.
Workaround:  Second monitor with tool pre-loaded; browser bookmarks; the
             paste-to-terminal trick.
```

What changed: the stated want (keyboard shortcut) is one possible solution. The real need is "don't break flow" — which could be served by a keyboard shortcut, a quick-switcher overlay, an IDE integration, or a CLI. Knowing the need opens the solution space; only knowing the want would have locked the team into shipping the literal shortcut.

## Example 4 — Internal admin tool

### Stated want
> "I want to bulk-update 500 records at once."

### Ladder

1. Mirror: "Bulk update 500 records."
2. Why: "I'm fixing data that was imported wrong last quarter."
3. Context: "Monday after a quarterly import. Always the same task."
4. Outcome: "Fix the data without manually clicking 500 times."
5. Alternative: "Engineering writes a one-off script, but it takes 2 weeks to get scheduled."

### Job statement

```
JOB STATEMENT

Functional:  When quarterly imports bring in data with predictable errors,
             I want to correct the errors in bulk without engineering support.
Emotional:   I want to feel capable of handling my own work. I want to avoid
             the feeling of being dependent on engineering for a routine task.
Social:      I want my team to see operations as self-sufficient, not
             engineering-dependent.
Frequency:   Quarterly (4 times a year, very concentrated).
Pain today:  2 weeks of lag to get engineering help; manual clicking takes
             a full day and is error-prone.
Workaround:  Wait for engineering; or click manually; or use an Excel
             export-edit-reimport cycle that sometimes corrupts data.
```

What changed: the stated want is a feature (bulk update). The real need is operational self-sufficiency — the user wants to not be engineering-dependent for routine tasks. This reframes the solution space: bulk update is one path, CSV import with data corrections is another, a pre-import validation step that prevents errors is a third (and potentially better) path.

## Lessons from the examples

1. **Every want hides at least one job layer the user hasn't named.** The ladder surfaces it.
2. **The emotional layer is often the primary driver.** Functional alone rarely explains adoption or loyalty.
3. **The workaround is evidence.** How the user copes today is the most reliable data for what need is real.
4. **The alternative question (step 5) is diagnostic.** Users who have no alternative have anchored to a specific solution; re-ask.
5. **Frequency determines prioritization.** A strong need that arises quarterly competes with weaker needs that arise daily.

## Using the examples

For each user you're researching:

1. Collect the stated want verbatim.
2. Walk the five-step ladder.
3. Fill the three-dimension job statement template.
4. Identify the workaround — that's the strongest signal.
5. Compare to similar users in the segment. If the job statement matches, you have segment-level evidence.
