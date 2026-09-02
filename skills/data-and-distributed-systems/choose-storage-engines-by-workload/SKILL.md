---
name: choose-storage-engines-by-workload
description: "Matches the physical storage engine - B-tree, LSM-tree, columnar, in-memory - to the workload's read/write ratio, value sizes, and durability needs. Use when choosing between an InnoDB-style and a RocksDB or Cassandra-style engine for a high-write service, deciding whether an analytical workload belongs in a columnar store, or debugging write amplification, compaction stalls, or tail-latency reads that trace to the engine rather than application code. Not for the logical shape of the data (see choose-data-models-from-access-patterns) or how many copies to keep (see design-replication-for-the-required-guarantees)."
license: MIT
---

# Choose Storage Engines by Workload

## Intent
Match the storage engine's internal write and read path — B-tree, LSM-tree/SSTable, columnar, or in-memory — to the workload's actual read/write ratio, value sizes, and durability requirements, instead of assuming one engine family is universally best.

## Procedure
1. Characterize the workload numerically: approximate write throughput, read throughput, read/write ratio, typical value size, and whether reads are point lookups, range scans, or full-column scans.
2. Determine durability and latency requirements: can writes be batched/buffered, or must each write be fsynced before acknowledging, and what tail-latency (p99/p999) is acceptable for reads.
3. For write-heavy workloads with sequential or high-throughput random writes, evaluate an LSM-tree engine (sequential writes, background compaction) against a B-tree engine (in-place random writes, page splits) — LSM generally wins on write throughput at the cost of read amplification and compaction overhead.
4. For read-heavy workloads with point lookups on stable data, evaluate a B-tree engine, which offers more predictable read latency without compaction-driven read amplification.
5. For analytical workloads that scan few columns across many rows, evaluate a columnar engine, which avoids reading unused columns and compresses far better than row storage for that access pattern.
6. If the working set fits in memory and durability requirements allow it (or are met via replication/snapshotting instead of per-write fsync), evaluate an in-memory engine for the latency win, and explicitly define what data loss is acceptable on crash.
7. Load-test the shortlisted engine(s) with production-representative value sizes and concurrency, not synthetic uniform-key benchmarks, since compaction and page-split behavior are sensitive to key distribution and value size.

## Decision rules
- High sustained write throughput with tolerance for eventual background compaction: prefer LSM-tree engines.
- Latency-sensitive point reads on data that doesn't change much: prefer B-tree engines, which avoid read-amplification from multiple SSTable levels.
- Wide tables where queries touch a small subset of columns across many rows (aggregations, reporting): prefer columnar storage over row storage.
- Small hot working set with a tolerance for defined data-loss-on-crash windows: prefer an in-memory engine with periodic snapshotting or an AOF-style log, sized against the actual acceptable loss window.
- Range scans over sorted keys (time-series, ordered event logs): prefer engines that keep data sorted on disk (LSM-tree SSTables or clustered B-tree indexes) over hash-based storage.
- Every fsync-per-write requirement trades throughput for durability; batch writes with group commit where the durability requirement allows a small bounded window of loss.

## Anti-patterns
- Running heavy analytical scans directly against a row-oriented OLTP engine tuned for point lookups, then concluding "the database is slow" instead of routing analytics to a columnar store or read replica built for it.
- Choosing an LSM-tree engine for a read-heavy, rarely-updated dataset and then fighting read amplification and compaction I/O that a B-tree engine wouldn't have incurred.
- Ignoring value size when picking an engine — very large values in an LSM-tree engine (without a separate value log / WiscKey-style design) inflate compaction cost dramatically.
- Benchmarking a storage engine with uniformly random keys and small values, then deploying it against a workload with skewed keys or large values and being surprised by different performance characteristics.
- Turning off or loosening fsync/durability settings to "fix" write latency without documenting and getting sign-off on the resulting crash data-loss window.

## Exceptions and trade-offs
- Hybrid engines (e.g., B-tree with an LSM-style write buffer, or tiered storage with hot data in-memory and cold data columnar) can serve mixed workloads better than any single pure engine, at the cost of more operational complexity and more tuning knobs.
- Compaction strategy (leveled vs. size-tiered) inside an LSM-tree engine is itself a workload-dependent choice — leveled compaction favors read latency, size-tiered favors write throughput — worth revisiting once the coarse engine family is chosen.
- Managed/cloud database offerings often hide the underlying engine choice; when the workload is unusual (very high write throughput, very large values, heavy analytics), verify what engine and configuration the managed service actually uses rather than assuming it's tuned for you.

## Verification
- Confirm the shortlisted engine was benchmarked with production-representative key distribution, value size, and concurrency before committing.
- Confirm p99/p999 read and write latency were measured under sustained load with compaction/background maintenance running concurrently, not only on an idle system.
- Confirm the durability configuration (fsync behavior, replication factor, snapshot interval) matches a stated, agreed-upon acceptable data-loss window.
- Confirm the choice was re-validated after any major change in workload shape (e.g., a new bulk-import feature that shifts a read-heavy workload to write-heavy).
