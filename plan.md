# Garage Renovation — Master Plan

## Overview

Renovate one wall of garage: structural, electrical, plumbing, gray water, insulation, and drywall. Work is sequenced so all rough-in happens before walls are closed.

---

## Phases & Dependencies

```
Phase 1: Permits & Planning
  ├── Electrical permit (subpanel + circuits)
  ├── Plumbing permit (washer hookup reroute)
  ├── Gray water permit (bath + washer diversion)
  └── Building permit (seismic plywood — check if required locally)

Phase 2: Rough-In (all behind-wall work, before drywall)
  ├── 2A. Seismic plywood on target wall
  │     └── No dependency on permits in most jurisdictions, but confirm
  ├── 2B. Electrical rough-in [REQUIRES: electrical permit pulled]
  │     ├── Install new subpanel (flush-mount between studs on target wall)
  │     │     Feed from main panel (175A, downgraded from 200A — investigate)
  │     ├── Run 240V/50A circuit — EV charger (NEMA 14-50)
  │     ├── Run 240V circuit — dryer
  │     ├── Run 120V circuit — washer
  │     └── Run 120V circuits — general outlets
  ├── 2C. Plumbing rough-in [REQUIRES: plumbing permit pulled]
  │     ├── Reroute washer supply lines (currently external to wall)
  │     ├── Install washer box (recessed outlet box with valves + drain)
  │     └── Remove/cap old garage sink connections if no longer needed
  └── 2D. Gray water rough-in [REQUIRES: gray water permit pulled]
        ├── Tap into bath drain (accessible from garage ceiling/wall)
        ├── Tap into washer drain
        └── Route gray water lines to collection/irrigation

Phase 3: Insulation
  ├── Finish ceiling insulation (currently ~90% done)
  └── Insulate target wall if not already done
      └── Must happen AFTER all rough-in is complete and inspected

Phase 4: Inspections
  ├── Electrical rough-in inspection
  ├── Plumbing rough-in inspection
  ├── Gray water inspection
  └── Insulation inspection (if required locally)

Phase 5: Close Walls
  ├── Drywall ceiling
  └── Drywall target wall
      └── BLOCKED until all Phase 4 inspections pass
```

---

## Task Status

| # | Task | Status | Permit Needed | Notes |
|---|------|--------|---------------|-------|
| 1 | Seismic plywood | Not started | Check locally | One wall only |
| 2 | New subpanel | Not started | Electrical | Flush-mount between studs; feed from 175A main (was 200A — why?) |
| 3a | 240V/50A — EV charger | Not started | Electrical | NEMA 14-50; depends on subpanel; **PRIORITY** |
| 3b | 240V — dryer | Not started | Electrical | Depends on subpanel |
| 3c | 120V — washer | Not started | Electrical | Depends on subpanel |
| 3d | 120V — general outlets | Not started | Electrical | Depends on subpanel |
| 4 | Washer plumbing reroute | Not started | Plumbing | Move from external/sink to in-wall washer box |
| 5a | Gray water — bath | Not started | Gray water | Accessible from garage ceiling |
| 5b | Gray water — washer | Not started | Gray water | |
| 6 | Ceiling insulation | 90% complete | Probably not | Finish remaining 10% |
| 7a | Drywall — ceiling | Not started | No | After all inspections |
| 7b | Drywall — walls | Not started | No | After all inspections; half currently done with tile |

---

## Permits Tracker

| Permit | Status | Applied | Approved | Inspection Scheduled | Inspection Passed |
|--------|--------|---------|----------|---------------------|-------------------|
| Electrical | Not applied | — | — | — | — |
| Plumbing | Not applied | — | — | — | — |
| Gray water | Not applied | — | — | — | — |
| Building (seismic) | TBD if needed | — | — | — | — |

---

## Jurisdiction

San Francisco, CA — permits through SF Department of Building Inspection (SFDBI). See `notes/jurisdiction.md` for details.

## Open Questions

- [ ] Does seismic plywood require a building permit in your jurisdiction?
- [ ] Gray water: what's the intended destination? (irrigation, holding tank, etc.)
- [ ] Dryer: gas or electric? (affects whether dryer needs 240V or just 120V + gas line)
- [ ] Do you need to keep the garage sink, or is it being removed?
- [ ] Why was main panel downgraded from 200A to 175A during PV+battery install? (affects subpanel sizing)
- [ ] Can available capacity support a 60A subpanel feed given PV+battery+existing loads?
- [ ] Explore "electrician as supervisor" model — will SF DBI allow homeowner to do work under informal supervision, or does the permit need to be under a licensed contractor?
- [ ] Existing wall tile on the other half — are you keeping it, or will that wall eventually get renovated too?

---

## Materials & Budget

_To be filled in as research progresses._

---

## Notes

- Washer "receptacle" = likely a washer outlet box (e.g., Oatey or Sioux Chief) with hot/cold valves and a drain standpipe built into the wall.
- Gray water from bath and washer is typically "light" gray water and easier to permit than kitchen/dishwasher gray water.
- EV charger 240V circuit is typically 50A for a NEMA 14-50 outlet (or hardwired, depending on charger).
