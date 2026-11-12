# Academic writing and abstracts

## Contents

- Scope and intake
- Evidence and argument
- Drafting and editing
- Abstracts
- Literature-review writing
- Citations, disclosure, and document formats
- Output and final checks
- Adaptation sources

## Scope and intake

Use this workflow for planning, outlines, drafting, abstract writing, editing, literature-review prose, and publication preparation. Select the requested scope immediately. An abstract request does not start a full-paper pipeline; a formatting request does not authorize changing the research claims.

Reuse the user's supplied research question, contribution, venue, target audience, language, length, source set, and earlier decisions. Do useful work with available material. Ask only for a missing fact that materially changes the requested deliverable. If the user has supplied only a broad topic and wants help developing a study, help narrow the question before treating it as an established contribution. An explicit request for a tentative outline can proceed with clearly labeled assumptions.

Explain decisions in Simplified Chinese unless the user requests otherwise. Preserve the manuscript's requested language and citation convention. Do not automatically add a second-language abstract, extra sections, or new experiments.

When reviewing or revising an existing manuscript, lead with the overall assessment, concrete issues, and proposed changes. Give a complete rewrite or full LaTeX source only on explicit request. Provide a targeted edit when the user asks for one.

## Evidence and argument

For substantial new drafting, establish a compact argument map:

| Element | Record |
|---|---|
| Research question | The question the study actually answers |
| Contribution | The proposed advance, with its scope |
| Claim | One testable, analytical, or conceptual assertion |
| Evidence | Supplied result, identified source, derivation, or missing support |
| Reasoning | Why that evidence supports this assertion |
| Boundary | Assumptions, alternatives, and limits on generalization |

Keep user-provided results, externally verified literature, and proposed future work distinguishable. A claim reported in a draft is not an independently verified result. Never invent citations, datasets, baselines, numerical gains, experimental settings, implementation details, or completed studies. When necessary, produce a bounded draft with clearly marked missing information, rather than filling the gap with plausible facts.

Explain the contribution relative to the nearest relevant work when that work is available. Avoid absolute priority claims such as “the first” without an appropriately bounded literature investigation. Never invent search dates or databases to make a novelty claim appear verified. Clearer wording may emphasize a supported contribution; it must not enlarge it.

## Drafting and editing

For an outline, map sections to questions, claims, and supporting material. Fit the requested article type and space budget; do not impose IMRaD on every discipline. An engineering paper may instead use problem formulation, method, implementation, evaluation, and discussion when appropriate.

For drafting, build a traceable sequence: problem and consequences; limitation of existing approaches; research question or objective; proposed mechanism; evidence; interpretation and limits. Write paragraphs around one substantive point. Use concrete subjects and verbs, consistent terminology, and proportionate technical detail. Connect each experimental finding to the claim it supports.

For editing, preserve numbers, units, mathematical meaning, method names, citation targets, and the user's chosen contribution. Prefer targeted changes when the user requests local revision. Separate stylistic improvement from changes that would require new evidence or a scientific decision. Apply already authorized changes; do not ask again merely because a workflow has another stage.

Maintain claim strength during rewriting and compression. Do not turn association into causation, a selected benchmark result into general superiority, a simulation success into correctness, or a proposed mechanism into a proven guarantee. Preserve qualifiers that bound the claim, such as the evaluated conditions, task, population, or uncertainty. Improve emphasis and sentence structure without silently removing those limits.

If the user asks to shorten text, preserve the problem, gap, differentiating mechanism, evaluation scope, and supported outcome before removing explanatory detail. If the user specifies facts or wording that must remain, treat them as explicit constraints. Check the actual word count when a strict limit matters.

## Abstracts

Write an abstract from supplied evidence using the needed components: problem and significance; unresolved difficulty; approach and its distinguishing mechanism; evaluation and results; supported implication. Adapt emphasis and sentence allocation to the paper and venue rather than forcing a fixed number of sentences.

Make the problem's consequence concrete. State what current approaches struggle to diagnose, repair, measure, or establish when that is the paper's motivation. Explain the proposed method enough for the reader to recognize its contribution, without expanding the abstract into an implementation inventory.

Use quantitative results only when supplied or verified. If only qualitative outcomes are available, state them with the actual comparison and evaluation scope. Do not add benchmark names the user has chosen to omit. When evaluations measure different capabilities, preserve that distinction. For example, repair on original testbenches and localization under injected faults support different claims.

For abstract-only critique, evaluate clarity, argument continuity, identifiable novelty framing, technical specificity, evidence wording, and fit to the stated audience. Distinguish “not explained in the abstract” from “absent from the research.” Do not infer full-paper methodological validity, comprehensive novelty, or an acceptance verdict from the abstract alone. Provide text-local reasons and practical edits without demanding that every full-paper detail appear in the abstract.

If two languages are requested, compose fluent versions with the same claims, numbers, scope, and limitations. Check semantic alignment rather than requiring sentence-by-sentence translation. Define acronyms within each abstract when needed for its intended audience; follow an explicit venue convention if supplied.

## Literature-review writing

Distinguish writing a related-work or literature-review section from conducting a systematic review. For prose based on supplied papers, synthesize themes, competing findings, methods, limitations, and the relationship to the user's question. Do not turn a source list into a succession of isolated paper summaries.

Attach important comparative claims to identifiable sources and record access limitations. An abstract or search snippet is not full-text verification. If the user requests new discovery or a systematic review, use the research workflow first; do not label an informal search exhaustive or systematic.

## Citations, disclosure, and document formats

For citation checks, separate bibliographic existence, metadata correctness, in-text/reference-list consistency, and whether the cited passage supports the claim. A DOI match does not establish claim support. Preserve the source version used and report unavailable full text or unresolved matches. Use current primary sources for verification and the user's requested citation style.

For AI-use or funding/authorship statements, use only the activities, roles, and support the user has actually supplied. Check current official venue requirements when the requested statement depends on them. Do not claim compliance from memory or invent approvals, contributions, funding, or disclosures. Draft a bounded statement while identifying any required missing facts.

For LaTeX, DOCX, PDF, figures, or other deliverables, use the host's relevant document skills and available tools. Preserve the established template. Inspect the rendered result when layout matters and report any build limitation. Do not claim a document was compiled, a figure was checked, or a file was created without the corresponding evidence.

## Output and final checks

For new drafting, lead with the requested text. For review or revision, lead with the assessment. For a substantive revision, explain the consequential changes and unresolved evidence needs. Offer variants only when they illuminate a real choice or the user requests them.

Before delivery, verify the requested scope, language and length; unchanged factual values; coherent terminology; traceable claims; preserved limitations; and consistency among abstract, body, tables, figures, and conclusion to the extent those materials were provided. Clearly distinguish completed checks from unavailable ones.

## Adaptation sources

Derived and condensed from ARS `academic-paper/WORKFLOW.md`, `academic-paper/agents/argument_builder_agent.md`, `academic-paper/agents/draft_writer_agent.md`, `academic-paper/agents/abstract_bilingual_agent.md`, and `academic-paper/references/abstract_writing_guide.md`. These paths identify upstream methodology; they are not runtime dependencies of this adaptation. See the skill's provenance record for attribution and changes.
