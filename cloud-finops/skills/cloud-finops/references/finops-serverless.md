# FinOps for Serverless

> Serverless removes capacity decisions but introduces new cost traps. Pay-per-use sounds
> efficient until uncontrolled invocations, memory over-provisioning, and hidden ancillary
> costs accumulate. This reference covers the serverless cost model, cross-provider
> comparison, optimization patterns, and governance controls.

---

## The serverless cost model

### Billing dimensions

Serverless pricing is multidimensional. All three levers interact and must be understood
together.

| Billing dimension | AWS Lambda example | Notes |
|---|---|---|
| Invocations | $0.20 / 1M requests | First 1M free per month |
| Duration × Memory (GB-seconds) | $0.0000166667 / GB-second | Primary cost driver |
| Provisioned concurrency | $0.0000041667 / GB-second | Charged whether invoked or not |
| Data transfer | Varies by destination | Often overlooked at design time |

**Billing rounding:** AWS Lambda rounds duration up to the nearest 1 ms. At very short
execution times (<1 ms of actual compute), billing granularity can inflate effective cost
significantly. Academic benchmarks have measured up to 5.5× actual compute cost at
extreme short-duration workloads. In practice, functions running 10–100 ms experience
5–15% rounding inflation.

**GB-seconds math:**
```
Cost = (invocations × duration_seconds × memory_GB) × $0.0000166667

Example: 10M invocations × 0.2s × 0.512 GB = 1,024,000 GB-seconds = ~$17.07/month
```

### The hidden cost iceberg

Lambda/Functions compute charges are the visible tip. Ancillary costs frequently exceed
the compute line item in production workloads.

| Cost category | Typical culprit | Scale indicator |
|---|---|---|
| API Gateway | $3.50 / 1M REST API requests | High-traffic public APIs |
| CloudWatch Logs ingestion | $0.50 / GB ingested | Verbose logging, high invocation rate |
| CloudWatch Logs storage | $0.03 / GB stored | Default retention is infinite |
| NAT Gateway | $0.045 / GB processed | Lambda in VPC accessing the internet |
| VPC ENI creation | Delays and throttling risk | Lambda-to-VPC cold start overhead |
| Data transfer (cross-region) | $0.02–$0.09 / GB | Multi-region architectures |
| Step Functions | $0.025 / 1K state transitions | Complex orchestration workflows |
| SQS / SNS triggers | Per-request charges | High-fan-out event patterns |
| EventBridge | $1.00 / 1M events | Event-driven architectures |
| DynamoDB Streams | Read throughput charges | Lambda triggered by stream |

**Audit rule:** Run a monthly cost breakdown at the service level. If CloudWatch, API
Gateway, or NAT Gateway are not on the report, they are likely untagged or missed —
not free.

---

## Cross-provider comparison

| Dimension | AWS Lambda | Azure Functions | Google Cloud Run |
|---|---|---|---|
| Billing model | Invocations + GB-seconds | Invocations + GB-seconds (Consumption) | Requests + vCPU-seconds + memory-seconds |
| Free tier | 1M req + 400K GB-sec/month | 1M req + 400K GB-sec/month | 2M req/month |
| Min billing duration | 1 ms | 1 ms | 100 ms (min 1 request) |
| Max memory | 10 GB | 14 GB (Premium) | 32 GB |
| Max execution time | 15 minutes | 10 min (Consumption) / unlimited (Premium) | 3600 seconds (60 min default) |
| Cold start mitigation | Provisioned Concurrency, SnapStart | Premium plan always-warm, minimum instances | Min instances (billed when idle) |
| ARM / low-cost compute | Graviton2 (20–30% cheaper) | Not available on Consumption | Not applicable (container-based) |
| Batch / async support | SQS, EventBridge, async invoke | Durable Functions, Service Bus | Pub/Sub push, Cloud Tasks |
| Container image support | Yes (up to 10 GB) | Yes | Native (primary deployment model) |
| VPC integration | Yes (may add cold start) | Yes (Premium/Dedicated only) | Yes (Serverless VPC Access) |

**Decision rule for provider selection:** Evaluate total cost of ecosystem, not just
compute unit price. A cheaper per-GB-second rate is irrelevant if API Gateway, logging,
and networking add 3× overhead.

---

## Optimization patterns

### Memory rightsizing (highest impact)

Memory is the single most impactful lever available without architectural changes.

**Why memory affects more than memory:**
- AWS Lambda: memory allocation scales CPU proportionally. Doubling memory roughly
  doubles CPU, which can halve execution time.
- Net result: higher memory allocation can **reduce total cost** when functions are
  CPU-bound.

**Memory rightsizing process:**

1. Instrument function with execution time logging (duration in CloudWatch Logs)
2. Run AWS Lambda Power Tuning (open-source Step Functions state machine) across
   memory sizes: 128 MB → 256 → 512 → 1024 → 2048 → 3008 MB
3. Plot cost = invocations × duration × memory for each configuration
4. Select the memory size at the cost minimum, not the duration minimum
5. Validate against real traffic before applying to production

**Typical outcomes:**
- Compute-intensive functions (JSON parsing, image processing, ML inference): 20–30%
  cost reduction by increasing memory
- I/O-bound functions (waiting on network/database): minimal benefit from more memory;
  optimize at the I/O layer instead
- Functions with tight latency SLOs: accept higher cost at the duration minimum

**Anti-pattern:** Using the Lambda default (128 MB) in production without profiling.
128 MB is the lowest memory tier and often not the cheapest due to longer execution.

### ARM / Graviton migration

| Aspect | Detail |
|---|---|
| Cost saving | ~20% price reduction vs x86 at equivalent memory |
| Performance | Equal or better for most workloads |
| Runtimes supported | Python, Node.js, Java, Ruby, .NET, Go (custom runtime) |
| Runtimes NOT supported | Some older custom runtimes; verify before migrating |
| Code change required | None for interpreted runtimes; recompile for compiled languages |
| Rollout approach | Deploy to non-production first; validate behavior under load |

**Migration checklist:**
- [ ] Verify all dependencies are ARM-compatible (especially native modules in Node.js)
- [ ] Test with equivalent load to x86 baseline
- [ ] Update IaC (Terraform `architectures = ["arm64"]`, SAM `Architectures: [arm64]`)
- [ ] Monitor error rates and duration for 48 hours post-migration
- [ ] Confirm no behavior regressions in integration tests

### Event filtering and trigger optimization

Unproductive invocations are pure waste: the function runs, consumes GB-seconds, and
produces no business value.

**Filter at the source, not inside the function:**

| Trigger type | Filtering mechanism | What to filter |
|---|---|---|
| SQS | Message attribute filter policies | Route by message type before Lambda sees it |
| DynamoDB Streams | Event filter patterns (Lambda-side) | Only trigger on specific attribute changes, not all writes |
| EventBridge | Rule event patterns | Narrow event patterns to relevant source/detail-type |
| S3 | Event notification filters | Prefix and suffix filters on object key |
| SNS | Subscription filter policies | Attribute-based routing before Lambda invocation |
| Kinesis | Enhanced fan-out + Lambda filter | Filter by partition key or record content |

**Impact:** A DynamoDB table with 1,000 writes/minute where only 50 are relevant means
950 unproductive invocations/minute = 40.7M wasted invocations/month at full scale.

### Cold start cost management

Cold starts are primarily a **latency problem**, not a direct cost problem. However,
the mitigations for cold starts (provisioned concurrency) are a significant **cost
problem** if applied without discipline.

| Mitigation | Cost impact | When to use |
|---|---|---|
| Provisioned concurrency | Ongoing GB-second charge (idle) | Latency-critical endpoints only |
| Scheduled provisioned concurrency | Reduced by limiting to peak hours | Predictable traffic patterns |
| SnapStart (Java) | No additional cost | Java functions with >1s cold starts |
| Container image optimization | Reduces cold start duration | Reduce init time without ongoing cost |
| Package size reduction | Reduces cold start duration | Always applicable |
| Warm-up pings (manual) | Minimal invocation cost | Last resort; use SnapStart/PC instead |

**Provisioned concurrency cost formula:**
```
Monthly cost = concurrency_units × memory_GB × 730_hours × 3600 × $0.0000041667

Example: 10 units × 0.512 GB × 730h × 3600s = 13,496,832 GB-seconds = ~$56.24/month
```

**Rule:** Never apply provisioned concurrency 24/7 to handle traffic that is only peak
for 4–8 hours/day. Use Application Auto Scaling with scheduled scaling actions.

### Package optimization

| Technique | Impact | Effort |
|---|---|---|
| Remove unused dependencies | Reduces cold start (smaller init) | Low |
| Use Lambda Layers for shared libs | Enables layer caching; reduces per-function package size | Medium |
| Tree-shaking (Node.js / TypeScript) | Eliminates dead code from bundles | Low (esbuild / webpack) |
| Minification | Reduces package size 30–60% | Low |
| Split monolithic functions | Smaller packages; independent scaling | High (architectural) |
| Use slim base images (container) | Reduces cold start time | Low–Medium |

**Target:** Function deployment package under 5 MB for fast cold starts. Container
images under 500 MB.

### Architectural right-sizing: serverless vs. containers vs. VMs

Serverless is not always the cheapest option at scale. Evaluate against alternatives
before committing to a pattern.

| Workload characteristic | Best fit | Rationale |
|---|---|---|
| Sporadic / bursty (unpredictable) | Serverless | Pay-per-use wins vs. idle reserved capacity |
| Consistent 24/7 load (predictable) | Containers or VMs | Reserved/committed pricing beats per-invocation |
| Long-running (>15 min) | Containers (ECS/EKS) | Lambda 15-min limit; containers have no ceiling |
| GPU-required | VMs or Kubernetes | Lambda has no GPU support |
| High concurrency, low latency | Containers with HPA | Avoid provisioned concurrency overhead |
| Cost-sensitive at high scale (>1B req/month) | Evaluate breakeven | Calculate container equivalent cost |

**Breakeven calculation (Lambda vs. container):**
```
Lambda monthly cost = invocations × duration × memory × $0.0000166667
Container monthly cost = vCPU × hours × rate + memory × hours × rate

Crossover point typically occurs at sustained >60% utilization of an equivalent
container. Use AWS Pricing Calculator to model both sides.
```

---

## Cost visibility

Native per-function cost attribution is weak across all major providers. CloudWatch
Metrics and Cost Explorer report Lambda spend at the service level, not the function
level, by default.

**Strategies for per-function visibility:**

| Approach | Detail | Complexity |
|---|---|---|
| Resource tagging | Tag functions by team, product, environment | Low — apply at deploy time |
| Cost allocation tags | Enable tags in AWS billing, activate in Cost Explorer | Low |
| Application-level instrumentation | Log invocation cost = duration × memory / 1000 × rate | Medium |
| Third-party FinOps platforms | Cloudability, Apptio, Ternary — function-level attribution | High (procurement) |
| AWS Cost Explorer resource-level data | Enable per-resource data (additional $0.01/resource/day) | Medium |

**Estimation tools:**
- [serverlesscalc.com](https://serverlesscalc.com) — quick Lambda cost estimation
- AWS Pricing Calculator — model Lambda vs. container vs. EC2 breakeven
- Azure Pricing Calculator — Consumption vs. Premium plan comparison
- Infracost — IaC-integrated cost estimation for Terraform

**Cost anomaly detection for serverless:**
Set up AWS Cost Anomaly Detection monitors at the Lambda service level and per-account
level. Serverless costs can spike rapidly (recursive invocations, runaway event loops)
and anomaly detection is the primary safety net.

---

## Governance checklist

- [ ] Profile and set memory allocation based on Lambda Power Tuning, not defaults
- [ ] Set concurrency limits (`ReservedConcurrency`) on all functions to prevent runaway
      invocations consuming account-wide concurrency quota
- [ ] Monitor invocation count trends — unexpected spikes indicate trigger misconfiguration
      or recursive invocation patterns
- [ ] Audit for recursive invocation patterns (function triggering itself via S3, SQS,
      SNS, or DynamoDB Streams it also writes to)
- [ ] Review ancillary costs monthly (API Gateway, NAT Gateway, CloudWatch Logs) — they
      often exceed compute charges in high-traffic workloads
- [ ] Evaluate ARM/Graviton for all Lambda functions; migrate compatible runtimes
- [ ] Set CloudWatch Logs retention policies on all Lambda log groups (default: infinite)
- [ ] Run Lambda Power Tuning on all functions before production deployment
- [ ] Alert on any function exceeding $50/month — review for optimization potential
- [ ] Apply event source filters at the trigger layer to eliminate unproductive invocations
- [ ] Schedule provisioned concurrency — do not leave it on 24/7 for peak-hours-only traffic
- [ ] Tag all functions with Owner, CostCenter, and Environment at deploy time
- [ ] Review Step Functions and EventBridge state transition counts monthly
- [ ] Enforce maximum execution timeout per function — prevent accidental long-running
      invocations that inflate GB-second charges

---

> *Cloud FinOps Skill by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
