---
name: rr
description: Scan a codebase for provably unused or redundant code and remove safe candidates without broad rewrites.
---

# RR

RR means Remove Redundancies. Use it when the user wants an existing application cleaned up by removing dead code, unused variables, stale paths, or code that repeats a guarantee the application already enforces.

The target is a smaller live code path that still works. Do not rewrite active code or compress it just to reduce line count. Keep the existing design unless a redundant piece can be removed without changing the behavior that users or supported callers rely on.

## Workflow

1. Establish the baseline.

   - Inspect the repository status, project documentation, entry points, package scripts, CI configuration, and generated-code conventions.
   - Identify the relevant formatter, linter, type checker, test command, build command, and app smoke check from the repository. Do not invent commands when the project already documents them.
   - Run the most relevant baseline checks when practical. Record failures that existed before the cleanup so they are not mistaken for regressions.

2. Find candidates.

   Start with the language's compiler and linter warnings, then confirm candidates with repository search such as `rg`. Look for:

   - unused imports, locals, parameters, fields, types, functions, classes, components, and modules;
   - exports and files with no live internal consumer;
   - unreachable branches, impossible cases, stale feature-flag paths, and duplicate fallbacks;
   - defensive checks that repeat a guarantee already enforced at a real boundary;
   - duplicate registration, configuration, or transformation steps whose removal leaves one correct path.

   Treat a warning or a missing text match as a lead, not proof. "Not covered by tests" does not mean "unused."

3. Prove each removal.

   For every candidate, check its imports, exports, re-exports, package entry points, scripts, tests, configuration, and documentation. Also check mechanisms that ordinary search can miss:

   - dynamic imports and file-path lookups;
   - reflection, dependency injection, registries, event handlers, and plugin discovery;
   - framework conventions such as route, middleware, serializer, lifecycle, or component names;
   - string-based commands, environment configuration, serialization formats, and generated callers;
   - top-level side effects, registration, cleanup, metrics, logging, and initialization order.

   Treat public exports as used unless the user explicitly includes an API change and the supported consumers are known. Do not edit generated files, vendored code, migrations, fixtures, examples, or build output unless the repository's workflow says they are maintained source.

   Remove a candidate only when one of these is true:

   - no supported caller or runtime discovery path can reach it;
   - the compiler or type system proves a branch impossible;
   - an invariant is enforced at the boundary, making the inner branch unreachable for every supported input;
   - one of two paths is demonstrably redundant and the remaining path preserves the same contract and side effects.

   Be cautious with validation, authorization, error handling, cleanup, retries, concurrency controls, and compatibility code. Remove them only when the replacement guarantee is explicit, enforced, and within the same supported boundary. A current caller's habit is not a guarantee.

4. Make small edits.

   Delete the smallest proven unit. Remove imports, exports, and nearby comments that became obsolete. Update direct callers only when that is required to make the deletion correct. Do not add an abstraction, rename unrelated symbols, reformat files, or deduplicate broad regions as part of the cleanup.

   Work in small logical batches. After each batch, inspect the diff and search for stale references before starting the next one.

5. Verify the real application.

   Run the formatter or lint check, type check, focused tests, full tests, and build or startup smoke check that the repository supports. Use the smallest useful sequence first, then run the broader checks before finishing. Run `git diff --check` and review the final diff for unrelated changes.

   If a check fails, determine whether the failure comes from the cleanup or from the baseline. Fix regressions before continuing. If safe proof is not possible, leave the candidate in place and explain what evidence is missing.

## Completion report

Report:

- what was removed and why it was proven redundant;
- the checks that passed and any pre-existing failures;
- candidates left untouched because they may be public, dynamic, side-effectful, generated, or otherwise unproven;
- any behavior or API boundary that the cleanup deliberately preserved.

Never claim that the codebase has no redundancy unless the available static and runtime evidence supports that claim. The useful result is a smaller, verified code path, not a smaller number in a line counter.
