> **v1.0.15** | Strategic Thinking | 16 iterations

# Creative Problem Solving

Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, SCAMPER, and strategic reframing -- for problems where conventional analysis reinforces the constraints instead of questioning them.

## What Problem Does This Solve

Most problem-solving stalls because people attack the stated problem directly, constrained by invisible assumptions about what is fixed, what is possible, and what the goal actually is. A team asked "how do we make the system faster?" never considers whether speed is actually the problem (maybe perceived speed is, and async processing solves it). Conventional analysis reinforces those constraints rather than questioning them. This skill applies a structured five-phase process -- deep understanding, strategic reframing, broad generation, rigorous analysis, and optimal recommendation -- to break through mental blocks and find high-leverage solutions that direct approaches miss.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install creative-problem-solving@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a single-skill plugin with five reference documents:

| Component | Description |
|---|---|
| `skills/creative-problem-solving/SKILL.md` | Core skill covering the five-phase process (deep understanding, strategic reframing, solution generation, rigorous analysis, optimal recommendation), problem type identification, assumption challenging, and three worked examples (competitive strategy, technical performance, organizational collaboration) |
| `references/lateral-thinking.md` | Random entry, provocation statements, assumption escape, concept fan, and movement techniques for breaking mental blocks |
| `references/strategic-frameworks.md` | Game theory (Nash equilibrium, incentive alignment, backwards induction), first principles thinking, systems thinking (feedback loops, leverage points), and constraints analysis |
| `references/reframing-techniques.md` | Meta-level shifts (chunk up/down/sideways), perspective rotation, context changes, and constraint manipulation (what if fixed constraints were variable?) |
| `references/ideation-techniques.md` | SCAMPER (Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse), morphological analysis, analogical thinking, and TRIZ principles |
| `references/decision-frameworks.md` | Multi-criteria analysis, Pareto optimization, expected value calculation, real options for flexibility value, reversibility test (one-way vs. two-way doors), and bias mitigation |

## Usage Scenarios

**1. Competing against a larger, better-resourced competitor**

Instead of asking "how do we match their resources," reframe to "how do we win differently." Apply game theory to map where competitors are committed and what they cannot do because of their size. Use first principles to decompose what customers actually value. Generate asymmetric strategy options: niche domination, speed/agility advantage, relationship depth, or constraint-based innovation.

**2. System performance problem with no obvious bottleneck**

The stated problem is "make it faster." Challenge the assumption: must you make it faster, or can you change the perception of speed? Chunk up: what is the real goal -- user satisfaction, throughput, or cost reduction? First principles: what are the theoretical limits and where is the actual bottleneck? Alternative reframes: make slow parts async, reduce the need for the operation entirely, cache, or precompute. Apply a decision framework with cost-benefit, reversibility, and time-to-value for each approach.

**3. Teams not collaborating across organizational boundaries**

Apply systems thinking: is poor collaboration a symptom or the root cause? What incentive structures exist? Use game theory: are individual and collective incentives misaligned (prisoner's dilemma)? Reframe from each team's perspective: what does each team's optimal strategy look like, and why would they not collaborate? Identify leverage points: change information flows, adjust metrics that reward local optimization, restructure shared accountability. Analyze second-order effects of proposed changes.

**4. Brainstorming creative solutions for a product pivot**

Use the SCAMPER framework systematically: what can you Substitute (different technology, market, delivery model)? Combine (merge two offerings)? Adapt (what works in an adjacent industry)? Modify (scale up or down)? Put to other use (same technology, different market)? Eliminate (what would the product look like with 80% fewer features)? Reverse (invert the value chain)? Cross-reference with analogical thinking from other domains that solved similar structural problems.

**5. Making a high-stakes decision under uncertainty**

Apply probabilistic assessment: estimate expected value (probability times outcome) for each option. Use Bayesian updating with available evidence. Analyze tail risks (low probability, high impact). Apply the reversibility test: one-way doors deserve more analysis, two-way doors favor speed. Use Nash equilibrium analysis if the decision involves strategic interactions with other parties. Provide explicit decision criteria for when to choose each alternative.

## How to Use

**Direct invocation:**

```
Use the creative-problem-solving skill to find unconventional approaches for our market entry strategy
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `problem-solving`
- `lateral-thinking`
- `game-theory`

## When to Use / When NOT to Use

**Use when:**
- You need creative, unconventional solutions
- Conventional approaches have stalled or all obvious options have problems
- Strategic decisions under uncertainty
- Reframing the problem itself may be more valuable than solving it as stated
- Game theory analysis of competitive or organizational dynamics

**Do NOT use when:**
- Analyzing or critiquing existing ideas, detecting bias, or recognizing patterns in evidence -- use [critical-intuition](../critical-intuition/) instead

## Related Plugins

- **[Critical Intuition](../critical-intuition/)** -- Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with Bayesian reasoning and red flag detection
- **[Outcome Orientation](../outcome-orientation/)** -- Focus on measurable outcomes using OKRs, results-driven thinking, and the outcome vs. output distinction
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making
- **[Risk Management](../risk-management/)** -- Risk assessment frameworks, mitigation strategies, risk registers, and monitoring
- **[Systems Thinking](../systems-thinking/)** -- Feedback loops, leverage points, and system dynamics for analyzing complex problems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
