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

## Use cases and practical guidance

This section maps real-world scenarios to the specific references and outcomes this skill
provides. Use it to understand what this skill can do for you and which references to load.

### AI & GenAI cost management

**When to use:** You are building, deploying, or scaling AI/ML features and need to
understand, control, or forecast the costs involved.

| Scenario | Load | What you get |
|---|---|---|
| "Our AI feature costs are unpredictable and growing fast" | `finops-for-ai.md` | Four-phase implementation (visibility → unit economics → optimize → govern), six anti-patterns to audit for, request-level instrumentation guide |
| "We need to justify AI investment to leadership" | `finops-ai-value-management.md` | AI Investment Council model, stage-gate funding framework, ROI metrics that connect cost to business value |
| "Should we buy provisioned throughput for our LLM workloads?" | `finops-genai-capacity.md` | Traffic shape analysis, break-even utilization calculator, provider comparison (Bedrock vs Vertex vs Azure OpenAI), decision framework |
| "Our dev team's AI coding tool spend is out of control" | `finops-ai-dev-tools.md` | Billing model comparison (seat+usage vs BYOK), per-tool cost profiles (Cursor, Claude Code, Copilot, Windsurf, Codex), attribution via LiteLLM proxy |
| "We want to use AI to automate our FinOps processes" | `finops-ai-automation.md` | Advisory-to-autonomous maturity spectrum, tool landscape (Amnic, CloudPilot, Vantage), guardrails for automated actions |
| "Our LLM bills doubled but usage looks flat" | `finops-for-ai.md` | Context-length pricing threshold detection (the 200K token cliff that doubles input cost), prompt caching strategies, agentic loop cost patterns |
| "We need to attribute AI costs per feature, not just per account" | `finops-for-ai.md` | Proxy/gateway instrumentation guide, metadata tagging at invocation time, harness cost map (vector DB, embeddings, egress, orchestration) |

**Key questions this area answers:**
- What does our AI feature actually cost per user/conversation/document?
- Which model tier should each feature use? (model rightsizing = biggest lever)
- How do we detect zombie AI features still consuming tokens with no users?
- When does provisioned capacity save money vs pay-as-you-go?
- How do we prevent agentic retry loops from generating $27K/month in unintended spend?

---

### Cloud provider optimization (AWS, Azure, GCP, OCI)

**When to use:** You are running workloads on one or more cloud providers and need to
reduce spend, improve commitment strategy, or establish cost governance.

| Scenario | Load | What you get |
|---|---|---|
| "We're spending $500K/month on AWS and don't know where it goes" | `finops-aws.md` | CUR setup, Cost Explorer configuration, 128 optimization patterns, cost allocation by account structure |
| "Should we buy Reserved Instances or Savings Plans?" | `finops-aws.md` or `finops-azure.md` | Commitment decision trees, instrument layering strategy (Spot → Compute SP → EC2 SP → Standard RI), portfolio liquidity analysis |
| "We're negotiating an AWS Enterprise Discount Program" | `finops-aws.md` | EDP preparation roadmap, growth commitment analysis, internal alignment requirements |
| "Our Azure bill has unexpected charges after EA-to-MCA migration" | `finops-azure.md` | EA-to-MCA transition checklist, FinOps Toolkit migration paths, billing scope changes |
| "We haven't enabled Azure Hybrid Benefit anywhere" | `finops-azure.md` | AHB activation guide (free savings, no commitment, immediate effect — do this before any other Azure optimization) |
| "Our Bedrock/Claude API costs are higher than expected" | `finops-bedrock.md` + `finops-anthropic.md` | Model pricing comparison, batch inference discounts (50% off), Fast mode cost multiplier (6×), long-context pricing cliffs |
| "We want to optimize GCP but don't know where to start" | `finops-gcp.md` | 26 optimization patterns across Compute Engine, Cloud SQL, GCS, BigQuery, networking |
| "We're evaluating Azure OpenAI PTUs vs pay-as-you-go" | `finops-azure-openai.md` | PTU pool model explanation, spillover mechanics, break-even analysis (GPT-5 provisioned is +67% even at 100% utilization) |

**Key questions this area answers:**
- What is the right commitment coverage target for our workload mix?
- How do we layer Spot, Savings Plans, and Reserved Instances without over-committing?
- Which of our 128 (AWS) / 48 (Azure) / 26 (GCP) optimization patterns apply?
- What is our phased purchasing strategy to avoid cliff expirations?
- How do we handle commitment portfolio liquidity (exchange, refund, marketplace)?

---

### Infrastructure and platform optimization

**When to use:** You are running Kubernetes clusters, serverless functions, or data
platforms and need to understand their cost structure and optimize spend.

| Scenario | Load | What you get |
|---|---|---|
| "We can't attribute costs to teams on our shared K8s cluster" | `finops-kubernetes.md` | Namespace-based and label-based attribution patterns, OpenCost vs Kubecost comparison, shared cost distribution models |
| "Our Kubernetes clusters are over-provisioned but we're afraid to rightsize" | `finops-kubernetes.md` | Pod rightsizing with VPA, request-to-actual ratio monitoring (target <1.5×), node pool optimization, Spot node pools for dev/test |
| "Our Lambda costs seem disproportionate to our usage" | `finops-serverless.md` | Hidden cost iceberg (API Gateway, NAT, CloudWatch often exceed Lambda), memory rightsizing guide, ARM/Graviton migration (20-30% savings) |
| "We're paying too much for Kafka/MSK" | `finops-data-platforms.md` | Cross-AZ replication cost trap (can be 80-90% of total Kafka cost), tiered storage, partition optimization, compression strategies |
| "Should we migrate from Redis to Valkey?" | `finops-data-platforms.md` | Zero-downtime migration path, 20-33% cost savings on AWS, full API compatibility, migration checklist |
| "Our Elasticsearch cluster costs are growing linearly with data" | `finops-data-platforms.md` | Data tiering strategy (UltraWarm = 90% cheaper than hot), index lifecycle policies, shard sizing optimization |
| "Databricks costs are hard to control across teams" | `finops-databricks.md` | 18 optimization patterns, cluster segmentation, Photon vs non-Photon governance, serverless vs classic jobs |
| "Snowflake credits are being consumed faster than budgeted" | `finops-snowflake.md` | Credit model fundamentals, hidden cost categories (time travel, auto-clustering, Snowpipe, MVs), 13 optimization patterns |

**Key questions this area answers:**
- How do we build showback reports for Kubernetes namespaces?
- Is our Lambda memory allocation right-sized or are we paying for idle memory?
- What's the real total cost of our Kafka deployment (including cross-AZ networking)?
- Should we migrate to Valkey and how much will we save?
- Which Snowflake warehouses are consuming credits without proportionate business value?

---

### Multi-cloud, data standards, and governance

**When to use:** You operate across multiple providers, need standardized cost data,
or are building tagging/governance foundations.

| Scenario | Load | What you get |
|---|---|---|
| "We use AWS, Azure, and GCP but can't compare costs across them" | `finops-multi-cloud.md` + `finops-focus.md` | Terminology normalization table, FOCUS specification for unified billing data, cross-cloud commitment comparison |
| "Our tagging compliance is below 60% and we can't allocate costs" | `finops-tagging.md` | 5-tag minimum taxonomy, three enforcement layers (IaC prevention, detection, remediation), maturity progression |
| "We need to understand the FinOps framework for our team" | `finops-framework.md` | 2026 framework with 4 domains, 23 capabilities, 6 personas, Scopes, Technology Categories |
| "Leadership wants to know our cloud carbon footprint" | `greenops-cloud-carbon.md` | Carbon measurement tools (AWS CCFT, GCP, Azure), region selection for low-carbon, GHG Protocol reporting, Carbon Aware SDK |
| "We're adopting FOCUS but don't know where to start" | `finops-focus.md` | FOCUS 1.3 spec overview, provider support matrix, implementation path, adoption guidance |
| "Our FinOps maturity is at Crawl — what should we do first?" | `finops-framework.md` + `finops-tagging.md` | Crawl priorities (visibility before optimization), mandatory tag taxonomy, anomaly detection setup |

**Key questions this area answers:**
- How do we normalize AWS CUR, Azure Cost Exports, and GCP BigQuery exports into one view?
- What tags are mandatory and how do we enforce them across providers?
- Where is our organization on the FinOps maturity model and what's the right next step?
- How do we connect cloud efficiency work to ESG/sustainability reporting?
- What does the FOCUS specification change about how we process billing data?

---

### SaaS and licence management

**When to use:** You are managing SaaS subscriptions, software licences, or vendor
relationships and need to reduce sprawl, optimize licences, or improve governance.

| Scenario | Load | What you get |
|---|---|---|
| "We suspect we have significant SaaS overlap and shadow IT" | `finops-sam.md` | Six SaaS sprawl patterns, multi-method discovery approach (SSO, financial records, CASB, browser extensions), SMP vendor comparison |
| "SaaS renewals keep auto-renewing without review" | `finops-sam.md` | Renewal governance framework, 90-day pre-renewal review process, contract metadata requirements |
| "We need to bring ITAM and FinOps teams together" | `finops-itam.md` | Joint operating model, RACI, shared data requirements, Tier 1 vendor management (Microsoft, AWS, Oracle, Salesforce) |
| "We're not leveraging BYOL on Azure/AWS" | `finops-itam.md` | BYOL mechanics (Azure Hybrid Benefit, AWS Licence Manager, Oracle on cloud), marketplace channel governance |
| "Our consumption-based SaaS is over budget" | `finops-itam.md` | Consumption monitoring patterns, entitlement management, vendor co-management strategies |

**Key questions this area answers:**
- How many SaaS subscriptions do we actually have across the organization?
- Which licences are underutilized and can be reclaimed or downtiered?
- How do we prevent shadow SaaS from bypassing procurement?
- Are we missing BYOL savings on cloud deployments?
- How should FinOps and ITAM collaborate without duplicating effort?

---

### Common multi-reference scenarios

Some questions span multiple domains. Here are the most common combinations:

| Scenario | References to load together |
|---|---|
| "We're starting a FinOps practice from scratch" | `finops-framework.md` + `finops-tagging.md` + `optimnow-methodology.md` |
| "Our cloud + AI + SaaS total spend needs a unified view" | `finops-multi-cloud.md` + `finops-focus.md` + `finops-sam.md` |
| "We need to present AI ROI to the board" | `finops-for-ai.md` + `finops-ai-value-management.md` + provider-specific reference |
| "Our Kubernetes GPU workloads for ML are expensive" | `finops-kubernetes.md` + `finops-for-ai.md` + provider-specific reference |
| "We want to optimize everything — where do we start?" | `finops-framework.md` (assess maturity first) → then provider-specific + `finops-tagging.md` |
| "We're migrating from on-prem to cloud and need cost governance" | `finops-framework.md` + provider-specific + `finops-tagging.md` + `finops-itam.md` |

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

> *FinOps Skill by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
