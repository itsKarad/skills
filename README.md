# Shared LLM skills

A portable collection of skills I use across LLM agents.

## Skills

- `grill-me`: user-invoked entry point for pressure-testing a plan or design.
- `grilling`: companion interview primitive used by `grill-me`.
- `explain-diff`: creates a self-contained interactive HTML explanation of a code change, diff, branch, or PR. 
- `explain-diff-notion`: creates a rich Notion-page explanation of a code change, diff, branch, or PR. Useful for persisting data into Notion.
- `excalidraw`: creates and visually validates Excalidraw diagram JSON files, with renderer and schema references bundled in the skill folder. I usually use this skill for understanding the design of a complex codebase or component. I also use this skill for making system design architecture diagrams for sharing with a coding agent.