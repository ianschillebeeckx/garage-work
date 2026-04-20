# Decision: Drywall Requirements by Wall/Ceiling

**Date:** 2026-03-25
**Updated:** 2026-04-09 — corrected cardinal directions; added CRC R302.1 fire-rated exterior wall analysis
**Source:** California Residential Code R302.6 and R302.1
**URLs:**
- https://up.codes/s/dwelling-garage-and-or-carport-fire-separation
- https://up.codes/viewer/california/ca-residential-code-2022/chapter/3/building-planning

## Code 1: CRC R302.6 — Dwelling-Garage Fire Separation

Applies where the garage adjoins living space.

Table R302.6 specifies:

| Separation | Required Material |
|---|---|
| Garage from residence and attics | Min. 1/2" gypsum board, applied to garage side |
| Habitable rooms above garage/carport | Min. 5/8" Type X gypsum board |
| Structural supports for floor/ceiling assemblies used for separation | Min. 1/2" gypsum board |
| Garage within 3ft of other dwelling on same lot | Min. 1/2" gypsum board on interior side of exterior walls |

## Code 2: CRC R302.1 — Exterior Wall Fire Resistance Near Property Line

Separate rule that applies to **any** exterior wall (not just garages) based on distance to the property line. The threshold is typically **5 feet** — walls closer than 5 ft to a property line require fire-resistance rating.

## Application to This Garage

The garage is on the east half of the 1st floor. It runs north–south, with:
- **East wall** (target wall) — exterior, ~4 ft from property line, neighbor's house ~8 ft beyond
- **West wall** — separates garage from 1st-floor living space (already drywalled, fire-sealed)
- **North wall** — exterior, garage door, street side
- **South wall** — exterior, door to outside
- **Ceiling** — 2nd-floor living space above

| Surface | Adjacent to | Rule that applies | Drywall required? | Spec |
|---------|-------------|-------------------|-------------------|------|
| **Ceiling** | 2nd floor living space | R302.6 (habitable rooms above) | **YES** | 5/8" Type X gypsum board |
| **West wall** | 1st floor living space | R302.6 (residence) | **YES — already done** | 5/8" gypsum, fire-sealed (existing) |
| **East wall (target)** | Exterior, **exactly 4 ft to property line** | **R302.1** — confirmed | **YES** | 1-hour fire-rated assembly. Interior side: 5/8" Type X gypsum board. Wall is currently unfinished (no existing fire rating). |
| **North wall** | Exterior, street | None (assuming >5 ft to property line) | NO | Confirm distance to PL |
| **South wall** | Exterior, door | None (assuming >5 ft to property line) | NO | Confirm distance to PL |

## Key Finding — CONFIRMED

**The east (target) wall is exactly 4 feet from the property line and is currently unfinished (no existing fire rating).** Under CRC R302.1, exterior walls within 5 ft of a property line in a non-sprinklered dwelling require **1-hour fire-resistance-rated construction**.

This means the east wall **must be built up to a 1-hour fire-rated assembly** before being closed in. The interior side requires **5/8" Type X gypsum board** as part of that assembly.

**Reduced setback for sprinklered homes:** If the home had an automatic sprinkler system per R313, the threshold drops to 3 ft. This home is not sprinklered, so the 5 ft threshold applies.

## Outlet Boxes in the Fire-Rated East Wall

Per **NEC 300.21** and the listing requirements for the fire-rated assembly:

- **Same-side boxes (your case):** No NEC minimum spacing rule between adjacent boxes on the interior (garage) side. The 14-50 box and any 120V duplex boxes can be installed in the same stud bay.
- **Box openings:** Each individual outlet box opening must not exceed 16 sq in unless tested otherwise. Total openings on either side of the wall in any 100 sq ft area must not exceed 100 sq in.
- **Use fire-rated putty pads** on the back of every box on the east wall (e.g., 3M MPP+, Specified Technologies). ~$5 each. Maintains the fire rating regardless of box construction.
- **Back-to-back boxes** (boxes directly behind each other on opposite sides of a fire-rated wall) require a **24" horizontal separation** per NEC 300.21 informational note. Not applicable here since the exterior side has no boxes.
- Use boxes **listed for use in fire-rated assemblies**, or apply putty pads.

## What This Means for the Project — REVISED

- **East wall (target):** **Plywood alone is NOT sufficient.** Wall assembly must be 1-hour fire-rated. Plan:
  1. Run electrical rough-in (current work)
  2. Install fire-rated putty pads on every outlet box on the east wall
  3. Install plywood sheathing (for seismic permit / shear wall purposes) — directly on studs
  4. Install **5/8" Type X gypsum board** over the plywood as the interior finish
  5. Tape and finish gypsum joints
- **Ceiling:** Must install 5/8" Type X drywall (already in plan, Phase 5).
- **West wall:** Already drywalled and fire-sealed.
- **North wall, south wall:** Confirm distance to property line. If >5 ft, no fire rating required.

## Sources

- CRC R302.1 — Exterior wall fire-resistance requirements: https://up.codes/viewer/california/ca-residential-code-2022/chapter/3/building-planning
- Humboldt County summary of CRC R302: https://humboldtgov.org/3434/Fire-Resistant-Construction-CRC-R302
- Carmel CA fire-resistive construction memo (R-3 walls): https://ci.carmel.ca.us/sites/main/files/file-attachments/sog_18-02_fire_resistive_construction_0.pdf
- NEC 300.21 (boxes in fire-rated walls) — referenced in NEC guide p.50

## Note on R302.6 (3ft rule)

The R302.6 "garage within 3ft of other dwelling on same lot" row does NOT apply here. That rule is about another dwelling on the **same lot** (e.g., an ADU). The neighbor's house is on a different lot, so R302.6 doesn't trigger. But R302.1 (property line proximity) is a separate rule that DOES apply.
