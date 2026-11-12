# Research and evidence synthesis

Apply the root skill's authority, language, source, and capability rules. Choose the smallest workflow that completes the requested deliverable. Read supplied research questions, source lists, results, and prior decisions before asking for information again. Preserve an explicit mode even when its inputs are incomplete.

## Select a mode

| Request | Method and usual output |
|---|---|
| Quick background or decision brief | Bounded search; answer, supporting evidence, uncertainty, and references |
| Deep research with an answerable question | Scope, investigate, synthesize, challenge, and report |
| Literature review | Source matrix, thematic or methodological synthesis, disagreements, and bounded gaps |
| Three-way paper comparison | Compare WHY (problem), HOW (method), and WHAT (findings and limits) |
| Fact-check | Claim-by-claim support assessment with source locators |
| Map a research direction or recent work | Compare research lines, representative studies, benchmarks, and evidence-backed open questions |
| Explore or refine a research direction | Guided question refinement; candidate questions and feasible study options |
| Explicit systematic review or meta-analysis | Documented protocol, search, selection provenance, extraction, appraisal, synthesis, and reporting coverage |

A request for an abstract, manuscript revision, or peer review stays in the writing/review workflow. A literature review does not automatically become a systematic review. Do not begin record-level screening merely because supplied material includes database exports; use the screening reference when the user explicitly requests screening.

## 1. Establish the research frame

Extract the question, intended use, field, audience, scope, relevant time interval, geography or population, requested depth, and available materials. Infer routine details where reasonable and label assumptions. Ask only for missing decisions that materially change the work.

For an unclear research direction, identify the actual bottleneck, unit of analysis, variables or constructs, available evidence, and a feasible contribution. Evaluate feasibility, relevance, ethical constraints where applicable, and what would distinguish the result from existing work. Suggest candidate questions when the user wants ideas; use a question-led approach when they request coaching. Do not invent novelty scores or force a fixed number of dialogue rounds.

For a settled question, record a compact brief: question, subquestions, in/out scope, evidence needed, and intended output. Reuse an already accepted brief. Ask before materially changing the research question or study design; a routine search refinement is not a new authorization gate.

## 2. Retrieve and inspect evidence

Use supplied papers and bibliographies first, then fill gaps. For external research, search using the available browsing tools and open relevant sources. Prefer original papers, official documentation, datasets, standards, and other primary material suited to the claim. Use reviews for orientation and synthesis without treating their cited studies as read.

Record the actual search sources, dates, query concepts, and material scope limits. A general web search is not an exhaustive scholarly-database search. Keep retrieved counts distinct from eligible, included, or fully read counts. Do not infer zero relevant studies from an unsuccessful search.

Maintain an evidence matrix proportionate to the task:

| Field | Record |
|---|---|
| Identity | Stable source ID, title, authors, year, URL/DOI, and version when available |
| Access | Full text, specified sections, abstract only, metadata only, or inaccessible |
| Substance | Question, design, data, method, main finding, and relevant limitations |
| Support | Exact claim supported and a page, section, table, figure, or passage locator |
| Appraisal | Fit for this claim, methodological limitations, conflicts, and unresolved checks |

Separate verifying that a source exists from verifying that it supports a claim. Preserve preprint/published-version distinctions. Mark inaccessible sources as candidates or unresolved references. Do not invent metadata, quotations, page numbers, findings, or access. Evaluate evidence by the discipline and question: a clinical study hierarchy is not a universal ranking for engineering, mathematics, or humanities.

## 3. Synthesize and challenge

Organize around the research question, mechanisms, methods, and evidence rather than listing papers one by one. Explain where findings converge or conflict and whether differences in populations, designs, metrics, datasets, assumptions, or conditions account for the discrepancy. Distinguish reported observations, author interpretations, and the assistant's inferences.

Test the emerging explanation against counterevidence, plausible alternatives, selection effects, and missing comparisons. Identify the condition under which a claimed advantage or mechanism would fail. State gaps relative to the inspected literature; avoid unbounded claims such as "no previous work" without an appropriately comprehensive basis.

For source-specific methodological weaknesses, label author-acknowledged limitations with locators and reader-inferred concerns as untested inferences. Limit absence claims to sections actually inspected. With only an abstract, describe what cannot be assessed; do not invent a flaw in the unseen method.

Use native subagents only when independent source subsets or challenge questions would help. Consolidate their evidence yourself and verify material citations. Describe actual work performed; several role perspectives in one session do not constitute independent replication or cross-model verification.

## 4. Deliver according to the mode

- **Research brief/full report:** direct answer, scope, evidence-backed analysis, disagreements, limits, and references. Include a research plan only when requested or required by the question.
- **Literature review:** evidence matrix plus an argument organized by themes, technical approaches, or development of the field; connect each gap to a concrete unresolved question.
- **WHY/HOW/WHAT:** compact per-paper comparisons, common motivation, differing methods, supported outcomes, and remaining uncertainty. Suggest new research directions only when requested.
- **Fact-check:** claim, verdict (supported, partly supported, contradicted, or unresolved), evidence, scope qualification, and a correction if justified. Inaccessibility is not falsity.
- **Question refinement:** a usable question, rationale, scope, feasible evidence strategy, and the next material decision. Do not manufacture findings for the proposed study.

## Research direction mapping

Set a time window that reflects the request and state the actual search date. Start from recent work and include earlier work when it establishes a method, benchmark, or problem definition. Search terminology variants and follow relevant citations to distinguish emerging topics from renamed approaches.

Group studies by research question or technical approach. For each group, identify representative papers and their publication status, methods, datasets or benchmarks, evaluation criteria, recurring results, and unresolved assumptions. Distinguish an evidenced gap from a gap in search coverage. When the user requests directions to pursue, connect each candidate question to the relevant work, a feasible experiment or analysis, and what evidence would distinguish it from the closest prior work.

## Systematic review and quantitative synthesis

Record the chosen review type and protocol: question framework, eligibility criteria, information sources, reproducible queries, time limits, selection procedure, extraction fields, appraisal method, and planned synthesis. Record registration as a real status; do not claim registration or reporting-guideline compliance without evidence. Distinguish a protocol draft or review plan from a completed review.

Use a supplied, documented screened corpus or an explicitly authorized screening workflow. If selection remains unresolved, complete the useful search/protocol work and identify that missing step rather than fabricate a selected corpus. Report actual study-flow counts and unresolved records. An attractive flow diagram does not establish exhaustive coverage.

Extract design-appropriate data and assess bias using a justified framework. Pool only compatible outcomes and study designs. Identify the effect measure, uncertainty, model, dependencies, heterogeneity, planned sensitivity analyses, and limitations before calculation. Compute from actual data with available analysis tools; otherwise provide an analysis plan. Do not fabricate pooled estimates, confidence intervals, certainty grades, or publication-bias conclusions. Verify current reporting requirements when making formal compliance claims.

## Handoff

Pass the accepted question, inspected source matrix, synthesis, actual selection status, constraints, and unresolved evidence gaps into writing. Reuse existing work instead of repeating intake or search. Do not represent proposed methods, secondary summaries, or planned experiments as completed original research.

## Upstream basis

Adapted from `ars/deep-research/WORKFLOW.md`; `ars/deep-research/references/source_quality_hierarchy.md`; `ars/deep-research/references/systematic_review_protocol.md`; and the source-specific weakness rules in the three-way-scan workflow. See `provenance.md` for source identity, attribution, and license. This adaptation replaces fixed agents, model tiers, proprietary calls, rigid report lengths, and executable handoff schemas with native capabilities and explicit evidence records.
