# Electrical Permit — San Francisco DBI

## Scope of Work

- New subpanel (flush-mount between studs; 100A bus, 100A feeder from main panel)
- 240V/50A circuit for EV charger (NEMA 14-50) — **PRIORITY**
- 240V/30A circuit for electric dryer (NEMA 14-30) — confirm gas vs electric
- 120V/20A circuit for washer
- 120V/20A general purpose outlets (quantity TBD)

## Do I Need a Permit?

**Yes, for both the subpanel and the EV circuit.**

- Installing a new NEMA 14-50 outlet requires an electrical permit because you're adding a new circuit and modifying the electrical system.
- Installing a new subpanel always requires a permit.
- The only exception where no permit is needed: plugging an EV charger into an *existing, previously approved* NEMA 14-50 outlet. That doesn't apply here since the outlet doesn't exist yet.
- Since you're installing a new subpanel (not just tapping an existing panel with spare capacity), DBI requires an **electrical load calculation** to be submitted with the permit.

## SF DBI Permit Process

**Authority:** San Francisco Department of Building Inspection (SFDBI)
**Type:** Electrical permit (separate from building/plumbing)
**Process:** Over-the-counter for residential — no plan review wait

### Steps

- [ ] Complete the **Homeowner's Electrical Permit Application** (available at sf.gov or DBI 4th floor)
- [ ] Prepare electrical load calculation (required because new subpanel)
- [ ] Bring application + load calc to DBI, 49 South Van Ness Ave, 4th floor, Inspection Services counter
- [ ] Bring photo ID proving you are the owner (or proof of ownership if recently purchased)
- [ ] Receive approval and permit number (same day for OTC)
- [ ] Do the work
- [ ] Schedule rough-in inspection BEFORE covering any wiring (call or use DBI online scheduling)
- [ ] Pass rough-in inspection
- [ ] Close walls / install covers
- [ ] Schedule final inspection
- [ ] Pass final inspection

### Key Links

- Apply: https://www.sf.gov/apply-electrical-permit
- DBI info sheets (including IS E-02 for EV): https://www.sf.gov/resource--2022--information-sheets-dbi
- Permit scheduling: https://dbiweb02.sfgov.org/dbi_electrical/
- Fee schedule (2025): https://media.api.sf.gov/documents/REVISED_Table_1A-E_-_Electrical_Permit_Issuance_and_Inspection_2025.pdf
- Contact: 628-652-3320 or dbionlineservices@sfgov.org

## Homeowner Pull Notes

**Homeowner can legally DIY all electrical work including subpanel.** No licensed electrician required by code. See full sourced finding: [`decisions/electrical-homeowner-diy-legal.md`](../decisions/electrical-homeowner-diy-legal.md)

- CA B&P Code § 7044: homeowner exemption from contractor licensing
- SF Electrical Code § 89.120(E): homeowner permit for single-family dwelling
- No amperage or scope restriction on homeowner work
- Work must be done by permit holder or immediate family
- Friend advising informally is fine; friend cannot do the work under your permit
- DBI info sheet IS E-03 covers license requirements for electrical permit issuance

## Load Calculation Concern

- Main panel is 175A (downgraded from 200A during PV+battery install)
- The downgrade was likely for NEC 705.12 compliance (120% bus bar rule for solar backfeed)
- **Must determine available capacity** before sizing the subpanel feed
- Need to check: main bus bar rating, solar breaker size, existing loads
- Formula: main breaker + solar breaker ≤ bus bar rating × 1.2

## Key Code References

- California Electrical Code (CEC) 2025 — SF's adopted code
- Garage outlets must be GFCI protected (CEC 210.8)
- EV charging circuits: NEC/CEC 625
- Subpanel grounding: may need own grounding electrode
- SF Building Code 106A.1.16 — EV charging station permits
