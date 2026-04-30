#!/usr/bin/env python3
"""Add H.R. 1329 (Miller substitute) entry to data.json.

Captures the March 19, 2025 House Administration Committee markup that
gutted a previously bipartisan site-authorization bill for the Smithsonian
American Women's History Museum and replaced it with provisions barring
transgender women from museum exhibits and granting the President
unilateral site-override authority.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-hr1329"
)

ENTRY = {
    "id": "hr-1329-119",
    "t": "Bill",
    "n": "H.R. 1329",
    "T": '<span style="color: #CA8A04;">H.R. 1329:</span> Smithsonian American Women\'s History Museum Site Authorization Act (Miller Substitute)',
    "s": "American Women's History Museum (Miller substitute)",
    "d": "2025-03-19",
    "a": "Trump II",
    "A": ["Smithsonian"],
    "S": "Pending. Reported out of the Committee on House Administration on 2025-03-19 with the Miller substitute amendment adopted on a party-line vote. Awaiting House floor consideration.",
    "L": "HARMFUL",
    "D": (
        "<b>BILL:</b> H.R. 1329, 119th Congress. The Smithsonian American Women's History Museum Site Authorization Act began as bipartisan legislation with more than 200 cosponsors. Its original purpose was narrow. The bill would have authorized a site on the National Mall for the Smithsonian American Women's History Museum, a project Congress first approved in the Consolidated Appropriations Act of 2021 (P.L. 116-260) and that has stalled for years awaiting a site-authorization vote.<br><br>"
        "<b>THE MILLER SUBSTITUTE.</b> On March 19, 2025, Representative Mary Miller (R-IL) introduced a substitute amendment in the House Administration Committee. The substitute gutted the original text. It replaced the clean site authorization with provisions that codify the Trump administration's policy of erasing transgender people from federal cultural institutions. The committee adopted the substitute on a party-line vote. All Democratic cosponsors withdrew their support.<br><br>"
        "<b>KEY PROVISIONS OF THE MILLER SUBSTITUTE.</b> First, the bill restricts museum content to the history of <i>biological women</i> and bars the museum from identifying, presenting, describing, or otherwise depicting any biological male as female. Second, the bill grants the President unilateral authority to designate an alternative museum site within 180 days of enactment, overriding the Smithsonian Institution's own site recommendation. The first provision controls who may appear in the museum. The second provision controls where the museum will stand.<br><br>"
        "<b>WHO WOULD BE ERASED.</b> The substitute, if enacted, would bar the museum from depicting named historical figures whose contributions sit at the center of American women's history. Sylvia Rivera, the Puerto Rican trans woman who helped ignite the Stonewall uprising and co-founded Street Transvestite Action Revolutionaries (STAR), would be excluded. Marsha P. Johnson, the African-American trans woman who co-founded STAR with Rivera and led the modern LGBTQ+ rights movement in its earliest years, would be excluded. Lynn Conway, the computer scientist who pioneered Very-Large-Scale Integration architecture at Xerox PARC and was fired from IBM in 1968 for being transgender, would be excluded. Representative Sarah McBride (D-DE), the first openly transgender member of Congress, would be barred from depiction in any contemporary exhibit. The bill performs erasure by statute on a federally chartered institution.<br><br>"
        "<b>EXECUTIVE PRECURSOR.</b> The Miller substitute legislatively codifies Executive Order 14253, \"Restoring Truth and Sanity to American History\" (March 27, 2025), which directed Vice President Vance to eliminate \"divisive, race-centered ideology\" from the Smithsonian and demanded that future appropriations ensure the Women's History Museum and other Smithsonian museums \"not recognize men as women in any respect.\" The executive order established the policy. The Miller substitute fixes that policy in statute and adds a presidential site-selection lever the executive order did not provide.<br><br>"
        "<b>BROADER ERASURE PATTERN.</b> The bill is one component of a coordinated federal effort to remove transgender people from the public historical record. The National Park Service stripped transgender people from the Stonewall National Monument's website and changed \"LGBTQ+\" to \"LGB.\" The Department of Justice ordered the National Center for Missing and Exploited Children to deadname missing transgender children or lose federal funding. Federal agencies have removed gender-identity references from thousands of government web pages and removed gender-identity data from federal health surveys and CDC datasets. Nonprofits including RAINN and the Boys and Girls Clubs of America deleted transgender references from their websites in preemptive compliance.<br><br>"
        "<b>CULTURAL HARM ACROSS COMMUNITIES.</b> The bill harms African-descendant, Latiné, and Indigenous cultural continuity by erasing the trans women within those communities whose lives and labors built movements of liberation that all communities inherit. Marsha P. Johnson's place in Black liberation history would be expunged from the federal women's history record. Sylvia Rivera's place in Puerto Rican and broader Latiné liberation history would be expunged from the same record. Indigenous Two-Spirit and trans figures whose contributions shape intertribal cultural transmission would similarly be barred. The bill also restructures federal cultural memory by transferring museum-site authority from the Smithsonian (a quasi-independent trust instrumentality with curatorial expertise and a 178-year governance record) to the President personally. That transfer subordinates federal cultural recognition to electoral politics.<br><br>"
        "<b>LEGAL MECHANISM.</b> Congressional Article I authority over the Smithsonian Institution under 20 U.S.C. § 41 et seq. Article I, Section 7 procedure: passage by both chambers and presentment to the President. The Smithsonian operates 21 museums, the National Zoo, and 9 research centers as a trust instrumentality of the United States, governed by a Board of Regents that includes the Chief Justice, the Vice President, three Senators, three Representatives, and nine citizen regents. The Miller substitute would override the Board's site recommendation and override the Institution's curatorial judgment by federal statute.<br><br>"
        "<b>STATUS AND PATH.</b> Reported out of the Committee on House Administration on March 19, 2025 on a party-line vote, with the Miller substitute as the operative text. The amended bill awaits House floor action. Senate companion S. 1303 (introduced April 7, 2025) advances a clean version without the Miller restrictions and sits in the Senate Committee on Rules and Administration. If H.R. 1329 passes the House in its current form, the anti-trans provision faces a steeper procedural hurdle in the Senate, where it could draw filibuster opposition and where reconciliation with the clean Senate companion would be required."
    ),
    "I": {
        "African-descendant": {
            "people": "Black trans women erased from the federal women's history record. Marsha P. Johnson, co-founder of STAR and a central figure in the modern LGBTQ+ rights movement, would be barred from depiction. Black trans women living today, including political leaders, artists, and activists, would be excluded from contemporary exhibits.",
            "places": "The Smithsonian American Women's History Museum, a federally chartered institution intended to occupy the National Mall, would be barred from telling the full story of Black women's history. The bill would also let the President move the museum off its Smithsonian-recommended site by fiat.",
            "practices": "Public history practice at the Smithsonian, the federal government's flagship cultural memory institution, would be dictated by statute rather than by curatorial expertise. Black-led history-keeping traditions that center trans women's contributions would be excluded from federal recognition.",
            "treasures": "Archival materials, photographs, oral histories, personal effects, and written records of Black trans women would be barred from acquisition, display, or interpretation in the museum's permanent and temporary collections."
        },
        "Latiné": {
            "people": "Latina trans women erased from the federal women's history record. Sylvia Rivera, the Puerto Rican trans woman who helped ignite the Stonewall uprising and co-founded STAR, would be barred from depiction. Contemporary Latina trans leaders, artists, and activists would be excluded from contemporary exhibits.",
            "places": "The Smithsonian American Women's History Museum would be barred from telling the full story of Latina women's history, including the contributions of Latina trans women to U.S. civil rights and cultural movements.",
            "practices": "Public history practice on Latiné contributions to American women's history would be statutorily restricted. Latiné community history-keeping traditions that include trans women's leadership would be excluded from federal recognition.",
            "treasures": "Archival materials documenting Latina trans women's lives, including Sylvia Rivera's papers and effects held by partner institutions, would be barred from federal museum interpretation under the bill's restrictions."
        },
        "Indigenous": {
            "people": "Indigenous Two-Spirit and trans figures whose contributions shape intertribal cultural transmission would be barred from depiction in the federal women's history record.",
            "places": "The Smithsonian American Women's History Museum would be barred from depicting Indigenous Two-Spirit and trans women in connection with tribal lands, ceremonial sites, and cultural centers where their contributions are documented.",
            "practices": "Indigenous gender frameworks that recognize Two-Spirit and trans roles within tribal cultural continuity would be excluded from federal cultural recognition. The bill imposes a binary gender definition on the federal museum that contradicts the gender frameworks of many Indigenous nations.",
            "treasures": "Material culture, oral histories, and archival documentation of Indigenous Two-Spirit and trans women would be barred from federal museum interpretation."
        }
    },
    "c": ["African-descendant", "Latiné", "Indigenous", "lgbtq", "women", "All communities"],
    "U": "https://www.congress.gov/bill/119th-congress/house-bill/1329",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    legislation = data.get("legislation", [])
    if any((e.get("id") or e.get("i")) == ENTRY["id"] for e in legislation):
        raise SystemExit(f"Entry {ENTRY['id']} already exists. Aborting.")

    legislation.append(ENTRY)
    data["legislation"] = legislation

    if "meta" in data and isinstance(data["meta"], dict):
        meta = data["meta"]
        if "totalEntries" in meta:
            meta["totalEntries"] = sum(
                len(data[k]) for k in [
                    "executive_actions", "agency_actions", "legislation",
                    "litigation", "other_domestic", "international"
                ] if isinstance(data.get(k), list)
            )
        meta["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Inserted {ENTRY['id']} into legislation. Total legislation: {len(legislation)}.")


if __name__ == "__main__":
    main()
