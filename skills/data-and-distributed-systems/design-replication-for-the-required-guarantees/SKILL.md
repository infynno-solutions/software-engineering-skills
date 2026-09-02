---
name: design-replication-for-the-required-guarantees
description: "Picks a replication topology - single-leader, multi-leader, or leaderless - and its quorum settings so availability, write-conflict behavior, and staleness match what the application requires. Use when standing up a replicated datastore, adding multi-region writes and needing a conflict-resolution rule, or debugging a write that disappeared because a read hit a lagging replica. Not for stating the guarantee clients need in the abstract (see reason-explicitly-about-consistency), or splitting data across nodes for scale (see partition-data-with-explicit-trade-offs)."
license: MIT
---

# Design Replication for the Required Guarantees

## Intent
Pick a replication topology — single-leader, multi-leader, or leaderless — and its quorum/consistency settings so the resulting availability, write-conflict behavior, and staleness match what the application genuinely requires, rather than inheriting a database's default configuration unexamined.

## Procedure
1. State the guarantee the application needs from replicas: can a client ever read stale data, and if so how stale (read-your-writes, monotonic reads, bounded staleness, or none of these constraints)?
2. State the write-availability requirement: must writes succeed during a single node/region outage, and if writes can happen concurrently in two places, how should conflicts be resolved (last-write-wins, application-level merge, CRDTs)?
3. If writes only ever need to originate from one place at a time, default to single-leader replication — it avoids write-conflict resolution entirely and is the simplest model to reason about.
4. If writes must be accepted in multiple regions concurrently (for write latency or regional availability), evaluate multi-leader replication and design the conflict-resolution strategy explicitly before enabling it — don't let the database's default (often last-write-wins by timestamp) be an accidental, unreviewed choice.
5. If the workload needs to tolerate individual node failure without a leader-based failover process, evaluate a leaderless/quorum design (read quorum R + write quorum W > total replicas N) and choose R and W to match the durability vs. latency trade-off needed.
6. Decide how replicas catch up after a failure or a network partition heals: full resync, catch-up from a replication log, or anti-entropy/read-repair — and confirm the chosen mechanism doesn't silently drop writes.
7. Instrument and alert on replication lag (single/multi-leader) or on quorum failures / read-repair rates (leaderless) so drift and degraded guarantees are visible before a user reports them.

## Decision rules
- Default to single-leader replication unless there's a stated requirement (regional write latency, write availability during a region outage) that specifically needs multi-leader or leaderless.
- If clients read their own writes shortly after making them, guarantee read-your-writes explicitly (route the client's own reads to the leader or a replica confirmed caught up) — don't assume eventual consistency is invisible to users.
- In multi-leader or leaderless designs, decide the conflict-resolution strategy before enabling concurrent writes; last-write-wins silently discards data and is only acceptable when the application genuinely doesn't care which concurrent write wins.
- Choose leaderless quorum sizes (R + W > N) based on which failure you need to tolerate without blocking: larger W favors durability of writes, larger R favors read consistency, and both trade off against latency and availability during node loss.
- Failover in single-leader replication should be deliberate (manual or carefully fenced automatic) — an automatic failover without a fencing mechanism risks two nodes believing they're the leader simultaneously.

## Anti-patterns
- Enabling multi-leader or leaderless replication for write-scalability reasons without ever deciding how concurrent write conflicts are resolved, then discovering last-write-wins has been silently dropping data.
- Sending a user's read to a lagging read replica immediately after they wrote, producing a "my change didn't save" support ticket that's actually just replication lag.
- Assuming automatic failover is always safe; promoting a new leader without fencing the old one can produce two leaders accepting writes simultaneously (split brain) after the old leader resumes from a pause.
- Treating replication as a solved default of "just turn on read replicas" without checking whether the application's read paths can tolerate the resulting staleness.
- Running leaderless replication with a quorum configuration (e.g., R=1, W=1 on N=3) that doesn't actually guarantee overlap between read and write sets, then being surprised reads can return stale or missing data.

## Exceptions and trade-offs
- Multi-leader replication genuinely earns its complexity for offline-capable clients (mobile apps that must accept writes disconnected) and multi-datacenter deployments where cross-region write latency to a single leader is unacceptable.
- CRDTs or operational-transformation-based merge can make multi-leader conflict resolution automatic and safe for specific data shapes (counters, sets, collaborative text) but don't generalize to arbitrary application state — evaluate per data type, not as a blanket strategy.
- Synchronous replication (wait for replica ack before acknowledging the write) trades write latency and availability for a stronger durability guarantee; asynchronous replication trades a small window of possible data loss on leader failure for lower write latency — pick per the durability requirement, not by default.

## Verification
- Confirm the chosen topology was tested through the specific failure it must survive (leader crash, region network partition, node loss under leaderless quorum) and reaches a correct, defined end state.
- Confirm replication lag and, where applicable, conflict/read-repair rates are monitored with alerting thresholds tied to the stated staleness requirement.
- Confirm the conflict-resolution strategy for concurrent writes (multi-leader/leaderless) was explicitly chosen and tested with a deliberately concurrent write scenario, not left at the database default.
- Confirm failover (automatic or manual) was tested for split-brain risk, including a scenario where the old leader resumes after being presumed dead.
