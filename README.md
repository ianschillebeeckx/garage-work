# Garage Renovation

Project management and technical reference for a garage renovation on the east wall of a residential home in San Francisco.

## Goals

1. **Use AI to help me do electrical work in my garage** (and pass inspection)
2. **Practice building and validating RAG** with new technologies

The main interface is the terminal via [Claude Code](https://claude.ai/code) — all research, planning, code lookups, and project tracking happen through the agentic loop.

## Project Scope

- **100A subpanel** fed from main panel (2/0 AL SER feeder)
- **EV charger circuit** (50A/240V, NEMA 14-50)
- **Dryer circuit** (30A/240V, NEMA 14-30)
- **5x 120V general-purpose circuits** (washer, laundry, workshop, general)
- **Plumbing** — washer/dryer hookups, gray water diversion, exterior hot water hose bib
- **Seismic plywood sheathing** on east wall
- **Fire-rated drywall** (5/8" Type X) — east wall (4ft to property line) and ceiling (habitable space above)
- All work owner-performed under homeowner permits (SF DBI)

## Repo Structure

```
plan.md              Master project plan, phases, dependencies, status
permits/             Permit tracking and checklists (electrical, plumbing, building)
decisions/           Sourced decision records with code citations
notes/               Research, shopping lists, vendor info
photos/              Site photos, nameplates, panel photos
nec_vectordb/        NEC code reference — vector database + query CLI
private/             Gitignored — filled-in permit forms, personal info
```

## NEC Vector Database

A searchable vector database built from the *Illustrated Guide to the National Electrical Code, 6th Edition*. Used for code lookups during the project.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Ingest (run once, requires the PDF in `nec_vectordb/`)

```bash
python3 nec_vectordb/ingest.py
```

### Query

```bash
python3 nec_vectordb/query.py "GFCI requirements for garage receptacles"
python3 nec_vectordb/query.py "conductor ampacity 75 degrees" --top 10
```

### Validation

```bash
python3 nec_vectordb/test.py                    # golden queries + content checks
python3 nec_vectordb/test_extraction.py          # PDF text extraction spot checks
```

## Claude Code Integration

- **`/lookup`** — Skill that queries the NEC vector database (6 parallel reformulations) and supplements with web search. Results are tiered by source confidence.
- **`CLAUDE.md`** — Project instructions for Claude Code, including traceability requirements and structure guidance.

## Jurisdiction

- **City:** San Francisco, CA
- **Property:** Block 3005 / Lot 006, RH-1(D) zoning
- **Permits through:** SF Department of Building Inspection (DBI), 49 South Van Ness Ave
- **Code basis:** California Electrical Code (CEC), California Residential Code (CRC), based on NEC/IRC with state amendments
