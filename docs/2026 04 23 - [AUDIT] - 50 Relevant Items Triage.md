# Pipeline Run 2026-04-23 — 50-Item Relevance Triage

**Source:** `/tmp/tckc-pipeline-20260422.log`
**Context:** Pipeline fetched 4 sources (Federal Register, Congress, CourtListener, News). 50 items cleared both keyword + Claude Haiku relevance screening. The 15-item generation cap then dropped 35. Only 3 entries survived generation + dedup.

## Classification legend

- **✅ FEDERAL-CODE** — genuine federal action, should be coded
- **⏸ FEDERAL-LOW** — federal but routine/low-signal (NAGPRA compliance filings, meeting notices); code if volume budget allows
- **🔇 MUTE** — federal framing but sub-federal actor; code then mute
- **❌ DROP** — noise, opinion, tabloid, or explicit duplicate
- **🔁 DUP** — duplicate of earlier item in the same run

## Already processed in this run

| # | Item | Status |
|---|---|---|
| 43 | SPLC / DOJ probe (PBS source) | Generated → merged into #44 |
| 44 | SPLC / DOJ probe (AP source) | Generated → kept as `doj-v-splc-2026` |
| 9 | Garvies Point NAGPRA Inventory | Generated → `doi-notice-2026-009` |
| 39 | "Woke judge sentences man who throttled toddler" | Generation FAILED (correct call — tabloid) |
| 46 | National Forests Texas Oil/Gas Leasing | Generated → `usfs-notice-2026-001` (duplicate skipped on dedup) |
| 1 | H.Res Arab American Heritage Month | Generated → `hres-351-119` (duplicate skipped on dedup) |

## The remaining 44 items

### ✅ FEDERAL-CODE (high-value, should be coded in follow-up pass)

| # | Item | Category | Likely severity | Why |
|---|---|---|---|---|
| 27 | Safeguarding Women from Chemical Abortion Act | legislation | **SEVERE** | Federal abortion-restriction legislation; affects women + health equity |
| 32 | Joint Employer Status Under the Fair Labor Standards Act | agency_actions | HARMFUL | Labor-protection rollback; affects low-wage workers, Latiné farmworkers, immigrants |
| 35 | National Emission Standards for HAP: Crude Oil and Natural Gas | agency_actions | HARMFUL | EPA rulemaking on oil/gas emissions; environmental justice angle |
| 36 | No Place for LGBTQ+ Hate Act | legislation | PROTECTIVE | Federal anti-hate legislation |
| 37 | Educational Equity Challenge Grant Act of 2026 | legislation | PROTECTIVE | Federal education equity funding |
| 38 | HBCU Research Capacity Act | legislation | PROTECTIVE | Federal HBCU legislation; direct CKC scope |
| 17 | Senate Resolution — 2026 Day of Silence | legislation | PROTECTIVE | Federal LGBTQ+ solidarity resolution |
| 22/29 | April 11–17 week designation (likely Black Maternal Health Week) | legislation | PROTECTIVE | Federal commemorative resolution |
| 24 | Utah Uinta Basin 8-Hour Ozone NAAQS Reclassification | agency_actions | Likely HARMFUL | EPA ozone reclassification in area with tribal interests |
| 25 | Great Plains Tribal Portions — Failure to Attain/Reclassification | agency_actions | HARMFUL | EPA air-quality reclassification affecting tribal lands |
| 26 | Re-Establishment of Hunting and Shooting Sports Conservation Council | agency_actions | HARMFUL | DOI re-establishes sport-focused advisory body over conservation |
| 34 | Idaho Power Company Tribal Consultation Meeting | agency_actions | PROTECTIVE | Tribal consultation notice |
| 42 | Smithsonian Taps Peabody Essex's Lynda Roscoe Hartigan to Lead American Art Museum | agency_actions | Neutral / monitor | Federal cultural institution leadership change |
| 49 | Maryland Advisory Committee to U.S. Commission on Civil Rights | agency_actions | PROTECTIVE | Federal civil-rights commission advisory meeting |

**14 items worth coding.**

### ⏸ FEDERAL-LOW (NAGPRA routine notices — code if generation-cap budget allows)

These are individual NAGPRA inventory-completion and intended-repatriation notices published in the Federal Register. All are federal-law implementation, but they're high-volume routine filings. Each is PROTECTIVE.

| # | Institution | Status |
|---|---|---|
| 2 | University of Nebraska State Museum | NAGPRA inventory |
| 3 | University of Texas at San Antonio | NAGPRA inventory |
| 4 | San Bernardino County Museum | NAGPRA repatriation |
| 5 | Field Museum, Chicago | NAGPRA inventory |
| 6 | Martha's Vineyard Museum | NAGPRA repatriation |
| 7 | American Museum of Natural History (NYC) | NAGPRA repatriation |
| 8 | Denver Museum of Nature & Science | NAGPRA repatriation |
| 10 | Brooklyn Museum | NAGPRA repatriation |
| 11 | Yale Peabody Museum | NAGPRA inventory |
| 12 | Yale Peabody Museum | NAGPRA repatriation |
| 13 | University of Michigan | NAGPRA inventory |
| 14 | Indiana University | NAGPRA inventory |
| 15 | U.S. DOI / NPS | NAGPRA inventory (federal actor) |
| 16 | Miami University (Ohio) | NAGPRA repatriation |
| 18 | Florida Department of State | NAGPRA inventory |
| 19 | Thornton W. Burgess Society | NAGPRA repatriation |
| 20 | U.S. Army Corps of Engineers, Tulsa | NAGPRA inventory (federal actor) |
| 21 | Robert S. Peabody Institute | NAGPRA repatriation |
| 33 | Culturally Significant Objects Imported for Exhibition | Cultural property clearance |

**19 NAGPRA-type items.** Recommend coding batch-style with a compressed PROTECTIVE entry pattern or one aggregate entry rather than 19 individual ones. Historical coding precedent in the tracker is individual entries; ask whether to continue that pattern.

### ❌ DROP (noise, opinion, editorial)

| # | Item | Why drop |
|---|---|---|
| 40 | HGTV stars sued for showing burial remains on TV | Tabloid; not a federal action |
| 41 | "Intersectionality – The Rise of a Dangerous Anti-American Ideology" | Opinion / polemic, not a federal action. Likely right-wing commentary that slipped through keyword filter. |
| 45 | War, climate change, and AI at UN Indigenous forum | Commentary on international event; could be INTERNATIONAL-coded but low value |
| 47 | Public Meeting of the Advisory Board for Exceptional Children | Routine BIE meeting notice |
| 48 | Survey of Postgraduate data collection | OMB paperwork burden notice |
| 50 | Proposed Data Collection Submitted for Public Comment | Generic OMB paperwork notice |
| 23/30/31 | Networks for School Improvement Evaluation | OERI research report, not a federal action |

**9 items to drop** (including the duplicates within the drops).

### 🔁 DUP (duplicates within the batch)

| # | Item | Dup of |
|---|---|---|
| 28 | Arab American Heritage Month | #1 |
| 29 | April 11-17 week designation | #22 |
| 30 | Networks for School Improvement (1) | #23 |
| 31 | Networks for School Improvement (2) | #23 |

**4 duplicates** (listed above for reference; don't double-count).

### 🔇 MUTE (state/local, even if coded)

Under current standards: **none** in this batch. All 50 items either are federal actions, federal-law implementation, federal publications, or federal legislation. No state-legislature bills, no municipal ordinances, no campus-government resolutions, no local events appeared in this run's 50.

However, two ambiguous items warrant flagging:
- #18 Florida Dept. of State NAGPRA notice — actor is a state agency complying with federal NAGPRA. Underlying law federal, actor state. Recommend code as FEDERAL-LOW (not MUTE) since Federal Register publication makes it a federal compliance action.
- #49 Maryland Advisory Committee to U.S. Commission on Civil Rights — the Advisory Committee is the state chapter of a federal commission. Federal framing holds.

## Summary totals

| Bucket | Count | Recommended action |
|---|---|---|
| Already processed | 6 | Done |
| FEDERAL-CODE (high-value) | 14 | Re-run with raised cap |
| FEDERAL-LOW (NAGPRA) | 19 | Re-run with raised cap; consider batch template |
| DROP (noise) | 7 | Skip; tune keyword/Haiku filter |
| DUP (within-run duplicates) | 4 | Let dedup handle |
| **Total 50** | **50** | |

## Recommendation for the follow-up pipeline pass

1. **Raise `MAX_ENTRIES_PER_RUN` to 60** (the current 15 cap throttled 35 of 50 legitimate candidates). 60 covers this batch + some headroom for NAGPRA volume spikes.
2. **Reset the state-file's `processed_ids` for source items tied to the 35 dropped items** so they get re-fetched on the next pass. (Or alternatively, re-fetch with `LOOKBACK_DAYS=5` to force reprocessing.)
3. **Tune the Haiku screener** to drop polemic/opinion pieces (#39, #40, #41) at the relevance stage rather than generation stage. Low priority.
4. **Decide NAGPRA batching policy.** Either code all 19 individually (historical pattern) or implement a monthly NAGPRA-roundup PROTECTIVE entry that aggregates repatriation activity.

---

*Audit prepared 2026-04-23.*
