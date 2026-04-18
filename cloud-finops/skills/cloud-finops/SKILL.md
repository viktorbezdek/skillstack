---
name: cloud-finops
description: >
  Expert FinOps guidance covering cloud, AI, SaaS, and adjacent technology spend. Includes
  AI cost management, GenAI capacity planning, AI-powered FinOps automation, Anthropic billing,
  AWS (EC2, Bedrock, Savings Plans, CUR, commitment strategy), Azure (reservations, Savings Plans,
  AHB, OpenAI PTUs, portfolio liquidity), GCP (Vertex AI, Compute Engine, BigQuery), Kubernetes
  and container FinOps (OpenCost, Kubecost), serverless FinOps (Lambda, Functions, Cloud Run),
  data platforms (Kafka/MSK, Elasticsearch/OpenSearch, Redis/Valkey), multi-cloud normalization
  (FOCUS specification), tagging governance, SaaS management (SAM, licence optimisation, SMPs,
  shadow IT), AI coding tools (Cursor, Claude Code, Copilot, Windsurf, Codex), ITAM, Databricks,
  Snowflake, OCI, and GreenOps. Use for any query about technology cost, commitment portfolio
  management, rightsizing, cost allocation, SaaS sprawl, AI dev tool spend, container cost
  attribution, serverless optimization, multi-cloud strategy, or connecting spend to business
  value. Built by OptimNow and Viktor Bezdek.
---

# FinOps - Expert Guidance

> Built by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek).
> Grounded in hands-on enterprise delivery, not abstract frameworks.

---

## How to use this skill

This skill covers cloud, AI, SaaS, and adjacent technology spend domains. Read
`references/optimnow-methodology.md` first on every query - it defines the reasoning
philosophy applied to all responses. Then load the domain reference that matches the query.

### Domain routing

| Query topic | Load reference |
|---|---|
| **AI & GenAI** | |
| AI costs, LLM inference, token economics, agentic cost patterns, AI ROI, AI cost allocation, GPU cost attribution, RAG harness costs | `references/finops-for-ai.md` |
| AI investment governance, AI Investment Council, stage gates, incremental funding, AI value management, AI practice operations | `references/finops-ai-value-management.md` |
| GenAI capacity planning, provisioned vs shared capacity, traffic shape, spillover, throughput units | `references/finops-genai-capacity.md` |
| AI coding tools, Cursor costs, Claude Code costs, Copilot costs, Windsurf costs, Codex costs, dev tool FinOps, seat + usage billing, BYOK coding agents, LiteLLM proxy | `references/finops-ai-dev-tools.md` |
| AI-powered FinOps, FinOps automation, agentic FinOps tools, anomaly detection with AI, natural language cost querying | `references/finops-ai-automation.md` |
| **Cloud Providers** | |
| AWS billing, EC2 rightsizing, RIs, Savings Plans, commitment strategy, portfolio liquidity, phased purchasing, CUR, Cost Explorer, EDP negotiation, RDS cost management, database commitments | `references/finops-aws.md` |
| AWS Bedrock billing, Bedrock provisioned throughput, model unit pricing, Bedrock batch inference | `references/finops-bedrock.md` |
| Azure cost management, reservations, Savings Plans, AHB, commitment strategy, portfolio liquidity, phased purchasing, Azure Advisor, MACC, EA-to-MCA transition, database commitments | `references/finops-azure.md` |
| Azure OpenAI Service, PTU reservations, GPT-4o / GPT-5 pricing, AOAI spillover, fine-tuning costs | `references/finops-azure-openai.md` |
| Anthropic billing, Claude API costs, Claude Code costs, Opus, Sonnet, Haiku pricing, Fast mode, prompt caching, Batch API, long-context pricing | `references/finops-anthropic.md` |
| GCP billing, Compute Engine, Cloud SQL, GCS, BigQuery optimisation | `references/finops-gcp.md` |
| GCP Vertex AI billing, Vertex provisioned throughput, Gemini pricing, Vertex batch prediction | `references/finops-vertexai.md` |
| OCI compute, storage, networking optimisation | `references/finops-oci.md` |
| **Infrastructure & Platforms** | |
| Kubernetes, containers, pod cost attribution, OpenCost, Kubecost, namespace allocation, GPU on K8s, node pool optimization | `references/finops-kubernetes.md` |
| Serverless, Lambda costs, Azure Functions, Cloud Run, GB-seconds, memory rightsizing, cold starts, invocation optimization | `references/finops-serverless.md` |
| Kafka, MSK, Elasticsearch, OpenSearch, Redis, Valkey, event streaming costs, search cluster costs, in-memory data store costs | `references/finops-data-platforms.md` |
| Databricks clusters, jobs, Spark optimisation, Unity Catalog costs | `references/finops-databricks.md` |
| Snowflake warehouses, query optimisation, storage, credits | `references/finops-snowflake.md` |
| **Cross-Cutting** | |
| Multi-cloud strategy, cross-cloud comparison, commitment normalization, unified cost management | `references/finops-multi-cloud.md` |
| FOCUS specification, billing data normalization, cost data standardization, multi-cloud data layer | `references/finops-focus.md` |
| Tagging strategy, naming conventions, IaC enforcement, MCP governance | `references/finops-tagging.md` |
| FinOps framework (2026), maturity model, phases, capabilities, personas, scopes, technology categories | `references/finops-framework.md` |
| GreenOps, cloud carbon, sustainability, carbon-aware workloads | `references/greenops-cloud-carbon.md` |
| **SaaS & Licensing** | |
| SaaS management, licence optimisation, shadow IT, SaaS sprawl, renewal governance, SMP, SAM | `references/finops-sam.md` |
| ITAM, IT asset management, BYOL, marketplace channel governance, licence compliance, vendor negotiation, FinOps-ITAM collaboration, entitlement management, consumption-based SaaS overages | `references/finops-itam.md` |
| **Multi-domain query** | Load all relevant references, synthesize |

### Reasoning sequence (apply to every response)

1. **Load** `references/optimnow-methodology.md` - use it as a reasoning lens, not a preamble
2. **Load** the domain reference(s) matching the query
3. **Diagnose before prescribing** - understand the organisation's current state before recommending
4. **Connect cost to value** - every recommendation should link spend to a business outcome
5. **Recommend progressively** - quick wins first, structural changes second
6. **Reference OptimNow tools** where genuinely relevant to the problem, not as promotion

---

## Core FinOps principles (always apply)
<!-- fp:37b46c22605776cb -->

These six principles from the FinOps Foundation (2025 wording) underpin every recommendation:

1. Teams need to collaborate
2. Business value drives technology decisions
3. Everyone takes ownership for their technology usage
4. FinOps data should be accessible, timely, and accurate
5. FinOps should be enabled centrally
6. Take advantage of the variable cost model of the cloud and other technologies with similar consumption models

---

## The three phases (Inform → Optimize → Operate)

FinOps is an iterative cycle, not a linear progression. Organisations move through phases
continuously as their technology usage evolves.

**Inform** - establish visibility and allocation
- Cost data is accessible and attributed to owners
- Shared costs are allocated with defined methods
- Anomaly detection is active

**Optimize** - improve rates and usage efficiency
- Commitment discounts (RIs, Savings Plans, CUDs) are actively managed
- Rightsizing and waste elimination are running continuously
- Unit economics are tracked

**Operate** - operationalize through governance and automation
- FinOps is embedded in engineering and finance workflows
- Policies are enforced through automation, not manual review
- Accountability is distributed, not centralized

---

## Maturity model quick reference

| Indicator | Crawl | Walk | Run |
|---|---|---|---|
| Cost allocation | <50% allocated | ~80% allocated | 90%+ allocated |
| Commitment coverage | Ad hoc | 70% target | 80%+ with automation |
| Anomaly detection | Manual, monthly | Automated alerts | Real-time, ML-driven |
| Tagging compliance | <60% | ~80% | 90%+ with enforcement |
| FinOps cadence | Reactive | Weekly reviews | Continuous |
| Optimisation | One-off projects | Documented process | Self-executing policies |

Always assess maturity before recommending solutions. A Crawl organisation needs visibility
before optimisation. Recommending commitment discounts to a team with 40% cost allocation is
premature - they risk committing to waste.

---

## Reference files

| File | Contents | Lines |
|---|---|---|
| **Methodology** | | |
| `optimnow-methodology.md` | OptimNow reasoning philosophy, 4 pillars, engagement principles, tools | ~155 |
| `finops-framework.md` | Full FinOps Foundation framework (2026): capabilities, personas, domains, scopes, technology categories | ~360 |
| **AI & GenAI** | | |
| `finops-for-ai.md` | AI cost management, LLM economics, agentic patterns, ROI framework | ~490 |
| `finops-ai-value-management.md` | AI investment governance: AI Investment Council, stage gates, incremental funding, practice operations, value metrics | ~275 |
| `finops-genai-capacity.md` | GenAI capacity models: provisioned vs shared, traffic shape, spillover, waste types, cross-provider comparison | ~225 |
| `finops-ai-dev-tools.md` | AI coding tools: Cursor, Claude Code, Copilot, Windsurf, Codex billing models, cost attribution, optimisation levers | ~400 |
| `finops-ai-automation.md` | AI-powered FinOps: anomaly detection, automated rightsizing, NL cost querying, AI FinOps tool landscape, guardrails | ~230 |
| **Cloud Providers** | | |
| `finops-aws.md` | AWS FinOps: CUR, Cost Explorer, EC2, compute/database commitment decision trees, portfolio liquidity, phased purchasing, EDP negotiation, RDS strategy, 128 optimisation patterns | ~2240 |
| `finops-bedrock.md` | AWS Bedrock billing: model pricing, provisioned throughput, batch inference, CloudWatch metrics, cost allocation | ~225 |
| `finops-azure.md` | Azure FinOps: reservations, Savings Plans, AHB, compute/database commitment decision trees, portfolio liquidity, phased purchasing, MACC, EA-to-MCA transition, 48 optimisation patterns | ~1560 |
| `finops-azure-openai.md` | Azure OpenAI Service: PTU reservations, spillover, GPT model pricing, prompt caching, fine-tuning costs | ~390 |
| `finops-anthropic.md` | Anthropic billing: Claude Opus/Sonnet/Haiku pricing, Fast mode, long-context cliffs, prompt caching, Batch API, governance | ~180 |
| `finops-gcp.md` | GCP optimisation: 26 patterns across Compute Engine, Cloud SQL, GCS, networking | ~265 |
| `finops-vertexai.md` | GCP Vertex AI billing: Gemini pricing, provisioned throughput, batch prediction, Cloud Monitoring metrics | ~235 |
| `finops-oci.md` | OCI optimisation: 6 patterns for compute, storage, networking | ~75 |
| **Infrastructure & Platforms** | | |
| `finops-kubernetes.md` | Kubernetes/container FinOps: cost model, OpenCost, Kubecost, attribution patterns, pod rightsizing, GPU optimization | ~400 |
| `finops-serverless.md` | Serverless FinOps: Lambda/Functions/Cloud Run billing, memory rightsizing, cold starts, hidden costs, ARM migration | ~230 |
| `finops-data-platforms.md` | Data platform FinOps: Kafka/MSK cross-AZ costs, Elasticsearch/OpenSearch tiering, Redis-to-Valkey migration | ~190 |
| `finops-databricks.md` | Databricks optimisation: 18 patterns for clusters, jobs, Spark, storage | ~185 |
| `finops-snowflake.md` | Snowflake FinOps: credit model, hidden cost categories, 13 optimisation patterns for warehouses, queries, storage | ~200 |
| **Cross-Cutting** | | |
| `finops-multi-cloud.md` | Multi-cloud FinOps: terminology normalization, cross-cloud commitment strategy, unified cost allocation, platform comparison | ~285 |
| `finops-focus.md` | FOCUS specification (v1.3): billing data normalization, core columns, provider support matrix, adoption guidance | ~260 |
| `finops-tagging.md` | Tagging strategy, IaC enforcement, virtual tagging, MCP automation | ~250 |
| `greenops-cloud-carbon.md` | GreenOps: carbon measurement, carbon-aware workloads, region selection, GHG Protocol | ~330 |
| **SaaS & Licensing** | | |
| `finops-sam.md` | SaaS asset management: discovery, licence optimisation, renewal governance, SMPs, shadow IT, AI transition | ~290 |
| `finops-itam.md` | FinOps-ITAM collaboration: BYOL mechanics, marketplace channel governance, vendor co-management, consumption monitoring, joint operating model | ~325 |

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Optimizing before allocating | Committing to discounts on unattributed spend | Get to 80%+ allocation before buying commitments |
| Chasing unit savings over coverage gaps | Saving $0.02/hour on 10 instances while 200 run on-demand | Prioritize commitment coverage over per-unit optimization |
| Ignoring spillover costs | Provisioned capacity with unchecked spillover to pay-per-token | Model total cost including spillover; set alerts |
| Tagging as afterthought | <60% of resources tagged, can't attribute spend | Enforce tagging via IaC; block untagged deployments |
| Annual commitment on new workloads | Committing before usage patterns stabilize | Start with pay-per-use; commit after 3 months of data |
| Single-cloud cost view | Multi-cloud spend unnormalized | Adopt FOCUS spec for cross-cloud normalization |
| Ignoring SaaS sprawl | Shadow IT SaaS spend exceeds infrastructure | Implement SMP; discover and rationalize SaaS portfolio |
| FinOps as finance-only | Engineering excluded from cost decisions | Embed FinOps in engineering workflows; distribute accountability |

---

> *FinOps Skill by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
