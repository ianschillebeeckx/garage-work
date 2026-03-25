# Shopping List — Garage Subpanel Installation

## Subpanel

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Siemens SN2448L1125 — 125A main lug, 24-space/48-circuit, plug-on neutral, indoor | SN2448L1125 | 1 | To match existing house subpanel (also Siemens). 125A bus handles the 100A feeder. Main lug is correct — the HOM2100 in the main panel serves as the disconnect. Plug-on neutral makes GFCI breaker install cleaner. |

## Feeder (Main Panel → Subpanel, ~15ft horizontal run through wall)

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Feeder breaker (main panel) | Square D HOM2100 — Homeline 100A 2-pole | 1 | Goes in main panel to feed the subpanel |
| Anti-oxidant compound | Burndy Penetrox or equivalent | 1 tube | Required for aluminum terminations, good practice for copper too. |

### Option A: Aluminum SER cable (RECOMMENDED)

Matches existing house subpanel feeder (Southwire Alumaflex). No conduit needed — runs through bored stud holes like Romex. Cheaper, lighter, and simpler than copper THHN in conduit.

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| 2/0-2/0-2/0-1 aluminum SER cable | Southwire Alumaflex or equivalent | ~20 ft | 3× 2/0 AWG (2 hots + neutral) + 1× 1 AWG ground. 100A rated. Buy by the foot at Home Depot — search "2/0 SER aluminum" or ask at wire cutting counter for "two-ought SER." OD ~1.2-1.3", fits through 2.2" max bore in 2×6 studs. |

### Option B: Copper THHN in conduit (alternative)

More expensive, requires conduit, but avoids aluminum termination concerns.

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| 1 AWG copper THHN/THWN — black | Stranded, 1 AWG | ~20 ft | Hot leg 1. Buy extra for termination slack. |
| 1 AWG copper THHN/THWN — red | Stranded, 1 AWG | ~20 ft | Hot leg 2. If red unavailable, use black + red tape at ends. |
| 1 AWG copper THHN/THWN — white | Stranded, 1 AWG | ~20 ft | Neutral. If unavailable, use black + white tape at ends. |
| 1 AWG copper THHN/THWN — green (or bare) | Stranded, 1 AWG | ~20 ft | Ground. |
| Conduit — 1.5" EMT or flexible LFNC | | ~15 ft | Threading rigid conduit through stud bores is difficult. Flexible LFNC (liquidtight) is easier but 1.25-1.5" is tight in 2.2" bore holes. |
| Conduit fittings | Connectors, couplings, straps | As needed | |

## Subpanel Breakers

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| 50A 2-pole | Siemens Q250 | 1 | HVAC condenser (relocated from main panel). Hardwired equipment — GFCI not required. |
| 50A 2-pole GFCI | Siemens QF250A | 1 | EV charger — NEMA 14-50. GFCI required per CEC 625 + 210.8(A). See note below about nuisance tripping. |
| 30A 2-pole GFCI | Siemens QF230A | 1 | Electric dryer (future). GFCI required for 240V garage receptacle per CEC 210.8(A). |
| 20A 1-pole GFCI | Siemens QF120A | 4 | Washer, general/garage door, workshop tools, dust collection. All garage receptacles must be GFCI per CEC 210.8(A)(2). |
| Type 2 SPD | Siemens QSA2020SPD or FS140 | 1 | **Surge protection — required per DBI inspector** (2nd subpanel). Takes 2 breaker slots. ~$50-100. |

**Note:** The SN series panel supports plug-on neutral breakers (no pigtail needed). The QF-series breakers above are pigtail-style and work fine in the SN panel. If you prefer the cleaner plug-on neutral install, look for the equivalent Siemens PON GFCI breakers — but QF series is widely available and works in any Siemens panel.

### GFCI Notes

**HVAC condenser (Q250):** No GFCI needed. CEC 210.8 applies to *receptacle outlets*, not hardwired equipment. The condenser is hardwired via a disconnect/whip, so a standard breaker is fine.

**EV charger (QF250A):** GFCI is required by both CEC 210.8(A) (garage receptacle) and CEC 625 (EV charging receptacles specifically require GFCI). However, most EVSEs (including Emporia) have a built-in CCID (Charging Circuit Interrupting Device) that trips at 20mA. The Class A GFCI breaker trips at 5mA. Running both in series can cause **nuisance tripping** from self-test cycles and minor leakage. If this becomes a problem:
- Check if Emporia has guidance on compatibility with upstream GFCI breakers
- Some electricians use a standard breaker and rely on the EVSE's built-in GFCI — but this technically doesn't satisfy CEC 210.8 for the receptacle itself
- A dual-function (AFCI/GFCI) breaker is NOT needed here — just GFCI

**Dryer (QF230A):** GFCI required per CEC 210.8(A) for 240V receptacles in garages (2020+ code cycle).

**120V circuits (QF120A):** GFCI required for all 125V receptacles in garages per CEC 210.8(A)(2).

## Branch Circuit Wiring

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| 6/3 NM-B (Romex) w/ ground | 6 AWG, 3-conductor | ~25 ft | EV charger circuit (subpanel → NEMA 14-50). Length depends on outlet placement. |
| 10/3 NM-B (Romex) w/ ground | 10 AWG, 3-conductor | ~25 ft | Dryer circuit (subpanel → dryer receptacle) |
| 12/2 NM-B (Romex) w/ ground | 12 AWG, 2-conductor | ~100 ft | Four 20A 120V circuits (washer, general, workshop ×2). Estimate ~25ft each. |
| HVAC whip / wire | Reuse existing | — | Existing AC wire runs through garage already — cut and re-terminate at subpanel |

## Receptacles & Boxes

### Wall Build-Up Note

Finished wall = stud + plywood sheathing (1/2"–5/8") + fire-rated drywall (5/8" Type X) = **~1-1/4" total over stud face**. All boxes must be set to protrude 1-1/4" from stud face so they sit flush with finished wall. **Measure actual material thickness before mounting boxes.**

### Receptacles

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| ~~NEMA 14-50R receptacle~~ | ~~50A 240V~~ | ~~1~~ | **ALREADY OWNED** — check if flush-mount box can be shimmed/set to correct depth for plywood+drywall |
| ~~NEMA 14-50 box~~ | | ~~1~~ | **ALREADY OWNED** — verify depth works with 1-1/4" wall build-up |
| NEMA 14-30R receptacle | 30A 240V, flush mount | 1 | Dryer outlet |
| 20A duplex receptacles | Tamper-resistant | 6-8 | For the four 120V circuits. Number depends on how many outlets per circuit. |

### Boxes

All boxes are **new-work nail-on** type — mount to studs during rough-in with face set to protrude 1-1/4" from stud (flush with finished plywood + drywall surface).

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Deep single-gang new-work boxes | Nail-on, 2-1/2" or 3-1/2" deep, adjustable | 6-8 | For 20A duplex receptacles. Deep boxes give room for GFCI receptacles if ever needed, and for wire fill. |
| 2-gang or large single-gang new-work box | Nail-on, rated for 30A receptacle | 1 | For NEMA 14-30R dryer outlet. Check receptacle mounting pattern. |
| Box for NEMA 14-50 | | 0 | **ALREADY OWNED** — confirm it can mount to framing at correct depth |
| Box extenders | Single-gang | 2-3 spare | Keep on hand in case any box ends up recessed after plywood + drywall. Cheaper than remounting. |

### Wall Plates

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Single-gang wall plates | Standard, match receptacle color | 6-8 | For 20A duplex receptacles |
| Wall plate — NEMA 14-50 | Flush mount | 1 | If not integrated into existing box/receptacle |
| Wall plate — NEMA 14-30 | Flush mount | 1 | Dryer |

## Grounding

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Ground bar kit | Compatible with Siemens SN series | 1 | If not included with panel. Subpanel must have separate neutral and ground bars. Check if the SN panel already has separate bars — many do. |
| Grounding electrode conductor | 6 AWG copper bare | ~10 ft | If subpanel requires its own grounding electrode — check local code. May bond to existing water pipe or drive a ground rod. |
| Ground rod + clamp | 8 ft copper-clad ground rod | 0-1 | Only if required by inspector |

## Misc Hardware

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| Steel nail plates | 1/16" thick, 1.5"×3" or similar | 1 box (20-50 pcs) | Required where wire passes within 1-1/4" of stud face (NEC 300.4). With plywood + drywall going on, install liberally on any bored hole near the face. Cheap insurance. |
| Cable staples — NM-B (12/2, 10/3) | Plastic or metal, various sizes | 1 box each | Secure Romex within 12" of boxes and every 4.5 ft per NEC 334.30. |
| Cable staples — SER feeder | Sized for 2/0 SER cable (~1.2" OD) | 1 pack | If using Option A (SER). Secure within 12" of panel and every 4.5 ft. |
| Wire nuts / Wago connectors | Assorted sizes | 1 pack | |
| Cable clamps | For panel knockouts | As needed | NM-B and SER cable clamps for subpanel and boxes |
| Electrical tape | Black, red, white | 1 each | |
| Wire labels / markers | | 1 pack | Label circuits in panel |
| Torque screwdriver or wrench | Inch-pound rated | 1 | Breaker and lug terminations have specified torque values. Inspectors may check. |

## Not Needed Now (Future)

| Item | Notes |
|------|-------|
| Transfer switch | For future DIY battery storage |
| Inverter + batteries | Future project |
| Emporia CTs for subpanel | If you want to monitor the new subpanel circuits |

---

## Estimated Wire Lengths Summary

| Run | Wire | Est. Length |
|-----|------|-------------|
| Main panel → subpanel (feeder) | 1 AWG copper × 4 conductors | ~15 ft each |
| Subpanel → EV charger (NEMA 14-50) | 6/3 NM-B | ~15-25 ft |
| Subpanel → dryer outlet | 10/3 NM-B | ~15-25 ft |
| Subpanel → washer outlet | 12/2 NM-B | ~15-25 ft |
| Subpanel → workshop/general outlets | 12/2 NM-B | ~25 ft × 3 circuits |
| HVAC condenser | Reuse existing wire | — |

**Note:** Measure actual runs before buying. Add 10-15% for routing around obstacles and termination slack. Wire is sold by the foot at most home improvement stores — buy what you need, don't overbuy the heavy gauge stuff.
