---
name: git-checkpoint
description: Create verified Git commits at meaningful milestones during a task when working inside a Git repository.
---

# Git checkpoint

Use this skill when the user wants milestone commits during a task. It applies only inside a Git repository.

## Workflow

1. At the start, identify the repository root, current branch, and existing worktree changes. Treat pre-existing changes as belonging to the user.
2. Define a small set of meaningful checkpoints from the task. A checkpoint should represent a coherent, reviewable unit such as a scaffold, a completed behavior, or a verified fix. Do not create commits for every file or trivial edit.
3. Before each checkpoint commit, run the relevant focused checks for the work completed so far. If checks fail, fix the issue or report it rather than presenting the commit as verified.
4. Stage only files or hunks produced for the current task. Do not absorb unrelated changes, secrets, generated artifacts, or the user's pre-existing edits. If a file mixes task changes with unrelated edits, use selective staging or leave that checkpoint uncommitted and explain why.
5. Create a normal commit with a concise message that describes the completed milestone. Never amend, rebase, reset, force-push, or otherwise rewrite history as part of this skill.
6. Continue work after each checkpoint. At the end, report the checkpoint commits and any remaining uncommitted changes.

If the current directory is not inside a Git repository, skip committing and continue the task normally. If there are no changes for a planned checkpoint, do not create an empty commit. For a genuinely one-step task, one verified final checkpoint is enough; for multi-stage work, commit at multiple natural boundaries.
