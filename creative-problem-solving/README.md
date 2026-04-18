> **v1.0.16** | Strategic Thinking | 16 iterations

# Creative Problem Solving

> Break through mental blocks and find high-leverage solutions using lateral thinking, first principles reasoning, game theory, SCAMPER, and strategic reframing -- when conventional approaches have failed or the problem demands unconventional thinking.
> Single skill + 5 reference documents | 13 trigger evals, 3 output evals

## The Problem

Most problem-solving follows a narrow pattern: identify the problem, brainstorm variations of familiar solutions, pick the least bad option. This works for routine problems. For complex, ambiguous, or stuck problems -- where the obvious approaches have already failed or the solution space is much larger than what conventional thinking explores -- this pattern produces mediocre results. Teams waste weeks iterating on variations of the same failing approach instead of stepping back to see the problem differently.

The deeper failure is invisible constraints. Every problem comes wrapped in assumptions that limit the solution space: "we have to use this technology," "the budget is fixed," "customers want feature X." Some of these constraints are real. Many are ghost constraints -- legacy assumptions baked into the current approach that no longer apply. Without a systematic way to surface and challenge assumptions, teams optimize within an artificially narrow space and miss the high-leverage solutions outside it.

Strategic thinking compounds the problem. Most teams solve problems in isolation when the real dynamics are interactive -- competitors react, stakeholders have misaligned incentives, second-order effects create feedback loops. Without frameworks like game theory, systems thinking, and probabilistic reasoning, solutions that look optimal in isolation fail when they encounter the real world's strategic complexity.

## The Solution

This plugin provides a five-step creative problem-solving process backed by five comprehensive reference documents covering lateral thinking, strategic frameworks, reframing techniques, ideation techniques, and decision frameworks. The process moves from deep understanding (extracting the real problem beneath the stated one) through strategic reframing (viewing from multiple angles), solution generation (using specific creativity techniques matched to the problem type), rigorous analysis (game theory, Bayesian reasoning, systems dynamics), to optimal recommendation (with decision criteria and implementation steps).

The skill selects techniques based on problem type: lateral thinking for mental blocks, SCAMPER and morphological analysis for systematic exploration, game theory and first principles for strategic innovation, and multi-criteria analysis for decision-making under uncertainty. It challenges assumptions explicitly, identifies hidden constraints, and grounds recommendations in probabilistic reasoning rather than gut feel.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Brainstorm variations of familiar solutions; miss unconventional high-leverage options | Systematic lateral thinking and SCAMPER explore a much wider solution space across domains |
| Hidden assumptions narrow the solution space invisibly | Explicit assumption challenging surfaces ghost constraints and opens new options |
| Solutions analyzed in isolation; fail when competitors or stakeholders react | Game theory maps incentives, Nash equilibria, and strategic interactions before committing |
| Decisions based on "best case" thinking without probabilistic grounding | Bayesian reasoning, expected value calculation, and tail risk analysis ground every recommendation |
| Problem taken at face value without questioning whether it is the right problem | Strategic reframing at multiple levels (abstraction shifts, perspective rotation, constraint manipulation, inversion) |
| Second-order effects and feedback loops discovered only after implementation | Systems thinking identifies reinforcing loops, balancing loops, and leverage points during analysis |

## Context to Provide

Creative problem-solving needs to know what has already been tried before it can find what has not been tried. Without that context, it risks regenerating solutions you have already rejected. The more specifically you describe the stuck state, the more precisely the skill can target unconventional alternatives.

**What to include in your prompt:**
- **What you have already tried** and specifically why each approach failed -- this is the single most important input; it prevents the skill from regenerating rejected solutions
- **The real constraint** vs. the assumed constraint -- state which constraints are hard (budget, timeline, physical limits) and which you are not sure about
- **Who the relevant actors are** (competitors, stakeholders, customers, internal teams) -- game theory analysis requires named players with real incentives
- **The resources and advantages you have** -- asymmetric strategy depends on knowing what you have that the competitor or situation lacks
- **What "success" looks like** -- helps with expected value calculation and decision criteria

**What makes results better:**
- Describing the problem history ("we've been trying this for 3 months, here's why each approach failed")
- Being explicit about which constraints are assumptions vs. verified requirements ("we assume we need X because Y, but we're not sure")
- Naming the specific people or teams involved in organizational problems -- game theory works with real actors
- Stating scale and resource context (10-person team, $50K budget, 3-month deadline)

**What makes results worse:**
- Asking for "the answer" -- creative problem-solving generates diverse options with trade-offs, not a single verdict
- Asking to critique an existing plan -- use `critical-intuition` for evaluation; this skill generates alternatives
- Providing no context about what has already failed -- the skill will explore the same solution space your team already explored

**Template prompt:**
```
We have been trying to [solve problem] for [duration]. Approaches we've tried: [list each with why it failed]. The constraint we're working within: [describe, noting which constraints are assumptions]. Our resources/advantages: [list]. Stakeholders involved: [who has influence or incentives that matter]. Help me find approaches outside our current thinking.
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install creative-problem-solving@skillstack
```

### Prerequisites

No additional dependencies. Pairs powerfully with `critical-intuition` (analyzing and critiquing the solutions this skill generates), `systems-thinking` (deeper systems dynamics), and `prioritization` (ranking generated solutions).

### Verify installation

After installing, test with:

```
We've been trying to reduce customer churn for 6 months. Nothing is working. Help me think about this problem differently.
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"We're stuck on how to compete with a larger competitor. What are unconventional approaches we haven't considered?"`
3. The skill activates and walks you through assumption challenging, strategic reframing, and game theory analysis
4. Follow up with: `"What's the expected value of the top 3 approaches? What are the tail risks?"`
5. The skill provides probabilistic assessment with decision criteria for choosing between options

---

## System Overview

```
creative-problem-solving (plugin)
└── creative-problem-solving (skill)
    ├── 5-step process
    │   ├── Step 1: Deep Understanding (extract real problem)
    │   ├── Step 2: Strategic Reframing (multiple lenses)
    │   ├── Step 3: Solution Generation (creativity techniques)
    │   ├── Step 4: Solution Analysis (strategic frameworks)
    │   └── Step 5: Decision & Recommendation (optimal synthesis)
    └── references/
        ├── lateral-thinking.md (random entry, provocation, escape)
        ├── strategic-frameworks.md (game theory, first principles, systems thinking)
        ├── reframing-techniques.md (meta-level shifts, perspective rotation)
        ├── ideation-techniques.md (SCAMPER, morphological analysis, TRIZ)
        └── decision-frameworks.md (multi-criteria analysis, optimization, risk)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `creative-problem-solving` | Skill | Five-step process from problem understanding to optimal recommendation |
| `lateral-thinking.md` | Reference | Random entry, provocation, challenge assumptions, concept fan, movement |
| `strategic-frameworks.md` | Reference | Game theory (Nash equilibrium, incentives), first principles, systems thinking |
| `reframing-techniques.md` | Reference | Meta-level shifts, perspective rotation, context changes, constraint manipulation |
| `ideation-techniques.md` | Reference | SCAMPER, morphological analysis, analogical thinking, TRIZ principles |
| `decision-frameworks.md` | Reference | Multi-criteria analysis, weighted scoring, optimization, risk analysis, bias mitigation |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### creative-problem-solving (skill)

**What it does:** Activates when users need breakthrough solutions to complex or stuck problems. Follows a five-step process: understand the real problem, reframe strategically, generate diverse solutions using matched creativity techniques, analyze rigorously with strategic frameworks, and synthesize into optimal recommendations with probabilistic grounding.

**Input -> Output:** A problem description (stuck project, competitive challenge, resource constraint, organizational issue) -> Reframed problem statement, 5-10 unconventional solution approaches with strategic analysis, probabilistic assessment, and a primary recommendation with implementation steps.

**When to use:**
- Conventional approaches have failed and you need fresh thinking
- Complex problems requiring creative or out-of-the-box solutions
- Strategic decisions involving competitors, stakeholders, or incentive dynamics
- Breaking through mental blocks on a project or initiative
- First-principles analysis of whether the problem itself is the right one to solve

**When NOT to use:**
- Analyzing or critiquing existing ideas (use `critical-intuition`)
- Detecting bias in evidence or proposals (use `critical-intuition`)
- Pattern recognition in data or behavior (use `critical-intuition`)

**Try these prompts:**

```
We've been stuck for 3 months trying to reduce page load time below 2 seconds. We've tried CDN, lazy loading, image optimization, and moving to edge functions. Each got us closer but we're stuck at 2.4 seconds. The constraint is our monolithic backend that can't be decomposed without a 6-month rewrite. What are we missing?
```

```
Our startup has 5 engineers competing in the project management space against a company with 500 engineers and $50M in funding. We can't outbuild them on features. Our advantage is we can ship in days where they take months, and we can offer hands-on customer support. What's our asymmetric strategy?
```

```
We need to cut cloud costs by 40% without degrading user experience. We're on AWS, spending $80K/month, mostly on EC2 (60%) and RDS (30%). We've already done reserved instances. We assumed we need RDS for consistency, but our app is actually read-heavy (90% reads). Help me challenge this assumption from first principles.
```

```
Teams A and B both maintain our shared payment service. Team A owns the API layer, Team B owns the data model. They keep breaking each other's integrations because each team optimizes for their own quarterly metrics. Use game theory to map why this situation is stable and what incentive change would make cooperation the dominant strategy.
```

**Key references:**

| Reference | Topic |
|---|---|
| `lateral-thinking.md` | Random entry, provocation, escape assumptions, concept fan for breaking mental blocks |
| `strategic-frameworks.md` | Game theory, first principles, systems thinking, constraints analysis for strategic decisions |
| `reframing-techniques.md` | Abstraction shifts, perspective rotation, constraint manipulation, inversion for seeing problems differently |
| `ideation-techniques.md` | SCAMPER, morphological analysis, analogical thinking, TRIZ for systematic solution generation |
| `decision-frameworks.md` | Multi-criteria analysis, expected value, Pareto optimization, bias mitigation for choosing between options |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "Give me ideas" | "We've tried X, Y, and Z to reduce churn. None worked. What unconventional approaches are we missing?" |
| "Help me think" | "Use first principles to analyze whether we even need a database for this -- what are the fundamental requirements?" |
| "What should we do?" | "Two teams want different architectures. Use game theory to map the incentives and find a Nash equilibrium." |
| "Be creative" | "Apply SCAMPER to our onboarding flow. What happens if we eliminate the signup form entirely?" |

### Structured Prompt Templates

**For stuck problems:**
```
We've been trying to solve [problem] for [duration]. Approaches we've tried: [list]. They failed because [reasons]. Help me reframe this problem and find approaches outside our current thinking.
```

**For competitive strategy:**
```
We compete with [competitor type] who has [advantages]. Our strengths are [list]. What asymmetric strategies exploit their constraints?
```

**For first-principles analysis:**
```
We assume we need [thing] because [reason]. Challenge this assumption from first principles. What are the fundamental requirements, and what becomes possible if we remove [assumed constraint]?
```

### Prompt Anti-Patterns

- **Asking for analysis of existing ideas:** "Critique this proposal" is analysis, not generation. Use `critical-intuition` for critiquing and this skill for generating alternatives.
- **Requesting a single "best" answer:** Creative problem-solving generates diverse options with trade-offs. Asking for "the answer" short-circuits the process. Ask for "approaches with trade-offs."
- **Not sharing what has already been tried:** Without knowing what failed, the skill may regenerate solutions you already rejected. Always share prior approaches and why they did not work.

## Real-World Walkthrough

**Starting situation:** You lead engineering at a B2B SaaS company. Your largest customer (30% of revenue) has threatened to leave because your API response times are too slow for their real-time trading system. Your team has spent 3 months optimizing -- database indices, caching layers, CDN, connection pooling -- and gotten response times from 800ms to 350ms. The customer needs under 100ms. Your CTO says it is physically impossible with your current architecture.

**Step 1: Extract the real problem.** You ask: "Our biggest customer needs sub-100ms API responses. We've optimized from 800ms to 350ms but our CTO says we can't go further. Help me think about this differently."

The skill starts by separating the stated problem ("make API faster") from the underlying need. The customer is building a real-time trading system. They do not actually need your API to be fast -- they need data to arrive in time for trading decisions. This reframing opens an entirely different solution space.

**Step 2: Challenge assumptions.** The skill identifies three ghost constraints: (1) the assumption that the customer must call your API synchronously, (2) the assumption that you must serve from your existing infrastructure, (3) the assumption that you need to send complete responses. Each assumption, when questioned, reveals new approaches.

**Step 3: Generate solutions across domains.** Using lateral thinking (random entry from financial markets), the skill draws an analogy to market data feeds: exchanges do not wait for clients to request prices -- they push updates. This generates a push-based architecture using WebSockets or server-sent events. Using SCAMPER (Eliminate: eliminate the request-response cycle entirely; Reverse: instead of the customer pulling data, push data before they need it), more variations emerge: pre-computed results pushed on a schedule, edge-deployed computation nodes closer to the customer's infrastructure, a shared-nothing data partition dedicated to this customer.

**Step 4: Analyze with game theory and systems thinking.** Game theory analysis reveals that accommodating this one customer's architecture needs creates a strategic commitment: you become the only vendor who can serve real-time trading, creating a moat. Systems thinking identifies a reinforcing loop: faster service attracts more trading customers, which justifies more investment in real-time infrastructure, which attracts more customers. First principles analysis shows that sub-100ms is achievable with edge deployment (data physically closer = less latency) even without algorithmic changes.

**Step 5: Synthesize recommendation.** The skill produces a ranked recommendation: (1) Push architecture with WebSocket streaming (eliminates the latency problem entirely, estimated 3 weeks), (2) Edge-deployed data partition for this customer (reduces latency to ~50ms, estimated 6 weeks), (3) Shared-nothing architecture for real-time customers (strategic platform investment, 3 months). Decision criteria: if the customer can accept a push model, option 1 is fastest and cheapest. If they require request-response, option 2 is the bridge.

**Gotchas discovered:** The CTO was right that the current architecture could not reach 100ms -- but the constraint was the request-response model, not the technology. Reframing "make the API faster" to "get data to the customer in time" changed the problem from impossible to straightforward.

## Usage Scenarios

### Scenario 1: Breaking through a technical dead end

**Context:** Your team has spent a month trying to make a batch processing pipeline faster and has exhausted all conventional optimization approaches.

**You say:** "We've tried parallelization, caching, algorithmic optimization, and hardware upgrades for our batch pipeline. It's still too slow. What are we missing?"

**The skill provides:**
- Assumption challenging: must it be batch? What if it were streaming?
- First principles: what's the theoretical minimum time for this computation?
- Cross-domain analogy from game engines (spatial partitioning) to data processing
- SCAMPER analysis: eliminate (which processing steps are unnecessary?), reverse (process output-first)

**You end up with:** 3-5 unconventional approaches that reframe the problem rather than optimizing within the current paradigm.

### Scenario 2: Competitive strategy with resource disadvantage

**Context:** You are a 10-person startup competing with a well-funded company with 200 engineers in the same space.

**You say:** "We have 10 engineers vs their 200. We can't outbuild them. What's our asymmetric strategy?"

**The skill provides:**
- Game theory analysis of where the competitor is committed and cannot pivot
- First principles on what customers actually value that scale prevents (speed, personal attention, flexibility)
- Inversion: what would guarantee failure? (Trying to match features) What's the opposite? (Dominate a niche)
- Strategic commitment analysis: which moves create irreversible advantages?

**You end up with:** A strategic direction that exploits the competitor's structural disadvantages rather than competing on their strengths.

### Scenario 3: Organizational incentive misalignment

**Context:** Two engineering teams are blocking each other on a shared service. Each team optimizes for their own metrics, creating a prisoner's dilemma.

**You say:** "Teams A and B both need the shared payment service but they keep breaking each other's integrations. How do I fix this with game theory?"

**The skill provides:**
- Nash equilibrium analysis showing why the current state is stable but suboptimal
- Incentive restructuring options (shared metrics, joint ownership, API contract)
- Repeated-game dynamics: how reputation and cooperation evolve over repeated interactions
- Mechanism design: change the game, not the players

**You end up with:** A concrete incentive restructuring plan that makes cooperation the dominant strategy for both teams.

---

## Decision Logic

**When does creative-problem-solving activate vs. critical-intuition?**

These two skills are complementary opposites:
- **creative-problem-solving:** Generating new ideas, finding unconventional solutions, breaking through blocks, exploring solution spaces. Forward-looking, divergent.
- **critical-intuition:** Analyzing existing ideas, detecting bias, evaluating evidence, finding hidden problems. Backward-looking, convergent.

If the user needs new solutions -> creative-problem-solving. If the user needs to evaluate existing ideas -> critical-intuition. Often used in sequence: generate with creative-problem-solving, then critique with critical-intuition.

**Which creativity technique does the skill select?**

Based on problem type:
- Mental block or stuck thinking -> Lateral thinking (random entry, provocation, escape)
- Systematic exploration needed -> SCAMPER, morphological analysis
- Strategic or competitive problem -> Game theory, first principles
- Decision between options -> Multi-criteria analysis, expected value

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Creative solutions are impractical | Generated ideas are inspiring but have no implementation path | Ensure Step 4 (analysis) and Step 5 (recommendation) are not skipped; every idea needs feasibility assessment |
| Problem was not properly understood before generating solutions | Solutions address the stated problem but not the real underlying need | Return to Step 1; spend more time extracting the real problem with "What is the underlying goal?" and "What happens if we do nothing?" |
| Game theory analysis is too abstract | Strategic recommendations do not map to concrete actions | Ground game theory in specific actors, specific moves, specific payoffs; name the people and teams involved |

## Ideal For

- **Engineering leaders** facing complex technical or organizational problems where conventional approaches have failed and fresh thinking is needed
- **Product managers** evaluating strategic directions who need to analyze competitive dynamics, customer incentives, and market positioning with game theory
- **Startup founders** competing against better-resourced competitors who need asymmetric strategies that exploit structural advantages
- **Technical architects** stuck on design decisions who need first-principles analysis to escape assumption-driven dead ends

## Not For

- **Analyzing or critiquing existing proposals** -- if you have a plan and want it stress-tested, use `critical-intuition`
- **Detecting bias or hidden patterns in data** -- if you need to evaluate evidence quality or find what's missing, use `critical-intuition`
- **Prioritizing a known list of options** -- if you already have options and need to rank them, use `prioritization`

## Related Plugins

- **critical-intuition** -- The analytical counterpart: critique and evaluate what creative-problem-solving generates
- **systems-thinking** -- Deeper systems dynamics (feedback loops, leverage points) for complex adaptive problems
- **prioritization** -- RICE, MoSCoW, ICE scoring for ranking generated solutions
- **risk-management** -- Systematic risk assessment for evaluating the riskier creative solutions
- **outcome-orientation** -- Define measurable success criteria for creative solutions using OKRs

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
