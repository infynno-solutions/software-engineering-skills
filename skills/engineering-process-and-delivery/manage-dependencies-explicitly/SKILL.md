---
name: manage-dependencies-explicitly
description: "Tracks direct and transitive dependencies, versions, ownership, and compatibility risk instead of relying on implicit environmental state. Use when adding a new third-party package, responding to a vulnerability alert, deciding whether to take a major-version upgrade, or resolving a transitive version conflict. Not for making the build deterministic once versions are chosen (see maintain-reproducible-builds), catching quality issues in your own code (see use-static-analysis-in-the-core-workflow), or keeping a framework out of business logic (see keep-frameworks-as-details)."
license: MIT
---

# Manage Dependencies Explicitly

## Intent
Track direct and transitive dependencies, versions, ownership, and compatibility risk instead of relying on implicit environmental state.

## Procedure
1. Before adding a dependency, check whether an existing one already covers the need, and weigh its maintenance burden against the code it saves writing.
2. Record why a dependency was added, in the PR or a dependency-notes doc, when the choice isn't obvious from its name.
3. Pin direct dependency versions explicitly; let the lockfile capture the resolved transitive graph.
4. Set up automated notification for vulnerable or outdated dependencies and triage findings on a regular cadence, not only reactively.
5. Assign informal ownership: someone should notice and act when a widely-used dependency has a breaking release or security advisory.
6. When upgrading, read the changelog or migration notes for breaking changes before bumping, especially across major versions.
7. Periodically prune dependencies that are no longer used.

## Decision rules
- A new dependency needs a stated justification if it pulls in a nontrivial transitive tree or duplicates existing functionality.
- Security patch upgrades should be fast-tracked; feature-motivated major upgrades can be scheduled deliberately.
- Prefer a well-maintained, widely-used package over a lightly-maintained one with marginally better fit, unless the fit gap is significant.
- Vendoring or forking a dependency is a last resort when upstream is abandoned and the dependency is load-bearing.

## Anti-patterns
- Adding a dependency for a single trivial utility function that could be a few lines of owned code.
- Wildcard or unpinned version ranges in a manifest with no lockfile pinning the actual resolved versions.
- Ignoring vulnerability scanner output until an audit or incident forces attention.
- Nobody on the team able to say why a given dependency is present or whether it's still needed.

## Exceptions and trade-offs
- Writing your own implementation instead of depending on a library trades dependency risk for maintenance burden — justify that trade explicitly for anything beyond a trivial utility.
- Staying on an older major version is sometimes the right call when the upgrade cost outweighs the benefit and there's no security exposure.
- Rapid prototypes may reasonably skip strict dependency governance until the code has a real deployment target.

## Verification
- Every direct dependency's presence can be explained.
- No manifest entries use unpinned or wildcard versions without a lockfile backing them.
- Recent vulnerability scan results have been triaged — fixed, accepted-risk, or false-positive — not left unread.
- No orphaned dependencies remain from removed features.
