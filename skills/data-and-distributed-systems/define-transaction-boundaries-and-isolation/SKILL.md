---
name: define-transaction-boundaries-and-isolation
description: "Sets transaction boundaries around exactly the operations that must succeed or fail together, and picks the weakest isolation level that still prevents the anomalies the application cannot tolerate. Use for read-modify-write code vulnerable to lost updates, deciding whether writes across tables or services must be atomic or need a saga, or debugging a double-booking or overdrawn balance that only reproduces under concurrent load. Not for consistency across replicas, caches, and services (see reason-explicitly-about-consistency), or whether to reach for distributed-transaction machinery at all (see avoid-distributed-coordination-unless-justified)."
license: MIT
---

# Define Transaction Boundaries and Isolation

## Intent
Set transaction boundaries around exactly the operations that must succeed or fail together, and pick the weakest isolation level that still prevents the specific concurrency anomalies the application logic cannot tolerate.

## Procedure
1. Identify the invariant that must hold across the operations in question (e.g., "account balance never goes negative," "a seat is never double-booked").
2. Draw the transaction boundary around the minimal set of reads and writes needed to enforce that invariant atomically — no more (don't hold a transaction open across an external API call or user think-time) and no less (don't split a read-modify-write across two transactions).
3. Identify which concurrency anomaly would violate the invariant if it occurred: dirty read, non-repeatable read, lost update, or write skew, and pick the weakest isolation level (read committed, snapshot isolation/repeatable read, or serializable) that rules that specific anomaly out.
4. For read-modify-write sequences, prefer an atomic single-statement update (`UPDATE ... SET x = x + 1`), a `SELECT ... FOR UPDATE`, or a compare-and-set/optimistic-concurrency check over relying on isolation level alone to prevent a lost update.
5. For invariants that span multiple rows chosen by a predicate (e.g., "no two rows with the same non-null value," "sum of allocations ≤ total"), recognize this as a write-skew risk under snapshot isolation and use serializable isolation, an explicit lock, or a database constraint instead.
6. If the operations span multiple databases or services, do not assume a single ACID transaction is available — decide explicitly between a distributed transaction (rare, costly), an idempotent saga with compensating actions, or accepting a bounded window of inconsistency with reconciliation.
7. Document, next to the transaction, which anomaly it exists to prevent, so a future refactor doesn't loosen isolation without understanding what breaks.

## Decision rules
- Use read committed as the default for isolated single-row read-modify-write operations expressed as atomic statements — it's cheap and sufficient when there's no cross-row invariant.
- Use snapshot isolation / repeatable read when a transaction needs a consistent view across multiple reads within itself, but be aware it does not prevent write skew.
- Use serializable isolation (or an explicit predicate lock / unique constraint) whenever the invariant depends on a *set* of rows matching a condition, not just a single row's value.
- Never rely on an application-level check-then-act ("check no conflicting row exists, then insert") without either a unique constraint or serializable isolation — under weaker isolation two concurrent transactions can both pass the check.
- Keep transactions short and free of external I/O (HTTP calls, waiting on user input) — every millisecond a transaction holds locks is contention and latency for everyone else.
- When correctness spans a service boundary, don't reach for a distributed transaction by default; prefer idempotent operations plus a saga/compensating-action or an outbox pattern, and treat true two-phase commit as a last resort.

## Anti-patterns
- Reading a value, computing a new value in application code, then writing it back in a separate statement/transaction without a lock or compare-and-set — a textbook lost-update bug under concurrent load.
- Assuming "repeatable read" or "snapshot isolation" prevents all anomalies, then getting bitten by write skew (e.g., two on-call engineers each check "someone else is on call" and both go off-call).
- Wrapping a transaction around a slow external call (payment gateway, email send), holding row locks for the duration and starving other transactions.
- Splitting a single invariant's enforcement across multiple transactions "for performance," reintroducing the race condition the original single transaction prevented.
- Reaching for two-phase commit across services as the default answer to "keep these two systems in sync" without first evaluating an idempotent saga or outbox-based approach.

## Exceptions and trade-offs
- Serializable isolation gives the strongest guarantee but costs throughput (via locking or abort-and-retry under optimistic schemes); reserve it for the specific transactions with a real write-skew or phantom-read risk rather than applying it globally.
- Long-running business processes (multi-day order fulfillment, multi-step onboarding) should almost never be a single database transaction — model them as an explicit state machine with idempotent steps instead.
- Optimistic concurrency control (version column + compare-and-set) can substitute for pessimistic locking or serializable isolation when conflicts are rare, trading occasional client-visible retries for lower lock contention.

## Verification
- Confirm every read-modify-write sequence is either a single atomic statement, protected by an explicit lock, or protected by a version-based compare-and-set.
- Confirm the isolation level chosen for each transaction is justified against the specific anomaly (dirty read / non-repeatable read / lost update / write skew) it needs to prevent, not chosen by default.
- Load-test invariant-critical transactions under realistic concurrency (not single-threaded tests) to confirm the invariant actually holds, since anomalies only manifest under concurrent execution.
- Confirm no transaction holds open across network I/O to an external system.
