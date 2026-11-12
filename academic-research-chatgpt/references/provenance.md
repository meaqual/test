# Provenance and adaptation boundaries

## Origin

This is an independent ChatGPT adaptation created at the user's request. It is not an
official release of Academic Research Skills, and neither its installation nor its name
implies endorsement by the original author, Anthropic or OpenAI.

Original project: [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)
by Cheng-I Wu (Imbad0202). Original copyright notice: Copyright (c) 2026 Cheng-I Wu.

The inspected source is the author's [ARS-Codex distribution](https://github.com/Imbad0202/academic-research-skills-codex),
version 3.24.2, at revision 82725acb393c4410ac6f47634a7f51b40a162fa4.
Its manifest pins Academic Research Skills v3.24.2 to
fd5ff1b858374219b4d342e38587b66e18f61cbd. In that distribution the main workflow
entrypoints are renamed from SKILL.md to WORKFLOW.md under the ars/ directory.

The supplementary experiment guidance draws on the separately identified
[experiment-agent project](https://github.com/Imbad0202/experiment-agent),
revision e291e7dc7ca268b2de7e1a9cf23bc2eef5dc0651, as vendored in the inspected distribution.

Adaptation version: 1.1.0. Adaptation date: 2026-11-12.
The machine-readable source record is [manifest.json](../manifest.json).

## License and attribution

The original ARS material is licensed under Creative Commons Attribution-NonCommercial 4.0
International. The original copyright notice and full license text are retained in
[LICENSE](../LICENSE). This adapted material is provided under the same license. Follow
that text for its terms. All workflow references identify the upstream files used.

ARS also acknowledges the claim-strength ladder/invariant-checking mechanism shape from
[sci-ssci-skills](https://github.com/Yila-AI/sci-ssci-skills), recorded in its THIRD_PARTY.md.
This adaptation preserves the general principle of not silently strengthening claims;
it does not copy that project's code or provide its deterministic invariant checker.

The adaptation is self-contained at runtime. It does not need the source checkout,
the user's original download location, a Claude installation, an API key, or GitHub access
to read its instructions. Sources are recorded for attribution and traceability, not
silently downloaded or executed during use.

## What was adapted

Version 1.1.0 adds recent-work direction mapping, makes assessment-first revision explicit,
and moves host-specific loading recovery and shortcut routing to a separate usage reference.

- Converted research, writing, review, revision and pipeline guidance into native ChatGPT
  task routing with on-demand references and explicit evidence boundaries.
- Added standalone reference/claim verification and compact continuation records.
- Added context-sensitive academic triggers and portable, paginated skill/reference
  loading with bounded recovery, stale-snapshot handling and accurate partial-load reporting.
- Preserved explicit study screening and experiment planning/analysis with honest
  capability limits, provenance and uncertainty.
- Replaced fixed Claude roles, model settings and tool names with available native browsing,
  computation, artifact skills and bounded collaboration.
- Kept ars-* names as text shortcuts. These do not register commands with the application.
- Reused user-supplied criteria and authority instead of imposing repeated routine
  confirmation cards or fixed interview/iteration counts.
- Defaulted explanations to Simplified Chinese in Chinese conversations while preserving
  manuscript language and explicit user preferences.
- Added scope-sensitive abstract assessment and optional EDA review questions. These are
  analytical aids, not official DAC/ICCAD rules or a substitute for current venue guidance.
- Replaced universal statistical cutoffs and arbitrary reproduction tolerances with
  study-specific assumptions, uncertainty, and declared comparison criteria.

## What is not included

This package does not reproduce Claude plugin hooks, registered subagents, local model/API
wrappers, upstream Python automation, exact Material Passport JSON schemas, cryptographic
receipts, automatic source refresh, fixed-size review panels, or the upstream evaluation
corpus and developer tests.

Native execution can still calculate from supplied data, inspect code, create documents,
or delegate useful work when the host permits it. Such actions are recorded as actual
native operations, not attributed to an unrun upstream script. An inline role pass is not
an independent review; a manually completed check is not mechanical enforcement.

The package makes no measured claim of research accuracy, publication acceptance, citation
completeness, official guideline compliance, or equivalence to the entire upstream runtime.
Verify scientific claims against actual evidence and describe material limitations.
