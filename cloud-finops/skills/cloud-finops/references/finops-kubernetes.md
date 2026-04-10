# FinOps for Kubernetes and Containers

> Kubernetes abstracts infrastructure from workloads, which creates a cost attribution gap.
> Cloud billing shows node costs - EC2 instances, VM SKUs, GKE node pools. Teams need pod,
> namespace, and service costs. Without a dedicated cost model, Kubernetes clusters become
> black boxes where spend grows invisibly and optimization savings cannot be traced to owners.
> This file covers the Kubernetes cost model, visibility tooling, attribution patterns,
> optimization levers, and governance practices.

---

## Why Kubernetes needs dedicated FinOps
<!-- doc:k8s-finops-intro -->

Kubernetes introduces cost management challenges that standard cloud FinOps tooling does
not address out of the box.

**The attribution gap:** Cloud billing reports at the node level. A single node runs
dozens of pods from multiple teams, products, and environments simultaneously. Without
additional tooling, there is no native mechanism to answer "how much did the checkout
service cost this week?" from a cloud invoice alone.

**The over-provisioning trap:** Kubernetes scheduling allocates capacity based on resource
*requests*, not actual usage. A pod requesting 2 CPU and 4 GB RAM reserves that capacity
on a node regardless of whether it uses it. Teams that copy resource requests from examples
or add safety margins without monitoring actual usage routinely over-provision by 3–5×.

**Shared cluster overhead:** Control plane, system namespaces (kube-system, monitoring,
logging), and cluster-level add-ons must be allocated somewhere. Without a defined shared
cost model, this overhead falls into an unattributed pool or is silently absorbed by the
largest tenant.

**GPU workloads compound the challenge:** GPU nodes cost 10–30× more per hour than
standard compute. GPUs are allocated as whole units by the Kubernetes scheduler -
a pod requesting one GPU locks the entire physical GPU regardless of utilisation.
Misattribution of GPU costs or poor utilisation directly translates to large, visible waste.

---

## The Kubernetes cost model
<!-- doc:k8s-cost-model -->

### Cost components

| Component | Description | Cost driver |
|---|---|---|
| Node compute (CPU) | vCPU allocated to node pool | Instance type × node count × hours |
| Node compute (memory) | RAM allocated to node pool | Instance type × node count × hours |
| GPU nodes | Accelerated compute for ML/inference | GPU instance × count × hours |
| Persistent storage | PersistentVolumes backed by EBS, Azure Disk, GCP PD | GB provisioned × hours |
| Network: ingress | Traffic entering the cluster via load balancers | Load balancer hours + data processed |
| Network: egress | Traffic leaving the cluster to internet or other regions | GB transferred × rate |
| Network: cross-AZ | Pod-to-pod traffic crossing availability zones | GB transferred × intra-region rate |
| Control plane | Managed K8s fee | EKS: $0.10/hr · AKS: free (standard tier) or $0.10/hr (premium) · GKE: $0.10/hr |
| Add-ons | Observability (Prometheus, Grafana), service mesh, ingress controllers | Varies - often 10–20% of cluster cost |

**Control plane note:** EKS and GKE charge per cluster regardless of node count. At small
scale, the $72/month control plane fee is significant. At large scale, it is negligible.
AKS free tier omits SLA guarantees - production clusters should budget for the premium tier.

### Request vs limit vs actual

Understanding these three metrics is the foundation of Kubernetes cost management.
Conflating them is the most common source of over-provisioning waste.

| Metric | Definition | Scheduler role | Cost implication |
|---|---|---|---|
| **Request** | Minimum resource the pod guarantees it needs | Scheduler reserves this capacity on a node | Cost floor - capacity is paid for whether used or not |
| **Limit** | Maximum resource the pod is allowed to consume | Enforced by the kubelet (CPU throttling, OOM kill) | Burst ceiling - does not reserve capacity |
| **Actual** | Real-time resource consumption observed by kubelet | No scheduling role | True cost driver - but not what you pay for |
| **Request-to-actual ratio** | Request ÷ actual (e.g., 3× means 3 CPU requested per 1 CPU used) | — | Efficiency indicator; target <1.5× |

**The waste formula:**
```
Wasted capacity = (Request - Actual) / Request × 100%
```
A cluster with 60% average CPU utilisation is paying for 40% unused capacity at full node
rates. At $0.10/vCPU-hour across 100 nodes, that is $14,400/month in wasted compute.

**Setting requests correctly:**
- Start at P95 actual usage over a representative 2-week window
- Add 20% safety buffer above P95
- Review and adjust quarterly, or after significant traffic changes

---

## Cost visibility tools
<!-- doc:k8s-visibility-tools -->

### OpenCost (CNCF)

OpenCost is the open-source standard for Kubernetes cost monitoring. It is a CNCF
incubating project and the implementation of the OpenCost specification.

**Key capabilities:**
- CPU, memory, GPU, network, and PersistentVolume cost allocation per pod, namespace,
  deployment, label, and annotation
- Multi-cloud support (AWS, Azure, GCP, on-premises)
- FOCUS specification alignment - output maps to the FinOps Open Cost and Usage
  Specification for interoperability with other FinOps platforms
- GPU utilisation tracking via chipset-specific metrics (NVIDIA DCGM, AMD ROCm)
- Deploys on Kubernetes 1.20+ as a lightweight sidecar to kube-state-metrics
- REST API and Prometheus metrics endpoint for custom dashboards
- Free, Apache 2.0 licensed with no node count restrictions

**Architecture:** OpenCost runs as a pod in the cluster, reads cloud pricing from provider
APIs (or a custom pricing CSV), and combines it with real-time resource metrics from
Prometheus to produce per-pod cost allocation continuously.

### Kubecost (IBM)

Kubecost is the commercial Kubernetes cost management platform, acquired by IBM in 2024
and integrated into the IBM FinOps suite alongside Cloudability and Turbonomic.

**Kubecost 3.0 (2025) key changes:**
- Expanded scope beyond Kubernetes to include cloud service costs (EC2, RDS, S3)
  alongside cluster costs in a unified view
- Dropped hard Prometheus dependency - can run with its own bundled metrics collection
- GPU monitoring via NVIDIA DCGM integration with per-pod GPU utilisation breakdown
- Integration with IBM Turbonomic for automated rightsizing recommendations and
  execution (not just advisory)
- Part of IBM FinOps suite: Cloudability (cloud billing) + Turbonomic (resource
  optimization) + Kubecost (K8s cost) - unified under a single platform contract

**Editions:** Free tier covers single-cluster, 15-day data retention. Enterprise tier
adds multi-cluster, SSO, RBAC, long-term retention, and Turbonomic integration.

### Comparison

| Dimension | OpenCost | Kubecost |
|---|---|---|
| Cost | Free (open source) | Free tier + paid enterprise |
| License | Apache 2.0 | Proprietary (free tier available) |
| Cloud support | AWS, Azure, GCP, on-premises | AWS, Azure, GCP (enterprise adds on-premises) |
| GPU support | Yes (DCGM, chipset-specific metrics) | Yes (NVIDIA DCGM, enterprise tier) |
| FOCUS alignment | Yes (native) | Partial (export support) |
| Prometheus dependency | Required | Optional (3.0+) |
| Automation capabilities | Advisory only | Automated rightsizing via Turbonomic (enterprise) |
| Multi-cluster | Yes | Enterprise tier |
| Cloud service costs | K8s only | K8s + cloud services (3.0+) |
| Best for | Cost-conscious teams, OSS stack, FOCUS alignment | Teams wanting automation, IBM ecosystem, unified cloud + K8s view |

---

## Cost attribution patterns
<!-- doc:k8s-attribution-patterns -->

### Namespace-based allocation

Namespaces are the primary organizational unit in Kubernetes and the most reliable
cost attribution boundary. Allocating costs at the namespace level maps naturally to
teams, products, or environments.

**Implementation:**
1. Define a namespace ownership model (one team per namespace, or one product per namespace)
2. Apply ownership labels at the namespace level - tools like OpenCost and Kubecost
   inherit these labels for all pods in the namespace
3. Define a policy for shared namespaces (monitoring, ingress, cert-manager): allocate
   overhead proportionally or as a fixed charge per tenant namespace

**Limitation:** Multi-tenant namespaces (where multiple teams deploy into a shared
namespace) break the simple mapping. Use label-based attribution for these cases.

### Label-based allocation

Labels applied at the pod or deployment level enable attribution within shared namespaces
and add dimensions beyond team ownership.

**Minimum required labels for cost attribution:**

```yaml
labels:
  team: platform-team
  product: checkout-service
  environment: prod
  cost-centre: cc-1234
```

**Enforcement:** Use an admission controller (OPA Gatekeeper or Kyverno) to reject
deployments that do not carry the required labels. This prevents attribution gaps from
accumulating silently over time.

**Extended label taxonomy:**

```yaml
labels:
  team: platform-team
  product: checkout-service
  environment: prod
  cost-centre: cc-1234
  tier: backend          # frontend / backend / data / gpu
  criticality: high      # high / medium / low (drives node pool selection)
```

### Shared cost distribution

Every cluster has overhead that cannot be attributed to a single workload: the control
plane, kube-system pods, monitoring infrastructure, and node capacity reserved for
system processes.

**Three distribution models:**

| Model | Description | When to use |
|---|---|---|
| **Proportional (CPU/memory requests)** | Each namespace pays for overhead proportional to its share of total cluster requests | Fair for homogeneous workloads; default recommendation |
| **Proportional (actual usage)** | Overhead distributed by actual CPU/memory consumed | More accurate but requires usage data; use for mature programs |
| **Fixed per-namespace** | Each namespace pays an equal flat share of overhead | Simple; penalizes small namespaces; use only when teams are roughly equivalent in size |

**Recommended approach:** Proportional by CPU+memory requests, recalculated monthly.
Apply the same model consistently - switching models mid-year invalidates historical
comparisons.

---

## Optimization patterns
<!-- doc:k8s-optimization-patterns -->

### Pod rightsizing

Rightsizing pod resource requests is the highest-ROI optimization in most Kubernetes
environments. It directly reduces the node capacity required to schedule workloads.

**Process:**
1. Collect actual CPU and memory usage for all pods over a representative period
   (minimum 2 weeks, ideally 4)
2. Calculate P95 actual usage per container
3. Set requests = P95 + 20% buffer
4. Set limits = 2–3× requests (allow burst without over-provisioning the scheduler)
5. Review quarterly or after sustained traffic changes

**Vertical Pod Autoscaler (VPA):** VPA automates the measurement and recommendation
steps. In `Off` mode it generates recommendations without modifying pods. In `Initial`
mode it sets requests at pod creation. In `Auto` mode it actively resizes running pods
(requires pod restart). Start with `Off` mode to gather data before enabling automatic
changes.

**Target efficiency ratio:** Request-to-actual ratio below 1.5× for CPU, below 1.3×
for memory (memory over-provisioning is less harmful than CPU throttling, but still
drives unnecessary node costs).

### Node pool optimization

Cluster-wide rightsizing focuses on the node pool layer - ensuring nodes are sized and
typed appropriately for the workloads they run.

- Separate node pools by workload profile: CPU-intensive (compute-optimized instances),
  memory-intensive (memory-optimized instances), GPU (accelerated compute), and
  general-purpose
- Use node labels and pod affinity/anti-affinity to route pods to the appropriate pool
- Match instance family to workload - a memory-optimized workload on a compute-optimized
  node wastes memory capacity and creates CPU contention
- Review node pool utilisation monthly - a pool running at <40% average utilisation is
  a candidate for consolidation or downsizing

### Cluster autoscaling

The Cluster Autoscaler adds nodes when pods cannot be scheduled and removes underutilised
nodes after a configurable delay.

**Key tuning parameters:**

| Parameter | Default | Recommendation |
|---|---|---|
| `scale-down-delay-after-add` | 10m | 10–30m for production; longer for GPU pools |
| `scale-down-unneeded-time` | 10m | 10–20m; too short causes thrashing |
| `scale-down-utilization-threshold` | 0.5 | 0.6–0.7 reduces premature scale-down |
| `max-node-provision-time` | 15m | Alert if provisioning consistently exceeds this |

**KEDA (Kubernetes Event-Driven Autoscaling):** For workloads driven by queue depth,
custom metrics, or external events (not CPU/memory), KEDA enables pod autoscaling that
pairs with cluster autoscaler to scale nodes only when demand exists.

### Spot and preemptible node optimization

Spot (AWS) and preemptible (GCP) and Spot (Azure) nodes cost 60–90% less than on-demand
for the same instance type. They are interrupted with short notice (2 minutes on AWS and
Azure, 30 seconds on GCP).

**Workloads suitable for Spot:**
- Batch processing and data pipelines (fault-tolerant by design)
- CI/CD build runners
- Development and staging environments
- Stateless services with >2 replicas (single interruption does not cause downtime)

**Workloads not suitable for Spot:**
- Stateful workloads with long restart times
- Services with strict latency SLAs and no replica redundancy
- GPU inference serving for synchronous user-facing requests

**Implementation pattern:** Mixed node groups - a small on-demand base capacity
(2–3 nodes per pool) combined with Spot nodes for burst. Karpenter (AWS-native) and
the Cluster Autoscaler with mixed instance policy handle this pattern natively.

### Non-production cost control

Non-production environments (dev, staging, QA) are the easiest optimization target.
They typically run 24/7 but are used for 8–10 hours per weekday.

**Approaches:**

| Approach | Tool | Savings potential |
|---|---|---|
| Scale to zero during off-hours | KubeGreen | 60–70% on non-prod node costs |
| Smaller node types for non-prod pools | Node pool config | 30–50% vs production sizing |
| Spot nodes for all non-prod workloads | Karpenter / Cluster Autoscaler | 60–90% on non-prod compute |
| Shared non-prod cluster (multiple envs) | Namespace isolation | 40–60% vs dedicated clusters |

**KubeGreen:** KubeGreen is a Kubernetes operator that suspends deployments and
CronJobs on a schedule - scaling replicas to zero outside working hours and restoring
them automatically. It requires no application changes and operates at the resource level.

### GPU cost optimization

GPU instances represent the highest per-node cost in Kubernetes environments.
Optimisation here has outsized financial impact.

**GPU utilisation baseline:** Target >60% average GPU utilisation for production
inference workloads. GPU nodes running at <30% average utilisation should be investigated
for consolidation, MIG partitioning, or time-slicing.

**NVIDIA MIG (Multi-Instance GPU):** MIG partitions a physical GPU into isolated slices
(e.g., A100 80GB can be partitioned into up to 7 independent 10GB instances). Each
MIG instance appears as a separate schedulable resource to Kubernetes. Benefits:
- Multiple pods share one physical GPU without contention
- Each slice has guaranteed memory and compute bandwidth
- DCGM Exporter reports per-MIG utilisation, enabling accurate cost attribution

**GPU time-slicing:** A lighter-weight sharing mechanism - multiple pods share a GPU
through time multiplexing. Unlike MIG, there is no memory isolation between tenants.
Suitable for development workloads where isolation is not required.

**Monitoring stack for GPU cost:**

| Layer | Tool |
|---|---|
| Node hardware labels and discovery | NVIDIA GPU Feature Discovery |
| Pod GPU utilisation metrics | NVIDIA DCGM Exporter + Prometheus |
| GPU memory per pod | DCGM Exporter `DCGM_FI_DEV_FB_USED` metric |
| Cost attribution | OpenCost or Kubecost with DCGM integration |
| GPU partitioning | NVIDIA MIG + NVIDIA GPU Operator |

---

## Governance checklist
<!-- doc:k8s-governance-checklist -->

**Visibility:**
- [ ] Deploy OpenCost or Kubecost for cluster cost visibility (per-namespace, per-label)
- [ ] Configure DCGM Exporter for GPU utilisation monitoring if GPU nodes are in use
- [ ] Integrate K8s cost data with cloud billing (FOCUS export or FinOps platform connector)
- [ ] Track cost per namespace and per team in weekly FinOps reviews

**Attribution:**
- [ ] Enforce mandatory labels via admission controller (OPA Gatekeeper or Kyverno)
- [ ] Define shared cost allocation model (proportional or fixed) and document it
- [ ] Apply namespace ownership labels on all namespaces (including system namespaces)

**Efficiency:**
- [ ] Set resource requests on all pods - no deployments without explicit CPU and memory requests
- [ ] Monitor request-to-actual ratio weekly; target <1.5× CPU, <1.3× memory
- [ ] Review node pool sizing monthly; flag pools below 50% average utilisation
- [ ] Enable VPA in `Off` mode to generate rightsizing recommendations
- [ ] Alert on namespaces with >50% resource waste (request-to-actual ratio >2×)

**Non-production:**
- [ ] Implement non-production scheduling (off-hours scale-down via KubeGreen or equivalent)
- [ ] Use Spot nodes for all non-production workloads
- [ ] Separate non-prod from prod clusters or enforce namespace-level resource quotas

**GPU:**
- [ ] Monitor GPU utilisation per pod via DCGM Exporter
- [ ] Enable NVIDIA MIG partitioning for GPU nodes running below 60% utilisation
- [ ] Apply GPU-specific labels to pods requesting GPU resources for attribution

---

## Decision framework: managed Kubernetes provider comparison
<!-- doc:k8s-provider-comparison -->

| Dimension | EKS (AWS) | AKS (Azure) | GKE (Google) |
|---|---|---|---|
| Control plane cost | $0.10/cluster/hr (~$72/month) | Free (standard) / $0.10/hr (premium w/ SLA) | $0.10/cluster/hr (~$72/month) |
| Default node types | EC2 (all families) | Azure VM (all families) | GCE (all families) |
| Spot node support | EC2 Spot via Karpenter or ASG | Azure Spot via VMSS | Spot VMs via GKE node pool config |
| GPU support | P, G, Inf families; NVIDIA + AWS Neuron | NC, ND families; NVIDIA only | A100, T4, L4 via accelerator node pools |
| Spot interruption notice | 2 minutes | 30 seconds (Eviction policy) | 30 seconds |
| Autoscaler options | Cluster Autoscaler, Karpenter | Cluster Autoscaler (KEDA add-on) | Cluster Autoscaler, GKE Autopilot |
| Cost tooling integration | OpenCost, Kubecost, Cost Explorer | OpenCost, Kubecost, Azure Cost Management | OpenCost, Kubecost, GCP Billing |
| FOCUS export | Via OpenCost or FinOps platform | Via OpenCost or FinOps platform | Via OpenCost or FinOps platform |
| Autopilot / serverless K8s | No native equivalent | ACI burst (limited) | GKE Autopilot (per-pod billing) |

**GKE Autopilot note:** GKE Autopilot bills per pod resource request rather than per
node, eliminating the node utilisation gap entirely for teams that adopt it. It is not
suitable for all workloads (GPU, host networking, privileged containers are restricted),
but it removes the need for node pool management and cluster autoscaler tuning for
compatible workloads.

---

> Sources: CNCF OpenCost documentation, Kubecost 3.0 release notes, NVIDIA MIG User Guide,
> KubeGreen documentation, FinOps Foundation Kubernetes working group, Karpenter documentation.

> *Cloud FinOps Skill by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
