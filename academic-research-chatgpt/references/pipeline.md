# Research-to-paper pipeline

## Contents

- Activate and resume
- Stage sequence
- Evidence boundaries and revision
- Compact continuation record
- Delivery and provenance

## Activate and resume

Use this reference only for an explicit end-to-end request, ars-full, or continuation of
an established pipeline. Keep a standalone abstract edit, review, citation check or format
conversion in its narrower workflow.

Identify the requested deliverable, stopping point, target audience/venue, current draft,
available evidence and established author decisions. Reuse prior work. With only a broad
topic, help refine an answerable question; do not manufacture a completed empirical study.
With an existing draft and a full-pipeline request, enter at the pre-review evidence check.
Treat an old verification report as context and check its relevance to the current version.

Name a single lead to own state, source/claim IDs, revisions and the final synthesis.
Delegate bounded independent tasks only when the host supports them and this improves the
work. Keep the requested stopping point stable unless the user changes it.

## Stage sequence

| Stage | Work and reference | Deliverable and transition |
|---|---|---|
| 1. Frame and research | Read [Research](research.md); establish question, corpus and evidence | Scoped synthesis or study plan; proceed when the draft has a defensible foundation |
| 2. Plan and draft | Read [Writing](writing.md); map claims to evidence before substantive drafting | Requested draft with supplied results and visible missing evidence |
| 2.5. Pre-review evidence check | Read [Evidence](evidence.md); inspect consequential claims, references and numbers in the current draft | Scoped findings; correct known errors and expose material unresolved items |
| 3. Review | Read [Review/revision](review-revision.md); use the target and actual available material | Prioritized evidence-anchored findings and feasible revisions |
| 4. Revise | Implement authorized choices, preserve scientific meaning and track changes | Revised draft plus a focused change map |
| 3R. Re-review | Compare original findings with actual changes and supporting evidence | Resolved, partly resolved, unresolved or not assessed for each material issue |
| 4R. Further revision when needed | Address concrete remaining issues within authorization and requested effort | Updated draft; no endless automatic review loop |
| 4.5. Final evidence check | Re-examine the actual latest draft and its consequential claims, including new claims introduced during revision | Final checked scope, unresolved items and remaining limitations |
| 5. Format and deliver | Use the requested native artifact workflow and actual venue rules | Final requested artifacts, concise change summary and material limitations |

Both a satisfactory initial review and completion of any revision path lead to the final
evidence check before full-pipeline finalization. Do not skip it because a response letter
claims the issues are fixed. Conversely, do not impose this whole sequence on a narrow task.

A request to draft a full paper without data may yield a proposal, structured draft or
clearly labeled placeholders, depending on the user's intent. It must not yield invented
experimental results. Continue valid portions while asking for indispensable results.

## Evidence boundaries and revision

At each evidence boundary, inspect applicable bibliographic identity, citation context,
numbers/results, observed close textual matches and claim support. Prioritize headline,
quantitative, causal, methodological and disputed statements. Explain actual coverage;
do not claim exhaustive semantic extraction, plagiarism clearance or global correctness.

Use clear findings instead of invented integrity scores. Resolve contradicted or fabricated
content before presenting it as fact. For missing access or evidence, obtain sources, narrow
the claim, label the limitation, or defer that part. Ask the author to decide a materially
different research/writing strategy when necessary; reuse a decision already given.

Never label unverified work verified after the user elects to proceed. Acknowledging a
limitation does not authorize fabricated sources, experiments or support. An exploratory
or incomplete artifact can still be delivered when clearly labeled and useful.

Re-review the manuscript and its evidence before evaluating whether a response letter
accurately describes the change. Preserve unaddressed comments with an honest rationale.
Do not turn an internal review outcome into a real venue decision or acceptance probability.

Run additional rounds only to address concrete unresolved work or a requested gate. Preserve
original numbers, task scope, qualifiers and null/negative results. Report new evidence-driven
changes to the author. Do not replace scientific decisions with arbitrary quality scores.

## Compact continuation record

For a long task, keep a compact record in the user's existing project or supported persistent
artifact. For a short interaction, use only the needed fields in the conversation. This is
a ChatGPT adaptation record, not an upstream Material Passport schema or cryptographic receipt.

    task:
      objective:
      workflow_and_stopping_point:
      venue_or_audience:
      output_language:
      author_constraints_and_decisions:
    artifact:
      actual_file_or_conversation_reference:
      version:
      computed_hash_if_available:
    state:
      current_stage:
      completed_work:
      next_action:
      material_open_questions:
    evidence:
      source_ids_versions_and_access:
      claim_ids:
      check_report_reference_and_scope:
      unresolved_and_stale_items:
    experiments:
      planned_executed_or_analyzed:
      data_code_environment_and_output_references:
      negative_results_and_limitations:
    review:
      criteria_and_original_findings:
      author_dispositions:
      before_after_drafts_and_change_map:
      response_letter_if_any:

Use unknown/null when unavailable. Do not invent times, paths, hashes, reading declarations
or confirmations. Quote consequential author instructions accurately and preserve their
scope. A saved record helps continuity; it does not itself create user authorization.

On resume, inspect the current artifact and compare it with the record. Reuse applicable
decisions and completed checks. Stale the affected findings when source versions, claims,
data or assumptions change. Reconstruct uncertain state from actual materials before
claiming that a step is complete. Do not rerun the entire pipeline merely because context
was compacted.

## Delivery

Provide the artifact the user asked for, the consequential changes, what was checked, and
what remains unresolved. Keep a full process report optional unless requested. Generate
actual document/PDF/spreadsheet/slides artifacts using available native skills and honor
the host's storage and preview requirements. Verify generated layout when the chosen
artifact workflow requires it.

Do not submit to a venue, email reviewers, publish a draft, or upload unpublished material
to another provider without the corresponding authorization. Never claim a scheduled
follow-up or background monitoring unless a real supported task has been created.

## Method provenance

Adapted from ARS academic-pipeline/WORKFLOW.md,
academic-pipeline/agents/pipeline_orchestrator_agent.md,
academic-pipeline/agents/state_tracker_agent.md,
academic-pipeline/references/integrity_review_protocol.md,
academic-pipeline/references/two_stage_review_protocol.md,
academic-pipeline/references/claim_verification_protocol.md, and shared/handoff_schemas.md.
See [provenance](provenance.md). Mandatory upstream runtime dispatch, observer scores,
fixed retry counts, session-reset machinery and validator contracts are not reproduced.
