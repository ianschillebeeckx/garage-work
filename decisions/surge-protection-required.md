# Decision: Surge Protection Required for 2nd Subpanel

**Date:** 2026-03-25
**Source:** SF DBI electrical inspector at permit counter (verbal, during permit issuance)
**Updated:** 2026-03-27 with code citations

## Finding

The DBI electrical inspector stated that since this is a **2nd subpanel** being added to the service, surge protection is required.

## Code Basis

Two NEC sections apply:

### NEC 230.67 — Surge Protection (at service)

> All services supplying dwelling units shall be provided with a surge-protective device (SPD).

- Introduced in the **2020 NEC**
- Requires a **Type 1 or Type 2 SPD** at the service equipment (main panel)
- The SPD must be integral to the service equipment or immediately adjacent
- Source: https://www.electricallicenserenewal.com/Electrical-Continuing-Education-Courses/NEC-Content.php?sectionID=843.0

### NEC 215.18 — Surge Protection (at feeders) — 2023 NEC

> Where a feeder supplies a dwelling unit, a surge-protective device (SPD) shall be installed.

- **This is the section that applies to the new subpanel.** The subpanel is fed by a feeder from the main panel.
- The SPD must be installed **in or adjacent to the distribution equipment** (i.e., in the subpanel itself)
- Must be a **Type 1 or Type 2 SPD**
- Must have a **nominal discharge current rating (In) of not less than 10kA**
- Source: https://www.electricallicenserenewal.com/Electrical-Continuing-Education-Courses/NEC-Content.php?sectionID=1440

### Not in the NEC Guide

The Illustrated Guide to the NEC (6th Edition) predates these requirements — NEC 230.67 was added in the 2020 cycle, and NEC 215.18 in 2023. No results found in the vector database for surge protection requirements.

## Resolution

- [x] Confirm exact code section: **NEC 215.18** for feeder-supplied subpanels, **NEC 230.67** for service
- [x] SPD goes in the **new subpanel** (per 215.18 — at the distribution equipment fed by the feeder)
- [x] Compatible SPD: **Siemens QSPD2A035B** (Type 1, 35kA, plug-in, fits SN series panel) — purchased
- [x] Added to shopping list

## Installed SPD

**Siemens QSPD2A035B** — BoltShield 35kA, 2-pole, Type 1 (also suitable for Type 2 use)
- Plugs into 2 breaker slots in the Siemens SN2448L1125 subpanel
- 35kA surge current rating (exceeds the 10kA minimum in NEC 215.18(E))
- No LED indicator (base model)
