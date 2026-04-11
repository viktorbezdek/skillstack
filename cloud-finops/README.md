# Cloud FinOps

> **v2.1.0** | DevOps & Infrastructure | 3 iterations

Expert Cloud FinOps guidance across 26 domain-specific reference files covering cloud, AI, SaaS, containers, serverless, data platforms, and sustainability. Built by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## What Problem Does This Solve

Organizations struggle to manage technology spend that spans cloud providers, AI workloads, SaaS subscriptions, Kubernetes clusters, serverless functions, and data platforms. Each has different billing models, pricing mechanics, and optimization levers. FinOps practitioners need domain-specific guidance that is current, actionable, and grounded in real delivery — not generic cost-cutting checklists.

This skill gives Claude deep FinOps expertise across all of these cost surfaces, enabling it to diagnose before prescribing, connect cost to business value, and recommend progressively from quick wins to structural changes.

## When to Use This Skill

### AI & GenAI costs

| You say... | The skill provides... |
|---|---|
| "Our AI feature costs are unpredictable and growing fast" | Four-phase implementation (visibility → unit economics → optimize → govern), six anti-patterns to audit for, request-level instrumentation guide |
| "We need to justify AI investment to leadership" | AI Investment Council model, stage-gate funding framework, ROI metrics connecting cost to business value |
| "Should we buy provisioned throughput for our LLM workloads?" | Traffic shape analysis, break-even utilization calculator, provider comparison (Bedrock vs Vertex vs Azure OpenAI) |
| "Our dev team's Cursor/Copilot/Claude Code spend is out of control" | Billing model comparison (seat+usage vs BYOK), per-tool cost profiles, attribution via LiteLLM proxy |
| "Our LLM bills doubled but usage looks flat" | Context-length pricing threshold detection (the 200K token cliff that doubles input cost), prompt caching strategies |
| "We want AI to automate our FinOps processes" | Advisory-to-autonomous maturity spectrum, tool landscape, guardrails for automated actions |

### Cloud provider optimization

| You say... | The skill provides... |
|---|---|
| "We're spending $500K/month on AWS and don't know where it goes" | CUR setup, Cost Explorer configuration, 128 optimization patterns, cost allocation by account structure |
| "Should we buy Reserved Instances or Savings Plans?" | Commitment decision trees, instrument layering (Spot → Compute SP → EC2 SP → RI), portfolio liquidity analysis |
| "We're negotiating an AWS EDP" | EDP preparation roadmap, growth commitment analysis, internal alignment requirements |
| "We haven't enabled Azure Hybrid Benefit" | AHB activation guide — free savings, no commitment, immediate effect. Do this before any other Azure optimization |
| "Our Azure bill spiked after EA-to-MCA migration" | EA-to-MCA transition checklist, FinOps Toolkit migration paths, billing scope changes |
| "Our Bedrock/Claude API costs are higher than expected" | Model pricing comparison, batch inference discounts (50% off), Fast mode 6× multiplier, long-context pricing cliffs |
| "We're evaluating Azure OpenAI PTUs vs pay-as-you-go" | PTU pool model, spillover mechanics, break-even analysis (GPT-5 provisioned is +67% even at 100% utilization) |

### Infrastructure & platforms

| You say... | The skill provides... |
|---|---|
| "We can't attribute costs to teams on shared Kubernetes" | Namespace and label attribution patterns, OpenCost vs Kubecost comparison, shared cost distribution models |
| "Our Lambda costs seem disproportionate" | Hidden cost iceberg (API Gateway, NAT, CloudWatch often exceed compute), memory rightsizing, ARM/Graviton migration (20-30% savings) |
| "Kafka cross-AZ costs dominate our MSK bill" | Cross-AZ replication cost trap (80-90% of total cost), tiered storage, compression strategies |
| "Should we migrate from Redis to Valkey?" | Zero-downtime migration path, 20-33% cost savings on AWS, full API compatibility, migration checklist |
| "Elasticsearch costs grow linearly with data volume" | Data tiering (UltraWarm = 90% cheaper than hot), index lifecycle policies, shard sizing |
| "Databricks/Snowflake costs are hard to control" | 18 Databricks patterns + 13 Snowflake patterns, credit model fundamentals, hidden cost categories |

### Governance & multi-cloud

| You say... | The skill provides... |
|---|---|
| "We use AWS + Azure + GCP but can't compare costs" | FOCUS specification for unified billing, terminology normalization table, cross-cloud commitment comparison |
| "Our tagging compliance is below 60%" | 5-tag minimum taxonomy, three enforcement layers (IaC prevention, detection, remediation), maturity progression |
| "We're starting FinOps from scratch" | 2026 framework (4 domains, 23 capabilities, 6 personas), maturity assessment, Crawl-first priorities |
| "Leadership wants our cloud carbon footprint" | Carbon measurement tools, low-carbon region selection, GHG Protocol reporting, Carbon Aware SDK |

### SaaS & licensing

| You say... | The skill provides... |
|---|---|
| "We suspect significant SaaS overlap and shadow IT" | Six sprawl patterns, multi-method discovery (SSO, financial records, CASB, browser extensions), SMP vendor comparison |
| "ITAM and FinOps teams need to work together" | Joint operating model, RACI, Tier 1 vendor management (Microsoft, AWS, Oracle, Salesforce) |
| "We're not leveraging BYOL on cloud" | BYOL mechanics (Azure Hybrid Benefit, AWS Licence Manager, Oracle on cloud), marketplace governance |

### Multi-domain scenarios

| You say... | References loaded together |
|---|---|
| "Starting a FinOps practice from scratch" | Framework + tagging + methodology |
| "Unified view of cloud + AI + SaaS spend" | Multi-cloud + FOCUS + SaaS management |
| "Present AI ROI to the board" | AI costs + AI value management + provider-specific |
| "GPU workloads for ML on Kubernetes are expensive" | Kubernetes + AI costs + provider-specific |
| "Optimize everything — where do we start?" | Framework (assess maturity first) → provider-specific + tagging |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/cloud-finops
```

## How to Use

**Direct invocation:**

```
Use the cloud-finops skill to analyze our AWS commitment strategy
```

```
Use the cloud-finops skill to help us set up AI cost attribution
```

```
Use the cloud-finops skill to compare provisioned vs on-demand for our Bedrock workloads
```

**Natural language triggers** — Claude activates this skill automatically when you mention:

`finops` · `cloud cost` · `cost optimization` · `aws cost` · `azure cost` · `gcp cost` · `kubernetes cost` · `serverless cost` · `multi-cloud` · `commitment strategy` · `rightsizing` · `tagging governance`

## What's Inside

**26 reference files** organized into 6 domains (~10,500 lines of practitioner guidance):

### AI & GenAI (5 files)
- **AI cost management** — LLM economics, agentic cost patterns, six anti-patterns, four-phase implementation, harness cost mapping
- **AI investment governance** — AI Investment Council, stage gates, incremental funding, value metrics
- **GenAI capacity planning** — provisioned vs shared capacity, traffic shape analysis, spillover, cross-provider comparison
- **AI coding tools** — Cursor, Claude Code, Copilot, Windsurf, Codex billing models, BYOK attribution, LiteLLM proxy
- **AI-powered FinOps** — anomaly detection, automated rightsizing, NL cost querying, advisory-to-autonomous spectrum

### Cloud Providers (8 files)
- **AWS** — CUR, Cost Explorer, 128 optimization patterns, commitment decision trees, EDP negotiation, RDS strategy (~2,240 lines)
- **Azure** — AHB, reservations, Savings Plans, 48 optimization patterns, MACC, EA-to-MCA transition (~1,560 lines)
- **GCP** — 26 optimization patterns across Compute Engine, Cloud SQL, GCS, BigQuery, networking
- **OCI** — 6 patterns for compute, storage, networking
- **AWS Bedrock** — model pricing, provisioned throughput, batch inference, CloudWatch metrics
- **Azure OpenAI** — PTU reservations, spillover mechanics, GPT model pricing, prompt caching
- **Anthropic** — Claude Opus/Sonnet/Haiku pricing, Fast mode, long-context cliffs, Batch API
- **Vertex AI** — Gemini pricing, provisioned throughput, batch prediction

### Infrastructure & Platforms (5 files)
- **Kubernetes** — cost model, OpenCost/Kubecost, attribution patterns, pod rightsizing, GPU optimization, provider comparison
- **Serverless** — Lambda/Functions/Cloud Run billing, memory rightsizing, hidden cost iceberg, ARM migration
- **Data platforms** — Kafka cross-AZ cost trap, OpenSearch data tiering, Redis-to-Valkey migration (20-33% savings)
- **Databricks** — 18 optimization patterns, cluster segmentation, Photon governance
- **Snowflake** — credit model, hidden costs (time travel, auto-clustering), 13 optimization patterns

### Cross-Cutting (5 files)
- **Multi-cloud** — terminology normalization, cross-cloud commitment strategy, unified cost allocation
- **FOCUS specification** — v1.3 billing data standard, provider support matrix, adoption guidance
- **Tagging** — 5-tag taxonomy, IaC enforcement, virtual tagging, MCP automation
- **FinOps framework** — 2026 version with Scopes, Technology Categories, 23 capabilities, converging disciplines
- **GreenOps** — carbon measurement, carbon-aware workloads, low-carbon regions, GHG Protocol

### SaaS & Licensing (2 files)
- **SaaS management** — six sprawl patterns, discovery methods, licence optimization, SMP landscape
- **ITAM** — BYOL mechanics, marketplace governance, vendor co-management, consumption monitoring

### Methodology (1 file)
- **OptimNow methodology** — reasoning philosophy, four pillars, engagement principles (loaded on every query as a reasoning lens)

## Version History

- `2.1.0` Added comprehensive use-case guide to README, fixed SKILL.md to be lean LLM instructions only
- `2.0.0` Major expansion: 6 new reference files (Kubernetes, serverless, data platforms, multi-cloud, FOCUS, AI automation), framework updated to 2026, coauthorship added
- `1.0.0` Initial release by OptimNow

## Related Skills

- **[Cicd Pipelines](../cicd-pipelines/)** — CI/CD pipeline design, DevOps automation, infrastructure as code
- **[Docker Containerization](../docker-containerization/)** — Docker basics, multi-stage builds, Compose orchestration
- **[Workflow Automation](../workflow-automation/)** — CI/CD pipelines, multi-agent orchestration, parallel task execution

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — 50 production-grade plugins for Claude Code.
