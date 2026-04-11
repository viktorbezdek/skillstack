> Data does not speak for itself. Charts without narrative are noise — and charts with the wrong narrative are worse than no charts because they mislead with the authority of numbers. This reference covers the structural frameworks, visual logic, and anti-patterns for communicating quantitative findings to human audiences.

---

## The Three Modes of Data Communication

Cole Nussbaumer Knaflic's distinction between modes is the most important diagnostic a data communicator can make.

| Mode | Who is it for | What is happening | Where storytelling applies |
|------|--------------|-------------------|---------------------------|
| Exploratory analysis | You, working alone | Finding what matters in the data | No — this is discovery work |
| Confirmatory analysis | You and a specific hypothesis | Testing whether something is true | Partially — the hypothesis shapes the frame |
| Explanatory communication | An audience who needs to act | Telling them what you found | Yes — narrative is required |

**The most common error in data communication:** Showing exploratory work to an explanatory audience.

An analyst who has spent two weeks in a dataset develops a map of all the patterns, exceptions, dead ends, and findings. Presenting all of this to an executive audience is not thoroughness — it is exporting your cognitive burden to people who are not equipped to sort it. The analyst's job is to do the sorting and deliver only the finding that requires a decision.

The exploratory dataset is your working notes. The explanatory presentation is the one paragraph that came out of those notes.

---

## Situation-Complication-Resolution (SCR)

From Barbara Minto's *The Pyramid Principle*, refined through decades of McKinsey consulting practice. Every data story should have this skeleton; without it, charts become orphan facts.

**Structure:**

| Part | Definition | Example |
|------|-----------|---------|
| Situation | Context the audience already agrees on | "Our Q2 retention rate has held steady at 87% for the past six quarters." |
| Complication | The thing that disturbed or threatens to disturb the status quo | "In Q3, we saw the first significant drop — retention fell to 79%, concentrated in the enterprise segment." |
| Resolution | What to do about it — the recommendation or the decision required | "We recommend an immediate review of the enterprise onboarding flow, starting with accounts that churned in the first 90 days." |

**Why this structure works for data:** It respects the audience's time (they understand the situation quickly), establishes stakes (the complication shows why this matters), and gives them a clear next action (the resolution). Dashboards without this frame require the audience to construct the complication and resolution themselves — most won't.

**Apply at every scale:** SCR works for a three-minute stand-up update, a single slide, a quarterly business review, and a 40-page analyst report. The content changes; the skeleton doesn't.

---

## The Story of the Data vs. The Data of the Story

Two fundamentally different modes of working with data — and conflating them is intellectually dishonest.

**Story of the data:** Start with the data. Ask what it says. Report what you find, including findings that contradict your expectations. This is honest discovery-driven analysis.

**Data of the story:** Start with a narrative you want to tell. Find data that supports it. This is persuasion.

Both modes exist in legitimate professional practice. Investor decks, product pitches, and advocacy campaigns are data of the story: you have a position, and you are marshaling evidence for it.

The problem is mixing them unconsciously. An analyst who believes the product is working will unconsciously select timeframes, segmentations, and metrics that confirm that belief — and present it as discovery-driven analysis. The audience believes they are receiving objective findings when they are receiving selective evidence.

**Discipline:** Be explicit with yourself and, when appropriate, with your audience about which mode you are in. "We set out to test whether X was true. Here is what we found" is story of the data. "Here is why we believe X is the right strategy, supported by three data points" is data of the story. Both are legitimate. Mislabeling one as the other is not.

---

## Knaflic's Six Lessons

From *Storytelling with Data*. These are sequential — each lesson depends on the one before.

| Lesson | Principle | Common failure |
|--------|-----------|---------------|
| 1. Understand the context | Who is the audience? What do they need to do? How will this be consumed? | Building a viz before answering these questions |
| 2. Choose an appropriate visual | Match chart type to the relationship you are communicating | Default to bar charts regardless of what the data is saying |
| 3. Eliminate clutter | Remove anything that does not add informational value | Gridlines, background colors, 3D effects, dual axes, logos |
| 4. Focus attention | Use color, size, and position to direct the eye to what matters | Treating all elements equally when one insight is central |
| 5. Think like a designer | Every element is a choice; every choice communicates | Treating visual presentation as decoration, not communication |
| 6. Tell a story | Every chart needs a beginning (context), middle (complication), and end (so what) | Delivering charts without answering "so what" |

---

## Chart Types as Narrative Devices

The chart is not the story — it is the evidence. Choose the chart type that makes the specific narrative claim visible.

| If the story is... | Use this chart |
|--------------------|---------------|
| Things are growing (or declining) | Line chart |
| These categories differ from each other | Bar chart (horizontal for long labels) |
| This one thing matters most | Single highlighted metric or big number with context |
| These two things are related | Scatterplot |
| This changed dramatically at a point in time | Line chart with annotation at the inflection point |
| These parts make up a whole | Stacked bar chart (rarely pie) |
| This is happening geographically | Map |
| The audience needs to look up specific values | Table |
| Comparing two time points for multiple items | Slope chart |

**Notes on specific chart types:**

- **Pie charts:** Only work with 5 or fewer slices, where proportions are meaningfully distinct. The human eye compares angles poorly; a bar chart is almost always more readable. Never use a pie to show that one slice is dominant — just show the one number.
- **Tables:** Tables are for reference, not presentation. If you are presenting to an audience, they cannot read a table and listen simultaneously. Use a chart; make the table available as an appendix or handout.
- **Dual-axis charts:** Rarely justified and frequently misleading. Dual axes allow the presenter to manipulate visual correlation by adjusting scale independently. The default assumption when you see a dual-axis chart should be skepticism.

---

## The Single-Sentence Summary Rule

If you cannot summarize the insight of a chart in one sentence, the chart is probably not ready.

**Test:** Write the headline before building the chart. The headline is the insight, stated plainly: "Enterprise churn increased 8 points in Q3" not "Q3 Churn by Segment."

A chart title that describes what the chart shows ("Monthly Active Users by Region, 2022-2024") is not a headline. It is a label. A headline states the finding: "Western region MAU growth outpaced all other regions for the third consecutive year."

**The headline test:** Show the headline to someone without showing the chart. If they can tell you what decision the insight requires, the headline is working. If they say "interesting, but what does that mean?" the headline is not the insight yet.

Every chart in a presentation should have a headline. Charts without headlines export interpretation to the audience.

---

## Executive Briefing Structure

Executives read in Z-pattern: top-left, top-right, then diagonal, then bottom. They skim before they read. They will often decide whether to engage with the full document based on the first two sentences.

**Structural principle:** Answer first. Then support. Then detail.

| Layer | Content | Format |
|-------|---------|--------|
| Top line | The single most important finding and its implication | One or two sentences, large, top-left |
| Supporting evidence | The two or three data points that make the top line credible | Charts or bullets, mid-section |
| Detail and methodology | How the analysis was done; data sources; caveats | Appendix or footnotes |

**The most common executive briefing error:** Burying the conclusion. Analysts are trained to show their work — the methodology, the data, the intermediate findings, and finally the conclusion. This is appropriate for academic communication and thoroughly wrong for executive communication. The executive does not need to understand how you got there; they need to know what to do. Lead with the conclusion.

---

## The Pyramid Principle

From Barbara Minto's *The Pyramid Principle*: any piece of communication should be structured as a pyramid.

```
          [Main Argument / Recommendation]
         /              |              \
  [Support 1]      [Support 2]      [Support 3]
    /    \            /    \            /    \
[data] [data]    [data] [data]    [data] [data]
```

**The principle:** Top = main argument. Middle = supporting arguments. Bottom = data.

**Why most data communication fails:** Analysts build from the bottom up (because that's how the analysis was done) and then present bottom-up. The audience gets the data before they know why it matters. The natural instinct to "show your work" is the enemy of clear communication.

**Minto's SCQA variant:** Situation → Complication → Question → Answer. The audience asks the question implicitly; your job is to have already answered it before they finish asking.

---

## The Before/After Transformation Pattern

A teaching technique as well as a communication technique. Showing a chart in its raw state and then progressively reducing it to the essential trains the audience to see what you see — and is itself a narrative.

**Steps:**

1. Show the original chart as exported from your tool: gridlines, legend, default colors, all data series.
2. Remove elements one at a time: gridlines first, then legend (move labels directly to lines), then background colors, then axis labels that repeat information.
3. Add emphasis: color the one line or bar that matters; gray out the rest.
4. Add the headline.

**Why it works in presentations:** Audiences who watch this transformation understand the reasoning behind the final chart in a way that seeing only the final chart does not produce. They absorb the principle, not just the output.

---

## Anti-Patterns

| Anti-pattern | Why it misleads | Fix |
|-------------|----------------|-----|
| Truncated Y-axis | Makes small differences look dramatic | Start bar charts at zero; annotate if starting elsewhere |
| Dual-axis charts | Two scales let you manufacture visual correlation | Use two separate charts; or use a scatterplot if correlation is the claim |
| Pie charts with more than 5 slices | Human eye cannot compare angles accurately | Use a bar chart |
| 3D charts | The third dimension adds no information and distorts area perception | Use 2D exclusively |
| Rainbow/sequential color for categorical data | Implies ordering or progression that doesn't exist | Use distinct, non-ordered colors for categorical; sequential palette for ordered data |
| Correlation presented as causation | Misleads the audience about mechanism | Add explicit disclaimer; name confounding factors; or avoid the claim entirely |
| Showing all the data | Overwhelms the audience with exploratory output | Apply SCR; present only the finding that requires a decision |
| Chart titles instead of headlines | Forces the audience to interpret the chart | Replace every title with a one-sentence insight statement |
| Unlabeled axes | Audience must guess the units | Always label axes with unit |

---

## Quick-Reference Checklist

Before presenting any data visualization:

- [ ] Is the chart type matched to the narrative claim?
- [ ] Does the chart have a headline (not a title)?
- [ ] Can you state the insight in one sentence?
- [ ] Have you applied SCR — does the audience know the situation, complication, and resolution?
- [ ] Is the Y-axis starting at zero (bar charts) or clearly annotated (line charts)?
- [ ] Has clutter been eliminated (gridlines, unnecessary legend, background, 3D effects)?
- [ ] Is the most important element visually emphasized?
- [ ] Are you in explanatory mode — have you already done the exploratory work and are now presenting only the finding?
- [ ] Are correlation claims flagged as correlation, not causation?

---

## Further Reading

- Cole Nussbaumer Knaflic — *Storytelling with Data* (2015)
- Edward Tufte — *The Visual Display of Quantitative Information* (2001)
- Barbara Minto — *The Pyramid Principle* (1987)
- Alberto Cairo — *The Functional Art* (2012)
- Alberto Cairo — *How Charts Lie* (2019) — a direct treatment of chart anti-patterns
- Dona Wong — *The Wall Street Journal Guide to Information Graphics* (2010)

---

> *Storytelling skill by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
