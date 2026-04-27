---
name: build-ai-agent
description: Funnel workflow for going from "I want an agent that does X" to a deployed, evaluated, cost-monitored agent. Runs through nine phases starting with the is-this-task-agent-appropriate check (agent-project-development), then prompt design with eval criteria first (prompt-engineering), tool design and consolidation (tool-design), architecture selection for multi-step work (multi-agent-patterns), persistence decisions (memory-systems), context-window management (context-optimization), evaluation pipeline construction (agent-evaluation), deployment (hosted-agents), and ongoing cost and quality monitoring (cloud-finops + agent-evaluation). Use when you're starting a new agent project and want to avoid the common failure modes. NOT for one-shot prompts — use prompt-engineering directly for those.
---

# Build AI Agent

> The most common failure in agent projects is skipping the first question: "should this even be an agent?" The second most common failure is building the agent without an evaluation pipeline, so nobody can tell if it's getting better or worse over time. This workflow forces both.

An agent is a prompt plus tools plus state plus cost. Teams that optimize only the prompt ship fragile systems. Teams that follow this funnel ship agents that survive real use.

---

## When to use this workflow

- Starting a new agent project from scratch
- Rewriting an existing agent that has grown into a maintenance nightmare
- Planning a multi-step AI feature that can't be one prompt
- Building something with long-running state (memory, conversation history)
- Shipping to production with real users and cost exposure

## When NOT to use this workflow

- **One-shot prompts** — `prompt-engineering` alone is enough
- **Classification, extraction, summarization** — these rarely need full agent architecture
- **Prototypes never intended for production** — skip the deployment and monitoring phases
- **The task is not agent-appropriate** — Phase 1 will tell you. Respect it.

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-project-development@skillstack
/plugin install prompt-engineering@skillstack
/plugin install tool-design@skillstack
/plugin install multi-agent-patterns@skillstack
/plugin install memory-systems@skillstack
/plugin install context-optimization@skillstack
/plugin install agent-evaluation@skillstack
/plugin install hosted-agents@skillstack
/plugin install cloud-finops@skillstack
```

---

## Core principle

**Build the evaluation pipeline before you build the agent.** If you don't know how to measure whether the agent is getting better or worse with each change, you're not iterating — you're hoping. The eval pipeline is the feedback loop that turns agent development from art into engineering.

Secondary principle: **tool surface is a liability, not an asset.** Every tool you give an agent is a way it can misbehave. Start with the minimum and add only what the evaluation shows is needed.

---

## The funnel

### Phase 1 — is this even an agent problem? (agent-project-development)

Load the `agent-project-development` skill first. It has an explicit "should this be an agent?" framework. The classes of task that benefit from agent architecture are narrower than people assume.

Agent-appropriate tasks have these properties:
- The path from input to output involves multiple steps with decisions at each step
- Different inputs require different sequences of actions
- External state (tool results, retrieved information) shapes what happens next
- A failure in the middle should cause the agent to adapt, not crash

Agent-INappropriate tasks include most of what people try to build agents for:
- Text classification (use a prompt or a classifier)
- Extraction from a known schema (use structured output)
- Summarization (use a prompt)
- Translation (use a prompt)
- Single-step generation with no feedback loop (use a prompt)

If Phase 1 concludes the task isn't actually an agent task, stop this workflow. Use `prompt-engineering` directly. Building an agent for a non-agent task produces worse results at higher cost.

### Phase 2 — design the evaluation criteria FIRST (prompt-engineering + agent-evaluation)

Before writing any prompt, answer: "what would success look like, and how will I measure it on 100 cases without running them all by hand?"

From `agent-evaluation`, build:
- **A rubric** — the dimensions you care about (correctness, faithfulness, safety, style, cost, latency). Not just "is it good?"
- **An eval set** — 50-200 example inputs with expected outputs or expected properties. If you can't produce 50 examples, you don't understand the task well enough to build an agent for it.
- **A scoring method** — direct scoring, pairwise comparison, LLM-as-judge with bias mitigation. `agent-evaluation` has guidance on which to use when.
- **A baseline** — what does a naive prompt score? What about the previous version? You need a reference to know whether your changes help.

Only NOW start writing prompts with the `prompt-engineering` skill. Without the eval harness, prompt iteration is guessing.

### Phase 3 — tool design and surface reduction (tool-design)

Load the `tool-design` skill.

For each capability the agent needs:
- Can this be a tool, or can it be inlined into the prompt? (Many "tools" are actually just context.)
- If it's a tool, can it be the smallest possible API? The mistake is exposing a dozen fine-grained tools when three coarse-grained ones would work better.
- What does the tool description tell the agent? Agents choose tools based on descriptions, not source code. A bad description means the right tool never gets called.
- What does the tool response look like? Unbounded responses poison the context window. Cap lengths, structure output, return IDs instead of blobs.

Start with the absolute minimum tool set. Measure with the eval harness. Add tools only when the eval shows the agent failing on cases that additional capability would solve.

### Phase 4 — architecture choice (multi-agent-patterns)

If the task has multiple phases with different specializations, load `multi-agent-patterns` and choose:

- **Single agent with tools** — the default. Try this first. Most problems don't need multi-agent.
- **Supervisor + workers** — one agent routes to specialists. Good when specializations are clear and don't need to interact much.
- **Swarm / peer-to-peer** — agents hand off to each other. More complex; use only when supervisor adds too much overhead.
- **Hierarchical** — supervisors of supervisors. Rare; reserve for genuinely complex workflows.

The cost of multi-agent architectures isn't just tokens — it's the increased surface area for cascading failures. Each handoff is a place where information can be lost. Stay single-agent unless the eval shows you need more.

### Phase 5 — memory (memory-systems)

Load `memory-systems` if and only if the agent needs persistence across sessions.

- **Short-term memory** (within a session) — use context window management, not a memory system
- **Long-term memory** (across sessions) — evaluate Mem0 / Zep / Graphiti / Letta / LangMem / Cognee using the skill's comparison matrix
- **Neither** — skip this phase

The common mistake: adding memory "because we might need it later". Memory systems have operational cost, retrieval latency, and debugging complexity. Add them when the eval shows the agent failing because it can't remember things.

### Phase 6 — context optimization (context-optimization)

Load `context-optimization`. Even before production, plan for:

- **KV-cache optimization** — structure the context so repeated prefixes hit cache
- **Observation masking** — hide tool calls and intermediate results from later turns where they don't add value
- **Context partitioning** — split the agent's "working memory" from "reference knowledge"
- **Retrieval over inclusion** — don't stuff everything into the prompt; retrieve only what's needed per turn

Teams that skip this phase are the ones who hit the 200K token pricing cliff in production (see `cloud-finops`'s `finops-for-ai` reference) and are surprised by the bill.

### Phase 7 — build the eval pipeline (agent-evaluation)

Now that the agent exists and works in development, build the CI pipeline around it.

- Automated eval on every change — run the rubric against the eval set
- Regression alerts — any score drop on any dimension triggers a notification
- Human-in-the-loop sampling — a small percentage of production traffic gets human review
- Production monitoring — the same eval criteria running on real traffic
- Feedback loop — user corrections feed back into the eval set

The eval harness you built in Phase 2 is the skeleton; Phase 7 turns it into ongoing operations.

### Phase 8 — deployment (hosted-agents)

Load `hosted-agents`. Key decisions:

- **Sandboxed environment** — isolated per user/session
- **Scale-to-zero** — agents that idle between sessions should not cost compute
- **Session persistence** — for multi-turn conversations, where does state live?
- **Multiplayer** — if multiple users share one agent session
- **Security boundary** — what the agent can and cannot reach

The `hosted-agents` skill covers the operational patterns for all of these.

### Phase 9 — ongoing: cost and quality monitoring

The agent is live. Now two ongoing loops run in parallel:

**Cost loop (cloud-finops, especially the `finops-for-ai` reference):**
- Token cost per interaction
- Unit economics (cost per successful task vs. cost per failed task)
- Anti-pattern detection (see the six AI cost anti-patterns in `finops-for-ai`) — zombie features, agentic loops, context-length cliffs, technology churn
- Budget guardrails — hard caps at the feature level, not just the account level

**Quality loop (agent-evaluation):**
- Continuous eval on production sample
- Regression detection
- Drift detection (is the model's behavior shifting over time?)
- Edge case discovery (new failure modes from real traffic feed back into the eval set)

These loops are the difference between "we shipped an agent" and "we're running an agent". Most projects die in the transition between those two phrases.

---

## Gates and failure modes

**Gate 1: the task-fit gate.** Phase 1 must conclude positively. If the task isn't agent-appropriate, stop. Don't build an agent for a non-agent task.

**Gate 2: the eval gate.** Phase 3 cannot start until Phase 2's eval set exists. If you start writing prompts before you can measure them, you're guessing.

**Gate 3: the minimal-tools gate.** Phase 4 cannot start until Phase 3 has produced the smallest possible tool set. "We might need X later" is not a reason to add X now.

**Gate 4: the deployment gate.** Phase 8 cannot start until Phases 2 and 7 have produced the eval harness AND a cost budget. Deploying without these is how agent projects become money pits with no quality signal.

**Failure mode: prompt hill-climbing without eval.** The team iterates on prompts based on how they "feel", not measurement. Results drift. Debugging happens in threads instead of in the eval harness. Mitigation: Phase 2. No prompt iteration without the eval harness.

**Failure mode: tool bloat.** Every sprint adds a new tool. The agent now has 30+ tools, half of which are never called, and the tool descriptions compete for attention. Mitigation: Phase 3 discipline. Tools are added only when eval shows they're needed.

**Failure mode: ludocost dissonance.** The agent works great in demos but costs $4 per interaction in production. Nobody noticed because cost wasn't tracked. Mitigation: Phase 6 and Phase 9's cost loop.

**Failure mode: silent drift.** The agent worked at launch. Six months later it's slightly worse and nobody can pinpoint when. Mitigation: Phase 9's continuous eval on production sample.

---

## Output artifacts

A completed build produces:

1. **A deployed agent** — sandboxed, scale-to-zero, with session persistence if needed
2. **An evaluation harness** — eval set + rubric + scoring method + CI integration
3. **A tool catalog** — every tool with its description, expected inputs, expected outputs, and the eval evidence that justified its inclusion
4. **A cost model** — expected cost per interaction, unit economics, anomaly thresholds
5. **A monitoring dashboard** — cost loop + quality loop
6. **A decision log** — why this architecture, why these tools, why this memory system (or no memory system)

---

## Related workflows and skills

- For debugging a misbehaving agent in production, use the `debug-complex-issue` workflow with the LLM/agent variant
- For managing LLM costs after the agent is live, use the `llm-cost-optimization` workflow
- For the theory underneath agent memory, see the `memory-systems` skill's framework comparison
- For evaluating whether an agent is even worth building, start with `agent-project-development` alone before committing to this full workflow

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
