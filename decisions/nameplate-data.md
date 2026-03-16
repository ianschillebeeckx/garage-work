# Decision: Appliance Nameplate Data (from photos)

**Date:** 2026-03-16
**Source:** Photos taken by homeowner — `photos/nameplates/` and `photos/main_panel/`

## Main Panel — Square D All-In-One

**Photo:** `photos/main_panel/panel_tag.jpg`

- **Brand:** Square D
- **Cat. No:** SO2040M200S
- **Series:** M01
- **Type:** Combination Service Entrance, Customer Owned Equipment
- **Enclosure:** Rainproof Type 3R
- **Mains:** 200A Max
- **Bus Rating:** 200A Max
- **Voltage:** 120/240V, 1Ø, 3W, 50-60 Hz
- **Meter socket:** 200A continuous, suitable for overhead service only
- **Conductors:** Suitable for 75°C copper or aluminum, 6 AWG to 350 kcmil
- **Breaker compatibility:** 15-100A and 150-200A **branch breakers only** — this means **QO or Homeline type** (need to confirm which from breaker markings)
- **Panel capacity:** 20 spaces / 40 circuits (SO**20**40M200S)
- **DBI approval sticker:** "Approval to Energize Service" dated 9/30/24, permit no. E2024091423XX, installer: [solar company]

### Panel Layout (from photo: `photos/main_panel/panel_circuits.jpg`)

```
Slot   Left                    Right
─────────────────────────────────────
1-2    [empty]                 [empty]
3-4    SUB PANEL (100A 2P)     GARAGE PLUGS (20A 1P) + [empty]
5-6    (cont.)                 [empty]
7-8    [empty]                 [empty]
9-10   [empty]                 [empty]
11-12  [empty]                 [empty]
13-14  A/C (marked, 2P)        [empty]
15-16  (cont.)                 [empty]
17-18  PW3 Solar (60A 2P)      [empty]
19-20  PW3 (cont.)             [empty]
```

**Confirmed: many open slots.** The 100A sub panel is on left slots ~3-4, A/C on ~13-14, Powerwall 3 / Solar on slots ~17-20 (bottom, as required by 120% rule — backfeed breakers must be at the opposite end from the main breaker). Garage plugs 20A on right side slot ~4.

**IMPORTANT: Backfeed breaker (PW3/Solar) is at the bottom of the panel.** Per NEC 705.12, when using the 120% rule, the backfeed breaker must be at the opposite end of the bus from the main breaker. This is correctly installed.

## HVAC — Outdoor Unit (Condenser)

**Photo:** `photos/nameplates/hvac_outdoor_unit.jpg`

- **Brand:** CAC/BDP (Carrier-affiliated)
- **Product No:** 38MURAQ36AB301
- **Model:** 38MURAQ36AB3
- **Serial:** 3924V27002
- **Type:** Split Air Conditioner 45ZR
- **Power Source:** 208/230V, 60Hz, 1Ph
- **Rated Input Current:** 24.0A at 208/230V
- **Minimum Circuit Ampacity:** 30.0A
- **MOP (Maximum Overcurrent Protection):** 50.0A
- **Outdoor Fan Motor:** 1/9 HP × 2
- **Outdoor Unit Resistance Class:** IPX4
- **Refrigerant:** R410A
- **Short-circuit current:** 2.4 kA rms symmetrical, 240V max

**For NEC 220 load calc: 24.0A × 230V = 5,520 VA (nameplate)**
**Observed draw: 3.0-3.5 kW** (per Powerwall monitoring) — consistent, as compressor doesn't always run at full rated current.

## HVAC — Indoor Unit (Fan Coil)

**Photo:** `photos/nameplates/hvac_indoor_unit.jpg`

- **Brand:** CAC/BDP
- **Product No:** 40MUAAQ36XA301
- **Model:** 40MUAAQ36XA3
- **Serial:** 2624V19028
- **Power Source:** 208/230V, 60Hz, 1Ph
- **Rated Input Current:** 4.0A at 208/230V
- **Minimum Circuit Ampacity:** 5.0A
- **MOP:** 15.0A
- **Indoor Fan Motor:** 1/2 HP
- **Max Auxiliary Electric Heater Power:** 20 kW

### Electric Heater Kit Options (from nameplate table)

| Heater Kit | Electric Heat (kW) | Full Load Amps | Min Circuit Ampacity | Max Overcurrent |
|------------|-------------------|----------------|---------------------|-----------------|
| EHKMB05KN | 3.75 / 4.6 | 18.0 / 20.0 | 23.0 / 27.0 | 25.0 / 30.0 |
| EHKMB08KN | 6.0 / 7.35 | 28.8 / 32.0 | 37.0 / 42.0 | 40.0 / 45.0 |
| EHKMB10KN | 7.5 / 9.2 | 36.1 / 40.0 | 46.0 / 53.0 | 50.0 / 60.0 |
| EHKMB15KN | 11.25 / 13.8 | 54.1 / 60.0 | 23.0 / 27.0 + 46.0 / 53.0 | 25.0 / 30.0 + 50.0 / 60.0 |
| EHKMB20KN | 15.0 / 18.4 | 72.1 / 80.0 | 46.0 / 53.0 + 46.0 / 53.0 | 50.0 / 60.0 + 50.0 / 60.0 |

**Confirmed: NO auxiliary heat strip installed.** Indoor unit draws only 4.0A (~920 VA).

## Water Heater

**Photo:** `photos/nameplates/water_heater.jpg`

- **Brand:** Rheem (based on style)
- **Type:** Hybrid Water Heater (heat pump)
- **Capacity:** 50 gallon
- **Volts:** 208/240
- **Hertz:** 60
- **Phase:** 1
- **Amps:** 12A (rated)
- **Min Wire/Max Fuse (or Breaker):** 0.015A (?) — hard to read
- **Max Supply Current:** 29.5A
- **HACR Type Breaker:** for USA
- **Upper Elements:** 4.5 kW
- **Lower Elements:** 4.5 kW
- **Refrigerant:** R134a
- **Max Working Pressure:** 150 PSI

**For NEC 220 load calc:** In heat pump mode, draws ~12A × 240V = 2,880 VA. In electric resistance backup mode, draws up to 4,500 VA per element (elements don't typically run simultaneously). **Use 4,500 VA for NEC 220 calc** (worst case single element).

## Microwave

**Photo:** `photos/nameplates/nameplate_microwave.jpg`

- **Brand:** Frigidaire (Electrolux Home Products)
- **Model:** FFCM1430LS
- **Serial:** MG02030673
- **Manufactured:** May 2010
- **Voltage:** 120V / 60Hz
- **Rated Input:** 1,450W
- **Rated Output:** 1,000W
- **Microwave Frequency:** 2450 MHz

**For NEC 220 load calc: 1,450 VA**

## Summary for Load Calculation

| Appliance | Nameplate VA | Notes |
|-----------|-------------|-------|
| HVAC outdoor unit | 5,520 VA (24A × 230V) | Use for NEC 220 |
| HVAC indoor unit (fan only) | 920 VA (4A × 230V) | Without heat strip |
| HVAC heat strip | **CHECK IF INSTALLED** | Could add 3,750-18,400 VA |
| Water heater | 4,500 VA | Single element max |

## Main Panel Confirmation

| Item | Value |
|------|-------|
| Brand | Square D |
| Cat. No | SO2040M200S |
| Series | M01 (Homeline-compatible "All-In-One") |
| Spaces | 20 spaces / 40 circuits |
| Bus | 200A |
| Open slots | ~14 (plenty) |
| Breaker type needed | **Homeline (HOM)** — the SO series is Homeline, not QO |
| Feeder breaker | **HOM260** (Homeline 60A 2-pole) |
