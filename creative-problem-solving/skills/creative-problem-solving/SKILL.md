---
name: creative-problem-solving
description: Generate new ideas and breakthrough solutions using brainstorming, lateral thinking, SCAMPER, first principles reasoning, game theory, and strategic reframing. Use when the user asks to brainstorm, ideate, "think outside the box", generate alternatives, explore creative solutions, reframe a problem, or come up with ideas — especially when stuck in conventional thinking. NOT for stress-testing or finding flaws in existing ideas (use critical-intuition), NOT for making a final decision between options (use strategic-decision or prioritization), NOT for detecting bias or evaluating evidence quality (use critical-intuition).
---

# Creative Problem-Solving

Generate breakthrough solutions using structured creativity techniques matched to problem type. Forward-looking, divergent thinking — complements critical-intuition (backward-looking, convergent).

## When to Use / Not Use

**Use when:**
- Conventional approaches have failed and you need fresh thinking
- Breaking through mental blocks on a project
- Strategic decisions involving competitors, stakeholders, or incentive dynamics
- First-principles analysis of whether the problem itself is the right one to solve
- Generating diverse alternatives with trade-offs

**Do NOT use when:**
- Analyzing or critiquing existing ideas -> use `critical-intuition`
- Detecting bias in evidence or proposals -> use `critical-intuition`
- Making a final decision between known options -> use `prioritization`
- Pattern recognition in data -> use `critical-intuition`

## Decision Tree

```
What type of problem are you solving?
├── Stuck in conventional thinking / mental block
│   └── Lateral Thinking -> random entry, provocation, escape assumptions
├── Need systematic exploration of solution space
│   └── SCAMPER + Morphological Analysis -> structured ideation
├── Strategic or competitive problem
│   ├── Incentives/misaligned actors -> Game Theory -> Nash equilibrium, incentive alignment
│   └── Fundamental constraints -> First Principles -> question everything assumed
├── Organizational/team dynamics
│   └── Systems Thinking -> feedback loops, leverage points, second-order effects
├── Choosing between generated options
│   └── Decision Frameworks -> expected value, Pareto optimization, reversibility test
└── Need to evaluate existing ideas, not generate new ones?
    └── Use critical-intuition instead
```

## Five-Step Process

### Step 1: Deep Understanding

Extract the real problem beneath the stated one:
- What is the stated problem vs. the underlying goal?
- What constraints are real vs. assumed (ghost constraints)?
- Who are the stakeholders and what do they want?
- What happens if we do nothing?

Challenge assumptions explicitly. List all implicit assumptions and question which can be removed.

### Step 2: Strategic Reframing

View the problem through multiple lenses before solving:
- **Abstraction shifts**: Chunk up (broader purpose), down (specific components), sideways (analogies)
- **Perspective rotation**: Different stakeholders, time horizons, scales
- **Constraint manipulation**: What if fixed constraints were variable?
- **Inversion**: How would we guarantee failure? What would make this worse?

For techniques, read `references/reframing-techniques.md`.

### Step 3: Solution Generation

Generate diverse solutions using matched creativity techniques:

| Problem Type | Technique | Reference |
|---|---|---|
| Mental blocks | Random entry, provocation, escape assumptions | `references/lateral-thinking.md` |
| Systematic exploration | SCAMPER, morphological analysis, cross-domain transfer | `references/ideation-techniques.md` |
| Strategic innovation | Game theory, first principles, systems thinking | `references/strategic-frameworks.md` |

### Step 4: Solution Analysis

Evaluate generated solutions with strategic frameworks:

- **Probabilistic**: Expected value, base rates, Bayesian updating, tail risk
- **Game theory**: Nash equilibrium, incentive alignment, strategic commitment, backwards induction
- **System dynamics**: Feedback loops, leverage points, second-order effects, time delays

For frameworks, read `references/strategic-frameworks.md`.

### Step 5: Decision & Recommendation

Synthesize into actionable recommendations:
1. Primary recommendation with reasoning
2. Key advantages (why this is superior)
3. Critical risks (what could go wrong)
4. Mitigation strategies
5. Decision criteria (when to choose alternatives)
6. First concrete implementation steps

Apply decision frameworks: expected value for uncertainty, Pareto for trade-offs, real options for flexibility, reversibility test for one-way vs. two-way doors.

For frameworks, read `references/decision-frameworks.md`.

## Technique Selection Guide

| Signal | Use Technique | Why |
|--------|--------------|-----|
| "We've tried everything" | Lateral thinking + inversion | Break the pattern by forcing random connections |
| "We need more options" | SCAMPER + morphological analysis | Systematically explore combinations |
| "Competitors react to our moves" | Game theory | Map incentives and equilibrium outcomes |
| "Why do we even do it this way?" | First principles | Strip to fundamentals and rebuild |
| "Teams are blocking each other" | Systems thinking + game theory | Find incentive misalignment and leverage points |
| "What's the best approach?" | Expected value + reversibility test | Quantify trade-offs and identify safe-to-reverse options |

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Skipping Step 1 (deep understanding) | Solutions address stated problem, not real need | Always extract: "What is the underlying goal?" and "What happens if we do nothing?" |
| Jumping to a single "best" answer | Short-circuits divergent exploration; misses high-leverage unconventional options | Generate 5-10 alternatives before converging; ask for approaches with trade-offs, not "the answer" |
| Not sharing what has already been tried | Skill regenerates solutions already rejected | Provide prior approaches and why each failed in your prompt |
| Critiquing instead of generating | Asking "critique this plan" triggers analysis, not ideation | Use this skill for generating alternatives; use critical-intuition for critique |
| Abstraction without grounding | Game theory analysis too abstract to map to concrete actions | Name specific actors, specific moves, specific payoffs; ground in real people and teams |
| Skipping feasibility assessment | Generated ideas are inspiring but have no implementation path | Never skip Step 4 (analysis) and Step 5 (recommendation); every idea needs feasibility check |
| Assuming constraints are real | Ghost constraints narrow solution space invisibly | Explicitly label each constraint as "verified" or "assumption" and challenge assumptions |
| Creative thinking without rigor | Unconventional ideas fail in real-world strategic complexity | Always pair generation (this skill) with analysis (game theory, Bayesian reasoning, systems thinking) |

## Input Requirements

What to include in your prompt for best results:

| Input | Why It Matters |
|-------|---------------|
| What you have already tried + why each failed | Prevents regenerating rejected solutions |
| Real constraint vs. assumed constraint | Identifies ghost constraints to challenge |
| Who the relevant actors are | Game theory needs named players with real incentives |
| Your resources and advantages | Asymmetric strategy depends on knowing your strengths |
| What "success" looks like | Enables expected value calculation and decision criteria |

**Template prompt:**
```
We have been trying to [solve problem] for [duration]. Approaches we've tried: [list each with why it failed]. The constraint we're working within: [describe, noting which are assumptions]. Our resources/advantages: [list]. Stakeholders involved: [who has influence]. Help me find approaches outside our current thinking.
```

## Integration

- critical-intuition — Analytical counterpart: critique what this skill generates
- systems-thinking — Deeper systems dynamics for complex adaptive problems
- prioritization — RICE, MoSCoW, ICE scoring for ranking generated solutions
- risk-management — Systematic risk assessment for riskier creative solutions
- outcome-orientation — Define measurable success criteria using OKRs

## References

- `references/lateral-thinking.md` — Random entry, provocation, escape assumptions, concept fan
- `references/strategic-frameworks.md` — Game theory, first principles, systems thinking
- `references/reframing-techniques.md` — Abstraction shifts, perspective rotation, constraint manipulation
- `references/ideation-techniques.md` — SCAMPER, morphological analysis, TRIZ principles
- `references/decision-frameworks.md` — Multi-criteria analysis, expected value, bias mitigation
