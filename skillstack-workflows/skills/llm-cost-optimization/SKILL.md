---
name: llm-cost-optimization
description: Funnel-with-gate workflow for reducing LLM costs without degrading quality. Starts with diagnosing the cost surface using cloud-finops (specifically the finops-for-ai and finops-anthropic references), then applies context-optimization to reduce context per call, context-compression to compress what can't be reduced, prompt-engineering for shorter prompts and better model selection, and uses agent-evaluation as a mandatory gate — if any optimization degrades quality, roll it back. Finishes with prioritization of remaining opportunities and risk-management guardrails for future auto-scaling. Use when LLM costs are growing faster than usage, when leadership is asking why the bill doubled, when unit economics are turning negative, or when a new feature is about to ship and cost containment is part of the launch plan. NOT for cost reductions that don't involve LLMs — use cloud-finops directly.
---

# LLM Cost Optimization

> The failure mode in LLM cost optimization isn't cutting costs — it's cutting costs by degrading quality without noticing. The gate at `agent-evaluation` is non-negotiable: any optimization that makes the product worse is a failure, not a savings. This workflow treats cost and quality as a single optimization problem with two axes, not as cost alone.

LLM costs are fundamentally different from traditional cloud costs: they're incurred at the moment a decision is made, not when capacity is provisioned. This makes them invisible to traditional FinOps reviews and catastrophic when anti-patterns persist. The workflow maps those anti-patterns and applies the specific optimizations that address them.

---

## When to use this workflow

- LLM costs are growing faster than usage (suggests anti-patterns)
- A feature's unit economics are turning negative (cost per interaction > revenue per interaction)
- Leadership is asking why the Anthropic / OpenAI / Bedrock / Vertex bill doubled
- A new feature is about to ship and you need cost containment in the launch plan
- You just discovered your agent is in an agentic loop and the bill has already arrived

## When NOT to use this workflow

- **Traditional cloud costs** — use the `cloud-finops` skill directly
- **Fixed-cost LLM services** (provisioned throughput only) — use capacity planning, not this workflow
- **Early-stage experiments** — don't optimize costs before you know the product works
- **Cost reductions that would require changing the product** — use the `strategic-decision` workflow to decide if the product change is worth it

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install cloud-finops@skillstack
/plugin install context-optimization@skillstack
/plugin install context-compression@skillstack
/plugin install prompt-engineering@skillstack
/plugin install agent-evaluation@skillstack
/plugin install prioritization@skillstack
/plugin install risk-management@skillstack
```

---

## Core principle

**Cost without quality is not savings.** Every optimization in this workflow is paired with a quality check. If the optimization reduces cost and quality, it's rolled back. If the optimization reduces cost but not quality, it's kept. If the optimization reduces cost and IMPROVES quality (rare but possible — smaller prompts are often clearer prompts), it's celebrated.

Secondary principle: **the cost problem is usually not where you first look.** Teams typically assume the cost is in token rates and try to negotiate better rates. The actual causes are almost always context bloat, agentic loops, zombie features, or crossing long-context pricing thresholds. Diagnose before prescribing.

---

## The funnel

### Phase 1 — diagnose the cost surface (cloud-finops / finops-for-ai)

Load the `cloud-finops` skill, specifically its `finops-for-ai` reference (which covers LLM-specific cost patterns). If you're using Anthropic, Bedrock, Vertex, or Azure OpenAI, also load the provider-specific reference (`finops-anthropic`, `finops-bedrock`, `finops-vertexai`, `finops-azure-openai`).

Audit for the six AI cost anti-patterns (from `finops-for-ai`):

1. **Zombie AI features** — a feature's usage dropped but it's still processing (pre-embedding, indexing, maintaining state). Signal: token consumption stable or rising while active user sessions decline. Fix: detection + decommissioning process.

2. **Technology churn debt** — leftover API keys, buckets, reservations from abandoned experiments. Signal: AI spend in accounts with no recent deployments. Fix: audit and cleanup.

3. **Agentic loops** — agents calling agents, retries multiplying token consumption 5-50× per user request. Signal: average tokens per request significantly above design estimate; cost growing faster than user volume. Fix: retry limits, loop detection, and the specific case in `finops-for-ai`.

4. **Data egress in AI pipelines** — RAG systems with data in one region, embeddings in another, inference in a third. Signal: S3/network costs rising in proportion with AI feature usage. Fix: co-locate, or reduce cross-region transfer.

5. **Negative unit economics at scale** — each interaction loses money but the losses are small until adoption grows. Signal: AI costs growing proportionally with user adoption; unit margin declining as volume increases. Fix: price the feature, gate access, or redesign.

6. **Context-length pricing thresholds** — crossing 200K/272K input tokens doubles the input rate for the WHOLE request, not just the tokens above the threshold. This is the silent multiplier. Signal: invoice cost per token higher than expected from flat-rate model. Fix: threshold detection in instrumentation, chunk differently, or use caching.

Output: a prioritized list of which anti-patterns are active in your system and the estimated cost impact of each.

### Phase 2 — reduce context per call (context-optimization)

Load the `context-optimization` skill.

Context reduction is the highest-leverage lever in LLM cost work because tokens are almost always the dominant cost driver and most systems ship with more context than needed.

Techniques:

- **KV-cache optimization** — structure the prompt so repeated prefixes hit the cache. Anthropic offers up to 90% discount on cached prefixes; Azure OpenAI offers ~75%. If your agent has a stable system prompt + dynamic user content, put the stable part first and enable caching. This alone often cuts costs 40-60%.

- **Observation masking** — hide tool calls, intermediate results, and debug traces from later turns where they don't add value. The agent doesn't need to see every past tool response to reason correctly.

- **Context partitioning** — split "working memory" (what the agent is doing right now) from "reference knowledge" (what it might need to look up). Working memory lives in the prompt; reference knowledge lives in retrieval.

- **Retrieval over inclusion** — the opposite of stuffing: instead of passing all documents, retrieve only the relevant ones per turn. Requires embeddings and vector search, but pays for itself quickly.

- **Output masking from next turn** — for multi-step agents, the N-turn context includes all previous inputs AND outputs. Output masking removes past outputs that the agent doesn't need to see again, preserving inputs (which maintain the reasoning chain).

For each technique, measure before and after:
- Input tokens per request
- Output tokens per request
- Cost per request
- Latency per request

Output: a set of context reductions with measured impact on each metric.

### Phase 3 — compress what you can't reduce (context-compression)

Load the `context-compression` skill.

What's left after Phase 2's reduction is context that's actually needed but expensive. Compression techniques:

- **Summarization of history** — long conversations can be summarized periodically, replacing raw history with a summary that preserves key facts.
- **Anchored iterative summarization** — summarization with stable anchors so facts aren't lost between summarizations.
- **Tokens-per-task optimization** — structure the task so the model gets what it needs in fewer tokens (prompt structure matters).
- **Compaction triggers** — rules for when to compact (conversation length, tool response size, total token count).
- **Probe-based evaluation** — check that compressed context still preserves the information the model needs by probing for it.

Compression is trickier than reduction because it can lose information silently. Always pair with Phase 5's quality gate.

Output: a compression policy for each long-context feature with measured cost savings and quality preservation.

### Phase 4 — prompt and model changes (prompt-engineering)

Load the `prompt-engineering` skill.

- **Shorter prompts** — most production prompts are longer than they need to be. Go through each and ask: "what would happen if I cut this line?" Cut and test.
- **Model rightsizing** — this is the biggest lever most teams don't pull. See `finops-for-ai`:
  - Simple tasks (classification, extraction, routing) → Haiku / GPT-4o mini / Gemini Flash. Cost ratio ~1×.
  - Complex reasoning, code generation → Sonnet / GPT-4o / Gemini Pro. Cost ratio ~12×.
  - Research, nuanced judgment → Opus / GPT-4 / Gemini Ultra. Cost ratio ~60×.
  
  Teams default to the largest model for everything. Changing a classification step from Opus to Haiku is often a 60× cost reduction on that step with no quality change.

- **Tiered routing** — classify query complexity first (cheap), route to appropriate model. Simple queries to small models; complex queries to large models.

- **Temperature and max_tokens** — always set `max_tokens`. Unbounded responses are a common cost leak. Lower temperature for deterministic outputs.

- **Prompt caching** — if not already done via Phase 2, cache system prompts and static context explicitly.

- **Batch inference** — for non-interactive workloads (offline classification, evaluation, document processing), providers offer 50% discounts on batch APIs. Use them.

Output: a set of prompt/model changes with before/after cost measurements.

### Phase 5 — THE QUALITY GATE (agent-evaluation)

**This gate is non-negotiable.** Every change from Phases 2-4 must pass through this gate before it's kept.

Load the `agent-evaluation` skill. For each optimization:

1. **Run the eval set through both the old and new version.**
2. **Score on the same rubric.**
3. **Compare.**

Three outcomes:

- **Cost down, quality unchanged or improved** → keep the change. This is the goal.
- **Cost down, quality unchanged** → keep the change. Still the goal.
- **Cost down, quality degraded measurably** → ROLL BACK the change. The savings are not savings. Find a different lever.

Without this gate, the workflow becomes a cost-cutting exercise that silently ships a worse product. Teams that skip this gate end up with a dashboard showing cost savings and a support queue showing quality complaints, and they can't connect the two.

**Build the eval harness once, run it for every change.** The infrastructure from the `build-ai-agent` workflow's Phase 2 applies here too; if you don't have it yet, build it now — before Phase 2 of this workflow. It is the prerequisite, not a nice-to-have.

### Phase 6 — prioritize remaining opportunities (prioritization)

Load the `prioritization` skill.

After the first pass, you'll have a list of optimizations that either didn't make it through the gate or weren't implemented. Rank them by impact (cost savings potential) vs. effort (implementation complexity) vs. risk (quality impact uncertainty).

Patterns:

- **High impact, low effort, low risk** → do next
- **High impact, high effort, low risk** → plan for next quarter
- **High impact, any effort, high risk** → investigate before committing
- **Low impact, any effort, any risk** → deprioritize

Output: a ranked backlog of future optimization work with estimated savings.

### Phase 7 — guardrails for the future (risk-management)

Load the `risk-management` skill.

Optimizations you made today will drift. Usage grows, features are added, models are updated, prompts are edited. The cost structure you optimized will degrade.

Add guardrails:

- **Cost anomaly alerts** — at the feature level, not just the account level. A 20% daily increase in cost per feature should page someone.
- **Unit economic tracking** — cost per user, cost per interaction, cost per successful task. Plot over time.
- **Hard spending caps** at feature level — prevents unbounded failures (e.g., an agent loop running overnight).
- **Model selection review** — quarterly check that each use case is still on the right model tier.
- **Context growth monitoring** — average input tokens per request. When this starts growing, something has been added that's costing more than it should.
- **Feature decommissioning process** — zombie detection. When a feature's usage drops below a threshold, it's flagged for review.

Output: monitoring dashboards, alerts, and a quarterly review process.

---

## Gates and failure modes

**Gate 1: the diagnosis gate.** Phase 2 cannot start until Phase 1's audit has named specific anti-patterns. Reducing context on a system whose real problem is an agentic loop is treating the symptom while the fire burns.

**Gate 2: the eval gate** (the workflow's core gate). Every optimization from Phases 2-4 must pass through Phase 5 before being kept. No exceptions. This is what makes this an optimization workflow and not just a cost-cutting exercise.

**Gate 3: the monitoring gate.** Phase 7 cannot be skipped. Without monitoring, the gains you just captured will erode.

**Failure mode: premature Phase 4.** The team jumps straight to "use a cheaper model" without diagnosing context bloat. They save 20% via model switching but leave 60% savings on the table in Phase 2. Mitigation: follow the phases in order.

**Failure mode: skipping the gate.** "The eval would have passed anyway, we don't need to run it." Then three weeks later a customer reports that the product got worse, and nobody can tell which optimization caused the regression. Mitigation: non-negotiable gate.

**Failure mode: vanity savings.** Dashboard says "we saved $40K/month!" Then someone points out that usage also dropped 30% due to churn caused by the quality degradation. Net savings: negative. Mitigation: track unit economics (cost per successful task), not raw cost.

**Failure mode: the one-time savings trap.** You optimize, you celebrate, you move on. Six months later costs are back because nothing maintained the discipline. Mitigation: Phase 7's ongoing monitoring.

**Failure mode: the "we'll add the eval harness later" trap.** You optimize first, intending to validate later. Later never comes. You're flying blind. Mitigation: build the eval harness BEFORE Phase 2. If it doesn't exist, that's Phase 0.

---

## Output artifacts

A completed optimization cycle produces:

1. **An anti-pattern audit report** — which of the six anti-patterns were active, with evidence
2. **A set of implemented optimizations** — each with before/after cost, latency, and quality measurements
3. **An eval harness** (if it didn't exist) — reusable for all future changes
4. **A monitoring dashboard** — cost per feature, unit economics, anomaly alerts
5. **A prioritized backlog** — remaining opportunities ranked
6. **A guardrails document** — alerts, caps, review cadence
7. **An executive summary** — cost savings, quality preservation, risk changes (for stakeholders)

---

## Related workflows and skills

- For the agent whose costs you're optimizing (if it doesn't exist yet), use the `build-ai-agent` workflow — Phase 2 of that workflow builds the eval harness this workflow requires
- For broader cloud cost optimization (not just LLMs), use `cloud-finops` directly with its AWS/Azure/GCP references
- For the strategic decision of whether to pay the cost or change the product, use the `strategic-decision` workflow
- For debugging specific cost spikes, use the `debug-complex-issue` workflow with the LLM variant

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
