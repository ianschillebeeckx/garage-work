# Decision: 100A Feeder, Move AC to Garage Subpanel

**Date:** 2026-03-23
**Supersedes:** Previous 60A→80A feeder decisions in `main-panel-capacity.md` and `subpanel-placement.md`

## Decision

Upsize garage subpanel feeder from 80A to 100A and move the HVAC condenser circuit from the main panel to the garage subpanel.

## Motivation: Future DIY Battery Storage

The long-term plan is to add DIY battery storage (self-contained inverter + transfer switch) for the garage subpanel. The subpanel would become a "backed up" panel — loads on it would be powered by battery during grid outages.

Moving the AC onto this subpanel means it can be battery-backed in the future. The more critical loads consolidated on this panel, the more useful the battery backup becomes.

This may require rewiring between the main service panel and the garage subpanel when the transfer switch is added, but that's acceptable.

## Why 100A Over 80A

With AC added to the garage subpanel, worst-case simultaneous loads:
- EV charger: 40A continuous
- AC condenser: 24A (nameplate)
- Dryer: 24A
- Misc (washer, workshop, general): 10-15A
- **Total: ~98-103A**

An 80A feeder would trip under EV + dryer + AC (88A > 80A). A 100A feeder handles all loads simultaneously without relying on Emporia load management.

## Changes

| Item | Was | Now |
|------|-----|-----|
| Feeder breaker | HOM280 (80A 2-pole) | HOM2100 (100A 2-pole) |
| Feeder wire | 4 AWG copper | 1 AWG copper or 2/0 aluminum |
| AC condenser circuit | Main panel, 50A 2-pole | Garage subpanel, 50A 2-pole |
| Subpanel bus | 100A (unchanged) | 100A (unchanged) |
| Total service load calc | 163A on 175A (unchanged) | 163A on 175A (unchanged) |

## AC Wiring Note

The existing AC wire already runs through the garage to reach the main panel. Moving the circuit to the garage subpanel shortens the run — the existing wire can likely be reused by cutting and re-terminating at the subpanel.

## Future Battery Storage Notes

- Transfer switch would go between the main panel feeder and the garage subpanel
- Inverter/battery would connect to the subpanel (load side of transfer switch)
- Grid power flows: Main panel → transfer switch → subpanel
- Battery power flows: Battery → inverter → transfer switch → subpanel
- Existing Powerwall 3 on main panel is separate — this would be a second, independent battery system for the garage/backed-up loads
