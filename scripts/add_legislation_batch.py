#!/usr/bin/env python3
"""Add batch of legislation entries to data.json and remove Nevada Test Range entry."""
import json
from pathlib import Path
from datetime import date

DATA_PATH = Path(__file__).parent.parent / 'data' / 'data.json'

# ── All new legislation entries ──
NEW_ENTRIES = [
    # ═══ BLACK HISTORY & AFRICAN AMERICAN HERITAGE ═══
    {
        "id": "hr-1359-119", "t": "Bill", "n": "H.R. 1359",
        "T": "<span style=\"color: #065F46;\">H.R. 1359:</span> Black History Matters Act",
        "s": "Black History Matters Act",
        "d": "2025-02-13",
        "a": "Trump II", "A": ["ED", "NEH"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 1359, 119th Congress. The Black History Matters Act seeks to strengthen and expand the teaching of Black history across the United States public education system. The legislation responds to a growing wave of state-level efforts to restrict or dilute instruction on African American history, systemic racism, and the ongoing effects of slavery, segregation, and discrimination. KEY PROVISIONS: The bill would establish federal support for curriculum development, teacher training programs, and educational resource creation focused on Black history, including the African diaspora, the civil rights movement, Reconstruction, and contemporary contributions of Black Americans to every sphere of American life. It mandates the inclusion of primary source materials, oral histories, and perspectives from historically Black colleges and universities (HBCUs). CONTEXT: Introduced during Black History Month 2025, this bill directly counters executive and state-level actions that have sought to restrict critical race-related instruction. Under the Trump II administration, Executive Order 14151 ('Ending Radical and Wasteful Government DEI Programs') and related directives have chilled diversity and inclusion efforts across federal agencies and education policy. Multiple states have enacted or proposed legislation banning the teaching of concepts related to systemic racism. IMPACT: The bill affects African-descendant communities most directly, but also Indigenous, Latiné, Asian American, and all communities whose histories intersect with the broader story of racial justice in America. If enacted, it would create a federal floor for Black history education, ensuring that efforts to erase or minimize this history at the state level are met with federal counter-programming. SIGNIFICANCE: The bill represents a legislative effort to protect cultural and historical knowledge as a public good, recognizing that accurate education about Black history is essential for democratic citizenship and interracial understanding.",
        "I": {"African-descendant": {"people": "Students, educators, HBCU scholars, Black communities", "places": "Public schools, HBCUs, libraries, cultural institutions", "practices": "Teaching Black history, curriculum development, oral history", "treasures": "Historical records, primary sources, cultural narratives"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1359",
        "_source": "manual"
    },
    {
        "id": "hr-844-119", "t": "Bill", "n": "H.R. 844",
        "T": "<span style=\"color: #065F46;\">H.R. 844:</span> Black History is American History Act",
        "s": "Black History is American History Act",
        "d": "2025-01-28",
        "a": "Trump II", "A": ["ED"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 844, 119th Congress. The Black History is American History Act affirms that Black history is an integral and inseparable component of American history and seeks to ensure its comprehensive inclusion in K-12 public education curricula nationwide. KEY PROVISIONS: The bill establishes a federal grant program to support states, school districts, and educational nonprofits in developing and implementing comprehensive Black history curricula. It emphasizes the full scope of the Black American experience — from the forced migration of enslaved Africans, through Reconstruction, Jim Crow, the Great Migration, the civil rights movement, and into contemporary Black excellence in science, arts, politics, business, and culture. The legislation also calls for professional development for educators, the creation of culturally responsive teaching materials, and partnerships with museums, archives, and HBCUs. CONTEXT: This bill arrives during a period of active regression in diversity education. Multiple states have enacted laws restricting discussions of race and racism in schools, and the Trump II administration has issued executive orders targeting DEI programs across the federal government. The bill's title itself is a statement: Black history is not separate from American history — it IS American history. IMPACT: Primary beneficiaries include African-descendant communities, particularly students who deserve to see their history accurately reflected in education. The bill also benefits all American students by providing a more complete and truthful account of the nation's history.",
        "I": {"African-descendant": {"people": "Black students, educators, historians", "places": "Public schools, HBCUs, museums", "practices": "History education, curriculum development", "treasures": "Historical archives, cultural knowledge, oral traditions"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/844",
        "_source": "manual"
    },
    {
        "id": "hr-7549-119", "t": "Bill", "n": "H.R. 7549",
        "T": "<span style=\"color: #065F46;\">H.R. 7549:</span> National Council on African American History and Culture Act of 2026",
        "s": "African American History Council (House)",
        "d": "2026-02-27",
        "a": "Trump II", "A": ["Smithsonian"],
        "S": "Pending — Referred to Committee on House Administration",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 7549, 119th Congress. House companion to S. 3890. The National Council on African American History and Culture Act of 2026 would establish a permanent National Council dedicated to the preservation, study, and promotion of African American history and culture. KEY PROVISIONS: The Council would serve as an advisory body to Congress and the executive branch on matters relating to African American history, including recommendations for the preservation of historic sites, the expansion of museum collections, the development of educational programs, and the protection of cultural heritage. It would coordinate with the Smithsonian Institution's National Museum of African American History and Culture, the National Archives, HBCUs, and community-based organizations. CONTEXT: This legislation builds on the success of the National Museum of African American History and Culture (NMAAHC), which opened in 2016 and has become one of the most visited museums in the Smithsonian system. The bill responds to threats against DEI programs, cultural institutions, and the integrity of historical narratives under the current administration. SIGNIFICANCE: Establishing a permanent federal advisory council ensures that African American history and culture have a sustained institutional voice in federal policymaking, surviving changes in administration.",
        "I": {"African-descendant": {"people": "Black historians, scholars, community leaders", "places": "NMAAHC, historic sites, HBCUs, archives", "practices": "History preservation, cultural programming, education", "treasures": "Museum collections, archives, historic sites, oral histories"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/7549",
        "_source": "manual"
    },
    {
        "id": "sres-99-119", "t": "Resolution", "n": "S.Res. 99",
        "T": "<span style=\"color: #065F46;\">S.Res. 99:</span> A resolution celebrating Black History Month",
        "s": "Celebrating Black History Month",
        "d": "2025-02-27",
        "a": "Trump II", "A": [],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 99, 119th Congress. This Senate resolution formally celebrates Black History Month and recognizes the central role of African Americans in shaping every aspect of American society, culture, and democracy. KEY PROVISIONS: The resolution acknowledges the contributions of African Americans to the arts, sciences, politics, military service, entrepreneurship, and civic life. It calls on the people of the United States to observe Black History Month with appropriate programs, ceremonies, and activities that honor the achievements and struggles of African Americans. CONTEXT: Black History Month, established in 1976 as an expansion of Negro History Week (created by historian Carter G. Woodson in 1926), has been observed annually in February. This resolution takes on heightened significance during the Trump II administration, which has issued executive orders dismantling DEI programs and chilling diversity-focused initiatives. The Senate's passage of this resolution represents a bipartisan acknowledgment that Black history is foundational to American identity.",
        "I": {"African-descendant": {"people": "All Black Americans", "places": "Schools, museums, community centers, government buildings", "practices": "Black History Month observances, cultural programming", "treasures": "Cultural heritage, historical legacy, educational resources"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/99",
        "_source": "manual"
    },
    {
        "id": "hr-1817-119", "t": "Bill", "n": "H.R. 1817",
        "T": "<span style=\"color: #065F46;\">H.R. 1817:</span> Arturo Alfonso Schomburg Congressional Gold Medal Act",
        "s": "Schomburg Congressional Gold Medal",
        "d": "2025-03-06",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Financial Services",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 1817, 119th Congress. The Arturo Alfonso Schomburg Congressional Gold Medal Act would award a Congressional Gold Medal posthumously to Arturo Alfonso Schomburg (1874–1938), the Afro-Puerto Rican historian, writer, and activist whose personal collection of books, manuscripts, and artwork became the foundation of the Schomburg Center for Research in Black Culture at the New York Public Library — one of the world's most important research facilities devoted to the history and culture of people of African descent. KEY PROVISIONS: The bill authorizes the minting and award of a Congressional Gold Medal — one of the highest civilian honors — to Schomburg in recognition of his extraordinary contributions to the preservation and study of Black history and culture. SIGNIFICANCE: Schomburg's legacy is uniquely intersectional: as an Afro-Puerto Rican immigrant, he bridged African-descendant and Latiné communities, and his life's work demonstrated that the African diaspora's history is vast, rich, and essential to understanding world civilization. His collection, assembled at his own expense, became the nucleus of a research center that has served scholars, artists, and communities for nearly a century. CONTEXT: This bill also connects to H.Res. 766, celebrating the 100th anniversary of the Schomburg Center. Together, these measures affirm the enduring importance of Black cultural institutions.",
        "I": {"African-descendant": {"people": "Scholars, researchers, Black communities, Afro-Latiné communities", "places": "Schomburg Center, NYPL, museums", "practices": "Historical research, cultural preservation, archival work", "treasures": "Schomburg's collection, manuscripts, artworks, rare books"}},
        "c": ["African-descendant", "Latiné", "Immigrant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1817",
        "_source": "manual"
    },
    {
        "id": "hres-766-119", "t": "Resolution", "n": "H.Res. 766",
        "T": "<span style=\"color: #065F46;\">H.Res. 766:</span> Celebrating the 100th anniversary of the founding of the Schomburg Center for Research in Black Culture",
        "s": "Schomburg Center 100th Anniversary",
        "d": "2025-10-17",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 766, 119th Congress. This resolution celebrates the 100th anniversary of the Schomburg Center for Research in Black Culture, a division of the New York Public Library and one of the world's leading research facilities devoted to documenting, preserving, and providing access to materials relating to the history and experiences of people of African descent worldwide. Founded in 1925 from the personal collection of Arturo Alfonso Schomburg, the Center holds over 11 million items including rare manuscripts, photographs, art, moving images, and recorded sound. The Center has been a vital resource for scholars, artists, writers, and communities for a century. This resolution recognizes the Center's irreplaceable role in preserving Black cultural heritage and calls for its continued support.",
        "I": {"African-descendant": {"people": "Scholars, artists, researchers, Black communities", "places": "Schomburg Center, Harlem, New York", "practices": "Archival research, cultural programming, exhibitions", "treasures": "11 million+ items: manuscripts, photographs, art, recordings"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/766",
        "_source": "manual"
    },
    {
        "id": "hres-1080-119", "t": "Resolution", "n": "H.Res. 1080",
        "T": "<span style=\"color: #065F46;\">H.Res. 1080:</span> Original Black History Month Resolution of 2026",
        "s": "Black History Month Resolution 2026",
        "d": "2026-02-04",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 1080, 119th Congress. This House resolution recognizes and celebrates Black History Month in February 2026, honoring the extraordinary contributions of African Americans throughout the history of the United States. The resolution acknowledges the ongoing significance of studying and honoring Black history, particularly in an era when diversity education and cultural programming face political challenges. It calls on all Americans to observe Black History Month with appropriate ceremonies, activities, and programs.",
        "I": {"African-descendant": {"people": "All Black Americans, students, educators", "places": "Schools, cultural institutions, government buildings", "practices": "Black History Month observances, cultural education", "treasures": "Historical legacy, cultural heritage"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/1080",
        "_source": "manual"
    },
    {
        "id": "hres-1088-119", "t": "Resolution", "n": "H.Res. 1088",
        "T": "<span style=\"color: #065F46;\">H.Res. 1088:</span> Recognizing and celebrating the significance of Black history museums and cultural institutions",
        "s": "Black History Museums Recognition",
        "d": "2026-02-07",
        "a": "Trump II", "A": ["Smithsonian", "IMLS"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 1088, 119th Congress. This resolution formally recognizes and celebrates the significance of Black history museums and cultural institutions across the United States, including the National Museum of African American History and Culture, the DuSable Museum, the Charles H. Wright Museum, the National Civil Rights Museum, the Studio Museum in Harlem, and hundreds of local and regional institutions. These museums serve as custodians of African American cultural heritage, providing educational programming, preserving artifacts and archives, and serving as community anchors. The resolution arrives at a critical moment when federal funding for cultural institutions faces unprecedented cuts and when the role of museums in preserving accurate historical narratives is being challenged. It calls on Congress to support these institutions through sustained federal funding and to recognize their vital role in American civic life.",
        "I": {"African-descendant": {"people": "Museum staff, educators, Black communities, visitors", "places": "NMAAHC, DuSable Museum, Wright Museum, Civil Rights Museum, local Black museums", "practices": "Museum operations, exhibitions, educational programming, archival preservation", "treasures": "Collections, artifacts, artworks, historical documents, oral histories"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/1088",
        "_source": "manual"
    },
    {
        "id": "s-3953-119", "t": "Bill", "n": "S. 3953",
        "T": "<span style=\"color: #065F46;\">S. 3953:</span> A bill to authorize the Director of the National Museum of African American History and Culture to support African American history education programs",
        "s": "NMAAHC Education Programs Authorization",
        "d": "2026-03-03",
        "a": "Trump II", "A": ["Smithsonian", "ED"],
        "S": "Pending — Referred to Committee on Rules and Administration",
        "L": "PROTECTIVE",
        "D": "BILL: S. 3953, 119th Congress. This bill authorizes the Director of the National Museum of African American History and Culture (NMAAHC) to develop, support, and expand African American history education programs nationwide. KEY PROVISIONS: The legislation would empower the NMAAHC to create curriculum resources, teacher training programs, traveling exhibitions, digital educational tools, and community partnerships designed to bring African American history education to schools and communities across the country, particularly in underserved areas. The bill authorizes appropriations for these programs and establishes an advisory committee of educators, historians, and community leaders. CONTEXT: The NMAAHC, which opened on the National Mall in 2016, has become the most visited Smithsonian museum. This legislation would extend its educational mission beyond its physical walls, creating a national network of African American history education. This is especially significant given ongoing efforts to restrict race-related education in multiple states.",
        "I": {"African-descendant": {"people": "Students, educators, Black communities nationwide", "places": "NMAAHC, schools, community centers, libraries", "practices": "History education, curriculum development, teacher training", "treasures": "Educational resources, digital tools, traveling exhibitions"}},
        "c": ["African-descendant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/3953",
        "_source": "manual"
    },

    # ═══ FILIPINO AMERICAN HERITAGE ═══
    {
        "id": "sres-423-119", "t": "Resolution", "n": "S.Res. 423",
        "T": "<span style=\"color: #065F46;\">S.Res. 423:</span> A resolution recognizing the month of October 2025 as Filipino American History Month",
        "s": "Filipino American History Month (Senate)",
        "d": "2025-10-07",
        "a": "Trump II", "A": [],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 423, 119th Congress. This Senate resolution recognizes October 2025 as Filipino American History Month and celebrates the history and culture of Filipino Americans and their immense contributions to the United States. Filipino Americans are one of the largest Asian American communities, with over 4 million people of Filipino descent in the United States. Filipino American History Month commemorates the first recorded presence of Filipinos in the continental United States on October 18, 1587, when Filipino sailors aboard the Spanish galleon Nuestra Señora de Buena Esperanza landed at Morro Bay, California. The resolution honors Filipino Americans' contributions to agriculture, labor, military service (including over 250,000 who served under the U.S. flag in World War II), healthcare, arts, education, and public service.",
        "I": {"Asian American": {"people": "Filipino American communities, veterans, healthcare workers", "places": "Filipino American cultural centers, communities nationwide", "practices": "Filipino American History Month observances, cultural celebrations", "treasures": "Filipino cultural heritage, military service records, historical archives"}},
        "c": ["Asian American", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/423",
        "_source": "manual"
    },
    {
        "id": "hres-774-119", "t": "Resolution", "n": "H.Res. 774",
        "T": "<span style=\"color: #065F46;\">H.Res. 774:</span> Expressing support for the recognition of October 2025 as Filipino American History Month",
        "s": "Filipino American History Month (House)",
        "d": "2025-10-17",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 774, 119th Congress. House companion to S.Res. 423. This resolution expresses support for the recognition of October 2025 as Filipino American History Month and celebrates the history, culture, and contributions of Filipino Americans to the United States. The resolution highlights the Filipino American community's contributions across all sectors of American life, including healthcare (Filipino Americans are one of the largest groups of nurses in the U.S.), military service, labor, education, arts, and civic engagement.",
        "I": {"Asian American": {"people": "Filipino American communities nationwide", "places": "Filipino American cultural centers, healthcare institutions", "practices": "Cultural celebrations, heritage month observances", "treasures": "Cultural traditions, historical legacy, community institutions"}},
        "c": ["Asian American", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/774",
        "_source": "manual"
    },

    # ═══ NATIVE HAWAIIAN HERITAGE ═══
    {
        "id": "hres-787-119", "t": "Resolution", "n": "H.Res. 787",
        "T": "<span style=\"color: #065F46;\">H.Res. 787:</span> Expressing support for the designation of September 2025 as \"Hawaiian History Month\"",
        "s": "Hawaiian History Month (House)",
        "d": "2025-10-23",
        "a": "Trump II", "A": ["DOI"],
        "S": "Pending — Referred to Committee on Natural Resources",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 787, 119th Congress. This resolution expresses support for designating September 2025 as 'Hawaiian History Month' to recognize the history, culture, and contributions of Native Hawaiians and to reaffirm the United States federal trust responsibility to the Native Hawaiian community. The resolution acknowledges Native Hawaiians as the indigenous people of Hawaiʻi, with a rich cultural heritage spanning over a millennium. It recognizes the illegal overthrow of the Hawaiian Kingdom in 1893 (acknowledged by Congress in the 1993 Apology Resolution), the suppression of Hawaiian language and cultural practices, and the ongoing federal trust relationship. SIGNIFICANCE: This resolution is especially important in the current political environment where federal trust responsibilities to Indigenous peoples, including Native Hawaiians, face potential erosion. It reaffirms the unique political and legal relationship between the United States and Native Hawaiians.",
        "I": {"Native Hawaiian": {"people": "Native Hawaiian communities, cultural practitioners", "places": "Hawaiʻi, Native Hawaiian cultural sites, heiau", "practices": "Hawaiian cultural traditions, hula, language, navigation, land stewardship", "treasures": "Cultural sites, traditional knowledge, Hawaiian language, cultural practices"}},
        "c": ["Native Hawaiian", "Pacific Islander", "Indigenous/Tribal"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/787",
        "_source": "manual"
    },
    {
        "id": "sres-419-119", "t": "Resolution", "n": "S.Res. 419",
        "T": "<span style=\"color: #065F46;\">S.Res. 419:</span> A resolution expressing support for the designation of September 2025 as \"Hawaiian History Month\"",
        "s": "Hawaiian History Month (Senate)",
        "d": "2025-10-02",
        "a": "Trump II", "A": ["DOI"],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 419, 119th Congress. Senate companion to H.Res. 787. This resolution expresses support for designating September 2025 as 'Hawaiian History Month' to recognize the history, culture, and contributions of Native Hawaiians and reaffirm the United States federal trust responsibility to the Native Hawaiian community. Agreed to by the Senate, this resolution represents a formal Congressional acknowledgment of Native Hawaiian heritage and the federal government's ongoing obligations.",
        "I": {"Native Hawaiian": {"people": "Native Hawaiian communities", "places": "Hawaiʻi, cultural sites", "practices": "Hawaiian cultural traditions, language preservation", "treasures": "Cultural heritage, traditional knowledge"}},
        "c": ["Native Hawaiian", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/419",
        "_source": "manual"
    },
    {
        "id": "sres-83-119", "t": "Resolution", "n": "S.Res. 83",
        "T": "<span style=\"color: #065F46;\">S.Res. 83:</span> A resolution designating February 2025 as \"Hawaiian Language Month\" or \"ʻŌlelo Hawaiʻi Month\"",
        "s": "Hawaiian Language Month 2025 (Senate)",
        "d": "2025-02-12",
        "a": "Trump II", "A": [],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 83, 119th Congress. This Senate resolution designates February 2025 as 'Hawaiian Language Month' or 'ʻŌlelo Hawaiʻi Month,' recognizing the Hawaiian language as a vital part of Native Hawaiian cultural heritage and American linguistic diversity. ʻŌlelo Hawaiʻi was nearly driven to extinction after it was banned from use in schools following the overthrow of the Hawaiian Kingdom in 1893. By the 1980s, fewer than 50 children under 18 were native speakers. The revitalization movement, including Hawaiian language immersion schools (kula kaiapuni), has been a remarkable success story, with thousands now learning the language. This resolution affirms the importance of continuing these efforts.",
        "I": {"Native Hawaiian": {"people": "Native Hawaiian speakers, students, language educators", "places": "Hawaiian language immersion schools, Hawaiʻi", "practices": "Hawaiian language education, cultural transmission", "treasures": "ʻŌlelo Hawaiʻi, oral traditions, chants, place names"}},
        "c": ["Native Hawaiian", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/83",
        "_source": "manual"
    },
    {
        "id": "hres-136-119", "t": "Resolution", "n": "H.Res. 136",
        "T": "<span style=\"color: #065F46;\">H.Res. 136:</span> Expressing support for the designation of February 2025 as \"Hawaiian Language Month\" or \"ʻŌlelo Hawaiʻi Month\"",
        "s": "Hawaiian Language Month 2025 (House)",
        "d": "2025-02-12",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 136, 119th Congress. House companion to S.Res. 83. This resolution supports the designation of February 2025 as 'Hawaiian Language Month' or 'ʻŌlelo Hawaiʻi Month,' recognizing the importance of the Hawaiian language to Native Hawaiian cultural identity and heritage.",
        "I": {"Native Hawaiian": {"people": "Native Hawaiian speakers, students", "places": "Hawaiian language schools, Hawaiʻi", "practices": "Language revitalization, cultural education", "treasures": "Hawaiian language, oral traditions"}},
        "c": ["Native Hawaiian", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/136",
        "_source": "manual"
    },
    {
        "id": "sres-625-119", "t": "Resolution", "n": "S.Res. 625",
        "T": "<span style=\"color: #065F46;\">S.Res. 625:</span> A resolution designating February 2026 as \"Hawaiian Language Month\" or \"Olelo Hawaiʻi Month\"",
        "s": "Hawaiian Language Month 2026",
        "d": "2026-02-11",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 625, 119th Congress. Continuing the annual tradition, this resolution designates February 2026 as 'Hawaiian Language Month,' building on previous years' successful resolutions (S.Res. 83 in 2025) to maintain federal recognition of the importance of ʻŌlelo Hawaiʻi language preservation and revitalization.",
        "I": {"Native Hawaiian": {"people": "Native Hawaiian communities, language learners", "places": "Hawaiian language programs, schools", "practices": "Language preservation, cultural education", "treasures": "Hawaiian language, chants, oral traditions"}},
        "c": ["Native Hawaiian", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/625",
        "_source": "manual"
    },

    # ═══ INDIGENOUS PEOPLES ═══
    {
        "id": "hres-809-119", "t": "Resolution", "n": "H.Res. 809",
        "T": "<span style=\"color: #065F46;\">H.Res. 809:</span> Expressing support for the designation of the second Monday in October 2025 as \"Indigenous Peoples' Day\"",
        "s": "Indigenous Peoples' Day (House)",
        "d": "2025-10-28",
        "a": "Trump II", "A": ["DOI", "BIA"],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 809, 119th Congress. This resolution expresses support for designating the second Monday in October 2025 as 'Indigenous Peoples' Day' to celebrate and honor Indigenous Peoples and their shared history and culture. The resolution represents an important counterpoint to the Trump II administration's reinstatement of Columbus Day as the exclusive federal observance, reversing the Biden administration's recognition of Indigenous Peoples' Day. SIGNIFICANCE: The movement to replace Columbus Day with Indigenous Peoples' Day recognizes the historical violence and colonization that followed Columbus's arrival while centering the cultures, contributions, and resilience of Indigenous peoples. Hundreds of cities, counties, and states have adopted Indigenous Peoples' Day, making this resolution a reflection of a broader national shift.",
        "I": {"Indigenous/Tribal": {"people": "All Indigenous peoples, Native Americans, Alaska Natives", "places": "Tribal lands, reservations, cultural sites, schools", "practices": "Indigenous cultural celebrations, traditional ceremonies, education", "treasures": "Indigenous cultural heritage, languages, traditions, sacred sites"}},
        "c": ["Indigenous/Tribal", "Alaska Native", "Native Hawaiian"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/809",
        "_source": "manual"
    },
    {
        "id": "sres-450-119", "t": "Resolution", "n": "S.Res. 450",
        "T": "<span style=\"color: #065F46;\">S.Res. 450:</span> A resolution expressing support for the designation of the second Monday in October 2025 as \"Indigenous Peoples' Day\"",
        "s": "Indigenous Peoples' Day (Senate)",
        "d": "2025-10-28",
        "a": "Trump II", "A": ["DOI", "BIA"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 450, 119th Congress. Senate companion to H.Res. 809. This resolution expresses support for designating the second Monday in October 2025 as 'Indigenous Peoples' Day' to celebrate and honor Indigenous Peoples and their shared history and culture. It represents a Senate-level affirmation of the movement to honor Indigenous peoples on a day historically associated with colonization.",
        "I": {"Indigenous/Tribal": {"people": "All Indigenous peoples", "places": "Tribal lands, cultural sites", "practices": "Cultural celebrations, traditional ceremonies", "treasures": "Indigenous heritage, languages, sacred sites"}},
        "c": ["Indigenous/Tribal", "Alaska Native", "Native Hawaiian"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/450",
        "_source": "manual"
    },
    {
        "id": "hres-911-119", "t": "Resolution", "n": "H.Res. 911",
        "T": "<span style=\"color: #065F46;\">H.Res. 911:</span> Recognizing National Native American Heritage Month and celebrating the heritages and cultures of Native Americans",
        "s": "Native American Heritage Month",
        "d": "2025-12-06",
        "a": "Trump II", "A": ["DOI", "BIA"],
        "S": "Pending — Referred to Committee on Natural Resources",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 911, 119th Congress. This resolution recognizes November as National Native American Heritage Month and celebrates the heritages and cultures of Native Americans and their contributions to the United States. The resolution acknowledges the rich traditions, languages, and cultural practices of more than 570 federally recognized tribal nations, and calls for continued support of tribal sovereignty, self-determination, and the federal trust responsibility.",
        "I": {"Indigenous/Tribal": {"people": "Native American communities, tribal nations", "places": "Tribal lands, reservations, cultural sites", "practices": "Traditional ceremonies, cultural celebrations, language preservation", "treasures": "Indigenous languages, sacred sites, cultural traditions, artifacts"}},
        "c": ["Indigenous/Tribal", "Alaska Native"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/911",
        "_source": "manual"
    },
    {
        "id": "sres-501-119", "t": "Resolution", "n": "S.Res. 501",
        "T": "<span style=\"color: #065F46;\">S.Res. 501:</span> A resolution recognizing National Native American Heritage Month",
        "s": "Native American Heritage Month (Senate)",
        "d": "2025-11-20",
        "a": "Trump II", "A": ["DOI", "BIA"],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 501, 119th Congress. This Senate resolution recognizes National Native American Heritage Month and celebrates the heritages and cultures of Native Americans and their contributions to the United States. Agreed to by the Senate.",
        "I": {"Indigenous/Tribal": {"people": "Native American communities, tribal nations", "places": "Tribal lands, cultural sites", "practices": "Heritage month observances, cultural celebrations", "treasures": "Indigenous cultural heritage, traditions, languages"}},
        "c": ["Indigenous/Tribal", "Alaska Native"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/501",
        "_source": "manual"
    },

    # ═══ ASIAN AMERICAN, NATIVE HAWAIIAN, PACIFIC ISLANDER ═══
    {
        "id": "aanhpi-museum-commission-119", "t": "Congressional Record", "n": "Congressional Record Vol. 171, No. 2",
        "T": "<span style=\"color: #065F46;\">Congressional Record:</span> Appointment of individual to the Commission to Study the Potential Creation of a National Museum of Asian Pacific American History and Culture Act",
        "s": "AANHPI Museum Commission Appointment",
        "d": "2025-02-07",
        "a": "Trump II", "A": ["Smithsonian"],
        "S": "Appointment made — Commission member named",
        "L": "PROTECTIVE",
        "D": "CONGRESSIONAL RECORD: Vol. 171, No. 2, House of Representatives, February 7, 2025. The Speaker of the House announced the appointment of an individual to serve on the Commission to Study the Potential Creation of a National Museum of Asian Pacific American History and Culture, as authorized by the Commission To Study the Potential Creation of a National Museum of Asian Pacific American History and Culture Act. This commission is tasked with studying the feasibility and advisability of establishing a museum within the Smithsonian Institution dedicated to Asian Pacific American history and culture. SIGNIFICANCE: The appointment signals continued Congressional commitment to exploring the creation of a national museum dedicated to Asian Pacific American history, similar to the successful establishment of the National Museum of African American History and Culture. The potential museum would serve as a national repository for Asian Pacific American stories, artifacts, and cultural heritage.",
        "I": {"Asian American": {"people": "Asian American and Pacific Islander communities", "places": "Smithsonian Institution, potential museum site", "practices": "Museum planning, cultural heritage preservation, community engagement", "treasures": "AAPI historical artifacts, archives, cultural collections"}},
        "c": ["Asian American", "Pacific Islander", "Native Hawaiian"],
        "U": "https://www.congress.gov/congressional-record/volume-171/issue-2/house-section",
        "_source": "manual"
    },
    {
        "id": "sres-214-119", "t": "Resolution", "n": "S.Res. 214",
        "T": "<span style=\"color: #065F46;\">S.Res. 214:</span> A resolution recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month",
        "s": "AANHPI Heritage Month (Senate)",
        "d": "2025-05-15",
        "a": "Trump II", "A": [],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 214, 119th Congress. This Senate resolution recognizes the significance of Asian American, Native Hawaiian, and Pacific Islander (AANHPI) Heritage Month in May as an important time to celebrate the significant contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the history of the United States. The AANHPI community, comprising over 24 million people, represents one of the fastest-growing demographic groups in the nation. The resolution acknowledges contributions across all sectors and recognizes the ongoing challenges facing AANHPI communities, including anti-Asian hate, immigration issues, language access, and disaggregated data needs.",
        "I": {"Asian American": {"people": "Asian American, Native Hawaiian, Pacific Islander communities", "places": "AANHPI cultural centers, communities nationwide", "practices": "Heritage month celebrations, cultural programming", "treasures": "AANHPI cultural heritage, historical legacy"}},
        "c": ["Asian American", "Pacific Islander", "Native Hawaiian"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/214",
        "_source": "manual"
    },
    {
        "id": "hres-400-119", "t": "Resolution", "n": "H.Res. 400",
        "T": "<span style=\"color: #065F46;\">H.Res. 400:</span> Recognizing the significance of Asian American, Native Hawaiian, and Pacific Islander Heritage Month",
        "s": "AANHPI Heritage Month (House)",
        "d": "2025-05-16",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 400, 119th Congress. House companion to S.Res. 214. This resolution recognizes the significance of AANHPI Heritage Month as an important time to celebrate the contributions of Asian Americans, Native Hawaiians, and Pacific Islanders to the United States.",
        "I": {"Asian American": {"people": "AANHPI communities nationwide", "places": "Cultural centers, communities", "practices": "Heritage month observances, cultural celebrations", "treasures": "Cultural heritage, historical legacy"}},
        "c": ["Asian American", "Pacific Islander", "Native Hawaiian"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/400",
        "_source": "manual"
    },
    {
        "id": "s-1844-119", "t": "Bill", "n": "S. 1844",
        "T": "<span style=\"color: #065F46;\">S. 1844:</span> Teaching Asian American, Native Hawaiian, and Pacific Islander History Act of 2025",
        "s": "Teaching AANHPI History Act (Senate)",
        "d": "2025-05-22",
        "a": "Trump II", "A": ["ED"],
        "S": "Pending — Referred to Committee on Health, Education, Labor, and Pensions",
        "L": "PROTECTIVE",
        "D": "BILL: S. 1844, 119th Congress. The Teaching Asian American, Native Hawaiian, and Pacific Islander History Act would establish federal support for the inclusion of AANHPI history in K-12 education curricula. KEY PROVISIONS: The bill creates a grant program for states and school districts to develop AANHPI history curricula, train teachers, and create educational resources. It covers the full breadth of AANHPI history — from the earliest Asian immigrants in the 1700s, through the Chinese Exclusion Act, Japanese American incarceration, the Filipino farm workers movement, the Vietnam War refugee experience, and contemporary issues including anti-Asian hate. SIGNIFICANCE: AANHPI history is dramatically underrepresented in American education. Studies show that less than 1% of history curriculum time is devoted to AANHPI contributions. This bill would create a federal framework for correcting this erasure.",
        "I": {"Asian American": {"people": "AANHPI students, educators, communities", "places": "K-12 schools nationwide", "practices": "History education, curriculum development, teacher training", "treasures": "AANHPI historical records, oral histories, cultural knowledge"}},
        "c": ["Asian American", "Pacific Islander", "Native Hawaiian"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/1844",
        "_source": "manual"
    },
    {
        "id": "hr-3551-119", "t": "Bill", "n": "H.R. 3551",
        "T": "<span style=\"color: #065F46;\">H.R. 3551:</span> Teaching Asian American, Native Hawaiian, and Pacific Islander History Act",
        "s": "Teaching AANHPI History Act (House)",
        "d": "2025-05-22",
        "a": "Trump II", "A": ["ED"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 3551, 119th Congress. House companion to S. 1844. The Teaching AANHPI History Act would establish federal grants for K-12 AANHPI history education, including curriculum development, teacher training, and educational resources covering the full breadth of Asian American, Native Hawaiian, and Pacific Islander history and contributions.",
        "I": {"Asian American": {"people": "AANHPI students, educators", "places": "Schools nationwide", "practices": "History education, curriculum development", "treasures": "AANHPI historical knowledge, cultural heritage"}},
        "c": ["Asian American", "Pacific Islander", "Native Hawaiian"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/3551",
        "_source": "manual"
    },

    # ═══ LATINÉ HERITAGE ═══
    {
        "id": "hres-261-119", "t": "Resolution", "n": "H.Res. 261",
        "T": "<span style=\"color: #065F46;\">H.Res. 261:</span> Recognizing the heritage, culture, and contributions of Latinas in the United States",
        "s": "Latina Heritage Recognition (House)",
        "d": "2025-03-26",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 261, 119th Congress. This resolution recognizes the heritage, culture, and contributions of Latinas in the United States. It acknowledges Latinas' leadership in education, healthcare, business, public service, the arts, sciences, and social justice movements. The resolution highlights the unique challenges facing Latinas, including the gender and racial pay gap, barriers to healthcare access, and immigration-related vulnerabilities.",
        "I": {"Latiné": {"people": "Latinas across the United States", "places": "Communities, workplaces, educational institutions", "practices": "Cultural celebrations, advocacy, professional achievement", "treasures": "Latina cultural heritage, contributions, historical legacy"}},
        "c": ["Latiné", "Women", "Immigrant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/261",
        "_source": "manual"
    },
    {
        "id": "sres-144-119", "t": "Resolution", "n": "S.Res. 144",
        "T": "<span style=\"color: #065F46;\">S.Res. 144:</span> A resolution recognizing the heritage, culture, and contributions of Latinas in the United States",
        "s": "Latina Heritage Recognition (Senate)",
        "d": "2025-03-25",
        "a": "Trump II", "A": [],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 144, 119th Congress. Senate companion to H.Res. 261. This resolution recognizes the heritage, culture, and contributions of Latinas in the United States. Agreed to by the Senate.",
        "I": {"Latiné": {"people": "Latinas across the United States", "places": "Communities nationwide", "practices": "Cultural celebrations, advocacy", "treasures": "Latina cultural heritage, historical contributions"}},
        "c": ["Latiné", "Women"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/144",
        "_source": "manual"
    },
    {
        "id": "sres-428-119", "t": "Resolution", "n": "S.Res. 428",
        "T": "<span style=\"color: #065F46;\">S.Res. 428:</span> A resolution recognizing Hispanic Heritage Month",
        "s": "Hispanic Heritage Month Recognition",
        "d": "2025-10-09",
        "a": "Trump II", "A": [],
        "S": "Agreed to in the Senate",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: S.Res. 428, 119th Congress. This Senate resolution recognizes Hispanic Heritage Month (September 15 – October 15) and celebrates the heritage and culture of Latinos in the United States and their immense contributions to the nation. The resolution acknowledges the over 65 million Hispanic and Latino Americans who enrich every aspect of American life. Agreed to by the Senate.",
        "I": {"Latiné": {"people": "Hispanic and Latino communities", "places": "Communities nationwide, cultural institutions", "practices": "Hispanic Heritage Month celebrations, cultural programming", "treasures": "Latino cultural heritage, artistic traditions, historical legacy"}},
        "c": ["Latiné"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-resolution/428",
        "_source": "manual"
    },

    # ═══ ARAB AMERICAN HERITAGE ═══
    {
        "id": "hres-351-119", "t": "Resolution", "n": "H.Res. 351",
        "T": "<span style=\"color: #065F46;\">H.Res. 351:</span> Expressing support for the recognition of April as \"National Arab American Heritage Month\"",
        "s": "Arab American Heritage Month",
        "d": "2025-04-29",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 351, 119th Congress. This resolution expresses support for the recognition of April as 'National Arab American Heritage Month' (NAAHM) and celebrates the heritage and culture of Arab Americans in the United States. There are approximately 3.7 million Arab Americans in the United States, tracing their origins to 22 Arabic-speaking countries. The resolution acknowledges Arab Americans' contributions to science, medicine, business, the arts, government, and military service. CONTEXT: Arab American Heritage Month takes on heightened significance during a period of increased Islamophobia, anti-Arab sentiment, and immigration restrictions that disproportionately affect Arab and Middle Eastern communities.",
        "I": {"All communities": {"people": "Arab American communities", "places": "Arab American cultural centers, communities", "practices": "Heritage month celebrations, cultural education", "treasures": "Arab American cultural heritage, traditions, contributions"}},
        "c": ["Muslim", "Immigrant", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/351",
        "_source": "manual"
    },

    # ═══ GARIFUNA HERITAGE ═══
    {
        "id": "hres-288-119", "t": "Resolution", "n": "H.Res. 288",
        "T": "<span style=\"color: #065F46;\">H.Res. 288:</span> Expressing the sense that there should be established a \"National Garifuna Immigrant Heritage Month\" in April",
        "s": "Garifuna Immigrant Heritage Month",
        "d": "2025-04-01",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 288, 119th Congress. This resolution expresses the sense that there should be established a 'National Garifuna Immigrant Heritage Month' in April to celebrate the contributions of Americans of Garifuna immigrant heritage. The Garifuna people, descended from West African, Central African, Arawak, and Island Carib peoples, have a unique cultural heritage that includes the Garifuna language (a UNESCO Masterpiece of the Oral and Intangible Heritage of Humanity), punta music and dance, cassava-based foodways, and a rich oral tradition. Garifuna Americans, primarily from Honduras, Belize, Guatemala, and Nicaragua, have made significant contributions to American culture, particularly in music, food, and community organizing. SIGNIFICANCE: This resolution recognizes a community often invisible in larger demographic categories, affirming the diversity within Afro-Latiné and Caribbean communities.",
        "I": {"African-descendant": {"people": "Garifuna Americans, Afro-Latiné communities", "places": "Garifuna communities (especially NYC, LA, Houston, New Orleans)", "practices": "Punta music and dance, Garifuna language, cassava foodways, oral traditions", "treasures": "Garifuna language, music, dance, culinary traditions, oral history"}},
        "c": ["African-descendant", "Latiné", "Immigrant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/288",
        "_source": "manual"
    },

    # ═══ TAMIL HERITAGE ═══
    {
        "id": "hres-41-119", "t": "Resolution", "n": "H.Res. 41",
        "T": "<span style=\"color: #065F46;\">H.Res. 41:</span> Expressing support for the designation of January as \"Tamil Language and Heritage Month\"",
        "s": "Tamil Language and Heritage Month",
        "d": "2025-01-14",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Oversight and Accountability",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 41, 119th Congress. This resolution expresses support for the designation of January as 'Tamil Language and Heritage Month,' recognizing the Tamil language as one of the world's oldest continuously spoken classical languages, with a literary tradition spanning over 2,000 years. Tamil is spoken by approximately 80 million people worldwide, and Tamil Americans are a vibrant community contributing to science, technology, medicine, business, arts, and culture in the United States. The resolution acknowledges the rich cultural heritage of Tamil civilization, including its contributions to mathematics, astronomy, architecture, literature, music, and dance (Bharatanatyam).",
        "I": {"Asian American": {"people": "Tamil American communities", "places": "Tamil cultural centers, temples, communities", "practices": "Tamil language education, Bharatanatyam dance, music, literature", "treasures": "Tamil language, classical literature, artistic traditions"}},
        "c": ["Asian American", "Immigrant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/41",
        "_source": "manual"
    },

    # ═══ SMITHSONIAN & MUSEUMS ═══
    {
        "id": "s-1303-119", "t": "Bill", "n": "S. 1303",
        "T": "<span style=\"color: #065F46;\">S. 1303:</span> Smithsonian American Women's History Museum Act",
        "s": "American Women's History Museum",
        "d": "2025-04-07",
        "a": "Trump II", "A": ["Smithsonian"],
        "S": "Pending — Referred to Committee on Rules and Administration",
        "L": "PROTECTIVE",
        "D": "BILL: S. 1303, 119th Congress. The Smithsonian American Women's History Museum Act advances the creation of a dedicated museum within the Smithsonian Institution to collect, study, and present the full spectrum of women's contributions to American history. While the museum was authorized in the Smithsonian American Women's History Museum Act of 2020 (P.L. 116-260), this bill addresses implementation, site selection, and funding mechanisms. SIGNIFICANCE: The museum would join the National Museum of African American History and Culture and the future National Museum of the American Latino as part of an expanding effort to ensure that the Smithsonian reflects the full diversity of American history.",
        "I": {"Women": {"people": "Women of all backgrounds, scholars, educators", "places": "Smithsonian campus, National Mall area", "practices": "Museum curation, educational programming, historical research", "treasures": "Women's history artifacts, archives, artworks, documents"}},
        "c": ["Women", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/1303",
        "_source": "manual"
    },

    # ═══ IMMIGRATION & IMMIGRANT RIGHTS ═══
    {
        "id": "hr-6149-119", "t": "Bill", "n": "H.R. 6149",
        "T": "<span style=\"color: #065F46;\">H.R. 6149:</span> FAIR Act (Fair Adjudication of Immigration Rights)",
        "s": "FAIR Act — Immigration Rights",
        "d": "2025-10-28",
        "a": "Trump II", "A": ["DOJ", "DHS"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 6149, 119th Congress. The FAIR Act (Fair Adjudication of Immigration Rights Act) seeks to reform the immigration court system to ensure fair and impartial adjudication of immigration cases. KEY PROVISIONS: The bill would establish an independent Article I immigration court system, separating immigration judges from the Department of Justice and shielding them from political pressure. It addresses chronic backlogs (currently over 3 million pending cases), ensures access to legal representation, and establishes due process protections for immigrants facing deportation proceedings. CONTEXT: Under the Trump II administration, immigration courts have faced increased political pressure, with reports of judges being evaluated on case completion rates rather than fair adjudication. The bill responds to these concerns by creating structural independence.",
        "I": {"Immigrant": {"people": "Immigrants, asylum seekers, immigration judges, attorneys", "places": "Immigration courts nationwide", "practices": "Immigration adjudication, due process, legal representation", "treasures": "Legal rights, due process protections, judicial independence"}},
        "c": ["Immigrant", "Latiné", "Asian American", "African-descendant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/6149",
        "_source": "manual"
    },
    {
        "id": "hr-2851-119", "t": "Bill", "n": "H.R. 2851",
        "T": "<span style=\"color: #065F46;\">H.R. 2851:</span> WISE Act (Welcoming Immigrants Safely and Equitably)",
        "s": "WISE Act — Immigrant Welcome",
        "d": "2025-04-10",
        "a": "Trump II", "A": ["DHS", "HHS"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 2851, 119th Congress. The WISE Act (Welcoming Immigrants Safely and Equitably Act) establishes a framework for welcoming immigrants while ensuring public safety and equitable resource distribution. The bill creates federal-local coordination mechanisms, community integration programs, and support services for newly arrived immigrants.",
        "I": {"Immigrant": {"people": "Immigrants, refugee communities, local governments", "places": "Communities receiving immigrants, integration centers", "practices": "Community integration, language access, social services", "treasures": "Immigrant cultural heritage, community bonds"}},
        "c": ["Immigrant", "Latiné", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/2851",
        "_source": "manual"
    },
    {
        "id": "hres-909-119", "t": "Resolution", "n": "H.Res. 909",
        "T": "<span style=\"color: #065F46;\">H.Res. 909:</span> Recognizing that immigrant justice and reproductive justice are inseparable",
        "s": "Immigrant & Reproductive Justice",
        "d": "2025-12-05",
        "a": "Trump II", "A": ["DHS", "HHS"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 909, 119th Congress. This resolution recognizes that immigrant justice and reproductive justice are inseparable and must be pursued together. It highlights the unique reproductive health challenges facing immigrant communities, including barriers to healthcare access, conditions in immigration detention, forced sterilization concerns, and the impact of immigration enforcement on pregnant individuals and families.",
        "I": {"Immigrant": {"people": "Immigrant women, detained individuals, families", "places": "Immigration detention facilities, communities", "practices": "Healthcare access, reproductive rights advocacy", "treasures": "Family unity, bodily autonomy, human dignity"}},
        "c": ["Immigrant", "Women", "Latiné"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/909",
        "_source": "manual"
    },
    {
        "id": "s-3702-119", "t": "Bill", "n": "S. 3702",
        "T": "<span style=\"color: #065F46;\">S. 3702:</span> Dignity for Detained Immigrants Act",
        "s": "Dignity for Detained Immigrants (Senate)",
        "d": "2026-01-28",
        "a": "Trump II", "A": ["DHS", "ICE"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: S. 3702, 119th Congress. The Dignity for Detained Immigrants Act establishes comprehensive standards for the treatment of individuals in immigration detention. KEY PROVISIONS: The bill mandates access to legal counsel, medical and mental health care, nutritious food, and sanitary living conditions. It prohibits the use of solitary confinement except in extreme circumstances, establishes oversight mechanisms, and requires regular inspections of detention facilities. It also addresses the specific needs of vulnerable populations including children, pregnant individuals, LGBTQ+ individuals, and people with disabilities. CONTEXT: Reports of inhumane conditions, medical neglect, and abuse in immigration detention have increased under the Trump II administration's expanded enforcement operations.",
        "I": {"Immigrant": {"people": "Detained immigrants, asylum seekers, families", "places": "ICE detention facilities, processing centers", "practices": "Detention standards, medical care, legal access", "treasures": "Human dignity, legal rights, family connections"}},
        "c": ["Immigrant", "Latiné", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/3702",
        "_source": "manual"
    },
    {
        "id": "hr-6397-119", "t": "Bill", "n": "H.R. 6397",
        "T": "<span style=\"color: #065F46;\">H.R. 6397:</span> Dignity for Detained Immigrants Act",
        "s": "Dignity for Detained Immigrants (House)",
        "d": "2025-11-13",
        "a": "Trump II", "A": ["DHS", "ICE"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 6397, 119th Congress. House companion to S. 3702. This bill establishes comprehensive standards for the treatment of individuals in immigration detention, mandating access to legal counsel, healthcare, and humane conditions.",
        "I": {"Immigrant": {"people": "Detained immigrants, asylum seekers", "places": "ICE detention facilities", "practices": "Detention standards, medical care, legal access", "treasures": "Human dignity, legal rights"}},
        "c": ["Immigrant", "Latiné"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/6397",
        "_source": "manual"
    },
    {
        "id": "hr-3101-119", "t": "Bill", "n": "H.R. 3101",
        "T": "<span style=\"color: #065F46;\">H.R. 3101:</span> SHIELD Act (Safeguarding Human rights and Immigrant Equality in Legal Deportation)",
        "s": "SHIELD Act — Deportation Safeguards",
        "d": "2025-04-30",
        "a": "Trump II", "A": ["DHS", "DOJ"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 3101, 119th Congress. The SHIELD Act establishes safeguards for human rights and equality in deportation proceedings, ensuring that individuals facing removal receive due process protections and are not deported to countries where they face persecution, torture, or death.",
        "I": {"Immigrant": {"people": "Immigrants facing deportation, asylum seekers", "places": "Immigration courts, detention facilities, communities", "practices": "Due process, legal representation, human rights protection", "treasures": "Legal rights, human dignity, family unity"}},
        "c": ["Immigrant", "Latiné", "African-descendant", "Asian American"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/3101",
        "_source": "manual"
    },
    {
        "id": "hr-1680-119", "t": "Bill", "n": "H.R. 1680",
        "T": "<span style=\"color: #065F46;\">H.R. 1680:</span> UPLIFT Act (Undocumented People Living in Fear Today)",
        "s": "UPLIFT Act — Undocumented Protection",
        "d": "2025-02-27",
        "a": "Trump II", "A": ["DHS"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 1680, 119th Congress. The UPLIFT Act addresses the needs and rights of undocumented individuals living in the United States, providing pathways to legal status and protections against exploitation and abuse.",
        "I": {"Immigrant": {"people": "Undocumented immigrants, mixed-status families", "places": "Communities nationwide", "practices": "Immigration status adjustment, community protection", "treasures": "Family unity, community stability, human dignity"}},
        "c": ["Immigrant", "Latiné", "Asian American"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1680",
        "_source": "manual"
    },
    {
        "id": "hr-4393-119", "t": "Bill", "n": "H.R. 4393",
        "T": "<span style=\"color: #065F46;\">H.R. 4393:</span> DIGNIDAD (Dignity) Act of 2025",
        "s": "DIGNIDAD Act — Immigrant Dignity",
        "d": "2025-07-09",
        "a": "Trump II", "A": ["DHS", "DOJ"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 4393, 119th Congress. The DIGNIDAD (Dignity) Act of 2025 establishes comprehensive protections for immigrants' dignity and rights throughout the immigration enforcement process. The Spanish word 'dignidad' means dignity, reflecting the bill's focus on Latiné immigrant communities disproportionately affected by enforcement actions.",
        "I": {"Immigrant": {"people": "Immigrants, Latiné communities, families", "places": "Communities, workplaces, enforcement zones", "practices": "Immigration enforcement reform, community protection", "treasures": "Human dignity, family unity, cultural continuity"}},
        "c": ["Immigrant", "Latiné"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/4393",
        "_source": "manual"
    },
    {
        "id": "s-391-119", "t": "Bill", "n": "S. 391",
        "T": "<span style=\"color: #065F46;\">S. 391:</span> Access to Counsel Act of 2025",
        "s": "Access to Counsel Act",
        "d": "2025-02-05",
        "a": "Trump II", "A": ["DOJ", "DHS"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: S. 391, 119th Congress. The Access to Counsel Act of 2025 guarantees the right to legal counsel for all individuals in immigration proceedings, regardless of their ability to pay. Currently, unlike in criminal proceedings, there is no right to appointed counsel in immigration court. Studies show that immigrants with legal representation are far more likely to receive fair outcomes. This bill would fund a nationwide system of legal representation, particularly benefiting asylum seekers, detained individuals, and unaccompanied minors.",
        "I": {"Immigrant": {"people": "Immigrants in proceedings, asylum seekers, unaccompanied minors", "places": "Immigration courts, detention facilities", "practices": "Legal representation, due process", "treasures": "Legal rights, access to justice"}},
        "c": ["Immigrant", "Latiné", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/391",
        "_source": "manual"
    },

    # ═══ REPRODUCTIVE RIGHTS ═══
    {
        "id": "s-422-119", "t": "Bill", "n": "S. 422",
        "T": "<span style=\"color: #065F46;\">S. 422:</span> Right to Contraception Act",
        "s": "Right to Contraception Act (Senate)",
        "d": "2025-02-06",
        "a": "Trump II", "A": ["HHS"],
        "S": "Pending — Referred to Committee on Health, Education, Labor, and Pensions",
        "L": "PROTECTIVE",
        "D": "BILL: S. 422, 119th Congress. The Right to Contraception Act establishes a federal statutory right to access and use contraception, protecting this right in the wake of the Dobbs v. Jackson decision and concerns about potential further erosion of reproductive rights. The bill prohibits states from restricting access to contraception and ensures insurance coverage. IMPACT: Restrictions on contraception access disproportionately affect low-income communities, communities of color, rural communities, and immigrant communities.",
        "I": {"Women": {"people": "Women, families, healthcare providers", "places": "Healthcare facilities, pharmacies", "practices": "Reproductive healthcare, family planning", "treasures": "Reproductive autonomy, healthcare access"}},
        "c": ["Women", "Low-income", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/422",
        "_source": "manual"
    },
    {
        "id": "hr-999-119", "t": "Bill", "n": "H.R. 999",
        "T": "<span style=\"color: #065F46;\">H.R. 999:</span> Right to Contraception Act",
        "s": "Right to Contraception Act (House)",
        "d": "2025-02-04",
        "a": "Trump II", "A": ["HHS"],
        "S": "Pending — Referred to Committee on Energy and Commerce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 999, 119th Congress. House companion to S. 422. Establishes a federal statutory right to access and use contraception.",
        "I": {"Women": {"people": "Women, families, healthcare providers", "places": "Healthcare facilities", "practices": "Reproductive healthcare, family planning", "treasures": "Reproductive autonomy, healthcare access"}},
        "c": ["Women", "Low-income", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/999",
        "_source": "manual"
    },
    {
        "id": "hconres-65-119", "t": "Resolution", "n": "H.Con.Res. 65",
        "T": "<span style=\"color: #065F46;\">H.Con.Res. 65:</span> Commending State and local governments for championing reproductive rights as human rights",
        "s": "Reproductive Rights as Human Rights",
        "d": "2025-07-23",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Energy and Commerce",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Con.Res. 65, 119th Congress. This concurrent resolution commends state and local governments that have championed reproductive rights as human rights, recognizing their efforts to protect access to reproductive healthcare in the post-Dobbs landscape.",
        "I": {"Women": {"people": "Women, families, healthcare providers", "places": "States and localities protecting reproductive rights", "practices": "Reproductive healthcare, advocacy", "treasures": "Reproductive autonomy, human rights"}},
        "c": ["Women", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/65",
        "_source": "manual"
    },

    # ═══ WORKERS' RIGHTS ═══
    {
        "id": "hr-3971-119", "t": "Bill", "n": "H.R. 3971",
        "T": "<span style=\"color: #065F46;\">H.R. 3971:</span> Domestic Workers Bill of Rights Act",
        "s": "Domestic Workers Bill of Rights (House)",
        "d": "2025-06-10",
        "a": "Trump II", "A": ["DOL"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 3971, 119th Congress. The Domestic Workers Bill of Rights Act extends federal labor protections to domestic workers — nannies, housekeepers, caregivers, and home health aides — who have historically been excluded from major labor laws including the National Labor Relations Act and the Fair Labor Standards Act. These exclusions trace directly to racial discrimination: domestic work was excluded from New Deal-era labor protections specifically because these occupations were predominantly held by Black and immigrant workers. Today, domestic workers are overwhelmingly women of color and immigrants. KEY PROVISIONS: The bill guarantees domestic workers minimum wage, overtime pay, meal and rest breaks, paid sick leave, protection from harassment and discrimination, and the right to organize.",
        "I": {"Immigrant": {"people": "Domestic workers, nannies, caregivers, home health aides", "places": "Private homes, communities", "practices": "Caregiving, housekeeping, home health care", "treasures": "Labor rights, dignity of work, economic justice"}},
        "c": ["Women", "Immigrant", "African-descendant", "Latiné", "Low-income"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/3971",
        "_source": "manual"
    },
    {
        "id": "s-3396-119", "t": "Bill", "n": "S. 3396",
        "T": "<span style=\"color: #065F46;\">S. 3396:</span> Domestic Workers Bill of Rights Act",
        "s": "Domestic Workers Bill of Rights (Senate)",
        "d": "2025-12-10",
        "a": "Trump II", "A": ["DOL"],
        "S": "Pending — Referred to Committee on Health, Education, Labor, and Pensions",
        "L": "PROTECTIVE",
        "D": "BILL: S. 3396, 119th Congress. Senate companion to H.R. 3971. Extends federal labor protections to domestic workers.",
        "I": {"Immigrant": {"people": "Domestic workers, caregivers", "places": "Private homes, communities", "practices": "Caregiving, housekeeping", "treasures": "Labor rights, economic justice"}},
        "c": ["Women", "Immigrant", "African-descendant", "Latiné", "Low-income"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/3396",
        "_source": "manual"
    },

    # ═══ VOTING RIGHTS ═══
    {
        "id": "s-2589-119", "t": "Bill", "n": "S. 2589",
        "T": "<span style=\"color: #065F46;\">S. 2589:</span> Expanding the VOTE Act",
        "s": "Expanding the VOTE Act (Senate)",
        "d": "2025-08-01",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Rules and Administration",
        "L": "PROTECTIVE",
        "D": "BILL: S. 2589, 119th Congress. The Expanding the VOTE Act strengthens voting rights and expands voter access, particularly for communities of color, language minorities, and rural communities disproportionately affected by voter suppression.",
        "I": {"All communities": {"people": "Voters, communities of color, language minorities", "places": "Polling places, election offices", "practices": "Voting, voter registration, civic participation", "treasures": "Voting rights, democratic participation"}},
        "c": ["African-descendant", "Latiné", "Indigenous/Tribal", "Asian American", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/2589",
        "_source": "manual"
    },
    {
        "id": "hr-4917-119", "t": "Bill", "n": "H.R. 4917",
        "T": "<span style=\"color: #065F46;\">H.R. 4917:</span> Expanding the VOTE Act",
        "s": "Expanding the VOTE Act (House)",
        "d": "2025-08-01",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on House Administration",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 4917, 119th Congress. House companion to S. 2589. Expands voting rights and voter access for underserved communities.",
        "I": {"All communities": {"people": "Voters, communities of color, language minorities", "places": "Polling places, election offices", "practices": "Voting, civic participation", "treasures": "Voting rights, democratic participation"}},
        "c": ["African-descendant", "Latiné", "Indigenous/Tribal", "Asian American", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/4917",
        "_source": "manual"
    },

    # ═══ LANGUAGE RIGHTS & ACCESS ═══
    {
        "id": "hr-1572-119", "t": "Bill", "n": "H.R. 1572",
        "T": "<span style=\"color: #065F46;\">H.R. 1572:</span> World LEAP Act (Language Education and Preservation)",
        "s": "World LEAP Act — Language Preservation",
        "d": "2025-02-25",
        "a": "Trump II", "A": ["ED", "STATE"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 1572, 119th Congress. The World LEAP Act supports language education and the preservation of world languages, including heritage languages spoken by immigrant and Indigenous communities in the United States.",
        "I": {"All communities": {"people": "Language communities, heritage speakers, students", "places": "Schools, language programs, communities", "practices": "Language education, heritage language preservation", "treasures": "Linguistic diversity, heritage languages, cultural knowledge"}},
        "c": ["Immigrant", "Indigenous/Tribal", "Asian American", "Latiné", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1572",
        "_source": "manual"
    },
    {
        "id": "hr-1772-119", "t": "Bill", "n": "H.R. 1772",
        "T": "<span style=\"color: #CA8A04;\">H.R. 1772:</span> Designation of English as the Official Language of the United States Act of 2025",
        "s": "English Official Language Act",
        "d": "2025-03-03",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "HARMFUL",
        "D": "BILL: H.R. 1772, 119th Congress. This bill would designate English as the official language of the United States, potentially eliminating federal requirements for multilingual government services, translated documents, and language access programs. IMPACT: The designation of an official language poses significant threats to immigrant communities, Indigenous language preservation, and language access in government services, healthcare, courts, and voting. It particularly affects Latiné, Asian American, Indigenous, and Pacific Islander communities whose members may have limited English proficiency. It could undermine the Voting Rights Act's language minority provisions, reduce access to justice, and chill heritage language use. CONTEXT: English-only legislation has been introduced repeatedly in Congress but has never passed. Under the Trump II administration, with its restrictionist immigration stance, such legislation takes on heightened significance.",
        "I": {"Immigrant": {"people": "Limited English proficiency communities, heritage language speakers", "places": "Government offices, courts, healthcare facilities, schools, voting sites", "practices": "Multilingual services, language access programs, heritage language education", "treasures": "Linguistic diversity, heritage languages, multilingual government services"}},
        "c": ["Immigrant", "Latiné", "Asian American", "Indigenous/Tribal", "Pacific Islander"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1772",
        "_source": "manual"
    },
    {
        "id": "hr-1862-119", "t": "Bill", "n": "H.R. 1862",
        "T": "<span style=\"color: #CA8A04;\">H.R. 1862:</span> English Language Unity Act of 2025",
        "s": "English Language Unity Act (House)",
        "d": "2025-03-06",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "HARMFUL",
        "D": "BILL: H.R. 1862, 119th Congress. The English Language Unity Act would establish English as the official language of the United States and mandate that all official government functions be conducted in English. Similar to H.R. 1772, this bill threatens language access and multilingual services.",
        "I": {"Immigrant": {"people": "LEP communities, heritage language speakers", "places": "Government offices, courts, schools", "practices": "Language access, multilingual services", "treasures": "Linguistic diversity, heritage languages"}},
        "c": ["Immigrant", "Latiné", "Asian American", "Indigenous/Tribal"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1862",
        "_source": "manual"
    },
    {
        "id": "s-542-119", "t": "Bill", "n": "S. 542",
        "T": "<span style=\"color: #CA8A04;\">S. 542:</span> English Language Unity Act of 2025",
        "s": "English Language Unity Act (Senate)",
        "d": "2025-02-13",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Homeland Security and Governmental Affairs",
        "L": "HARMFUL",
        "D": "BILL: S. 542, 119th Congress. Senate companion to H.R. 1862. Would establish English as the official language of the United States.",
        "I": {"Immigrant": {"people": "LEP communities, heritage language speakers", "places": "Government offices, courts, schools", "practices": "Language access, multilingual services", "treasures": "Linguistic diversity, heritage languages"}},
        "c": ["Immigrant", "Latiné", "Asian American", "Indigenous/Tribal"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/542",
        "_source": "manual"
    },
    {
        "id": "hr-1660-119", "t": "Bill", "n": "H.R. 1660",
        "T": "<span style=\"color: #065F46;\">H.R. 1660:</span> BEST Act (Bilingual Education and Students' Transformation)",
        "s": "BEST Act — Bilingual Education",
        "d": "2025-02-27",
        "a": "Trump II", "A": ["ED"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 1660, 119th Congress. The BEST Act supports bilingual education programs and recognizes the cognitive, cultural, and economic benefits of bilingualism and multilingualism.",
        "I": {"All communities": {"people": "Bilingual students, heritage language communities", "places": "Schools, bilingual education programs", "practices": "Bilingual education, heritage language instruction", "treasures": "Linguistic diversity, bilingual skills, cultural knowledge"}},
        "c": ["Immigrant", "Latiné", "Asian American", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/1660",
        "_source": "manual"
    },
    {
        "id": "hr-3728-119", "t": "Bill", "n": "H.R. 3728",
        "T": "<span style=\"color: #065F46;\">H.R. 3728:</span> Language Access in Transit Act",
        "s": "Language Access in Transit Act",
        "d": "2025-05-30",
        "a": "Trump II", "A": ["DOT"],
        "S": "Pending — Referred to Committee on Transportation and Infrastructure",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 3728, 119th Congress. The Language Access in Transit Act requires public transit agencies receiving federal funding to provide multilingual signage, announcements, and customer service materials in languages spoken by a significant number of riders in their service area.",
        "I": {"Immigrant": {"people": "LEP transit riders, immigrant communities", "places": "Public transit systems, bus stops, train stations", "practices": "Multilingual transit communication, language access", "treasures": "Language access, community mobility, public safety"}},
        "c": ["Immigrant", "Latiné", "Asian American"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/3728",
        "_source": "manual"
    },
    {
        "id": "hres-804-119", "t": "Resolution", "n": "H.Res. 804",
        "T": "<span style=\"color: #065F46;\">H.Res. 804:</span> Recognizing the importance of Spanish-language media in the United States",
        "s": "Spanish-Language Media Recognition",
        "d": "2025-10-28",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Energy and Commerce",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 804, 119th Congress. This resolution recognizes the importance of Spanish-language media in the United States, acknowledging its critical role in informing, educating, and connecting over 40 million Spanish speakers and the broader Latino community.",
        "I": {"Latiné": {"people": "Spanish-speaking communities, Latino media professionals", "places": "Media outlets, communities nationwide", "practices": "Spanish-language journalism, broadcasting, cultural programming", "treasures": "Spanish-language media infrastructure, cultural communication"}},
        "c": ["Latiné", "Immigrant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/804",
        "_source": "manual"
    },
    {
        "id": "hres-149-119", "t": "Resolution", "n": "H.Res. 149",
        "T": "<span style=\"color: #065F46;\">H.Res. 149:</span> Supporting the goals and ideals of International Mother Language Day",
        "s": "International Mother Language Day",
        "d": "2025-02-13",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Foreign Affairs",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 149, 119th Congress. This resolution supports the goals and ideals of International Mother Language Day (February 21) in bringing attention to the importance of preserving linguistic and cultural heritage through education. UNESCO established International Mother Language Day to promote linguistic diversity and multilingual education.",
        "I": {"All communities": {"people": "All linguistic communities, heritage language speakers", "places": "Schools, communities worldwide", "practices": "Mother language education, linguistic heritage preservation", "treasures": "World's languages, linguistic diversity, cultural knowledge"}},
        "c": ["All communities", "Indigenous/Tribal", "Immigrant"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/149",
        "_source": "manual"
    },
    {
        "id": "hr-3238-119", "t": "Bill", "n": "H.R. 3238",
        "T": "<span style=\"color: #065F46;\">H.R. 3238:</span> HABLA Act of 2025",
        "s": "HABLA Act — Language Access",
        "d": "2025-05-08",
        "a": "Trump II", "A": ["HHS", "DOJ"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 3238, 119th Congress. The HABLA Act (Helping to Advance Bilingual Liaisons and Access) improves language access in federal agencies and programs, ensuring that limited English proficiency individuals can access government services, healthcare, and legal proceedings.",
        "I": {"Immigrant": {"people": "LEP communities, immigrant families", "places": "Federal agencies, courts, healthcare facilities", "practices": "Language access services, interpretation, translation", "treasures": "Language access, equal access to services"}},
        "c": ["Immigrant", "Latiné", "Asian American"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/3238",
        "_source": "manual"
    },

    # ═══ EQUALITY & CIVIL RIGHTS ═══
    {
        "id": "hr-4373-119", "t": "Bill", "n": "H.R. 4373",
        "T": "<span style=\"color: #065F46;\">H.R. 4373:</span> Equality in Laws Act",
        "s": "Equality in Laws Act",
        "d": "2025-07-08",
        "a": "Trump II", "A": ["DOJ"],
        "S": "Pending — Referred to Committee on the Judiciary",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 4373, 119th Congress. The Equality in Laws Act seeks to eliminate legal distinctions based on sex, gender identity, and sexual orientation across federal law, ensuring equal treatment under the law for all individuals.",
        "I": {"All communities": {"people": "LGBTQ+ individuals, women, all Americans", "places": "Workplaces, schools, government agencies", "practices": "Equal protection, anti-discrimination", "treasures": "Civil rights, equality under law"}},
        "c": ["LGBTQ+", "Women", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/4373",
        "_source": "manual"
    },

    # ═══ INTERNATIONAL ═══
    {
        "id": "hr-2416-119", "t": "Bill", "n": "H.R. 2416",
        "T": "<span style=\"color: #065F46;\">H.R. 2416:</span> Taiwan International Solidarity Act",
        "s": "Taiwan International Solidarity (House)",
        "d": "2025-03-27",
        "a": "Trump II", "A": ["STATE"],
        "S": "Pending — Referred to Committee on Foreign Affairs",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 2416, 119th Congress. The Taiwan International Solidarity Act strengthens U.S. support for Taiwan's participation in international organizations, affirming Taiwan's right to international recognition and resisting efforts by the People's Republic of China to isolate Taiwan diplomatically. CULTURAL RELEVANCE: Taiwan is home to rich Indigenous Austronesian cultures, a vibrant democracy with extensive civil liberties protections, and significant cultural institutions. Supporting Taiwan's international participation also protects the cultural and political autonomy of its 23.5 million people.",
        "I": {"Asian American": {"people": "Taiwanese Americans, Asian American communities", "places": "Taiwan, international organizations", "practices": "Diplomatic engagement, international participation", "treasures": "Taiwanese democratic institutions, cultural heritage, Indigenous cultures"}},
        "c": ["Asian American"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/2416",
        "_source": "manual"
    },
    {
        "id": "s-2224-119", "t": "Bill", "n": "S. 2224",
        "T": "<span style=\"color: #065F46;\">S. 2224:</span> Taiwan International Solidarity Act",
        "s": "Taiwan International Solidarity (Senate)",
        "d": "2025-07-10",
        "a": "Trump II", "A": ["STATE"],
        "S": "Pending — Referred to Committee on Foreign Relations",
        "L": "PROTECTIVE",
        "D": "BILL: S. 2224, 119th Congress. Senate companion to H.R. 2416. Strengthens U.S. support for Taiwan's participation in international organizations.",
        "I": {"Asian American": {"people": "Taiwanese Americans", "places": "Taiwan, international bodies", "practices": "Diplomatic engagement", "treasures": "Taiwanese cultural and democratic heritage"}},
        "c": ["Asian American"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/2224",
        "_source": "manual"
    },

    # ═══ ARTS, EDUCATION, CULTURAL FUNDING ═══
    {
        "id": "hr-82-119", "t": "Bill", "n": "H.R. 82",
        "T": "<span style=\"color: #991B1B;\">H.R. 82:</span> Defund National Endowment for the Humanities Act of 2025",
        "s": "Defund NEH Act",
        "d": "2025-01-03",
        "a": "Trump II", "A": ["NEH"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "SEVERE",
        "D": "BILL: H.R. 82, 119th Congress. This bill would eliminate all federal funding for the National Endowment for the Humanities (NEH), effectively dismantling an agency that has supported humanities research, education, cultural preservation, and public programming since 1965. IMPACT: NEH funding is critical for preserving cultural heritage across all communities — supporting Indigenous language documentation, African American oral history projects, Latino cultural archives, Asian American historical research, rural library programs, and museum exhibitions. Defunding NEH would devastate cultural preservation efforts nationwide, particularly for underserved communities that lack alternative funding sources. NEH grants support thousands of institutions including museums, libraries, colleges, historical societies, and tribal organizations. CONTEXT: This bill aligns with broader administration efforts to reduce federal support for arts and humanities, including proposed cuts to the NEA, IMLS, and CPB.",
        "I": {"All communities": {"people": "Scholars, educators, museum staff, librarians, cultural organizations", "places": "Museums, libraries, universities, archives, tribal organizations", "practices": "Humanities research, cultural preservation, public programming, education", "treasures": "Cultural archives, historical collections, research, educational programs"}},
        "c": ["All communities", "Indigenous/Tribal", "African-descendant", "Latiné", "Asian American", "Rural"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/82",
        "_source": "manual"
    },
    {
        "id": "hr-2485-119", "t": "Bill", "n": "H.R. 2485",
        "T": "<span style=\"color: #065F46;\">H.R. 2485:</span> Arts Education for All Act",
        "s": "Arts Education for All Act",
        "d": "2025-03-31",
        "a": "Trump II", "A": ["ED", "NEA"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 2485, 119th Congress. The Arts Education for All Act establishes federal grant programs to ensure access to arts education — including visual arts, music, theater, dance, and media arts — for all K-12 students, particularly in underserved communities where arts programs have been cut due to budget constraints.",
        "I": {"All communities": {"people": "Students, arts educators, communities", "places": "K-12 schools, particularly underserved areas", "practices": "Arts education, creative expression, cultural learning", "treasures": "Artistic traditions, creative skills, cultural expression"}},
        "c": ["All communities", "Low-income", "African-descendant", "Latiné"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/2485",
        "_source": "manual"
    },
    {
        "id": "hr-5399-119", "t": "Bill", "n": "H.R. 5399",
        "T": "<span style=\"color: #065F46;\">H.R. 5399:</span> Equitable Arts Education Enhancement Act",
        "s": "Equitable Arts Education Act",
        "d": "2025-09-15",
        "a": "Trump II", "A": ["ED", "NEA"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 5399, 119th Congress. The Equitable Arts Education Enhancement Act focuses on reducing disparities in access to arts education, targeting resources to schools and communities where arts programs are most lacking.",
        "I": {"All communities": {"people": "Underserved students, arts educators", "places": "Under-resourced schools, rural and urban communities", "practices": "Arts education, equity programming", "treasures": "Artistic skills, cultural expression, creative development"}},
        "c": ["All communities", "Low-income", "African-descendant", "Latiné"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/5399",
        "_source": "manual"
    },
    {
        "id": "hr-3852-119", "t": "Bill", "n": "H.R. 3852",
        "T": "<span style=\"color: #065F46;\">H.R. 3852:</span> Reimagining Inclusive Arts Education Act",
        "s": "Inclusive Arts Education Act",
        "d": "2025-06-05",
        "a": "Trump II", "A": ["ED", "NEA"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 3852, 119th Congress. The Reimagining Inclusive Arts Education Act supports the development of arts education programs that are inclusive of diverse cultural traditions, abilities, and identities, ensuring that all students can participate in and benefit from arts education.",
        "I": {"All communities": {"people": "Students of all backgrounds and abilities", "places": "Schools, arts education programs", "practices": "Inclusive arts education, culturally responsive teaching", "treasures": "Diverse artistic traditions, inclusive creative spaces"}},
        "c": ["All communities", "Disabled"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/3852",
        "_source": "manual"
    },
    {
        "id": "hr-5009-119", "t": "Bill", "n": "H.R. 5009",
        "T": "<span style=\"color: #065F46;\">H.R. 5009:</span> Fine Arts Protection Act of 2025",
        "s": "Fine Arts Protection Act",
        "d": "2025-08-08",
        "a": "Trump II", "A": ["Smithsonian", "NEA"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 5009, 119th Congress. The Fine Arts Protection Act of 2025 establishes legal protections for fine arts and cultural property, including protections against destruction, deaccession, and loss of public art and cultural collections.",
        "I": {"Arts community": {"people": "Artists, museum professionals, cultural organizations", "places": "Museums, galleries, public art installations", "practices": "Art preservation, collection stewardship", "treasures": "Fine art collections, public art, cultural property"}},
        "c": ["Arts community", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/5009",
        "_source": "manual"
    },
    {
        "id": "hr-4754-119", "t": "Bill", "n": "H.R. 4754",
        "T": "<span style=\"color: #065F46;\">H.R. 4754:</span> Department of the Interior, Environment, and Related Agencies Appropriations Act, 2026 (House)",
        "s": "Interior Appropriations FY2026 (House)",
        "d": "2025-07-23",
        "a": "Trump II", "A": ["DOI", "EPA", "NEA", "NEH", "Smithsonian", "IMLS"],
        "S": "Pending — Referred to Committee on Appropriations",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 4754, 119th Congress. The House Interior, Environment, and Related Agencies Appropriations Act for FY2026 sets funding levels for the Department of the Interior, EPA, and cultural agencies including the NEA, NEH, Smithsonian Institution, and IMLS. SIGNIFICANCE: This is the primary vehicle for funding federal cultural programs, national parks, tribal programs, historic preservation, and environmental protections. Funding levels for NEA, NEH, Smithsonian, and IMLS directly determine the federal government's capacity to support cultural heritage preservation across all communities.",
        "I": {"All communities": {"people": "Museum staff, park rangers, cultural organizations, tribal communities", "places": "National parks, museums, libraries, tribal lands, cultural sites", "practices": "Cultural programming, historic preservation, arts funding", "treasures": "Federal cultural collections, national parks, historic sites"}},
        "c": ["All communities", "Indigenous/Tribal", "Arts community"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/4754",
        "_source": "manual"
    },
    {
        "id": "s-2431-119", "t": "Bill", "n": "S. 2431",
        "T": "<span style=\"color: #065F46;\">S. 2431:</span> Department of the Interior, Environment, and Related Agencies Appropriations Act, 2026 (Senate)",
        "s": "Interior Appropriations FY2026 (Senate)",
        "d": "2025-07-24",
        "a": "Trump II", "A": ["DOI", "EPA", "NEA", "NEH", "Smithsonian", "IMLS"],
        "S": "Pending — Reported by Senate Appropriations Committee",
        "L": "PROTECTIVE",
        "D": "BILL: S. 2431, 119th Congress. Senate companion to H.R. 4754. Sets funding levels for Interior, Environment, and cultural agencies for FY2026.",
        "I": {"All communities": {"people": "Cultural organizations, tribal communities, park visitors", "places": "National parks, museums, libraries, cultural sites", "practices": "Cultural programming, historic preservation", "treasures": "Federal cultural infrastructure, collections, sites"}},
        "c": ["All communities", "Indigenous/Tribal", "Arts community"],
        "U": "https://www.congress.gov/bill/119th-congress/senate-bill/2431",
        "_source": "manual"
    },
    {
        "id": "hr-6165-119", "t": "Bill", "n": "H.R. 6165",
        "T": "<span style=\"color: #065F46;\">H.R. 6165:</span> CREATIVE Act of 2025",
        "s": "CREATIVE Act — Arts Support",
        "d": "2025-10-22",
        "a": "Trump II", "A": ["NEA"],
        "S": "Pending — Referred to Committee on Education and the Workforce",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 6165, 119th Congress. The CREATIVE Act of 2025 strengthens federal support for creative industries, arts organizations, and individual artists, recognizing the arts sector's economic and cultural contributions to the United States.",
        "I": {"Arts community": {"people": "Artists, arts organizations, creative workers", "places": "Arts venues, studios, communities", "practices": "Artistic creation, cultural production, arts programming", "treasures": "American artistic heritage, creative economy"}},
        "c": ["Arts community", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/6165",
        "_source": "manual"
    },

    # ═══ KENNEDY CENTER ═══
    {
        "id": "hr-6925-119", "t": "Bill", "n": "H.R. 6925",
        "T": "<span style=\"color: #065F46;\">H.R. 6925:</span> Kennedy Center Protection Act",
        "s": "Kennedy Center Protection Act",
        "d": "2025-12-18",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Transportation and Infrastructure",
        "L": "PROTECTIVE",
        "D": "BILL: H.R. 6925, 119th Congress. The Kennedy Center Protection Act safeguards the John F. Kennedy Center for the Performing Arts from political interference, ensuring its continued operation as the nation's premier performing arts center. The bill responds to concerns about potential politicization of the Center and protects its mission to present and support the performing arts.",
        "I": {"Arts community": {"people": "Performing artists, audiences, cultural professionals", "places": "Kennedy Center, Washington D.C.", "practices": "Performing arts, cultural programming, arts education", "treasures": "Kennedy Center programs, performing arts heritage"}},
        "c": ["Arts community", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-bill/6925",
        "_source": "manual"
    },
    {
        "id": "hres-973-119", "t": "Resolution", "n": "H.Res. 973",
        "T": "<span style=\"color: #065F46;\">H.Res. 973:</span> Expressing the sense that the \"Donald J. Trump and the John F. Kennedy Memorial Center\" designation constitutes a violation of Federal law",
        "s": "Kennedy Center Renaming Violation",
        "d": "2026-01-22",
        "a": "Trump II", "A": [],
        "S": "Pending — Referred to Committee on Transportation and Infrastructure",
        "L": "PROTECTIVE",
        "D": "RESOLUTION: H.Res. 973, 119th Congress. This resolution expresses the sense of the House that the proposed designation of the Kennedy Center as the 'Donald J. Trump and the John F. Kennedy Memorial Center for the Performing Arts' constitutes a violation of federal law. The resolution argues that renaming the Center without proper Congressional authorization violates the statute establishing the Center and the naming conventions for federal buildings.",
        "I": {"Arts community": {"people": "Performing artists, audiences, Kennedy family", "places": "Kennedy Center, Washington D.C.", "practices": "Institutional integrity, performing arts programming", "treasures": "Kennedy Center's legacy, institutional independence"}},
        "c": ["Arts community", "All communities"],
        "U": "https://www.congress.gov/bill/119th-congress/house-resolution/973",
        "_source": "manual"
    },
]


def main():
    # Load existing data
    data = json.loads(DATA_PATH.read_text())

    # Remove Nevada Test Range entry
    data['legislation'] = [
        e for e in data['legislation']
        if e.get('id') != 'hr-1400-119'
    ]
    print(f"Removed hr-1400-119 (Nevada Test Range)")

    # Check for duplicates before adding
    existing_ids = {e.get('id') for e in data['legislation']}
    added = 0
    skipped = 0

    for entry in NEW_ENTRIES:
        if entry['id'] in existing_ids:
            print(f"  SKIP (exists): {entry['id']}")
            skipped += 1
            continue
        data['legislation'].append(entry)
        existing_ids.add(entry['id'])
        added += 1

    # Update meta
    total = sum(len(v) for k, v in data.items() if k != 'meta' and isinstance(v, list))
    data['meta']['total'] = total
    data['meta']['by_category']['legislation'] = len(data['legislation'])

    # Save
    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False))
    print(f"\nAdded {added} entries, skipped {skipped} duplicates")
    print(f"Total entries: {total}")
    print(f"Legislation entries: {len(data['legislation'])}")


if __name__ == '__main__':
    main()
