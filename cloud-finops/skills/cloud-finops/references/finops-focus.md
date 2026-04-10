# FOCUS: FinOps Open Cost & Usage Specification

> FOCUS (FinOps Open Cost & Usage Specification) is the billing data normalization standard
> developed by the FinOps Foundation. It defines a common schema and column semantics for
> cloud cost and usage data across providers, enabling multi-cloud comparison, consistent
> tooling, and portable FinOps workflows. Without FOCUS, every provider speaks a different
> dialect. With it, cost data becomes a lingua franca.

---

## Why FOCUS matters for FinOps

### The fragmentation problem

Every major cloud provider exports billing data in a proprietary format. AWS uses the
Cost and Usage Report (CUR). Azure uses Cost Management exports. GCP uses BigQuery
billing export. Each has different column names, different cost semantics, different
granularity, and different handling of commitment discounts.

This fragmentation has real costs:
- Multi-cloud cost analysis requires custom ETL for each provider's schema
- FinOps tooling built for one provider cannot be reused against another
- Cost metrics like "amortized cost" mean different things in different exports
- Teams switching providers or adding a second cloud face months of data migration work
- Third-party FinOps platforms must maintain N independent billing parsers

### FOCUS as the Rosetta Stone

FOCUS defines a single schema that any provider can export against. A `BilledCost` column
means the same thing whether the row describes an EC2 instance, an Azure VM, or a GCP
Compute Engine resource. A practitioner who understands FOCUS can work with data from any
FOCUS-compliant provider without relearning the schema.

**What this unlocks:**
- Multi-cloud cost dashboards built on a single query layer
- Portable FinOps tooling that works across providers without provider-specific connectors
- Accurate apples-to-apples cost comparisons across clouds
- Reduced vendor lock-in for FinOps platforms - swap the provider, keep the tooling
- Faster onboarding when adding a new cloud or SaaS provider to the estate

---

## Specification overview

**Current version:** FOCUS 1.3 (ratified December 5, 2025)

### Version history

| Version | Released | Key additions |
|---|---|---|
| 1.0 | 2024 | Initial release. Standardized cloud billing columns, cost types, resource identifiers, and pricing constructs. Established the foundational schema. |
| 1.1 | 2024 | Multi-currency support. Improved provider and service metadata. Minor column clarifications. |
| 1.2 | May 2025 | Expanded scope beyond cloud infrastructure to SaaS and PaaS. Unified schema for mixed-provider estates. Invoice reconciliation columns for billing accuracy validation. |
| 1.3 | December 2025 | Contract Commitment dataset (separate from cost/usage rows). Allocation methodology columns for transparency on how shared costs are distributed. Data recency and completeness metadata. `ServiceProvider` vs `HostProvider` distinction for reseller and marketplace scenarios. |

---

## Core columns and schema

FOCUS defines a set of required and recommended columns. Understanding the cost columns is
critical - they represent distinct economic perspectives on the same charge.

### Cost columns

| Column | Definition | When to use |
|---|---|---|
| `BilledCost` | The amount invoiced by the provider. Includes upfront RI/SP fees in the period paid. | Invoice reconciliation, cash flow reporting. |
| `EffectiveCost` | `BilledCost` amortized over the commitment term. Spreads upfront fees across the benefit period. | Day-to-day cost tracking, team showback, anomaly detection. |
| `ListCost` | The on-demand list price cost if no discounts were applied. | Calculating discount value and savings. |
| `ContractedCost` | Cost after negotiated discounts (EDPs, private pricing agreements), before commitment amortization. | Measuring negotiated discount value independently from commitment discounts. |

**The key distinction:** Use `EffectiveCost` for most FinOps analysis - it smooths out
the distortion caused by large upfront payments. Use `BilledCost` only when matching
to an actual invoice.

### Resource and service columns

| Column | Definition |
|---|---|
| `ResourceId` | Provider-native identifier for the billed resource |
| `ResourceName` | Human-readable resource name |
| `ServiceCategory` | Standardized service category (Compute, Storage, Networking, Database, AI/ML, etc.) |
| `ServiceName` | Provider-specific service name (e.g., "Amazon EC2", "Azure Blob Storage") |
| `ProviderName` | The cloud or SaaS provider |
| `PublisherName` | The entity that published the service (relevant for marketplace charges) |
| `RegionId` / `RegionName` | Standardized region identifier and display name |

### Pricing and commitment columns

| Column | Definition |
|---|---|
| `PricingCategory` | On-Demand, Committed, Dynamic, or Other |
| `CommitmentDiscountId` | Links a charge to the commitment discount that covered it |
| `CommitmentDiscountType` | Reserved Instance, Savings Plan, Committed Use Discount, etc. |
| `CommitmentDiscountStatus` | Whether the commitment was used, unused, or partially used |

### FOCUS 1.3: Contract Commitment dataset

Prior to 1.3, commitment discount purchases appeared as line items in the same dataset
as usage charges. FOCUS 1.3 introduces a separate **Contract Commitment dataset** for
commitment purchases, renewals, and expirations. This separation makes it possible to:
- Build commitment inventory reports without filtering out usage rows
- Track commitment lifecycle events (purchase, expiry, renewal) independently
- Reconcile amortized cost in the usage dataset against commitment purchases in the
  commitment dataset without double-counting

### FOCUS 1.3: ServiceProvider vs HostProvider

For reseller and marketplace scenarios, FOCUS 1.3 distinguishes between:
- `ServiceProvider`: The entity the customer has a commercial relationship with
  (e.g., a cloud reseller, MSP, or marketplace)
- `HostProvider`: The underlying infrastructure provider executing the compute
  (e.g., AWS, Azure, GCP)

This is significant for organizations buying cloud through resellers or managing
multi-tier commercial relationships.

---

## Provider support matrix

| Provider | FOCUS version | Export method | Notes |
|---|---|---|---|
| AWS | 1.0+ | CUR 2.0 with FOCUS export enabled in Cost Explorer | Available in all commercial regions. Enable in Billing console. |
| Azure | 1.0+ | Cost Management FOCUS export | Available in EA, MCA, and CSP billing accounts. |
| GCP | 1.0+ | BigQuery billing export (FOCUS table) | Requires BigQuery billing export enabled. |
| OCI | 1.0+ | Cost and Usage Reports (FOCUS format) | Available in all regions via Object Storage delivery. |
| Alibaba Cloud | 1.0 | Billing API / Cost Management export | Partial column support; verify schema completeness. |
| Databricks | 1.2+ | System tables (`system.billing.usage`) with FOCUS mapping | Requires Unity Catalog. See finops-databricks reference. |
| Snowflake | 1.2+ | Account Usage view with FOCUS-aligned export | Third-party tooling required for full FOCUS output. |

**Verification note:** Provider FOCUS support evolves rapidly. Always verify current
column completeness against the FOCUS 1.3 requirements before building production
pipelines against a provider's export.

---

## Adoption guidance

### When to adopt FOCUS

**Multi-cloud environments (immediate value)**
If you have two or more cloud providers, FOCUS eliminates the custom ETL layer required
to normalize disparate billing schemas. The ROI is immediate: one pipeline, one schema,
unified dashboards.

**Single cloud preparing for multi-cloud**
Adopting FOCUS before adding a second provider means your tooling, dashboards, and
allocation logic are already provider-agnostic when the time comes. Retrofitting is
significantly more expensive.

**Building custom FinOps tooling**
If you are building internal dashboards, allocation engines, or anomaly detection, build
against FOCUS columns from the start. The effort to support additional providers later
drops from months to days.

**Evaluating FinOps platforms**
FOCUS support is now a meaningful differentiator when evaluating commercial FinOps
platforms. Native FOCUS ingestion means less vendor-specific transformation and cleaner
data portability if you switch platforms.

### Implementation path

1. **Enable FOCUS exports from each provider.** Run FOCUS exports in parallel with
   existing legacy exports during the transition period. Do not disable legacy exports
   until dashboards and alerts are fully migrated.

2. **Map existing reports and dashboards to FOCUS columns.** Document the mapping from
   your current provider-native columns (e.g., AWS CUR `line_item_unblended_cost`) to
   FOCUS equivalents (e.g., `BilledCost`). Identify any columns in current reports
   that have no FOCUS equivalent and decide whether they are still needed.

3. **Build a unified data lake or warehouse with FOCUS schema.** Ingest FOCUS exports
   from all providers into a single table or schema partition. A single `SELECT * FROM
   focus_costs WHERE provider = 'AWS'` should return the same column structure as
   `WHERE provider = 'Azure'`.

4. **Migrate dashboards and alerts to FOCUS-based queries.** Replace provider-native
   column references with FOCUS equivalents. Validate that metric values match within
   acceptable tolerance before cutting over.

5. **Evaluate tooling vendors for native FOCUS support.** Prefer platforms that ingest
   FOCUS directly over those that transform provider-native data internally. Native
   FOCUS support means the platform stays current with FOCUS versions without
   custom maintenance on your end.

### Adoption statistics (State of FinOps 2025/2026)

- 57% of organizations have concrete plans to adopt FOCUS
- 24% are evaluating whether to adopt
- 18% have no current plans to adopt

**Primary adoption barriers:**
- Time constraints - FOCUS adoption competes with other FinOps priorities
- Limited internal skills - practitioners unfamiliar with FOCUS schema semantics
- Billing vendor lag - some FinOps platform vendors have not yet implemented FOCUS natively
- Data pipeline debt - existing legacy pipelines require significant rework to migrate

---

## FOCUS and existing FinOps tools

**Commercial FinOps platforms** are moving toward native FOCUS ingestion. Platforms that
previously required provider-specific connectors are replacing them with a single FOCUS
ingestor. For practitioners evaluating platforms, native FOCUS support reduces onboarding
time and simplifies multi-cloud configuration.

**OpenCost** is aligning its cost model terminology to FOCUS. Kubernetes cost allocation
mapped to FOCUS columns enables unified reporting across container workloads and cloud
billing in the same schema.

**Custom tooling** benefits most from FOCUS standardization. Teams that built bespoke
allocation engines on CUR or Azure exports face the highest migration effort but also
gain the most: a FOCUS-based engine requires no provider-specific branching logic.

**dbt and data engineering layers** can implement FOCUS normalization as a model in an
existing data warehouse pipeline, making FOCUS available to any downstream consumer
without changing source systems.

---

## FOCUS for SaaS and data platforms (1.2+)

FOCUS 1.2 formally extended the specification beyond cloud infrastructure to cover SaaS
and PaaS providers. This reflects the reality that modern technology spend is not
limited to AWS, Azure, and GCP - organizations also manage significant spend in
Databricks, Snowflake, GitHub, Salesforce, and dozens of other platforms.

**What SaaS normalization enables:**
- A single cost dataset covering cloud infrastructure, data platforms, and SaaS tools
- Consistent cost allocation methodology applied across all vendor types
- FinOps governance workflows (budgets, anomaly detection, showback) applied to SaaS
  spend using the same tooling as cloud spend

**Data platform cost standardization:**
Databricks and Snowflake both produce usage-level billing data that maps to FOCUS columns.
With FOCUS 1.2+ exports or FOCUS-mapped views, Databricks DBU costs and Snowflake credit
consumption appear in the same schema as EC2 and Azure Compute charges. This enables
unit economics calculations that span infrastructure and compute platform costs in a
single query.

See the finops-databricks and finops-snowflake reference files for platform-specific
cost management patterns.

---

## Governance checklist

- [ ] Identify which providers in your estate support FOCUS exports and at which version
- [ ] Enable FOCUS-format exports alongside legacy formats (parallel run, do not cut over immediately)
- [ ] Map internal cost allocation taxonomy to FOCUS columns (document the mapping explicitly)
- [ ] Define transition timeline from legacy to FOCUS-primary reporting (recommend 90-day parallel run)
- [ ] Train FinOps team on FOCUS schema, column semantics, and cost type distinctions
- [ ] Evaluate FinOps tooling vendors for native FOCUS support before renewal or new procurement
- [ ] Plan for FOCUS version updates (annual cadence expected; 1.3 → 1.4 likely in 2026)
- [ ] Validate exported data completeness - not all providers implement all required columns at launch
- [ ] Establish a FOCUS validation step in data pipelines (FOCUS Validator tool available on GitHub)

---

## Resources

- **Specification:** [focus.finops.org](https://focus.finops.org) - full schema, column
  definitions, requirements, and conformance guidance
- **Free course:** "Introduction to FOCUS" at [learn.finops.org](https://learn.finops.org)
- **Certification:** Certified FOCUS Analyst - validates practitioner proficiency in
  FOCUS schema and implementation
- **FOCUS Validator:** Open-source tool on GitHub for validating provider exports against
  FOCUS requirements
- **Requirements Analyzer:** GitHub tool for assessing provider export completeness
  against FOCUS column requirements
- **FinOps Foundation FOCUS working group:** Active community developing the specification,
  open to practitioners contributing feedback and use cases

---

> *Cloud FinOps Skill by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
