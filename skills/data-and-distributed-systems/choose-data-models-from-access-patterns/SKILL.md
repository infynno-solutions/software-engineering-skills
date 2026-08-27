---
name: choose-data-models-from-access-patterns
description: "Derives the logical data model - relational, document, graph, key-value, wide-column - from the concrete queries and mutations the application actually performs. Use when a new service must pick a model before the first table or collection, when deep join chains on the hot path or whole-document rewrites for one field signal the model is wrong, or when weighing denormalizing into embedded documents. Not for the physical engine underneath (see choose-storage-engines-by-workload), evolving a schema that already has live readers (see design-schema-and-encoding-evolution), or splitting data across nodes (see partition-data-with-explicit-trade-offs)."
license: MIT
---

# Choose Data Models From Access Patterns

## Intent
Derive the data model — relational, document, graph, key-value, or wide-column — from the concrete queries and mutations the application actually performs, so the model minimizes joins, N+1 lookups, or write amplification for the real workload.

## Procedure
1. List the application's actual queries and mutations, each annotated with frequency and latency sensitivity (e.g., "fetch order + line items: 10k/s, <50ms" vs. "generate monthly report: 1/day").
2. For each frequent, latency-sensitive query, identify whether it needs data that spans a hierarchy naturally owned together (favors document embedding), a graph of many-to-many relationships traversed at arbitrary depth (favors a graph model), simple key lookups (favors key-value), or ad hoc relational joins across many entity types (favors relational).
3. Identify which entities are updated independently and how often — data that changes together and is read together is a good candidate for embedding; data that changes independently but is read together is a better candidate for normalization with an explicit join or a denormalized read-side copy.
4. Check for access patterns that don't fit the leading candidate model at all (e.g., an occasional ad hoc analytical query against a document store) and decide whether those are served by a secondary index, a separate read replica/warehouse, or accepted as slow.
5. Prototype the model against the top 2-3 hottest queries with representative data volume before committing, since join cost and document growth both behave differently at scale than in a small sample.
6. Record the access patterns the model was chosen for, so a future reviewer can tell whether a new feature's query pattern still fits or requires re-evaluating the model.

## Decision rules
- If most reads fetch a whole aggregate (e.g., an order with its line items) and that aggregate is written together, prefer a document model with the aggregate embedded.
- If the same child entity must be read independently of its "parent" in other frequent queries, don't embed it — normalize it or duplicate it deliberately with a plan to keep copies consistent.
- If the dominant access pattern is traversing variable-depth relationships (social graphs, permission hierarchies, recommendation paths), prefer a graph model over simulating traversal with repeated joins.
- If access is purely by a single key with no need for secondary queries, a key-value store is simpler and cheaper than a general-purpose document or relational database.
- If the workload needs flexible, unanticipated ad hoc queries (BI, exploratory analytics) across many entities, prefer a relational or columnar model with strong join support over a document model that assumes access patterns are known in advance.
- Many-to-many relationships that are relational in nature (e.g., users and roles) usually don't need a graph database — they need a join table; reserve graph models for genuinely deep/variable traversals.

## Anti-patterns
- Picking a document database because "NoSQL scales better" without checking whether the access pattern actually involves whole-aggregate reads/writes.
- Embedding a frequently-and-independently-updated child entity inside a parent document, causing every unrelated update to rewrite the whole document and causing write contention.
- Modeling an inherently graph-shaped problem (deep, variable-depth relationships) as a relational schema with recursive self-joins that become unmanageable past a few hops.
- Normalizing aggressively in a document store out of relational habit, reintroducing the multi-document "joins" (application-side fan-out reads) the document model was chosen to avoid.
- Choosing the model based on a demo dataset an order of magnitude smaller than production, missing document-growth or join-fanout problems that only appear at scale.

## Exceptions and trade-offs
- A single service sometimes genuinely needs two models for two different access patterns (e.g., relational for transactional writes, a search index or graph for a specific query type) — that's a legitimate polyglot-persistence trade-off, not a failure to pick "the" model, as long as keeping them in sync is designed for explicitly.
- Denormalizing for a hot read path trades write complexity (keeping duplicates in sync) for read simplicity — only take that trade when the read path is hot enough, and prefer a mechanism (e.g., CDC-driven projection) that keeps the duplication consistent automatically rather than manually.
- Early-stage products with genuinely unknown access patterns may reasonably default to the most flexible model (usually relational) and defer specialization until real query patterns emerge.

## Verification
- Confirm the top hot-path queries were actually run against a data-volume-representative prototype of the chosen model, not just reasoned about abstractly.
- Confirm any denormalized/embedded copies have an explicit, tested mechanism for staying consistent with their source of truth.
- Confirm the chosen model doesn't require an unbounded-depth join or an unbounded-size document/collection to satisfy a stated frequent query.
- Confirm a reviewer can trace each hot query in the access-pattern list to the specific model feature (embedding, index, join, traversal) that serves it.
