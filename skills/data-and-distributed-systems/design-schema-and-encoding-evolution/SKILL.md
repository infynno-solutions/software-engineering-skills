---
name: design-schema-and-encoding-evolution
description: "Treats any schema or wire encoding with more than one deployed version as a compatibility boundary, making each change forward- and backward-compatible so old and new code coexist during rollout. Use when adding, removing, renaming, or retyping a field in a table, Protobuf/Avro message, or JSON API read by more than one service or version; when producer and consumer will not deploy atomically; or when a migration adds a NOT NULL column to a live table. Not for choosing a schema's shape before it exists (see choose-data-models-from-access-patterns), or whether to use a log or CDC at all (see use-logs-events-and-change-data-capture-deliberately)."
license: MIT
---

# Design Schema and Encoding Evolution

## Intent
Treat any schema or wire encoding with more than one deployed version — a database column, an event format, an API payload — as a compatibility boundary, and make every change to it forward- and backward-compatible so old and new code can coexist safely during rollout.

## Procedure
1. Identify every reader and writer of the schema/encoding, including ones that deploy independently (other services, mobile clients, batch jobs, downstream consumers of an event stream) — the compatibility requirement is defined by the slowest one to update.
2. For each proposed change, classify it: additive (new optional field), and check whether it's backward-compatible (old readers ignore the new field safely) and forward-compatible (new readers handle records written by old code that lack the field, typically via a default value).
3. Never repurpose or change the meaning of an existing field/tag/column name — always add a new one and deprecate the old, since a repurposed field is silently misinterpreted by any reader still running the old logic.
4. For "expand" changes (rename, retype, tighten a constraint), use the expand/contract pattern: add the new field or relaxed constraint first, dual-write to old and new for a transition period, migrate all readers to the new field, then remove the old one only once nothing reads it.
5. For schemas with an explicit schema definition (Protobuf, Avro, Thrift), set and rely on defaults for new fields, never reuse a field number/tag, and run the format's own compatibility checker against the previous schema version before merging.
6. For schemaless formats (plain JSON), be explicit about what "unknown field" and "missing field" mean to every reader, since there's no compiler-enforced compatibility check — write and run compatibility tests directly.
7. Sequence the rollout so it tolerates the actual deployment order: readers that must tolerate new fields deploy before writers start producing them; writers that must keep producing an old field deploy their removal only after all readers stop needing it.

## Decision rules
- Adding an optional field with a sensible default is always safe; removing a field is only safe once every reader has been confirmed to no longer need it.
- Never change a field's type in place; add a new field with the new type, migrate, and retire the old one — an in-place type change breaks any reader still expecting the old type.
- Never make a previously-optional field required (`NOT NULL`, a required Protobuf field) until every writer in production has been verified to always populate it.
- Field/tag identity in structured binary formats (Protobuf field numbers, Avro field names/aliases) is the actual compatibility key — treat renumbering or reusing a tag as a breaking change even if the field name changes.
- When a producer and consumer of an encoded record can be deployed independently and out of order, always design for both "old writer, new reader" and "new writer, old reader" simultaneously, not just the direction being actively rolled out.

## Anti-patterns
- Renaming a database column or Protobuf field in place instead of adding a new one, breaking any code still deployed with the old name/tag during a rolling deployment.
- Adding a `NOT NULL` column with no default directly to a live table, which fails or blocks on existing rows and breaks in-flight writers that don't yet populate it.
- Reusing a Protobuf field number after removing an old field, causing old binary data to be silently misinterpreted as the new field's type.
- Changing a JSON field's type (e.g., string to object) without versioning the payload, silently breaking any consumer that doesn't defensively type-check.
- Coordinating a schema change through simultaneous "flag day" deployment of every reader and writer instead of an expand/contract rollout, which is fragile the moment any one deploy is delayed or rolled back.

## Exceptions and trade-offs
- A genuinely breaking change is sometimes unavoidable (e.g., a security fix that must reject old malformed data); in that case, version the schema/endpoint explicitly (a new topic, a new API version, a schema major-version bump) rather than mutating the existing compatibility contract in place.
- Internal, single-deploy-unit data (a schema used only within one process's own storage, never read by another version of itself) doesn't need the full expand/contract ceremony — the compatibility requirement only exists where more than one version is live at once.
- Expand/contract migrations take longer and require temporary dual-write/dual-read code that must later be cleaned up — that cost is the price of a safe rollout, not overhead to be skipped under time pressure.

## Verification
- Confirm a schema-compatibility check (Protobuf/Avro schema registry compatibility mode, or an equivalent test for JSON) runs in CI against the previous version before merging any schema change.
- Confirm a rollback scenario was considered: if the writer is rolled back after the reader has deployed (or vice versa), the system still functions.
- For structural database migrations, confirm the change was split into backward-compatible steps (add nullable column → backfill → add constraint → remove old column) each independently deployable.
- Confirm old field/tag names and numbers are never reused after retirement, and that this is enforced (schema registry, lint rule, or code review checklist) rather than left to memory.
