# Skill access and ARS shortcuts

## Load the installed copy

A listed skill name is not a completed load. Use instructions actually read in this
conversation; reuse them on continuation when still available. Never claim a fresh read,
successful load, saved preference, or cross-conversation persistence without evidence.

1. Use the current catalog entry's exact `package` and `main_resource` with `skills.read`.
   If the entry is missing or a cached locator fails, discover available skills through
   `skills.list`. Follow every `next_cursor` until this skill is found or that catalog is
   exhausted. A first-page miss is not evidence that the skill is uninstalled.
2. Follow `skills.read` pagination when present. For a reference, retain the same package
   and replace the final `/SKILL.md` in its returned resource URI with the relative path,
   such as `/references/writing.md`. For filesystem access, resolve relative paths from
   the current read's verified `skill_root`. Do not guess a directory from the skill name,
   reuse a prior session's absolute path, or mix cloud and executor resource locators.
3. On a stale-path, not-found or provider-availability error, refresh discovery and retry
   once with current locators. Another available, authorized authority may expose the
   same active skill. Never bypass an access denial or disabled skill. If no supported
   read route is available, state that limitation; do not invent successful loading.
   After a confirmed update, a host may still serve an earlier snapshot. If a verified
   installed filesystem root is available, read the current files there. Otherwise
   report stale-version access accurately; do not confuse it with an uninstalled skill
   or claim that the new instructions have been loaded.
4. Distinguish an unreadable entry point from an unreadable task reference. Name the part
   that failed, and do not declare the entire skill unavailable because one reference
   failed. Complete work supported by the material actually read, explicitly identifying
   any affected portion. Never claim to have followed an unread workflow.

These recovery rules guide callers that can see this entry or its metadata. They do not
install tools, force host-side skill discovery, or repair a host service outage.

## ARS text shortcuts

Treat a shortcut at the beginning of a request as an explicit mode. A skill selector may
precede it. Accept both ars-abstract and /ars-abstract when the host passes the text through.
These are prompt shortcuts, not newly registered application commands. Ignore shortcuts
quoted inside a paper, code, or an example. If slash input is intercepted, use plain ars-*.

| Shortcut | Route |
|---|---|
| ars-plan / ars-outline | Writing: argument plan / outline |
| ars-abstract | Writing: abstract only; evaluate first only if requested |
| ars-lit-review | Research: literature synthesis using supplied corpus or authorized search |
| ars-3w | Research: WHY/HOW/WHAT comparison as defined in the Research reference |
| ars-reviewer | Review: scope to the supplied abstract, sections or full paper |
| ars-revision-coach | Review: actionable revision plan |
| ars-revision | Writing/review: implement requested or approved revisions |
| ars-rebuttal-audit | Review: audit existing responses against comments and actual changes |
| ars-citation-check | Evidence: identity, cited version, claim support and formatting |
| ars-disclosure | Writing: truthful disclosure of actual assistance |
| ars-format-convert | Writing: native artifact workflow for the requested format |
| ars-mark-read / ars-unmark-read | Evidence: record or retract an author reading declaration |
| ars-cache-invalidate | Evidence: retire a specified evidence entry |
| ars-full | Pipeline: start at the earliest missing stage and reuse completed work |

Keep an explicitly selected mode even when usual inputs are absent. A revision request
without reviewer comments is still revision. Do available work and request only indispensable
missing inputs; do not redirect it into an automatic Socratic interview.
