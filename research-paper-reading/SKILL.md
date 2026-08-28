---
name: research-paper-reading
description: "Read and explain technology and systems research papers from supplied links or PDFs, with source-backed analysis, deep architecture walkthroughs, and Excalidraw diagrams."
---

# Research paper reading

Use this skill when the user wants to understand one or more research papers about computing, systems, software, hardware, networking, security, or related technology.

## Start with the sources

Begin by accepting paper URLs, local PDFs, uploaded files, or a mix of them. If the user has not supplied a source, ask for the links or PDFs before attempting an analysis.

Create a `references/` directory in the current analysis workspace. Put every source artifact there, including:

- downloaded PDFs and HTML articles
- supplementary papers, technical reports, datasets, source code, and documentation
- figures or images that help explain the paper
- any local files copied into the workspace
- a machine-readable manifest of where each artifact came from

Run `scripts/collect_references.py` for supplied URLs and local files. It creates the directory, preserves useful filenames, avoids overwriting existing files, and writes `references/manifest.json`. Use the browser or web tools to discover additional sources, then save those artifacts into `references/` as well. Do not claim that an artifact was downloaded if the request failed. Record failures in the manifest or explain them in the response.

Keep original sources separate from your notes. Store analysis notes and diagrams outside `references/`, unless the user asks for everything in one folder. Never modify a downloaded source.

## Read in layers

Read the paper itself before relying on commentary about it. For a long paper, work through the abstract, introduction, figures, system or method sections, evaluation, limitations, and conclusion, then return to details needed to resolve open questions. Inspect tables, captions, appendices, and supplementary material when they affect the claims.

Build a claim ledger while reading. For each important claim, record the local source artifact and page, section, figure, table, or URL that supports it. Mark statements as one of:

- `paper claim`, when the authors state or measure it
- `reported result`, when it comes from an experiment or comparison
- `interpretation`, when you infer meaning from the paper
- `open question`, when the paper does not establish the point

Do not invent missing implementation details. Say when the paper leaves a choice unspecified. Separate the authors' novelty claim from your assessment of how strong or narrow that novelty is.

## Produce the explanation

Unless the user asks for a different format, explain the paper in this order:

1. **One-paragraph overview.** State the problem, why existing approaches fall short, what the paper builds or proves, and the main result.
2. **Core idea.** Explain the smallest idea that makes the paper work. Include the key abstraction, algorithm, protocol, or systems tradeoff.
3. **What is new.** Identify the claimed contribution and the actual evidence for it. Use "novel" only when the paper or a reliable comparison supports that wording. Explain what the work does not establish.
4. **Architecture.** Trace the system from input to output. Name components, data structures, control paths, state, scheduling, failure handling, and external dependencies. Explain why each component exists and what would break if it were removed.
5. **Execution walkthrough.** Follow one concrete request, job, packet, query, or training step through the system. Use real names and formats from the paper when available.
6. **Evaluation.** Explain the baselines, workload, metrics, ablations, and threats to validity. Quote exact numbers sparingly and include the comparison that gives each number meaning.
7. **Limits and follow-up questions.** Cover assumptions, costs, missing experiments, deployment constraints, and questions a reader should investigate.
8. **Source map.** Link each major section of the explanation to the relevant local artifact and page or section, plus stable web sources when used.

For architecture explanations, prefer concrete detail over a list of component names. Include data movement, timing, ownership of state, synchronization, consistency, retries, backpressure, and failure paths when the paper discusses them. If the paper presents only a conceptual design, label the walkthrough as a reconstruction rather than an implementation fact.

## Make diagrams part of the argument

The answer must contain text and at least one Excalidraw visualization for a systems paper, unless the user explicitly asks for text only. Use the available `excalidraw` skill. Read its color palette and relevant templates before creating diagrams, and follow its render, inspect, and fix loop.

For a substantial paper, create separate diagrams when they answer different questions:

- a summary flow showing the problem, intervention, and outcome
- a component architecture showing boundaries, state, and data/control paths
- a detailed execution or failure-path view when the behavior is easy to misunderstand

Use real component names, message types, APIs, formats, and measured quantities from the paper. Add evidence artifacts such as a small input/output example, a protocol message, a timeline, or a compact pseudocode fragment. Do not fill the canvas with generic boxes. The layout should show causality, fan-out, convergence, cycles, or separation where those relationships matter.

Save diagrams in the analysis workspace, for example `paper-architecture.excalidraw`, and render each one to PNG for visual inspection. Include links to the `.excalidraw` files and rendered images in the final response. If a diagram cannot be rendered because the Excalidraw setup is unavailable, report that clearly and still provide the JSON artifact when possible.

## Writing standard

Use `$unslop` while drafting and revising the explanation. Write in plain, direct language. Vary sentence length, use active voice, avoid inflated claims, and do not hide uncertainty behind vague phrases. Prefer "the paper measures" or "I infer" over anonymous authority. Do not use a polished tone to paper over a weak result. State the interesting tension plainly when a design is impressive but costly, narrow, fragile, or difficult to reproduce.

## Final checks

Before answering, verify that:

- all supplied sources were copied or downloaded into `references/`
- `references/manifest.json` identifies each artifact and failed fetch
- the explanation distinguishes paper claims from interpretation
- important numbers have a source location
- the architecture follows actual data and control flow
- diagrams use paper-specific evidence, render successfully, and have no clipping or overlap
- the prose has been revised with `$unslop`
