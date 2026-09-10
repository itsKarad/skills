# Shared LLM skills

A portable collection of skills for LLM agents.

## Skills

### Planning, design, and review

- `architect`: Sketch types, signatures, and module structure before implementation.
- `arena`: Compare parallel candidates, choose the strongest base, and combine useful parts.
- `blast-radius`: Find what a change could break beyond the diff and verify the important risk.
- `grill-me`: Pressure-test a plan or design through a focused interview.
- `grilling`: Challenge a plan, decision, or idea from several angles.
- `how`: Explain codebase architecture, runtime flow, ownership, and placement.
- `interrogate`: Run an adversarial multi-review of code or a proposed change.
- `why`: Explain design rationale, regressions, and decisions using available evidence.

### Execution and code quality

- `automate-me`: Turn working preferences into a reusable personal mode skill.
- `poteto-mode`: Work with concise prose, deliberate delegation, simple code, and verification.
- `reflect`: Review the current work and turn concrete lessons into skill edits.
- `rr`: Find and remove provably unused or redundant code without broad rewrites.
- `show-me-your-work`: Keep a TSV decision log for long-running or unattended work.
- `swarm`: Run parallel workers for broad exploration, comparison, or coverage.
- `unslop`: Remove AI writing patterns and make text clearer and more human.

### Principles

- `principle-boundary-discipline`: Keep validation and error handling at system boundaries.
- `principle-build-the-lever`: Build a reusable tool that performs or proves non-trivial work.
- `principle-encode-lessons-in-structure`: Turn repeated corrections into checks or structure.
- `principle-exhaust-the-design-space`: Compare competing prototypes before choosing a novel design.
- `principle-experience-first`: Prefer a smaller polished user experience over rough breadth.
- `principle-fix-root-causes`: Reproduce bugs and fix their underlying cause.
- `principle-foundational-thinking`: Choose sound types and data structures before writing logic.
- `principle-guard-the-context-window`: Route bulk work away from the main context when needed.
- `principle-laziness-protocol`: Prefer the smallest change that solves the problem.
- `principle-make-operations-idempotent`: Make retries and restarts converge on the same result.
- `principle-migrate-callers-then-delete-legacy-apis`: Move callers and remove obsolete APIs together.
- `principle-minimize-reader-load`: Reduce layers and hidden state that make code hard to trace.
- `principle-model-the-domain`: Encode repeated state and branching rules in domain structures.
- `principle-never-block-on-the-human`: Proceed with reversible work and surface the result.
- `principle-outcome-oriented-execution`: Drive rewrites and migrations toward the target design.
- `principle-prove-it-works`: Verify the real artifact before declaring work complete.
- `principle-redesign-from-first-principles`: Integrate new requirements into the design at its foundation.
- `principle-separate-before-serializing-shared-state`: Remove shared writers before adding serialization.
- `principle-sequence-verifiable-units`: Break multi-step work into small, checkable units.
- `principle-subtract-before-you-add`: Remove dead weight before adding new structure.
- `principle-type-system-discipline`: Use types to make invalid states and contracts explicit.

### Artifacts and research

- `excalidraw`: Create Excalidraw diagrams that explain systems and workflows.
- `explain-diff`: Create a self-contained HTML explanation of a code change.
- `explain-diff-notion`: Create a rich Notion explanation of a code change.
- `research-paper-reading`: Explain technical papers with source-backed analysis and diagrams.
