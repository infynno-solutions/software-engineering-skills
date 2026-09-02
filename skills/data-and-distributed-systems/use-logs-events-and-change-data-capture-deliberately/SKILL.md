---
name: use-logs-events-and-change-data-capture-deliberately
description: "Uses an append-only log or CDC stream as the integration mechanism between systems only when replay, auditability, ordering, or decoupled fan-out are genuinely needed, and designs its retention, partitioning, and delivery semantics to match consumers. Use when two services must stay in sync and the choice is dual-writes versus an event log, when introducing Debezium-style binlog tailing, or when a new Kafka topic's retention and delivery semantics are undecided. Not for the derived data's own correctness and rebuild path (see design-dataflow-and-derived-state), or the timing model of its consumers (see choose-batch-vs-stream-processing)."
license: MIT
---

# Use Logs, Events, and Change Data Capture Deliberately

## Intent
Use an immutable, append-only log or a change-data-capture stream as the mechanism for propagating changes between systems only when its actual benefits — replay, auditability, decoupled multi-consumer fan-out, ordering — are needed, and design its retention, partitioning, and delivery semantics to match how consumers will actually use it.

## Procedure
1. Identify the actual reason a log-based approach is being considered: replay/reprocessing (rebuild a derived store from history), auditability (an immutable record of what happened and when), or decoupled fan-out (multiple independent consumers reacting to the same change without the producer knowing about them).
2. If the real need is just "keep these two specific systems in sync" with a single consumer and no replay requirement, weigh whether a simpler mechanism (a transactional outbox with direct delivery, or a synchronous call with retries) meets the need with less operational overhead than a full log/streaming platform.
3. If using CDC to capture a database's changes, verify it captures the actual committed change stream (not periodic polling that can miss or coalesce rapid updates) and handles schema changes without dropping events.
4. Design the log's retention period around the actual replay requirement — "how far back must a new consumer be able to reprocess from" — not around a default retention setting picked without that question being asked.
5. Choose the partition/key strategy so that events which must be processed in order relative to each other (e.g., all updates to one entity) land in the same partition, since ordering is only preserved within a partition, not across the whole topic.
6. Decide and document the delivery semantics consumers must assume (at-least-once is the practical default) and require every consumer to be idempotent with respect to reprocessing or duplicate delivery.
7. Treat the log as the source of truth for anything meant to be replayable/rebuildable from it; if a consumer's derived state and the log ever disagree, the resolution is to replay the log, not to patch the derived state by hand.

## Decision rules
- Reach for an event log/CDC when more than one consumer needs the same change independently, when history must be replayable to rebuild derived state, or when an audit trail of what changed and when is a real requirement — not merely because "event-driven" is the team's default architecture style.
- Prefer CDC over application-level dual-writes when the source of truth is a database whose changes must be captured completely and in commit order; dual-writes are prone to the writer succeeding on one side and failing on the other with no atomicity.
- Set log retention based on the longest replay/reprocessing window any consumer (including a not-yet-built one) might need, and revisit retention explicitly whenever a new consumer with a different replay need is added.
- Key/partition events by the entity whose per-entity ordering matters; never assume cross-partition ordering, and never rely on wall-clock timestamps alone to reconstruct order across partitions.
- Require every consumer of the log to handle at-least-once delivery (duplicate events) and out-of-order arrival across partitions; a consumer that assumes exactly-once, strictly-ordered delivery without verifying the platform provides it will eventually corrupt its state.

## Anti-patterns
- Adding a Kafka topic and a streaming consumer for a simple one-producer-one-consumer sync that a transactional outbox or direct call would have solved with far less operational overhead.
- Application-level dual-writes to a database and a message queue in the same request without a transactional outbox, so a crash between the two writes silently loses or duplicates the event.
- Setting log retention to a platform default (e.g., 7 days) without checking whether any consumer — including future backfill/rebuild needs — requires replaying further back.
- Relying on a topic's overall arrival order to reconstruct causality across partitions, when the platform only guarantees order within a single partition.
- Treating an event log as disposable/transient after each consumer has processed it once, then discovering a new consumer or a rebuild need with no history left to replay.

## Exceptions and trade-offs
- CDC captures database changes but not application intent (why the change happened) — when the "why" matters to consumers (a reason code, a user-initiated action vs. a system correction), emit explicit domain events from the application in addition to or instead of raw CDC.
- Long retention for full replay capability has real storage cost and, for compacted topics, ongoing compaction overhead — that cost is justified when replay/audit is a genuine requirement, not a default to apply to every topic regardless of need.
- A synchronous call or direct dual-write, despite its atomicity/coupling downsides, is sometimes the right simpler choice when there is exactly one consumer, no replay need, and low latency between write and propagation matters more than decoupling.

## Verification
- Confirm the specific reason for using a log/CDC (replay, audit, fan-out) is stated, and that a simpler direct mechanism was considered and rejected for a stated reason.
- Confirm retention is set against an explicit replay-window requirement, not a platform default, and is revisited when a new consumer is added.
- Confirm every consumer is tested for idempotent handling of duplicate and out-of-order delivery within the platform's actual guarantees.
- If CDC is used, confirm it was tested against a schema change on the source table to verify it doesn't silently drop or misinterpret events.
