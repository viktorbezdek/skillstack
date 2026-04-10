# FinOps for Data Platforms

> Databricks and Snowflake have dedicated references in this skill. This file covers the other data platforms that generate significant cloud spend: event streaming (Kafka/MSK), search and analytics (Elasticsearch/OpenSearch), and in-memory data stores (Redis/Valkey).

---

## Event Streaming: Kafka and MSK

### Cost model

| Component | MSK | Confluent Cloud | Self-managed Kafka |
|---|---|---|---|
| Compute | Broker instance hours | CKU consumption units | EC2/VM instance hours |
| Storage | EBS volumes per broker | Storage included in CKU | EBS or instance storage |
| Data transfer | Cross-AZ + egress charged separately | Included in CKU up to limits | Cloud provider rates apply |
| Management | AWS-managed control plane | Fully managed | Full infrastructure ownership |

**MSK pricing levers:** broker instance type, storage provisioned per broker, cross-AZ replication traffic, data transfer out.

**Confluent Cloud pricing lever:** CKU count. One CKU supports approximately 250 Mbps ingress and 750 Mbps egress. CKUs scale independently of the number of topics or partitions.

### The cross-AZ cost trap

Kafka replicates every partition across brokers. In a standard three-AZ deployment, every byte written is replicated to two additional brokers — brokers that are, by default, in different Availability Zones. The result: cross-AZ data transfer fees that are invisible in Kafka metrics and only visible in cloud networking billing.

**In some deployments, cross-AZ networking fees represent 80–90% of total Kafka infrastructure cost.** This is the single most common overlooked cost driver in Kafka deployments.

How it compounds:
- Replication factor of 3 means each byte crosses AZ boundaries twice
- High-throughput topics amplify the effect proportionally
- Producers and consumers in different AZs from their assigned partition leaders add additional cross-AZ reads

### MSK vs. Confluent Cloud economics

| Dimension | MSK | Confluent Cloud |
|---|---|---|
| Management overhead | AWS handles broker patching, ZooKeeper/KRaft; teams manage topics, configs | Fully managed including connectors and Schema Registry |
| Pricing model | Instance hours + storage + networking | CKU-based; consumption-linked but not linear |
| Cross-AZ costs | Charged at full AWS data transfer rates | Included in CKU up to egress limits |
| Tiered storage | MSK Tiered Storage (move cold data to S3) | Confluent Infinite Storage |
| Auto-scaling | Manual broker scaling; MSK Serverless for unpredictable workloads | Automatic within CKU model |
| Cost predictability | Higher variability (networking costs fluctuate) | More predictable for stable throughput |
| Best fit | Stable throughput, AWS-native architecture | Variable workloads, managed operations priority |

### Optimization patterns

1. **Right-size broker instances** — monitor actual CPU, memory, and disk I/O; MSK brokers are frequently overprovisioned relative to observed utilization.
2. **Enable tiered storage for cold data** — MSK Tiered Storage and Confluent Infinite Storage move inactive data to S3-backed storage at significantly lower cost; hot data stays on broker EBS.
3. **Optimize partition count** — over-partitioned topics increase replication traffic volume and broker memory overhead; audit topics with partition counts far exceeding consumer parallelism needs.
4. **Review retention periods** — the default 7-day retention is often excessive; topics used for event-driven microservices frequently need hours, not days; reduce where applicable.
5. **Co-locate producers and consumers in the same AZ** — use consumer group assignment and producer configuration to minimize cross-AZ reads and writes; this directly reduces networking costs.
6. **Use compression** — LZ4 or zstd reduce wire transfer volume; zstd achieves better compression ratios at comparable CPU cost to LZ4; configure at the producer level.
7. **Consider MSK Serverless for low-throughput topics** — Serverless eliminates broker management and idle capacity cost for topics with unpredictable or intermittent throughput; not suited for latency-sensitive workloads.
8. **Monitor consumer lag** — persistent consumer lag indicates consumers are falling behind; unprocessed data generates ongoing storage cost and may eventually trigger reprocessing, which multiplies compute cost.

### Diagnostic questions for Kafka/MSK

1. What percentage of total Kafka cost appears in networking billing vs. compute and storage?
2. Are producers, consumers, and partition leaders co-located in the same AZ?
3. What is the average partition count per topic relative to consumer group parallelism?
4. Which topics have retention periods exceeding actual downstream consumption patterns?
5. Is tiered storage enabled on MSK clusters with large cold data volumes?

---

## Search and Analytics: Elasticsearch / OpenSearch

### Cost model

| Component | Billing basis |
|---|---|
| Data nodes | Instance hours (instance type × count) |
| Dedicated master nodes | Instance hours (3 or 5 nodes recommended for production) |
| UltraWarm nodes | Instance hours (S3-backed; lower instance cost than hot) |
| Cold storage | S3 storage only (no running instances) |
| EBS storage (hot tier) | GB-month for gp2/gp3 volumes attached to data nodes |
| Data transfer | Standard cloud provider rates |
| OpenSearch Serverless | OCU-hours for indexing and search independently |

**OpenSearch Serverless minimum floor:** approximately $350/month at minimum OCU allocation. This makes it unsuitable for small or development workloads where a traditional two-node cluster would cost a fraction of that.

### Data tiering (highest-impact lever)

| Tier | Storage type | Cost relative to hot tier | Query latency | Use case |
|---|---|---|---|---|
| Hot | SSD/EBS attached to data nodes | 1× (baseline) | Lowest | Active queries, recent data, real-time analytics |
| UltraWarm | S3-backed, managed by AWS | ~0.1× (up to 90% cheaper) | Higher (S3 fetch) | Infrequent queries, historical data, compliance lookups |
| Cold | S3 directly | ~0.03× | High (manual attach required) | Archival, regulatory retention, rarely queried |

Moving indices from hot to UltraWarm is typically the single highest-ROI action available in an Elasticsearch/OpenSearch deployment. Most organizations with time-series data have weeks or months of hot-tier indices that are queried rarely or not at all.

### Optimization patterns

1. **Implement index lifecycle policies** — configure ISM (Index State Management) on OpenSearch or ILM on Elasticsearch to automatically transition indices to UltraWarm after 7–30 days and cold storage after 90+ days; this should be applied cluster-wide via index templates.
2. **Right-size data nodes** — monitor JVM heap utilization (target 50–75% under load), disk utilization, and CPU; over-provisioned data nodes are common and frequently the largest cost line item.
3. **Use Graviton instances** — Graviton-based instance families (e.g., `r6g`, `m6g`) provide 15–20% price-performance improvement over equivalent x86 instances for most Elasticsearch/OpenSearch workloads.
4. **Apply Reserved Instances for stable workloads** — data nodes running continuously are strong RI candidates; 1-year no-upfront RIs typically yield 31–36% savings; 3-year no-upfront yield 52%+ vs on-demand.
5. **Optimize shard sizing** — target 10–50 GB per shard; shards smaller than 1 GB waste heap on overhead; shards larger than 50 GB slow recovery and rebalancing; over-sharding is a common antipattern inherited from Elasticsearch 2.x guidance.
6. **Review index retention** — delete indices that are no longer queried; a retention policy meeting data classification requirements is preferable to keeping all indices indefinitely.
7. **Disable replicas on non-production clusters** — replica shards double storage and compute cost; development and staging clusters rarely need replica redundancy.
8. **Use index templates to enforce lifecycle policies** — manually applying ISM policies to individual indices is error-prone; templates ensure all new indices inherit the correct lifecycle from creation.
9. **Evaluate OpenSearch Serverless fit carefully** — the minimum OCU floor (~$350/month) makes Serverless cost-effective only for genuinely bursty, unpredictable workloads with throughput spikes that would require significant over-provisioning on traditional clusters.
10. **Audit for extended support pricing** — AWS charges additional fees for clusters running Elasticsearch versions past end-of-standard-support; older versions are also a security risk; upgrade cadence should be tracked.

### Real-world reference

Octus achieved an 85% infrastructure cost reduction by migrating to Amazon OpenSearch Service and implementing proper data tiering with UltraWarm for historical data. The savings came primarily from eliminating over-provisioned hot-tier nodes holding data that had not been queried in months.

### Diagnostic questions for Elasticsearch / OpenSearch

1. What percentage of total index count is older than 30 days and still on hot-tier EBS storage?
2. Is UltraWarm enabled on the cluster? What is the current hot-to-UltraWarm ratio?
3. What is the average shard size across the top 10 largest indices?
4. Are dedicated master nodes right-sized relative to cluster scale (node count, index count)?
5. Is the cluster running an Elasticsearch version subject to extended support charges?
6. Are ISM/ILM policies applied cluster-wide via templates, or manually on individual indices?

---

## In-Memory Data Stores: Redis / Valkey

### The Redis-to-Valkey opportunity

In March 2024, Redis Ltd. changed the Redis license from BSD-3-Clause to a dual-license model (RSALv2 + SSPLv1). This triggered an immediate fork: **Valkey**, governed under BSD-3-Clause and backed by AWS, Google, Oracle, Ericsson, and others under the Linux Foundation.

Valkey maintains full API and data format compatibility with Redis. AWS introduced ElastiCache for Valkey and MemoryDB for Valkey with meaningfully lower pricing than their Redis equivalents.

**Savings available today with zero application changes:**
- ElastiCache Serverless: **33% lower** pricing for Valkey vs. Redis
- ElastiCache node-based: **20% lower** pricing for Valkey vs. Redis
- Full API compatibility: standard Redis commands work against Valkey endpoints without modification
- In-place upgrade path available: zero-downtime migration supported

**Estimated annual savings:** ~$6,000/year per average customer; $100K+/year for large enterprise deployments with significant Redis fleet size.

### Cost model comparison

| Dimension | ElastiCache Redis | ElastiCache Valkey | MemoryDB Valkey |
|---|---|---|---|
| Pricing tier | Standard | 20–33% lower than Redis | Comparable to MemoryDB Redis |
| Serverless pricing | Higher baseline | 33% lower | N/A |
| Node-based pricing | On-demand + RI available | 20% lower on-demand | On-demand + RI available |
| Durability | In-memory + optional persistence | In-memory + optional persistence | Durable (multi-AZ transaction log) |
| Use case | Caching, sessions, pub/sub | Caching, sessions, pub/sub (Redis replacement) | Durable primary database workloads |
| License | Proprietary (RSALv2 + SSPLv1) | Open source (BSD-3-Clause) | Open source (BSD-3-Clause) |

### Optimization patterns

1. **Migrate to Valkey** — this is the single highest-ROI action available for Redis users on AWS; 20–33% savings with zero application code changes; in-place upgrade path minimizes operational risk.
2. **Right-size node types** — monitor memory utilization and connection count; the most common mistake is over-provisioning memory to avoid evictions rather than tuning eviction policies appropriately.
3. **Use Reserved Nodes for stable workloads** — ElastiCache Reserved Nodes provide significant discounts vs. on-demand for clusters with predictable, continuous usage patterns.
4. **Enable data tiering for large datasets** — ElastiCache data tiering extends in-memory capacity by spilling infrequently accessed data to NVMe SSD; effective for datasets 2–5× larger than available DRAM.
5. **Review Multi-AZ replication on non-production clusters** — replica nodes and cross-AZ replication double or triple cluster cost; non-production environments rarely require production-grade availability.
6. **Set appropriate eviction policies** — `allkeys-lru` or `volatile-lru` prevent OOM-triggered scaling events; clusters configured with `noeviction` on cache workloads are at risk of runaway scaling.
7. **Monitor cache hit ratios** — a hit ratio below 80% on a caching cluster indicates the dataset is too large, the TTL is too short, or the key design is ineffective; a low hit ratio means the cluster is paying for memory it is not benefiting from.
8. **Audit for idle clusters** — development and test ElastiCache clusters are frequently left running after the work is complete; schedule automated audits to identify clusters with zero connections over 72-hour windows.

### Migration checklist: Redis to Valkey

- [ ] Verify application uses standard Redis commands (no Redis-specific proprietary modules such as RedisSearch, RedisJSON native modules — standard commands work, commercial modules do not)
- [ ] Identify all ElastiCache clusters and MemoryDB clusters running Redis engine
- [ ] Estimate savings: multiply current Redis monthly spend by 0.20–0.33 for Valkey discount
- [ ] Test in non-production by creating a Valkey cluster and pointing a test environment at the new endpoint
- [ ] Validate application behavior under the Valkey endpoint (connection handling, pipelining, Lua scripts)
- [ ] Execute in-place upgrade for each production cluster (zero-downtime path)
- [ ] Update monitoring dashboards and CloudWatch alarms to reference new cluster names/metrics
- [ ] Verify backup and snapshot compatibility post-migration
- [ ] Update IaC templates (Terraform `engine = "valkey"`, CloudFormation `Engine: valkey`)
- [ ] Track cost delta in the billing console for 30 days post-migration to confirm savings

---

## Cross-platform governance checklist

- [ ] Inventory all data platform services (MSK, Elasticsearch/OpenSearch, ElastiCache) and their monthly spend by service
- [ ] Identify cross-AZ data transfer costs in networking billing — attribute to specific Kafka clusters or services
- [ ] Review retention and lifecycle policies for all data stores (Kafka topic retention, index lifecycle policies, Redis TTLs)
- [ ] Evaluate Redis-to-Valkey migration for all ElastiCache Redis and MemoryDB Redis deployments — document estimated savings
- [ ] Implement data tiering on all Elasticsearch/OpenSearch clusters with data older than 30 days on hot tier
- [ ] Right-size Kafka brokers using throughput metrics from the last 30 days (CPU, network I/O, disk I/O)
- [ ] Apply Reserved Instances or Savings Plans to stable data platform workloads with predictable usage
- [ ] Use Graviton/ARM instances for Elasticsearch/OpenSearch where workloads are compatible
- [ ] Disable replica nodes and Multi-AZ replication on all non-production ElastiCache clusters
- [ ] Enforce shard sizing targets on Elasticsearch/OpenSearch (10–50 GB per shard) via index templates

---

> *Cloud FinOps Skill by [OptimNow](https://optimnow.io) and [Viktor Bezdek](https://github.com/viktorbezdek) - licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
