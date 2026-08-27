---
name: design-for-partial-failure-in-distributed-systems
description: "Designs cross-node calls and message consumers to stay correct when messages are delayed, duplicated, reordered, or dropped and nodes fail independently. Use when an RPC path ignores that a timeout may mean the call actually succeeded, a consumer assumes exactly-once in-order delivery, a retry policy is being added, or a zombie leader or twice-run job needs debugging. Not for how replicas of the same data handle node failure (see design-replication-for-the-required-guarantees) or whether to add coordination machinery at all (see avoid-distributed-coordination-unless-justified); for the incident-facing reliability version see reason-about-partial-failure."
license: MIT
---

# Design for Partial Failure in Distributed Systems

## Intent
Design cross-node communication so the system stays correct when messages are delayed, duplicated, reordered, or dropped, and when individual nodes crash, pause, or become unreachable independently — rather than assuming failures are clean, total, and simultaneously visible to everyone.

## Procedure
1. For every cross-node call (RPC, HTTP, message publish), explicitly enumerate the three possible outcomes: the call never reached the remote node, it reached and succeeded but the response was lost, or it reached and failed — and note that from the caller's perspective, a timeout cannot distinguish these.
2. Make the remote operation idempotent (safe to execute more than once with the same effect) wherever the caller might retry, using an idempotency key, a natural unique constraint, or a compare-and-set on a version.
3. For message consumers, determine the broker's actual delivery guarantee (at-most-once, at-least-once, exactly-once-within-broker) and design the consumer for at-least-once with idempotent processing unless the broker and configuration are verified to do otherwise.
4. Do not assume message order is preserved across partitions/consumers; if order matters for correctness, key messages so related ones land on the same ordered partition, and design the consumer to detect and handle out-of-order arrival explicitly.
5. Assume a node can be alive but unable to communicate (a network partition, a long GC pause) rather than only "up" or "down" — use fencing tokens or leases with expiry so a node that appears dead to others but is still running can't take unsafe action after being superseded.
6. Set explicit, bounded timeouts for every cross-node call, and define what the caller does on timeout (retry with backoff, fail the operation, degrade gracefully) rather than blocking indefinitely.
7. Test the design against actual fault injection — kill a node mid-operation, delay/drop/duplicate/reorder messages, partition the network — not just against the happy path.

## Decision rules
- Treat every cross-node call's outcome as one of {succeeded, failed, unknown} — code that only handles {succeeded, failed} will misbehave on timeout.
- Default to at-least-once delivery semantics and idempotent handlers; only rely on exactly-once if the specific broker/consumer combination provides a verified transactional guarantee end-to-end, including the side effect the handler performs.
- A node that hasn't responded is not the same as a node that is dead — never take an action (like promoting a new leader) that assumes the old one has stopped acting without a fencing mechanism to actually stop it.
- Use bounded timeouts and explicit backoff/retry budgets everywhere; an unbounded wait on a remote call turns one slow dependency into cascading failure for every caller.
- Prefer designs where duplicate delivery is harmless (idempotent writes, deduplication keys) over designs that try to guarantee no duplicates are ever delivered, since the latter is far harder to actually achieve across a real network.

## Anti-patterns
- A retry loop around a non-idempotent operation (e.g., "charge the card," "send the email") that can double-execute the side effect on timeout-then-retry.
- A leader-election scheme that promotes a new leader on missed heartbeats without fencing the old one, allowing a paused-then-resumed old leader to keep writing (split brain).
- A consumer that assumes messages from a queue/topic arrive in the exact order they were produced, without partitioning or sequencing to guarantee it.
- Code that treats an RPC timeout as equivalent to a clean failure and immediately compensates (e.g., refunds a payment) for an operation that may have actually succeeded on the far side.
- No timeout at all on a cross-node call, so a single unresponsive dependency exhausts a caller's thread/connection pool and takes down unrelated functionality.
- A design reviewed and tested only under "the network always works and nodes fail cleanly" — never validated against a deliberately delayed, duplicated, reordered, or dropped message, or a node paused mid-operation and resumed later.

## Exceptions and trade-offs
- Idempotency has a cost (deduplication storage, request tracking) that isn't free — for operations with truly no side effect (pure reads, purely commutative writes) it can be skipped, but that exemption should be an explicit, reviewed judgment, not an oversight.
- Exactly-once processing is achievable end-to-end in narrower cases (e.g., a single Kafka-to-Kafka pipeline with transactional producers/consumers) — when the whole path is verified to support it, it's a legitimate simplification over building idempotency by hand.
- Strict message ordering guarantees limit horizontal scalability (single partition = single consumer throughput); only pay that cost for the specific streams where order genuinely affects correctness.

## Verification
- Confirm every retried operation is idempotent or deduplicated, with a test that executes it twice and asserts the same end state.
- Confirm timeouts are set and bounded on every cross-node call, and that the caller's behavior on timeout is explicitly implemented and tested.
- Run a fault-injection test (kill a node mid-operation, or delay/duplicate/reorder/drop a message) and confirm the system reaches a correct end state.
- Confirm any leader/lock-holder mechanism uses fencing tokens or leases, and that a test simulates a paused-then-resumed node to confirm it can't act after being superseded.
