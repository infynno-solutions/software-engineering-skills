---
name: reason-about-partial-failure
description: "Works out what state a distributed operation might actually be in when some participants fail, stall, or become unreachable while others keep running. Use when an operation touches more than one service or database (update A then B, or write then publish an event), when a scatter-gather must define success with only some responses in, or when code treats a timeout as proof the remote operation did not happen. Not for what to serve to a user while degraded (see degrade-gracefully), preventing spread (see isolate-failures-and-limit-blast-radius), or making retried steps safe (see design-idempotent-operations); for the data-layer design version see design-for-partial-failure-in-distributed-systems."
license: MIT
---

# Reason About Partial Failure

## Intent
Design and reason about distributed operations with the explicit assumption that some participants can fail, be slow, or become unreachable while others continue running — so the system has a correct answer for every combination of outcomes, not just "it worked" or "it didn't."

## Procedure
1. For any operation spanning multiple participants, enumerate the outcomes explicitly: all succeeded, all failed, and every interesting subset in between (A succeeded but B didn't, A succeeded and B's result is unknown).
2. Recognize that "no response" is not the same as "it didn't happen" — a timeout means the outcome is *unknown*, not negative; the write may have landed on the other side. Do not code as if timeout implies failure.
3. Decide the consistency strategy for the operation as a whole: two-phase commit/distributed transaction (rare, expensive), saga with compensating actions, eventual consistency with reconciliation, or accept and design around a defined "in-between" state.
4. For fan-out calls, decide and document the quorum/completion semantics up front: is success "all responded," "majority responded," or "at least one responded" — and what happens to the stragglers that respond late or never.
5. Make partial-failure states detectable and reconcilable: log/record enough to later determine which participants actually completed, so an operator or automated reconciler can resolve ambiguity rather than it being lost.

## Decision rules
- Never infer "the remote side did nothing" purely from a timeout or connection error — the request may have arrived and been processed; use idempotency keys and post-hoc status checks to resolve ambiguity rather than assuming.
- Prefer sagas with compensating actions over distributed transactions for cross-service consistency in most application-level flows; reserve true distributed transactions for the narrow cases that truly require atomicity and can afford the coordination cost.
- For fan-out reads/writes, decide the acceptable completion threshold (all/majority/quorum/any) based on what the caller actually needs, not on whatever the client library defaults to.
- When a partial-failure state is detected, prefer converging to a known-consistent state through reconciliation over leaving it ambiguous indefinitely — an unreconciled partial state is a latent correctness bug.

## Anti-patterns
- Code that treats "the HTTP call threw a timeout exception" as equivalent to "the operation did not happen," then safely retries a non-idempotent write and creates a duplicate.
- A multi-step operation (write to DB, then call service B, then publish event) with no compensating action or reconciliation if step 2 or 3 fails after step 1 succeeded — leaving the system permanently inconsistent.
- Fan-out logic that silently treats "0 of 5 replicas responded in time" the same as "5 of 5 succeeded" because the code only checks for the absence of an exception, not the actual count/quorum.
- Assuming all nodes/services observe events or clock time in the same order, leading to logic that breaks under real network reordering or clock skew.

## Exceptions and trade-offs
- Full distributed-transaction consistency (2PC/XA) is available in some contexts but trades away availability and adds coordinator complexity; most systems are better served by sagas plus reconciliation, accepting a window of eventual consistency.
- Building explicit reconciliation logic for every possible partial-failure state adds real engineering cost; prioritize it for operations with financial, safety, or hard-to-reverse consequences, and accept simpler "log and alert a human" handling for low-stakes ones.
- Treating every timeout as "unknown" rather than "failed" is more correct but adds complexity (status-check calls, idempotency); for genuinely cheap-to-retry, side-effect-free operations, this rigor may not be worth it.

## Verification
- Confirm the design/code enumerates the interesting partial-outcome states for each multi-participant operation, not just "success" and "generic failure."
- Confirm no code path treats a timeout/connection error as proof-of-non-occurrence for a write; confirm there's a status-check or idempotent-retry story instead.
- Confirm fan-out operations have an explicit, tested completion threshold (all/quorum/any) rather than implicit behavior from the first response or the client library's default.
- Confirm a reconciliation or alerting path exists for partial-failure states that aren't automatically resolved, so ambiguity doesn't sit unnoticed.
