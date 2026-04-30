#!/usr/bin/env python3
"""Add Josef Palermo Atlantic op-ed entry to data.json.

Captures the April 16, 2026 first-person whistleblower account by the
Kennedy Center's first curator of visual arts. The Atlantic op-ed is the
primary-source artifact behind the existing CBS-News-derived Palermo
entry (kennedy-center-financial-decline-2026-002) and contains specific
allegations the CBS entry does not document, including the order to
disperse the permanent art collection, the lounge-renaming-for-donors
scheme, the NDA condition imposed on laid-off staff, and the explicit
call for Congress to install a firewall.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-palermo-atlantic"
)

NEW_ID = "kennedy-center-palermo-atlantic-2026-003"

ENTRY = {
    "i": NEW_ID,
    "t": "Whistleblower Report",
    "n": "The Atlantic: \"What I Saw Inside the Kennedy Center\" by Josef Palermo, April 16, 2026",
    "T": '<span style="color: #991B1B;">Whistleblower Report:</span> Former Kennedy Center Curator Josef Palermo Documents Art-Collection Purge Order, Donor Lounge-Renaming Scheme, and NDA Suppression of Laid-Off Staff in The Atlantic',
    "s": "Palermo Atlantic whistleblower op-ed",
    "d": "2026-04-16",
    "a": "Trump II",
    "A": ["Kennedy Center"],
    "S": "Active. The Atlantic published Palermo's first-person op-ed on 2026-04-16. Palermo is cooperating with Senator Sheldon Whitehouse's investigation and coordinating with Representative Joyce Beatty's legal team in Beatty v. Trump (Case 1:25-cv-03891 (D.D.C.)). Cross-references: kennedy-center-financial-decline-2026-002 (CBS News follow-up interview, 2026-04-21), v2025-009 (February 2025 board purge), aa-2026-kennedy-closure (2-year closure order), beatty-v-trump-2025 (renaming litigation).",
    "L": "SEVERE",
    "D": (
        "<b>WHISTLEBLOWER REPORT.</b> On April 16, 2026, The Atlantic published \"What I Saw Inside the Kennedy Center,\" a long-form first-person account by Josef Palermo, the institution's first curator of visual arts. Palermo served approximately ten months at the John F. Kennedy Center for the Performing Arts before being laid off during the Trump administration's takeover of the federally chartered cultural institution. His op-ed names specific individuals, specific schemes, and specific institutional decisions that he characterizes as \"cronyism, incompetence, and a series of bizarre moves\" driving the Center toward financial and artistic collapse.<br><br>"
        "<b>ART COLLECTION PURGE ORDER.</b> Palermo reports that interim Kennedy Center President Richard Grenell directly instructed him to \"get rid of\" the Center's permanent art collection. Grenell told Palermo that if donors would not pay the removal costs, the works would be auctioned or given away. Pieces from the collection have been moved to archives. The Kennedy Center's permanent art collection includes artworks acquired over decades for federal display and represents a discrete cultural treasure whose stewardship is part of the Center's congressional charter. The order to disperse the collection by sale or gift, conditional on donor willingness to pay for removal, is a direct attack on a federal cultural treasure.<br><br>"
        "<b>LOUNGE-RENAMING SCHEME.</b> Palermo reports that the Kennedy Center's culturally named lounges, including the Israeli Lounge, the Chinese Lounge, the Circles Lounge, and the African Room, were offered to donors with the promise that each space would be renamed for whoever donated the largest amount. These spaces host receptions and private dinners and have historically been associated with international cultural exchange and diasporic recognition. The scheme would convert federally housed cultural spaces honoring international and diasporic communities into vehicles for donor recognition by the highest bidder. The African Room and Chinese Lounge represent named institutional acknowledgements of African-descendant and Asian cultural presence at the federal performing-arts memorial; their conversion into donor-renamed spaces directly harms those communities' federal cultural recognition.<br><br>"
        "<b>FUNDRAISING THROUGH PRESIDENTIAL ACCESS.</b> Palermo reports that Kennedy Center fundraising tactics under the Trump-led leadership centered on selling access to the President himself, leveraging Trump's chairmanship and proximity to the President through preview events as the principal donor draw. Top fundraising officer Lisa Dale, by Palermo's account, was unfamiliar with basic arts and culture terminology, indicating that the fundraising operation was being conducted by personnel without sector experience.<br><br>"
        "<b>CRONYISM AND PROGRAMMING COLLAPSE.</b> Palermo reports that multiple Kennedy Center staffers under the new leadership had Republican political connections but no arts experience and were \"miscast in their roles.\" Palermo's own first three exhibitions developed under the new administration never came to be because he could not get the executive team to allocate institutional resources or funding. The cancellation of curated programming under conditions of executive disengagement and resource starvation is a documented mechanism of institutional decline.<br><br>"
        "<b>NDA SUPPRESSION OF LAID-OFF STAFF.</b> Palermo reports that laid-off Kennedy Center employees were offered additional severance only on the condition of signing confidentiality and nondisparagement agreements. Palermo rejected the offer. He stated that he did so because Americans deserve to know about the desecration of the Center. The NDA practice has the effect of suppressing first-person witness testimony from former federal-cultural-institution staff at the moment when public oversight is most needed.<br><br>"
        "<b>COOPERATION WITH CONGRESSIONAL AND LITIGATION OVERSIGHT.</b> Palermo reports that he is cooperating with Senator Sheldon Whitehouse's investigation into the Kennedy Center takeover and is coordinating with Representative Joyce Beatty's legal team in connection with Beatty v. Trump (Case 1:25-cv-03891 (D.D.C.)), the pending litigation challenging the renaming of the Center to include the President's name. His op-ed concludes with an explicit call to Congress: \"There must be a firewall put in place by Congress to prevent this kind of hostile political takeover.\"<br><br>"
        "<b>RELATIONSHIP TO RELATED TRACKER ENTRIES.</b> This entry documents the Atlantic op-ed as a discrete primary-source artifact. The same testimony was elaborated five days later in a CBS News interview captured at kennedy-center-financial-decline-2026-002. The underlying federal action (the February 2025 board purge that installed Trump as chairman) is captured at v2025-009. The February 2026 closure-and-rebuild order is captured at aa-2026-kennedy-closure. The renaming litigation referenced by Palermo is captured at beatty-v-trump-2025. The renaming itself is captured at v2025-001. The boycott response is captured at v2025-kennedy-002.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Palermo's testimony documents direct harm to (1) federal cultural Treasures (permanent art collection ordered removed by sale or gift), (2) federal cultural Places (culturally named lounges sold to highest-bidder donors; permanent collection display spaces emptied), (3) federal cultural Practices (curatorial work supplanted by political fundraising; programming cancelled for lack of institutional support; donor relations conducted by personnel without arts background), and (4) federal cultural People (curators and staff laid off and replaced with politically connected personnel without arts experience; remaining and departed staff silenced by NDA conditions). The harms are concrete, named, ongoing, and partially irreversible. Items already auctioned or gifted from the permanent collection cannot be returned without negotiation and expense. NDAs already signed will continue to suppress testimony for years. The harms attack the federal infrastructure through which African-descendant artists, Asian artists, immigrant and diaspora artists, and pluralistic American audiences access a federally funded high-capacity cultural platform."
    ),
    "I": {
        "allCommunities": {
            "people": "American audiences, artists, curators, and cultural workers across every discipline are affected by the documented conditions at the Kennedy Center. Palermo's testimony establishes that curatorial expertise is being displaced by political appointees without arts background, that federal cultural-institution staff are being silenced by NDA-conditioned severance, and that the Kennedy Center's capacity to function as a national cultural institution is being deliberately eroded. Visitors to the federally chartered living memorial to President Kennedy will encounter a hollowed-out programming offering and a defaced art collection.",
            "places": "The Kennedy Center complex itself, including its named lounges (Israeli Lounge, Chinese Lounge, Circles Lounge, African Room) and its permanent art collection display spaces, faces direct alteration. Spaces honoring international cultural exchange are being converted into donor-naming opportunities. Permanent collection display spaces have been emptied as artworks are moved to archives pending sale or gift.",
            "practices": "Curatorial practice at a flagship federal cultural institution is being displaced by political fundraising tactics. The practice of museum-grade collection stewardship is being replaced with collection dispersal contingent on donor willingness to pay removal costs. Donor relations practice is being conducted by personnel without sector experience.",
            "treasures": "The Kennedy Center's permanent art collection, accumulated over decades for federal display, has been ordered for removal by sale, gift, or auction. Items already moved to archives await disposition. The cultural memory embodied by the Center's named international lounges, originally established as recognitions of foreign and diasporic cultural presence, faces alienation through renaming for donor recognition."
        },
        "africanDescendant": {
            "people": "Black artists, curators, and cultural workers lose institutional advocates as experienced curatorial staff (including Palermo's professional cohort) are forced out. Black audiences lose access to a federal cultural platform whose programming has historically included jazz, gospel, theater, and dance traditions central to African American cultural life. The displacement of curatorial expertise reduces the institutional knowledge required to commission and present new work by Black artists.",
            "places": "The African Room at the Kennedy Center, a named institutional acknowledgement of African-descendant cultural presence in the federal performing-arts memorial, has been offered to donors for renaming. Conversion of this named space into donor-recognition real estate alienates a discrete federal site of African-descendant cultural recognition. Programming spaces that have historically presented Black artistic traditions face cancellation through resource starvation.",
            "practices": "The curatorial and programming practices that have brought African American jazz, gospel, theater, and dance traditions onto Kennedy Center stages depend on experienced staff and institutional resources, both of which Palermo reports are being stripped. Practices of long-term commissioning and multi-year residency for Black artists require institutional financial stability that the Center no longer offers under the documented conditions.",
            "treasures": "Works by African-descendant artists held in the Kennedy Center's permanent art collection are now subject to the disposal order Grenell issued to Palermo. Archival records of past Kennedy Center performances by Black artists, including Honors recipients, depend on stewardship by curatorial and archival staff whose ranks Palermo reports are being depleted. The naming history of the African Room itself is part of the institutional record now under threat of erasure through donor-driven renaming."
        },
        "asianAmerican": {
            "people": "Asian and Asian American artists and audiences face direct institutional harm through the lounge-renaming scheme and the broader programming collapse. The Chinese Lounge, named for a discrete recognition of Chinese cultural presence at the Center, has been offered for donor renaming. Asian American curators and cultural workers within the Center's prior staff are part of the cohort displaced by politically connected appointees without arts experience.",
            "places": "The Chinese Lounge at the Kennedy Center, like the African Room, has been offered to donors for renaming. The conversion of this named space alienates a discrete federal site of Asian cultural recognition. Programming spaces that present Asian classical music, theater, and dance traditions face cancellation through the resource starvation Palermo documents.",
            "practices": "Curatorial practice supporting the presentation of Asian performing arts traditions depends on the staff and resources Palermo reports are being eliminated. Cultural diplomacy through Asian performing arts exchange (a function the Center has historically performed) cannot continue without curatorial infrastructure.",
            "treasures": "Works by Asian and Asian American artists held in the Center's permanent art collection are subject to the same disposal order. The institutional naming history of the Chinese Lounge is part of the cultural record now at risk of donor-driven erasure."
        },
        "immigrant": {
            "people": "Immigrant and diaspora artists, including the international performing artists who have appeared at the Kennedy Center through its international programming and immigrant-origin American artists whose traditions have been represented in Center programming, face direct harm. The lounges that recognize international cultural exchange (Israeli, Chinese, African, Circles) constituted institutional acknowledgement of diaspora and international presence at the federal memorial. Their conversion into donor-naming real estate erases that acknowledgement.",
            "places": "Programming and reception spaces historically used for international cultural exchange face conversion through the donor-renaming scheme. International cultural institutions and presenting partners that have maintained co-production relationships with the Center face the loss of their American institutional partner as financial instability and political interference reshape the Center's international engagement.",
            "practices": "International cultural programming and cultural diplomacy through performing arts exchange depend on curatorial expertise and institutional financial stability, both of which Palermo reports are being stripped. The practice of contextualizing immigrant and diaspora cultural traditions in a federal-platform setting is threatened by the displacement of curatorial staff.",
            "treasures": "Documentation of international and diaspora performing arts presented at the Kennedy Center, along with works from immigrant and diaspora visual artists held in the permanent collection, are subject to the disposal order and to the broader institutional decay Palermo documents."
        }
    },
    "c": ["All Communities", "African-descendant", "Asian", "Immigrant/Diaspora"],
    "U": "https://www.theatlantic.com/culture/2026/04/inside-kennedy-center-shutdown-drama/686801/",
    "_source": "news_2026",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    other_domestic = data.get("other_domestic", [])
    if any((e.get("id") or e.get("i")) == NEW_ID for e in other_domestic):
        raise SystemExit(f"Entry {NEW_ID} already exists. Aborting.")

    # Em-dash audit before writing
    em_dash = "—"
    if em_dash in json.dumps(ENTRY, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash detected in new entry. Style violation.")

    other_domestic.append(ENTRY)
    data["other_domestic"] = other_domestic

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Inserted {NEW_ID} into other_domestic. Total other_domestic: {len(other_domestic)}.")


if __name__ == "__main__":
    main()
