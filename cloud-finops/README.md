# Cloud FinOps

> **v1.0.0** | DevOps & Infrastructure | 1 iteration

Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, cloud billing (AWS, Azure, GCP), commitment strategy, tagging governance, SaaS asset management, ITAM, and GreenOps. Includes 20 domain-specific reference files grounded in enterprise delivery experience. Built by [OptimNow](https://optimnow.io), licensed CC BY-SA 4.0.

## What Problem Does This Solve

General-purpose LLMs make confident but incorrect statements on FinOps topics. They miscalculate PTU break-even rates, confuse Azure and AWS reservation mechanics, and give generic advice that ignores how billing actually works on Bedrock or Azure OpenAI. This skill injects verified, curated FinOps knowledge directly into the model's context -- covering billing models, cost allocation patterns, optimisation frameworks, and governance practices across major cloud providers and AI platforms.

## When to Use This Skill

Use for any query about cloud cost management, AI inference economics, commitment portfolio strategy, rightsizing, cost allocation, tagging governance, SaaS sprawl, AI dev tool spend, or connecting technology spend to business value. Covers AWS, Azure, GCP, Anthropic, Bedrock, Azure OpenAI, Vertex AI, Databricks, Snowflake, OCI, and GreenOps.

## When NOT to Use This Skill

- General cloud infrastructure design (use cicd-pipelines or docker-containerization)
- Application performance optimization unrelated to cost
- Non-cloud software licensing questions

## How to Use

**Direct invocation:**

```
Use the cloud-finops skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `finops`
- `cloud cost`
- `cost optimization`
- `cloud billing`
- `ai cost`
- `reserved instances`
- `savings plans`
- `tagging governance`
- `bedrock pricing`
- `azure openai ptu`

## What's Inside

- **Domain Router** -- Routes queries to the correct reference file across 20 domains
- **OptimNow Methodology** -- Reasoning philosophy: diagnose before prescribing, connect cost to value
- **AI Cost Management** -- LLM inference economics, agentic cost patterns, ROI frameworks
- **AI Value Management** -- AI Investment Council, stage gate model, incremental funding
- **GenAI Capacity Planning** -- Provisioned vs shared capacity, traffic shape, spillover mechanics
- **Cloud Provider FinOps** -- AWS (128 patterns), Azure (48 patterns), GCP (26 patterns), OCI
- **AI Platform Billing** -- Anthropic, Bedrock, Azure OpenAI PTUs, Vertex AI
- **Data Platform Costs** -- Databricks cluster optimisation, Snowflake credit management
- **AI Coding Tools** -- Cursor, Claude Code, Copilot, Windsurf, Codex billing and attribution
- **Governance** -- Tagging strategy, SaaS asset management, ITAM collaboration
- **GreenOps** -- Cloud carbon measurement, carbon-aware workload shifting
- **FinOps Framework** -- Full FinOps Foundation framework, 22 capabilities, maturity model

## Reference Files

| File | Domain | Lines |
|---|---|---|
| `optimnow-methodology.md` | OptimNow reasoning philosophy | ~155 |
| `finops-for-ai.md` | AI cost management, LLM economics | ~490 |
| `finops-ai-value-management.md` | AI investment governance | ~275 |
| `finops-genai-capacity.md` | GenAI capacity models | ~225 |
| `finops-anthropic.md` | Anthropic billing and governance | ~180 |
| `finops-aws.md` | AWS FinOps (128 optimisation patterns) | ~2240 |
| `finops-bedrock.md` | AWS Bedrock billing | ~225 |
| `finops-azure.md` | Azure FinOps (48 patterns) | ~1560 |
| `finops-azure-openai.md` | Azure OpenAI Service (PTUs) | ~390 |
| `finops-gcp.md` | GCP optimisation (26 patterns) | ~265 |
| `finops-vertexai.md` | GCP Vertex AI billing | ~235 |
| `finops-tagging.md` | Tagging and naming governance | ~250 |
| `finops-framework.md` | FinOps Foundation framework | ~280 |
| `finops-databricks.md` | Databricks optimisation | ~185 |
| `finops-snowflake.md` | Snowflake FinOps | ~200 |
| `finops-ai-dev-tools.md` | AI coding tools billing | ~400 |
| `finops-oci.md` | OCI optimisation | ~75 |
| `finops-sam.md` | SaaS asset management | ~290 |
| `finops-itam.md` | ITAM collaboration | ~325 |
| `greenops-cloud-carbon.md` | GreenOps and cloud carbon | ~330 |

## Attribution

Built by [OptimNow](https://optimnow.io) (James Barney). Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Upstream: [github.com/OptimNow/cloud-finops-skills](https://github.com/OptimNow/cloud-finops-skills).

## Version History

- `1.0.0` Initial integration from OptimNow/cloud-finops-skills

## Related Skills

- **[CI/CD Pipelines](../cicd-pipelines/)** -- CI/CD pipeline design, DevOps automation, infrastructure as code
- **[Docker Containerization](../docker-containerization/)** -- Docker basics, multi-stage builds, Docker Compose orchestration
- **[Workflow Automation](../workflow-automation/)** -- Development workflow automation, CI/CD pipelines, multi-agent orchestration

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 48 production-grade plugins for Claude Code.
