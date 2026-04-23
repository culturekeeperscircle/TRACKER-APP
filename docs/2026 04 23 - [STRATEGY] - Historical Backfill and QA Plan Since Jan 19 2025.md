# Historical Backfill + QA Strategy
## Since Trump II Inauguration (2025-01-19) to Today (2026-04-23)

**Problem statement.** The TCKC Threat Tracker has an entry-generation cap introduced 2026-02-26 that silently dropped legitimate candidate entries on heavy news days. Additional gaps likely exist from pre-cap keyword coverage, pipeline downtime, and source-query limits. Prince requires comprehensive coverage of the Trump II era. This document specifies the diagnostic, the queries the pipeline actually runs, and a multi-phase backfill plan.

---

## Part 1. Diagnostic — What the Data Shows

### Current coverage by month since Jan 19, 2025

| Period | Entries | Avg/month | Era |
|---|---|---|---|
| 2025-01-19 → 2025-07 | 254 | 42 | No cap |
| 2025-08 → 2025-11 | 59 | 15 | No cap (but pipeline likely underused) |
| 2025-12 | 28 | 28 | No cap |
| 2026-01 | 64 | 64 | No cap |
| 2026-02 → 2026-04 (cap era) | 263 | 88 | Cap 15 or 25 |
| 2026-05 (partial) | 1 | — | Cap era |
| **Total** | **669** | | |

### Two distinct gap patterns

1. **Pre-cap quiet months (Aug–Nov 2025).** 15 entries/month average. Pipeline was likely under-run or the cron job faltered during that period. UPDATE_SUMMARY_2026_04_21.md confirms a billing failure poisoned the dedup state from April 4–17, 2026, and an April 19 state reset fixed it. A similar outage may have happened in fall 2025.
2. **Cap-era loss on heavy days.** The cap was 25 (Feb 26) → 15 (Feb 27) → 15 configurable (Apr 19). Tonight's 50-item batch from a 3-day window proves the cap drops entries. One heavy day can produce 50+ relevant candidates, of which only 15 survived.

Tonight's re-run confirms: when the cap was lifted to 50, **55** AI-relevant items surfaced from the same window. Five more were dropped at the raised cap. A lookback of 15 months with a cap of 15 per run on roughly-daily runs almost certainly dropped **hundreds** of legitimate candidates over the cap era alone.

---

## Part 2. The Queries the Pipeline Actually Runs

### Federal Register
- **Scope:** All new documents published since last run, up to 1,000/run.
- **Filter:** Keyword match against the list below.
- **No search query.** Federal Register returns everything; keyword filter selects.

### Congress.gov
- **Subjects (the actual filter):**
  1. Arts, Culture, Religion
  2. Civil Rights and Liberties, Minority Issues
  3. Environmental Protection
  4. Immigration
  5. Indian, Inuit, Alaskan Native Affairs
  6. International Affairs
  7. Government Operations and Politics
  8. Public Lands and Natural Resources
  9. Education
  10. Social Welfare
  11. Native Americans
  12. Historic Preservation
- **Scope:** Up to 500 bills per run across all subjects.
- **Plus:** `TRACKED_BILLS` list of specific bill numbers that always pass filter.

### CourtListener (federal court opinions)
**13 search queries:**
1. cultural resources historic preservation heritage
2. tribal sovereignty sacred sites NAGPRA indigenous
3. national monument Antiquities Act preservation
4. environmental justice civil rights Title VI discrimination
5. immigration deportation asylum TPS DACA refugee
6. NEA NEH arts funding Smithsonian IMLS
7. treaty rights Native American tribal consultation
8. African American civil rights racial equity HBCU
9. Latino Hispanic farmworker immigrant community
10. Asian American Pacific Islander AAPI hate crime
11. cultural practice traditional knowledge language preservation
12. museum library school university cultural programming education
13. foodways folk arts cultural arts celebration parade festival

Each query pulls up to 20 results per run.

### NewsAPI
**11 search queries** (quoted phrase groups):
1. "cultural resources" OR "historic preservation" OR "cultural heritage" OR "national monument"
2. "tribal sovereignty" OR "sacred sites" OR NAGPRA OR "indigenous rights" OR "Native American"
3. "environmental justice" OR "civil rights" OR "racial equity" OR "Title VI" OR discrimination
4. NEA OR NEH OR Smithsonian OR IMLS OR "arts funding" OR "cultural institution"
5. immigration OR deportation OR "refugee policy" OR DACA OR TPS OR asylum
6. "African American" OR "Black community" OR HBCU OR "racial justice" OR reparations
7. "Latino" OR "Hispanic" OR "farmworker" OR "immigrant community" OR Latinx
8. "Asian American" OR "Pacific Islander" OR AAPI OR "hate crime" OR "anti-Asian"
9. "cultural practice" OR "language preservation" OR "traditional knowledge" OR "folk art"
10. foodways OR "folk arts" OR "cultural arts" OR parade OR "cultural festival" OR celebration
11. museum OR library OR university OR school OR "cultural programming" OR "cultural center"

Each query pulls up to 20 articles per run.

### Keyword relevance filter (applied to Federal Register output)
Approximately 170 keywords across 12 community/topic categories: cultural heritage, Indigenous/Tribal, African-descendant, Latiné, AAPI, Other ethnic identity, Heritage months, Specific bills, Civil rights, Immigration, Environment, Arts/Education, Cultural life.

### Gaps in the current query design (even with cap lifted)
1. **No Federal Register search query per se.** All 1,000 daily Federal Register docs go through keyword filter. On busy days, true positives at rank 1001+ are never seen.
2. **CourtListener queries miss LGBTQ, women's rights, voting rights, reproductive rights, disability, faith-community cases.** Only 13 queries cover the 27-community taxonomy.
3. **NewsAPI queries miss reproductive rights, women, LGBTQ, disability, faith, voting rights, labor.** Only 11 queries for a 27-community taxonomy.
4. **No search for specific Trump II signature terms:** "DEI rollback," "Stop WOKE," "birthright citizenship," "Stop AAPI Hate Act," "sanctuary city," "MAGA," "America First."
5. **No Whitehouse.gov scraper.** Executive orders appear in Federal Register with a 1–3 day lag, and EO rescissions and proclamations often publish first at whitehouse.gov/presidential-actions.
6. **No executive-agency press-release scrapers.** Significant policy pronouncements (ED, DOJ, HHS, DHS, DOI, EPA) often appear in press releases before Federal Register.

---

## Part 3. The Four-Phase Backfill Plan

### Phase 0. Let tonight's follow-up pipeline finish (in progress)

The cap was raised to 50 for the current run. 55 items passed AI screening; 50 are generating now. Expected to finish within ~30 min from 10:10 PM ET. This captures the bulk of the last 3 days' backlog.

**Deliverable:** ~30–45 new entries added; Prince reviews post-pipeline.

### Phase 1. External cross-validation (cheapest, highest-yield)

Pull comprehensive lists of high-profile Trump II actions from authoritative external trackers, then check each against the TCKC Threat Tracker. Any missing items are candidate backfill entries.

**Sources to cross-reference:**

| External tracker | Scope | URL approach |
|---|---|---|
| ACLU Trump 2.0 Tracker | EOs, agency actions, litigation | aclu.org action tracker |
| Democracy Docket | Voting, civil rights litigation | democracydocket.com |
| Just Security Litigation Tracker | All challenges to Trump II actions | justsecurity.org/litigation-tracker/ |
| Brennan Center | Voting rights, democracy | brennancenter.org/research |
| Federation of American Scientists EO Tracker | Full EO list | sgp.fas.org |
| WaPo / NYT executive orders databases | EO scorecard | wapo.com / nytimes.com |
| Center for American Progress | Agency rollbacks | americanprogress.org |
| ProPublica Federal Layoffs Tracker | Agency staffing | propublica.org |
| Georgetown Law DEI Rollback Tracker | DEI-specific | law.georgetown.edu |
| NAACP LDF / LDF Thurgood Marshall Institute | Civil rights litigation | naacpldf.org |
| National Indian Law Library | Tribal court and federal | narf.org/nill |
| National Trust for Historic Preservation | Preservation threats | savingplaces.org |
| ALA / PEN America | Library / book-ban tracking | ala.org / pen.org |
| Cultural Heritage Partners Fight Back tracker | EO-specific Section 106 bypass | culturalheritagepartners.com |

**Method.**
1. Dispatch parallel Explore agents to scrape each tracker for all entries since 2025-01-19.
2. Each agent returns a structured list of actions with title, date, source URL.
3. Aggregate into a master candidate list.
4. Cross-reference against TCKC Threat Tracker by title, date, and agency.
5. Flag items missing from TCKC as Phase 3 backfill targets.

**Cost:** ~$20–40 (Claude Sonnet for ~15 parallel Explore agents, each doing web research).
**Time:** 60–90 min for agents in parallel.

### Phase 2. Topical coverage audit

For each of 13 major topic areas, produce a "should-have" list of top Trump II actions and compare against TCKC coverage.

| Topic Area | Signature events to verify |
|---|---|
| DEI rollbacks | EO 14173, EO 14151, agency DEI terminations, Stop WOKE Act challenges |
| Cultural-institution defunding | Kennedy Center, NEA, NEH, IMLS, SI Latino + API museums, CPB |
| Civil-rights enforcement | EEOC, DOJ CRT, DOE OCR rescissions and rule reversals |
| Immigration enforcement | ICE enforcement expansions, sensitive-locations rescission, DACA, TPS terminations |
| Birthright citizenship | EO 14160, multi-circuit litigation, SCOTUS proceedings |
| Tribal sovereignty | BIA decisions, NAGPRA, sacred sites, public lands |
| Federal lands | NPS, NPS disparage-America database, monument reviews, offshore wind |
| Education | ED dismantling, Title I/IX rescissions, HBCU funding, curriculum bans |
| LGBTQ+ | Title IX reversal, trans-rights EOs, healthcare bans |
| Reproductive rights | FDA mifepristone, Comstock revival, federal abortion restrictions |
| Voting rights | EO on elections, DOJ CRT voting, SAVE Act |
| Language access | EO 14224 official English, interpreter defunding |
| International / UN | UNESCO, UN forums, treaty actions, sanctions |

**Method.** For each topic area, produce a 10–20 item checklist of the most consequential Trump II actions. Check each against TCKC Threat Tracker. Flag missing ones.

**Deliverable:** A 150–200 item "must-have" backfill list.

### Phase 3. Source-sweep pipeline run with expanded queries

Re-run the pipeline with:
- `LOOKBACK_DAYS=460` (Jan 19, 2025 to today)
- `MAX_ENTRIES_PER_RUN=500`
- `SCREENING_TIME_BUDGET=7200` (2 hours)
- **Expanded CourtListener queries** (+6): LGBTQ rights, reproductive rights, voting rights, disability rights, faith communities, labor rights
- **Expanded NewsAPI queries** (+5): same gaps as above
- **Reset processed_ids** to empty

**Cost estimate.**
- Haiku screening for ~15,000 items = ~$30
- Sonnet generation for up to 500 items = ~$35
- Total: **~$65–80**

**Runtime:** ~8–12 hours, or overnight.

**Risks.**
- API rate limits (mitigated by existing rate limiter in pipeline)
- Potential Federal Register duplicate loss (1000-doc cap per run means some docs from busy January weeks may not be fetched even over multiple runs)
- State corruption (mitigate with full state backup before run)

**Deliverable:** Exhaustive re-fetch + re-screen + re-generate across the Trump II era with a sensible cap.

### Phase 4. Manual backfill for Phase-1/2 gaps not caught by Phase 3

Some items will be missing because:
- They were discussed in news but not in Federal Register / Congress.gov / CourtListener / NewsAPI (e.g., agency memos that never hit Federal Register, leaked documents, investigative-journalism scoops)
- They occurred outside the keyword taxonomy's reach
- They require judgment about cultural-resource impact

For each such item:
- Manually draft an entry using the pipeline's `scripts/add_legislation_batch.py` or a new `scripts/add_manual_entry.py` utility.
- Feed through schema validation.

**Cost:** Time. Estimate 5 min/entry × ~100 gap entries = **8–10 hours of Prince's time**, or roughly 3 hours if delegated to Kiran with clear source materials.

---

## Part 4. QA Framework (applies to all backfilled entries)

Every backfilled entry must pass:

1. **Schema validation.** Matches `pipeline/data/schema.py` structure.
2. **Community coding consistency.** Uses canonical 27-community taxonomy.
3. **PPPT impact analysis.** At least 250 words of `impactByCommunity.{community}` text describing effects on People, Places, Practices, and Treasures.
4. **Severity code justification.** SEVERE, HARMFUL, WATCH, or PROTECTIVE with 2-sentence rationale in `impact_rationale`.
5. **Source citation.** Primary source URL (Federal Register, Congress.gov, court opinion, news article) in `U` field.
6. **Cross-reference check.** Not a duplicate of an existing entry (ID-based dedup).
7. **Federal-actor rule.** State/university actors are muted, not individually coded (per the 2026-04-23 NAGPRA policy, applies to all entry types).

**Recommended QA audit script.** I can build a `scripts/audit_backfill.py` that runs the 7 checks on a newly generated entry before it's committed to data.json.

---

## Part 5. Execution Order and Time Budget

| Phase | Task | Time | Cost | Priority |
|---|---|---|---|---|
| 0 | Let tonight's follow-up pipeline finish + apply NAGPRA aggregation + mute state/university | ~30 min pipeline + ~15 min post-processing | Already spent | Critical |
| 1 | External cross-validation (15 parallel Explore agents) | 90 min | $30 | High |
| 2 | Topical coverage audit (produce must-have list) | 2–3 hours Prince | $0 | High |
| 3 | Source-sweep pipeline run with expanded queries, 460-day lookback | 8–12 hours overnight | $80 | Medium |
| 4 | Manual backfill of persistent gaps | 3–10 hours Kiran+Prince | Kiran API use | Medium |
| — | **Raise the default cap permanently** to 50 in pipeline/main.py and workflow | 5 min | $0 | Critical (do now) |
| — | **Expand source queries** (CourtListener + NewsAPI) | 30 min | $0 | High (do before Phase 3) |
| — | **Add whitehouse.gov and agency-press-release connectors** | 4–6 hours | $0 | Future enhancement |

---

## Part 6. Immediate Next Actions (Tonight)

1. **Wait for follow-up pipeline to finish** (running). Expect ~30–45 new entries.
2. **Post-pipeline: apply new policies:**
   - Mute any state/university NAGPRA entries that got coded.
   - Generate single "NAGPRA Roundup: April 2026" PROTECTIVE aggregate.
3. **Raise default cap to 50** in `pipeline/main.py:158` (one-line edit, pending Prince's confirmation).
4. **Commit all changes** to git with summary.
5. **Schedule Phase 1** (external cross-validation) for tomorrow morning when Prince is fresh. This is cheap, parallelizable, and gives the comprehensive picture of what the tracker is missing.

---

## Part 7. The Strategic Question You Should Hold

**Should the TCKC Threat Tracker aim for comprehensive coverage or curated coverage?**

- **Comprehensive** = every federal action affecting any of 27 communities, coded. High signal-to-noise but high volume. Your current direction.
- **Curated** = the 300–400 most consequential actions per year, coded deeply. Lower volume, more authority per entry.

The cap was introduced because the pipeline was structurally optimized for curated. Lifting it pushes toward comprehensive. This backfill should determine which of the two the tracker commits to for the long run. Either is defensible. Pick one and tune the pipeline accordingly.

---

*Strategy drafted 2026-04-23. Execute in phases 0 → 1 → 2 → 3 → 4. Revisit weekly during execution.*
