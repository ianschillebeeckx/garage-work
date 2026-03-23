# NEC STANDARD ELECTRICAL LOAD CALCULATION FOR SINGLE FAMILY DWELLING

Service Rating: 120/240 Volt, 3 Wire

---

| | |
|---|---|
| **Owner** | [NAME] |
| **Address** | [STREET] |
| | [CITY, STATE ZIP] |
| **Total Floor Area** | 1,700 sq ft |
| **Date** | _______________ |
| **Permit No.** | _______________ |

---

## SERVICE INFORMATION

| | |
|---|---|
| Panel | Square D SO2040M200S, Series M01 |
| Service Voltage | 120/240V, 1Ø, 3W |
| Bus Rating | 200A |
| Main Breaker | 175A (derated per CEC 705.12 for solar backfeed) |
| Solar Backfeed Breaker | 60A (Tesla Powerwall 3) |
| 120% Rule (CEC 705.12) | 175A + 60A = 235A ≤ 240A (200 × 1.2) ✓ |

---

## PROPOSED WORK

New 100A subpanel feeder to attached garage (100A bus subpanel), fed from main panel. Relocate existing 50A HVAC condenser circuit from main panel to garage subpanel. New circuits: 240V/50A EV charger (NEMA 14-50), 240V/30A dryer, 120V/20A washer, 120V/20A general receptacles (relocated existing), 120V/20A workshop power tools, 120V/20A workshop dust collection.

---

## LOAD CALCULATION — NEC ARTICLE 220 STANDARD METHOD

### GENERAL LIGHTING, SMALL APPLIANCE & LAUNDRY LOADS

| Line | Description | NEC Ref | Calculation | VA |
|------|-------------|---------|-------------|---:|
| 1 | General lighting & receptacles | 220.12 | 1,700 sf × 3 VA/sf | 5,100 |
| 2 | Small appliance circuits (min. 2) | 220.52(A) | 2 × 1,500 VA | 3,000 |
| 3 | Laundry circuit (min. 1) | 220.52(B) | 1 × 1,500 VA | 1,500 |
| 4 | **Subtotal (Lines 1+2+3)** | | | **9,600** |

### DEMAND FACTOR — TABLE 220.42

| Line | Description | NEC Ref | Calculation | VA |
|------|-------------|---------|-------------|---:|
| 5 | First 3,000 VA at 100% | Table 220.42 | 3,000 × 1.00 | 3,000 |
| 6 | Remainder at 35% | Table 220.42 | (9,600 − 3,000) × 0.35 | 2,310 |
| 7 | **Net lighting/appliance/laundry load** | | **Line 5 + Line 6** | **5,310** |

### FIXED APPLIANCES — NEC 220.53

| Line | Appliance | Nameplate Rating | VA |
|------|-----------|-----------------|---:|
| 8a | Water heater — Rheem hybrid HP, 50 gal | 4,500W | 4,500 |
| 8b | Electric oven — ZLINE RA36 dual fuel range | 7,200W (30A × 240V) | 7,200 |
| 8c | Microwave — Frigidaire FFCM1430LS | 1,450W | 1,450 |
| 8d | Dishwasher | 1,440W | 1,440 |
| 8e | Refrigerator | 600W (est.) | 600 |
| 8f | Subtotal (5 appliances) | | 15,190 |
| 8 | **≥ 4 appliances: apply 75% demand** | 220.53 | **15,190 × 0.75** | **11,393** |

### HVAC — LARGEST OF HEATING OR COOLING — NEC 220.60

| Line | Component | Model | Nameplate | VA |
|------|-----------|-------|-----------|---:|
| 9a | Outdoor condenser | CAC/BDP 38MURAQ36AB3 | 24.0A × 230V | 5,520 |
| 9b | Indoor fan coil | CAC/BDP 40MUAAQ36XA3 | 4.0A × 230V | 920 |
| 9c | Auxiliary electric heat strip | None installed | — | 0 |
| 9 | **Total HVAC (heating and cooling are noncoincident)** | | | **6,440** |

### DRYER — NEC 220.54

| Line | Description | NEC Ref | VA |
|------|-------------|---------|---:|
| 10 | Electric dryer (planned — 5,000 VA min. per 220.54) | 220.54 | **5,000** |

### RANGE / COOKING — NEC TABLE 220.55

| Line | Description | NEC Ref | VA |
|------|-------------|---------|---:|
| 11 | Range/cooktop: currently gas (no electric load) | 220.55 | **0** |

### ELECTRIC VEHICLE CHARGER — NEC 625

| Line | Description | NEC Ref | Calculation | VA |
|------|-------------|---------|-------------|---:|
| 12 | Level 2 EVSE, NEMA 14-50 receptacle | 625 | 40A cont. × 240V | **9,600** |

### LARGEST MOTOR — NEC 220.14(A), 430.24

| Line | Description | VA |
|------|-------------|---:|
| 13 | 25% of largest motor (HVAC outdoor: 24A × 230V × 0.25) | **1,380** |

---

## TOTAL CALCULATED DEMAND (Summary of Lines 1–13 above)

| Line | Category | NEC Ref | VA |
|------|----------|---------|---:|
| A | General lighting + small appliance + laundry (after demand) | 220.12/42/52 | 5,310 |
| B | Fixed appliances (5 at 75%) | 220.53 | 11,393 |
| C | HVAC — heat pump, no aux. heat | 220.60 | 6,440 |
| D | Dryer | 220.54 | 5,000 |
| E | Range/cooktop (gas — no electric load) | 220.55 | 0 |
| F | EV charger | 625 | 9,600 |
| G | Largest motor (25%) | 430.24 | 1,380 |
| | **TOTAL CALCULATED LOAD (A–G)** | | **39,123 VA** |

---

## SERVICE ADEQUACY

| | |
|---|---:|
| Total calculated load | 39,123 VA |
| Total calculated current (÷ 240V) | **163.0A** |
| Existing main breaker | 175A |
| Available margin | 12.0A |
| **Service is adequate?** | **YES** |

---

## EXISTING BREAKER SCHEDULE — MAIN PANEL (Square D SO2040M200S)

| Slot | Left Side | | Slot | Right Side |
|------|-----------|---|------|------------|
| 1 | — (empty) | | 2 | — (empty) |
| 3 | 100A 2P — House subpanel | | 4 | 20A 1P — Garage recepts (relocating) |
| 5 | (continued) | | 6 | — (empty) |
| 7 | — (empty) | | 8 | — (empty) |
| 9 | — (empty) | | 10 | — (empty) |
| 11 | — (empty) | | 12 | — (empty) |
| 13 | ~~50A 2P — HVAC~~ (removed — relocated to garage subpanel) | | 14 | — (empty) |
| 15 | — (empty) | | 16 | — (empty) |
| 17 | 60A 2P — PW3/Solar (backfeed) | | 18 | — (empty) |
| 19 | (continued) | | 20 | — (empty) |

**New:** 100A 2-pole — Garage subpanel feeder (to be installed in open slot)

## NEW GARAGE SUBPANEL SCHEDULE

| Breaker | Circuit |
|---------|---------|
| 50A 2-pole | HVAC condenser (relocated from main panel) |
| 50A 2-pole | EV charger — NEMA 14-50 receptacle |
| 30A 2-pole | Electric dryer receptacle |
| 20A 1-pole | Washer receptacle |
| 20A 1-pole | General receptacles + garage door opener (relocated) |
| 20A 1-pole | Workshop receptacles — power tools (table saw, drill press, etc.) |
| 20A 1-pole | Workshop receptacles — dust collection / shop vac |

---

## NOTES

1. Main breaker was derated from 200A to 175A during PV/battery installation (permit E2024091423XX, energized 9/30/2024) per CEC 705.12 (120% bus bar rule for solar backfeed).
2. Dryer is currently gas. This calculation includes a planned future electric dryer at NEC 220.54 minimum of 5,000 VA to avoid re-permitting.
3. EV charger is an Emporia smart EVSE with load management capability. Load calculation uses full rated continuous current (40A) without load management credit.
4. HVAC system has no auxiliary electric heat strip installed. Confirmed by homeowner inspection of indoor air handler.
5. Nameplate data for HVAC outdoor unit, indoor fan coil, and water heater taken from equipment labels (photos on file).
6. All appliance ratings from nameplate or manufacturer specs. Refrigerator uses 600W estimate (nameplate not accessible).
7. All garage receptacles will be GFCI protected per CEC 210.8(A)(2).
8. Subpanel will have separate neutral and ground bus bars per CEC 250.
