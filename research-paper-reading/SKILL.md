---
name: research-paper-reading
description: "Teach academic papers in finance, CS, mathematics, systems, ML, and AI section by section, with worked math, code, source-backed results, historical context, and an interactive HTML reading guide. Use when a user wants to read or understand a paper from a link or PDF."
---

# Research paper reading

Teach the paper to a proficient software engineer who has not studied advanced math. The goal is to let the reader reason through the method, follow its mathematics, and judge its evidence. A short summary cannot satisfy this task.

Default to a complete, self-contained HTML reading guide. Follow the presentation approach of `explain-diff`: skippable background, concrete intuition, detailed walkthroughs, diagrams, and an interactive quiz. The requirements below stand alone, so that skill is not a runtime dependency. Use `unslop` when available and apply the writing standard below in every case.

## Obtain and read the sources

Accept paper URLs, local PDFs, uploaded files, or an identifiable title. Resolve a title to a primary source and check authors and version. Ask for a source if none is supplied, or clarification if several papers match. Do not invent a paper to demonstrate the skill.

Create a separate analysis workspace outside the code repository unless the user specifies a location. Keep source artifacts in its `references/` directory and notes outside that directory. Use the bundled `scripts/collect_references.py` with `--output <analysis-workspace>/references` to collect supplied URLs and local files. It writes `manifest.json` and records failed fetches. Preserve originals. Save additional sources when permitted, or record their URLs and access limitations without claiming a download succeeded.

Read the full paper, including captions, tables, and appendices that support central claims. Inspect rendered pages where extraction loses equations, symbols, or layout. Check that a downloaded file contains the expected paper. If only an abstract or excerpt is accessible, state the coverage limit and request the missing material before claiming a complete walkthrough.

Record the title, authors, first public release date, venue date if different, and version used. Build a compact claim ledger in the notes. For each consequential claim, keep its source and precise location, such as section, page, equation, theorem, figure, or table. Distinguish author claims, reported measurements, proven results, your interpretations, and unresolved questions. Keep teaching examples separate from paper results.

## Build the reading guide

Use this order unless the user requests another. Retain the paper's original section names and numbering within the walkthrough so the reader can move between documents.

### Orientation and prerequisites

Start with a brief statement of the problem, the approach, and the main finding. Then show a reading map and the prerequisites this particular paper needs. Put optional foundations in expandable sections. Explain mathematical concepts at first use even if they also appear in the background.

Assume familiarity with code, APIs, data structures, and debugging. Do not assume fluency in calculus, linear algebra, probability, optimization, or proof techniques. Introduce only the background needed to understand this paper.

### Why this paper appeared when it did

Explain the prior bottleneck and what changed enough to make this work possible or worthwhile. Research the context using primary sources, including relevant prior papers, dated releases, datasets, hardware documentation, and the authors' contemporaneous explanations.

Identify enabling technology where supported. Other causes can include a new mathematical technique, cheaper computation, available data, infrastructure, a changed market, or a newly important problem. Do not force every paper into a hardware or technology story.

Use a short dated timeline when it clarifies the dependencies. Connect each proposed enabler to a specific part of the method or evaluation. Separate established history from a plausible inference. An earlier invention's existence alone does not prove it caused this paper. Do not attribute motives to authors without evidence or treat later technology as an original enabler. If the publication's exact timing is unknown, say so.

### Section-by-section walkthrough

Cover every substantive section, including relevant appendices. A brief abstract or conclusion can receive a short treatment; method, theory, and evidence need depth. Keep a coverage map for long papers and identify any appendix material omitted and why. Reorganize prerequisites when useful, but preserve links back to the original sections.

For each section, explain:

- The question it answers and how that question follows from the previous section.
- The argument, mechanism, or result in plain language, with its source location.
- The details needed to follow it, including definitions, assumptions, equations, algorithms, figures, and tables.
- A concrete worked example where the idea is difficult. Carry one running example across sections when possible.
- What the section establishes, what remains assumed, and what the next section needs from it.

Do not merely paraphrase headings. Reconstruct the reasoning. Explain consequential figures by identifying axes, units, trends, and what conclusion they support. For systems papers, trace actual data and control flow, state ownership, timing, and relevant failure paths. Label reconstructed implementation choices as teaching assumptions.

### Teach the mathematics through worked examples

For each central equation or theorem:

1. State the question it answers before presenting notation.
2. Define symbols, dimensions, units, domains, and assumptions. Distinguish a scalar, vector, matrix, random variable, and sample when that matters.
3. Read the expression aloud in ordinary language and explain why its terms are present.
4. Derive consequential steps without skipping the algebra or prerequisite idea that makes the transition valid. Explain a named rule before using it.
5. Work a small numerical example through intermediate values to the result. Connect the numbers back to the paper's purpose.
6. Show a boundary case, counterexample, or changed assumption that reveals where the reasoning stops working.

Separate intuition, proof sketch, and complete proof. Numerical examples illustrate a theorem; they do not prove it. If the paper omits a derivation, label any derivation you supply and check its assumptions against the original. Never repair an ambiguous equation silently.

For an equation-light paper, give equally concrete execution traces or invariants. Do not add irrelevant mathematics to meet a template.

### Explain the method with code

Include actual code blocks that teach the central computation, algorithm, simulation, or proof intuition. Prefer small runnable Python examples with explicit inputs, dependencies, and expected output. Use another language when it better fits the paper or the user's request.

Connect variables and code lines to the paper's notation and steps. Show intermediate values or shapes where they help. Explain simplifications and separate a teaching implementation from the authors' implementation or an experimental reproduction. Clearly label pseudocode if runnable code would hide or distort the idea. A simulation is not a proof.

Execute runnable examples when tools are available. Check their outputs against worked calculations using justified numerical tolerances. Record what ran and what did not. Never invent execution results. Avoid expensive training runs or large dependencies when a small calculation teaches the same point.

### Key insights

Give this its own section. Explain the few ideas worth retaining after the details fade: the observation, why it works, the tradeoff it introduces, and when it is useful. Link each insight back to the walkthrough. Distinguish the authors' claimed novelty from your assessment and support comparisons to prior work.

### Key results and strength of evidence

Give this its own section, separate from insights. For empirical results, use a compact table with the finding, baseline, metric and units, dataset or workload, conditions, and exact source location. Include uncertainty, repetitions, or significance when reported. Say when they are absent. Distinguish absolute changes, percentage points, and relative improvements.

For theoretical results, state the theorem in plain language, its assumptions, the guarantee, its scope, and the proof's central move. For mixed papers, cover both evidence types. Never invent benchmark numbers for a theoretical paper.

Explain which comparisons or ablations support each claim and which do not. Read evidence using the field's relevant constraints:

- Finance may require transaction costs, temporal splits, look-ahead bias, survivorship bias, and the difference between backtests and live results.
- ML and AI may require data leakage checks, compute budgets, seeds, evaluation protocols, and matched baselines.
- Systems may require workload realism, hardware, tail latency, throughput, resource costs, and failure behavior.
- Mathematics may require quantifiers, regularity assumptions, asymptotic conditions, and the difference between existence and a constructive algorithm.

Use only the checks relevant to the paper. Separate limitations the authors acknowledge from limitations you infer.

### Understanding check and sources

Finish with five medium-difficulty multiple-choice questions. Test reasoning about the method, math, evidence, and assumptions rather than names or dates. Use plausible misconceptions as distractors. Give answer-specific feedback after selection, including why a wrong answer fails and a link to the relevant explanation. Allow retrying.

End with open questions, limitations, and a source map. Cite major claims near the text as well as in the source map. Use stable primary-source links and precise paper locations. Keep quotations short and write explanations in your own words.

## HTML delivery

Write one long HTML page with embedded CSS and JavaScript, a table of contents, stable anchors, and sentence-case section headings. Do not use top-level tabs. Save outside the code repository with today's local date in the filename, for example `/tmp/YYYY-MM-DD-paper-reading-<slug>.html`. Avoid overwriting an existing guide silently.

The guide must work offline. Embed diagrams as inline SVG or HTML and images as data URLs when appropriate. Use native MathML, readable HTML notation, or bundled inline math-rendering code so formulas do not depend on a CDN. Escape source text and code before inserting it into HTML. External citation links may require a connection; reading the explanation and using its controls must not.

Use `<pre><code>` for code, with explicit `white-space: pre` or `pre-wrap` CSS. Preserve indentation and escape angle brackets. Give formulas a plain-language explanation and diagrams a text description. Use a small set of consistent diagram types with paper-specific values. Do not use ASCII diagrams or generic boxes that hide the mechanism.

Use readable line lengths, responsive layouts, accessible contrast, keyboard-operable controls, and visible focus. Use callouts for definitions, assumptions, and failure cases. Keep deep prerequisites expandable while leaving the main argument visible. Make quiz feedback readable to assistive technology. If a slider or stepper materially helps explain an equation or execution, connect it to the actual calculation and state the model's simplifications.

Check the saved file in a browser when available, at desktop and narrow widths. Check navigation, math rendering, code whitespace, diagram clipping, and correct and incorrect quiz choices. Ensure print styles reveal explanatory details and remove unnecessary controls. Report any verification you could not perform.

## Writing and completion

Apply `unslop` to the final prose. Use active voice, concrete nouns, and connected explanations. Remove hype, stock transitions, forced contrasts, and decorative headings. Use short sentences for difficult ideas. Keep formal notation and code exact even when the prose avoids jargon.

Before delivering, verify section coverage, source locations, historical chronology, numerical calculations, and distinctions between claims and evidence. Confirm that the HTML is self-contained and its controls work. Do not claim a complete guide if central sections remain unread or unexplained.

Return a short message linking to the HTML file, with material coverage or verification limits. Open it in the app when available. In follow-up tutoring, focus on the user's point of confusion with another worked example and revise the guide when requested. If the user explicitly asks for a paced reading session, teach one section at a time and keep the guide's completion status clear.
