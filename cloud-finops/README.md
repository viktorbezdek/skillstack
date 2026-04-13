# Cloud FinOps

> **v2.1.0** | DevOps & Infrastructure | 3 iterations

Expert Cloud FinOps guidance across 26 domain-specific reference files covering cloud, AI, SaaS, containers, serverless, data platforms, and sustainability. Built by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## What Problem Does This Solve

Technology spend now spans cloud providers, AI/LLM workloads, SaaS subscriptions, Kubernetes clusters, serverless functions, data platforms (Kafka, Elasticsearch, Snowflake, Databricks), and AI coding tools -- each with different billing models, pricing mechanics, and optimization levers. FinOps practitioners need guidance that is current, domain-specific, and grounded in real delivery experience, not generic cost-cutting checklists. A team that commits to Reserved Instances before achieving 80% cost allocation is committing to waste. A team that buys Azure OpenAI PTUs without understanding the break-even utilization threshold overspends from day one.

This skill gives Claude deep FinOps expertise across all of these cost surfaces. It follows the OptimNow methodology: diagnose before prescribing, connect cost to business value, and recommend progressively from quick wins to structural changes. Every response loads the reasoning philosophy first, then the domain-specific reference matching the query.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install cloud-finops@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention FinOps, cloud cost, or optimization topics, or you can invoke it explicitly with `Use the cloud-finops skill to analyze our AWS commitment strategy`.

## What's Inside

**26 reference files** organized into 6 domains (~10,500 lines of practitioner guidance):

### AI & GenAI (5 files)

| Reference | Coverage |
|---|---|
| **AI cost management** | LLM economics, agentic cost patterns, six anti-patterns, four-phase implementation (visibility, unit economics, optimize, govern), harness cost mapping |
| **AI investment governance** | AI Investment Council model, stage-gate funding framework, incremental funding, value metrics connecting cost to business outcomes |
| **GenAI capacity planning** | Provisioned vs shared capacity, traffic shape analysis, break-even utilization calculator, spillover mechanics, cross-provider comparison (Bedrock vs Vertex vs Azure OpenAI) |
| **AI coding tools** | Cursor, Claude Code, Copilot, Windsurf, Codex billing models (seat+usage vs BYOK), per-tool cost profiles, attribution via LiteLLM proxy |
| **AI-powered FinOps** | Anomaly detection, automated rightsizing, natural-language cost querying, advisory-to-autonomous maturity spectrum, tool landscape, guardrails |

### Cloud Providers (8 files)

| Reference | Coverage |
|---|---|
| **AWS** | CUR setup, Cost Explorer, 128 optimization patterns, commitment decision trees (Spot, Compute SP, EC2 SP, RI layering), portfolio liquidity, phased purchasing, EDP negotiation, RDS strategy (~2,240 lines) |
| **Azure** | AHB activation (free savings, no commitment), reservations, Savings Plans, 48 optimization patterns, MACC, EA-to-MCA transition checklist (~1,560 lines) |
| **GCP** | 26 optimization patterns across Compute Engine, Cloud SQL, GCS, BigQuery, networking |
| **OCI** | 6 patterns for compute, storage, networking |
| **AWS Bedrock** | Model pricing, provisioned throughput, batch inference (50% discount), CloudWatch metrics, cost allocation |
| **Azure OpenAI** | PTU reservations, spillover mechanics, GPT model pricing, prompt caching, fine-tuning costs |
| **Anthropic** | Claude Opus/Sonnet/Haiku pricing, Fast mode (6x multiplier), long-context cliffs (200K threshold doubles input cost), Batch API, prompt caching |
| **Vertex AI** | Gemini pricing, provisioned throughput, batch prediction, Cloud Monitoring metrics |

### Infrastructure & Platforms (5 files)

| Reference | Coverage |
|---|---|
| **Kubernetes** | Cost model, OpenCost vs Kubecost comparison, namespace/label attribution, shared cost distribution, pod rightsizing, GPU optimization |
| **Serverless** | Lambda/Functions/Cloud Run billing, hidden cost iceberg (API Gateway + NAT + CloudWatch often exceed compute), memory rightsizing, ARM/Graviton migration (20-30% savings) |
| **Data platforms** | Kafka/MSK cross-AZ cost trap (80-90% of total cost), OpenSearch data tiering (UltraWarm = 90% cheaper), Redis-to-Valkey migration (20-33% savings) |
| **Databricks** | 18 optimization patterns, cluster segmentation, Photon governance, Unity Catalog costs |
| **Snowflake** | Credit model fundamentals, hidden costs (time travel, auto-clustering), 13 optimization patterns for warehouses, queries, storage |

### Cross-Cutting (5 files)

| Reference | Coverage |
|---|---|
| **Multi-cloud** | Terminology normalization table, cross-cloud commitment strategy comparison, unified cost allocation methodology |
| **FOCUS specification** | v1.3 billing data standard, core columns, provider support matrix, adoption guidance for multi-cloud normalization |
| **Tagging** | 5-tag minimum taxonomy, three enforcement layers (IaC prevention, detection, remediation), maturity progression |
| **FinOps framework** | 2026 version with 4 domains, 23 capabilities, 6 personas, Scopes, Technology Categories |
| **GreenOps** | Carbon measurement tools, low-carbon region selection, carbon-aware workloads, GHG Protocol reporting, Carbon Aware SDK |

### SaaS & Licensing (2 files)

| Reference | Coverage |
|---|---|
| **SaaS management** | Six sprawl patterns, multi-method discovery (SSO, financial records, CASB, browser extensions), licence optimization, SMP vendor comparison |
| **ITAM** | BYOL mechanics (Azure Hybrid Benefit, AWS Licence Manager, Oracle on cloud), marketplace governance, vendor co-management, consumption monitoring, joint operating model |

### Methodology (1 file)

**OptimNow methodology** -- reasoning philosophy, four pillars, engagement principles. Loaded on every query as a reasoning lens, not a preamble.

## Usage Scenarios

**1. "We're spending $500K/month on AWS and don't know where the money goes."**
Start with CUR setup and Cost Explorer configuration from the AWS reference. Apply cost allocation by account structure. Use the tagging reference to implement the 5-tag minimum taxonomy. Assess maturity level first -- if cost allocation is below 50%, focus on visibility (Inform phase) before any optimization. The 128 AWS optimization patterns are organized by service for targeted action.

**2. "Should we buy Reserved Instances or Savings Plans for our compute?"**
Load the AWS or Azure commitment decision tree. The instrument layering strategy goes: Spot/preemptible first (biggest discount for fault-tolerant), then Compute Savings Plans (most flexible commitment), then EC2/instance-family SPs (deeper discount, less flexible), then RIs (deepest discount, least flexible). Apply the portfolio liquidity analysis to avoid over-commitment. Use phased purchasing rather than buying all commitment at once.

**3. "Our AI feature costs are unpredictable and growing fast."**
Load the AI cost management reference. Follow the four-phase approach: visibility (instrument every request with model, tokens, latency), unit economics (cost per successful completion, not per API call), optimize (prompt caching, batch inference, model routing), govern (budgets, alerts, stage-gate approvals). Audit for the six anti-patterns. Check for the 200K token cliff in the Anthropic reference -- crossing it doubles input cost.

**4. "We need to justify our AI investment to leadership."**
Load the AI value management reference. Use the AI Investment Council model to structure governance. Apply the stage-gate funding framework with incremental approval. Connect cost to business value with the ROI metrics. Present spend alongside business outcomes, not in isolation. Load the AI coding tools reference if dev tool costs (Cursor, Copilot, Claude Code) are part of the conversation.

**5. "Our Kubernetes costs are impossible to attribute to teams."**
Load the Kubernetes reference. Implement namespace and label-based attribution using OpenCost or Kubecost. Choose a shared cost distribution model (proportional, fixed, or weighted). For GPU workloads, add the AI cost reference for GPU-specific optimization patterns. Node pool optimization and pod rightsizing typically provide 20-40% savings.

## When to Use / When NOT to Use

**Use when:**
- Analyzing or optimizing cloud spend (AWS, Azure, GCP, OCI)
- Managing AI/LLM costs, GenAI capacity planning, or AI investment governance
- Implementing commitment strategies (RIs, Savings Plans, CUDs)
- Attributing costs in Kubernetes, serverless, or multi-tenant environments
- Optimizing data platform costs (Kafka, Elasticsearch, Snowflake, Databricks)
- Setting up tagging governance, multi-cloud normalization, or SaaS management
- Measuring cloud carbon footprint for sustainability reporting

**Do NOT use when:**
- Building CI/CD pipelines or infrastructure automation -- use [cicd-pipelines](../cicd-pipelines/) instead
- Writing Dockerfiles or container configurations -- use [docker-containerization](../docker-containerization/) instead

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline design, DevOps automation, infrastructure as code
- **[Docker Containerization](../docker-containerization/)** -- Docker basics, multi-stage builds, Compose orchestration
- **[Workflow Automation](../workflow-automation/)** -- CI/CD orchestration, multi-agent parallel execution

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
