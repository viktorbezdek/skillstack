# Kano Model — Deep Dive

The Kano model categorizes product features by customer reaction, revealing which features drive satisfaction and which merely prevent dissatisfaction. It is the filter that prevents teams from over-investing in polish while basics are broken.

## The five categories

Kano's original taxonomy has five categories. Three are primary for product decisions:

### 1. Basic (Must-have, threshold)

**Present**: no pleasure — the customer expected it.
**Absent**: strong dissatisfaction, churn, or refusal to use.

Examples:
- Login works reliably.
- The app does not lose your data.
- Core search returns results.

Implication: **underinvesting in basics is lethal.** No amount of delighters compensates for missing basics. A team that ships a delighter while a basic is broken will see retention drop.

### 2. Performance (Linear, one-dimensional)

**Present**: satisfaction scales with quality.
**Absent**: dissatisfaction if weak; strong satisfaction if strong.

Examples:
- Upload speed.
- Search relevance.
- Load time.
- Battery life.

Implication: **diminishing returns above a threshold.** Going from 2-second load to 1-second load delights users. Going from 0.5 to 0.3 seconds is invisible to most. Invest until you reach "good enough"; further investment is wasted unless competitors are making the dimension a differentiator.

### 3. Delighter (Attractive, excitement)

**Present**: joy, word of mouth, brand loyalty.
**Absent**: no dissatisfaction — the customer did not expect it.

Examples (today):
- Auto-summary of a meeting.
- AI-generated first draft.
- One-click integration with a third-party tool.

Implication: **asymmetric payoff.** Delighters cost less to add than basics and produce disproportionate retention / referral effects. But only after basics are solid.

### 4. Indifferent

Customer doesn't care either way. Often features teams build for internal reasons.

Examples:
- Admin-only configuration nobody uses.
- A setting that has one correct value and shouldn't be surfaced.

Implication: **cut from scope.** If the feature moves neither satisfaction axis, it's cost without return.

### 5. Reverse

Customer actively prefers this feature to be absent.

Examples:
- Intrusive tracking with no user benefit.
- Dark patterns in cancellation flows.

Implication: **not on the roadmap unless forced.** Measure the cost to the relationship, not just the short-term metric it drives.

## The category decay problem

The most important Kano insight: **features move categories over time.**

```
Delighter → Performance → Basic
(year 1)    (year 3)      (year 5)
```

Examples of decay:

- Auto-save was a delighter in 2010, a performance attribute by 2015, a basic by 2020.
- One-click checkout was a delighter at Amazon's launch, now a basic in any ecommerce.
- Dark mode was a delighter in 2018, now a basic in consumer apps.

Implications:
- **Today's delighter is tomorrow's basic.** A product that stops shipping delighters eventually has only basics and performance attributes — parity with competitors, no differentiation.
- **Revisit categorization quarterly.** A feature categorized as a delighter two years ago may now be a basic.
- **Basics grow.** The set of must-have capabilities keeps expanding as the category matures.

## Kano survey method

To categorize a feature empirically, ask two questions for each:

**Functional** (if the feature is present): How would you feel?
**Dysfunctional** (if the feature is absent): How would you feel?

Answer options:
- I like it
- I expect it
- I am neutral
- I can live with it
- I dislike it

Map the two answers to a category using the Kano matrix:

| Functional ↓ / Dysfunctional → | Like | Expect | Neutral | Live with | Dislike |
|---|---|---|---|---|---|
| **Like** | Questionable | Delighter | Delighter | Delighter | Performance |
| **Expect** | Reverse | Indifferent | Indifferent | Indifferent | Basic |
| **Neutral** | Reverse | Indifferent | Indifferent | Indifferent | Basic |
| **Live with** | Reverse | Indifferent | Indifferent | Indifferent | Basic |
| **Dislike** | Reverse | Reverse | Reverse | Reverse | Questionable |

Sample size: at least 30 per segment for reliable categorization. Smaller samples produce noise.

## Using Kano in practice

### Before build

1. List candidate features.
2. Classify each provisionally (team opinion or survey).
3. Check portfolio balance:
   - Enough basics to avoid churn.
   - Enough performance to stay competitive.
   - At least one delighter per release to build differentiation.
4. Re-sequence the roadmap: basics that are weak before delighters; delighters before further performance optimization.

### During prioritization

Kano is a filter on RICE / MoSCoW. A high-RICE delighter is worth more than an equally-high-RICE performance attribute past the "good enough" line. A missing basic outranks every delighter.

### After launch

Track the category. A delighter that fails to produce satisfaction may have been miscategorized or may already be decaying. A performance attribute that unexpectedly drives retention may have crossed into delighter territory.

## Common mistakes

- **Everything is a delighter** — team classifies every roadmap item as a delighter because it's exciting. In reality, the portfolio is mostly performance with a few basics.
- **Basics are assumed, not validated** — team ships a "delighter" while login is flaky. Always audit basics first.
- **Static categorization** — categorization is treated as permanent. Features decay; revisit.
- **Single-segment categorization** — a feature that is a delighter for power users may be indifferent for new users. Categorize per segment.
- **Kano instead of JTBD** — Kano is a categorization tool, not a discovery tool. Use JTBD to find the right features; use Kano to categorize and sequence them.

## Integration with the VPC

Kano categorization applies to pain relievers and gain creators on the value map. A gain creator that is a delighter is a strong differentiator; a gain creator that is merely a basic is table stakes. When compressing to the value proposition statement, lead with delighters; baseline on basics; cite performance attributes only when quantifiably better than the alternative.
