# FinOps Framework Reference

> Source: FinOps Foundation (finops.org/framework), 2026 version.
> This file covers the complete FinOps Framework: principles, phases, maturity model,
> domains, capabilities, personas, scopes, and technology categories.
>
> Updated definition (2026): "FinOps is an operational framework and cultural practice
> which maximizes the business value of technology."

---

## The 6 FinOps Principles
<!-- idx:37b46c22605776cb -->

1. **Teams need to collaborate** - FinOps requires cooperation across engineering, finance,
   product, and leadership. No single team can practice FinOps alone.

2. **Business value drives technology decisions** - the goal is not cost minimization but
   value maximization. Decisions should connect spend to outcomes.

3. **Everyone takes ownership for their technology usage** - distributed accountability is more
   effective than centralized policing. Engineers who see their costs act on them.

4. **FinOps data should be accessible, timely, and accurate** - delayed, incomplete, or
   unattributed data cannot support good decisions. Visibility is the foundation.

5. **FinOps should be enabled centrally** - a central FinOps function sets standards,
   builds tooling, and enables teams. It does not own all decisions.

6. **Take advantage of the variable cost model of the cloud and other technologies with
   similar consumption models** - elasticity is an asset across cloud, SaaS, and data
   platforms. Commit to baseline, keep growth variable, avoid over-provisioning.

**Common principle violations to identify:**
- Teams optimizing in isolation without cross-functional alignment (violates #1)
- Cost cutting that degrades revenue-generating systems (violates #2)
- All FinOps work done by one team with no engineering engagement (violates #3)
- Monthly reporting with no anomaly detection (violates #4)
- Decentralized, inconsistent tooling and processes (violates #5)
- Treating cloud like on-premises - fixed capacity, no elasticity (violates #6)

---

## The 3 Phases

FinOps phases are iterative, not sequential. Organizations cycle through them continuously
as their cloud usage evolves. Being in "Operate" for one capability does not mean an
organization has left "Inform" for another.

### Inform - Establish visibility and allocation

**Goal:** Make cost data accessible, attributed, and actionable.

**Key activities:**
- Set up data ingestion (AWS CUR / Azure Cost Export / GCP BigQuery billing export)
- Implement cost allocation - by account, subscription, project, or tag
- Build executive dashboards showing top cost drivers and trends
- Configure anomaly alerts (recommended threshold: >20% daily change)
- Establish a shared cost allocation methodology

**Crawl targets:** >50% of spend allocated, basic dashboards live, alerts configured
**Walk targets:** >80% allocated, hierarchical allocation, showback reports to teams
**Run targets:** >90% allocated, automated allocation, real-time visibility

### Optimize - Improve rates and usage efficiency

**Goal:** Reduce cost while maintaining or improving performance and reliability.

**Key activities:**
- Rightsize compute resources (EC2, VMs, containers, databases)
- Implement commitment discounts (Reserved Instances, Savings Plans, CUDs)
- Eliminate waste - unattached volumes, idle resources, zombie features
- Schedule non-production environments (60–70% savings on dev/test)
- Implement lifecycle policies for storage and data

**Crawl targets:** Obvious waste eliminated, basic rightsizing started
**Walk targets:** 70% commitment discount coverage, documented optimization process
**Run targets:** 80%+ commitment coverage, continuous rightsizing, automated policies

### Operate - Operationalize through governance and automation

**Goal:** Embed FinOps into engineering and finance workflows permanently.

**Key activities:**
- Establish weekly or biweekly cost review cadence with engineering teams
- Define and enforce mandatory tagging policies
- Implement budget alerts and approval workflows for new spend
- Automate governance through policy-as-code (Cloud Custodian, OpenOps, AWS Config)
- Build chargeback or showback reporting into finance workflows

**Crawl targets:** Weekly cost reviews established, mandatory tags defined
**Walk targets:** Automated alerts, showback reports delivered to teams
**Run targets:** Chargeback implemented, policies self-enforcing, anomalies auto-investigated

---

## Scopes (new in 2025)

A Scope is a defined segment of spending across technology categories, aligned to
business constructs. Scopes enable organizations to apply FinOps capabilities to
different cost surfaces systematically.

**Initial Scopes defined by the FinOps Foundation:**
- **Public Cloud** - AWS, Azure, GCP, OCI, and other IaaS/PaaS providers
- **SaaS** - software-as-a-service subscriptions and usage
- **Data Center** - on-premises and colocation infrastructure

**Custom Scopes** organizations may define:
- AI (LLM inference, training, agent infrastructure)
- Licensing (software entitlements, BYOL, marketplace)
- Private Cloud (VMware, OpenStack, internal platforms)
- Containers (Kubernetes across providers)

Scopes allow a FinOps team to track maturity independently per scope. An organization
may be at Run maturity for Public Cloud but Crawl for SaaS or AI.

---

## Technology Categories (new in 2026)

The 2026 framework introduced five structured Technology Category pages, each providing
dedicated guidance for applying FinOps capabilities to that category:

| Technology Category | Primary cost surface |
|---|---|
| **Public Cloud** | IaaS/PaaS compute, storage, networking, managed services |
| **SaaS** | Subscription fees, usage-based charges, seat licenses |
| **Data Center** | Power, cooling, hardware lifecycle, colocation fees |
| **Data Cloud Platforms** | Databricks, Snowflake, and similar consumption-based data services |
| **AI** | LLM inference, training compute, agent infrastructure, GPU cost |

Technology Categories and Scopes are related but distinct: Categories define the cost
surface; Scopes define the organizational boundary for managing it.

---

## The 4 Domains and Capabilities

> **Note on capability count:** The FinOps Foundation lists capabilities across four domains.
> The 2026 framework added Executive Strategy Alignment, renamed six capabilities, and
> restructured Domain 4. The previous version of this reference listed 22 capabilities in a
> simplified view. The tables below reflect the 2026 canonical framework. Some capabilities
> (e.g., Sustainability) appear in multiple domains with different scope emphases. Cloud
> Vendor Management (previously listed in Domain 4) was merged into Invoicing and Chargeback
> and Governance, Policy & Risk in the 2026 restructuring.

### Domain 1: Understand Usage and Cost

| Capability | Description |
|---|---|
| Data Ingestion | Collecting billing data from cloud providers into a central platform |
| Allocation | Distributing shared costs to cost centers, teams, or products |
| Reporting and Analytics | Providing actionable cost and usage reports |
| Anomaly Management | Detecting and responding to unexpected cost changes |

### Domain 2: Quantify Business Value

| Capability | Description |
|---|---|
| Planning and Estimating | Forecasting cloud spend for new projects and features |
| Budgeting | Setting and managing cloud budgets across the organization |
| Forecasting | Predicting future cloud spend based on current trends |
| Unit Economics | Connecting cloud cost to business output metrics |
| Sustainability | Measuring and reducing the carbon impact of cloud usage |

### Domain 3: Optimize Usage and Cost

| Capability | Description |
|---|---|
| Rightsizing | Matching resource size to actual workload requirements |
| Commitment Discounts | Managing RIs, Savings Plans, and CUDs for sustained workloads |
| Usage Optimization | Architectural changes that reduce cost at the workload level *(renamed from Workload Optimization in 2026)* |
| License Optimization | Managing software licenses (BYOL, AHUB, marketplace) |
| Sustainability | Reducing energy and carbon footprint of technology usage *(renamed from Cloud Sustainability in 2026)* |

### Domain 4: Manage the FinOps Practice

| Capability | Description |
|---|---|
| FinOps Practice Operations | Running the FinOps team and driving organizational adoption |
| FinOps Assessment | Measuring maturity across all capabilities |
| FinOps Education and Enablement | Training teams to incorporate FinOps into daily work |
| Onboarding Workflows | Managing cost implications of cloud migrations |
| Governance, Policy & Risk | Establishing controls that align technology use with business objectives *(renamed from Cloud Policy and Governance in 2026)* |
| Automation, Tools & Services | Evaluating and integrating tools to support FinOps capabilities *(renamed from FinOps Tools and Services in 2026)* |
| Invoicing and Chargeback | Reconciling invoices and implementing financial accountability |
| KPI & Benchmarking | Measuring FinOps performance against industry baselines *(renamed from Benchmarking in 2026)* |
| Architecting & Workload Placement | Designing cost-efficient architectures and selecting optimal deployment targets *(renamed from Architecting for Cloud in 2026)* |
| **Executive Strategy Alignment** | Connecting FinOps to executive priorities, multi-year investment strategy, product prioritization, and strategic decision support *(new in 2026)* |

---

## Personas

### Core Personas

**FinOps Practitioner**
Central coordinator of the FinOps practice. Owns the process, tooling, and cross-functional
relationships. Bridges engineering and finance. Does not own all decisions - enables others
to make good ones.

**Engineering**
Implements optimization recommendations. Owns rightsizing, architecture decisions, and
tagging at the resource level. Needs cost visibility in their existing workflows (not
separate dashboards).

**Finance**
Owns budgets, forecasting, and financial reporting. Needs cloud cost data mapped to
existing budget structures and accounting categories. Primary audience for chargeback.

**Product**
Connects cloud spend to product features and user outcomes. Key partner for unit economics.
Often the right owner for AI feature cost management.

**Procurement**
Manages cloud vendor contracts, enterprise discounts, and commitment purchases. Involved
in Reserved Instance and Savings Plan purchasing decisions.

**Leadership (C-suite, VP)**
Requires executive dashboards showing cloud spend vs. budget, trend, and business value.
Primary sponsor for FinOps culture change. Engaged for chargeback decisions and large
commitment purchases.

### Allied Personas

**ITAM (IT Asset Management)** - manages software licenses, intersects with license
optimization and cloud license portability (BYOL, AHUB).

**Sustainability** - connects cloud efficiency work to carbon metrics and ESG reporting.

**ITSM (IT Service Management)** - integrates FinOps into change management and
service catalog processes.

**Security** - intersects with governance, tagging policy enforcement, and access controls
for cost management tools.

---

## FinOps organisational placement

The State of FinOps 2026 survey (6th edition, 1,192 respondents, published February 2026)
provides current data on how FinOps practices are structured and positioned within
organisations.

**Reporting line:** 78% of FinOps practices now report into the CTO/CIO organisation
(up 18% vs 2023). Teams reporting to the CFO declined to 8%. Practitioners aligned with
CTOs and CIOs indicated two to four times more influence over technology selection -
reinforcing that FinOps is increasingly viewed as a technology capability tied to
architecture and platform decisions, not financial reporting alone.

**Team structure:** Centralized enablement remains the dominant model (60%), followed by
hub-and-spoke (21%) which is more common in large enterprises. Team sizes remain small:
organisations managing over $100M in cloud spend typically average 8-10 practitioners
and 3-10 contractors.

**Scope expansion:** FinOps has moved decisively beyond cloud-only cost management. 90%
of respondents now manage SaaS (up from 65% in 2025), 64% manage licensing (up from
49%), 57% manage private cloud, and 48% manage data centres. An emerging 28% are
beginning to include labour costs.

**Mission change:** These trends prompted the FinOps Foundation to update its mission
from "Advancing the People who manage the Value of Cloud" to "Advancing the People who
manage the Value of Technology."

---

## Maturity Model - Detailed

### Crawl
- Processes are manual, reactive, and inconsistent
- Basic cost visibility exists but allocation is incomplete (<50%)
- Optimization is ad hoc - one-off projects rather than continuous practice
- FinOps is driven by one person or team with limited organizational reach
- Commitment discount coverage is low and unmanaged

**Priority at Crawl:** Establish visibility and allocation before anything else.
Do not attempt chargeback. Do not purchase large commitment discounts without allocation.

### Walk
- Processes are documented and repeatable
- Cost allocation >80%, showback reports delivered to teams
- Optimization is proactive - rightsizing and waste elimination run continuously
- FinOps is cross-functional - engineering and finance participate regularly
- Commitment discount coverage ~70%, managed with utilization monitoring

**Priority at Walk:** Establish unit economics, expand optimization scope, begin
governance automation. Evaluate readiness for chargeback.

### Run
- Processes are automated and self-improving
- Cost allocation >90%, real-time visibility, anomalies auto-detected
- Optimization is embedded in engineering workflows - not a separate activity
- FinOps culture is distributed - teams own their costs without central policing
- Commitment discount coverage 80%+, managed by automation with human oversight
- Chargeback implemented where organizationally appropriate

**Priority at Run:** Continuous improvement, automation of governance, agentic FinOps
patterns where they add value without introducing risk.

---

## Common FinOps implementation mistakes

**Starting with optimization before visibility**
Rightsizing without allocation produces savings no one can claim or repeat. Establish
who owns what before optimizing what.

**Purchasing commitment discounts on unallocated spend**
Committing to reserved capacity before understanding usage patterns creates stranded
reservations. Analyze 90+ days of usage before purchasing commitments.

**Implementing chargeback before showback**
Organizations that jump to financial accountability before teams understand their costs
create resistance, not ownership. Show first, charge second.

**Building dashboards instead of processes**
A new dashboard without a defined review cadence and decision-making process is
documentation, not FinOps. The meeting matters as much as the data.

**Treating tagging as a one-time project**
Tagging compliance degrades over time without enforcement. Treat it as an ongoing
operational process with automated compliance checking.

**Centralizing all FinOps decisions**
A FinOps team that owns all decisions creates a bottleneck and removes team ownership.
The FinOps function should enable distributed decision-making, not replace it.

---

## Converging Disciplines (2026)

The 2026 framework formally recognizes that FinOps intersects with several adjacent
disciplines. Effective FinOps practices build explicit collaboration models with each:

| Discipline | Intersection with FinOps |
|---|---|
| **ITAM** (IT Asset Management) | License optimization, BYOL, marketplace governance, vendor co-management (see `finops-itam.md`) |
| **ITFM** (IT Financial Management) | Budget processes, allocation models, chargeback, financial reporting |
| **Sustainability** | Carbon metrics alongside cost metrics, GreenOps (see `greenops-cloud-carbon.md`) |
| **Security** | Tag governance, policy enforcement, access controls for cost tools |
| **Enterprise Architecture** | Workload placement, architecture cost reviews, tech debt assessment |

These are not FinOps capabilities but related disciplines whose practices overlap.
Organizations that treat them as separate silos miss optimization opportunities.

---

## 2026 Framework Changes Summary

For practitioners updating from the 2024 framework:

| Change | Detail |
|---|---|
| Updated definition | "...maximizes the business value of technology" (was "cloud") |
| Updated mission | "...manage the Value of Technology" (was "Cloud") |
| Scopes added (2025) | Public Cloud, SaaS, Data Center, plus custom scopes |
| Technology Categories added (2026) | Public Cloud, SaaS, Data Center, Data Cloud Platforms, AI |
| New capability | Executive Strategy Alignment (Domain 4) |
| 6 capabilities renamed | Usage Optimization, Sustainability, Governance Policy & Risk, Automation Tools & Services, KPI & Benchmarking, Architecting & Workload Placement |
| Merged capability | Cloud Vendor Management scope absorbed into Governance, Policy & Risk and Invoicing and Chargeback |
| Previously unlisted | KPI & Benchmarking and Architecting & Workload Placement existed in the Foundation's canonical framework but were omitted from v1.0 of this reference |
| Converging disciplines | ITAM, ITFM, Sustainability, Security, Enterprise Architecture |

---

> Sources: FinOps Foundation (finops.org/framework, 2026 version; State of FinOps 2026, 6th edition).

> *Cloud FinOps Skill by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
