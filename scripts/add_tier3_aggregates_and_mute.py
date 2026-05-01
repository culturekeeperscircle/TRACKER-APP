#!/usr/bin/env python3
"""Tier 3: roll remaining HIGH items into aggregates + state/municipal mute audit.

Operations:
1. Add hearth-act-approvals-2025-2026 aggregate (7 PROTECTIVE Tribal
   Leasing Ordinance approvals under the HEARTH Act)
2. Add federal-acknowledgment-petitions-2025-2026 aggregate (9 WATCH
   Federal Acknowledgment process notices)
3. Update nagpra-roundup-2026-03 with 2 additional notices found in
   the audit (Gilcrease Museum + New York State Parks transfer)
4. Update alaska-oil-gas-leasing-pivot-2025-2026 with the 4 component
   FR document URLs that were named but not URL-listed
5. Mute lit-2026-ks-sb244-001 (Kansas SB 244 ACLU challenge) per the
   tracker's federal-actor-only coding policy. The entry references
   only a "Kansas district court" with no federal-court markers, no
   42 U.S.C. 1983 citation, no D. Kan. (federal) venue indicator,
   suggesting state-court litigation against state legislation. Per
   CLAUDE.md, state/local actions slip through must be muted with
   reason and date, never deleted.
"""
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-tier3-aggregates"
)

CLUSTER_DATA = json.loads(open('/tmp/tier3_clusters.json').read())


def make_hearth_act_aggregate(items):
    items_sorted = sorted(items, key=lambda x: x['fr_action'].get('publication_date',''))
    n = len(items_sorted)
    body = []
    body.append(f"<b>AGGREGATE.</b> Between April 17, 2025 and December 15, 2025, the Bureau of Indian Affairs published in the Federal Register {n} approvals of tribal leasing ordinances under the Helping Expedite and Advance Responsible Tribal Home Ownership Act of 2012 (HEARTH Act, Public Law 112-151, codified at 25 U.S.C. 415). Each HEARTH Act approval grants the participating tribal nation autonomous authority to execute leases of tribal trust lands without further federal Secretarial approval for each transaction. Per the TCKC federal-actor coding convention, these routine PROTECTIVE federal approvals are aggregated rather than coded individually.<br><br>")
    body.append("<b>HEARTH ACT CONTEXT.</b> The HEARTH Act amends the Indian Long-Term Leasing Act of 1955 (25 U.S.C. 415) to authorize federally recognized Indian tribes to enter into surface leases of tribal trust lands without further Secretarial approval, provided the tribe has adopted leasing regulations approved by the Secretary. The Act applies to business, residential, agricultural, recreational, religious, and educational leases (other than mineral leases). Approval of a tribe's leasing regulations is the operative federal action; subsequent leases proceed under tribal-government authority alone.<br><br>")
    body.append(f"<b>2025 APPROVALS LIST ({n} ordinances).</b><br>")
    for item in items_sorted:
        fr = item['fr_action']
        body.append(f"- <b>{fr.get('publication_date','')}</b>: {fr.get('title','')[:200]} (Federal Register {fr.get('document_number','')})<br>")
        body.append(f"  <a href=\"{fr.get('html_url','')}\">{fr.get('html_url','')}</a><br>")
    body.append("<br><b>SOURCES.</b><br>")
    body.append("HEARTH Act of 2012, Public Law 112-151, 25 U.S.C. 415. Federal Register publication of each approval is the primary source for that approval. Aggregate URLs listed above.<br>")
    body.append("Related tracker entries: bia-tribal-self-governance-fy2027-deadline-2026; doi-southern-ute-tera-2026; ancsa-conveyances-2026; indian-gaming-compacts-2025-2026 (parallel tribal-sovereignty federal-actor PROTECTIVE patterns).")

    return {
        "i": "hearth-act-approvals-2025-2026",
        "t": "Aggregate Analysis",
        "n": f"Aggregate: BIA HEARTH Act Approvals of Tribal Leasing Ordinances, April-December 2025 ({n} ordinances)",
        "T": f'<span style="color: #065F46;">Aggregate Analysis:</span> BIA Approvals of {n} Tribal Leasing Ordinances Under the HEARTH Act of 2012, April-December 2025',
        "s": "HEARTH Act approvals 2025",
        "d": "2025-12-15",
        "a": "Trump II",
        "A": ["DOI", "BIA"],
        "S": f"Active aggregate. {n} HEARTH Act tribal leasing ordinance approvals between April 17, 2025 and December 15, 2025. Aggregate per TCKC federal-actor coding convention.",
        "L": "PROTECTIVE",
        "D": "".join(body),
        "I": {
            "indigenous": {
                "people": f"Tribal members of the {n} federally recognized Tribes whose leasing ordinances were approved benefit from increased tribal-government authority over leases of tribal trust lands. The approving Tribes include the Dry Creek Rancheria Band of Pomo Indians (California), the Shivwits Band of Paiutes (Utah), the Jamul Indian Village of California, the Choctaw Nation of Oklahoma, the Squaxin Island Tribe (Washington), the Shawnee Tribe (Oklahoma), and others. Tribal-government departments responsible for land-management gain operating authority. The HEARTH Act framework demonstrates a federal-statutory pathway for tribal sovereignty over land use.",
                "places": f"Tribal trust lands across {n} reservations and trust-land holdings benefit from streamlined leasing authority. The lands include Dry Creek Rancheria Tribal Trust Land in Sonoma County, California; Shivwits Reservation in southern Utah; Jamul Indian Village land in San Diego County, California; Choctaw Nation lands across southeastern Oklahoma; Squaxin Island Reservation in Washington State; Shawnee Tribe lands in northeastern Oklahoma; and others. Cultural-resource sites within these lands face protective tenure under tribal-government leasing-ordinance frameworks.",
                "practices": "Tribal-government land-management practice expands as Tribes assume per-transaction approval authority for surface leases. Tribal cultural-resource-management practices, including consultation with Tribal Historic Preservation Officers, proceed under tribal-government leasing-ordinance frameworks. Tribal economic-development practices benefit from reduced federal-permitting timelines.",
                "treasures": "The HEARTH Act statutory framework, accumulated since 2012, is itself a cultural-policy treasure that protects tribal sovereignty over land use. Each approved leasing ordinance is an institutional treasure of the participating Tribe. Cultural-resource sites within tribal trust lands face protection through tribal-government leasing-ordinance frameworks rather than through federal Secretarial approval timelines."
            }
        },
        "c": ["Indigenous", "All Communities"],
        "U": items_sorted[0]['fr_action'].get('html_url','') if items_sorted else "https://www.federalregister.gov/",
        "_source": "manual",
        "_isAggregate": True,
    }


def make_fed_acknowledgment_aggregate(items):
    items_sorted = sorted(items, key=lambda x: x['fr_action'].get('publication_date',''))
    n = len(items_sorted)
    body = []
    body.append(f"<b>AGGREGATE.</b> Between September 2025 and February 2026, the Bureau of Indian Affairs published in the Federal Register {n} notices related to the federal acknowledgment process under 25 CFR Part 83. The notices include receipt of documented petitions for federal acknowledgment as an American Indian Tribe, receipt of requests for authorization to re-petition, and the annual Indian Entities Recognized by and Eligible To Receive Services From the United States Bureau of Indian Affairs list. Per the TCKC federal-actor coding convention, these process notices are aggregated rather than coded individually.<br><br>")
    body.append("<b>FEDERAL ACKNOWLEDGMENT CONTEXT.</b> Federal acknowledgment is the formal recognition by the United States that a tribal entity exists as a sovereign Indian Tribe with a government-to-government relationship to the federal government. The 25 CFR Part 83 process governs petitions for federal acknowledgment, with criteria including continuous community existence, political authority, and descent from a historical Indian Tribe. Federal acknowledgment carries fundamental implications for tribal access to federal services, sovereignty, treaty rights, and cultural-continuity protections. Petition processing typically requires several years and substantial tribal-government documentation work.<br><br>")
    body.append("<b>TRACKER POSTURE.</b> Federal acknowledgment process notices receive a WATCH classification because their cultural-resource impact depends on the substantive outcome of the petition review (acknowledgment, denial, or remand). Receipt-of-petition notices initiate the process. Re-petition notices provide a second pathway for previously denied applicants. The annual Indian Entities list documents the operative recognized-tribes universe. Each receipt or re-petition notice is a step toward potential full federal acknowledgment, which would convert the tracker classification from WATCH to PROTECTIVE.<br><br>")
    body.append(f"<b>2025-2026 AGGREGATE LIST ({n} notices).</b><br>")
    for item in items_sorted:
        fr = item['fr_action']
        body.append(f"- <b>{fr.get('publication_date','')}</b>: {fr.get('title','')[:200]} (Federal Register {fr.get('document_number','')})<br>")
        body.append(f"  <a href=\"{fr.get('html_url','')}\">{fr.get('html_url','')}</a><br>")
    body.append("<br><b>SOURCES.</b><br>")
    body.append("Federal acknowledgment regulations at 25 CFR Part 83. Federal Register publication of each notice is the primary source. Aggregate URLs listed above.<br>")
    body.append("Related tracker entries: chinook-nation-cert-denied-2026 (parallel federal-acknowledgment harm; SCOTUS denial of cert in Chinook Indian Nation case); v2026-indigenous-cultural-threat-analysis.")

    return {
        "i": "federal-acknowledgment-petitions-2025-2026",
        "t": "Aggregate Analysis",
        "n": f"Aggregate: BIA Federal Acknowledgment Process Notices, September 2025 to February 2026 ({n} notices)",
        "T": f'<span style="color: #6B7280;">Aggregate Analysis:</span> BIA Federal Acknowledgment Process Notices, September 2025 to February 2026 ({n} notices). Documents Petitions, Re-Petitions, and Annual Recognized-Tribes List Under 25 CFR Part 83',
        "s": "Federal Acknowledgment petitions 2025-2026",
        "d": "2026-02-06",
        "a": "Trump II",
        "A": ["DOI", "BIA"],
        "S": f"Active aggregate. {n} federal acknowledgment process notices between September 2025 and February 2026. Aggregate per TCKC federal-actor coding convention. Each notice's substantive outcome will be tracked individually as decisions issue.",
        "L": "WATCH",
        "D": "".join(body),
        "I": {
            "indigenous": {
                "people": "Tribal members of the petitioning groups whose recognition requests are reflected in this aggregate carry forward multi-generational federal-acknowledgment work. Petitioning groups include those whose names appear in the Federal Register notices; specific identities are detailed in each component notice. Tribal-government leadership, tribal-genealogy specialists, and tribal-cultural-affiliation researchers in petitioning groups invest sustained labor in producing the documentation 25 CFR Part 83 requires. Successful petitioners gain access to federal services, sovereignty rights, and federal-trust protections; unsuccessful petitioners face continued non-recognition.",
                "places": "Petitioning groups' historical territories, ceremonial sites, ancestral burial places, and traditional-subsistence landscapes face sustained pressure during the multi-year acknowledgment process. Without recognition, tribes hold no federal-trust authority over these places and rely on state-level cultural-resource protections and broader civil-society advocacy. The annual Indian Entities list documents the operative-recognized-tribes universe.",
                "practices": "Federal acknowledgment process practice itself constitutes a form of cultural continuity work. Petitioning groups maintain language, ceremonies, governance, and intergenerational transmission practices over decades while documenting these practices for federal review. The 25 CFR Part 83 process operates as a formal acknowledgment of practices that the petitioning groups have maintained continuously.",
                "treasures": "Tribal-government documentation produced during the federal acknowledgment process, including genealogical records, cultural-affiliation documentation, oral history collections, and treaty-and-historic-record research, constitutes a cultural treasure of the petitioning group regardless of recognition outcome. The 25 CFR Part 83 framework itself, accumulated since 1978, is a federal-statutory cultural-policy treasure whose operating practice includes both protective and harm dimensions."
            }
        },
        "c": ["Indigenous", "All Communities"],
        "U": items_sorted[0]['fr_action'].get('html_url','') if items_sorted else "https://www.federalregister.gov/",
        "_source": "manual",
        "_isAggregate": True,
    }


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    # 1. Add HEARTH Act aggregate
    hearth = make_hearth_act_aggregate(CLUSTER_DATA['clusters']['hearth_act'])
    if em_dash in json.dumps(hearth, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash in HEARTH aggregate")
    if not any((e.get('id') or e.get('i')) == hearth['i'] for e in data['agency_actions']):
        data['agency_actions'].append(hearth)
        print(f"  ADD: {hearth['i']} ({len(CLUSTER_DATA['clusters']['hearth_act'])} HEARTH approvals)")

    # 2. Add Federal Acknowledgment aggregate
    fed_ack = make_fed_acknowledgment_aggregate(CLUSTER_DATA['clusters']['fed_recognition'])
    if em_dash in json.dumps(fed_ack, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash in fed-ack aggregate")
    if not any((e.get('id') or e.get('i')) == fed_ack['i'] for e in data['agency_actions']):
        data['agency_actions'].append(fed_ack)
        print(f"  ADD: {fed_ack['i']} ({len(CLUSTER_DATA['clusters']['fed_recognition'])} acknowledgment notices)")

    # 3. Update nagpra-roundup-2026-03 with 2 additional notices
    nagpra_extras = []
    for r in CLUSTER_DATA['nagpra']:
        nagpra_extras.append(r['fr_action'])
    if nagpra_extras:
        for entry in data['agency_actions']:
            if (entry.get('id') or entry.get('i')) == 'nagpra-roundup-2026-03':
                if "[UPDATE 2026-04-30 with audit-discovered notices]" in entry.get('D',''):
                    print("  SKIP: nagpra-roundup-2026-03 already updated")
                    break
                add_block = f"<br><br><b>UPDATE 2026-04-30.</b> The 2026-04-30 agency-coverage audit surfaced {len(nagpra_extras)} additional March 2026 NAGPRA notices not initially captured in the aggregate [UPDATE 2026-04-30 with audit-discovered notices].<br><br>"
                add_block += f"<b>ADDITIONAL MARCH 2026 NOTICES.</b><br>"
                for fr in sorted(nagpra_extras, key=lambda x: x.get('publication_date','')):
                    add_block += f"- <b>{fr.get('publication_date','')}</b>: {fr.get('title','')[:200]} (Federal Register {fr.get('document_number','')})<br>"
                    add_block += f"  <a href=\"{fr.get('html_url','')}\">{fr.get('html_url','')}</a><br>"
                if "<b>SOURCES.</b>" in entry['D']:
                    entry['D'] = entry['D'].replace("<b>SOURCES.</b>", add_block + "<br><b>SOURCES.</b>", 1)
                else:
                    entry['D'] = entry['D'] + add_block
                print(f"  UPDATE: nagpra-roundup-2026-03 with {len(nagpra_extras)} additional notices")
                break

    # 4. Update alaska-oil-gas-leasing-pivot-2025-2026 with 4 FR URLs
    oil_gas_extras = CLUSTER_DATA.get('oil_gas_alaska', [])
    if oil_gas_extras:
        for entry in data['agency_actions']:
            if (entry.get('id') or entry.get('i')) == 'alaska-oil-gas-leasing-pivot-2025-2026':
                if "[UPDATE 2026-04-30 with component FR URLs]" in entry.get('D',''):
                    print("  SKIP: alaska-oil-gas-leasing-pivot-2025-2026 already updated")
                    break
                add_block = f"<br><br><b>UPDATE 2026-04-30.</b> The 2026-04-30 agency-coverage audit surfaced {len(oil_gas_extras)} component Federal Register documents underlying the components named in this aggregate [UPDATE 2026-04-30 with component FR URLs]:<br><br>"
                for r in sorted(oil_gas_extras, key=lambda x: x['fr_action'].get('publication_date','')):
                    fr = r['fr_action']
                    add_block += f"- <b>{fr.get('publication_date','')}</b>: {fr.get('title','')[:200]} (Federal Register {fr.get('document_number','')})<br>"
                    add_block += f"  <a href=\"{fr.get('html_url','')}\">{fr.get('html_url','')}</a><br>"
                if "<b>SOURCES.</b>" in entry['D']:
                    entry['D'] = entry['D'].replace("<b>SOURCES.</b>", add_block + "<br><b>SOURCES.</b>", 1)
                else:
                    entry['D'] = entry['D'] + add_block
                print(f"  UPDATE: alaska-oil-gas-leasing-pivot-2025-2026 with {len(oil_gas_extras)} component URLs")
                break

    # 5. Mute lit-2026-ks-sb244-001
    for entry in data['litigation']:
        if (entry.get('id') or entry.get('i')) == 'lit-2026-ks-sb244-001':
            if entry.get('muted'):
                print("  SKIP: lit-2026-ks-sb244-001 already muted")
                break
            entry['muted'] = True
            entry['_mutedReason'] = (
                "State-only litigation. The entry references only a 'Kansas district court' with no federal-court "
                "venue marker (no D. Kan., no U.S. District Court for the District of Kansas), no 42 U.S.C. 1983 "
                "citation, and no federal-defendant. The case caption is Doe v. State of Kansas, suggesting state-"
                "court litigation against state-level legislation (SB 244). Per the TCKC federal-actor coding policy "
                "locked 2026-04-23, state legislation and state-court challenges are out of scope. Mute rather than "
                "delete preserves the entry for unmuting if federal-court status is verified."
            )
            entry['_mutedDate'] = "2026-04-30"
            print("  MUTE: lit-2026-ks-sb244-001 (state-only, no federal-court nexus)")
            break

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    total = sum(len(data.get(k,[])) for k in ['executive_actions','agency_actions','legislation','litigation','other_domestic','international'])
    muted = sum(1 for k in ['executive_actions','agency_actions','legislation','litigation','other_domestic','international'] for e in data.get(k,[]) if e.get('muted'))
    print(f"\nDone. Total entries: {total} | Muted: {muted}")


if __name__ == "__main__":
    main()
