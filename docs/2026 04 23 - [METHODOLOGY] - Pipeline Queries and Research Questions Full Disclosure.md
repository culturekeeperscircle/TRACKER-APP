# TCKC Threat Tracker — Research Methodology: Full Query Disclosure

**Purpose.** Complete transparency on every query, search term, and research question the automated pipeline uses to find and generate entries. For QA, audit, and external review.

**Prepared:** 2026-04-23

---

## The Canonical Research Question (locked 2026-04-23)

All tracker work answers the same question, whether machine-generated or human-drafted:

> **Which laws and policies from [GOVERNMENT ENTITY] will severely harm the cultural resources (People, Places, Practices, and Treasures) paramount to the cultural continuity of [CULTURAL COMMUNITY], moderately harm those same cultural resources, or protect those same cultural resources?**

Where:

- **[GOVERNMENT ENTITY]** is a U.S. federal entity identified by the tracker's source pipeline: White House, federal agency, Congress, federal court, or international body.
- **[CULTURAL COMMUNITY]** is one of the **five primary ethnic communities** the tracker covers:
  1. **Indigenous** (Native American nations, Alaska Native, Native Hawaiian)
  2. **African-descendant** (African American, Afro-Caribbean, Afro-Latiné, African diaspora)
  3. **Latiné** (Latin American, Chicano, Hispanic, Latinx)
  4. **Asian** (Asian American, AANHPI, South Asian, Southeast Asian, East Asian)
  5. **Pacific Islander** (Native Hawaiian, Samoan, Tongan, Chamorro, Polynesian, Micronesian, Melanesian)

The three valid answers are **SEVERE**, **HARMFUL**, and **PROTECTIVE** (with **WATCH** for developing threats). Severity is pegged to impact on **cultural continuity** — the community's capacity to persist as a distinct cultural entity across generations — along one of the four PPPT resource dimensions (People, Places, Practices, Treasures).

Items may touch secondary communities (LGBTQ+, immigrants, women, disabled, faith, environmental-justice, federal employees, etc.). Secondary communities are coded as additional affected communities; the canonical analytical focus stays on the five ethnic communities above.

The canonical question is now embedded directly in the Claude Haiku screening prompt (`pipeline/prompts/relevance_screening.txt`) and in every downstream analytical step. See Stage 3 below for the full prompt.

---

## The Pipeline Has Four Research Stages

```
Stage 1: SOURCE FETCH     → Each database gets its own search strategy
Stage 2: KEYWORD FILTER    → 170+ keywords narrow the pool
Stage 3: AI SCREENING      → Claude Haiku answers "is this relevant?" against an explicit 3-research-question frame
Stage 4: AI GENERATION     → Claude Sonnet writes the entry to a strict schema
Stage 5: AI VALIDATION     → Claude Haiku quality-checks the entry before write
```

What follows documents every query, prompt, and filter at every stage.

---

## Stage 1 — Database Search Strategies

### Database 1: Federal Register (federalregister.gov)

- **Search approach:** **No search query.** The connector fetches ALL new Federal Register documents published since the last successful pipeline run, up to **1,000 documents per run**.
- **What is fetched:** Rules, proposed rules, notices, presidential documents, agency orders.
- **Filter applied locally:** Keyword match (see Stage 2).
- **Rationale:** Federal Register is low volume and every entry is a primary-source government document; easier to fetch everything and filter.
- **Risk:** On a busy week (≥1,000 documents/day), post-1,000 items get dropped silently.

### Database 2: Congress.gov (api.congress.gov)

- **Search approach:** Subject-based filter. The connector fetches bills whose subject matches one of **12 congressional subjects:**
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
- **Scope:** Up to **500 bills per run**.
- **Tracked bill numbers:** A manual list (`TRACKED_BILLS` in pipeline/config.py) of specific bill numbers that always pass. Includes Black History, Filipino American, Native Hawaiian, and heritage-month resolutions.
- **Risk:** Bills filed under other subjects (e.g., "Health" or "Taxation") are invisible to the pipeline even when they directly affect cultural communities.

### Database 3: CourtListener (courtlistener.com)

- **Search approach:** 13 keyword queries. Each runs independently; results merge.
  1. `cultural resources historic preservation heritage`
  2. `tribal sovereignty sacred sites NAGPRA indigenous`
  3. `national monument Antiquities Act preservation`
  4. `environmental justice civil rights Title VI discrimination`
  5. `immigration deportation asylum TPS DACA refugee`
  6. `NEA NEH arts funding Smithsonian IMLS`
  7. `treaty rights Native American tribal consultation`
  8. `African American civil rights racial equity HBCU`
  9. `Latino Hispanic farmworker immigrant community`
  10. `Asian American Pacific Islander AAPI hate crime`
  11. `cultural practice traditional knowledge language preservation`
  12. `museum library school university cultural programming education`
  13. `foodways folk arts cultural arts celebration parade festival`
- **Scope:** Up to **20 opinions per query per run** = 260 opinions max per run.
- **What is fetched:** Federal court opinions (district, circuit, Supreme).

### Database 4: NewsAPI (newsapi.org)

- **Search approach:** 11 Boolean phrase queries. Each query runs independently; results merge.
  1. `"cultural resources" OR "historic preservation" OR "cultural heritage" OR "national monument"`
  2. `"tribal sovereignty" OR "sacred sites" OR NAGPRA OR "indigenous rights" OR "Native American"`
  3. `"environmental justice" OR "civil rights" OR "racial equity" OR "Title VI" OR discrimination`
  4. `NEA OR NEH OR Smithsonian OR IMLS OR "arts funding" OR "cultural institution"`
  5. `immigration OR deportation OR "refugee policy" OR DACA OR TPS OR asylum`
  6. `"African American" OR "Black community" OR HBCU OR "racial justice" OR reparations`
  7. `"Latino" OR "Hispanic" OR "farmworker" OR "immigrant community" OR Latinx`
  8. `"Asian American" OR "Pacific Islander" OR AAPI OR "hate crime" OR "anti-Asian"`
  9. `"cultural practice" OR "language preservation" OR "traditional knowledge" OR "folk art"`
  10. `foodways OR "folk arts" OR "cultural arts" OR parade OR "cultural festival" OR celebration`
  11. `museum OR library OR university OR school OR "cultural programming" OR "cultural center"`
- **Scope:** Up to **20 articles per query per run** = 220 articles max per run.
- **Outlet coverage:** NewsAPI's free tier indexes ~150,000 sources but truncates article content and limits historical depth.

---

## Stage 2 — Keyword Relevance Filter (Applied to Federal Register)

The 170+ keyword list is applied to Federal Register document titles and abstracts. A document passes if any one keyword matches. Keywords grouped by category:

**Cultural heritage & preservation.** cultural resource, cultural heritage, cultural practice, cultural property, cultural tradition, cultural identity, intangible heritage, historic preservation, heritage, monument, museum, memorial, archaeological, sacred site, burial ground, cemetery, historic site, NAGPRA, NHPA, Section 106, National Register, historic district, Antiquities Act, historic landmark, World Heritage.

**Indigenous / Tribal.** tribal, indigenous, Native American, Alaska Native, Native Hawaiian, treaty, sovereignty, reservation, BIA, Indian Affairs, tribal consultation, tribal land, First Nations, aboriginal.

**African-descendant.** African American, Black community, Black history, civil rights, racial justice, racial equity, reparations, Juneteenth, historically Black, HBCU, African diaspora, Afro-.

**Latiné / Hispanic.** Latino, Latina, Latiné, Latinx, Hispanic, Chicano, Chicana, farmworker, bracero, Spanish-speaking, Latin American.

**Asian American / Pacific Islander.** Asian American, Pacific Islander, AAPI, AANHPI, Chinese American, Japanese American, Korean American, Filipino, Vietnamese, South Asian, Southeast Asian, Polynesian.

**Other ethnic / identity communities.** LGBTQ, disability, women, Muslim, Jewish, Sikh, Hindu, Arab American, Middle Eastern, immigrant community, refugee community, Garifuna, Tamil, Tamil American.

**Heritage months & recognition resolutions.** heritage month, history month, recognition month, awareness month, National Day of, commemorat-, designat-, Black History, African American History, Filipino American History, Native Hawaiian, Asian Pacific American Heritage, AANHPI Heritage, Hispanic Heritage, Arab American Heritage, Indigenous Peoples Day, Juneteenth National Independence Day.

**Specific bill topics.** official language, English-only, national language, language access, multilingual, bilingual, interpreter, translation, reproductive rights, reproductive health, contraception, abortion, maternal health, birth equity, worker rights, labor rights, wage theft, workplace safety, fair scheduling, domestic workers, gig workers, Kennedy Center, National Museum, Smithsonian museum, African American Museum, Latino Museum, Women's History Museum, Asian Pacific American, American Indian Museum.

**Civil rights & equity.** DEI, environmental justice, Title VI, discrimination, equity, hate crime, civil liberties, equal protection, voting rights.

**Immigration.** immigration, refugee, asylum, deportation, TPS, visa, ICE, DACA, naturalization, USCIS, border, migrant.

**Environment & land.** climate change, EPA, NEPA, environmental review, conservation, endangered species, public lands, national park, wilderness, clean water, clean air, environmental protection.

**Arts, education, cultural institutions.** education, NEA, NEH, Smithsonian, library, arts funding, public broadcasting, CPB, PBS, NPR, IMLS, arts community, cultural institution, humanities, folk art, language preservation, oral history, traditional knowledge, arts education, creative workforce, cultural funding, arts grant, National Endowment, Corporation for Public Broadcasting.

**Cultural life.** foodways, landways, folk arts, cultural arts, performing arts, parade, celebration, festival, ceremony, cultural event, cultural programming, cultural center, community center.

**Education & knowledge institutions.** school, university, college, museum, library, archive, curriculum, Title I, Title IX, student, scholarship, tribal college, community college, head start.

---

## Stage 3 — AI Relevance Screening (Claude Haiku 4.5)

This is the **research-questions frame** the pipeline uses. Claude Haiku receives the following prompt for every item that survives Stage 2. (Note the prompt's framing: it tells the AI what questions to hold.)

### The full screening prompt

```
You are a cultural resource policy analyst for The Culture Keepers Circle.
Your task is to determine if a government action, court case, or news item
is relevant to the TCKC Cultural Resource Threat Tracker.

The tracker monitors ALL U.S. government actions from ANY agency that affect:

- Cultural resources, cultural heritage, cultural practices, cultural property,
  and cultural identity
- Historic preservation, monuments, museums, archaeological sites, sacred sites
- Ethnic communities: Indigenous/Tribal, African-descendant, Latiné/Hispanic,
  Asian American, Pacific Islander, Native Hawaiian, Alaska Native,
  immigrant/refugee communities
- Civil rights, racial justice, equity, anti-discrimination, voting rights,
  hate crimes
- Immigration, asylum, deportation, refugee policy, TPS, DACA, visa policy
- Environmental justice, environmental protection, public lands, conservation
- Arts/education/humanities funding (NEA, NEH, Smithsonian, IMLS, CPB, libraries)
- Language preservation, traditional knowledge, oral history, folk arts,
  intangible heritage
- Foodways, landways, cultural arts, parades, celebrations, festivals, ceremonies
- Schools, universities, museums, libraries, archives, cultural centers,
  cultural programming

ALWAYS mark as RELEVANT (high confidence) if the item involves ANY of:

- Heritage month resolutions or cultural recognition
- Official language / English-only legislation (mark as HARMFUL)
- Language access, multilingual services, interpreter/translation rights
- Reproductive rights and health legislation
- Worker rights, labor protections, domestic worker/gig worker bills
- Cultural institution legislation
- Immigration reform, immigrant protections, DACA, TPS, asylum, deportation
- Voting rights, election access, democracy protection
- Arts education, creative workforce, cultural funding
- Any bill or resolution naming a specific ethnic, racial, or cultural community

Mark as relevant if the action could directly or indirectly impact ANY ethnic
community or cultural heritage/practice in the United States.

Analyze this item and determine relevance: {ITEM_DATA}

Respond with ONLY this JSON:
{
  "relevant": true or false,
  "confidence": 0.0 to 1.0,
  "category": "executive_actions" | "agency_actions" | "legislation"
              | "litigation" | "other_domestic" | "international",
  "threat_level": "SEVERE" | "HARMFUL" | "PROTECTIVE",
  "brief_reason": "one sentence explaining why this is or isn't relevant"
}
```

Only items where `relevant: true` AND `confidence >= 0.6` advance to Stage 4.

### The three implicit research questions

Embedded in the prompt above, the AI is actually asking three questions per item:

1. **Is this a U.S. federal government action?** (Executive, congressional, judicial, or administrative.)
2. **Does it touch one or more of 27 cultural communities OR one of 10 cultural-resource domains?** (The 27 communities + 10 domains are listed in the prompt.)
3. **What is the directional impact?** (SEVERE harm / HARMFUL / PROTECTIVE.)

If yes to #1, yes to #2, and the AI can code #3 with ≥60% confidence, the item proceeds.

---

## Stage 4 — AI Entry Generation (Claude Sonnet 4.6)

Items that pass screening get a full entry generated by Claude Sonnet, following a strict schema. The prompt:

- Specifies **exact ID formats per category** (`eo-{number}` for executive orders, `hr-{number}-{congress}` for House bills, etc.)
- Requires **500–1500 word description** with concrete legal mechanisms, timelines, funding amounts, and impacts
- Requires **Impact-by-Community (PPPT) analysis** for 2–4 affected communities, each community with 4 fields (People, Places, Practices, Treasures), each field 150–300 words
- Specifies **threat-level guidance** for common bill types:
  - Heritage-month / cultural-recognition → **PROTECTIVE**
  - English-only / official-language → **HARMFUL**
  - Immigration-protection bills → **PROTECTIVE**
  - Anti-immigration-enforcement bills → **HARMFUL or SEVERE**
  - Arts/education funding cuts → **SEVERE**
  - Reproductive-rights protections → **PROTECTIVE**
  - Voting-rights protections → **PROTECTIVE**
- Requires **source URL** that must be the official government/court URL, not a news article
- Pulls **two existing entries** from the same category and threat level as few-shot examples

### Critical rules enforced in the prompt

1. Only include verified facts. Do not hallucinate citations, dates, or numbers.
2. Impact analysis must be specific. Name real places, organizations, programs.
3. Each PPPT field must be 150–300 words.
4. Threat level must accurately reflect the action's impact.

---

## Stage 5 — AI Quality Validation (Claude Haiku 4.5)

Generated entries get a validation pass asking:

1. Does threat level match the impact described?
2. Are community impacts specific (real names) not generic?
3. Are legal mechanisms correctly cited?
4. Is date in YYYY-MM-DD format?
5. Does administration match the date?
6. Are all required schema fields present?
7. Is the title HTML color span correct for the threat level?
8. Is description ≥500 words?
9. Is each PPPT field ≥150 words?
10. Is the source URL an official government/court URL?

---

## Cross-Reference with "Credible News Sources" — The Honest Answer

You asked specifically about credible news-source cross-referencing. Here is what the data actually shows:

### Top 30 source domains cited in the 755 existing entries

| Rank | Domain | Entries | Type |
|---:|---|---:|---|
| 1 | whitehouse.gov | 172 | Primary government |
| 2 | congress.gov | 166 | Primary government |
| 3 | federalregister.gov | 105 | Primary government |
| 4 | courtlistener.com | 84 | Primary court records |
| 5 | state.gov | 40 | Primary government |
| 6 | supremecourt.gov | 19 | Primary court |
| 7 | dhs.gov | 15 | Primary government |
| 8 | nps.gov | 11 | Primary government |
| 9 | govtrack.us | 10 | Legislative tracker |
| 10 | api.congress.gov | 9 | Primary government |
| 11 | noaa.gov | 7 | Primary government |
| 12 | blm.gov | 7 | Primary government |
| 13–20 | doi.gov, justice.gov, hhs.gov, ed.gov, epa.gov, archives.gov, usda.gov, arts.gov | 4–6 each | Primary government |
| 21 | ice.gov | 3 | Primary government |
| 22 | si.edu | 3 | Federal cultural institution |
| 23 | loc.gov | 3 | Federal cultural institution |
| 24 | imls.gov | 2 | Primary government |
| 25 | **19thnews.org** | 2 | Independent news |
| 26 | sf.funcheap.com | 2 | Local event listings |
| 27 | **artsjournal.com** | 2 | Cultural journalism |
| 28 | ohchr.org | 2 | UN human rights |
| 29 | ustr.gov | 2 | Primary government |
| 30 | worldbank.org | 2 | International body |

### The uncomfortable finding

**The tracker is overwhelmingly a primary-source tool, not a news-aggregation tool.** Of 755 entries, only a small handful cite news outlets. News coverage enters the pipeline as a SIGNAL for Claude to search for the underlying government action; once found, the government action becomes the citation, and the news lead gets dropped.

### What this means for "credibility"

**Strengths.**
- Entries cite primary documents: executive orders, Federal Register entries, court opinions, agency rulemakings. This is the highest possible source tier.
- No dependence on paywalled outlets.
- Citations survive even if a news site deletes coverage.

**Gaps.**
- **Leaked or reported-but-not-yet-published actions** (agency memos, draft guidance, pre-publication EOs) get missed until they hit a primary source.
- **Press-conference / informal statements** by agency heads are invisible.
- **Investigative-journalism scoops** (ProPublica, NYT, WaPo, The Guardian, 19thnews) are not systematically triangulated.
- **Community-outlet reporting** (The Root, Indian Country Today, Colorlines, Prism Reports) appears sporadically.

### News outlets the pipeline SHOULD be ingesting systematically (currently absent or sporadic)

**Investigative / accountability journalism.**
- ProPublica
- The Intercept
- Reveal from Center for Investigative Reporting
- Mother Jones
- Democracy Docket
- 19thnews (The 19th)
- Prism Reports
- Capital B (Black journalism)

**Mainstream wire.**
- Associated Press (AP)
- Reuters

**Opinion pages / long-form.**
- New York Times (paywalled; News API free tier has limited access)
- Washington Post
- The Atlantic
- The New Yorker

**Community-based.**
- Indian Country Today / ICT News
- The Root
- Colorlines / Race Forward
- Rafu Shimpo (Japanese American)
- Hyphen Magazine (Asian American)
- Haitian Times
- El Nuevo Día / La Opinión (Latiné)

**Cultural-heritage specialty.**
- ArtsJournal
- Art Newspaper
- Inside Higher Ed
- Chronicle of Higher Education
- ArtNet News
- Hyperallergic

**Legal / policy.**
- Law360
- Reuters Legal
- Bloomberg Law
- Just Security
- Lawfare

---

## Gaps in the Current Methodology

### A. Source gaps
1. **No whitehouse.gov/presidential-actions scraper.** Presidential actions appear on whitehouse.gov before Federal Register publication. 172 whitehouse.gov citations in existing data were added manually.
2. **No agency-press-release scrapers.** Significant pronouncements (ED, DOJ, HHS, DHS, DOI, EPA) often appear in press releases before Federal Register.
3. **No investigative-news ingest.** ProPublica, 19thnews, The Intercept, Democracy Docket have no systematic connector.
4. **No community-outlet ingest.** Indian Country Today, The Root, Prism Reports, etc. not systematically fetched.

### B. Query gaps
1. **CourtListener has 13 queries; should have ~20 to cover 27 communities + 10 domains.** Missing: LGBTQ rights cases, reproductive rights cases, voting rights cases, disability rights cases, faith community cases, labor rights cases.
2. **NewsAPI has 11 queries; should have ~16 to cover same ground.** Same gaps as CourtListener.
3. **No queries for Trump-II-specific signature terms:** "DEI rollback," "Stop WOKE," "birthright citizenship," "sanctuary city," "anti-woke," "America First," "MAGA."
4. **Federal Register fetches up to 1,000 docs per day unfiltered.** On busy publication days, post-1,000 items are invisible to the keyword filter.

### C. Screening gaps
1. **AI screening has a 60% confidence threshold.** Items rated 40–59% confident are discarded without review. The floor is aggressive.
2. **No re-screening of borderline items.** Once discarded, an item is gone.

### D. Workflow gaps
1. **No manual-entry override.** Items Prince or a staffer notice via Twitter, journal article, or conversation have no clean path into the tracker. They must be retrofitted after the fact.
2. **No triangulation check.** An action is never required to appear in ≥2 sources before being coded. A single Federal Register notice or news article is enough.
3. **No periodic completeness audit.** The pipeline doesn't cross-check itself against external trackers (ACLU, Democracy Docket, Brennan Center, Just Security, FAS EO Tracker) to find items it missed.

---

## Remediation Options (Priority-Ordered)

### Immediate (this week)

1. **Expand CourtListener queries** from 13 to 20. Add: LGBTQ rights, reproductive rights, voting rights, disability rights, faith communities, labor rights, Trump II EO challenges. ~30 minutes of code change.
2. **Expand NewsAPI queries** from 11 to 16. Same categories. ~30 minutes.
3. **Add Trump-II signature-term queries** to both CourtListener and NewsAPI: `"DEI rollback" OR "Stop WOKE"`, `"birthright citizenship"`, `"sanctuary" OR "ICE enforcement"`, `"anti-woke" OR "MAGA"`. ~15 minutes.

### Short-term (next 2–4 weeks)

4. **Build a whitehouse.gov/presidential-actions scraper.** 4–6 hours. Eliminates 1–3 day lag on EOs.
5. **Build an agency-press-release scraper** for ED, DOJ, HHS, DHS, DOI, EPA. ~12 hours total.
6. **Add a ProPublica / 19thnews / The Intercept / Democracy Docket ingest** via their RSS feeds or APIs. ~6 hours.

### Medium-term (next quarter)

7. **Triangulation requirement.** Implement a `triangulated: true/false` field; optional requirement that SEVERE-coded items appear in ≥2 sources.
8. **Weekly external-tracker audit.** Automated cross-check against ACLU Trump 2.0, Democracy Docket, FAS EO Tracker, Brennan Center, Just Security Litigation Tracker.
9. **Community-outlet ingest.** Indian Country Today, The Root, Capital B, Prism Reports, Haitian Times.

### Long-term (strategic)

10. **Re-run the full pipeline over Jan 19, 2025 → today** with expanded queries, raised cap, and triangulation (see `2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md`).

---

## TL;DR

- **Where the pipeline looks:** 4 databases (Federal Register, Congress.gov, CourtListener, NewsAPI) with the queries listed above.
- **What research questions it asks:** The Claude Haiku screening prompt frames three questions: federal government action? touches a cultural community or resource domain? directional impact? Items passing all three advance.
- **How it cross-references news:** Minimally. News outlets provide signals; once Claude finds the underlying government document, the news citation is dropped. Only ~20 entries out of 755 cite news sources directly.
- **What's missing:** LGBTQ, reproductive rights, voting rights, disability, faith, labor queries on CourtListener and NewsAPI. No whitehouse.gov or agency-press-release ingest. No systematic investigative-news or community-outlet coverage. No triangulation check. No periodic self-audit against external trackers.

The pipeline is rigorous about primary-source citation. It is less rigorous about completeness and news-source cross-validation. The backfill + methodology expansion in `2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md` addresses these gaps.

---

*Methodology disclosure prepared 2026-04-23. Share with partners, funders, law review reviewers, and journalists who need to evaluate the tracker's research basis.*
