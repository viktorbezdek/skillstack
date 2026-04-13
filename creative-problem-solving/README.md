> **v1.0.15** | Strategic Thinking | 16 iterations

# Creative Problem Solving

> Break through mental blocks and find high-leverage solutions using lateral thinking, first principles reasoning, game theory, and strategic reframing.

## The Problem

When teams face complex problems, they converge too fast. Someone proposes the obvious solution in the first five minutes, the room nods, and implementation begins -- only to discover weeks later that they were solving the wrong problem, or that a far simpler approach existed if they had questioned the assumptions. The cost is not just the wasted engineering time but the opportunity cost of the better solution they never considered.

This happens because the standard approach to problem-solving is linear: understand the problem as stated, brainstorm solutions within existing constraints, pick the most familiar one, and execute. No one challenges whether the constraints are real or assumed. No one reframes the problem from a different stakeholder's perspective. No one asks what would make the problem disappear entirely rather than what would address the symptoms. And no one applies structured analytical frameworks like game theory or expected value calculations to evaluate whether the chosen solution is actually optimal or just comfortable.

The result is systematic mediocrity. Teams pick safe, conventional solutions that feel productive but miss the high-leverage opportunities that come from questioning the problem itself. They build elaborate solutions to problems that could be eliminated. They optimize local metrics while ignoring systemic dynamics. And when they do need genuinely creative solutions -- competing against a larger opponent, breaking into a new market, resolving a deadlock between stakeholders -- they have no structured process for generating or evaluating unconventional ideas.

## The Solution

This plugin provides a five-step creative problem-solving methodology backed by five reference libraries covering lateral thinking, strategic frameworks, reframing techniques, ideation methods, and decision-making tools. Instead of jumping from problem to solution, it walks you through deep understanding (extracting the real problem from the stated problem), strategic reframing (viewing from multiple angles before solving), broad generation (exploring the full solution space), rigorous analysis (applying game theory, probabilistic reasoning, and system dynamics), and optimal recommendation (synthesized, actionable, with escape routes).

Each step draws on specific techniques. The generation phase uses lateral thinking (random entry, provocation, assumption escape), SCAMPER (Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse), and cross-domain transfer. The analysis phase applies game theory (Nash equilibrium, incentive alignment, backward induction), first principles reasoning (fundamental truths over conventions), and systems thinking (feedback loops, leverage points, second-order effects). The decision phase uses expected value calculations, Pareto optimization, real options analysis, and the reversibility test.

The result is not just more creative solutions but better-analyzed ones. You get unconventional ideas with rigorous evaluation, not brainstorming hand-waves.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Converge on the obvious solution in five minutes without questioning assumptions | Systematically challenge every assumption and identify which constraints are real vs assumed |
| Solve the stated problem without asking whether it is the right problem | Strategic reframing reveals the underlying goal, often leading to simpler or more impactful solutions |
| Brainstorm within existing mental models, producing familiar variations | Lateral thinking, SCAMPER, and cross-domain transfer generate genuinely novel options |
| Pick solutions based on comfort and familiarity | Game theory, expected value, and decision frameworks evaluate options rigorously |
| Miss systemic dynamics and second-order effects | Systems thinking identifies feedback loops, leverage points, and unintended consequences |
| No structured process when creative thinking is actually needed | Five-step methodology with reference libraries for each phase |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install creative-problem-solving@skillstack
```

### Verify installation

After installing, test with:

```
Help me think outside the box about our user onboarding -- we've been iterating on the same flow for months and conversion hasn't improved
```

## Quick Start

1. Install the plugin using the commands above
2. Describe a problem you are stuck on: `We need to reduce our CI pipeline from 45 minutes to under 10 but we've already optimized every step`
3. The skill challenges your assumptions (do you need to run everything sequentially? is every step necessary?) and reframes the problem (what if the goal is not a faster pipeline but faster feedback?)
4. It generates solutions across multiple domains: parallelization, speculative execution, incremental testing, test impact analysis, or eliminating the need for some tests entirely
5. Each solution is evaluated with expected impact, implementation cost, reversibility, and risk

## What's Inside

| Component | Description |
|---|---|
| `creative-problem-solving` skill | Core skill with the five-step methodology: deep understanding, strategic reframing, solution generation, solution analysis, and decision/recommendation |
| 5 reference libraries | Lateral thinking, strategic frameworks, reframing techniques, ideation techniques, and decision-making frameworks |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests creative generation, strategic analysis, and recommendation quality |

### creative-problem-solving

**What it does:** Activates when you need creative solutions, unconventional approaches, strategic analysis, or help breaking through mental blocks. Walks you through a structured process from problem understanding through reframing, generation, analysis, and recommendation -- applying lateral thinking, game theory, first principles, and systems thinking as appropriate to your specific problem.

**Try these prompts:**

```
Help me think outside the box -- we need to compete with a company that has 10x our engineering team and budget
```

```
I'm stuck on a technical architecture decision between microservices and a modular monolith -- apply first principles to help me see past the hype
```

```
Use game theory to analyze our pricing strategy -- we're in a market with two dominant competitors and we keep getting into price wars
```

```
Reframe this problem for me: our support team is overwhelmed with tickets and we can't hire fast enough to keep up
```

```
I need creative solutions for reducing our cloud costs by 40% without degrading performance -- we've already done the obvious optimizations
```

**Key references:**

| Reference | Topic |
|---|---|
| `lateral-thinking.md` | Random entry, provocation, challenge assumptions, concept fan, movement techniques |
| `strategic-frameworks.md` | Game theory analysis, first principles reasoning, systems thinking, constraint analysis |
| `reframing-techniques.md` | Meta-level shifts, perspective rotation, context changes, constraint manipulation |
| `ideation-techniques.md` | SCAMPER, morphological analysis, analogical thinking, TRIZ innovation principles |
| `decision-frameworks.md` | Multi-criteria analysis, optimization methods, risk analysis, bias mitigation |

## Real-World Walkthrough

You are the tech lead at a mid-stage startup. Your team has been trying to reduce page load time from 4.2 seconds to under 2 seconds for three months. You have already optimized images, added lazy loading, implemented code splitting, and moved to a CDN. The load time dropped to 3.1 seconds but has plateaued. The CEO is pushing hard because conversion drops 7% for every additional second of load time.

You open Claude Code feeling stuck:

```
We've been trying to get our page load time under 2 seconds for months. We've already done image optimization, lazy loading, code splitting, and CDN. We're at 3.1 seconds and stuck. The CEO wants 2 seconds. I need creative solutions because the obvious ones are exhausted.
```

The creative-problem-solving skill activates and starts with deep understanding. Before generating solutions, it challenges your framing:

**What is the real problem?** You stated "reduce load time to under 2 seconds." But the underlying goal is conversion improvement. The CEO cares about load time because of its impact on conversion, not as a metric in itself.

**Challenge assumptions:** The skill asks you to list what you assume is true. You say: "We need to make the page load faster." It identifies this as a constraining assumption. What if the goal is not faster loading but the perception of faster loading? What if meaningful content appears in 1.5 seconds even though full page load takes 3.1 seconds?

This reframe opens new solution territory. The skill generates ideas across three categories:

**Perception-based solutions** (from the reframe): Progressive rendering to show above-the-fold content in under 1 second. Skeleton screens that give the impression of instant loading. Optimistic UI updates that show expected content before data arrives. These do not change actual load time but change the user's experience of it.

**Elimination-based solutions** (from first principles): What is loading that does not need to load? The skill walks through analyzing your page: analytics scripts, A/B testing frameworks, chat widgets, social proof notifications. These add 800ms of load time but are invisible to the user for the first 10 seconds. Deferring them entirely changes nothing about the user experience but drops your perceived load time to 2.3 seconds.

**Inversion-based solutions** (from lateral thinking): Instead of making the page load faster, make less page load. The skill asks what percentage of visitors actually scroll below the fold on their first visit. Your analytics show 23%. So 77% of visitors see only the top of the page. A radically different architecture loads only the visible viewport initially, then loads the rest on scroll intent. This is different from lazy loading (which still loads the page structure) -- this is genuinely not loading 70% of the page for 77% of visitors.

**Game theory analysis:** The skill examines your competitive landscape. Your two main competitors load in 2.8 and 3.5 seconds. Getting to 2 seconds would be a differentiator. But getting perceived load time to under 1 second would be a dramatic differentiator -- and it is achievable through the perception-based solutions without the engineering effort of shaving another 1.1 seconds off actual load time.

**Expected value comparison:**
- Option A (keep optimizing actual load time): High engineering effort, uncertain outcome, 3-6 months. Expected improvement: 0.3-0.5 seconds.
- Option B (perception optimization): Low-medium effort, well-understood techniques, 2-4 weeks. Expected perceived improvement: 1.5-2.0 seconds.
- Option C (eliminate unnecessary loading): Low effort, immediate. Expected improvement: 0.5-0.8 seconds.

The skill recommends combining Options B and C first (4 weeks, low risk, high impact) and measuring the conversion effect before investing in further actual load time optimization. The reversibility test confirms both options are two-way doors -- easy to roll back if they do not improve conversion.

You implement the combined approach. Above-the-fold content renders in 0.9 seconds with skeleton screens. Deferred scripts save 0.8 seconds. The full page still loads in 2.3 seconds but users perceive sub-second performance. Conversion improves 12% -- exceeding what the 2-second target would have delivered.

The CEO is happy. And your team learned that the problem was never "make the page load in 2 seconds" -- it was "make users feel like the page loads instantly."

## Usage Scenarios

### Scenario 1: Competing with a larger, better-funded competitor

**Context:** You run a 15-person startup competing against a 500-person company with 20x your budget. They can outspend you on features, marketing, and engineering. You need a strategy that does not require matching their resources.

**You say:** `How can we compete with a competitor that has 20x our engineering budget? We can't match them feature for feature.`

**The skill provides:**
- Reframe: from "how to match resources" to "how to win differently"
- Game theory analysis: where are they committed and unable to pivot? What can a small team do that a large one cannot?
- First principles: what do customers value that scale actively prevents (speed, personal attention, willingness to customize)?
- Strategic options: niche domination, speed of iteration, relationship depth, constraint-based innovation

**You end up with:** An asymmetric competitive strategy that exploits your advantages rather than trying to overcome your disadvantages.

### Scenario 2: Breaking a technical deadlock

**Context:** Your team has been debating microservices vs monolith for weeks. Both sides have valid arguments. No consensus is forming and the debate is blocking progress.

**You say:** `We're deadlocked on microservices vs monolith -- the debate has been going on for weeks and both sides have good points. Help me break through this.`

**The skill provides:**
- Challenge assumptions: does the choice have to be binary? Is this a one-way door?
- First principles: what is the actual problem -- deployment independence, team autonomy, scaling, or something else?
- Reversibility test: which choice is easier to reverse? Start with the more reversible option.
- Second-order effects: what organizational changes does each choice force?

**You end up with:** A reframed decision that dissolves the deadlock -- often by revealing that the real question is not architectural but organizational.

### Scenario 3: Finding cost savings beyond the obvious

**Context:** You have been asked to cut cloud costs by 40% but your team has already implemented reserved instances, right-sized VMs, and shut down unused resources. The obvious optimizations are done.

**You say:** `I need to cut another 40% from our cloud bill and we've already done the obvious stuff -- reserved instances, right-sizing, cleanup. I need creative ideas.`

**The skill provides:**
- Inversion: what if the workload did not need to run on cloud at all? (dedicated hardware for stable base load)
- Cross-domain transfer: how do fintech companies handle compute-heavy intermittent workloads? (spot instances with checkpointing)
- Systems thinking: which cost drivers create feedback loops? (more data stored = more compute to process = more data generated)
- SCAMPER: Eliminate (which services produce no value?), Combine (can multiple low-usage services share infrastructure?), Reverse (prepay for lower unit costs)

**You end up with:** A portfolio of non-obvious cost reduction strategies, each evaluated for expected savings, implementation effort, and risk.

### Scenario 4: Resolving stakeholder misalignment

**Context:** Product wants to ship a feature fast, engineering wants to build it properly, design wants to nail the UX, and leadership wants to hit a quarterly target. Everyone has different success criteria and the project is stalled.

**You say:** `Product, engineering, design, and leadership all want different things from this project -- how do I align them without someone losing?`

**The skill provides:**
- Game theory: map each stakeholder's incentives and identify where they naturally align vs conflict
- Perspective rotation: view the project from each stakeholder's success criteria
- Positive-sum analysis: identify solutions that partially satisfy all parties rather than fully satisfying one
- Second-order effects: what happens to each stakeholder's relationship if they "win" vs if they compromise?

**You end up with:** A phased approach that sequences deliverables to hit the quarterly target (leadership), with proper UX for the first phase (design), clean architecture for extensibility (engineering), and a fast initial launch (product).

## Ideal For

- **Tech leads and architects** facing decisions where the obvious answer feels wrong but alternatives are unclear
- **Founders and product leaders** who need competitive strategies that do not require matching larger competitors' resources
- **Anyone stuck on a problem** for more than a week where incremental optimization has stopped producing results
- **Strategic planners** who need to analyze multi-party dynamics, incentive structures, and second-order effects
- **Teams in deadlock** where multiple valid perspectives have created an impasse that linear discussion cannot resolve

## Not For

- **Analyzing or critiquing existing ideas** with bias detection and evidence evaluation -- use [critical-intuition](../critical-intuition/) instead
- **Systematic risk assessment** with probability matrices and mitigation planning -- use [risk-management](../risk-management/) instead
- **Prioritizing a backlog** or deciding what to build next -- use [prioritization](../prioritization/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with five reference libraries providing deep technique coverage.

The **core skill** (`SKILL.md`) defines the five-step methodology: deep understanding (extract the real problem, challenge assumptions, classify the problem type), strategic reframing (abstraction shifts, perspective rotation, constraint manipulation, inversion), solution generation (lateral thinking, SCAMPER, cross-domain transfer, game theory, first principles, systems thinking), solution analysis (probabilistic assessment, game theory validation, system dynamics), and decision/recommendation (expected value, Pareto optimization, real options, reversibility test).

The five **reference libraries** provide technique depth on demand:
- **Lateral thinking** -- random entry, provocation, assumption challenge, concept fan, and movement techniques for breaking mental blocks
- **Strategic frameworks** -- game theory analysis (Nash equilibrium, incentive alignment, backward induction), first principles reasoning, systems thinking (feedback loops, leverage points), and constraint analysis
- **Reframing techniques** -- meta-level shifts, perspective rotation, context changes, and constraint manipulation for viewing problems from new angles
- **Ideation techniques** -- SCAMPER methodology, morphological analysis, analogical thinking, and TRIZ innovation principles for systematic idea generation
- **Decision frameworks** -- multi-criteria analysis, optimization methods, risk analysis, and cognitive bias mitigation for rigorous solution evaluation

The skill explicitly routes to critical-intuition when the user needs analysis or critique of existing ideas rather than generation of new ones.

## Related Plugins

- **[Critical Intuition](../critical-intuition/)** -- Analyze and critique existing ideas through pattern recognition, bias detection, and evidence evaluation
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, ICE, and effort-impact matrices for decision-making on what to build
- **[Risk Management](../risk-management/)** -- Systematic risk assessment with probability matrices, mitigation strategies, and monitoring
- **[Systems Thinking](../systems-thinking/)** -- Analyze complex problems through feedback loops, leverage points, and system dynamics

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
