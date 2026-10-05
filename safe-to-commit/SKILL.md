---
name: safe-to-commit
description: Review files about to be staged or committed for secrets, machine-specific paths, and references outside the project.
---

# Safe to commit

Use this skill before staging files or creating a commit. It checks the proposed Git changes for credentials and machine-specific content that should stay local.

This is a review, not a guarantee that a repository is secret-free. Never print a suspected credential value into the chat or terminal output.

## Workflow

1. Find the project root with `git rev-parse --show-toplevel`. Identify the intended files from the user's request or the pending checkpoint. Review staged, modified, and untracked candidate files. Include ignored files only when the user intends to add them. If the user asks for a whole-repository audit, expand the scope to tracked project files.
2. Inspect the candidate paths before opening file contents. Flag sensitive filenames and directories such as `.env` files, credential stores, private keys, cloud CLI credentials, package publishing config, and local database or editor state. Check symlinks and report any target outside the project root.
3. Review candidate text contents and diffs for passwords, API keys, access tokens, private key material, connection strings, cookies, and other credentials. Use an installed secret scanner such as `gitleaks` when available, then inspect its findings. Also search for common credential formats and suspicious high-entropy values. Treat scanner output as leads, not proof. Do not install tools or send repository contents to external services.
4. Look for machine-specific references: absolute paths under a user's home directory, `/Users`, `/home`, or Windows profile directories; `file://` links; local hostnames and IPs; paths that traverse above the project root; and references to files elsewhere on the developer's machine. Inspect scripts, configuration, documentation, IDE settings, and symlink targets. Distinguish generic system paths and documented examples from references tied to this machine.
5. Report findings with file and line where possible. Redact secret values; show only the type of value and enough surrounding context to locate it. Classify each as likely secret, possible secret, machine-specific path, outside-project reference, or benign example. State the scan scope and any files or formats you could not inspect.
6. Do not stage, delete, rewrite, or otherwise alter files. If a likely credential or private local reference appears in the candidate set, tell the user to remove it or explicitly resolve the finding before staging. Do not declare the changes safe based only on a clean scanner result.

## Completion

Give a concise result that names the reviewed scope, lists actionable findings without exposing secret values, and says whether the proposed files are clear to stage or need review. "No findings" means this review found no matching issue in the inspected files; it does not prove that no sensitive data exists.
