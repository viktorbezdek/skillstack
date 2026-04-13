# Cloud FinOps

> **v2.1.0** | DevOps & Infrastructure | 3 iterations

> Expert FinOps guidance across cloud, AI, SaaS, containers, serverless, data platforms, and sustainability -- 26 domain-specific reference files grounded in enterprise delivery. Built by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## The Problem

Cloud bills grow faster than anyone expects. An AWS account starts at $5K/month and hits $50K/month within a year, with nobody able to explain where the money went. Development instances run 24/7 with nobody using them on weekends. Reserved instances expire without renewal because no one tracked the commitment lifecycle. Kubernetes clusters are over-provisioned by 60% because right-sizing feels risky. AI inference costs explode when the team ships a GPT-4o integration without understanding token economics. SaaS subscriptions accumulate across the organization with 30% of licenses unused and nobody tracking renewals until a surprise auto-renewal bill arrives.

FinOps knowledge is fragmented across provider-specific documentation, framework whitepapers, and consultant tribal knowledge. AWS commitment strategy differs fundamentally from Azure which differs from GCP -- but most teams manage multi-cloud environments and need consistent decision frameworks. AI cost management barely existed two years ago, and now organizations are spending six figures on LLM inference without the same maturity they have for compute costs. Data platforms (Kafka, Elasticsearch, Snowflake, Databricks) have their own cost models that traditional compute optimization does not address.

The gap is not "we need to save money" -- it is that building a mature FinOps practice requires expertise across cloud providers, AI services, containers, serverless, data platforms, SaaS licensing, tagging governance, and sustainability. No single engineer or consultant has all of this, and the landscape changes quarterly with new pricing models and commitment options.

## The Solution

This plugin provides expert FinOps guidance across every technology domain through 26 reference files grounded in hands-on enterprise delivery. It covers all major cloud providers (AWS with 128 optimization patterns, Azure with 48 patterns, GCP with 26 patterns, plus OCI), AI cost management (Anthropic, Bedrock, Azure OpenAI, Vertex AI, AI coding tools like Cursor and Claude Code), infrastructure platforms (Kubernetes with OpenCost/Kubecost, serverless Lambda/Functions/Cloud Run), data platforms (Kafka/MSK, Elasticsearch/OpenSearch, Redis/Valkey, Databricks, Snowflake), cross-cutting concerns (multi-cloud normalization via FOCUS spec, tagging governance, GreenOps), and SaaS/licensing (SAM, ITAM, shadow IT, renewal governance).

The skill applies a consistent reasoning framework to every query: diagnose before prescribing, assess maturity before recommending solutions (a "Crawl" organization needs visibility before optimization), connect cost to business value, and recommend progressively (quick wins first, structural changes second). It draws from the OptimNow methodology built on real engagement experience, not abstract frameworks.

You ask about any technology cost concern -- from "our AWS bill jumped 40% last month" to "how do I plan GenAI capacity across Azure OpenAI and Bedrock?" -- and get specific, actionable guidance grounded in the relevant domain reference, with maturity-appropriate recommendations and provider-specific implementation steps.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| AWS commitment strategy based on generic blog posts | 128 AWS optimization patterns with decision trees for compute and database commitments, portfolio liquidity strategies, phased purchasing |
| No idea what AI inference is costing or how to optimize it | Token economics, prompt caching, batch API patterns, provisioned vs shared capacity planning across Anthropic, Bedrock, Azure OpenAI, Vertex AI |
| Kubernetes clusters over-provisioned by 60% with no cost attribution | OpenCost/Kubecost patterns for pod cost attribution, namespace allocation, GPU optimization, node pool right-sizing |
| SaaS sprawl with 30% unused licenses and surprise renewal bills | SaaS asset management with discovery, license optimization, renewal governance, shadow IT detection |
| Multi-cloud cost data in incompatible formats | FOCUS specification for billing data normalization across providers, unified cost allocation |
| Optimization recommendations disconnected from business outcomes | Every recommendation linked to business value through the FinOps framework's phases and maturity model |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install cloud-finops@skillstack
```

### Verify Installation

After installing, test with:

```
Our AWS bill jumped 30% last month -- help me figure out what changed and how to optimize
```

The skill activates automatically when you mention cloud costs, FinOps, cost optimization, or specific provider billing topics.

## Quick Start

1. Install the plugin using the commands above.
2. Ask about any technology cost concern:
   ```
   We're spending $15K/month on AWS and I don't know where to start optimizing -- assess our situation
   ```
3. The skill assesses your FinOps maturity (Crawl/Walk/Run), identifies your phase (Inform/Optimize/Operate), and recommends actions appropriate to your current state.
4. Dive into specifics:
   ```
   We have 50 EC2 instances -- should we buy Reserved Instances or Savings Plans?
   ```
5. You get a provider-specific commitment decision tree with portfolio liquidity considerations and phased purchasing strategy.

## What's Inside

This is a single-skill plugin with 26 deep reference documents organized by domain, totaling over 8,000 lines of production FinOps guidance.

| Component | Purpose |
|---|---|
| **cloud-finops** skill | Core framework: FinOps principles, three phases (Inform/Optimize/Operate), maturity model, domain routing table, reasoning sequence |
| **26 reference documents** | Domain-specific deep dives (see table below) |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: cloud-finops

**What it does:** Provides expert FinOps guidance for any technology cost question. Activates when you mention cloud bills, cost optimization, commitment strategy, AI inference costs, Kubernetes cost attribution, serverless optimization, SaaS management, tagging governance, or sustainability. Applies a consistent reasoning framework: diagnose maturity first, then recommend progressively from quick wins to structural changes, always connecting cost to business value.

**Try these prompts:**

```
Our AWS EC2 spend is $40K/month with 200 instances -- design a commitment strategy using Savings Plans and Reserved Instances
```

```
We just shipped a Claude-powered feature and API costs are 3x what we budgeted -- how do we optimize Anthropic spend?
```

```
Help me set up Kubernetes cost attribution -- we have 8 teams sharing 3 EKS clusters and nobody knows who's spending what
```

```
We have 150 SaaS subscriptions across the company and at least 30% are unused -- how do we get this under control?
```

```
Design a tagging strategy for our multi-cloud environment -- AWS, Azure, and some GCP
```

**Key references by domain:**

| Domain | References |
|---|---|
| **Methodology & Framework** | `optimnow-methodology.md` (reasoning philosophy), `finops-framework.md` (FinOps Foundation 2026 framework) |
| **AI & GenAI** | `finops-for-ai.md` (AI cost management, 490 lines), `finops-ai-value-management.md` (AI investment governance), `finops-genai-capacity.md` (capacity planning), `finops-ai-dev-tools.md` (Cursor/Claude Code/Copilot costs), `finops-ai-automation.md` (AI-powered FinOps) |
| **Cloud Providers** | `finops-aws.md` (128 patterns, 2240 lines), `finops-bedrock.md`, `finops-azure.md` (48 patterns, 1560 lines), `finops-azure-openai.md`, `finops-anthropic.md`, `finops-gcp.md` (26 patterns), `finops-vertexai.md`, `finops-oci.md` |
| **Infrastructure** | `finops-kubernetes.md` (OpenCost, Kubecost, pod attribution), `finops-serverless.md` (Lambda/Functions/Cloud Run), `finops-data-platforms.md` (Kafka, OpenSearch, Redis/Valkey) |
| **Data Platforms** | `finops-databricks.md` (18 cluster/Spark patterns), `finops-snowflake.md` (13 warehouse/query patterns) |
| **Cross-Cutting** | `finops-multi-cloud.md`, `finops-focus.md` (FOCUS spec v1.3), `finops-tagging.md`, `greenops-cloud-carbon.md` |
| **SaaS & Licensing** | `finops-sam.md` (SaaS asset management), `finops-itam.md` (ITAM, BYOL, vendor negotiation) |

## Real-World Walkthrough

Your company spends $120K/month across AWS ($80K), Azure ($30K), and a growing portfolio of AI services ($10K and climbing fast). The CFO wants a 20% cost reduction plan. The engineering team just launched a customer-facing chatbot running on Claude via AWS Bedrock, and its costs doubled last month. Nobody can explain where the Kubernetes spend is going across six teams sharing four clusters. And the procurement team just discovered 47 SaaS subscriptions nobody tracks.

You start with the big picture:

```
We spend $120K/month across AWS, Azure, and AI services. The CFO wants 20% reduction. Where do I start?
```

The skill assesses your maturity. You have basic cost visibility (Cost Explorer dashboards) but no tagging strategy, no commitment management, no cost attribution for Kubernetes, and no AI cost governance. That puts you at Crawl maturity. The skill recommends starting with the Inform phase: visibility and allocation must come before optimization. Committing to Reserved Instances when 40% of your spend is unallocated means you might be committing to waste.

First, tagging. The skill references `finops-tagging.md`:

```
Design a tagging strategy for our AWS and Azure accounts -- we have 6 engineering teams and no consistent tagging
```

You get a tagging taxonomy (team, environment, service, cost-center), IaC enforcement patterns (Terraform module defaults, Azure Policy, AWS Service Control Policies), and a compliance tracking approach. The skill recommends starting with the three most impactful tags (team, environment, service) and adding more only after reaching 80% compliance on those. Virtual tagging handles resources that cannot be tagged directly.

Next, the Kubernetes attribution problem:

```
Help me set up cost attribution for our EKS clusters -- 6 teams, 4 clusters, nobody knows who's spending what
```

The skill references `finops-kubernetes.md` and designs an OpenCost deployment with namespace-based allocation (each team gets a namespace), pod-level cost attribution using resource requests, shared cost allocation for cluster overhead (control plane, monitoring, logging), and GPU cost tracking for the ML team's training workloads. The idle compute (pods requesting more CPU/memory than they use) shows up as a 55% over-provisioning rate -- the skill recommends implementing Vertical Pod Autoscaler for right-sizing before buying more capacity.

Now the AI cost spike:

```
Our Bedrock chatbot costs doubled last month -- from $5K to $10K. How do we diagnose and optimize?
```

The skill references both `finops-bedrock.md` and `finops-for-ai.md`. Diagnosis first: check CloudWatch metrics for invocation count and token throughput. The spike correlates with the chatbot launch going viral on social media -- 4x more conversations than projected. Optimization options: enable prompt caching for the system prompt (saves 90% on repeated context), implement conversation summarization to reduce context length in long chats, batch non-real-time analysis requests using Bedrock's batch inference (50% cheaper), and evaluate whether Haiku handles the simple FAQ queries (80% of traffic) while Sonnet handles only complex cases. Projected savings: 40-55% reduction, bringing the $10K back to $5-6K even with higher traffic.

For the AWS commitment strategy:

```
Design a commitment strategy for our $80K/month AWS spend -- we have EC2, RDS, and Lambda
```

The skill references `finops-aws.md` and applies the commitment decision tree. EC2 ($45K): Compute Savings Plans for the stable baseline (70% of current usage), with on-demand for the variable portion. RDS ($20K): Reserved Instances for production databases (3 instances running 24/7), on-demand for dev/staging. Lambda ($15K): no commitment discounts available, but memory right-sizing and ARM migration (Graviton2) can cut costs 20-34%. Phased purchasing: buy 6-month commitments first to establish baseline, then convert to 1-year terms once patterns stabilize. Portfolio liquidity: maintain 15-20% on-demand headroom for flexibility.

The SaaS problem:

```
We found 47 SaaS subscriptions nobody tracks -- how do we get this under control?
```

The skill references `finops-sam.md` and designs a SaaS rationalization program: discovery (aggregate credit card, expense report, and SSO data to find all subscriptions), utilization analysis (login frequency, feature usage, API activity), optimization (eliminate unused licenses, right-size plans, consolidate overlapping tools), and governance (renewal calendar, approval workflow, automatic alerts 90 days before renewal).

After six weeks of implementing these recommendations, you report to the CFO: tagging at 82% compliance, Kubernetes right-sizing reclaiming 35% of cluster capacity, AI costs reduced 45% through prompt caching and model tiering, commitment purchases on track to save $12K/month once fully committed, and 12 SaaS subscriptions eliminated saving $3,200/month. Total reduction trajectory: 22%, exceeding the 20% target.

## Usage Scenarios

### Scenario 1: AWS commitment strategy design

**Context:** You are the FinOps lead responsible for $500K/month in AWS spend across 15 accounts. You have been buying Reserved Instances ad hoc and suspect you are overpaying.

**You say:** "Design an AWS commitment strategy for $500K/month across 15 accounts -- we have a mix of RIs and Savings Plans but no coherent strategy"

**The skill provides:**
- Commitment decision tree for compute vs. database workloads
- Portfolio liquidity analysis (what percentage should stay on-demand)
- Phased purchasing strategy (short-term first, extend as patterns stabilize)
- RI-to-Savings Plan migration path for flexibility
- EDP negotiation considerations for enterprise-scale spend

**You end up with:** A documented commitment strategy with specific recommendations per workload type, a purchasing schedule, and portfolio liquidity targets.

### Scenario 2: AI cost management for a new LLM deployment

**Context:** Your team is launching a Claude-powered feature and needs to budget and optimize AI inference costs. You have no experience with LLM cost management.

**You say:** "We're launching a Claude-powered customer support feature -- help me estimate costs, set up monitoring, and plan optimization"

**The skill provides:**
- Token economics for Anthropic models (Opus/Sonnet/Haiku pricing, input vs output)
- Cost estimation based on expected conversation volume and average tokens per interaction
- Prompt caching strategy for system prompts (90% savings on cached context)
- Model tiering: route simple queries to Haiku, complex to Sonnet
- Monitoring setup for tracking cost per conversation and cost per resolution

**You end up with:** A cost model with projections, optimization strategies that can reduce costs 40-60%, and monitoring dashboards tracking cost per business outcome.

### Scenario 3: Multi-cloud cost normalization

**Context:** Your company uses AWS, Azure, and GCP. Each team has their own dashboards and terminology. Finance wants a single cost view with consistent allocation.

**You say:** "We need unified cost reporting across AWS, Azure, and GCP -- finance can't compare costs across providers"

**The skill provides:**
- FOCUS specification (v1.3) for billing data normalization
- Core column mapping across providers (service name, resource ID, cost type)
- Unified tagging strategy that works across all three clouds
- Cross-cloud commitment strategy normalization
- Tool recommendations for multi-cloud cost platforms

**You end up with:** A FOCUS-based data normalization pipeline, consistent tagging taxonomy, and unified cost dashboards that finance can use for cross-provider comparison.

### Scenario 4: Kubernetes cost attribution and optimization

**Context:** Your platform team runs shared Kubernetes clusters for 10 product teams. Monthly cluster costs are $60K but nobody can explain per-team spend.

**You say:** "We spend $60K/month on Kubernetes with 10 teams sharing clusters -- I need per-team cost attribution and right-sizing"

**The skill provides:**
- OpenCost/Kubecost deployment and configuration for namespace-based attribution
- Shared cost allocation models for control plane, monitoring, and platform services
- Pod right-sizing analysis using resource request vs actual utilization
- Node pool optimization strategy (consolidation, spot instances, ARM nodes)
- GPU cost attribution for ML workloads

**You end up with:** Per-team cost dashboards, identified over-provisioning (typically 40-60% waste), and a right-sizing plan with projected savings.

## Ideal For

- **FinOps practitioners managing multi-cloud environments** -- 26 domain references cover AWS, Azure, GCP, OCI, Kubernetes, serverless, data platforms, AI, and SaaS with consistent methodology
- **Engineering teams launching AI features** -- AI cost management across Anthropic, Bedrock, Azure OpenAI, and Vertex AI with token economics, caching strategies, and model tiering
- **Platform teams running shared Kubernetes infrastructure** -- cost attribution patterns, pod right-sizing, GPU optimization, and namespace allocation
- **Finance teams needing cross-cloud cost visibility** -- FOCUS specification guidance, multi-cloud normalization, tagging governance, and unified reporting
- **Procurement teams managing SaaS sprawl** -- SaaS asset management with discovery, license optimization, renewal governance, and shadow IT detection

## Not For

- **Building CI/CD pipelines for cost-optimized infrastructure** -- use [cicd-pipelines](../cicd-pipelines/) for pipeline design and deployment automation
- **Docker container optimization (image size, build performance)** -- use [docker-containerization](../docker-containerization/) for Dockerfile best practices
- **Cloud architecture design (not cost-focused)** -- use cloud provider documentation for service selection and architecture patterns

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through 26 domain-specific reference files totaling over 8,000 lines.

The **SKILL.md** body provides the framework: the six FinOps principles, the three phases (Inform/Optimize/Operate), the maturity model (Crawl/Walk/Run), and the domain routing table that maps any cost query to the right reference file(s). It also defines the reasoning sequence applied to every response: load methodology, diagnose maturity, connect cost to value, recommend progressively.

The **26 reference files** are organized into six domains:

- **Methodology and Framework** (2 files): the OptimNow reasoning philosophy and the complete FinOps Foundation 2026 framework
- **AI and GenAI** (5 files): AI cost management, investment governance, capacity planning, coding tool costs, AI-powered automation
- **Cloud Providers** (8 files): AWS (2,240 lines), Azure (1,560 lines), GCP, Vertex AI, Bedrock, Azure OpenAI, Anthropic, OCI
- **Infrastructure and Platforms** (3 files): Kubernetes, serverless, data platforms (Kafka, OpenSearch, Redis)
- **Data Platforms** (2 files): Databricks and Snowflake with optimization patterns
- **Cross-Cutting and SaaS** (6 files): multi-cloud, FOCUS spec, tagging, GreenOps, SaaS management, ITAM

When you ask about AWS costs, the skill loads `finops-aws.md` (128 optimization patterns). When you ask about AI costs, it loads the relevant AI reference. Multi-domain queries load multiple references and synthesize across them.

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline design and DevOps automation for the infrastructure FinOps optimizes
- **[Docker Containerization](../docker-containerization/)** -- Container best practices that complement Kubernetes cost optimization
- **[Agent Project Development](../agent-project-development/)** -- Cost estimation framework for LLM project development

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
