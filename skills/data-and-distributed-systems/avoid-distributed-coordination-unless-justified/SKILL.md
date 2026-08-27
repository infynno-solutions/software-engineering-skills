---
name: avoid-distributed-coordination-unless-justified
description: "Checks whether a single owner, an idempotent operation, or a conflict-resolution strategy can replace consensus, distributed locks, two-phase commit, or a coordination service. Use when a design proposes a Redis, ZooKeeper, or DB advisory lock to stop two workers doing the same thing, a PR adds etcd or Consul purely to elect a leader, or someone proposes 2PC or a saga coordinator to keep two services in sync. Not for how to replicate once coordination is genuinely needed (see design-replication-for-the-required-guarantees), what guarantee is required (see reason-explicitly-about-consistency), or making existing cross-node calls fail safely (see design-for-partial-failure-in-distributed-systems)."
license: MIT
---

# Avoid Distributed Coordination Unless Justified

## Intent
Prevent unnecessary consensus, distributed locking, and cross-service transactions by first checking whether the correctness requirement can be met with a single owner, an idempotent operation, or a conflict-resolution strategy instead.

## Procedure
1. Identify the invariant the coordination is meant to protect (e.g., "only one worker processes a job," "the counter is never double-incremented," "the leader is unique").
2. Check whether the invariant can be enforced locally: a single-writer partition, a database unique constraint, an idempotency key, or a natural leader (e.g., the process that owns a partition already owns serialization for it).
3. Check whether the operation can be made idempotent or commutative instead of mutually exclusive — if duplicate execution is harmless, no lock is needed at all.
4. If coordination still seems required, quantify the cost: added latency per operation, a new availability dependency on the coordination service, and the failure modes when that service is partitioned or slow.
5. If justified, pick the narrowest mechanism that satisfies the invariant (e.g., a database row lock instead of a global distributed lock; a fencing token instead of blind mutual exclusion) rather than defaulting to full consensus.
6. Document the invariant, why local/idempotent options were insufficient, and what happens if the coordination service is unavailable (fail closed vs. fail open).

## Decision rules
- If duplicate or out-of-order execution can be made harmless (idempotency keys, upserts, monotonic versions), do that instead of adding a lock.
- If ownership can be partitioned so each partition has exactly one writer, prefer partitioned ownership over a shared distributed lock.
- Use a lock only to protect a genuinely non-idempotent, non-commutative operation with real consequences from concurrent execution (e.g., charging a card twice).
- When a coordination service is introduced, treat it as a new availability dependency for every operation that touches it, not a free correctness upgrade.
- Prefer a fencing token or lease with a clear expiry over an unbounded lock, since network partitions can strand lock holders indefinitely.

## Anti-patterns
- Wrapping every cross-service write in a distributed lock "to be safe" instead of checking if the operation is already idempotent.
- Standing up a new ZooKeeper/etcd cluster for a single leader-election use case that a database row with `FOR UPDATE SKIP LOCKED` or a cloud provider's native leader-election primitive would solve.
- Using two-phase commit across service boundaries to keep data "in sync" instead of an idempotent retry plus reconciliation or a saga with compensating actions.
- Holding a distributed lock across a slow external call (network I/O, third-party API) so that one dependency outage stalls every other lock holder.
- Treating "the lock service was available in the demo" as proof the design tolerates partition and GC-pause scenarios in production.

## Exceptions and trade-offs
- Genuine leader election (e.g., a single active writer for a replicated log) legitimately needs consensus (Raft/Paxos-based) — the goal is to isolate that need to the smallest component, not eliminate it outright.
- Financial or safety-critical operations where a double-execution has real-world cost (double charge, double shipment) justify the latency and complexity cost of a coordination mechanism.
- Coordination-free designs often push complexity into reconciliation and conflict resolution instead — that trade is only a win if the application can tolerate eventual correctness and has a place to detect and fix conflicts.

## Verification
- Confirm the chosen mechanism was tested under the failure mode it exists to prevent (concurrent execution, network partition, coordinator restart) — not just the happy path.
- Confirm there is an explicit answer for what the system does when the coordination service itself is unavailable.
- Confirm any lock has a bounded lease/timeout and a fencing token, not an unbounded hold.
- Confirm the invariant being protected is written down somewhere reviewers can check against future changes.
