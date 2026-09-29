---
name: pr-lunchbox
description: Write a paste-ready Markdown PR description from a repository change, commits, or completed task, with a newcomer-friendly overview, file-by-file summary, and verified testing.
---

# PR Lunchbox

Write a PR description the user can paste directly into a pull request. Return the entire description in one fenced `markdown` code block.

Use this order:

1. **Overview.** Explain the problem the PR fixes and the resulting behavior in plain language. Give enough context for someone new to the repository. Keep this at a high level.
2. **File-by-file changes.** List every file in the requested change. For each file, explain its role and the main change in one or two sentences. Group related files under short headings if that makes a large change easier to scan, but keep a distinct entry for each file. Explain behavior and purpose, not individual lines.
3. **Testing and validation.** State which automated tests were added or run and what manual checks were performed. Distinguish passed, failed, and unrun checks. Include relevant commands or results when available, and do not claim a check happened without evidence.

Inspect the actual diff or commits and the available test output before writing. If the user supplies a draft or a specific commit range, use that scope. For work completed in the current task, use the changes and checks actually made. If evidence for a section is missing, say so briefly inside that section rather than inventing details. Omit unrelated worktree changes.

Use short, approachable sentences and explain repository-specific names when a new reader would not know them. Follow any additional PR template or format the user provides, while preserving the three requested sections and the outer Markdown code block unless the user explicitly changes that preference.
