---
name: partition-data-with-explicit-trade-offs
description: "Chooses a partitioning or shard key and rebalancing scheme that spreads load and storage evenly while making cross-partition cost an explicit trade-off. Use when sharding a multi-tenant, user-data, or events table as it outgrows one node; choosing a Kafka or Kinesis partition key that also determines ordering; or diagnosing a hot shard taking disproportionate load from a skewed key. Not for how many copies of a partition exist and how they stay in sync (see design-replication-for-the-required-guarantees), or an invariant that must span partitions once partitioning is chosen (see define-transaction-boundaries-and-isolation)."
license: MIT
---

# Partition Data With Explicit Trade-offs

## Intent
Choose a partitioning key and scheme so load and storage split evenly across nodes without creating hot spots, while making the cost of cross-partition operations and future rebalancing an explicit, reviewed trade-off rather than a surprise discovered under load.

## Procedure
1. Identify the dominant access pattern the partitioning must serve well — usually "fetch everything for entity X" (favors partitioning by that entity's ID) — and any secondary patterns that will become cross-partition scatter-gather queries.
2. Check the candidate partition key's cardinality and real-world distribution, not just its theoretical range: a key with a small number of distinct values, or one with a naturally skewed distribution (a celebrity user, a popular SKU, a monotonically increasing timestamp), produces a hot partition regardless of how many partitions exist.
3. For monotonically increasing keys (auto-increment IDs, timestamps) that would concentrate all new writes on one partition, either hash the key, add a random/sharded prefix, or partition on a different, better-distributed attribute.
4. Decide how the partition count will grow: fixed partition count sized generously up front (simpler, but a ceiling), or dynamic splitting/rebalancing (scales further, but requires an online rebalancing mechanism and routing layer that can move data without downtime).
5. Identify every query or transaction that would need to span multiple partitions under the chosen key, and decide explicitly how each is served: a scatter-gather fan-out, a secondary global index, or accepting it as an unsupported/slow path.
6. Design the routing layer (how a client/query finds which partition holds a given key) and make sure it's updated atomically with any rebalancing, so requests are never routed to a partition mid-move without a defined behavior.
7. Load-test with a production-representative key distribution (not uniformly random synthetic keys) before committing, since skew is exactly the failure mode uniform test data hides.

## Decision rules
- Partition by the entity most frequently fetched as a whole (e.g., partition an orders table by customer ID if "all of a customer's orders" is the hot query), not by an unrelated technical convenience like row insertion order.
- Never partition directly on a monotonically increasing key for a write-heavy workload; hash it or prefix it to spread writes, unless range-scan-by-that-key is the dominant read pattern and outweighs the write hot-spot risk.
- If a query needs to span all partitions (e.g., "find by email" when partitioned by customer ID), either maintain an explicit secondary/global index or accept and design for a scatter-gather query — don't leave it undesigned until it's slow in production.
- Choose dynamic rebalancing only when growth is expected to exceed a comfortably over-provisioned fixed partition count; the operational complexity of live rebalancing is a real cost, not a free scalability upgrade.
- Keep the partition count a multiple of (or otherwise cleanly divisible across) the node count so rebalancing can move whole partitions between nodes without repartitioning data.

## Anti-patterns
- Partitioning an events/logs table by a creation timestamp when writes are the dominant load, concentrating all current writes on the single "today" partition while every other partition sits idle.
- Choosing a partition key with very low cardinality (e.g., partitioning by a boolean status flag or a small enum), guaranteeing a small number of massively unbalanced partitions.
- Building a system that assumes queries only ever touch one partition, then discovering a business-critical query needs to scan every partition with no index or fan-out strategy designed for it.
- Rebalancing partitions by manually moving data with the routing layer unaware mid-move, causing requests to silently read stale or missing data during the move window.
- Assuming a hash-based partition key that "looks random" is actually well distributed without checking the real key distribution (e.g., hashing a field where 90% of records share one value).

## Exceptions and trade-offs
- Partitioning by a hot, low-distribution key is sometimes unavoidable for the primary access pattern (e.g., multi-tenant systems partitioned by tenant, where one tenant is far larger than others); the mitigation there is sub-partitioning the largest key(s) further, not abandoning the otherwise-correct partition scheme.
- A fixed, generously over-provisioned partition count trades some up-front resource cost for avoiding the operational complexity of a live rebalancing system — a reasonable choice when growth is bounded or predictable.
- Global secondary indexes that span all partitions reintroduce a form of the coordination/hot-spot problem partitioning was meant to solve for the indexed attribute — use them deliberately for genuinely necessary cross-partition queries, not as a default for every field.

## Verification
- Confirm the chosen partition key's real production (or production-representative) distribution was measured, not assumed, before committing.
- Load-test with realistic key skew and confirm no single partition receives disproportionate load relative to its peers.
- Confirm every cross-partition query the application needs has an explicit, tested serving strategy (secondary index or scatter-gather), not an unhandled gap.
- If dynamic rebalancing is used, confirm it was tested for correctness during an in-progress move (routing layer consistency, no dropped or duplicated requests).
