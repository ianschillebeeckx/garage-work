# Decision: Garage Subpanel Placement

**Date:** 2026-03-16
**Status:** Pending — gas meter clearance needs verification

## Layout

```
              NORTH (garage door, street side)
    ┌──────────┬───────────────────────────────────┐
    │          │                                   │
    │ Living   │  GARAGE (east half, 1st floor)    │
    │ space    │  Long & slender, runs N/S         │
    │ (west    │                                   │
    │ half)    │  Main Panel ← exterior, Type 3R   │
    │          │  Gas Meter (inside, near main)    │
    │ 5/8" gyp │                                   │
    │ fire-    │  ⇧ proposed new subpanel here     │
    │ sealed   │                                   │
    │ wall ⇨   │                                   │
    │          │                                   │
    │          │                                   │
    │          │                                   │
    │          │                                   │
    │          ├───────────────────────────────────┤
    │          │   Door to outside (south side)    │
    └──────────┴───────────────────────────────────┘
              SOUTH (door)

    West (living space) ← → East (target wall, unfinished)
    Ceiling above garage: 2nd floor living space (unfinished)
```

## Walls / Surfaces Summary

| Surface | Faces | Status | What's on the other side |
|---------|-------|--------|--------------------------|
| **East wall** (target wall) | Outside | Unfinished — adding subpanel + circuits | Property line ~4 ft away, neighbor's house ~8 ft away |
| **West wall** | Living space | 5/8" gypsum, fire-sealed (existing) | Living space (1st floor) |
| **North wall** | Outside | — | Garage door, street |
| **South wall** | Outside | — | Door to outside |
| **Ceiling** | Up | Unfinished | 2nd floor living space (habitable) |

## Proposed Placement

New garage subpanel on the **east (target) wall**, inside the garage. Located between the existing main panel and existing house subpanel.

**Feeder run:** Main panel (exterior, on east wall) → through wall → new subpanel (interior, east wall). Estimated ~6-10 feet horizontal run through bored studs. At this distance, voltage drop is negligible for 100A.

## EV Charger Placement

Near garage door (north side) so charging cable can reach a car parked inside OR outside on the driveway. Chevy Bolt currently parks inside nightly.

## Gas Meter Clearance — RESOLVED

**The gas meter is inside the garage** with a window to the outside and a shutoff valve. The proposed subpanel location is ~8ft from the gas meter. This is well clear of all applicable requirements.

### PG&E Clearance Requirements (source: PG&E utility standards)

| Requirement | Distance | Source |
|-------------|----------|--------|
| Horizontal clearance from gas meter set | 12 inches minimum on either side | PG&E TD-7001M-B011 |
| Radial clearance from gas regulator vent | 36 inches (3 ft) | PG&E gas meter standards |
| Vertical clearance above regulator vent | 10 feet | PG&E gas meter standards |

**Sources:**
- PG&E Utility Bulletin TD-7001M-B011: https://www.pge.com/assets/pge/docs/account/service-requests/TD-7001M-B011.pdf
- PG&E Gas Meter Locations Standard J-15: https://www.pge.com/assets/pge/docs/account/service-requests/j-15.pdf
- PG&E Electric/Gas Meter Separation Figure: https://wrightresidential.com/wp-content/uploads/2018/12/PGE-Gas-Service-Clearances.pdf

**At ~8ft away, the new subpanel exceeds all clearance requirements by a wide margin.** Even 1 stud bay (~14.5") from the gas meter would clear the 12" horizontal minimum, though the 36" regulator vent radius could be a concern if the subpanel were that close. At 8ft, this is a non-issue.

## Main Panel Info

- **Brand:** Square D
- **Cat. No:** SO2040M200S, Series M01
- **Type:** Homeline "All-In-One" Combination Service Entrance
- **Spaces:** 20 spaces / 40 circuits
- **Open slots:** ~14 after relocating garage circuit
- **Feeder breaker needed:** **Square D HOM2100** (Homeline 100A 2-pole)
  - Confirmed Homeline series (SO prefix = Homeline All-In-One)
  - Do NOT use QO breakers in this panel

## Wire Sizing

For 100A feeder at ~8-10 ft run (through wall from exterior main to interior subpanel):
- **1 AWG copper** — rated 130A (NEC 310.16, 75°C column). Sufficient.
- **2/0 aluminum** — alternative, cheaper for longer runs but unnecessary at this distance
- Need 4 conductors: 2 hots + 1 neutral + 1 ground (subpanel requires separate neutral and ground bars)
- At this short distance, voltage drop is negligible (<0.5%)

## Open Questions

- [x] ~~Confirm Square D series~~ — Homeline (SO2040M200S). Feeder breaker: HOM2100.
- [ ] EV charger exact location — how far from subpanel? (affects circuit wire length)
- [x] ~~Gas meter clearance~~ — 8ft away, well exceeds all PG&E/code minimums
- [x] ~~Main panel brand~~ — Square D
