---
name: remember-failures
description: After a task succeeds despite repeated avoidable mistakes, record the verified recovery path in durable repository or task memory for the next agent.
---

# Remember failures

Use this after the requested task has succeeded and the agent repeated a wrong assumption or approach before finding the working one. A single ordinary failed attempt is not enough. Finish and verify the task first so the memory records a proven path.

## Capture the lesson

1. Reconstruct the loop from the task's actual evidence: what was attempted repeatedly, why it failed, what changed, and what confirmed success. Separate observed facts from guesses.
2. Reduce it to an instruction a future agent can act on at the start of the same kind of task. Name the trigger, the first useful check or action, and the verification signal. Include a failed approach only when knowing it would prevent the same loop.
3. Put the note where that agent will encounter it. For repository work, inspect existing `AGENTS.md` files and agent-facing documentation, then update the narrowest relevant location. If none exists, create a scoped `AGENTS.md` in the relevant directory. For work outside a repository, use the available persistent task memory. A note buried in this chat is not durable memory.
4. Keep the entry short and specific. Link to stable code or documentation when useful. Omit transcripts, temporary paths, secrets, and claims the successful run did not establish. Do not turn one incident into a universal rule.
5. Read back the saved note and check that its location is discoverable, its advice matches the verified result, and it does not conflict with existing instructions. Report where the lesson was stored.

If the same error can be prevented by a small check or code change within the task's scope, make that fix too. Keep the memory focused on the remaining judgment or workflow that a future agent needs.
