---
name: choose-batch-vs-stream-processing
description: "Chooses batch, streaming, or a hybrid pipeline from the job's actual latency, reprocessing, and state requirements. Use when designing a new ETL/ELT job and weighing a nightly Spark or dbt run against Flink or Kafka Streams, when a feature is called real-time without anyone checking the latency requirement, or when an expensive streaming job might be a much simpler batch job. Not for structuring the derived data and its rebuild path once the model is chosen (see design-dataflow-and-derived-state), or for whether an event log or CDC should be the source of the data (see use-logs-events-and-change-data-capture-deliberately)."
license: MIT
---

# Choose Batch vs Stream Processing

## Intent
Match the processing model — batch, stream, or hybrid — to the pipeline's actual latency and correctness requirements instead of defaulting to whichever paradigm the team already knows.

## Procedure
1. Write down the actual latency requirement in concrete units (e.g., "dashboard must reflect events within 5 minutes," not "as real-time as possible") — most stated real-time needs turn out to be soft.
2. Determine whether the computation needs to see out-of-order or late-arriving data corrected after the fact, and how much reprocessing/backfill capability that implies.
3. Estimate the state the computation must hold (windowed aggregates, joins across streams) and whether that state fits comfortably in a streaming engine's state store or needs a full table scan.
4. Weigh operational cost: a batch job restarted on failure is simple to reason about; a long-running streaming job needs monitoring for consumer lag, backpressure, and stateful failure recovery.
5. If requirements are mixed (some consumers need low latency, others need full historical correctness), consider a hybrid: a streaming path for fast approximate results plus a batch path that recomputes the authoritative result, reconciling the two explicitly.
6. Choose the simplest model that meets the stated latency bound, and record the latency requirement in the design so a future change to "make it faster" has a number to justify against.

## Decision rules
- If the consumer polls or refreshes on a schedule (dashboard refreshed hourly, daily report), batch on that same schedule — streaming buys nothing the consumer can observe.
- If correctness depends on late data arriving out of order and must be corrected retroactively, streaming needs watermarks and allowed lateness explicitly configured; if the team isn't prepared to reason about that, batch is often more correct by default.
- If the same logic must run in both a batch backfill and a live stream, prefer a single codebase/framework (Beam-style unified model, or a stream engine with a batch-replay mode) over hand-maintaining two implementations that can drift apart.
- Reprocessing a batch job is usually just "run it again on the range"; reprocessing a streaming job requires either replaying from a retained log or accepting the streaming state as final — decide which up front.
- Prefer batch as the default for anything without a hard sub-minute latency requirement; the operational and correctness overhead of streaming (state stores, checkpointing, exactly-once semantics) is not free.

## Anti-patterns
- Building a Kafka Streams/Flink pipeline for a report that's only ever looked at once a day.
- Running a "streaming" job that actually micro-batches every 30 seconds and calling it real-time while incurring full streaming operational cost.
- Ignoring late/out-of-order events in a streaming job and shipping numbers that silently diverge from the batch-computed "true" answer with no reconciliation.
- Choosing streaming because it feels more modern, without a stated latency requirement anyone signed off on.
- Building a Lambda architecture (separate batch and speed layers) without a plan to reconcile or eventually retire the divergence between the two, leaving two subtly different answers to the same question in production.

## Exceptions and trade-offs
- Fraud detection, alerting, and other action-triggering pipelines genuinely need stream processing regardless of team familiarity, since the value of the detection decays sharply with delay.
- A Kappa architecture (stream-only, batch is just "replay the log from the start") can remove the batch/stream duality but requires the log to retain enough history to replay, which has its own storage cost.
- Hybrid designs cost more to build and operate than either pure approach; only take that cost when different consumers of the same data genuinely have different latency requirements that can't be served by the faster path alone.

## Verification
- Confirm the chosen architecture's actual latency was measured end-to-end (source event to consumer-visible result), not just the processing engine's internal throughput.
- Confirm there is a defined and tested backfill/reprocessing procedure for the chosen model.
- If streaming was chosen, confirm out-of-order handling (watermarks, allowed lateness) is configured and tested with deliberately delayed events.
- If a hybrid was chosen, confirm there is a reconciliation process and that discrepancies between the fast and authoritative paths are monitored, not silently ignored.
