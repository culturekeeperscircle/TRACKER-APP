# TCKC Tracker — Harmonization Plan for the Three Semantic Refinements

**Prepared:** 2026-04-23
**Scope:** All 774 active (non-muted) entries in `data/data.json`.
**Purpose:** Bring existing entries into conformance with the canonical research question locked 2026-04-23, and set forward-facing rules so new entries conform automatically.

---

## The Three Refinements (Recap)

1. **Cultural continuity replaces cultural resources as the severity anchor.** SEVERE or HARMFUL requires a threat to the community's capacity to persist across generations. Generic harm to a museum without cultural-continuity impact no longer qualifies.
2. **Five primary communities tighten the frame.** Indigenous, African-descendant, Latiné, Asian, Pacific Islander. The existing 27-community taxonomy survives as a secondary layer; severity is pegged to the five.
3. **Diasporic scope on each primary community.** Indigenous includes Alaska Native and Native Hawaiian; African-descendant includes Afro-Caribbean and Afro-Latiné; Asian includes South, Southeast, East, AANHPI; Pacific Islander includes Compact of Free Association populations.

---

## Executive Summary of Findings

| Refinement | Flagged entries | % of 774 active | Workload |
|---|---:|---:|---|
| #1 — Missing continuity language on SEVERE/HARMFUL entries | **24** (of 613) | 3.9% | Light |
| #2 — Only secondary communities coded | **16** | 2.1% | Light |
| #3 — Primary community present but diasporic scope gap | **~300** (274 flag instances) | 38.8% | Heavy |
| Taxonomy normalization (newly surfaced) | **~774** (all entries) | 100% | Medium (scripted) |

**Total unique entries needing any revision: ~300 (~39% of active).** The lion's share is Refinement #3 (diasporic scope). Refinements #1 and #2 are small targeted cleanups.

---

## Refinement #1 — Cultural Continuity Language on Severe/Harmful Entries

### Clarification (2026-04-23 evening, per Prince)

The continuity frame is the **severity rubric** — the reason an entry earns SEVERE or HARMFUL. The PROSE in impact analysis should focus on **imminent, immediate, concrete harms** (specific places razed, specific ceremonies suppressed, specific funding rescinded, specific families separated), not formulaic use of words like "continuity," "generations," "persist."

**A keyword match on continuity language is not required.** An entry that describes real harm with named facts, real places, and identifiable people is doing the correct work even without the word "continuity."

### Finding (pre-clarification, keyword-based)

Of 613 active SEVERE or HARMFUL entries, **589 (96.1%)** invoke at least one cultural-continuity keyword. Only **24 (3.9%)** lack those specific keywords.

### Finding (post-clarification)

The 24 keyword-flagged entries are **not automatically deficient.** A keyword pass is a crude proxy. The real question for each of the 24 is: does the impact analysis describe concrete, imminent, immediate harm to the community's People, Places, Practices, or Treasures? Many of the 24 likely do this work substantively without using the specific words. A proper refinement-#1 audit requires Kiran or Prince to read each impact analysis against the substantive standard, not a keyword search.

### Sample flagged entries

- `usfs-notice-2026-001` (HARMFUL) — U.S. Forest Service Notice
- `ceq-notice-2026-001` (SEVERE) — CEQ Notice
- `doj-harvard-antisemitism-2026` (HARMFUL) — DOJ v. Harvard Antisemitism Lawsuit
- `aa-2026-ed-titleix-001` (SEVERE) — ED Title IX Transgender Student Investigations
- `hr1958-119-deporting-fraudsters` (SEVERE) — H.R. 1958 Deporting Fraudsters Act
- `hr7846-119-obstruct-ice` (SEVERE) — H.R. 7846 Criminal Penalties for Obstructing ICE
- Six unidentified legislation stubs (`s-3702-119`, `hr-6397-119`, `hconres-65-119`, etc.)

### Interpretation

Most of these likely ARE correctly coded SEVERE or HARMFUL — the impact is real; the prose just omits explicit continuity terminology. A handful may warrant re-examination against the new standard (e.g., some could be more accurately coded WATCH rather than HARMFUL if the continuity threat is speculative).

### Recommended action

**Targeted prose patch.** For each of the 24 entries, dispatch a narrow AI pass:

> Re-read this entry's impact analysis. If the SEVERE or HARMFUL coding is correct under the cultural-continuity standard, rewrite one or two sentences to explicitly name the continuity threat (generational transmission, demographic survival, lifeway erosion, loss of ceremonial capacity, etc.). If the coding is questionable, flag for human review.

**Cost:** ~24 × $0.10 = **$2.40** Sonnet calls; 30 min runtime.
**Risk:** Very low.

---

## Refinement #2 — Five Primary Communities

### Finding

Of 774 active entries, **758 (97.9%)** already code at least one primary community (Indigenous, African-descendant, Latiné, Asian, or Pacific Islander). Only **16 entries (2.1%)** are coded exclusively with secondary communities (LGBTQ+, women, disabled, immigrant, etc.).

### Sample flagged entries

- `eo-womens-history-2026-001` (HARMFUL) — Women's History Month Proclamation
- `eo-cybercrime-2026-001` (HARMFUL) — EO 14390 Cybercrime
- `fcc-notice-2026-001` (PROTECTIVE) — FCC notice
- `usccr-notice-2026-001` (PROTECTIVE) — USCCR antisemitism meeting
- `doj-harvard-antisemitism-2026` (HARMFUL) — DOJ v. Harvard
- `hhs-kennedy-gac-blocked-2026` (PROTECTIVE) — Gender-affirming care block
- `aa-2026-ed-titleix-001` (SEVERE) — ED Title IX trans investigations
- `aa-2026-ssa-doge-001` (SEVERE) — Social Security DOGE misuse

### Interpretation

Most of these are **intersectional**. For example, the Title IX trans-student investigations affect LGBTQ+ youth who are simultaneously Indigenous, African-descendant, Latiné, Asian, or Pacific Islander. The Women's History Month proclamation affects Black women, Indigenous women, Latina women, AAPI women. The ED Title IX action affects trans youth in all five primary communities.

Under the new standard, each of these 16 entries needs at minimum one primary-community tag added to `c` and a corresponding analytical paragraph added to `I` demonstrating the cultural-continuity angle. This is **intersectional augmentation**, not reclassification.

### Recommended action

**Targeted augmentation.** For each of the 16 entries, dispatch an AI pass:

> This entry affects a secondary community (e.g., LGBTQ+, women, disabled, immigrant). Identify which of the five primary ethnic communities are also affected through the intersectional impact on ethnic members of that secondary community. Add those primary communities to `c`, and add a short PPPT paragraph per community to `I`. Keep the existing secondary-community analysis.

**Cost:** ~16 × $0.15 = **$2.40** Sonnet calls; 20 min runtime.
**Risk:** Low. Intersectional framing is well-established.

---

## Refinement #3 — Diasporic Scope

### Finding

Of 758 entries with at least one primary community coding, **274 analytical fields** across **~300 unique entries** lack diasporic-scope language appropriate to the coded community.

| Primary community | Flagged entries | Missing diasporic framing |
|---|---:|---|
| **Indigenous** (`indigenous`) | 174 | Alaska Native, Native Hawaiian, First Nations, Inuit, Yupik, Aleut |
| **Latiné** (`latine`) | 84 | Mexican, Puerto Rican, Cuban, Dominican, Central American diaspora, Chicano, Chicana |
| **Pacific Islander** (`pacificIslander`) | 11 | Samoan, Tongan, Chamorro, Polynesian, Micronesian, Melanesian, Compact of Free Association (Marshall Islands, Micronesia, Palau) |
| **Asian** (`asianAmerican`) | 5 | South, Southeast, East Asian subgroups (Filipino, Vietnamese, Korean, Chinese, Japanese, Indian, Pakistani, Cambodian, etc.) |
| **African-descendant** (`africanDescendant`) | 0 | Already uses the diasporic frame via the `caribbean` secondary key |

### Important caveat: over-flagging risk

The 174 `indigenous` flags are likely **over-inclusive**. Many are federal actions that affect Indigenous communities generically (e.g., EO 14394 Removing Regulatory Barriers to Affordable Home Construction, TVA Compensation Cap, ICE Minnesota surge). These actions do not require Alaska Native or Native Hawaiian–specific framing because the action itself is not community-subset-specific.

**The rule should be:** a diasporic-scope gap exists only when the action **specifically affects** or **should analytically mention** a particular diasporic subset. Examples where gap is real:

- An EPA action on Arctic resources that doesn't mention Alaska Native subsistence → **real gap**.
- A DHS policy on Pacific visa categories that doesn't mention Compact of Free Association populations → **real gap**.
- A language-access rescission that doesn't mention specific immigrant Asian language communities → **real gap**.

Examples where a flag is a false positive:

- A generic federal DEI rescission that doesn't name Alaska Native specifically → **false positive** (the impact is generic across all Indigenous populations).

### Refined estimate after false-positive filter

After filtering for actions that actually warrant subset-specific framing, the true backlog is probably **80–120 entries**, concentrated in:

- Indigenous entries touching Arctic, Pacific, or island geography (~50)
- Latiné entries touching specific national origins (immigration enforcement, language access, diaspora identity) (~40)
- Pacific Islander entries touching Compact-of-Free-Association populations (~10)
- Asian entries touching specific language / national-origin groups (~5)

### Recommended action

**Two-stage process.**

**Stage A (cheap, automatable): triage scan.** A Sonnet pass that reads each flagged entry and returns one of:
- `FALSE_POSITIVE` — generic action, no subset framing needed.
- `GAP_INDIGENOUS_AK_NH` — real gap, Indigenous entry should mention Alaska Native and/or Native Hawaiian.
- `GAP_LATINE_SPECIFIC` — real gap, Latiné entry should name specific national origins.
- `GAP_AAPI_SPECIFIC` — real gap, Asian entry should name subgroups.
- `GAP_PI_COFA` — real gap, Pacific Islander entry should mention Compact of Free Association populations.

**Cost:** ~300 × $0.05 (Haiku) = **$15**; 45 min runtime.

**Stage B (targeted patching): augmentation.** For each `GAP_*` entry, dispatch a narrow Sonnet pass to rewrite the specific PPPT field with diasporic framing.

**Cost:** ~100 × $0.15 = **$15**; 1 hr runtime.

**Total Refinement #3 cost: ~$30, ~2 hours runtime.**

---

## Taxonomy Normalization (Newly Surfaced)

### Finding

Primary community labels are represented by **2–4 distinct variants each** across the tracker. Examples:

| Canonical community | Variants in use |
|---|---|
| Indigenous | `indigenous`, `Indigenous`, `Indigenous/Tribal`, `Native American` |
| Alaska Native | `alaskaNative`, `Alaska Native`, `Alaska Native communities` |
| Native Hawaiian | `nativeHawaiian`, `Native Hawaiian` |
| African-descendant | `africanDescendant`, `African-descendant`, `African-descendant Communities` |
| Caribbean | `caribbean`, `Caribbean` |
| Latiné | `latine`, `Latiné`, `Hispanic` |
| Asian | `asianAmerican`, `Asian American`, `South Asian`, `Southeast Asian` |
| Pacific Islander | `pacificIslander`, `Pacific Islander`, `Asian American/Pacific Islander` |

### Interpretation

The frontend (`index.html`) and downstream analysis tools face a consistent challenge: the same community shows up under multiple labels. This complicates filter-by-community in the public UI, makes the "9.3:1 SEVERE/HARMFUL vs. PROTECTIVE" law-review statistic harder to compute reliably, and confuses new entries about which label to use.

### Recommended action

**Two canonical forms per community:**

| Canonical camelCase (machine key) | Canonical display form | Purpose |
|---|---|---|
| `indigenous` | Indigenous | Machine key (for `I` object), display for UI |
| `alaskaNative` | Alaska Native | Subset |
| `nativeHawaiian` | Native Hawaiian | Subset |
| `africanDescendant` | African-descendant | Machine key, display |
| `caribbean` | Caribbean | Subset |
| `latine` | Latiné | Machine key, display (é preserved) |
| `asianAmerican` | Asian | Machine key, display simplified |
| `southAsian` | South Asian | Subset |
| `southeastAsian` | Southeast Asian | Subset |
| `eastAsian` | East Asian | Subset |
| `pacificIslander` | Pacific Islander | Machine key, display |
| `nativeHawaiian` (when PI context) | Native Hawaiian | Subset overlap with Indigenous |

**Normalize across the dataset with a script** that maps every variant to its canonical pair.

**Cost:** ~0 (pure string replacement); 15 min runtime.
**Risk:** Low; reversible from backup.

---

## Forward-Facing Changes (Prevent Regression)

### A. Update `pipeline/prompts/entry_generation.txt`

Add requirements to the Sonnet generation prompt:

1. **Severity justification must invoke cultural continuity.** The generated `I` analysis must explicitly explain how the action threatens (or protects) the community's capacity to persist across generations.
2. **Primary-community coding is mandatory.** Every entry must code at least one of the five primary communities (Indigenous, African-descendant, Latiné, Asian, Pacific Islander). If the action primarily affects secondary communities, identify which primary communities are intersectionally affected and code those as well.
3. **Diasporic specificity when relevant.** If the action touches a specific subset (Alaska Native subsistence, Pacific Islander Compact of Free Association, Latiné national-origin groups, Asian language communities), name that subset explicitly.
4. **Use canonical community labels only.** The camelCase keys listed in CLAUDE.md are the ONLY valid values for `c` and `I` keys.

### B. Update `pipeline/prompts/quality_check.txt`

Add validation checks:

1. Does every SEVERE/HARMFUL entry invoke continuity language?
2. Does the entry code at least one primary community?
3. Are community labels from the canonical set?
4. If the action is subset-specific, does the analysis name the subset?

### C. Update `pipeline/data/schema.py`

Require `primary_community` field on all new entries. Add enum validation for community keys against the canonical set.

### D. Update `CLAUDE.md` with the canonical community-label table

Add the two-form canonical table (machine key + display form) as the authoritative list. Deprecate all other variants.

---

## Proposed Execution Order

| # | Step | Cost | Time | Priority |
|---|---|---|---|---|
| 1 | Taxonomy normalization script (replace variants with canonical forms) | $0 | 15 min | **Critical** — do first, everything else builds on canonical taxonomy |
| 2 | Refinement #1 patch (24 entries, add continuity language) | $2.40 | 30 min | High |
| 3 | Refinement #2 augment (16 entries, add primary-community codings) | $2.40 | 20 min | High |
| 4 | Refinement #3 Stage A triage (300 entries, Haiku classification) | $15 | 45 min | Medium |
| 5 | Refinement #3 Stage B patch (~100 real gaps, targeted Sonnet rewrite) | $15 | 1 hr | Medium |
| 6 | Update entry_generation.txt prompt with three refinements | $0 | 15 min | **Critical** — prevents regression |
| 7 | Update quality_check.txt prompt with validation checks | $0 | 10 min | **Critical** |
| 8 | Update schema.py with canonical-label enum | $0 | 30 min | High |
| 9 | Add canonical-label table to CLAUDE.md | $0 | 10 min | High |
| — | **Grand total** | **~$35** | **~3 hr 45 min** | |

---

## Risk Mitigation

- **Back up `data/data.json`** before each batch patch. Use `data/data.json.bak-20260423-pre-refinement-patch` naming.
- **Validate each batch** with the existing `scripts/audit_toolkit.py --full` before the next batch.
- **Spot-check 10 random patched entries** after each batch to confirm the AI rewrote accurately without losing facts.
- **Reversibility:** every batch is revertible from backup within seconds.

---

## Downstream Effects

After harmonization, these analyses become reliable and replicable:

1. **Law review article statistics.** The 9.3:1 SEVERE/HARMFUL vs. PROTECTIVE ratio becomes verifiable per primary community and per diasporic subset.
2. **BGHPN Storymap state-layer.** The muted state-level entries can be classified to primary communities with the canonical taxonomy, enabling clean handoff.
3. **Public UI filtering.** Users can filter the tracker by canonical community without variant-label confusion.
4. **Cultural Heritage Partners integration.** CHP can query the tracker by community and get comprehensive results.
5. **Future pipeline runs.** New entries conform to the canonical standard from the moment of generation.

---

## Open Questions

1. **When do we execute?** The harmonization is reversible and takes under 4 hours of runtime. Schedule tonight, tomorrow morning, or as a deliberate "reset + audit" weekend?
2. **Spot-check sample size.** Is 10 per batch enough, or should we have Kiran spot-check more carefully?
3. **Should we archive the pre-harmonization data.json as a permanent reference point** so the tracker's pre- and post-harmonization state can be compared for any published law review statistics?

---

*Memo prepared 2026-04-23. Execute after review and approval.*
