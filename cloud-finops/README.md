# Cloud FinOps

> **v2.1.0** | Expert FinOps guidance covering cloud, AI, SaaS, and adjacent technology spend -- AWS, Azure, GCP, OCI, Kubernetes, serverless, data platforms, AI cost management, multi-cloud normalization, tagging, SaaS management, ITAM, and GreenOps.
> 1 skill | 26 references | 13 trigger evals, 3 output evals | Built by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) | CC BY-SA 4.0

## The Problem

Cloud bills grow faster than the businesses they serve. A typical enterprise discovers that 30% of cloud spend is waste -- idle instances, oversized resources, unattached storage volumes, and commitments that no longer match workloads. But the waste is invisible because cost data is fragmented across providers, allocation is incomplete (less than 50% of spend tagged to owners), and the people who make architecture decisions never see the bill.

AI makes this worse, not better. GenAI workloads introduce entirely new cost dimensions: token-based billing, provisioned throughput units, GPU instance hours, and model inference costs that scale with usage in unpredictable ways. A team that spins up Bedrock provisioned throughput for a demo and forgets to shut it down burns thousands per week. AI coding tools like Cursor, Claude Code, and Copilot add seat-based and usage-based costs that nobody tracks. The FinOps Foundation estimates that AI costs will exceed traditional compute costs for many organizations by 2027, yet most FinOps practices have no playbook for managing them.

The organizational gap is equally damaging. Engineering sees cost as someone else's problem. Finance sees infrastructure as a black box. Neither speaks the other's language. Without a framework that connects technical decisions to business outcomes, cost optimization devolves into periodic fire drills -- quarterly reviews that produce spreadsheets, not action.

## The Solution

This plugin provides expert FinOps guidance grounded in hands-on enterprise delivery, not abstract frameworks. It covers cloud providers (AWS, Azure, GCP, OCI), AI cost management (Bedrock, Azure OpenAI, Vertex AI, Anthropic, AI coding tools), Kubernetes and container FinOps, serverless optimization, data platforms (Kafka, OpenSearch, Redis/Valkey, Databricks, Snowflake), multi-cloud normalization (FOCUS specification), commitment strategy (RIs, Savings Plans, CUDs), tagging governance, SaaS management, ITAM, and GreenOps.

The skill ships with 26 domain-specific reference files totaling over 7,500 lines of actionable guidance. Every reference is built from real enterprise engagements -- AWS commitment portfolios, Azure reservation strategies, Kubernetes cost attribution models, and AI capacity planning frameworks. The reasoning methodology (from OptimNow) diagnoses before prescribing, connects every recommendation to business value, and progresses from quick wins to structural changes.

The result is not a cost-cutting exercise but a FinOps practice: continuous optimization that treats technology spend as a driver of business value rather than an expense to minimize.

## Context to Provide

FinOps advice is only as actionable as the cost data behind it. The more specific you are about spend figures, service breakdown, and organizational context, the more precise the recommendations will be.

**What information to include in your prompt:**

- **Cloud providers and monthly spend**: Which providers? Approximate monthly total by provider (e.g., "$180K/month: AWS 70%, Azure 25%, GCP 5%")
- **Top services by spend**: The 5-10 largest cost line items from your Cost Explorer or billing console (e.g., "EC2 $45K, RDS $28K, S3 $12K, Data Transfer $8K")
- **Tagging and allocation completeness**: What percentage of spend has cost allocation tags? How is the rest allocated?
- **Commitment coverage**: Do you have Reserved Instances, Savings Plans, or Committed Use Discounts? What percentage of your fleet do they cover?
- **FinOps maturity**: Do you have continuous cost monitoring? Automated anomaly detection? Per-team cost visibility?
- **Workload characteristics**: Which workloads are steady-state vs. variable? What is typical CPU/memory utilization for your largest instances?
- **AI and SaaS spend**: If relevant, describe your AI inference spend (which models, real-time vs batch, approximate tokens/month) and SaaS subscription count
- **Organizational context**: How many teams? Does engineering see cost data? Who owns the FinOps function?

**What makes results better:**
- Sharing actual spend numbers ("EC2 is $45K/month with 35% average utilization from CloudWatch") enables rightsizing analysis with concrete savings estimates
- Describing a specific bill increase ("AWS jumped 40% this quarter, I think it's EC2 but I'm not sure") enables root cause investigation with specific diagnostic steps
- Specifying risk tolerance ("we cannot afford downtime, prefer no-upfront commitments") calibrates the commitment strategy recommendation
- Describing your AI workload precisely ("60% real-time inference with Bedrock Sonnet, 40% batch jobs running overnight") enables model routing and batch inference optimization

**What makes results worse:**
- "Save money on cloud" without any spend data -- the skill cannot estimate savings or prioritize without cost visibility
- Requesting commitment strategy before rightsizing -- buying RIs for oversized instances locks in waste
- Treating AI cost like compute cost -- token-based billing requires different optimization levers (prompt caching, model routing, batch inference) not instance rightsizing

**Template prompt:**
```
[Investigate / Optimize / Design strategy for] our [AWS / Azure / GCP / multi-cloud] spend. Monthly total: $[amount]. Top services: [list with spend amounts]. Tagging compliance: [%]. Commitment coverage: [none / partial / describe]. Workload mix: [% steady-state vs variable]. Average utilization: [if known]. Problem to solve: [bill spike / no visibility / need commitment strategy / AI costs / SaaS sprawl]. Risk tolerance: [low / medium / high -- prefer no-upfront / OK with 1-year / OK with 3-year].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| 30% of cloud spend is unidentified waste | Systematic rightsizing, commitment strategy, and waste elimination across all providers |
| AI costs are invisible -- no one tracks token spend or provisioned throughput waste | AI cost management playbook: LLM economics, capacity planning, coding tool optimization |
| Tagging compliance below 60% -- most spend unallocated | Tagging governance framework with IaC enforcement reaching 90%+ compliance |
| Commitment strategy is ad hoc -- buying RIs without analysis | Portfolio liquidity approach: phased purchasing, coverage targets, cross-provider normalization |
| SaaS sprawl -- shadow IT subscriptions nobody tracks | SaaS asset management: discovery, license optimization, renewal governance |
| Cost reviews are quarterly fire drills | Continuous FinOps: automated anomaly detection, distributed accountability, real-time dashboards |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install cloud-finops@skillstack
```

### Verify installation

After installing, test with:

```
Our AWS bill jumped 40% this quarter -- help me investigate and find the biggest optimization opportunities
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Assess our cloud FinOps maturity -- we're on AWS with about 60% tagging compliance and no commitment strategy`
3. The skill assesses your maturity level (likely Crawl) and recommends a phased approach: visibility first, then optimization
4. Follow up: `What are the quick wins we can implement this week to cut AWS spend?`
5. Go deeper: `Design a commitment strategy for our EC2 fleet -- we have a mix of steady-state and variable workloads`

---

## System Overview

```
+------------------------------------------------------------------------+
|                         cloud-finops skill                              |
+------------------------------------------------------------------------+
|                                                                         |
|  Cloud Providers            AI & GenAI              Infrastructure      |
|  +------------------+       +------------------+    +----------------+  |
|  | AWS (2240 lines) |       | AI Costs         |    | Kubernetes     |  |
|  | Azure (1560 lines)|      | GenAI Capacity   |    | Serverless     |  |
|  | GCP              |       | AI Dev Tools     |    | Data Platforms |  |
|  | OCI              |       | AI Automation    |    | Databricks     |  |
|  | Bedrock          |       | AI Value Mgmt    |    | Snowflake      |  |
|  | Azure OpenAI     |       | Anthropic        |    +----------------+  |
|  | Vertex AI        |       +------------------+                        |
|  +------------------+                                                   |
|                                                                         |
|  Cross-Cutting              SaaS & Licensing        Methodology         |
|  +------------------+       +------------------+    +----------------+  |
|  | Multi-Cloud      |       | SaaS Management  |    | OptimNow       |  |
|  | FOCUS Spec       |       | ITAM             |    | FinOps Framework|  |
|  | Tagging          |       +------------------+    | GreenOps       |  |
|  +------------------+                               +----------------+  |
|                                                                         |
|  26 domain-specific reference files | ~7,500 lines of guidance          |
+------------------------------------------------------------------------+
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `cloud-finops` | Skill | Core FinOps methodology with domain routing table and reasoning sequence |

### References (26 files)

| Reference | Domain | Topic |
|---|---|---|
| `optimnow-methodology.md` | Methodology | OptimNow reasoning philosophy, 4 pillars, engagement principles |
| `finops-framework.md` | Methodology | FinOps Foundation framework (2026): capabilities, personas, domains, scopes |
| `finops-for-ai.md` | AI & GenAI | AI cost management, LLM economics, agentic patterns, ROI framework |
| `finops-ai-value-management.md` | AI & GenAI | AI Investment Council, stage gates, incremental funding |
| `finops-genai-capacity.md` | AI & GenAI | Provisioned vs shared capacity, traffic shape, spillover, waste types |
| `finops-ai-dev-tools.md` | AI & GenAI | Cursor, Claude Code, Copilot, Windsurf, Codex billing models and optimization |
| `finops-ai-automation.md` | AI & GenAI | AI-powered FinOps, anomaly detection, NL cost querying |
| `finops-aws.md` | Cloud Providers | AWS: 128 optimization patterns, commitment decision trees, CUR, EDP negotiation |
| `finops-bedrock.md` | Cloud Providers | AWS Bedrock billing, provisioned throughput, batch inference |
| `finops-azure.md` | Cloud Providers | Azure: 48 optimization patterns, reservations, Savings Plans, AHB |
| `finops-azure-openai.md` | Cloud Providers | Azure OpenAI PTU reservations, GPT pricing, spillover patterns |
| `finops-anthropic.md` | Cloud Providers | Claude API pricing, prompt caching, Batch API, long-context pricing |
| `finops-gcp.md` | Cloud Providers | GCP: 26 optimization patterns for Compute Engine, Cloud SQL, GCS |
| `finops-vertexai.md` | Cloud Providers | Vertex AI billing, Gemini pricing, provisioned throughput |
| `finops-oci.md` | Cloud Providers | OCI: 6 optimization patterns for compute, storage, networking |
| `finops-kubernetes.md` | Infrastructure | Kubernetes cost model, OpenCost, Kubecost, pod rightsizing, GPU |
| `finops-serverless.md` | Infrastructure | Lambda/Functions/Cloud Run billing, memory rightsizing, cold starts |
| `finops-data-platforms.md` | Infrastructure | Kafka/MSK, OpenSearch, Redis-to-Valkey migration |
| `finops-databricks.md` | Infrastructure | 18 optimization patterns for clusters, jobs, Spark |
| `finops-snowflake.md` | Infrastructure | Credit model, 13 optimization patterns for warehouses and queries |
| `finops-multi-cloud.md` | Cross-Cutting | Cross-cloud commitment strategy, unified cost allocation |
| `finops-focus.md` | Cross-Cutting | FOCUS spec v1.3: billing normalization, core columns, adoption |
| `finops-tagging.md` | Cross-Cutting | Tagging strategy, IaC enforcement, virtual tagging |
| `finops-sam.md` | SaaS & Licensing | SaaS discovery, license optimization, renewal governance |
| `finops-itam.md` | SaaS & Licensing | BYOL, marketplace governance, FinOps-ITAM collaboration |
| `greenops-cloud-carbon.md` | Sustainability | Carbon measurement, carbon-aware workloads, GHG Protocol |

### Component Spotlights

#### cloud-finops (skill)

**What it does:** Activates on any query about technology cost, cloud billing, commitment management, rightsizing, cost allocation, AI costs, SaaS spend, container cost attribution, or connecting spend to business value. Routes to the appropriate domain reference(s) and applies the OptimNow reasoning methodology.

**Input -> Output:** A cost question, bill analysis request, or optimization challenge -> Diagnosis of current state, prioritized recommendations (quick wins first, structural changes second), specific actions with business value connection.

**When to use:**
- Investigating a cloud bill increase
- Designing commitment strategy (RIs, Savings Plans, CUDs)
- Managing AI and GenAI costs (LLM inference, provisioned throughput, coding tools)
- Optimizing Kubernetes, serverless, or data platform spend
- Building tagging governance and cost allocation
- Managing SaaS subscriptions and license compliance
- Multi-cloud cost normalization with FOCUS specification
- Carbon footprint reduction (GreenOps)

**When NOT to use:**
- Building CI/CD pipelines or infrastructure -> use `cicd-pipelines`
- Writing Terraform or Kubernetes manifests -> use `cicd-pipelines`
- Designing cloud architecture from scratch -> this skill optimizes existing spend

**Try these prompts:**

```
Our AWS bill is $180K/month and growing 15% quarterly. Top services: EC2 $85K (35% avg utilization from CloudWatch), RDS $32K, Data Transfer $18K, S3 $12K. No Savings Plans. Tagging compliance 65%. We need to cut spend by 20% without disrupting production. Where do we start?
```

```
We're spending $12K/month on AI inference: Bedrock Claude Sonnet $7K (real-time customer chat, ~200M tokens/month), Azure OpenAI GPT-4 $5K (document summarization, running synchronously). Help me optimize without reducing quality. I can tolerate up to 2-second latency increase for the summarization workload.
```

```
Build a commitment strategy for our multi-cloud environment -- $150K/month: AWS $90K (60%), Azure $45K (30%), GCP $15K (10%). On AWS, 70% of EC2 is steady-state, 30% variable. No commitments on any cloud yet. Risk tolerance: prefer 1-year no-upfront on AWS, open to 3-year for specific RDS instances.
```

```
Our EKS clusters cost $60K/month across 5 teams and 40 namespaces. Average utilization: 38% CPU, 52% memory. Teams over-request because there is no chargeback -- cost is invisible to them. Design a governance framework that creates accountability without disrupting their workflows.
```

```
We have 200+ SaaS subscriptions across 8 departments. Finance only tracks 60 of them. Estimated annual spend: $800K but we genuinely don't know. 30-40% may be unused or duplicated. We have no SaaS management process. How do we discover, audit, and rationalize the portfolio?
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Save money on cloud" | "Our AWS EC2 spend is $45K/month with 35% average utilization. Recommend rightsizing and commitment strategy." |
| "AI costs are high" | "We're spending $8K/month on Claude API calls. 60% is Opus, 30% Sonnet, 10% Haiku. Where should we optimize?" |
| "Fix our tagging" | "Tagging compliance is 55% across 3 AWS accounts. We need a governance framework to reach 90% within 6 months." |
| "Use FinOps" | "Assess our FinOps maturity. We have no commitment strategy, ~70% cost allocation, monthly manual reviews, and no anomaly detection." |

### Structured Prompt Templates

**For bill investigation:**
```
Our [provider] bill increased [percentage] this [period]. Current spend: $[amount]/month. Key services: [list top 5 by spend]. Help me find the root cause and the biggest optimization opportunities.
```

**For commitment strategy:**
```
Design a commitment strategy for [provider]. Our workload: [steady-state %] is predictable, [variable %] fluctuates. Current commitment coverage: [%]. Budget: $[amount]/month. Risk tolerance: [low/medium/high].
```

**For AI cost management:**
```
Our AI costs: $[amount]/month across [services]. Models used: [list]. Usage pattern: [batch/real-time/mixed]. Help me optimize without reducing quality. I'm willing to accept [constraints].
```

### Prompt Anti-Patterns

- **Optimizing without visibility**: "Cut our cloud bill by 30%" -- you cannot optimize what you cannot measure. The skill first assesses whether you have adequate cost allocation and tagging before recommending optimizations.
- **Committing to waste**: "Buy Reserved Instances for everything" -- if 30% of your fleet is waste (idle or oversized), buying commitments locks in waste. The skill recommends rightsizing before committing.
- **Treating AI like compute**: "Right-size our LLM instances" -- AI costs are primarily token-based, not instance-based. The skill uses AI-specific optimization levers: prompt caching, model routing, batch inference, and provisioned throughput management.

## Real-World Walkthrough

**Starting situation:** You are a platform engineering lead at a mid-size SaaS company. Monthly cloud spend is $320K across AWS (primary) and Azure (secondary). The CFO has asked for a 20% cost reduction without impacting performance. You have no FinOps practice -- cost reviews happen quarterly as spreadsheet exercises.

**Step 1: Maturity assessment.** You ask: "Assess our FinOps maturity. We spend $320K/month on AWS and Azure. Tagging compliance is about 60%. No commitment strategy. Quarterly manual reviews. No anomaly detection." The skill assesses: Crawl maturity. At this level, you need visibility before optimization. Recommending commitment discounts with 60% allocation is premature -- you risk committing to waste.

**Step 2: Quick wins (Week 1).** You ask: "What can we do this week to start saving?" The skill identifies immediate actions: (1) identify and terminate idle resources -- unattached EBS volumes, stopped EC2 instances with EBS still attached, idle RDS instances, unused Elastic IPs. Typical savings: 5-8% of total spend. (2) Enable AWS Cost Explorer and Azure Cost Management with daily exports. (3) Tag the top 20 resources by spend manually while building the governance framework.

**Step 3: Tagging governance (Month 1).** You ask: "Get our tagging from 60% to 90%." The skill designs a tagging framework: mandatory tags (cost-center, team, environment, service), enforced through IaC (Terraform tag validation), with a virtual tagging fallback for legacy resources. SCP policies prevent launching untagged resources. Monthly compliance reporting to team leads. Target: 80% in 30 days, 90% in 90 days.

**Step 4: Rightsizing (Month 2).** With visibility established, you ask: "Right-size our EC2 fleet." The skill analyzes utilization patterns and categorizes: steady-state workloads (consistent 60%+ utilization) are candidates for commitments after rightsizing, variable workloads belong on smaller instances with auto-scaling, and truly idle resources should be terminated. Right-sizing recommendations typically save 20-30% on compute.

**Step 5: Commitment strategy (Month 3).** After rightsizing, you ask: "Design our commitment portfolio." The skill recommends a phased approach: start with 1-year no-upfront Savings Plans covering 60% of steady-state compute (conservative to maintain liquidity), add specific RI coverage for predictable RDS instances, and leave variable workloads on demand. Expected savings: 25-35% on committed workloads. The skill emphasizes portfolio liquidity -- avoid 3-year all-upfront commitments that lock you in.

**Step 6: AI cost management.** You mention AI costs are growing. The skill asks about your AI workloads and discovers: $15K/month on Bedrock, $8K/month on Azure OpenAI. It recommends: prompt caching for repeated prefixes (30-40% savings on Bedrock), model routing (Haiku for classification tasks instead of Sonnet), and batch inference for non-real-time workloads (50% discount).

**Final result:** Total savings identified: ~$85K/month (26.5%). Breakdown: idle resource elimination ($18K), rightsizing ($45K), AI optimization ($8K), commitment discounts to come ($14K+ when purchased in Month 3). The CFO's 20% target is exceeded, and the savings are sustainable because they come from structural changes, not one-time cuts.

**Gotchas discovered:** The initial rightsizing recommendation for an RDS instance was too aggressive -- it was a database with nightly batch jobs that spiked to 90% utilization for 2 hours. The skill's methodology caught this during utilization pattern analysis, recommending a moderate right-size that handled the batch peak.

## Usage Scenarios

### Scenario 1: Managing AI coding tool costs

**Context:** Your engineering team of 50 uses Cursor (30 seats), Claude Code (15 seats), and Copilot (5 seats). Monthly cost: $4,200. Management wants to know if this is justified.

**You say:** "We spend $4,200/month on AI coding tools across Cursor, Claude Code, and Copilot. Help me optimize without reducing developer productivity."

**The skill provides:**
- Per-tool cost breakdown and usage analysis framework
- Seat utilization metrics: active users vs. licensed seats
- Model routing recommendations (use Haiku/Flash for autocomplete, Sonnet/Opus for complex tasks)
- Consolidation analysis: can you standardize on fewer tools?
- ROI framework: developer time saved vs. tool cost

**You end up with:** A recommendation to reclaim 8 unused Cursor seats ($160/month), route simple completions to cheaper models ($300/month savings), and a dashboard tracking developer adoption and productivity impact.

### Scenario 2: Multi-cloud commitment strategy

**Context:** You run 60% AWS, 30% Azure, 10% GCP. Each cloud has different commitment mechanisms and your finance team wants a unified view.

**You say:** "Design a unified commitment strategy across AWS, Azure, and GCP. We want maximum savings with the flexibility to shift workloads between clouds."

**The skill provides:**
- Cross-cloud commitment comparison: AWS Savings Plans vs Azure Reservations vs GCP CUDs
- Portfolio approach: conservative coverage (60% of steady-state per cloud) with room for migration
- FOCUS specification adoption for unified billing normalization
- Quarterly review cadence with rebalancing triggers

**You end up with:** A commitment portfolio that saves 25-30% across all three clouds while maintaining the flexibility to shift 15-20% of workload between providers without penalty.

### Scenario 3: Kubernetes cost attribution

**Context:** Your Kubernetes clusters run 40 services across 5 teams. Nobody knows which team is responsible for what portion of the $60K/month cluster cost.

**You say:** "We can't attribute our $60K/month Kubernetes cost to teams. Design a cost allocation model with namespace-level attribution."

**The skill provides:**
- OpenCost or Kubecost deployment for pod-level cost attribution
- Namespace-to-team mapping with label-based allocation
- Resource request vs. actual usage analysis (over-requesting is the main waste driver)
- Chargeback vs. showback recommendation based on organizational maturity
- Pod rightsizing recommendations based on actual usage

**You end up with:** Per-team cost dashboards, identification of $18K/month in over-provisioned resources, and a governance framework where teams own their resource requests.

---

## Decision Logic

**When to use Savings Plans vs Reserved Instances?**

The skill follows a clear hierarchy: Savings Plans first (they are more flexible, covering any instance type within a compute family), RIs second (for specific, unchanging workloads where the deeper discount justifies the inflexibility), and CUDs for GCP equivalents. Savings Plans at 60-70% coverage of steady-state is the starting recommendation; RIs are added for predictable database workloads.

**How does the skill route across 26 reference files?**

The skill body contains a routing table that maps query topics to specific references. AI cost queries route to `finops-for-ai.md`, AWS billing routes to `finops-aws.md`, Kubernetes routes to `finops-kubernetes.md`. Multi-domain queries load multiple references. The OptimNow methodology (`optimnow-methodology.md`) is applied to every response as a reasoning lens.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Committing before rightsizing | Locked into paying for oversized instances for 1-3 years | Right-size first; start with short-term (1-year) no-upfront commitments; maintain portfolio liquidity |
| Tagging without enforcement | Compliance rises temporarily then decays as new resources are created untagged | Enforce via SCP policies and IaC validation; automate compliance reporting |
| Optimizing AI by reducing quality | Cheaper model produces worse results; users bypass the system | Model routing based on task complexity, not blanket downgrades; measure quality alongside cost |
| Ignoring shared costs | 40% of spend (networking, support, shared services) is unallocated | Define allocation methodology: proportional by usage, equal split, or custom rules per category |

## Ideal For

- **Platform engineering teams managing cloud spend** who need systematic optimization across providers with actionable recommendations
- **FinOps practitioners building or maturing a FinOps practice** who need the framework, maturity model, and domain-specific guidance in one skill
- **Engineering managers with AI cost concerns** who need to understand and optimize LLM inference, AI coding tools, and provisioned throughput costs
- **Finance teams working with engineering** who need a shared vocabulary and framework for connecting technology spend to business outcomes

## Not For

- **Building cloud infrastructure** -- this skill optimizes costs on existing infrastructure. For building pipelines and deploying resources, use `cicd-pipelines`.
- **Application architecture decisions** -- choosing between serverless and containers for functionality reasons, not cost. Use language-specific development skills.
- **One-time cost audits** -- this skill builds a continuous practice, not a point-in-time report. If you just need a quick number, start here but expect to build ongoing processes.

## Related Plugins

- **cicd-pipelines** -- Infrastructure provisioning and deployment that this skill helps optimize
- **docker-containerization** -- Container optimization patterns that affect Kubernetes costs
- **workflow-automation** -- Automate FinOps processes like anomaly alerting and commitment reviews
- **systems-thinking** -- Understand feedback loops between engineering decisions and cost outcomes

---

*FinOps Skill by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
