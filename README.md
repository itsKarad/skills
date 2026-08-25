# Shared LLM skills

A portable collection of skills I use across LLM agents.

## Included

- `grill-me`: user-invoked entry point for pressure-testing a plan or design.
- `grilling`: companion interview primitive used by `grill-me`.
- `explain-diff`: creates a self-contained interactive HTML explanation of a code change, diff, branch, or PR.
- `explain-diff-notion`: creates a rich Notion-page explanation of a code change, diff, branch, or PR.

The two skills are kept together because `grill-me` delegates its behavior to `grilling`.

## Source

Adapted from [Matt Pocock's skills repository](https://github.com/mattpocock/skills), specifically [`grill-me`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) and [`grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md).
