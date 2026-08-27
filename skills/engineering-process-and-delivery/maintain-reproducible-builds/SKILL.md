---
name: maintain-reproducible-builds
description: "Makes builds and their inputs explicit, deterministic where practical, and reconstructable by another developer or environment. Use when a build passes on one machine or CI runner and fails or differs on another, when pinning toolchain and runtime versions, or when setting up a new dev environment or container image. Not for choosing which third-party packages to depend on or when to upgrade them (see manage-dependencies-explicitly); this skill covers the build process being deterministic given whatever versions are chosen."
license: MIT
---

# Maintain Reproducible Builds

## Intent
Ensure builds and their inputs are explicit, deterministic where practical, and reconstructable by another developer or environment.

## Procedure
1. Identify every input the build depends on: language/runtime version, package manager version, OS-level tools, environment variables, network resources fetched at build time.
2. Pin exact versions (not ranges) for toolchain and dependencies via a lockfile or equivalent, checked into version control.
3. Eliminate implicit environment assumptions: replace "assumes X is installed globally" with an explicit, versioned declaration (container image, version manager file, devcontainer).
4. Remove non-determinism from the build itself: unpinned timestamps, unordered file globs, network calls during build that aren't cached or pinned.
5. Verify reproducibility by building twice from the same inputs and diffing outputs, or building on a second machine/CI runner and comparing.
6. Document the exact command(s) that produce a release build, and keep that path exercised by CI.

## Decision rules
- If a build step's output can differ between two runs on identical inputs, that's the priority fix before anything else.
- Prefer lockfiles and pinned container/toolchain images over "install latest" in build scripts.
- A new developer's first build attempt should not require undocumented tribal setup steps.
- Bit-for-bit determinism is a stretch goal; "same behavior and same dependency graph" is the practical minimum for most projects.

## Anti-patterns
- CI and local dev using different toolchain versions with no pinning mechanism reconciling them.
- Build scripts that silently pull "latest" of a dependency or base image.
- Relying on a developer's globally installed tools instead of a project-scoped, versioned toolchain.
- Treating a passing build today as proof it will pass identically in six months.

## Exceptions and trade-offs
- Full bit-for-bit determinism (fixed timestamps, sorted archives) is expensive; weigh it against the actual need (e.g., supply-chain verification) before chasing it.
- Some ecosystems can't fully pin transitive dependencies; document the gap and mitigate with periodic rebuild-and-diff checks instead.
- Rapid-prototype code may reasonably defer strict pinning until it has real users depending on stable builds.

## Verification
- A clean checkout on a fresh machine or container builds successfully following only the documented steps.
- Two builds from the same commit and lockfile produce equivalent, ideally identical, artifacts.
- The lockfile is checked in and CI fails if it's out of sync with the manifest.
