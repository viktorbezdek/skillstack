# Cloud FinOps

> **v2.1.0** | DevOps & Infrastructure | 3 iterations

Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, AI-powered FinOps automation, cloud billing (AWS, Azure, GCP, OCI), Kubernetes/container FinOps, serverless FinOps, data platform FinOps (Kafka, OpenSearch, Redis/Valkey), multi-cloud normalization (FOCUS specification), commitment strategy, tagging governance, SaaS asset management, ITAM, and GreenOps. Includes 26 domain-specific reference files grounded in enterprise delivery experience. Built by OptimNow and Viktor Bezdek, licensed CC BY-SA 4.0.

## What Problem Does This Solve

> Built by [OptimNow](https://optimnow.io) (James Barney) and [Viktor Bezdek](https://github.com/viktorbezdek). Grounded in hands-on enterprise delivery, not abstract frameworks.

Organizations struggle to manage technology spend across cloud providers, AI workloads, SaaS subscriptions, containers, serverless functions, and data platforms. This skill provides structured, practitioner-tested guidance for the full FinOps lifecycle: visibility, allocation, optimization, and governance across all technology cost surfaces.

## When to Use This Skill

Use this skill when you face any of these situations:

**AI costs are growing or unpredictable**
- "Our LLM feature costs doubled but usage is flat" → detects context-length pricing cliffs, agentic retry loops
- "We need to justify AI investment to the board" → AI Investment Council model, stage-gate funding, ROI framework
- "Dev team AI tool spend (Cursor, Copilot, Claude Code) is uncontrolled" → billing model comparison, BYOK attribution

**Cloud bill needs attention**
- "We're spending $500K/month on AWS and don't know where it goes" → 128 optimization patterns, CUR setup, cost allocation
- "Should we buy Reserved Instances or Savings Plans?" → commitment decision trees, layering strategy, portfolio liquidity
- "Azure Hybrid Benefit isn't enabled anywhere" → immediate free savings, no commitment required

**Infrastructure costs are unclear**
- "We can't attribute costs to teams on shared Kubernetes" → namespace/label attribution, OpenCost/Kubecost setup
- "Lambda costs seem disproportionate" → hidden cost iceberg (API Gateway, NAT, logs often exceed compute)
- "Kafka cross-AZ costs are 80% of our MSK bill" → replication optimization, tiered storage, compression

**Governance and multi-cloud**
- "We use AWS + Azure + GCP but can't compare" → FOCUS specification for unified billing, terminology normalization
- "Tagging compliance is below 60%" → 5-tag minimum taxonomy, IaC enforcement, maturity progression
- "We're starting FinOps from scratch" → 2026 framework, maturity assessment, phased approach

**SaaS and licensing**
- "We suspect significant SaaS overlap and shadow IT" → six sprawl patterns, multi-method discovery
- "BYOL savings aren't being captured on cloud" → Azure Hybrid Benefit, AWS Licence Manager mechanics

## How to Use

**Direct invocation:**

```
Use the cloud-finops skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `finops`
- `cloud-cost`
- `cost-optimization`
- `aws`
- `azure`
- `gcp`
- `kubernetes cost`
- `serverless cost`
- `multi-cloud`

## What's Inside

- **How to use this skill** -- domain routing table for 26 reference files
- **Core FinOps principles** (2026 framework, always apply)
- **The three phases** (Inform → Optimize → Operate)
- **Maturity model quick reference**
- **26 reference files** covering:
  - AI & GenAI (5 files): AI costs, investment governance, capacity planning, dev tools, AI automation
  - Cloud Providers (7 files): AWS, Azure, GCP, OCI, Bedrock, Azure OpenAI, Anthropic, Vertex AI
  - Infrastructure & Platforms (5 files): Kubernetes, serverless, Kafka/OpenSearch/Redis, Databricks, Snowflake
  - Cross-Cutting (4 files): multi-cloud, FOCUS specification, tagging, GreenOps
  - SaaS & Licensing (2 files): SaaS management, ITAM
  - Methodology (2 files): OptimNow methodology, FinOps framework

## Version History

- `2.1.0` Added comprehensive use-case guide with 35+ real-world scenarios mapped to specific references, practical "when to use" examples for all 6 domain areas, multi-reference scenario combinations
- `2.0.0` Major expansion: 6 new reference files (Kubernetes, serverless, data platforms, multi-cloud, FOCUS, AI automation), framework updated to 2026 (Scopes, Technology Categories, Executive Strategy Alignment capability), improved domain routing, coauthorship added
- `1.0.0` Initial release by OptimNow

## Related Skills

- **[Cicd Pipelines](../cicd-pipelines/)** -- Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise ...
- **[Docker Containerization](../docker-containerization/)** -- Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration...
- **[Git Workflow](../git-workflow/)** -- Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file gro...
- **[Workflow Automation](../workflow-automation/)** -- Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution,...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
