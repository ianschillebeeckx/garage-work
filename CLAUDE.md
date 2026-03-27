# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo serves two goals:

1. **Project management for a garage renovation** — notetaking, tracking dependencies, plans, permitting, and progress for home improvement work on one wall of a residential garage.
2. **Learning platform** — getting hands-on exposure to Claude Code, Claude skills, RAG (retrieval-augmented generation), and other agentic technologies.

## Key Constraints

- Owner-occupied, owner-performed work (homeowner in SF single-family dwelling)
- Homeowner can legally perform all electrical work including subpanel (see `decisions/` for sourcing)
- All electrical and plumbing rough-in must pass inspection before drywall closes walls
- Gray water systems have jurisdiction-specific rules (CA CPC Chapter 15)

## Traceability Requirement

**Every decision, code interpretation, or regulatory finding must be traceable to a source document.** When recording a finding:
- Cite the specific code section, statute, or official document (e.g., "CA B&P Code § 7044", "SF Electrical Code § 89.120(E)")
- Include a URL or document reference where possible
- Record the date the finding was made (information can go stale)
- Store findings in `decisions/` as individual files

This applies to permitting requirements, code interpretations, material choices, and any other decision where "why did we decide this?" might come up later.

## Structure

- `plan.md` — Master project plan with phases, dependencies, and current status
- `permits/` — Permit tracking, requirements, and checklists per trade
- `decisions/` — Sourced findings and decision records with citations
- `notes/` — Research, vendor quotes, material lists
- `photos/` — Nameplate photos, panel photos, site photos
- `private/` — **Gitignored.** Filled-in documents with personal info (address, etc.) for printing/submission. Never committed.

## How to Help

- When updating tasks, preserve dependency ordering — drywall is always last
- Permit status matters: don't suggest starting rough-in work before permits are pulled
- Track what needs inspection vs. what doesn't
- **Always cite sources** when recording regulatory or code findings — never state a code requirement without a reference
