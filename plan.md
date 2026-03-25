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

Phase 2: Rough-In (all work inside wall cavities — must be done before plywood covers studs)
  ├── 2A. Electrical rough-in [REQUIRES: electrical permit pulled]
  │     ├── Install new subpanel (flush-mount between studs on target wall)
  │     │     Feed from main panel (175A main, 100A feeder, 1 AWG copper)
  │     ├── Run 240V/50A circuit — EV charger (NEMA 14-50)
  │     ├── Run 240V circuit — dryer
  │     ├── Run 120V circuit — washer
  │     └── Run 120V circuits — workshop power tools, dust collection, general
  ├── 2B. Plumbing rough-in [REQUIRES: plumbing permit pulled]
  │     ├── Reroute washer supply lines (currently external to wall)
  │     ├── Install washer box (recessed outlet box with valves + drain)
  │     └── Remove/cap old garage sink connections if no longer needed
  └── 2C. Gray water rough-in [REQUIRES: gray water permit pulled]
        ├── Tap into bath drain (accessible from garage ceiling/wall)
        ├── Tap into washer drain
        └── Route gray water lines to collection/irrigation
  Note: 2A, 2B, 2C are independent — can be done in parallel or any order.

Phase 3: Inspections (before anything covers the stud bays)
  ├── Electrical rough-in inspection
  ├── Plumbing rough-in inspection
  ├── Gray water inspection
  └── All must PASS before Phase 4

Phase 4: Insulation + Seismic Plywood
  ├── Insulate target wall (after inspections pass)
  ├── Finish ceiling insulation (currently ~90% done)
  └── Seismic plywood on target wall (interior face of studs)
      └── Covers all rough-in — goes on AFTER inspections, BEFORE drywall

Phase 5: Close Walls
  ├── Drywall ceiling
  └── Drywall over seismic plywood on target wall
      └── BLOCKED until Phase 4 complete
```

---

## Task Status

| # | Task | Status | Permit Needed | Notes |
|---|------|--------|---------------|-------|
| 1 | New subpanel (100A feeder, 100A bus) | Not started | Electrical | Flush-mount between studs; HOM2100 breaker, 1 AWG copper; **PRIORITY** |
| 2a | 240V/50A — EV charger | Not started | Electrical | NEMA 14-50; depends on subpanel; **PRIORITY** |
| 2b | 240V — dryer | Not started | Electrical | Depends on subpanel |
| 2c | 120V — washer | Not started | Electrical | Depends on subpanel |
| 2d | 120V — workshop + general outlets | Not started | Electrical | 3 circuits: power tools, dust collection, general+garage door |
| 3 | Washer plumbing reroute | Not started | Plumbing | Move from external/sink to in-wall washer box |
| 4a | Gray water — bath | Not started | Gray water | Accessible from garage ceiling |
| 4b | Gray water — washer | Not started | Gray water | |
| 5 | Ceiling insulation | 90% complete | Probably not | Finish remaining 10% |
| 6 | Seismic plywood | Not started | Check locally | Interior face of studs; AFTER all rough-in inspections pass, BEFORE drywall |
| 7a | Drywall — ceiling | Not started | No | After plywood |
| 7b | Drywall — walls | Not started | No | Over seismic plywood; half currently done with tile |

---

## Permits Tracker

| Permit | Status | Applied | Approved | Inspection Scheduled | Inspection Passed |
|--------|--------|---------|----------|---------------------|-------------------|
| Electrical | **APPROVED** | 2026-03-25 | 2026-03-25 | — | — |
| Plumbing | Not applied | — | — | — | — |
| Gray water | Not applied | — | — | — | — |
| Building (seismic) | Needs plan | 2026-03-25 (asked) | — | — | — |

---

## Jurisdiction

San Francisco, CA — permits through SF Department of Building Inspection (SFDBI). See `notes/jurisdiction.md` for details.

## Open Questions

- [x] ~~Does seismic plywood require a building permit?~~ — YES, but OTC eligible at DBI. See `decisions/permits-needed-summary.md`
- [x] ~~Gray water: what's the intended destination?~~ — Subsurface landscape irrigation
- [x] ~~Why was main panel downgraded from 200A to 175A?~~ — NEC 120% rule for solar backfeed (175+60=235 ≤ 240). See `decisions/main-panel-capacity.md`
- [x] ~~Can available capacity support subpanel feed?~~ — Yes, 163A calculated on 175A service. See `permits/electrical-load-calc.md`
- [x] ~~Electrician as supervisor model?~~ — Homeowner pulls permit, does work, friend advises informally. See `decisions/electrical-homeowner-diy-legal.md`
- [ ] Dryer: gas or electric? (currently gas, planning electric — calc includes future electric)
- [ ] Do you need to keep the garage sink, or is it being removed?
- [ ] Existing wall tile on the other half — are you keeping it, or will that wall eventually get renovated too?

---

## Materials & Budget

_To be filled in as research progresses._

---

## Notes

- Washer "receptacle" = likely a washer outlet box (e.g., Oatey or Sioux Chief) with hot/cold valves and a drain standpipe built into the wall.
- Gray water from bath and washer is typically "light" gray water and easier to permit than kitchen/dishwasher gray water.
- EV charger 240V circuit is typically 50A for a NEMA 14-50 outlet (or hardwired, depending on charger).
