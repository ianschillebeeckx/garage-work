# Decision: NEC Article 220 Load Calculation

**Date:** 2026-03-16
**Status:** READY — all major nameplate data collected, no heat strip installed
**Applies to:** Electrical permit application, subpanel feeder sizing

## Home Data

- **Square footage:** ~1,700 sf
- **Service:** 200A bus, 175A main breaker (derated for solar backfeed)

## Existing Major Appliances

| Appliance | Type | Est. VA | Nameplate VA | Notes |
|-----------|------|---------|-------------|-------|
| HVAC outdoor (condenser) | Split AC, CAC/BDP 38MURAQ36AB3 | 5,520 | 5,520 (24A × 230V) | MOP 50A; observed 3-3.5 kW |
| HVAC indoor (fan coil) | CAC/BDP 40MUAAQ36XA3 | 920 | 920 (4A × 230V) | **Excludes heat strip — check if installed** |
| HVAC heat strip | **NOT INSTALLED** | 0 | 0 | Confirmed by homeowner — no aux heat strip |
| Water heater | Rheem hybrid heat pump, 50 gal | 4,500 | 4,500 (single element max) | 12A in heat pump mode; 4.5kW element backup |
| Oven/range | Electric oven / gas cooktop | 4,000 | **TODO** | Plan to upgrade to induction |
| Microwave | Standard | 1,500 | **TODO** | |
| Dishwasher | Standard | 1,800 | **TODO** | |
| Refrigerator | Standard | 600 | **TODO** | |

## New Garage Loads (to be added)

| Load | VA | Notes |
|------|-----|-------|
| EV charger (NEMA 14-50) | 9,600 | 40A × 240V continuous; Emporia smart charger with load mgmt |
| Dryer (electric, 240V) | 5,000 | NEC minimum; need nameplate if higher |
| Washer (120V) | 2,400 | |
| General outlets + garage door | 1,500 | |

## NEC 220 Standard Calculation (Draft)

### Step 1: General Lighting + Receptacles (NEC 220.12)

1,700 sf × 3 VA/sf = **5,100 VA**

### Step 2: Small Appliance + Laundry Circuits (NEC 220.52)

- 2 kitchen small appliance circuits × 1,500 VA = 3,000 VA
- 1 laundry circuit × 1,500 VA = 1,500 VA
- Subtotal: **4,500 VA**

### Step 3: Demand Factor on General + Small Appliance (NEC Table 220.42)

Combined: 5,100 + 4,500 = 9,600 VA
- First 3,000 VA at 100% = 3,000
- Remaining 6,600 VA at 35% = 2,310
- **Net: 5,310 VA**

### Step 4: Fixed Appliances (NEC 220.53)

| Appliance | VA |
|-----------|----|
| Water heater (heat pump) | 4,500 |
| Electric oven | 4,000 |
| Microwave | 1,500 |
| Dishwasher | 1,800 |
| **Subtotal** | **11,800** |

4 or more fixed appliances → 75% demand factor
11,800 × 0.75 = **8,850 VA**

### Step 5: HVAC — Largest of Heating or Cooling (NEC 220.60)

Heat pump serves both heating and cooling. Use larger of heating or cooling (not both — NEC 220.60).

**Cooling mode:** Outdoor 24A + Indoor fan 4A = 28A × 230V = **6,440 VA**
**Heating mode (heat pump only, no strip):** Similar to cooling — compressor runs in reverse. ~6,440 VA
**Heating mode (with heat strip):** If e.g. EHKMB10KN installed: 6,440 + 9,200 = **15,640 VA**

**Without heat strip: 6,440 VA** (use this unless strip is confirmed installed)
**With heat strip: up to 15,640 VA** (this would significantly tighten the calc)

Observed draw: 3-3.5 kW per Powerwall — consistent with partial-load compressor operation (nameplate is max rated).

### Step 6: Dryer (NEC 220.54)

Currently gas dryer (no electrical load beyond 120V motor).
**Planning to replace with electric dryer** — use 5,000 VA minimum per NEC 220.54: **5,000 VA**

### Step 7: EV Charger

40A continuous × 240V = **9,600 VA**

### Total Calculated Load

| Category | VA |
|----------|-----|
| General/small appliance/laundry (after demand) | 5,310 |
| Fixed appliances (at 75%) | 8,850 |
| HVAC (no heat strip) | 6,440 |
| Dryer (future electric) | 5,000 |
| EV charger | 9,600 |
| **TOTAL (no heat strip)** | **35,200 VA** |

**At 240V: 35,200 / 240 = ~147A**

**Margin under 175A main: ~28A (16%)** — comfortable

### If heat strip installed (e.g. 10kW EHKMB10KN)

| Category | VA |
|----------|-----|
| General/small appliance/laundry (after demand) | 5,310 |
| Fixed appliances (at 75%) | 8,850 |
| HVAC (with 10kW strip) | 15,640 |
| Dryer (future electric) | 5,000 |
| EV charger | 9,600 |
| **TOTAL** | **44,400 VA** |

**At 240V: 44,400 / 240 = ~185A — EXCEEDS 175A main**

This is why checking the heat strip matters.

### Scenario: Future Induction Range

If gas cooktop is replaced with induction range (~11,000-12,000 VA total for full induction range vs ~4,000 VA for current electric oven only):

Additional load: ~7,500 VA. But this replaces the oven in fixed appliances, so net add is smaller after demand factors.
Rough estimate with induction: ~140-145A. **Still fits under 175A, but tighter.**

### Caveats

- HVAC uses observed draw (3-3.5 kW) rather than nameplate. Standard NEC 220 calc technically requires nameplate. **Still need nameplate** for the formal permit application, but observed data gives confidence the number is reasonable.
- Dryer is currently gas. Calc includes a future electric dryer at NEC minimum 5,000 VA.
- These are **code-calculated** loads, not actual peak loads. Real usage will be lower due to diversity.
- Emporia load management on EV charger further reduces real peak demand.

## Alternative: NEC 220.87 — Existing Demand Data

**This may be the better path given the Emporia monitoring system.**

NEC 220.87 allows using **actual measured demand data** instead of the standard calculation for existing dwellings that are being expanded. Requirements:

> The existing demand at the point of service entrance shall be measured over a minimum 30-day period using a recording ammeter or power meter. The measured demand shall be the maximum demand at any 15-minute interval during the recording period.

**Emporia monitors 16 circuits on the existing house subpanel (not the mains directly). However, the Powerwall 3 effectively tracks total service entrance load.** If the Powerwall app can export peak 15-minute demand over a 30-day period, this could satisfy NEC 220.87.

The new load (garage subpanel) is then simply **added** to the measured peak demand:
> New calculated load = Measured peak demand + new loads being added (per standard NEC 220)

This is likely much more favorable because:
- The HVAC, water heater, oven, etc. will show real peak usage (probably well under theoretical)
- Diversity is captured in the measurement (not everything peaks at once)
- The EV charger with Emporia load management could be argued as demand-managed

### What to Export from Powerwall / Tesla App

- [ ] Maximum 15-minute demand (amps or kW) at the service entrance over any recent 30-day period
- [ ] Tesla app "Home Usage" or "Grid" data may show this
- [ ] DBI may accept Tesla app screenshots/exports as documentation
- [ ] Alternatively, Emporia sum-of-circuits could approximate total load (covers most circuits on house subpanel)

## Recommendation

1. **Check Emporia for peak 15-min demand over the last 30 days** — if available, use NEC 220.87 (likely much more favorable)
2. **If not available, start a 30-day recording period now** — slight delay but stronger permit application
3. **In parallel, collect nameplate data** on HVAC, water heater, oven to complete the standard 220 calc as a backup
4. **The standard calc at ~141A appears to fit under 175A** even with conservative estimates, but the HVAC nameplate could change that

## Open Questions

- [x] ~~HVAC heat pump nameplate~~ — outdoor: 24A/5,520VA; indoor fan: 4A/920VA. See `decisions/nameplate-data.md`
- [x] ~~Water heater heat pump nameplate~~ — Rheem hybrid 50gal, 4,500VA element. See `decisions/nameplate-data.md`
- [x] ~~Is an auxiliary electric heat strip installed?~~ — No. Confirmed no strip.
- [ ] Can Tesla/Powerwall app export peak 15-min demand for NEC 220.87?
- [ ] Will DBI accept Powerwall data as "recording ammeter" for 220.87? (worth asking at counter)
- [x] ~~Is the dryer gas or electric?~~ — Currently gas; planning to go electric (calc includes future electric dryer)
- [x] ~~Does Emporia monitor mains?~~ — No, monitors house subpanel circuits only. Powerwall tracks mains.

## Sources

- NEC Article 220: Branch-Circuit, Feeder, and Service Load Calculations
- NEC 220.42: General Lighting demand factors
- NEC 220.52: Small appliance and laundry loads
- NEC 220.53: Appliance demand factor (4+ appliances at 75%)
- NEC 220.54: Dryer loads
- NEC 220.60: Noncoincident loads (heating vs cooling)
- NEC 220.87: Determining existing loads (measured demand method)
