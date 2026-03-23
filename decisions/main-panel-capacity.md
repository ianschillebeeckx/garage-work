# Decision: Main Panel Capacity Analysis

**Date:** 2026-03-16
**Applies to:** Subpanel sizing, EV charger feasibility

## Panel Label Data (as read by homeowner)

- **Enclosure:** Rainproof Type 3R
- **Mains:** 200A max
- **Bus rating:** 200A max
- **Current main breaker:** 175A (downgraded from 200A during PV+battery install)

## Existing Breakers

| Breaker | Poles | Amps | Purpose |
|---------|-------|------|---------|
| Main | 2 | 175A | Main disconnect |
| CB1 | 2 | 100A | Existing house subpanel |
| CB2 | 2 | 50A | Air conditioning |
| CB3 | 2 | 60A | Powerwall 3 battery/inverter (solar backfeed) |
| CB4 | 1 | 20A | Garage plug + garage door (plan to relocate to new subpanel) |

## Why Main Was Downgraded: NEC 120% Rule

**Source:** NEC 705.12(B)(2)(3) / CEC 705.12 — bus bar rating rule for solar backfeed

The Powerwall 3's 60A breaker is a **backfeed** breaker (it pushes power INTO the panel from solar/battery). The 120% rule says:

> Main breaker + solar backfeed breaker ≤ bus bar rating × 1.20

**With original 200A main:**
200A + 60A = 260A > 240A (200 × 1.2) — **VIOLATION**

**With downgraded 175A main:**
175A + 60A = 235A ≤ 240A (200 × 1.2) — **COMPLIANT** (5A margin)

This confirms why the installer downgraded to 175A. It was required by code, not optional.

## Available Capacity for New Subpanel

The 120% rule only applies to backfeed (source) breakers, not load breakers. A new subpanel feed is a **load**, so the 120% rule does not limit it.

The real constraint is:
1. **Physical space** — are there open breaker slots in the main panel?
2. **Actual load calculation** — does total calculated load (NEC Article 220) fit under 175A?

### Breaker space — Main Panel

Current usage: 100A(2-pole) + 60A(2-pole) + 20A(1-pole) = 5 pole positions (50A HVAC breaker being relocated to garage subpanel).
**Open slots in main panel: 15 (16 after relocating 20A garage circuit and removing HVAC breaker)**
**No space constraint.** Plenty of room for a 2-pole feeder breaker.

### Breaker space — Existing House Subpanel (100A)

Only 2 open slots. Not relevant to this project (garage gets its own new subpanel off the main), but noted for reference. This is why the garage subpanel feeds from the main, not from the existing house sub.

### Load calculation (rough estimate, needs formal calc for permit)

Breaker ratings ≠ actual load. A 100A subpanel breaker doesn't mean the house draws 100A. Actual load is calculated per NEC Article 220 using:
- Square footage (general lighting/receptacle load)
- Fixed appliances
- AC
- Largest motor

**TODO: perform formal NEC Article 220 load calculation for permit application.**

### Subpanel sizing considerations

**Energy management ecosystem:**
- **Emporia EV charger** — controllable, can throttle based on available capacity
- **Emporia home energy monitor** — 16 circuits monitored (AC, water heater, microwave, fridge, etc.)
- **Powerwall 3** — battery/inverter with solar
- **Owner's intent:** charge EV only on surplus solar (after battery full + house load met)

This means the EV charger will rarely draw its full 40A continuous alongside other heavy loads. The Emporia system provides real-time load visibility and charger control.

**Planned garage subpanel loads:**
- 240V/50A HVAC condenser (relocated from main panel) — 24A typical
- 240V/50A EV charger (NEMA 14-50) — 40A continuous max, but software-throttled via Emporia
- 240V/30A dryer — ~24A typical
- 120V/20A washer — ~12A typical
- 120V/20A general outlets — ~5-10A typical
- 20A garage plug + door (relocated from main) — ~5A typical

**Worst case simultaneous (no load management):** ~110A (but limited by 100A feeder breaker)
**Realistic with Emporia load management:** EV throttles down when dryer/other loads are active. Typical simultaneous draw: 50-65A.

### Recommendation: 100A feeder, 100A bus subpanel

- **100A 2-pole feeder breaker** in the main panel — fits the available capacity and keeps total load well within 175A main
- **100A bus subpanel** — gives room for all planned breakers and future flexibility inside the garage
- The HVAC condenser circuit (50A 2-pole) is being relocated from the main panel to this subpanel, so the feeder must support the AC load in addition to EV + dryer

**Why 100A over 80A:** With the AC condenser relocated to the garage subpanel, the worst-case simultaneous load (HVAC 24A + EV charger 40A + dryer 24A = 88A) exceeds an 80A feeder. A 100A feeder provides headroom without relying solely on Emporia load management. The Emporia system still provides additional safety margin and optimizes real-world usage, but the feeder is sized to handle the three largest loads simultaneously even without load management.

**Wire sizing for 100A feeder:** 1 AWG copper (NEC 310.16, 75°C column, rated 130A). Alternative: 2/0 aluminum. **TODO: measure run length — if over ~50ft, may need to upsize for voltage drop.**

## Open Questions

- [ ] Formal NEC 220 load calculation needed for permit
- [ ] Measure feeder run distance (main panel to garage subpanel location) for voltage drop calc (1 AWG copper or 2/0 aluminum)
- [ ] Confirm main panel brand/model — new feeder breaker must be compatible
- [x] ~~How many open breaker slots remain in main panel?~~ — 13 open (14 after garage circuit moves). No space issue.
- [x] ~~Smart EV charger with load management?~~ — Yes, Emporia charger + 16-circuit monitor already in place
