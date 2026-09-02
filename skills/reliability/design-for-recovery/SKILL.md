---
name: design-for-recovery
description: "Makes restart, rebuild, failover, replay, and restore explicit, tested parts of the design so returning to a good state is a known procedure rather than improvised. Use when a component owns state with no tested way to rebuild it from scratch, when adding replication, backups, or snapshots without defining the restore path, or when cold-start behavior - empty cache, queue replayed from the beginning, leader re-election - has never been verified. Not for stopping a failure spreading while it happens (see isolate-failures-and-limit-blast-radius), or serving reduced functionality during the outage (see degrade-gracefully)."
license: MIT
---

# Design for Recovery

## Intent
Make restart, rebuild, failover, replay, and restoration paths explicit, tested parts of the design, so recovering from loss or corruption is a known procedure rather than something improvised during an incident.

## Procedure
1. For each piece of durable or semi-durable state, define what "recovered" means: an RPO (how much data loss is acceptable) and RTO (how long recovery may take).
2. Design the actual restoration mechanism: restore from backup, replay from an event log/WAL, rebuild from an upstream source of truth, or resync from a healthy replica — and identify which one applies to each component.
3. Make recovery idempotent and resumable where possible, so a recovery attempt that itself fails partway can be retried without making things worse (pairs with `design-idempotent-operations`).
4. Verify the recovery path restores the system to a *consistent* state, not just a populated one — partial replay or a backup mid-write can leave referential or logical inconsistency.
5. Exercise the recovery path on a schedule (restore-from-backup drill, forced failover, DR game day) rather than trusting it because it was designed correctly once.

## Decision rules
- If a component's data cannot be reconstructed from any other source and has no backup/replication, that is a single point of unrecoverable loss — flag it explicitly rather than assuming "we'll never lose it."
- Choose RPO/RTO targets based on the cost of data loss and downtime to the business, then work backward to the required backup frequency/replication topology — don't let the mechanism (nightly backup) silently set the target.
- Prefer recovery mechanisms that can be tested cheaply and often (replay from log, restore to a scratch environment) over ones only exercisable during a real disaster.
- When automatic failover exists, define what happens on failback (returning to the original primary) — asymmetric failover/failback handling is a common source of split-brain and data loss.

## Anti-patterns
- Backups that are taken but never test-restored, so the first real restore attempt happens during an actual outage.
- A "recovery procedure" that exists only as tribal knowledge in one engineer's head.
- Recovery logic that assumes it will only ever run once cleanly, so a crash mid-recovery leaves the system in a worse state than before recovery started.
- Treating replication as a substitute for backups — a replica faithfully propagates corruption or accidental deletion just as fast as it propagates good writes.

## Exceptions and trade-offs
- Fully automated, zero-RTO failover is expensive to build and operate; for less-critical systems, a documented and drilled manual recovery procedure with a longer RTO is a legitimate, cheaper choice — as long as it's actually drilled.
- Very short RPO (near-zero data loss) usually requires synchronous replication, which trades off latency and availability during network partitions — make that trade-off deliberately, not by default.
- Recovery drills carry real operational risk and cost (load on production, engineer time) — scale drill frequency to the component's criticality rather than drilling everything maximally.

## Verification
- Confirm each stateful component has a documented RPO/RTO and a named recovery mechanism that maps to it.
- Confirm the recovery path has been exercised end-to-end (restore drill, failover test) within a defined interval, not just designed.
- Confirm recovery is idempotent/resumable, or that a partial-recovery failure mode has been explicitly tested.
- Confirm backups and replicas are verified for restorability (checksum, test restore), not just verified to exist.
