---
name: reason-explicitly-about-consistency
description: "Replaces vague strongly consistent or eventually consistent claims with the specific guarantee a client needs - linearizability, read-your-writes, monotonic reads, causal - and confirms the datastore or API actually provides it under real failure modes. Use when a design doc or PR uses those labels without saying which reads see which writes, when a user's own write appears lost or two reads go backward in time, or when justifying the latency cost of a strongly consistent call. Not for the replication mechanism that delivers the guarantee (see design-replication-for-the-required-guarantees), or anomalies within one database's transactions (see define-transaction-boundaries-and-isolation)."
license: MIT
---

# Reason Explicitly About Consistency

## Intent
Replace vague claims of "strongly consistent" or "eventually consistent" with the specific guarantee a client actually requires — linearizability, read-your-writes, monotonic reads, causal consistency, or none — and confirm the datastore or API in use actually provides that guarantee under the failure modes it will encounter.

## Procedure
1. For the specific data path in question, name the actual guarantee needed using a precise term, not "strong" or "eventual": does the client need to see its own writes immediately (read-your-writes), never see time go backward across reads (monotonic reads), see causally related writes in order (causal consistency), or does staleness genuinely not matter for this path?
2. Identify which client and which reads the guarantee applies to — a guarantee is almost always about a specific (client, read) relationship, not a property of the whole system ("is the system consistent" is rarely a well-formed question).
3. Check what the actual datastore/API being used provides by default for that operation — read replicas, caches, and eventually-consistent APIs (e.g., S3 list operations, DNS, many managed NoSQL default read paths) frequently provide weaker guarantees than engineers assume.
4. If the required guarantee is stronger than the default, choose the specific mechanism to close the gap for just that read path: route to the primary/leader, use a "read your own writes" session token, use quorum reads, or add a sticky-session/session-consistency layer — rather than making the whole system stronger than necessary.
5. Where staleness is genuinely acceptable, state the bound explicitly (e.g., "may lag by up to N seconds") so it's a documented property, not an unstated assumption a future engineer trips over.
6. Write a test that actually exercises the guarantee under the condition that would violate it (concurrent writers, a lagging replica, a network delay) rather than only testing the single-threaded happy path where every consistency model looks the same.

## Decision rules
- Never describe a guarantee as "eventually consistent" without stating a bound or a convergence condition — "eventually" with no bound is not a testable claim and usually really means "we haven't measured it."
- Default every user-facing "did my action take effect" read path to read-your-writes at minimum; a user who just submitted a form and sees it missing on refresh will file a bug regardless of what the backend theoretically guarantees.
- Reserve linearizability (every operation appears to take effect atomically at some point between its start and end, visible identically to all clients) for cases that truly need it (e.g., a uniqueness constraint enforced across nodes) — it is the most expensive guarantee to provide and rarely required for read paths.
- When in doubt about what a managed service actually guarantees for a given operation, check its documentation for that specific operation rather than assuming "the database" is uniformly strongly or eventually consistent across every API it exposes.
- If two different guarantees are needed for two different reads of the same data (e.g., "the settings page must be read-your-writes, the analytics dashboard can be a minute stale"), give each its own explicit designation rather than picking one guarantee for the whole dataset.

## Anti-patterns
- Writing "this system uses eventual consistency" in a design doc with no statement of how eventual, under what conditions, or which reads it applies to.
- Assuming a "strongly consistent" label on a database means every read from every API it exposes is linearizable, when in practice some of its read paths (e.g., list/scan operations, cached metadata) are weaker by design.
- Reading immediately after writing from a replica or cache with no read-your-writes mechanism, then debugging a "data loss" report that's actually ordinary replication lag.
- Applying a linearizable/strongly consistent read to every request "to be safe," paying the latency and availability cost everywhere instead of only on the specific paths that need it.
- Testing consistency behavior only single-threaded/single-client, which cannot reveal read-your-writes or monotonic-read violations that only appear with concurrent or multi-session access.

## Exceptions and trade-offs
- Stronger guarantees cost latency, throughput, or availability (a linearizable read typically requires contacting a quorum or the leader); weaker guarantees cost application complexity (handling staleness, retries, conflict resolution) — there is no guarantee that's free, so the choice per read path should be a deliberate trade, not a default.
- Causal consistency and session-based guarantees (read-your-writes, monotonic reads) often deliver "good enough" behavior for user-facing systems at much lower cost than full linearizability — worth trying before reaching for the strongest guarantee.
- Some workloads (analytics, reporting, search indexes) genuinely don't need any consistency guarantee tighter than "eventually converges," and forcing a stronger guarantee onto them only adds cost with no user-visible benefit.

## Verification
- Confirm every place a consistency claim is made in documentation, comments, or a design doc names a specific guarantee and, for eventual consistency, a bound or convergence condition.
- Confirm the actual datastore/API documentation was checked for the specific operation in question, not inferred from the product's general marketing description.
- Confirm a concurrency/multi-session test exists for any path claiming read-your-writes or monotonic-read guarantees, and that it fails without the mechanism providing the guarantee.
- Confirm the strongest guarantee in use (e.g., linearizable reads) is applied only to the specific paths that were shown to require it, not applied uniformly by default.
