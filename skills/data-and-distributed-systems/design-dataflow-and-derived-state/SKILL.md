---
name: design-dataflow-and-derived-state
description: "Treats every cache, materialized view, denormalized table, or search index as derived data with an explicit source of truth, transformation, and tested rebuild path. Use when adding a Redis, in-process, or CDN cache with no answer yet on what invalidates it and what staleness is acceptable; when introducing a materialized view or Elasticsearch index; or when data is right in one place and wrong in another. Not for the propagation mechanism itself (see use-logs-events-and-change-data-capture-deliberately) or the pipeline's timing model (see choose-batch-vs-stream-processing)."
license: MIT
---

# Design Dataflow and Derived State

## Intent
Treat every cache, materialized view, denormalized copy, or precomputed aggregate as derived data with an explicit source of truth, a defined transformation, and a tested rebuild path, so staleness and inconsistency are a known, bounded property rather than a surprise.

## Procedure
1. For each piece of derived data, name its single source of truth explicitly — the table, event stream, or system that is authoritative if the derived copy and the source ever disagree.
2. Define the transformation from source to derived form as a pure, deterministic function of the source data wherever possible, so it can be recomputed identically from scratch.
3. Decide and document the staleness bound the derived data is allowed to have (e.g., "search index may lag writes by up to 30 seconds") — an unstated staleness bound means no one can tell a bug from expected behavior.
4. Design the update path: is the derived data refreshed synchronously on write, asynchronously via a queue/CDC stream, or recomputed on a schedule? Match this to the staleness bound from step 3.
5. Build and test a full rebuild path — a way to regenerate the derived data entirely from the source of truth — before the feature ships, not after the first time it drifts out of sync in production.
6. Add a way to detect drift (a checksum, a row-count comparison, a periodic reconciliation job) between the derived data and its source, rather than relying on users to report wrong numbers.
7. Make sure downstream consumers of the derived data know it's derived (naming, documentation) so no one later treats it as an independent source of truth and starts writing to it directly.

## Decision rules
- Every piece of derived data must have exactly one documented source of truth; if two derived stores disagree, the source of truth — never the derived data — wins.
- If a rebuild-from-scratch path doesn't exist and can't be built, that's a sign the "derived" data is actually acting as a second source of truth, and it needs to be treated (and protected) as such.
- Prefer deriving from an immutable append-only source (an event log, a CDC stream) over deriving from a mutable table snapshot when the transformation needs to be replayed deterministically.
- Synchronous updates (update cache/view in the same transaction as the source write) give tighter consistency but couple the derived store's availability to the write path; asynchronous updates decouple availability at the cost of a staleness window — choose deliberately, not by default.
- Never allow writes directly to derived data; all writes go to the source of truth, and the derived data only ever reflects it.

## Anti-patterns
- Adding a cache with no invalidation strategy beyond a TTL "that seems fine," with no one able to say what staleness window it actually produces.
- A materialized view or search index with no rebuild job, discovered only when it drifts out of sync and the team realizes there's no way to regenerate it short of manual data surgery.
- Two services each maintaining their own "authoritative" copy of the same conceptual data, with no agreed single source of truth and periodic manual reconciliation to paper over divergence.
- A denormalized read table that accepts direct writes from a "fast path" in addition to being derived from the source, so it silently becomes a second, undocumented source of truth.
- Building the transformation as a non-deterministic or side-effecting process (e.g., calling a live external API mid-transformation) that can't be replayed identically for a rebuild.

## Exceptions and trade-offs
- Full rebuild is sometimes prohibitively expensive (petabyte-scale reindex); in that case, invest instead in incremental repair (reconciling only detected drift) and be explicit that full rebuild is a last resort with a known, accepted cost.
- Synchronous dual-writes to source and derived store in one transaction eliminate staleness but only work when both live in the same transactional system; across service/database boundaries this isn't available and an asynchronous, eventually-consistent design (with its staleness window) is the honest trade-off.
- Some derived data (e.g., approximate counts, trending scores) doesn't need to be exactly reconstructable from source — when that's true, say so explicitly rather than half-heartedly trying to keep it exact.

## Verification
- Confirm every derived store's source of truth and staleness bound is written down somewhere a new engineer would find it.
- Actually run the rebuild-from-scratch path in a test or staging environment and confirm it produces data matching the source of truth.
- Confirm a drift-detection mechanism exists and has been exercised (e.g., deliberately desynced in a test) to verify it actually flags disagreement.
- Confirm no code path writes to the derived store other than the designated transformation/update path.
