# Evidence and citation verification

## Contents

- Scope and records
- Citation checks
- Empirical checks
- Reading declarations and stale evidence
- Reporting and method provenance

## Scope and records

Identify the available material: bibliography, abstract, manuscript, source PDFs, data,
code, logs, or a mixture. State the actual check. A valid DOI, successful execution, or
polished text does not establish every scientific claim.

Respect an explicit source boundary. For a supplied-text-only task, use that text and mark
external verification unperformed. Otherwise use browsing when current, niche, uncertain
or source-dependent facts require it. Prefer primary sources for technical claims. Read
the cited version; do not silently substitute a later preprint or another paper.

Separate bibliographic identity, formatting, claim support and empirical validation. A
formatting pass is not a source-integrity pass. Isolate uncertain claims while continuing
unaffected authorized work.

Use a source ledger for substantive checking:

| Source ID | Title/authors/year | DOI or stable URL | Version | Accessed material | Locator | Check date |
|---|---|---|---|---|---|---|

Describe access concretely: metadata, abstract, supplied excerpt, named pages, or full text.
Record access failure and version ambiguity. A search snippet is not full-text reading.

For multiple claims, keep:

| Claim ID and exact text/span | Source and locator | Observation | Judgment | Action |
|---|---|---|---|---|

Use explicit judgments:

- Supported within checked scope: accessed evidence supports this wording.
- Partially supported: evidence supports a narrower claim; identify the difference.
- Unsupported within checked material: the inspected material does not substantiate it.
- Contradicted: accessed evidence directly conflicts with the claim.
- Unresolved: required evidence cannot be accessed or identified.
- Not checked: outside scope or not yet examined.

Missing access is not proof of fabrication. Valid metadata is not claim support. Keep
suspected problems provisional. Record a calculation's actual inputs and method separately
from its source citation.

## Citation checks

1. Extract the reference and the statement it supports. With a bibliography alone, perform
   identity/format checks; do not claim to audit absent manuscript claims.
2. Resolve title, authors, year, venue, DOI and cited version using a primary record.
   Check corrections/retractions when relevant using current evidence.
3. Open the source and locate the supporting page, section, figure or table. Retain locators
   even when the final response uses the host's native citation system.
4. Compare population, hardware/task, conditions, baseline, metric, uncertainty, limitations
   and causal force. Inspect each source's contribution in a multi-source citation.
5. Detect association changed into causation, local results into universal superiority,
   proposed experiments into completed results, or small benchmarks into deployment claims.
6. Narrow the claim, replace the source with a verified suitable reference, or mark unresolved.
   Explain substantive changes. Never fill a citation gap with an invented reference.
7. Apply the requested citation style using supplied or verified rules. Keep style corrections
   separate from source truth and preserve accurate titles and authors.

A matching title or source existence does not establish support. A repository description
does not establish measured performance. Record software/version conditions where material.

## Empirical checks

Where relevant, examine these risks against the available evidence:

- Implementation errors invalidating measurements.
- Invented, mislabeled or untraceable results.
- Leakage or shortcuts that avoid the intended benchmark capability.
- Bugs/anomalies described as scientific discoveries.
- A described method that differs from code, protocol or observed execution.
- Premature commitment to a framing despite contrary evidence.
- Fabricated or non-supporting references.

For each applicable concern, give evidence, impact and action. Use not applicable or not
assessed honestly. A checklist is not a research-integrity certificate. Do not generate
numerical integrity or fabrication-risk scores.

Recompute only from actual data and calculations. Preserve absolute versus relative
change, denominators, units, sample sizes and uncertainty. In EDA, distinguish simulation
completion, test success, coverage adequacy and evidence of correctness.

For reproduction, record input version, environment, command, seed, outputs and declared
comparison criterion. Label missing components untested. Importing, compiling, or running
without errors is not reproduction of reported findings.

For central unsupported claims, propose obtaining evidence, narrowing, labeling a hypothesis,
or removal. Author preference may choose the writing strategy; it cannot turn an unverified
statement into a verified fact. Never conceal a known contradiction with cautious-sounding prose.

## Reading declarations and stale evidence

Separate model access from author reading. Mark a source as author-read only after explicit
author attestation, with source/version and scope (full text, named sections, or abstract).
Clarify a materially ambiguous scope. An upload is not a reading declaration; a declaration
is not proof of comprehension. Retract it on request.

When a manuscript claim, cited version, dataset, code revision or assumption changes, mark
affected checks stale and recheck them. Preserve unrelated completed checks. For
ars-cache-invalidate, retire the specified local evidence entry; do not delete sources or
pretend an external cache was changed.

## Report the findings

Lead with the practical finding and checked scope. For one claim, give the exact issue,
an evidence-supported repair, and missing material. For many references, report actual
counts examined, supported, mismatched and unresolved. Do not say all citations were
verified when only a sample, metadata, or provided excerpts were checked.

Use genuine host citation IDs and usable URLs. Cite supplied files by real filename and
section where appropriate. Never invent retrieval references or an authoritative-looking
unverified bibliography.

## Method provenance

Adapted from ARS academic-pipeline/agents/integrity_verification_agent.md,
academic-pipeline/references/integrity_review_protocol.md,
academic-pipeline/references/ai_research_failure_modes.md,
academic-pipeline/references/claim_verification_protocol.md,
commands/ars-citation-check.md, commands/ars-mark-read.md,
commands/ars-unmark-read.md, and shared/handoff_schemas.md.
See [provenance](provenance.md). This ledger replaces upstream validators; it is not their
schema or enforcement mechanism.
