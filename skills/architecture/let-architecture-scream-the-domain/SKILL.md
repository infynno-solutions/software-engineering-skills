---
name: let-architecture-scream-the-domain
description: "Structures top-level folders so the listing names business capabilities (billing, scheduling) rather than technical layers (controllers, services, models). Use when defining or reorganizing top-level structure, or a newcomer can see the framework but not the business problem. Not for keeping framework code out of business logic (see keep-frameworks-as-details), what goes inside a component (see choose-boundaries-by-change-and-coupling), or naming classes and functions (see name-for-meaning)."
license: MIT
---

# Let Architecture Scream the Domain

## Intent
Organize the codebase's top-level structure and entry points so its business capabilities and use cases are what a reader sees first — the architecture should announce "this is a hospital scheduling system," not "this is a Spring app" or "this is a React app."

## Procedure
1. List the top-level packages/folders/modules of the codebase (or the area under review) as they exist today.
2. For each, ask: does its name describe a business capability (billing, scheduling, patient intake) or a technical role/framework convention (controllers, models, services, utils)? Flag the technical-role ones.
3. For a flagged technical-role grouping, identify the business capabilities whose code is currently scattered across it (e.g., billing-related controllers, billing-related models, billing-related services all in different top-level folders) and regroup that code under one capability-named module.
4. Within each capability module, technical substructure (an internal `adapters/`, `web/`, `persistence/` subfolder) is fine — the rule applies to what's visible at the top level and in the entry point, not to banning technical organization entirely at every depth.
5. Check the system's entry point (main file, top-level README, the first thing a new engineer opens) — does it describe what the system does, or how it's built? Rewrite it to lead with capability if it leads with framework/technology.
6. Verify the framework's own generated structure (if the framework scaffolds `controllers/`, `models/`, etc.) has been adapted so those technical folders are demoted to internals of each capability module, not left as the system's primary organizing structure.

## Decision rules
- Top-level names should be nouns or noun phrases a business stakeholder would recognize (billing, inventory, scheduling), not technical layer names (controllers, services, DAOs, utils) or framework names.
- If the answer to "what does this system do" requires reading multiple technical-layer folders and mentally reassembling them, the architecture is not screaming the domain — it's screaming the framework or the layering pattern.
- Technical layering (MVC, ports/adapters, hexagonal) is a legitimate internal structure within a capability module; it becomes a problem specifically when it's the *top-level* organizing principle instead of business capability.
- A generic catch-all top-level folder (`utils/`, `common/`, `helpers/`, `misc/`) accumulating unrelated code across many capabilities is a sign the domain structure has been abandoned in favor of technical convenience — periodically audit and redistribute it.

## Anti-patterns
- Top-level folders named `controllers/`, `services/`, `models/`, `repositories/`, `views/` with business capability only visible one or two levels deeper (or not consistently named the same way across those folders, so it's not even easy to reassemble).
- A `utils/` or `common/` folder that has become a dumping ground for business logic that didn't obviously fit elsewhere, hiding real business capability inside a generic-sounding technical bucket.
- A project README or landing entry-point that describes the tech stack ("A Node.js/Express/Postgres application...") before it describes what the system does for its users.
- Naming a module after the framework pattern used to build it (e.g., `sagas/`, `reducers/`, `middlewares/`) as a top-level organizing concept, rather than naming it after the business process the pattern happens to implement.
- Adding a new business capability by dropping one new file into each of five existing technical-layer folders instead of creating one new capability-named module.

## Exceptions and trade-offs
- Infrastructure-only projects (a shared library of framework utilities, a platform team's tooling) genuinely have no business domain to scream — organizing those by technical concern is correct, not a violation; this skill applies to systems that implement business capabilities.
- Very small applications with one clear, singular purpose may not need capability-based subdivision at all — a flat structure is fine until there's more than one capability to distinguish.
- Where a framework's tooling (code generators, hot-reload, routing conventions) genuinely requires files to live in specific technically-named locations to function, that constraint can be accepted for those specific files while still keeping the domain-capability names as the primary folders those technical files are nested under or reference.

## Verification
- A newcomer reading only the top-level directory listing (or entry-point doc) can state, in business terms, what the system does — without needing to open files.
- No top-level folder is named purely for a technical layer or framework pattern with business capability only discoverable by opening it.
- Adding one new business capability doesn't require touching every existing technical-layer folder.
- Any `utils/`/`common/`-style catch-all is reviewed periodically and doesn't contain capability-specific business logic that belongs in a named module.
