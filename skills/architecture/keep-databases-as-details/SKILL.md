---
name: keep-databases-as-details
description: "Keeps business rules independent of persistence by expressing data access as repository interfaces in domain terms, not SQL, ORM entities, or driver types. Use when domain code holds SQL or ORM classes, or a schema change forces business-rule edits. Not for the general dependency-direction or policy/detail principle (see control-dependency-direction, separate-policy-from-details), test speed (see design-testable-architecture), or picking a data model or storage engine (see choose-data-models-from-access-patterns, choose-storage-engines-by-workload)."
license: MIT
---

# Keep Databases as Details

## Intent
Keep the choice of database technology, schema shape, and query mechanism a swappable implementation detail behind an interface defined in the business logic's own vocabulary, so business rules neither know nor care what stores their data.

## Procedure
1. Find where business logic currently talks to the database directly — SQL strings, ORM model classes used as domain objects, query-builder chains inside use-case or domain code.
2. Define a repository/gateway interface in the business logic's own vocabulary and owned by the business logic's component: methods like `findActiveSubscriptionsFor(customerId)` or `save(order)`, not `runQuery(sql)` or generic CRUD mirroring table structure.
3. Separate the domain model from the persistence model: the object business logic operates on (an `Order`, a `Customer`) should not be the same class the ORM maps to a table row, if the ORM's mapping constraints (lazy loading, table-shape-driven fields, framework base classes) would otherwise leak into domain code. A thin mapping layer converts between the two at the boundary.
4. Implement the interface in an infrastructure/persistence component using whatever database technology is appropriate — SQL, a document store, an in-memory cache — with that choice invisible to the caller.
5. Wire the concrete implementation to the interface at the composition root, not inside the business logic.
6. Confirm no business-rule file imports a database driver, ORM base class, or query type; confirm the persistence component imports the domain vocabulary types (or a mapping-layer DTO) but not vice versa beyond the interface.
7. For an existing schema-coupling problem, migrate one repository/interface at a time rather than attempting a system-wide rewrite; verify behavior via tests against the interface as each piece moves.

## Decision rules
- Business logic depends on an interface it owns and names in its own terms; the database component depends on (implements) that interface — never the reverse.
- A repository interface's method names and parameter/return types should read like the business problem ("reserveInventory", "outstandingInvoicesFor"), not like database operations ("selectWhere", "updateRow").
- If the ORM's entity classes are also being used directly as domain objects with business methods attached, and the ORM's mapping requirements (getters/setters shape, lazy-load proxies, framework annotations) are dictating the domain model's shape, that's the database leaking into policy — separate them.
- A schema migration, index change, or switch of database vendor should require changes only inside the persistence component and its tests — never inside business-rule code or its tests (aside from possibly updating an in-memory fake used by those tests).
- Query optimization concerns (indexes, denormalization, caching) belong entirely inside the persistence implementation; they should never shape the interface's method signatures beyond what the business logic actually needs.

## Anti-patterns
- Business-rule or use-case classes constructing and executing SQL, or calling an ORM's query API directly, instead of calling a repository interface.
- A "repository" interface that's really just a thin pass-through to the ORM's generic CRUD (`findById`, `save`, `deleteAll`) mirroring table structure rather than expressing the actual operations the business logic needs.
- Domain objects that are literally the ORM's mapped entity classes, carrying framework base-class requirements, lazy-loading behavior, or mapping annotations into code that's supposed to express pure business rules.
- Letting a database-specific concept (transactions spanning multiple aggregates, a specific SQL dialect's function, a NoSQL document's nesting shape) dictate the shape of a business-rule method signature.
- Writing business-logic tests that require a real database connection because the logic can't be exercised without going through the ORM.

## Exceptions and trade-offs
- For a small script, internal tool, or true CRUD app with no meaningful business rules beyond "store and retrieve this record," introducing a full repository abstraction is overhead without benefit — direct ORM/query use is reasonable there.
- Certain database features (full-text search ranking, geospatial queries, transactional guarantees across specific rows) may need to be exposed through the repository interface in a way that's shaped by the database, when there's no realistic alternative implementation ever expected — document that as a deliberate, scoped leak rather than pretending full independence.
- Reporting/analytics code that exists specifically to query the database in bulk, ad hoc ways is a different concern from transactional business logic and is not obligated to go through the same repository abstraction.

## Verification
- No business-rule or use-case file imports a database driver, ORM base class/annotation, or raw query type.
- Repository/gateway interfaces are named and shaped around business operations, not generic table CRUD.
- A test of business logic can substitute an in-memory fake for the repository interface and run with no real database connection.
- A recent schema or database-vendor change (if any) touched only the persistence component, not business-rule code.
