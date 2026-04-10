# Multi-Cloud FinOps

> Most enterprises operate across 2-3 cloud providers plus SaaS. Per-provider FinOps is
> necessary but insufficient. Managing AWS cost well, managing Azure cost well, and managing
> GCP cost well does not produce coherent multi-cloud cost management. This file covers
> the structural challenges of cross-cloud cost governance and the normalization patterns
> that make multi-cloud spend manageable as a portfolio rather than a collection of siloed
> programs.

---

## Why multi-cloud FinOps is structurally harder

### The fragmentation problem

Every major cloud provider has an independent billing format, pricing model, and governance
toolchain. When an organization spans two or more providers, FinOps practitioners must
operate in parallel, provider-specific modes unless they build or adopt a normalization
layer.

**Fragmentation surfaces in every FinOps discipline:**
- Billing formats differ: CUR (AWS), Cost Management Export (Azure), BigQuery Export (GCP)
- Commitment instruments differ in name, flexibility, and liquidity across providers
- Tag and label systems have different key/value constraints and enforcement mechanisms
- Billing data delivery cadences differ: near-real-time (GCP) vs. daily (AWS CUR)
- Cost semantics differ: "unblended cost", "effective cost", and "amortized cost" are
  calculated differently per provider before FOCUS normalization
- No native cross-cloud cost comparison exists without a normalization layer

**The consequence:** Multi-cloud analysis built on raw provider exports requires N
independent ETL pipelines, N schema mappings, and N provider-specific interpretations
for every cost metric. Each new provider added multiplies the complexity. Without
normalization, multi-cloud FinOps does not scale.

### Terminology normalization

Different providers use different names for functionally equivalent constructs. Practitioners
must map these to a common vocabulary to reason about commitment strategy and cost
optimization across the portfolio.

| Concept | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| Reserved capacity (resource-specific) | Reserved Instance (RI) | Reservation | Committed Use Discount (CUD) | Reserved Capacity |
| Flexible commitment (family/region-level) | Compute Savings Plan | Azure Savings Plan | Flexible CUD | - |
| Pre-emptible / interruptible compute | Spot Instance | Spot VM | Preemptible VM / Spot VM | Preemptible Instance |
| Cost export format | Cost and Usage Report (CUR) | Cost Management Export | BigQuery Billing Export | Cost and Usage Report |
| Tagging mechanism | Tags (key-value) | Tags (key-value) | Labels (key-value) | Tags (key-value) |
| Cost anomaly detection | Cost Anomaly Detection (ML-based) | Cost alerts + anomaly detection | Budgets + Cost anomaly detection | Budget alerts |
| Cloud cost management console | AWS Cost Explorer | Azure Cost Management | Cloud Billing Console | OCI Cost Management |

**OptimNow principle:** Normalize terminology before building dashboards or reports.
A "reservation" row in an Azure export and a "Reserved Instance" row in a CUR export
represent the same economic construct. Conflating or separating them produces incorrect
portfolio-level commitment utilization metrics.

---

## FOCUS as the normalization layer

FOCUS (FinOps Open Cost and Usage Specification) is the FinOps Foundation's standard
billing schema for cloud and SaaS providers. It defines a common column set and semantic
definitions that make cost data comparable across providers without provider-specific ETL.

**What FOCUS provides for multi-cloud FinOps:**
- A single schema (`BilledCost`, `EffectiveCost`, `ListCost`, `ServiceCategory`, etc.)
  with identical semantics regardless of which provider generated the row
- Standardized `PricingCategory` values (On-Demand, Committed, Dynamic) that map
  cleanly across providers
- Standardized `CommitmentDiscountType` values that normalize RI, Savings Plan, and CUD
  into comparable categories
- A single data pipeline for all providers: ingest FOCUS exports, no per-provider
  column mapping required

See `finops-focus.md` for full specification details, cost column semantics, and
provider-specific export configuration.

**Provider FOCUS export availability (as of FOCUS 1.3):**

| Provider | FOCUS support | Export method |
|---|---|---|
| AWS | 1.0+ | CUR 2.0 with FOCUS export enabled in Billing console |
| Azure | 1.0+ | Cost Management FOCUS export (EA, MCA, CSP) |
| GCP | 1.0+ | BigQuery billing export (FOCUS table) |
| OCI | 1.0+ | Cost and Usage Reports (FOCUS format, Object Storage delivery) |

**FOCUS adoption removes the primary technical blocker for multi-cloud FinOps.** Once
all providers export in FOCUS format and land in a unified data store, cross-cloud
queries, dashboards, and allocation rules operate on a single coherent dataset.

---

## Cross-cloud commitment strategy

### Provider-specific commitment instruments

Each provider's commitment hierarchy has different terms, flexibility, exchange rights,
and coverage scope. Treating them as equivalent is a common mistake.

| Dimension | AWS | Azure | GCP |
|---|---|---|---|
| Deepest discount instrument | 3-year All Upfront RI (up to 75% off On-Demand) | 3-year Reservation (up to 65% off) | 3-year CUD (up to 57% off) |
| Most flexible instrument | Compute Savings Plan (family, region) | Azure Savings Plan (compute, multi-region) | Flexible CUD (machine family, region) |
| Exchange / modification rights | Convertible RIs exchangeable; Standard RIs limited | Reservations not exchangeable after 7-day return window | CUDs not exchangeable |
| Refund / early cancellation | Convertible and Standard RIs can be listed on Marketplace | No self-service refund after return window | No cancellation |
| Commitment layering | Savings Plans apply first, then RIs | Savings Plan applies after Reservations | CUDs apply before On-Demand |
| Recommendation tooling | Cost Explorer SP/RI Recommendations | Azure Advisor Reservations | GCP Recommender |

### Portfolio-level commitment principles

Managing commitments per provider in isolation produces suboptimal portfolio outcomes.
These principles apply across all providers simultaneously.

1. **Commit only to workloads with proven, stable demand.** Require 90+ days of production
   utilization data before purchasing any commitment. New workloads, seasonal workloads,
   and experimental infrastructure belong in On-Demand or Spot/Preemptible.

2. **Use the most flexible instrument before the most restrictive.** On each provider,
   exhaust coverage with the most flexible commitment type (Compute Savings Plan, Azure
   Savings Plan, Flexible CUD) before purchasing resource-specific commitments (Standard RIs,
   Reservations, Resource CUDs). Flexibility costs 3-8% of additional discount; the
   optionality is worth it for most workloads.

3. **Maintain a 15-20% uncommitted liquidity buffer across the full portfolio.** The buffer
   absorbs workload migrations, provider shifts, and architecture changes without stranding
   committed capacity. Apply this at the total portfolio level, not per provider.

4. **Stagger commitment expirations across providers.** Avoid a multi-provider commitment
   cliff where large blocks of AWS RIs, Azure Reservations, and GCP CUDs expire in the
   same quarter. Stagger terms so renewals are spread across the year, preserving
   negotiating leverage with each provider at different points.

5. **Review the full multi-cloud commitment portfolio quarterly.** A quarterly review
   must cover utilization rates, expiring commitments, and new workload coverage
   opportunities across all providers simultaneously. Provider-siloed reviews miss
   portfolio-level rebalancing opportunities.

6. **Account for provider-shift risk in commitment terms.** If workloads are candidates
   for migration between providers, favor 1-year commitments and flexible instruments
   over 3-year resource-specific commitments. The discount differential between 1-year
   and 3-year is rarely worth the migration friction if a cloud migration is planned.

---

## Cross-cloud tagging strategy

### Minimum viable tag taxonomy (all providers)

The same tag keys must be used across all providers. AWS tags, Azure tags, and GCP labels
enforce identical keys and value conventions. This is the single most impactful cross-cloud
governance action an organization can take.

| Tag key | Purpose | Example values |
|---|---|---|
| `team` | Cost allocation to engineering team | `platform`, `data-eng`, `growth` |
| `product` | Group by product or service line | `checkout`, `search`, `ml-pipeline` |
| `environment` | Separate lifecycle stages | `prod`, `staging`, `dev`, `sandbox` |
| `cost-centre` | Map to finance budget structure | `CC-1042`, `engineering`, `data` |
| `owner` | Identify responsible individual or team | `jean.latiere`, `team-infra` |

### Normalization patterns

**Use identical tag keys across all providers.** The same key (`environment`, not
`Environment` on AWS and `env` on GCP) is required for unified queries. Enforce lowercase
keys and an approved value list from day one. Cross-provider inconsistency breaks
allocation queries as reliably as missing tags.

**Enforce via IaC, not per-provider policy engines.** Terraform modules, Pulumi component
resources, and CDK constructs can enforce tag requirements at resource creation across
all providers using the same definition. Per-provider enforcement (SCPs, Azure Policy,
GCP Organization Policies) is a useful second layer, but IaC is the primary gate.

**Apply virtual tagging for resources that cannot be physically tagged.** Shared
infrastructure, marketplace charges, and support costs cannot carry resource-level tags.
Use the billing layer's virtual tagging capability (AWS Cost Categories, Azure Cost
Management views, or the FinOps platform's allocation rules) to apply dimensions to
these costs. Virtual tagging is a complement, not a substitute for physical tags.
See `finops-tagging.md` for physical and virtual tagging strategy in detail.

**Map provider-specific naming to a common taxonomy in the FinOps platform.** Even
with identical tag keys, providers may enforce different case or value constraints.
Define the canonical mapping in the FinOps platform so reports always display
normalized values regardless of provider-specific raw tag values.

---

## Cross-cloud cost allocation

### Unified data lake approach

The most scalable architecture for multi-cloud cost management centralizes billing
data from all providers into a single data store with a unified schema.

1. **Enable FOCUS-format exports from each provider.** Run in parallel with legacy
   formats during the transition period (minimum 90-day parallel run before decommissioning
   legacy pipelines).

2. **Land all exports in a unified data warehouse.** BigQuery, Snowflake, Databricks,
   or a dedicated FinOps data lake. All providers write to the same FOCUS-schema table,
   partitioned by `ProviderName` or `BillingAccountId`.

3. **Apply common allocation rules and dimensions.** Shared cost allocation logic
   (splitting shared services, applying virtual tags) runs once against the unified
   dataset, not once per provider.

4. **Build unified dashboards with provider as a dimension.** Every cost report includes
   `ProviderName` as a filter and group-by dimension. Total technology spend (cloud +
   SaaS + data platforms) is visible in a single view.

### FinOps platform approach

Commercial FinOps platforms abstract the data layer and provide multi-cloud visibility
without requiring a custom data engineering pipeline.

| Platform | Multi-cloud support | FOCUS native | Notes |
|---|---|---|---|
| IBM Cloudability | AWS, Azure, GCP, OCI + SaaS | In progress | Strong enterprise cost allocation features |
| Flexera One | AWS, Azure, GCP, OCI + SaaS | In progress | Broad vendor coverage including on-premises |
| Vantage | AWS, Azure, GCP + SaaS | Yes (1.0+) | Developer-focused; strong API and Terraform provider |
| Apptio Cloudability | AWS, Azure, GCP | Partial | Strong TBM integration for technology business management |
| CloudHealth (Broadcom) | AWS, Azure, GCP | In progress | Mature platform; post-acquisition roadmap uncertain |
| nOps | AWS-primary, Azure/GCP beta | In progress | Strong commitment management automation |

**Selection criteria for multi-cloud platforms:** Prioritize native FOCUS ingestion,
breadth of provider connectors, and quality of cross-provider allocation capabilities.
Avoid platforms that normalize billing data with opaque internal transformations -
prefer platforms where the normalization layer is visible and auditable.

---

## Cross-cloud optimization comparison

### Compute

| Optimization lever | AWS | Azure | GCP |
|---|---|---|---|
| Rightsizing tool | Compute Optimizer | Azure Advisor | GCP Recommender |
| Commitment recommendation | Cost Explorer SP/RI | Azure Advisor Reservations | GCP Recommender CUD |
| Spot / preemptible usage | Spot Instances + Auto Scaling | Spot VMs + VMSS | Preemptible VMs + MIG |
| ARM / Ampere migration | Graviton (M8g, C8g, R8g) | Dpsv5 series (Ampere Altra) | T2A series (Ampere Altra) |
| Idle resource detection | Cost Explorer + Compute Optimizer | Azure Advisor | GCP Recommender |

**Cross-provider principle:** Rightsizing recommendations are generated independently
per provider. Consolidate them into a single optimization backlog with normalized
savings estimates (in absolute dollars, not percentage) for prioritization. Do not
let per-provider tooling fragment the optimization pipeline.

### Storage

| Optimization lever | AWS | Azure | GCP |
|---|---|---|---|
| Lifecycle policies | S3 Lifecycle Rules (to IA, Glacier, Deep Archive) | Blob Storage Lifecycle Management | GCS Object Lifecycle Management |
| Archive tiers | S3 Glacier Instant / Flexible / Deep Archive | Archive access tier | Coldline / Archive storage class |
| Snapshot management | EC2 / EBS snapshot lifecycle policies | Azure Backup + snapshot retention policies | GCP snapshot schedules + auto-delete |
| Orphaned volume detection | Compute Optimizer + AWS Config | Azure Advisor | GCP Recommender |

### Networking

| Optimization lever | AWS | Azure | GCP |
|---|---|---|---|
| Egress cost visibility | CUR `DataTransfer` usage type | Azure bandwidth charges | GCP Network Intelligence Center |
| Cross-region traffic reduction | VPC endpoints, Regional endpoints | Private Endpoints, Azure Front Door | Cloud Interconnect, Private Service Connect |
| NAT gateway optimization | NAT Gateway + VPC endpoints for AWS services | NAT Gateway + Private Endpoints | Cloud NAT + Private Google Access |

---

## Governance checklist

- [ ] Establish a common tag taxonomy with identical keys and value conventions across all providers
- [ ] Enable FOCUS-format billing exports from every provider in scope
- [ ] Build or procure a unified multi-cloud cost dashboard with provider as an explicit dimension
- [ ] Define a cross-provider commitment strategy reviewed as a single portfolio, not per provider
- [ ] Stagger commitment expirations to avoid multi-provider cliff renewals in the same quarter
- [ ] Review total technology spend quarterly: cloud infrastructure + SaaS + data platforms together
- [ ] Maintain a provider comparison matrix for common workload types (compute, storage, ML)
- [ ] Normalize unit economics across providers before making cost-based workload placement decisions
- [ ] Train FinOps practitioners on commitment instruments, billing formats, and optimization levers
  for every active provider - not just the primary one
- [ ] Apply virtual tagging in the FinOps platform for charges that cannot carry physical tags
- [ ] Validate FOCUS export completeness for each provider before decommissioning legacy pipelines
- [ ] Define a multi-cloud anomaly detection policy: alerts at both the provider level and the
  total-portfolio level

---

> *Cloud FinOps Skill by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
