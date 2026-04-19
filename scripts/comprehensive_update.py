#!/usr/bin/env python3
"""
TCKC Threat Tracker - Comprehensive Update Automation
Pulls current data from all sources, creates entries, and publishes to GitHub

Usage:
    python comprehensive_update.py                    # Interactive mode
    python comprehensive_update.py --auto             # Fully automated
    python comprehensive_update.py --dry-run          # Preview without commit
"""

import json
import os
import re
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import argparse
from typing import Dict, List, Optional

# Configuration
TRACKER_DIR = Path(__file__).parent.parent
DATA_DIR = TRACKER_DIR / "data"
DATA_FILE = DATA_DIR / "data.json"
STATE_FILE = DATA_DIR / "state.json"

# ---------------------------------------------------------------------------
# INDIGENOUS PEOPLES REFERENCE DATABASE
# Comprehensive mapping of Indigenous peoples to every US state, territory,
# collectivity, and Compact of Free Association (COFA) nation where federal
# agencies govern cultural resources.
#
# Each jurisdiction lists:
#   - Federally recognized nations with current presence
#   - State-recognized nations
#   - Unrecognized nations with documented community presence
#   - Historically displaced/removed nations whose cultural resources remain
#   - Self-determined names and colonial-era names where both are in use
#
# Source framework: Federal Register, BIA tribal leaders directory, NCSL
# state-recognized tribes list, tribal nation websites, NPS cultural
# affiliations, NAGPRA notices of inventory completion.
# ---------------------------------------------------------------------------

INDIGENOUS_PEOPLES_BY_JURISDICTION = {
    # ── 50 STATES ──────────────────────────────────────────────────────────

    'Alabama': {
        'federally_recognized': [
            'Poarch Band of Creek Indians (Muscogee)',
        ],
        'state_recognized': [
            'MOWA Band of Choctaw Indians',
            'Star Clan of Muscogee Creeks',
            'Cherokee Tribe of Northeast Alabama',
            'Echota Cherokee Tribe of Alabama',
            'MaChis Lower Creek Indian Tribe',
            'Cher-O-Creek Intra Tribal Indians',
        ],
        'displaced_peoples': [
            'Muscogee (Creek) Nation — removed via Trail of Tears 1836; ancestral homeland covers central and eastern Alabama',
            'Cherokee — ancestral northeastern Alabama, removed 1838',
            'Chickasaw — ancestral northwestern Alabama, removed 1837',
            'Choctaw — ancestral southwestern Alabama, removed 1831',
        ],
        'cultural_resources': [
            'Moundville Archaeological Park — Mississippian ceremonial center (1000–1450 CE), one of largest in North America',
            'Russell Cave National Monument — 10,000+ years continuous habitation',
            'Bottle Creek Mounds — Mobile-Tensaw Delta, Mississippian period',
            'Florence Indian Mound — largest domiciliary mound in Tennessee Valley',
        ],
    },

    'Alaska': {
        'federally_recognized': [
            'Tlingit', 'Haida', 'Tsimshian',  # Southeast
            'Alutiiq/Sugpiaq', 'Unangan/Aleut',  # Aleutian/Kodiak
            'Yup\'ik', 'Cup\'ik',  # Western
            'Iñupiaq/Inupiat',  # North Slope/Northwest Arctic
            'Athabascan/Dene (Gwich\'in, Koyukon, Tanana, Ahtna, Dena\'ina, Tanacross, Upper Tanana, Hän, Holikachuk, Deg Hit\'an, Kuskokwim)',
            'Eyak',
            'Yupik (St. Lawrence Island/Siberian Yupik)',
            # 229 federally recognized tribal entities in Alaska
        ],
        'cultural_concepts': [
            'Subsistence way of life — legally protected under ANILCA Title VIII, inseparable from cultural identity',
            'Potlatch/Ku.éex\' — Tlingit/Haida ceremonial redistribution and memorial',
            'Nalukataq — Iñupiaq whaling festival, blanket toss',
            'Yup\'ik Yuraq — dance festival, ceremonial mask traditions',
            'Seal Party/Kevgiq — intervillage Messenger Feast',
        ],
        'cultural_resources': [
            'Aniakchak National Monument — ancestral Sugpiaq territory',
            'Cape Krusenstern — 6,000+ years of Iñupiaq coastal habitation',
            'Sitka National Historical Park — Tlingit battle site and totem poles',
            'Alutiiq Museum (Kodiak) — community-governed collection',
            'Alaska Native Heritage Center (Anchorage)',
        ],
    },

    'Arizona': {
        'federally_recognized': [
            'Navajo Nation (Diné)',
            'Tohono O\'odham Nation',
            'Gila River Indian Community (Akimel O\'odham/Pee-Posh)',
            'Salt River Pima-Maricopa Indian Community',
            'Ak-Chin Indian Community (O\'odham)',
            'Hopi Tribe',
            'White Mountain Apache Tribe (Ndee)',
            'San Carlos Apache Tribe',
            'Tonto Apache Tribe',
            'Yavapai-Apache Nation',
            'Fort McDowell Yavapai Nation',
            'Yavapai-Prescott Indian Tribe',
            'Havasupai Tribe',
            'Hualapai Tribe',
            'Cocopah Tribe',
            'Quechan Tribe (Fort Yuma)',
            'Colorado River Indian Tribes (Mohave, Chemehuevi, Hopi, Navajo)',
            'Fort Mojave Indian Tribe',
            'Pascua Yaqui Tribe',
            'Kaibab Band of Paiute Indians',
            'San Juan Southern Paiute Tribe',
        ],
        'cultural_concepts': [
            'Hózhó — Diné (Navajo) foundational concept: harmony, beauty, balance, the ideal state of being',
            'Diné Bikéyah — Navajo homeland defined by four sacred mountains',
            'Katsina/Kachina — Hopi spiritual beings; ceremonies from winter solstice through Niman in July',
            'Blessingway (Hózhóójí) — foundational Navajo ceremony for harmony and protection',
            'Enemyway (Anaʼí Ndáá\') — Navajo ceremony for spiritual cleansing',
            'Kinaalda — Navajo coming-of-age ceremony for young women',
            'I\'itoi / Elder Brother — O\'odham creator figure, Man in the Maze',
            'Sunrise Ceremony (na\'ii\'ees) — Apache coming-of-age ceremony',
        ],
        'cultural_resources': [
            'Canyon de Chelly National Monument — continuous Navajo habitation, Ancestral Puebloan ruins',
            'Casa Grande Ruins National Monument — Hohokam/Ancestral Sonoran Desert People',
            'Montezuma Castle/Montezuma Well — Sinagua, Southern Tonto, Yavapai',
            'Tuzigoot National Monument — Sinagua pueblo',
            'Navajo National Monument (Betatakin, Keet Seel) — Ancestral Puebloan',
            'Wupatki National Monument — ancestral Hopi, Sinagua',
            'Walnut Canyon — Sinagua cliff dwellings',
            'Pipe Spring National Monument — Kaibab Paiute',
            'Organ Pipe Cactus — Tohono O\'odham ancestral corridor',
            'Heard Museum (Phoenix) — major Indigenous arts institution',
            'Oak Flat/Chi\'chil Biłdagoteel — Apache sacred site threatened by Resolution Copper mine',
        ],
    },

    'Arkansas': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Quapaw (Ogáxpa) — original people of the Arkansas River confluence; removed to Indian Territory 1833',
            'Caddo — ancestral southwestern Arkansas, Red River region; removed 1835',
            'Osage (Wazhazhe) — ancestral northwestern Arkansas and Ozarks; removed to Indian Territory',
            'Cherokee — briefly relocated to Arkansas 1817–1828 before further removal to Indian Territory',
            'Tunica — ancestral eastern Arkansas; now Tunica-Biloxi Tribe in Louisiana',
        ],
        'cultural_resources': [
            'Toltec Mounds State Park — Plum Bayou culture ceremonial center (600–1050 CE)',
            'Parkin Archeological State Park — Casqui province, likely first contact site with de Soto 1541',
            'Spiro Mounds connection — Caddo cultural sphere trade network extending into Arkansas',
            'Poverty Point World Heritage Site connection — Lower Mississippi Valley trade network',
            'Trail of Tears National Historic Trail — Cherokee removal route through Arkansas',
            'Blanchard Springs Caverns — Osage spiritual significance',
        ],
    },

    'California': {
        'federally_recognized': [
            'Yurok Tribe', 'Karuk Tribe', 'Hoopa Valley Tribe (Hupa)',
            'Round Valley Indian Tribes (Yuki, Concow, Little Lake Pomo, Nomlaki, Wailaki, Pit River)',
            'Pomo (multiple rancherias)', 'Miwok (multiple bands)',
            'Chumash (Santa Ynez Band)',
            'Cahuilla (Agua Caliente, Augustine, Cabazon, Morongo, Torres Martinez, others)',
            'Luiseño (Pechanga, Pauma, Pala, Rincon, La Jolla, Soboba)',
            'Serrano (San Manuel Band)', 'Kumeyaay (multiple bands)',
            'Washoe Tribe', 'Mono/Monache', 'Tule River Tribe',
            'Big Pine Paiute', 'Bishop Paiute', 'Fort Independence Paiute',
            'Lone Pine Paiute-Shoshone', 'Timbisha Shoshone',
            'Pit River Tribe (Achomawi/Atsugewi)',
            'Wiyot Tribe', 'Tolowa Dee-ni\' Nation',
            'Quartz Valley Indian Community (Shasta, Karuk, Klamath)',
            'Resighini Rancheria', 'Trinidad Rancheria',
            'Cher-Ae Heights Indian Community (Trinidad)',
            # 109 federally recognized entities in California
        ],
        'unrecognized_with_presence': [
            'Ohlone/Muwekma Ohlone — San Francisco Bay Area; petition for federal recognition pending since 1989',
            'Tongva/Gabrieleño — Los Angeles Basin ancestral people; no federal recognition despite continuous presence',
            'Juaneño Band of Mission Indians (Acjachemen) — Orange County/San Juan Capistrano',
            'Esselen — Monterey/Big Sur coast; recently restored land at Fort Ord',
            'Chumash (other non-federally-recognized bands)',
            'Tataviam — northern Los Angeles County/Santa Clarita Valley',
            'Kizh/Gabrieleño — distinct from Tongva; Los Angeles area',
            'Amah Mutsun Tribal Band — Monterey Bay/San Juan Bautista',
        ],
        'cultural_concepts': [
            'Acorn economy — oak woodland management and acorn processing as civilizational foundation',
            'Controlled burning/cultural fire — California tribal land management practiced for millennia',
            'Kuksu ceremonial complex — Central California spiritual tradition',
            'Toloache (Jimsonweed) ceremony — Luiseño, Gabrieleño, Chumash initiation',
            'World Renewal ceremonies — Yurok, Karuk, Hupa (Jump Dance, Brush Dance, Deerskin Dance)',
            'Tomol — Chumash ocean-going plank canoe; Brotherhood of the Tomol',
        ],
        'cultural_resources': [
            'Channel Islands National Park — Chumash ancestral islands, oldest human remains in Americas (Arlington Springs)',
            'Lava Beds National Monument — Modoc ancestral territory, Modoc War 1872-73',
            'Point Reyes National Seashore — Coast Miwok ancestral territory',
            'Joshua Tree National Park — Serrano, Chemehuevi, Cahuilla',
            'Death Valley National Park — Timbisha Shoshone homeland',
            'Sequoia/Kings Canyon — Monache, Yokuts, Western Shoshone',
            'Yosemite — Ahwahneechee (Southern Sierra Miwok), Mono Paiute',
            'Alcatraz Island — 1969-71 Indigenous occupation, pan-Indian movement landmark',
        ],
    },

    'Colorado': {
        'federally_recognized': [
            'Ute Mountain Ute Tribe',
            'Southern Ute Indian Tribe',
        ],
        'displaced_peoples': [
            'Ute (Núuchiu) — ancestral homeland covered most of western Colorado; Meeker Massacre 1879 and forced removal reduced territory by 95%',
            'Arapaho (Hinono\'eiteen) — eastern Colorado plains; removed after Sand Creek Massacre 1864',
            'Cheyenne (Tsitsistas) — eastern Colorado plains; Sand Creek Massacre 1864',
            'Jicarilla Apache — southwestern Colorado',
            'Comanche — southeastern Colorado plains',
            'Kiowa — southeastern Colorado plains',
            'Pueblo peoples — ancestral connection to Mesa Verde, Chimney Rock, and San Luis Valley',
        ],
        'cultural_resources': [
            'Mesa Verde National Park — Ancestral Puebloan cliff dwellings (600–1300 CE); 26 modern pueblos claim cultural affiliation',
            'Chimney Rock National Monument — Ancestral Puebloan great house, astronomical alignment',
            'Canyons of the Ancients National Monument — highest known density of archaeological sites in US',
            'Sand Creek Massacre National Historic Site — Cheyenne and Arapaho, November 29, 1864',
            'Hovenweep National Monument — Ancestral Puebloan towers',
            'Great Sand Dunes National Park — Ute, Apache, Comanche connections',
        ],
    },

    'Connecticut': {
        'federally_recognized': [
            'Mashantucket Pequot Tribal Nation',
            'Mohegan Tribe',
        ],
        'state_recognized': [
            'Schaghticoke Tribal Nation — federal recognition denied 2004 under controversial circumstances',
            'Golden Hill Paugussett Tribal Nation',
            'Eastern Pequot Tribal Nation — federal recognition denied 2005',
        ],
        'displaced_peoples': [
            'Pequot — Mystic Massacre 1637 and Pequot War nearly destroyed the nation',
            'Nipmuc — ancestral eastern Connecticut',
            'Quinnipiac — New Haven area, displaced by English colonization',
            'Mattabesett — central Connecticut River valley',
            'Podunk — Hartford area',
            'Tunxis — Farmington River valley',
            'Wangunk — Middletown area',
        ],
        'cultural_resources': [
            'Mashantucket Pequot Museum & Research Center — largest tribal museum in US',
            'Fort Hill (Mystic) — Pequot War / Mystic Massacre site 1637',
        ],
    },

    'Delaware': {
        'federally_recognized': [],
        'state_recognized': [
            'Lenape Indian Tribe of Delaware',
            'Nanticoke Indian Tribe',
        ],
        'displaced_peoples': [
            'Lenape (Delaware) — original people of the entire Delaware Valley; the "grandfather" nation of Algonquian peoples; removed westward through multiple forced relocations 1737–1867 (Walking Purchase fraud of 1737)',
            'Nanticoke — ancestral Delmarva Peninsula; maintain community in Indian River area',
            'Assateague — coastal people, Delmarva Peninsula',
        ],
        'cultural_resources': [
            'Island Field Site — 1,000+ year old Nanticoke/Lenape burial ground',
            'Nanticoke Indian Museum — Millsboro, community-governed',
            'Iron Hill — Lenape quartzite quarry site, ancient tool production',
        ],
    },

    'Florida': {
        'federally_recognized': [
            'Seminole Tribe of Florida',
            'Miccosukee Tribe of Indians of Florida',
        ],
        'displaced_peoples': [
            'Calusa — southwestern Florida, powerful chiefdom; destroyed by Spanish colonization and slave raids by 1700s',
            'Timucua — northern/central Florida, once 200,000+ people; destroyed by Spanish missions, disease, and English slave raids',
            'Apalachee — panhandle Florida; destroyed by English-Creek raids 1704; descendants among modern Creek/Seminole',
            'Tequesta — southeastern Florida / Miami area; destroyed by 1800',
            'Ais — central Atlantic coast; destroyed by 1700s',
            'Tocobaga — Tampa Bay area; destroyed by Spanish contact',
            'Jeaga — southeastern coast/Jupiter area',
            'Muscogee (Creek) — many Seminole descend from Creek people who migrated to Florida in 1700s',
        ],
        'cultural_concepts': [
            'Seminole patchwork — textile art tradition developed during Everglades resistance period',
            'Chickee — Seminole open-sided dwelling adapted to Everglades environment during resistance era',
            'Green Corn Ceremony (Busk) — annual renewal ceremony shared with Muscogee tradition',
            'Unconquered — Seminole self-designation; never signed a peace treaty with the US',
        ],
        'cultural_resources': [
            'Everglades National Park — Miccosukee and Seminole homeland; Tree Islands as habitation sites',
            'Big Cypress National Preserve — Seminole ancestral territory',
            'Canaveral National Seashore — Ais and Timucua shell middens',
            'De Soto National Memorial — contact site, Tocobaga/Calusa territory',
            'Fort Matanzas — Timucua territory, Spanish colonial period',
            'Castillo de San Marcos — built with coquina by Timucua and other Indigenous forced labor',
            'Crystal River Archaeological State Park — pre-Columbian ceremonial center 500 BCE–1400 CE',
            'Ah-Tah-Thi-Ki Museum — Seminole tribal museum, Big Cypress',
            'Pineland Site — Calusa capital, ceremonial shell mound complex',
            'Key Marco/Marco Island — Calusa carved wooden artifacts, one of most significant archaeological finds in Southeast',
        ],
    },

    'Georgia': {
        'federally_recognized': [],
        'state_recognized': [
            'Georgia Tribe of Eastern Cherokee',
            'Lower Muskogee Creek Tribe',
        ],
        'displaced_peoples': [
            'Muscogee (Creek) — central and southern Georgia was the heart of the Creek Confederacy; removed 1836',
            'Cherokee — northern Georgia including Dahlonega gold fields; removal forced by Georgia Guard and Trail of Tears 1838',
            'Hitchiti — central Georgia, absorbed into Creek Confederacy',
            'Yuchi (Euchee) — northern Georgia; removed with Creek',
            'Yamasee — coastal Georgia; Yamasee War 1715–17 shattered the nation',
            'Guale — coastal Georgia/Sea Islands; destroyed by Spanish mission system and English raids',
        ],
        'cultural_resources': [
            'Ocmulgee Mounds National Historical Park — 17,000 years of continuous human habitation; Muscogee ancestral ceremonial center with earth lodge',
            'Etowah Indian Mounds — Mississippian ceremonial center (1000–1550 CE), marble statues',
            'Kolomoki Mounds — Woodland period (350–750 CE)',
            'Fort Frederica — colonial-era conflicts affecting Guale and Yamasee',
            'Trail of Tears National Historic Trail — Cherokee removal routes through Georgia',
            'New Echota State Historic Site — last capital of the Cherokee Nation before removal',
            'Sapelo Island — Guale mission sites, also Gullah/Geechee heritage',
            'Rock Eagle Effigy Mound — Woodland period quartz effigy',
        ],
    },

    'Hawaii': {
        'federally_recognized': [],  # Native Hawaiians have unique political status under federal law but no tribal recognition
        'indigenous_peoples': [
            'Kānaka Maoli / Kānaka ʻŌiwi (Native Hawaiians) — Indigenous Polynesian people of the Hawaiian Islands',
        ],
        'cultural_concepts': [
            'Aloha ʻāina — love of the land; foundational concept connecting people, land, and spiritual practice',
            'Mālama ʻāina — stewardship/care of the land',
            'Kapu system — sacred law governing social, spiritual, and ecological relationships (pre-1819)',
            'Ahupuaʻa — traditional land division from mountain to sea, integrating all ecological zones',
            'Hoʻoponopono — practice of reconciliation and forgiveness',
            'Moʻolelo — oral history, genealogical narrative, story traditions',
            'Mana — spiritual power inherent in people, places, and objects',
            'ʻOhana — extended family as fundamental social unit',
        ],
        'cultural_resources': [
            'Puʻuhonua o Hōnaunau National Historical Park — sacred place of refuge',
            'Haleakalā National Park — sacred summit, Maui',
            'Hawaiʻi Volcanoes National Park — Pele, Kīlauea, spiritual landscape',
            'Kalaupapa National Historical Park — leprosy/Hansen\'s disease settlement, Native Hawaiian exile',
            'Pearl Harbor / Puʻuloa — Native Hawaiian fishpond site, spiritual significance predating military use',
            'Iolani Palace — seat of Hawaiian Kingdom, National Historic Landmark',
            'Mauna Kea/Maunakea — sacred summit, ongoing conflict over telescope construction',
            'Bishop Museum — largest collection of Polynesian cultural artifacts',
            'Heiau (temples) — sacred stone platform temples throughout islands',
            'Loko iʻa (fishponds) — Indigenous aquaculture technology, over 400 historically',
        ],
    },

    'Idaho': {
        'federally_recognized': [
            'Shoshone-Bannock Tribes (Fort Hall)',
            'Nez Perce Tribe (Nimiipuu)',
            'Coeur d\'Alene Tribe (Schitsu\'umsh)',
            'Shoshone-Paiute Tribes (Duck Valley)',
            'Kootenai Tribe of Idaho (Ktunaxa)',
        ],
        'cultural_concepts': [
            'Camas — blue camas lily root as staple food and cultural keystone for Nez Perce, Shoshone-Bannock',
            'Nimiipuu — "The People," Nez Perce self-designation',
            'Appaloosa horse — bred by Nez Perce, integral to culture',
        ],
        'cultural_resources': [
            'Nez Perce National Historical Park — 38 sites across Idaho, Oregon, Washington, Montana',
            'Craters of the Moon — Shoshone spiritual landscape',
            'City of Rocks — Shoshone ancestral territory, California Trail',
            'Camas Prairie — Nez Perce traditional gathering grounds',
            'Bear River Massacre Site (1863) — Shoshone, deadliest massacre in US western expansion',
        ],
    },

    'Illinois': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Illini/Illiniwek Confederacy (Peoria, Kaskaskia, Cahokia, Tamaroa, Michigamea) — the state\'s namesake people; removed to Indian Territory by 1832',
            'Potawatomi (Bodéwadmi) — northeastern Illinois including Chicago area; removed 1838 (Potawatomi Trail of Death)',
            'Kickapoo — central Illinois; removed 1830s',
            'Shawnee — southern Illinois',
            'Miami (Myaamia) — eastern Illinois',
            'Ho-Chunk/Winnebago — northern Illinois',
            'Sauk (Thakiwaki) and Meskwaki (Fox) — northwestern Illinois; Black Hawk War 1832',
            'Ojibwe/Chippewa — northeastern corner',
        ],
        'cultural_resources': [
            'Cahokia Mounds World Heritage Site — largest pre-Columbian settlement north of Mexico (1050–1350 CE), Monks Mound is largest earthen structure in Americas; Mississippian civilization',
            'Dickson Mounds Museum — Middle Mississippian village',
            'Starved Rock State Park — Illini/French colonial history; site of Illini last stand',
            'Fort de Chartres — French-Illini colonial site',
            'Chicago portage — Potawatomi homeland, strategic continental watershed',
            'Black Hawk State Historic Site — Sauk village Saukenuk',
        ],
    },

    'Indiana': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Miami (Myaamia) — central Indiana, the state\'s principal Indigenous nation; most removed 1846, some remained',
            'Potawatomi (Bodéwadmi) — northern Indiana; Trail of Death forced removal 1838',
            'Lenape (Delaware) — eastern Indiana; removed westward 1820s',
            'Shawnee — southern Indiana',
            'Kickapoo — western Indiana',
            'Wea — Wabash Valley (Miami-allied)',
            'Piankashaw — southern Indiana (Miami-allied)',
        ],
        'cultural_resources': [
            'Angel Mounds State Historic Site — Mississippian town (1100–1450 CE)',
            'Mounds State Park (Anderson) — Adena-Hopewell earthworks',
            'Indiana Dunes National Park — Potawatomi ancestral territory',
            'Prophetstown State Park — Shawnee Prophet Tenskwatawa\'s village',
            'Tippecanoe Battlefield — 1811 battle site, Shawnee/Tecumseh\'s confederacy',
        ],
    },

    'Iowa': {
        'federally_recognized': [
            'Meskwaki Nation (Sac and Fox Tribe of the Mississippi in Iowa) — uniquely purchased back their own land in 1856',
        ],
        'displaced_peoples': [
            'Ioway (Báxoje) — the state\'s namesake people; removed to Kansas/Nebraska/Oklahoma',
            'Sauk (Thakiwaki) — eastern Iowa; Black Hawk War removal 1832',
            'Meskwaki (Fox) — some remained (see above), most removed',
            'Omaha — western Iowa',
            'Otoe-Missouria — southwestern Iowa',
            'Winnebago/Ho-Chunk — northeastern Iowa; Neutral Ground period',
            'Santee Dakota — northwestern Iowa',
        ],
        'cultural_resources': [
            'Effigy Mounds National Monument — over 200 animal-shaped mounds (Woodland period)',
            'Blood Run National Historic Landmark — Oneota/Ioway village (1500–1700), pipestone',
            'Toolesboro Mounds — Hopewell culture',
            'Meskwaki Settlement (Tama) — only tribally owned land in Iowa, purchased by the nation itself',
        ],
    },

    'Kansas': {
        'federally_recognized': [
            'Prairie Band Potawatomi Nation',
            'Kickapoo Tribe in Kansas',
            'Iowa Tribe of Kansas and Nebraska',
            'Sac and Fox Nation of Missouri in Kansas and Nebraska',
        ],
        'displaced_peoples': [
            'Kaw/Kanza — the state\'s namesake people; Council Grove was last Kansas homeland before removal to Oklahoma 1873',
            'Osage (Wazhazhe) — southeastern Kansas; removed to Indian Territory',
            'Wichita — south-central Kansas',
            'Pawnee (Chatiks si chatiks) — north-central Kansas; removed to Oklahoma',
            'Comanche — western Kansas',
            'Kiowa — western Kansas',
            'Cheyenne — western Kansas',
            'Arapaho — western Kansas',
            'Shawnee — eastern Kansas (temporary relocation before further removal)',
            'Delaware/Lenape — eastern Kansas (temporary relocation)',
            'Wyandot — eastern Kansas (temporary relocation)',
        ],
        'cultural_resources': [
            'Council Grove — Kaw/Kanza last homeland, Santa Fe Trail',
            'Fort Larned National Historic Site — Southern Cheyenne, Kiowa, Comanche treaty context',
            'El Quartelejo Pueblo Ruins — northernmost pueblo in Americas, Taos Pueblo refugees',
            'Pawnee Indian Museum State Historic Site — ceremonial earth lodge',
            'Allegawaho Memorial Heritage Park — Kaw burial grounds and village',
        ],
    },

    'Kentucky': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Shawnee (Shawandasse) — primary nation of Kentucky; Boonesborough and colonial conflicts; removed by 1830s',
            'Cherokee — eastern Kentucky, hunting grounds; "dark and bloody ground" is a colonial mischaracterization',
            'Chickasaw — western Kentucky (Jackson Purchase area)',
            'Osage — western Kentucky',
            'Yuchi — eastern Kentucky',
        ],
        'cultural_resources': [
            'Mammoth Cave National Park — Indigenous use spanning 5,000+ years; ancient mining with cane torches',
            'Wickliffe Mounds — Mississippian village (1100–1350 CE)',
            'Indian Fort Mountain — ancient stone enclosure, ceremonial site',
            'Adena Park/C&O Mounds — Adena culture burial mounds',
            'Cumberland Gap National Historical Park — Shawnee/Cherokee migration and hunting corridor',
        ],
    },

    'Louisiana': {
        'federally_recognized': [
            'Chitimacha Tribe of Louisiana',
            'Coushatta Tribe of Louisiana',
            'Jena Band of Choctaw Indians',
            'Tunica-Biloxi Tribe',
        ],
        'state_recognized': [
            'Adai Caddo Indians',
            'Biloxi-Chitimacha-Choctaw (Isle de Jean Charles Band) — America\'s first climate refugees',
            'Choctaw-Apache Tribe of Ebarb',
            'Clifton Choctaw',
            'Four Winds Tribe Louisiana Cherokee Confederacy',
            'Grand Caillou/Dulac Band of Biloxi-Chitimacha-Choctaw',
            'Louisiana Band of Choctaw',
            'Natchitoches Tribe',
            'Pointe-au-Chien Indian Tribe',
            'United Houma Nation',
        ],
        'displaced_peoples': [
            'Natchez — Natchez Bluffs area; destroyed as a polity by French in 1730 Natchez War; survivors absorbed into Creek, Cherokee, Chickasaw',
            'Caddo — northwestern Louisiana, Red River; removed to Texas then Indian Territory',
            'Atakapa — southwestern Louisiana coast',
            'Bayougoula — lower Mississippi',
            'Houma — maintain large community in Terrebonne/Lafourche parishes without federal recognition',
        ],
        'cultural_resources': [
            'Poverty Point World Heritage Site — 3,700-year-old monumental earthwork complex, oldest in North America',
            'Marksville State Historic Site — Hopewell-related mounds',
            'Cane River National Heritage Area — Natchitoches and Caddo cultural landscape',
            'Jean Lafitte NHP Chalmette — multi-cultural site including Indigenous history',
            'Isle de Jean Charles — disappearing island, climate displacement of Biloxi-Chitimacha-Choctaw',
            'Chitimacha double-weave river cane baskets — among finest Indigenous textile arts in the world',
        ],
    },

    'Maine': {
        'federally_recognized': [
            'Penobscot Nation',
            'Passamaquoddy Tribe (Sipayik and Motahkomikuk)',
            'Houlton Band of Maliseet Indians (Wolastoqiyik)',
            'Mi\'kmaq Nation (Aroostook Band)',
        ],
        'cultural_concepts': [
            'Wabanaki — "People of the Dawnland," collective identity of Maine\'s four nations',
            'Wabanaki Confederacy — alliance including Penobscot, Passamaquoddy, Maliseet, Mi\'kmaq, Abenaki',
            'Brown ash basket making — endangered tradition due to emerald ash borer; UNESCO consideration',
        ],
        'cultural_resources': [
            'Acadia National Park — Wabanaki ancestral territory, Pemetic ("sloping land")',
            'Katahdin/Ktaadn — Penobscot sacred mountain, dwelling of storm spirit Pamola',
            'Abbe Museum — Wabanaki cultural institution, Bar Harbor',
            'Indian Island — Penobscot Nation homeland, Penobscot River',
        ],
    },

    'Maryland': {
        'federally_recognized': [],
        'state_recognized': [
            'Piscataway Indian Nation',
            'Piscataway Conoy Tribe',
            'Accohannock Indian Tribe',
            'Nause-Waiwash Band of Indians',
            'Youghiogheny Band of the Shawnee Nation',
        ],
        'displaced_peoples': [
            'Piscataway (Conoy) — ancestral people of the Potomac River and Chesapeake Bay western shore; maintain continuous community presence but lack federal recognition',
            'Nanticoke — Eastern Shore; maintain community in Delaware',
            'Susquehannock — northern Maryland; destroyed by colonial warfare and Iroquois attacks by 1675',
            'Shawnee — western Maryland',
            'Pocomoke — Eastern Shore',
            'Assateague — coastal Maryland/Virginia border',
        ],
        'cultural_resources': [
            'Piscataway Park — NPS site at Piscataway ancestral homeland, directly across Potomac from Mount Vernon',
            'Nassawango Iron Furnace — Pocomoke area, Indigenous landscape',
            'Chesapeake Bay — Algonquian name, the bay itself as cultural landscape',
            'St. Mary\'s City — colonial capital, site of earliest Piscataway-English encounter',
            'Biscayne National Park connection — Nanticoke trade networks',
        ],
    },

    'Massachusetts': {
        'federally_recognized': [
            'Mashpee Wampanoag Tribe — "People of the First Light"',
            'Wampanoag Tribe of Gay Head (Aquinnah) — Martha\'s Vineyard',
        ],
        'state_recognized': [
            'Nipmuc Tribal Council',
            'Chappaquiddick Tribe of the Wampanoag Nation',
        ],
        'displaced_peoples': [
            'Massachusett — the state\'s namesake people; devastated by 1616–19 epidemic and colonial displacement',
            'Nauset — Cape Cod; absorbed into Mashpee Wampanoag',
            'Pocumtuck — Connecticut River valley; destroyed by English-Mohawk alliance 1660s–70s',
            'Nipmuc — central Massachusetts; Praying Towns, King Philip\'s War devastation',
            'Pennacook — northern Massachusetts',
        ],
        'cultural_concepts': [
            'Wampum — shell beads as record-keeping, treaty material, and diplomatic protocol; Wampanoag origin',
            'Thanksgiving counter-narrative — National Day of Mourning observed by Wampanoag at Plymouth since 1970',
        ],
        'cultural_resources': [
            'Plymouth/Patuxet — Wampanoag homeland, site of English colonization 1620',
            'Cape Cod National Seashore — Nauset/Wampanoag ancestral territory',
            'Plimoth Patuxet Museums — includes Wampanoag homesite staffed by Wampanoag',
            'Deerfield — Pocumtuck homeland, 1704 raid site',
            'Martha\'s Vineyard — Aquinnah Wampanoag cliffs (Gay Head)',
        ],
    },

    'Michigan': {
        'federally_recognized': [
            'Bay Mills Indian Community (Ojibwe)',
            'Grand Traverse Band of Ottawa and Chippewa Indians',
            'Hannahville Indian Community (Potawatomi)',
            'Keweenaw Bay Indian Community (Ojibwe)',
            'Lac Vieux Desert Band of Lake Superior Chippewa',
            'Little River Band of Ottawa Indians',
            'Little Traverse Bay Bands of Odawa Indians',
            'Match-e-be-nash-she-wish Band of Pottawatomi (Gun Lake)',
            'Nottawaseppi Huron Band of the Potawatomi',
            'Pokagon Band of Potawatomi',
            'Saginaw Chippewa Indian Tribe',
            'Sault Ste. Marie Tribe of Chippewa Indians',
        ],
        'cultural_concepts': [
            'Three Fires Confederacy — alliance of Ojibwe, Odawa, Potawatomi',
            'Manoomin/wild rice — sacred food and cultural keystone; Ojibwe migration story ends where food grows on water',
            'Anishinaabe — collective identity: Ojibwe, Odawa, Potawatomi',
            'Birch bark — canoes, scrolls (wiigwaasabak), containers; birch bark scrolls record Midewiwin knowledge',
            'Midewiwin — Grand Medicine Society; Ojibwe spiritual/healing tradition',
        ],
        'cultural_resources': [
            'Isle Royale National Park — Ojibwe ancestral territory, ancient copper mining',
            'Sleeping Bear Dunes National Lakeshore — Ojibwe origin story, Sleeping Bear legend',
            'Pictured Rocks National Lakeshore — Ojibwe spiritual landscape',
            'Sanilac Petroglyphs — Woodland period rock art',
            'Ziibiwing Center — Saginaw Chippewa cultural museum',
            'Ancient copper mining sites (Keweenaw Peninsula) — 7,000+ year tradition, oldest metal mining in Americas',
        ],
    },

    'Minnesota': {
        'federally_recognized': [
            'Bois Forte Band of Chippewa (Ojibwe)',
            'Fond du Lac Band of Lake Superior Chippewa',
            'Grand Portage Band of Lake Superior Chippewa',
            'Leech Lake Band of Ojibwe',
            'Mille Lacs Band of Ojibwe',
            'Red Lake Nation (Ojibwe)',
            'White Earth Nation (Ojibwe)',
            'Lower Sioux Indian Community (Mdewakanton Dakota)',
            'Prairie Island Indian Community (Mdewakanton Dakota)',
            'Shakopee Mdewakanton Sioux Community',
            'Upper Sioux Community (Dakota)',
        ],
        'cultural_concepts': [
            'Mnísota Makhóčhe — Dakota name meaning "land where the waters reflect the clouds"',
            'Bdote — sacred Dakota site at confluence of Mississippi and Minnesota Rivers',
            'Manoomin/wild rice — sacred Ojibwe food, legally recognized as having rights in White Earth',
            'Dakota 38+2 — annual memorial horseback ride for 38 Dakota men hanged in Mankato 1862, largest mass execution in US history',
            'Midewiwin — Grand Medicine Society',
            'Jingle Dress Dance — originated with Ojibwe in Minnesota, healing dance',
        ],
        'cultural_resources': [
            'Grand Portage National Monument — Ojibwe homeland, fur trade era',
            'Voyageurs National Park — Ojibwe ancestral territory',
            'Pipestone National Monument — sacred pipestone/catlinite quarry, intertribal significance',
            'Bdote/Fort Snelling — Dakota sacred site, also site of Dakota internment camp 1862–63',
            'Mille Lacs Indian Museum — Ojibwe cultural institution',
            'Jeffers Petroglyphs — 7,000+ year Indigenous rock art',
        ],
    },

    'Mississippi': {
        'federally_recognized': [
            'Mississippi Band of Choctaw Indians — descendants who avoided removal',
        ],
        'displaced_peoples': [
            'Choctaw (Chahta) — central and southern Mississippi; Treaty of Dancing Rabbit Creek 1830, first major removal under Indian Removal Act',
            'Chickasaw — northern Mississippi, Tupelo area; removed 1837',
            'Natchez — southwestern Mississippi, Natchez Bluffs; destroyed by French 1730',
            'Biloxi — Gulf Coast',
            'Pascagoula — Gulf Coast, southeastern Mississippi',
            'Tunica — northwestern Mississippi (Yazoo Basin)',
            'Yazoo — Yazoo River area',
            'Chakchiuma — northeastern Mississippi',
        ],
        'cultural_resources': [
            'Nanih Waiya — Choctaw sacred mound, origin place of the Choctaw people',
            'Natchez Trace Parkway — Indigenous trade corridor spanning Mississippi to Tennessee',
            'Winterville Mounds — Mississippian ceremonial center (1000–1450 CE)',
            'Emerald Mound — second largest ceremonial mound in US (Natchez)',
            'Grand Village of the Natchez — Natchez political/ceremonial center',
            'Owl Creek Mounds — Chickasaw cultural affiliation',
            'Choctaw stickball (Ishtaboli) — ancestor of lacrosse, "the little brother of war"',
        ],
    },

    'Missouri': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Osage (Wazhazhe) — western Missouri was the heart of the Osage Nation; removed to Kansas then Indian Territory',
            'Missouria (Niúachi) — the state\'s namesake people; nearly destroyed by smallpox 1829; merged with Otoe',
            'Shawnee — southeastern Missouri',
            'Illini — northeastern Missouri',
            'Quapaw — southeastern corner (Boot Heel)',
            'Iowa (Báxoje) — northern Missouri',
            'Sauk and Meskwaki — northeastern Missouri',
            'Delaware/Lenape — briefly in Missouri during westward removal',
            'Cherokee — briefly in Missouri during removal',
        ],
        'cultural_resources': [
            'Gateway Arch/Cahokia connection — St. Louis was a Mississippian population center',
            'Osage Village State Historic Site — 18th century Osage capital',
            'Towosahgy State Historic Site — Mississippian ceremonial mound complex',
            'Mastodon State Historic Site — Clovis-era occupation, oldest in Missouri',
            'Trail of Tears State Park — Cherokee river crossing during removal',
            'Big Osage Village National Historic Landmark',
        ],
    },

    'Montana': {
        'federally_recognized': [
            'Blackfeet Nation (Amskapipiikani)',
            'Crow Tribe (Apsáalooke)',
            'Confederated Salish and Kootenai Tribes (Flathead Reservation — Séliš, Ql̓ispé, and Ktunaxa)',
            'Fort Belknap Indian Community (Aaniiih/Gros Ventre and Nakoda/Assiniboine)',
            'Fort Peck Assiniboine and Sioux Tribes (Nakoda and Dakota)',
            'Northern Cheyenne Tribe (Tsitsistas)',
            'Chippewa Cree Tribe (Rocky Boy\'s)',
            'Little Shell Tribe of Chippewa Indians — federally recognized 2019 after 130+ years',
        ],
        'cultural_concepts': [
            'Iinnii/Buffalo — Blackfeet cultural keystone, spiritual and material foundation',
            'Sun Dance (Okan) — Blackfeet, Crow, Cheyenne annual ceremony of renewal',
            'Apsáalooke (Crow) — "children of the large-beaked bird"; clan system matrilineal',
            'Counting coup — Plains warrior tradition of bravery without killing',
            'Star quilts — Northern Plains art form, gifted at ceremonies',
        ],
        'cultural_resources': [
            'Glacier National Park — Blackfeet ancestral territory, "Backbone of the World"',
            'Little Bighorn Battlefield National Monument — Lakota/Cheyenne/Arapaho victory 1876',
            'Big Hole National Battlefield — Nez Perce flight of 1877',
            'Bear Paw Battlefield — Nez Perce surrender site, Chief Joseph\'s famous speech',
            'First Peoples Buffalo Jump State Park — 2,000+ year buffalo drive',
            'Pictograph Cave State Park — 2,000+ year rock art',
            'Medicine Wheel (adjacent Wyoming) — Crow/multiple nations sacred site',
        ],
    },

    'Nebraska': {
        'federally_recognized': [
            'Omaha Tribe of Nebraska',
            'Winnebago Tribe of Nebraska (Ho-Chunk)',
            'Ponca Tribe of Nebraska',
            'Santee Sioux Nation',
        ],
        'displaced_peoples': [
            'Pawnee (Chatiks si chatiks) — central Nebraska, the state\'s most prominent historical nation; removed to Oklahoma 1870s',
            'Otoe-Missouria — southeastern Nebraska; removed to Indian Territory',
            'Arapaho — western Nebraska plains',
            'Cheyenne — western Nebraska plains',
            'Lakota/Sioux — northwestern Nebraska (Pine Ridge Reservation extends into Nebraska)',
        ],
        'cultural_resources': [
            'Agate Fossil Beds National Monument — Lakota sacred area, Cook collection of Lakota artifacts',
            'Scotts Bluff National Monument — Lakota and Cheyenne territory, Oregon Trail',
            'Chimney Rock — landmark on Oregon Trail, Lakota/Cheyenne territory',
            'Homestead National Historical Park — homesteading on ceded Otoe-Missouria/Pawnee land',
            'Ponca Trail of Tears — Standing Bear\'s 1879 case establishing Indigenous personhood under law',
        ],
    },

    'Nevada': {
        'federally_recognized': [
            'Western Shoshone — multiple bands/colonies',
            'Northern Paiute — multiple bands/colonies',
            'Southern Paiute — Moapa Band, Las Vegas Paiute',
            'Washoe Tribe of Nevada and California',
            'Te-Moak Tribe of Western Shoshone',
            'Walker River Paiute Tribe',
            'Pyramid Lake Paiute Tribe',
            'Fallon Paiute-Shoshone Tribe',
            'Shoshone-Paiute Tribes (Duck Valley)',
            'Yomba Shoshone Tribe',
            'Duckwater Shoshone Tribe',
            'Ely Shoshone Tribe',
        ],
        'cultural_concepts': [
            'Newe Sogobia — Western Shoshone name for their homeland, central Nevada/eastern California',
            'Pine nut harvest — cultural keystone, annual gathering cycle',
            'Cui-ui fish — sacred to Pyramid Lake Paiute, endemic to Pyramid Lake',
            'Tule — cattail/bulrush material culture (duck decoys, boats, shelters)',
        ],
        'cultural_resources': [
            'Great Basin National Park — Western Shoshone ancestral territory',
            'Tule Springs Fossil Beds — Southern Paiute landscape',
            'Spirit Cave (Fallon) — 9,400-year-old mummy repatriated to Fallon Paiute-Shoshone 2016',
            'Pyramid Lake — Paiute sacred lake, one of largest natural lakes in arid West',
            'Hidden Cave — 11,000+ year human use',
            'Ruby Valley Treaty (1863) — Western Shoshone treaty, land rights still contested',
        ],
    },

    'New Hampshire': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Abenaki (Alnôbak) — Western Abenaki/Pennacook; ancestral people of New Hampshire; displaced by colonial wars but maintain community presence, especially in northern regions',
            'Pennacook — Merrimack River valley; sub-group of Abenaki',
            'Wabanaki peoples — broader confederacy presence',
        ],
        'cultural_resources': [
            'Abenaki historical sites along Connecticut River',
            'Mount Washington/Agiocochook — Abenaki sacred mountain, "home of the Great Spirit"',
            'Lake Winnipesaukee — Abenaki name, "smile of the Great Spirit"',
        ],
    },

    'New Jersey': {
        'federally_recognized': [],
        'state_recognized': [
            'Ramapough Lenape Nation — Ramapo Mountains, NJ/NY border; also face environmental racism (Ford toxic waste)',
            'Powhatan Renape Nation',
            'Nanticoke Lenni-Lenape Tribal Nation',
        ],
        'displaced_peoples': [
            'Lenape (Lenni Lenape/Delaware) — the entire state of New Jersey is Lenape homeland (Lenapehoking); forced removal westward through colonial era and Walking Purchase fraud',
            'Munsee (northern Lenape dialect group)',
            'Unami (southern Lenape dialect group)',
        ],
        'cultural_resources': [
            'Lenapehoking — the entire Lenape homeland spanning NJ, eastern PA, southeastern NY, northern DE',
            'Abbott Farm National Historic Landmark — 13,000-year occupation site, Trenton',
            'Minisink — Upper Delaware Valley archaeological complex',
            'Pahaquarra — Lenape village site, Delaware Water Gap',
        ],
    },

    'New Mexico': {
        'federally_recognized': [
            'Navajo Nation (Diné) — largest reservation in US',
            'Pueblo of Acoma',
            'Pueblo of Cochiti',
            'Pueblo of Isleta',
            'Pueblo of Jemez (Walatowa)',
            'Pueblo of Laguna',
            'Pueblo of Nambe',
            'Pueblo of Ohkay Owingeh (San Juan)',
            'Pueblo of Picuris',
            'Pueblo of Pojoaque',
            'Pueblo of San Felipe',
            'Pueblo of San Ildefonso',
            'Pueblo of Sandia',
            'Pueblo of Santa Ana',
            'Pueblo of Santa Clara',
            'Pueblo of Santo Domingo (Kewa)',
            'Pueblo of Taos',
            'Pueblo of Tesuque',
            'Pueblo of Zia',
            'Pueblo of Zuni',
            'Jicarilla Apache Nation',
            'Mescalero Apache Tribe',
            'Fort Sill Apache Tribe (Chiricahua — headquartered in NM)',
        ],
        'cultural_concepts': [
            'Pueblo worldview — emergence from underworld, connection of all living things through sacred landscape',
            'Kiva — sacred ceremonial chamber, heart of Pueblo spiritual practice',
            'Corn/maize — Pueblo agricultural-spiritual foundation; multiple colored corn varieties with ceremonial significance',
            'All Pueblo Council — governing body uniting 20 pueblos, operating since at least 1598 (Pueblo Revolt organization)',
            'Pueblo Revolt of 1680 — only successful Indigenous revolution against European colonialism in North America',
            'Hózhó — Diné foundational concept (see Arizona)',
        ],
        'cultural_resources': [
            'Chaco Culture National Historical Park — Ancestral Puebloan great houses and roads, astronomical alignments; all 20 pueblos claim cultural affiliation',
            'Bandelier National Monument — Ancestral Puebloan cliff dwellings, Cochiti/San Ildefonso ancestral territory',
            'Gila Cliff Dwellings — Mogollon culture, Apache territory',
            'Aztec Ruins National Monument — Ancestral Puebloan great house, Chaco outlier',
            'Petroglyph National Monument — 24,000 petroglyphs, Pueblo sacred landscape',
            'Taos Pueblo — oldest continuously inhabited community in North America (1000+ years), UNESCO World Heritage Site',
            'Acoma Pueblo "Sky City" — oldest continuously inhabited settlement in US, atop 367-foot mesa',
            'Valles Caldera — Jemez Pueblo ancestral territory',
            'White Sands — Tularosa Basin, Apache territory; 23,000-year-old human footprints',
            'Indian Arts Research Center — School for Advanced Research, Santa Fe',
        ],
    },

    'New York': {
        'federally_recognized': [
            'Oneida Indian Nation',
            'Onondaga Nation — keeper of the Central Fire of the Haudenosaunee Confederacy',
            'Seneca Nation of Indians',
            'Tonawanda Band of Seneca',
            'Tuscarora Nation',
            'St. Regis Mohawk Tribe (Akwesasne — straddles US/Canada)',
            'Cayuga Nation',
            'Shinnecock Indian Nation — federally recognized 2010',
            'Unkechaug Nation (Poospatuck Reservation, Long Island)',
        ],
        'unrecognized_with_presence': [
            'Ramapough Lenape Nation — Ramapo Mountains, NY/NJ border',
            'Montauk — eastern Long Island; state says "extinct" but community persists',
        ],
        'cultural_concepts': [
            'Haudenosaunee Confederacy (Iroquois) — Mohawk, Oneida, Onondaga, Cayuga, Seneca, Tuscarora',
            'Kayanerenko:wa / Great Law of Peace — Haudenosaunee constitution, influenced US Constitution; oldest participatory democracy in the world',
            'Two Row Wampum (Kaswéntha) — treaty belt symbolizing parallel sovereignty, Haudenosaunee-Dutch 1613',
            'Hiawatha Belt — wampum belt representing the Haudenosaunee Confederacy',
            'Three Sisters agriculture — corn, beans, squash polyculture system',
            'Clan Mother system — matrilineal governance, women select and can remove chiefs',
            'Condolence Ceremony — diplomatic protocol for mourning and renewal',
            'Midwinter Ceremony — Haudenosaunee annual renewal',
            'Lacrosse (Dehuntshigwa\'es) — Creator\'s game, Haudenosaunee origin',
        ],
        'cultural_resources': [
            'Statue of Liberty/Ellis Island — Lenape ancestral territory (Mannahatta)',
            'Ganondagan State Historic Site — 17th century Seneca capital',
            'Fort Stanwix National Monument — Haudenosaunee treaty site, 1768 boundary line',
            'Onondaga Lake — sacred Haudenosaunee site, place of Confederacy founding; heavily polluted Superfund site',
            'National Museum of the American Indian (NYC, Smithsonian) — George Gustav Heye Center',
            'Saratoga National Historical Park — Mohawk and other Haudenosaunee territory',
        ],
    },

    'North Carolina': {
        'federally_recognized': [
            'Eastern Band of Cherokee Indians (EBCI) — descendants who avoided removal',
        ],
        'state_recognized': [
            'Lumbee Tribe — 55,000+ members, largest state-recognized tribe in US; federal recognition bill repeatedly introduced',
            'Haliwa-Saponi Tribe',
            'Sappony',
            'Occaneechi Band of the Saponi Nation',
            'Waccamaw Siouan Tribe',
            'Coharie Tribe',
            'Meherrin Indian Tribe',
        ],
        'displaced_peoples': [
            'Cherokee — western North Carolina was the heart of Cherokee country; most removed 1838, Eastern Band remained',
            'Tuscarora — eastern North Carolina; Tuscarora War 1711-15, most fled north to join Haudenosaunee Confederacy',
            'Catawba — Piedmont, Charlotte area; now in South Carolina',
        ],
        'cultural_concepts': [
            'Cherokee syllabary — writing system invented by Sequoyah (ᏍᏏᏉᏯ), one of few independently created writing systems in history',
            'Qualla Boundary — Eastern Band of Cherokee Indians trust land, not technically a reservation',
            'Gadugi — Cherokee cooperative labor tradition',
        ],
        'cultural_resources': [
            'Blue Ridge Parkway — Cherokee ancestral territory, passes through Qualla Boundary',
            'Great Smoky Mountains National Park — Cherokee ancestral homeland, Shaconage ("place of blue smoke")',
            'Carl Sandburg Home NHS — Cherokee territory context',
            'Museum of the Cherokee Indian — Cherokee cultural institution, Cherokee, NC',
            'Town Creek Indian Mound — Pee Dee culture ceremonial center (1150–1400 CE)',
            'Judaculla Rock — Cherokee petroglyph, largest in Southeast',
        ],
    },

    'North Dakota': {
        'federally_recognized': [
            'Mandan, Hidatsa, and Arikara Nation (Three Affiliated Tribes, Fort Berthold)',
            'Spirit Lake Tribe (Dakota)',
            'Standing Rock Sioux Tribe (Lakota/Dakota — straddles ND/SD border)',
            'Turtle Mountain Band of Chippewa Indians (Ojibwe/Métis)',
            'Sisseton-Wahpeton Oyate (Dakota — extends into ND)',
        ],
        'cultural_concepts': [
            'Three Affiliated Tribes — Mandan, Hidatsa, and Arikara each maintained distinct languages and ceremonies while sharing Fort Berthold',
            'Okipa ceremony — Mandan renewal ceremony, documented by Catlin and Bodmer',
            'Earth lodge villages — Mandan/Hidatsa agricultural civilization, permanent villages on Missouri',
            'Standing Rock water protectors — NoDAPL movement 2016',
        ],
        'cultural_resources': [
            'Theodore Roosevelt National Park — Mandan/Hidatsa/Arikara territory',
            'Knife River Indian Villages National Historic Site — Hidatsa earth lodge villages',
            'Fort Union Trading Post NHS — intertribal trade center',
            'Double Ditch Village — Mandan fortified earth lodge village',
            'On-A-Slant Village — Mandan earth lodge village at Fort Abraham Lincoln',
            'Huff Indian Village — Mandan fortified village (1450–1600 CE)',
            'Writing Rock — petroglyphs, multiple tribal affiliations',
        ],
    },

    'Ohio': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Shawnee (Shawandasse) — central and southern Ohio; Tecumseh\'s confederacy; removed by 1830s',
            'Wyandot (Wendat/Huron) — northern Ohio, Upper Sandusky; last tribe removed from Ohio 1843',
            'Miami (Myaamia) — western Ohio',
            'Ottawa (Odawa) — northern Ohio',
            'Ojibwe/Chippewa — northern Ohio',
            'Delaware/Lenape — eastern Ohio; Gnadenhütten Massacre 1782',
            'Mingo/Seneca — eastern Ohio; Logan\'s Lament',
            'Erie — northern Ohio, "Cat Nation"; destroyed by Iroquois 1650s',
            'Hopewell and Adena peoples — builders of Ohio\'s monumental earthworks, ancestors of multiple modern nations',
        ],
        'cultural_resources': [
            'Hopewell Culture National Historical Park — monumental geometric earthworks (200 BCE–500 CE); UNESCO World Heritage Site 2023',
            'Serpent Mound — world\'s largest effigy mound; Fort Ancient/Adena cultural affiliation',
            'Fort Ancient State Memorial — Hopewell-era hilltop enclosure',
            'Flint Ridge — 12,000+ year Indigenous quarry for Vanport chert/flint',
            'Newark Earthworks — Hopewell geometric enclosures, Great Circle and Octagon, lunar alignments; UNESCO World Heritage Site 2023',
            'Gnadenhütten — site of 1782 massacre of 96 Christian Lenape',
            'Fallen Timbers Battlefield — 1794, led to Treaty of Greenville and cession of most of Ohio',
            'Schoenbrunn Village — first Moravian-Lenape settlement',
        ],
    },

    'Oklahoma': {
        'federally_recognized': [
            # 39 federally recognized tribes in Oklahoma — more than any other state
            'Cherokee Nation', 'United Keetoowah Band of Cherokee',
            'Muscogee (Creek) Nation', 'Chickasaw Nation',
            'Choctaw Nation of Oklahoma', 'Seminole Nation of Oklahoma',
            'Osage Nation', 'Quapaw Nation',
            'Ponca Tribe of Indians of Oklahoma', 'Otoe-Missouria Tribe',
            'Pawnee Nation of Oklahoma', 'Kaw Nation',
            'Tonkawa Tribe', 'Wichita and Affiliated Tribes',
            'Caddo Nation', 'Delaware Nation', 'Delaware Tribe of Indians',
            'Wyandotte Nation',
            'Comanche Nation', 'Kiowa Tribe', 'Apache Tribe of Oklahoma (Plains Apache)',
            'Fort Sill Apache Tribe (Chiricahua)',
            'Cheyenne and Arapaho Tribes',
            'Sac and Fox Nation', 'Iowa Tribe of Oklahoma',
            'Kickapoo Tribe of Oklahoma',
            'Citizen Potawatomi Nation', 'Absentee Shawnee Tribe',
            'Eastern Shawnee Tribe of Oklahoma',
            'Shawnee Tribe', 'Miami Tribe of Oklahoma',
            'Modoc Tribe of Oklahoma', 'Peoria Tribe of Indians of Oklahoma',
            'Ottawa Tribe of Oklahoma', 'Seneca-Cayuga Nation',
            'Thlopthlocco Tribal Town', 'Kialegee Tribal Town',
            'Alabama-Quassarte Tribal Town',
            'United Keetoowah Band of Cherokee Indians',
        ],
        'cultural_concepts': [
            'Indian Territory — historical designation for lands promised "as long as the grass grows and the rivers flow"',
            'Trail of Tears — Cherokee, Choctaw, Chickasaw, Creek, Seminole forced removal 1830s–40s',
            'Stomp Dance — Muscogee/Cherokee/Seminole ceremonial tradition, fire-centered',
            'Green Corn Ceremony (Busk) — Muscogee/Seminole annual renewal',
            'Native American Church / Peyote Way — originated in Oklahoma, pan-Indian spiritual movement',
            'Gourd Dance — Kiowa origin, intertribal warrior society tradition',
            'McGirt v. Oklahoma (2020) — Supreme Court affirmed Muscogee reservation was never disestablished',
            'Allotment era — Dawes Act 1887 devastated Oklahoma tribal land holdings',
            'Ribbon work — Osage and other Oklahoma tribal textile art',
        ],
        'cultural_resources': [
            'Washita Battlefield National Historic Site — Cheyenne village attacked by Custer 1868',
            'Chickasaw National Recreation Area — Chickasaw cultural landscape',
            'Spiro Mounds — Caddo/Mississippian ceremonial center, one of most important archaeological sites in North America',
            'First Americans Museum (Oklahoma City)',
            'Gilcrease Museum (Tulsa) — extensive Indigenous art and artifact collection',
            'Philbrook Museum — on former Osage allotment land',
            'Cherokee National Capitol (Tahlequah)',
            'Sequoyah\'s Cabin — site where Cherokee syllabary was developed',
            'Fort Sill — Geronimo\'s imprisonment and death site; Chiricahua Apache prisoners of war',
        ],
    },

    'Oregon': {
        'federally_recognized': [
            'Burns Paiute Tribe',
            'Confederated Tribes of Coos, Lower Umpqua and Siuslaw',
            'Confederated Tribes of Grand Ronde — restored 1983 after termination',
            'Confederated Tribes of Siletz Indians — restored 1977 after termination, encompasses 27 original tribes/bands',
            'Confederated Tribes of the Umatilla Indian Reservation (Cayuse, Umatilla, Walla Walla)',
            'Confederated Tribes of Warm Springs (Warm Springs, Wasco, Paiute)',
            'Coquille Indian Tribe — restored 1989 after termination',
            'Cow Creek Band of Umpqua Tribe of Indians — restored 1982 after termination',
            'Klamath Tribes — restored 1986 after devastating termination in 1954',
        ],
        'cultural_concepts': [
            'Termination era — Oregon was ground zero; Klamath termination 1954 was most devastating single act, lost 860,000 acres',
            'First foods ceremonies — salmon, roots, berries ceremonial harvest sequence',
            'Celilo Falls — inundated by The Dalles Dam 1957, one of oldest continuously inhabited sites in North America, major fishery for 15,000+ years',
        ],
        'cultural_resources': [
            'Crater Lake National Park — Klamath Tribes sacred site, Giiwas ("sacred place")',
            'John Day Fossil Beds — Warm Springs/Paiute territory',
            'Oregon Caves National Monument — Takelma ancestral territory',
            'Lewis and Clark NHP — Chinook, Clatsop territory',
            'Tamástslikt Cultural Institute — Cayuse, Umatilla, Walla Walla',
            'Museum at Warm Springs',
        ],
    },

    'Pennsylvania': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Lenape (Delaware/Lenni Lenape) — the entire eastern half of Pennsylvania is Lenape homeland; Walking Purchase fraud 1737; removed westward',
            'Susquehannock (Conestoga) — Susquehanna River valley; destroyed by colonial warfare, Paxton Boys massacre 1763 killed last community',
            'Shawnee — western Pennsylvania; joined Tecumseh\'s confederacy',
            'Seneca/Mingo — northwestern Pennsylvania',
            'Erie — northwestern corner; destroyed by Iroquois 1650s',
            'Monongahela people — western Pennsylvania, pre-contact',
        ],
        'cultural_resources': [
            'Valley Forge — Lenape territory context',
            'Independence Hall / Philadelphia — Lenape homeland (Coaquannock/Shackamaxon)',
            'Fort Necessity — Seneca/Mingo territory, French and Indian War',
            'Delaware Water Gap NRA — Lenape (Minsi) ancestral landscape',
            'Meadowcroft Rockshelter — 19,000+ year human occupation, one of oldest in Americas',
            'Indian God Rock — petroglyphs, Allegheny River',
            'Kinzua Dam — flooded Seneca Nation Allegany Reservation, breaking 1794 Canandaigua Treaty',
        ],
    },

    'Rhode Island': {
        'federally_recognized': [
            'Narragansett Indian Tribe',
        ],
        'displaced_peoples': [
            'Narragansett — survived King Philip\'s War, Great Swamp Massacre 1675',
            'Wampanoag — eastern Rhode Island',
            'Niantic — southern coast',
        ],
        'cultural_resources': [
            'Great Swamp Fight site — Narragansett, December 1675',
            'Roger Williams National Memorial — colonial-era Indigenous context',
        ],
    },

    'South Carolina': {
        'federally_recognized': [
            'Catawba Indian Nation — "People of the River"',
        ],
        'state_recognized': [
            'Pee Dee Indian Nation',
            'Chicora Indian Tribe',
            'Edisto Natchez-Kusso Tribe',
            'Santee Indian Nation',
            'Beaver Creek Indians',
            'Wassamasaw Tribe of Varnertown Indians',
        ],
        'displaced_peoples': [
            'Cherokee — upstate South Carolina, Blue Ridge; removed 1838',
            'Yamasee — coastal South Carolina; Yamasee War 1715-17 shattered the nation; survivors scattered',
            'Cusabo — Charleston area coastal peoples',
            'Sewee — coastal, north of Charleston',
            'Waccamaw — Grand Strand/Waccamaw River area',
            'Congaree — central South Carolina, Columbia area; the national park is named for them',
        ],
        'cultural_resources': [
            'Congaree National Park — Congaree people\'s ancestral floodplain, old-growth bottomland forest',
            'Charles Pinckney NHS — enslaved and Indigenous labor context',
            'Fort Sumter — on traditional Cusabo/Etiwan territory',
            'Sewee Shell Ring — 4,000-year-old ceremonial site',
            'Santee Indian Mound — Santee cultural site',
        ],
    },

    'South Dakota': {
        'federally_recognized': [
            'Oglala Sioux Tribe (Oglala Lakota, Pine Ridge)',
            'Rosebud Sioux Tribe (Sicangu Lakota)',
            'Cheyenne River Sioux Tribe (multiple Lakota bands)',
            'Standing Rock Sioux Tribe (Lakota/Dakota — straddles SD/ND)',
            'Lower Brule Sioux Tribe (Kul Wicasa Lakota)',
            'Crow Creek Sioux Tribe (Dakota)',
            'Yankton Sioux Tribe (Ihanktonwan Dakota)',
            'Sisseton-Wahpeton Oyate (Dakota)',
            'Flandreau Santee Sioux Tribe',
        ],
        'cultural_concepts': [
            'Mitákuye Oyás\'iŋ — "all my relatives/we are all related," Lakota foundational concept of interconnection',
            'Ȟe Sápa / Paha Sápa (Black Hills) — sacred center of the Lakota universe, illegally seized despite 1868 Fort Laramie Treaty; Supreme Court ruled taking was illegal (1980) but Lakota have refused monetary settlement demanding land return',
            'Sun Dance (Wi Wanyang Wacipi) — central Lakota/Dakota spiritual ceremony; banned by US government 1883–1934',
            'Vision Quest (Haŋblečeya) — "crying for a dream," individual spiritual practice at sacred sites',
            'Sweat Lodge (Inipi) — purification ceremony',
            'Sacred Pipe (Čhaŋnúŋpa) — brought by White Buffalo Calf Woman',
            'Seven Sacred Rites of the Lakota',
            'Tiospaye — Lakota extended family/community structure',
            'Wičháša Wakȟáŋ — holy man/medicine person',
            'Wopila — ceremony of thanksgiving and giveaway',
        ],
        'cultural_resources': [
            'Badlands National Park — Oglala Lakota territory, South Unit co-managed with tribe',
            'Wind Cave National Park — Lakota emergence site, "where the buffalo came from"',
            'Jewel Cave — Lakota sacred underground landscape',
            'Mount Rushmore / Six Grandfathers — carved into Lakota sacred mountain Tȟuŋkášila Šákpe without consent',
            'Crazy Horse Memorial — privately funded, controversial among some Lakota',
            'Bear Butte / Mathó Pahá — sacred site for Lakota, Cheyenne, and multiple Plains nations',
            'Wounded Knee — site of 1890 massacre of 250+ Lakota by 7th Cavalry; 1973 AIM occupation',
            'Akta Lakota Museum — Chamberlain',
            'Pine Ridge Reservation — poorest census tract in US, Oglala Lakota homeland',
        ],
    },

    'Tennessee': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Cherokee — eastern Tennessee was core Cherokee territory, including Overhill Towns on Little Tennessee River; capital Chota was "city of refuge"',
            'Chickasaw — western Tennessee, Memphis area',
            'Muscogee (Creek) — southeastern corner',
            'Shawnee — Cumberland Plateau region',
            'Yuchi — eastern Tennessee',
        ],
        'cultural_resources': [
            'Great Smoky Mountains National Park — Cherokee homeland (see North Carolina)',
            'Shiloh National Military Park — Mississippian mound complex predating Civil War by centuries',
            'Stones River National Battlefield — on former Cherokee/Shawnee territory',
            'Old Stone Fort State Archaeological Park — 2,000-year-old ceremonial enclosure',
            'Pinson Mounds State Archaeological Park — Middle Woodland ceremonial center, Saul\'s Mound is second tallest in US',
            'Chucalissa Museum — Mississippian village, Memphis',
            'Sequoyah Birthplace Museum — Vonore, Cherokee cultural institution',
            'Red Clay State Historic Park — last Cherokee council ground before removal 1832–38',
        ],
    },

    'Texas': {
        'federally_recognized': [
            'Alabama-Coushatta Tribe of Texas',
            'Kickapoo Traditional Tribe of Texas',
            'Ysleta del Sur Pueblo (Tigua)',
        ],
        'displaced_peoples': [
            'Comanche (Numunuu) — the dominant nation of the Southern Plains; Comancheria covered most of western Texas; removed to Indian Territory',
            'Kiowa — Texas Panhandle and western Texas; removed to Indian Territory',
            'Lipan Apache (Ndé) — central and southern Texas; scattered by colonial and Comanche warfare',
            'Tonkawa — central Texas; repeatedly displaced, now in Oklahoma',
            'Wichita — north-central Texas; removed to Indian Territory',
            'Caddo — eastern Texas, East Texas Piney Woods; Caddo Mounds; removed to Indian Territory',
            'Coahuiltecan peoples — southern Texas/northern Mexico; absorbed into mission system',
            'Karankawa — Texas Gulf Coast; destroyed by colonization by 1860s',
            'Jumano — Trans-Pecos region; largely absorbed by 1700s',
            'Mescalero Apache — Trans-Pecos/Big Bend region',
            'Cherokee — briefly in East Texas 1820s–1839; expelled by Republic of Texas',
        ],
        'cultural_resources': [
            'Big Bend National Park — Chisos (Apache/Comanche), Jumano territory',
            'Guadalupe Mountains National Park — Mescalero Apache homeland',
            'Alibates Flint Quarries National Monument — 13,000+ year quarry, Comanche/Kiowa territory',
            'Palo Duro Canyon — Comanche/Kiowa homeland; 1874 battle ended Red River War',
            'Caddo Mounds State Historic Site — Caddo ceremonial center (800–1300 CE)',
            'Seminole Canyon State Park — 4,000-year-old rock art, Lower Pecos Canyonlands style',
            'Hueco Tanks — 10,000+ year human use, Kiowa migration story origin site',
            'San Antonio Missions NHP/World Heritage Site — Coahuiltecan peoples forced into missions',
            'Mission Ysleta — oldest mission in Texas, Tigua/Ysleta del Sur Pueblo',
        ],
    },

    'Utah': {
        'federally_recognized': [
            'Ute Indian Tribe (Uintah and Ouray)',
            'Paiute Indian Tribe of Utah (5 bands)',
            'Northwestern Band of the Shoshone Nation',
            'Skull Valley Band of Goshute Indians',
            'Confederated Tribes of the Goshute Reservation',
            'Navajo Nation (Utah portion)',
            'White Mesa Ute (Southern Ute portion)',
        ],
        'cultural_concepts': [
            'Nuche/Núuchiu — Ute self-designation, "The People"',
            'Bear Dance — Ute spring ceremony',
            'Sun Dance — Ute and Shoshone',
        ],
        'cultural_resources': [
            'Bears Ears National Monument / Shash Jáa — sacred to Hopi, Navajo, Ute Mountain Ute, Ute Indian Tribe, Zuni Pueblo; Bears Ears Inter-Tribal Coalition',
            'Canyonlands National Park — Ancestral Puebloan, Ute, Paiute',
            'Arches National Park — Ute territory',
            'Capitol Reef National Park — Fremont culture, Ute, Paiute',
            'Natural Bridges National Monument — Ancestral Puebloan',
            'Hovenweep National Monument — Ancestral Puebloan',
            'Grand Staircase-Escalante — Ancestral Puebloan, Paiute, Ute',
            'Newspaper Rock — 2,000+ year Indigenous rock art panel',
            'Nine Mile Canyon — "world\'s longest art gallery," Fremont/Ute rock art',
            'Golden Spike NHS — Shoshone territory, transcontinental railroad',
        ],
    },

    'Vermont': {
        'federally_recognized': [],
        'state_recognized': [
            'Nulhegan Band of the Coosuk Abenaki Nation',
            'Elnu Abenaki Tribe',
            'Koasek Traditional Band of the Koas Abenaki Nation',
            'Missisquoi Abenaki Tribe / Abenaki Nation at Missisquoi',
        ],
        'cultural_concepts': [
            'N\'dakinna — Abenaki name for their homeland, "our land"',
            'Eugenics — Vermont conducted forced sterilization targeting Abenaki people 1931–1963',
        ],
        'cultural_resources': [
            'Missisquoi River/Lake Champlain — Abenaki homeland',
            'Green Mountains — Abenaki hunting and gathering territory',
        ],
    },

    'Virginia': {
        'federally_recognized': [
            'Pamunkey Indian Tribe — federally recognized 2015; oldest reservation in US (1646 treaty)',
            'Chickahominy Indian Tribe — federally recognized 2018',
            'Chickahominy Indians Eastern Division — federally recognized 2018',
            'Upper Mattaponi Indian Tribe — federally recognized 2018',
            'Rappahannock Tribe — federally recognized 2018',
            'Monacan Indian Nation — federally recognized 2018',
            'Nansemond Indian Tribe — federally recognized 2018',
        ],
        'state_recognized': [
            'Mattaponi Indian Tribe — state reservation since colonial era; shad treaty with Governor',
            'Patawomeck Indian Tribe of Virginia',
            'Nottoway Indian Tribe of Virginia',
            'Cheroenhaka (Nottoway) Indian Tribe',
        ],
        'displaced_peoples': [
            'Powhatan Confederacy (Tsenacommacah) — 30+ Algonquian-speaking nations united under Wahunsenacah (Chief Powhatan); ancestral Tidewater Virginia',
            'Manahoac — Piedmont Virginia',
            'Saponi — central/southern Virginia',
            'Tutelo — western Virginia, Shenandoah',
            'Cherokee — southwestern Virginia',
            'Shawnee — southwestern Virginia (Appalachian region)',
        ],
        'cultural_concepts': [
            'Tsenacommacah — Powhatan name for their territory, "densely inhabited land"',
            'Walter Plecker / Racial Integrity Act of 1924 — Virginia\'s "paper genocide": state registrar reclassified all Indigenous people as "colored," destroying tribal records and identity documentation',
            'Annual Mattaponi/Pamunkey shad tribute to Virginia Governor — oldest continuing treaty relationship in US',
        ],
        'cultural_resources': [
            'Jamestown/Historic Jamestowne — Paspahegh/Powhatan homeland, site of first permanent English colony',
            'Shenandoah National Park — Monacan/Tutelo/Manahoac ancestral territory; families forcibly removed for park creation 1930s',
            'Colonial National Historical Park — Powhatan territory',
            'Pamunkey Indian Museum — oldest Indian reservation in US',
            'Werowocomoco — Powhatan paramount chief\'s capital, recently acquired by NPS',
            'Natural Bridge — Monacan sacred site',
            'Ely Mound — one of largest Mississippian mounds in Virginia',
        ],
    },

    'Washington': {
        'federally_recognized': [
            'Confederated Tribes and Bands of the Yakama Nation',
            'Tulalip Tribes', 'Muckleshoot Indian Tribe',
            'Puyallup Tribe', 'Squaxin Island Tribe',
            'Nisqually Indian Tribe', 'Swinomish Indian Tribal Community',
            'Lummi Nation', 'Nooksack Indian Tribe',
            'Suquamish Tribe', 'Skokomish Indian Tribe',
            'Snoqualmie Indian Tribe', 'Stillaguamish Tribe',
            'Quinault Indian Nation', 'Makah Tribe (Kwih-dich-chuh-ahtx)',
            'Hoh Tribe', 'Quileute Tribe',
            'Shoalwater Bay Indian Tribe', 'Chehalis Confederated Tribes',
            'Cowlitz Indian Tribe', 'Spokane Tribe',
            'Colville Confederated Tribes (12 bands)',
            'Kalispel Tribe', 'Coeur d\'Alene (extends into WA)',
            'Snohomish',
            'Sauk-Suiattle Indian Tribe',
            'Upper Skagit Indian Tribe',
            'Samish Indian Nation',
        ],
        'unrecognized_with_presence': [
            'Duwamish Tribal Organization — ancestral people of Seattle (named for Chief Si\'ahl); federal recognition denied despite continuous presence',
            'Chinook Indian Nation — ancestral people of the lower Columbia River; federal recognition denied despite treaty rights',
            'Steilacoom Tribe — ancestral Puget Sound; state recognized only',
            'Snohomish Tribe — distinct from Tulalip',
        ],
        'cultural_concepts': [
            'Salmon as first food — ceremonial first salmon catch and blessing; salmon as keystone of Pacific Northwest cultures',
            'Potlatch — ceremonial redistribution feast, banned by federal government 1884–1951',
            'Cedar — "tree of life," material for longhouses, canoes, clothing, baskets, medicine',
            'Boldt Decision (1974) — affirmed treaty fishing rights, tribes entitled to 50% of harvestable salmon',
            'Billy Frank Jr. — Nisqually, fish-in activist, treaty rights champion',
            'Coast Salish art — formline design tradition',
            'Totem poles — monumental carved cedar art form (Tlingit, Haida, Tsimshian, Coast Salish)',
            'Canoe culture — ocean-going canoes, Tribal Canoe Journeys annual event',
        ],
        'cultural_resources': [
            'Olympic National Park — Quinault, Makah, Hoh, Quileute ancestral territory',
            'Mount Rainier / Tahoma / Tacoma — sacred mountain to multiple Puget Sound nations',
            'North Cascades National Park — Upper Skagit territory',
            'San Juan Island NHP — Coast Salish ancestral territory',
            'Fort Vancouver NHS — Chinook/Cowlitz territory',
            'Whitman Mission NHS — Cayuse territory, Cayuse War context',
            'Makah Cultural and Research Center — Cape Flattery, Ozette Village',
            'Ozette archaeological site — Makah village buried by mudslide 500 years ago, "Pompeii of the Northwest"',
            'Duwamish Longhouse and Cultural Center — Seattle',
        ],
    },

    'West Virginia': {
        'federally_recognized': [],
        'displaced_peoples': [
            'Shawnee — primary nation of the Kanawha Valley and Ohio River region',
            'Cherokee — southern West Virginia',
            'Mingo/Seneca — northern panhandle, Ohio Valley',
            'Tutelo — eastern panhandle',
            'Monongahela people — pre-contact culture of the Monongahela Valley',
        ],
        'cultural_resources': [
            'New River Gorge National Park — Shawnee/Cherokee territory, one of oldest rivers in Americas',
            'Grave Creek Mound — largest Adena burial mound in Americas (250 BCE)',
            'Blennerhassett Island — Indigenous occupation, Ohio River',
            'South Charleston Mound — Adena culture',
        ],
    },

    'Wisconsin': {
        'federally_recognized': [
            'Bad River Band of the Lake Superior Chippewa Indians (Ojibwe)',
            'Ho-Chunk Nation',
            'Lac Courte Oreilles Band of Lake Superior Chippewa Indians',
            'Lac du Flambeau Band of Lake Superior Chippewa Indians',
            'Menominee Indian Tribe of Wisconsin — restored 1973 after termination in 1961',
            'Oneida Nation',
            'Forest County Potawatomi Community',
            'Red Cliff Band of Lake Superior Chippewa',
            'Sokaogon Chippewa Community (Mole Lake)',
            'St. Croix Chippewa Indians of Wisconsin',
            'Stockbridge-Munsee Community (Mohican)',
        ],
        'unrecognized_with_presence': [
            'Brothertown Indian Nation — only tribe created by act of Congress (1839); lost recognition through citizenship; seeking re-recognition',
        ],
        'cultural_concepts': [
            'Menominee Forest — 230,000 acres of sustained-yield forestry, more timber now than when reservation was established 1854; model of Indigenous land management',
            'Manoomin/wild rice — sacred Ojibwe food, Lac du Flambeau and other bands',
            'Spearfishing rights — Ojibwe treaty rights upheld through Voigt Decision 1983; walleye spearfishing',
            'Effigy Mound tradition — Wisconsin has largest concentration of effigy mounds in the world',
        ],
        'cultural_resources': [
            'Apostle Islands National Lakeshore — Ojibwe ancestral territory, La Pointe/Madeline Island was center of Ojibwe world',
            'Aztalan State Park — northernmost Mississippian settlement (1000–1300 CE)',
            'Menominee Logging Camp Museum',
            'Effigy Mounds — Man Mound near Baraboo, Lizard Mound County Park, others throughout southern Wisconsin',
            'High Cliff State Park — effigy mounds, Winnebago/Ho-Chunk',
            'Lac du Flambeau Museum — Ojibwe cultural institution',
        ],
    },

    'Wyoming': {
        'federally_recognized': [
            'Eastern Shoshone Tribe (Wind River Reservation)',
            'Northern Arapaho Tribe (Wind River Reservation — shared, though historically these were rival nations)',
        ],
        'displaced_peoples': [
            'Crow (Apsáalooke) — north-central Wyoming, Bighorn Basin',
            'Lakota/Sioux — northeastern Wyoming, Black Hills connection',
            'Cheyenne — eastern Wyoming plains',
            'Bannock — western Wyoming',
            'Blackfeet — northwestern corner',
            'Kiowa — southeastern Wyoming',
            'Comanche — southeastern Wyoming',
        ],
        'cultural_concepts': [
            'Sacagawea — Lemhi Shoshone woman, essential to Lewis and Clark expedition; buried at Wind River',
            'Washita — Arapaho name for the river',
        ],
        'cultural_resources': [
            'Yellowstone National Park — Shoshone, Crow, Blackfeet, Bannock, Nez Perce ancestral territory; first national park displaced Indigenous inhabitants',
            'Grand Teton National Park — Shoshone, "Teewinot" in Shoshone',
            'Devils Tower / Bear Lodge / Mathó Thípila — sacred to Lakota, Cheyenne, Crow, Kiowa, Shoshone, Arapaho; first national monument (1906)',
            'Bighorn Medicine Wheel — 800+ year old stone medicine wheel; sacred to Crow, Cheyenne, Lakota, Arapaho, Shoshone, and others',
            'Heart Mountain — Japanese American internment camp, on Crow ceded territory',
            'Fort Laramie NHS — 1851 and 1868 treaty sites',
            'Legend Rock Petroglyph Site — 11,000+ year rock art',
        ],
    },

    # ── US TERRITORIES ─────────────────────────────────────────────────────

    'Puerto Rico': {
        'indigenous_peoples': [
            'Taíno — Indigenous Arawakan people of Borikén (Puerto Rico); despite colonial narrative of extinction, genetic and cultural continuity is well-documented',
        ],
        'cultural_concepts': [
            'Borikén/Boriquén — Taíno name for Puerto Rico, "land of the brave lord"',
            'Boricua — Puerto Rican identity rooted in Taíno heritage',
            'Cacique — Taíno chief/leader',
            'Batey — ceremonial ball court/plaza, center of community life',
            'Cemí/Zemí — spiritual objects embodying ancestral and nature spirits',
            'Areíto — ceremonial songs, dances, and oral histories',
            'Yuca/cassava — staple crop, Taíno agricultural foundation',
            'Conuco — Taíno agricultural mound system',
            'Hamaca/hammock — Taíno invention',
            'Huracán — Taíno storm deity, origin of "hurricane"',
            'Barbacoa — Taíno smoking/grilling method, origin of "barbecue"',
        ],
        'cultural_resources': [
            'Caguana Ceremonial Ball Courts Site (Centro Ceremonial Indígena de Caguana) — largest and best-preserved Taíno batey complex',
            'Tibes Indigenous Ceremonial Center (Ponce) — oldest known ceremonial site in Caribbean (25 CE–1000 CE)',
            'Cueva del Indio — Taíno petroglyphs, Arecibo',
            'Paso del Indio — largest archaeological site in the Caribbean',
            'Taíno rock art throughout the island — petroglyphs and pictographs in caves and rivers',
        ],
    },

    'US Virgin Islands': {
        'indigenous_peoples': [
            'Taíno — inhabited St. Croix (Ay-Ay) at European contact',
            'Kalinago (Island Carib) — inhabited and contested the islands with Taíno',
        ],
        'cultural_resources': [
            'Salt River Bay National Historical Park (St. Croix) — site of Columbus\'s 1493 encounter with Kalinago warriors; ceremonial and habitation site spanning 2,000+ years',
            'Reef Bay Trail petroglyphs (St. John) — Taíno ceremonial rock art in Virgin Islands National Park',
            'Cinnamon Bay archaeological site (St. John) — Taíno village site',
            'Trunk Bay — Taíno cultural landscape',
        ],
    },

    'Guam': {
        'indigenous_peoples': [
            'CHamoru (self-determined spelling; colonial: "Chamorro") — Indigenous Austronesian people of Guåhan (Guam), continuous presence 4,000+ years',
        ],
        'cultural_concepts': [
            'Inafa\'maolek — interdependence, mutual respect; foundational CHamoru social value',
            'Latte stones — stone pillars supporting ancient CHamoru buildings; cultural icon of Guam',
            'Suruhånu/Suruhåna — traditional CHamoru healer (male/female)',
            'Fino\' CHamoru — CHamoru language, endangered',
            'Guåhan — CHamoru name for Guam',
        ],
        'cultural_resources': [
            'War in the Pacific National Historical Park — CHamoru territory, WWII and occupation history',
            'Latte Stone Park — ancient CHamoru architectural remains',
            'Latte of Freedom — cultural monument',
            'Sagan Kotturan CHamoru (CHamoru Cultural Village)',
            'Ritidian/Litekyan — ancient CHamoru village site, now partly wildlife refuge',
        ],
    },

    'American Samoa': {
        'indigenous_peoples': [
            'Samoan (Tagata Sāmoa) — Indigenous Polynesian people; American Samoa is the only US territory south of the equator',
        ],
        'cultural_concepts': [
            'Fa\'a Sāmoa — "the Samoan Way," traditional social structure and governance system',
            'Matai — chiefly system; customary land held communally, 90% of land is communally owned',
            'Fono — village council governance',
            'Siapo/tapa cloth — bark cloth art tradition',
            'Pe\'a (male) and Malu (female) — traditional tattooing, among most significant in Polynesia',
            'ʻAva/kava ceremony — ceremonial beverage, diplomatic and spiritual protocol',
            '\'Ie Tōga — fine mats, highest-value cultural treasure in Samoan society',
        ],
        'cultural_resources': [
            'National Park of American Samoa — rain forest, coral reef, and Samoan village; leased from villages via customary agreement',
            'Jean P. Haydon Museum — Samoan cultural institution, Pago Pago',
            'Fale (traditional houses) — open-sided structures reflecting communal values',
            'Star mounds (tia seu lupe) — ancient pigeon-catching mounds, ceremonial',
        ],
    },

    'Northern Mariana Islands (CNMI)': {
        'indigenous_peoples': [
            'CHamoru (self-determined spelling; colonial: "Chamorro") — Indigenous people of the Mariana Islands, 4,000+ years',
            'Carolinian (Refaluwasch) — Micronesian people who settled in CNMI from Caroline Islands beginning 1700s-1800s',
        ],
        'cultural_concepts': [
            'Latte stones — ancient CHamoru architectural columns (see Guam)',
            'Carolinian voyaging/navigation — traditional Pacific wayfinding without instruments',
            'Inafa\'maolek — see Guam (shared CHamoru value)',
        ],
        'cultural_resources': [
            'American Memorial Park (Saipan) — WWII history on CHamoru/Carolinian homeland',
            'House of Taga (Tinian) — largest latte stones in Mariana Islands',
            'Banzai Cliff/Suicide Cliff — WWII sites on Indigenous homeland',
            'Managaha Island — ancient CHamoru cultural site',
            'Grotto (Saipan) — culturally significant cave',
        ],
    },

    # ── COMPACT OF FREE ASSOCIATION (COFA) NATIONS ─────────────────────────
    # These independent nations have Compacts of Free Association with the US.
    # COFA citizens can live/work in the US. US federal agencies have obligations.

    'Republic of the Marshall Islands': {
        'indigenous_peoples': [
            'Marshallese (ri-Majōl) — Indigenous Micronesian people of the Marshall Islands',
        ],
        'cultural_concepts': [
            'Stick charts (rebbelib, meddo, mattang) — Indigenous navigation charts using shells and sticks to map ocean swells; unique in world maritime history',
            'Bwij/Jowi — matrilineal clan system, land inheritance through mother',
            'Iroij — chiefly system',
            'Nuclear legacy — Bikini and Enewetak atolls; 67 nuclear tests 1946–1958 (Castle Bravo was 15 megatons); ongoing displacement and health effects; Runit Dome leaking nuclear waste',
        ],
        'cultural_resources': [
            'Bikini Atoll Nuclear Test Site — UNESCO World Heritage Site; Bikinians remain displaced',
            'Alele Museum — Marshallese cultural institution, Majuro',
            'Traditional outrigger canoes (wa) — sophisticated ocean-going vessels',
        ],
    },

    'Republic of Palau (Belau)': {
        'indigenous_peoples': [
            'Palauan (tir a Belau) — Indigenous Micronesian/Melanesian people',
        ],
        'cultural_concepts': [
            'Bai — men\'s meeting house with elaborate painted storyboards, center of community governance',
            'Storyboards — carved and painted narrative panels depicting legends and history',
            'Mesei (taro patches) — women\'s agricultural domain, matrilineal inheritance',
            'Omengat — Palauan first-birth ceremony',
            'Udoud — Palauan money beads, traditional currency with clan histories',
        ],
        'cultural_resources': [
            'Rock Islands Southern Lagoon — UNESCO World Heritage Site, ancient villages, burial caves',
            'Belau National Museum — oldest museum in Micronesia',
            'Bai ra Irrai — reconstructed traditional men\'s meeting house',
            'Stone monoliths of Babeldaob — ancient basalt monoliths, unknown origin',
        ],
    },

    'Federated States of Micronesia': {
        'indigenous_peoples': [
            'Chuukese (Trukese) — people of Chuuk State; largest ethnic group in FSM',
            'Pohnpeian — people of Pohnpei State',
            'Kosraean — people of Kosrae State',
            'Yapese — people of Yap State',
        ],
        'cultural_concepts': [
            'Rai/stone money (Yapese) — massive circular stone discs quarried from Palau, value based on history not size; still used ceremonially',
            'Sou — Pohnpeian feast and tribute system to Nahnmwarki (paramount chief)',
            'Sakau/kava — Pohnpeian ceremonial beverage',
            'Mwarmwar — Kosraean ceremonial flower/leaf head wreath',
            'Traditional navigation (Yapese/Carolinian) — non-instrument open-ocean wayfinding spanning thousands of miles',
        ],
        'cultural_resources': [
            'Nan Madol (Pohnpei) — "Venice of the Pacific," ancient city of artificial islets built on coral reef (1200–1500 CE); UNESCO World Heritage Site; Saudeleur dynasty',
            'Lelu Ruins (Kosrae) — ancient basalt city, rival to Nan Madol',
            'Yapese stone money banks — circular stone discs displayed in village stone money banks',
            'Chuuk Lagoon — WWII Japanese fleet graveyard, on Indigenous homeland',
            'Menka Ruins (Chuuk) — ancient fortified hilltop settlement',
        ],
    },

    # ── DISTRICT OF COLUMBIA ───────────────────────────────────────────────

    'District of Columbia': {
        'indigenous_peoples': [
            'Nacotchtank (Anacostan/Nacostine) — the original people of the land where DC sits; Anacostia River and neighborhood named for them',
            'Piscataway — the broader nation of the Potomac River region; DC is within Piscataway ancestral territory',
        ],
        'cultural_concepts': [
            'Potomac — from Patawomeck, Algonquian word meaning "something brought" or "trading place"',
            'Anacostia — from Nacotchtank; the river, neighborhood, and community bear the original people\'s name',
        ],
        'cultural_resources': [
            'National Museum of the American Indian (Smithsonian) — on Nacotchtank/Piscataway ancestral land',
            'Anacostia River — Nacotchtank homeland and waterway',
            'Theodore Roosevelt Island — Nacotchtank village site Assateague/Analostan',
            'Rock Creek Park — Indigenous habitation sites, soapstone quarries used for 4,000+ years',
            'Kenilworth Aquatic Gardens — Indigenous wetland landscape',
        ],
    },
}

# Flattened index: geographic keyword → list of Indigenous peoples to check for
# Used to validate that entries mentioning these places name the relevant nations
GEOGRAPHIC_INDIGENOUS_INDEX = {}
for _jurisdiction, _data in INDIGENOUS_PEOPLES_BY_JURISDICTION.items():
    _peoples = []
    for _key in ('federally_recognized', 'state_recognized', 'displaced_peoples',
                 'indigenous_peoples', 'unrecognized_with_presence'):
        if _key in _data:
            _peoples.extend(_data[_key])
    if _peoples:
        GEOGRAPHIC_INDIGENOUS_INDEX[_jurisdiction] = _peoples

# Keywords that signal an entry involves Indigenous cultural resources
INDIGENOUS_SIGNAL_KEYWORDS = [
    'NAGPRA', 'repatriation', 'tribal', 'tribe', 'tribal consultation',
    'sacred site', 'national monument', 'national park', 'BLM', 'Bureau of Land Management',
    'Bureau of Indian Affairs', 'BIA', 'Indian', 'Indigenous', 'Native American',
    'federal land', 'public land', 'DOI', 'Department of Interior', 'Interior Department',
    'NPS', 'National Park Service', 'Forest Service', 'USFS',
    'Section 106', 'historic preservation', 'NHPA', 'AIRFA',
    'ICWA', 'Indian Child Welfare', 'reservation', 'trust land',
    'treaty', 'sovereignty', 'self-determination', 'allotment',
    'sacred', 'ceremonial', 'ancestral', 'aboriginal',
    'cultural affiliation', 'traditional cultural property',
    'archaeological', 'petroglyph', 'pictograph', 'mound', 'earthwork',
    'boarding school', 'termination', 'relocation',
    'Bears Ears', 'Grand Staircase', 'Chaco', 'Mesa Verde', 'Oak Flat',
    'Standing Rock', 'Pine Ridge', 'Wind River', 'Denali',
    'Yellowstone', 'Yosemite', 'Grand Canyon', 'Olympic',
    'Everglades', 'Great Smoky', 'Shenandoah', 'Glacier',
]

# Critical cultural concepts that should appear in Indigenous impact text
# when the entry's subject matter is relevant
INDIGENOUS_CULTURAL_CONCEPTS = {
    'legal_frameworks': [
        'NAGPRA (Native American Graves Protection and Repatriation Act)',
        'NHPA Section 106 (National Historic Preservation Act)',
        'AIRFA (American Indian Religious Freedom Act)',
        'ICWA (Indian Child Welfare Act)',
        'Indian Reorganization Act of 1934',
        'Termination era (House Concurrent Resolution 108)',
        'Public Law 280',
        'Plenary power doctrine',
        'Trust responsibility',
        'Government-to-government relationship',
        'Treaty rights',
        'Tribal sovereignty',
        'Self-determination (Indian Self-Determination Act 1975)',
        'Boldt Decision (1974, treaty fishing rights)',
        'McGirt v. Oklahoma (2020, reservation boundaries)',
        'Standing Bear v. Crook (1879, Indigenous personhood)',
    ],
    'foundational_concepts': [
        'Hózhó (Diné/Navajo — harmony, beauty, balance)',
        'Mitákuye Oyás\'iŋ (Lakota — "all my relatives," interconnection)',
        'Kayanerenko:wa / Great Law of Peace (Haudenosaunee — oldest participatory democracy)',
        'Seven Generations (decision-making considers seven generations forward)',
        'Aloha ʻāina (Kānaka Maoli — love of the land)',
        'Fa\'a Sāmoa (Samoan Way — traditional governance and social structure)',
        'Inafa\'maolek (CHamoru — interdependence)',
        'Turtle Island (Indigenous name for North America)',
        'Blood quantum (federal identity metric, colonial origin)',
        'Land Back (contemporary movement for land return)',
    ],
    'ceremonies': [
        'Sun Dance (Lakota, Cheyenne, Arapaho, Blackfeet, Crow, others)',
        'Green Corn Ceremony / Busk (Muscogee, Seminole, Cherokee)',
        'Potlatch / Ku.éex\' (Northwest Coast — Tlingit, Haida, Kwakwaka\'wakw)',
        'Blessingway / Hózhóójí (Navajo)',
        'Stomp Dance (Muscogee, Cherokee, Seminole)',
        'Ghost Dance (1890, Wovoka/Paiute origin, pan-Indian)',
        'Midewiwin / Grand Medicine Society (Ojibwe, Potawatomi)',
        'Kinaalda (Navajo coming-of-age)',
        'Sunrise Ceremony / Na\'ii\'ees (Apache coming-of-age)',
        'Gourd Dance (Kiowa origin, intertribal)',
        'Pipe Ceremony (Plains nations)',
        'Sweat Lodge / Inipi (Lakota and widespread)',
        'Vision Quest / Haŋblečeya (Lakota — "crying for a dream")',
        'First Salmon Ceremony (Pacific Northwest treaty tribes)',
        'World Renewal ceremonies (Yurok, Karuk, Hupa — Jump Dance, Brush Dance, Deerskin Dance)',
        'Niman ceremony (Hopi — Kachina farewell)',
    ],
    'food_and_agriculture': [
        'Three Sisters (corn, beans, squash polyculture — Haudenosaunee and widespread)',
        'Manoomin / wild rice (Ojibwe sacred food — "the food that grows on water")',
        'Acorn processing (California — Ohlone, Miwok, Pomo, Yurok, etc.)',
        'Camas root (Nez Perce, Shoshone-Bannock — prairie lily)',
        'Pemmican (Plains nations — preserved meat/fat/berry food)',
        'Blue corn (Pueblo — ceremonial and nutritional)',
        'Cultural burning / prescribed fire (California, Southeast, Plains)',
        'Salmon (Pacific Northwest — "first food," ceremonial, economic, spiritual)',
        'Bison / buffalo (Plains nations — Iinnii in Blackfeet, Tatanka in Lakota)',
        'Maple sugaring (Great Lakes Anishinaabe — Ziinzibaakwad)',
        'Wojapi (Lakota berry pudding)',
    ],
    'cultural_items': [
        'Wampum (Haudenosaunee/Algonquian — shell beads as treaty record, diplomacy, history)',
        'Katsina/Kachina (Hopi, Zuni — spiritual beings and carved figures)',
        'Totem poles (Tlingit, Haida, Tsimshian, Coast Salish — monumental carved cedar)',
        'Jingle dress (Ojibwe origin — healing dance regalia)',
        'Star quilts (Lakota/Northern Plains — gifted at ceremonies)',
        'Ribbon shirts/ribbon skirts (widespread — ceremonial and identity garments)',
        'Quillwork (Plains/Woodlands — porcupine quill embroidery)',
        'Beadwork (widespread — post-contact art form evolved from quillwork)',
        'Birch bark canoes (Ojibwe, Wabanaki, other Woodlands)',
        'Cradleboards (widespread — baby carriers with tribal-specific designs)',
        'Dreamcatchers (Ojibwe origin — Asabikeshiinh)',
        'Effigy mounds (Woodland period — Wisconsin, Iowa, Minnesota; animal-shaped earth sculptures)',
        'Regalia (ceremony-specific dress, not "costumes")',
        'Parfleche (Plains — rawhide container with geometric designs)',
        'Tule (California/Great Basin — cattail/bulrush material culture)',
        'Siapo/tapa cloth (Samoan bark cloth)',
        '\'Ie Tōga (Samoan fine mats — highest-value cultural treasure)',
        'Latte stones (CHamoru — ancient architectural pillars)',
    ],
}


# ---------------------------------------------------------------------------
# AFRICAN DESCENDANT PEOPLES REFERENCE DATABASE
# Comprehensive mapping of African-descendant communities to every US state,
# territory, collectivity, and COFA nation where federal agencies govern the
# cultural resources of communities.
#
# Each jurisdiction lists:
#   - Specific African-descendant communities/populations by name
#   - Key cities/areas with significant African-descendant populations
#   - Historic African-descendant neighborhoods and communities (including
#     those destroyed, displaced, or gentrified)
#   - Cultural resources: museums, historic sites, landmarks, archives
#   - Cultural practices, ceremonies, traditions at risk or at issue
#   - Afro-Indigenous communities (cross-referenced with Indigenous database)
#   - African diaspora communities: Haitian, West African, East African,
#     Afro-Caribbean, Afro-Latino, Cape Verdean, etc.
#
# Population notes use US Census / ACS 2020-2024 estimates.
# "Percentage" = % of state/territory population that is Black/African American.
# ---------------------------------------------------------------------------

AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION = {
    # ── 50 STATES ──────────────────────────────────────────────────────────

    'Alabama': {
        'population': '26.8% Black (1.3M) — 7th highest percentage nationally',
        'communities': [
            'Black Belt communities — named for dark prairie soil but defined by its large African-descendant population; arc of counties from Sumter to Bullock',
            'Africatown/Plateau (Mobile) — founded by survivors of the Clotilda, last known slave ship to arrive in US (1860); Cudjoe Lewis (Oluale Kossola) and 109 others from Dahomey/Benin',
            'Gee\'s Bend/Boykin (Wilcox County) — isolated Black community, world-renowned quilters; descendants of enslaved people from Pettway plantation',
            'Tuskegee community — historic Black university town, Macon County',
            'Birmingham Black community — 4th Avenue Business District, Ensley, Smithfield, Collegeville, Titusville',
            'Selma Black community — Brown Chapel AME Church, historic voting rights movement center',
            'Huntsville Black community — historically tied to Redstone Arsenal labor',
            'Montgomery Black community — Dexter Avenue, Centennial Hill',
        ],
        'afro_indigenous': [
            'Freedmen of the Muscogee (Creek) Nation — descendants of people enslaved by Creek who were removed on Trail of Tears; fought for citizenship rights',
            'MOWA Choctaw — some members have both African and Choctaw ancestry; historically classified under Virginia-style racial integrity laws',
            'Cajun/Creole communities of south Alabama — some have mixed African, Indigenous, and European heritage',
        ],
        'cultural_resources': [
            'Africatown Heritage House and Welcome Center (Mobile) — Clotilda survivor community, National Register site',
            'Clotilda shipwreck site (Mobile River) — discovered 2019, last known slave ship',
            'National Memorial for Peace and Justice (Montgomery) — lynching memorial, Equal Justice Initiative',
            'Legacy Museum: From Enslavement to Mass Incarceration (Montgomery)',
            'Edmund Pettus Bridge (Selma) — Bloody Sunday 1965, National Historic Landmark',
            'Brown Chapel AME Church (Selma) — staging ground for Selma-to-Montgomery marches',
            'Dexter Avenue King Memorial Baptist Church (Montgomery) — MLK\'s church during bus boycott',
            'Rosa Parks Museum (Montgomery)',
            '16th Street Baptist Church (Birmingham) — 1963 bombing site, four girls killed',
            'Birmingham Civil Rights National Monument — includes 16th Street Baptist, Kelly Ingram Park, Gaston Motel',
            'Tuskegee Institute National Historic Site — Booker T. Washington, George Washington Carver',
            'Tuskegee Airmen National Historic Site — first Black military aviators',
            'Gee\'s Bend Quilters Collective — internationally exhibited textile art tradition',
            'Old Cahawba Archaeological Park — enslaved persons\' quarters and community sites',
            'Freedom Riders National Monument (Anniston) — bus burning site 1961',
        ],
        'cultural_practices': [
            'Gee\'s Bend quilting — improvisational textile art tradition descended from West African textile arts; passed through generations of women in the Pettway, Bendolph, and Young families; exhibited at Whitney Museum, MFA Houston',
            'Africatown Yoruba/Fon cultural retention — community maintained West African naming conventions, agricultural knowledge, and social structures into 20th century; Cudjoe Lewis documented Yoruba language and customs',
            'Jubilee singing tradition — Tuskegee, Fisk connection; arranged spirituals as concert music',
            'Sacred Harp/shape-note singing — Black practitioners in Alabama\'s Black Belt, parallel tradition to white Sacred Harp',
            'Mardi Gras in Mobile — African-descendant krewes with distinct traditions predating New Orleans Mardi Gras',
        ],
    },

    'Alaska': {
        'population': '3.7% Black (27K) — small but significant military and urban population',
        'communities': [
            'Fairbanks Black community — military-connected, Fort Wainwright/Eielson AFB',
            'Anchorage Black community — largest in state, centered around Mountain View and Muldoon neighborhoods',
            'Joint Base Elmendorf-Richardson community',
        ],
        'afro_indigenous': [
            'Black-Indigenous Alaskans — historical intermarriage between African American military personnel and Alaska Native communities, particularly in Fairbanks and Anchorage; children navigating both cultural identities',
        ],
        'cultural_resources': [
            'Alaska Black Caucus archives',
            'Military heritage sites documenting Black service in Alaska — Alaska Highway construction (segregated Black engineering regiments), Cold War era',
        ],
        'cultural_practices': [
            'African-descendant cultural retention in extreme-climate diaspora — community-building practices adapted to isolation and climate of Alaska',
        ],
    },

    'Arizona': {
        'population': '5.2% Black (380K)',
        'communities': [
            'Phoenix South Mountain/Laveen — historic Black community',
            'Tucson African American community — Dunbar/Spring neighborhood (historically segregated)',
            'Maryvale, Phoenix — growing African immigrant community',
            'Mesa/Chandler — East African refugee community (Somali, Ethiopian, Eritrean)',
        ],
        'afro_indigenous': [
            'Buffalo Soldiers — Black cavalry stationed at Arizona forts (Fort Huachuca); fought in Apache Wars; complex legacy of serving colonial expansion while being oppressed',
            'Black Seminoles (Seminole Negro Indian Scouts) — historically passed through Arizona territory',
            'Afro-Diné (Navajo) — individuals with both African and Navajo ancestry',
        ],
        'cultural_resources': [
            'Fort Huachuca — Buffalo Soldiers history, only active fort from Indian Wars era',
            'George Washington Carver Museum and Cultural Center (Phoenix)',
            'Dunbar School (Tucson) — segregated-era school, now community center',
            'Phoenix African American community oral history projects',
        ],
        'cultural_practices': [
            'Buffalo Soldier heritage commemorations — annual events at Fort Huachuca',
            'East African immigrant cultural maintenance — Ethiopian/Eritrean coffee ceremonies, Somali community gatherings, Islamic religious practices adapted to desert Southwest',
        ],
    },

    'Arkansas': {
        'population': '15.7% Black (475K)',
        'communities': [
            'Little Rock Black community — 12th Street corridor, Dunbar/West Central, Granite Mountain',
            'Pine Bluff Black community — majority-Black city, UAPB (University of Arkansas at Pine Bluff, HBCU)',
            'Helena-West Helena/Phillips County — Mississippi Delta region, historically majority-Black',
            'Elaine community (Phillips County) — site of 1919 Elaine Massacre, one of deadliest racial violence events in US history; 200+ Black sharecroppers killed',
        ],
        'cultural_resources': [
            'Central High School National Historic Site (Little Rock) — Little Rock Nine, 1957 desegregation crisis',
            'Mosaic Templars Cultural Center (Little Rock) — Black history museum in former fraternal lodge',
            'Elaine Massacre Memorial (Phillips County) — erected 2019, 100 years after massacre of Black sharecroppers',
            'UAPB campus — HBCU heritage',
            'Daisy Bates House (Little Rock) — NAACP leader who mentored Little Rock Nine',
        ],
        'cultural_practices': [
            'Mississippi Delta Blues tradition — Helena\'s King Biscuit Blues Festival, the oldest Blues festival in the South',
            'Black agrarian traditions — sharecropping communities that maintained collective farming knowledge from enslavement through cooperative movements',
        ],
    },

    'California': {
        'population': '6.5% Black (2.6M) — largest Black population on West Coast',
        'communities': [
            'Los Angeles: South Central/South LA — Watts, Compton, Inglewood, Crenshaw, Leimert Park, Baldwin Hills, View Park-Windsor Hills; center of West Coast Black culture; Great Migration Second Wave destination (1940s–60s, migrants from Louisiana, Texas, Arkansas, Oklahoma via Southern Pacific Railroad and Route 66; defense industry jobs at Kaiser Shipyards, Douglas Aircraft, Lockheed)',
            'Oakland/East Bay — West Oakland, East Oakland, Fruitvale; Great Migration destination; Black Panther Party founded 1966',
            'San Francisco — Western Addition/Fillmore District ("Harlem of the West"), Bayview-Hunters Point; decimated by urban renewal',
            'Sacramento — Oak Park, Del Paso Heights; California\'s oldest Black community',
            'San Diego — Southeast San Diego, Encanto, Lincoln Park; historically military-connected',
            'Compton — historically Black city, now majority Latino; cultural legacy remains',
            'Richmond — shipyard workers during WWII, Great Migration community',
            'Stockton/San Joaquin Valley — agricultural workers, Great Migration legacy',
            'Little Ethiopia (Los Angeles) — Fairfax District, largest Ethiopian community outside DC area',
            'Little Mogadishu (San Diego) — City Heights, Somali refugee community',
        ],
        'afro_indigenous': [
            'Afro-Indigenous Californians — individuals with both African American and California Native ancestry, particularly from Chumash, Tongva, and Ohlone communities; historically rendered invisible by blood quantum and one-drop rules',
            'Black Seminole descendants in California — Great Migration brought Black Seminole families from Oklahoma and Texas',
        ],
        'cultural_resources': [
            'California African American Museum (CAAM, Los Angeles) — state-funded institution in Exposition Park',
            'Museum of the African Diaspora (MoAD, San Francisco)',
            'Leimert Park Village (LA) — Black cultural district: Vision Theatre, World Stage, Eso Won Books',
            'Fillmore Heritage Center (San Francisco) — commemorating "Harlem of the West"',
            'Black Panther Party headquarters sites (Oakland) — 1966–1982, multiple locations',
            'West Oakland 16th Street Station — Great Migration arrival point',
            'Port Chicago Naval Magazine National Memorial — 1944 explosion killed 320, mostly Black munitions loaders; mutiny trial',
            'Allensworth State Historic Park — only California town founded, financed, and governed by African Americans (1908)',
            'Biddy Mason Memorial Park (LA) — enslaved woman who won freedom in California and became philanthropist',
            'Golden State Mutual Life Building (LA) — murals by Hale Woodruff and Charles Alston',
            'Watts Towers — Simon Rodia, in heart of Black community; Watts Towers Arts Center',
            'Dunbar Hotel (LA) — historic Black hotel on Central Avenue Jazz Corridor',
        ],
        'cultural_practices': [
            'Central Avenue Jazz — Los Angeles\' historic Black entertainment corridor; Club Alabam, Dunbar Hotel, Last Word; Black jazz, blues, R&B from 1920s–60s',
            'West Coast hip-hop — emerged from South LA/Compton/Long Beach in 1980s; N.W.A., Tupac, Snoop Dogg, Kendrick Lamar; continuation of African-descendant oral/musical tradition',
            'Fillmore Jazz tradition (San Francisco) — Jimbo\'s Bop City, Jack\'s Tavern; lost to urban renewal/redevelopment',
            'Oakland Black cultural production — Black Arts Movement West Coast center; Black Panther Party\'s survival programs (free breakfast, clinics)',
            'Leimert Park drum circle — weekly community gathering, African-descended rhythmic tradition',
            'Kwanzaa — created by Maulana Karenga at Cal State Long Beach (1966); pan-African holiday now observed nationally',
            'Ethiopian/Eritrean immigrant cultural life — coffee ceremony (jebena buna), Ge\'ez script literacy, Orthodox Christian traditions, Timkat celebrations',
        ],
    },

    'Colorado': {
        'population': '4.6% Black (268K)',
        'communities': [
            'Denver Five Points — "Harlem of the West" (also used for SF Fillmore); historic Black cultural district; Welton Street corridor',
            'Denver Park Hill — historically Black, gentrifying rapidly',
            'Aurora — significant East African immigrant community (Ethiopian, Eritrean, Somali)',
            'Colorado Springs — military-connected Black community (Fort Carson, Peterson SFB)',
            'Dearfield (Weld County) — Black agrarian colony founded by O.T. Jackson 1910; ghost town, NPS study for national monument',
        ],
        'cultural_resources': [
            'Black American West Museum (Denver) — Justina Ford House, first Black female doctor in Colorado',
            'Blair-Caldwell African American Research Library (Denver)',
            'Dearfield historic site — Black homesteading colony, potential NPS designation',
            'Five Points Jazz Festival — honoring historic jazz corridor',
            'Rossonian Hotel (Denver) — historic Black hotel and jazz club, hosted Duke Ellington, Count Basie',
        ],
        'cultural_practices': [
            'Five Points jazz and blues tradition — Denver\'s Black entertainment district rivaled Harlem in the 1930s–50s',
            'Black agrarian colonization — Dearfield represents the broader movement of Black homesteading in the West',
            'Juneteenth celebration — Denver has held Juneteenth celebrations since 1953',
        ],
    },

    'Connecticut': {
        'population': '12.2% Black (440K)',
        'communities': [
            'Hartford — North End, Blue Hills, Upper Albany; insurance industry discrimination legacy',
            'New Haven — Dixwell/Newhallville, the Hill, Dwight; Yale University context',
            'Bridgeport — East Side, East End; largest city in CT',
            'Waterbury Black community',
            'West Indian/Caribbean communities — Hartford, Bridgeport, New Haven (Jamaican, Trinidadian, Haitian)',
        ],
        'afro_indigenous': [
            'Black Pequots — historical intermarriage between African Americans and Pequot people; some Mashantucket Pequot members have African ancestry, sparking identity and sovereignty debates',
            'Free Black-Indigenous communities of colonial Connecticut — mixed communities predating the Revolution',
        ],
        'cultural_resources': [
            'Amistad Center for Art & Culture (Hartford) — named for the 1839 slave revolt',
            'Prudence Crandall Museum (Canterbury) — teacher who admitted Black girls to school 1833',
            'Connecticut Freedom Trail — 130+ sites documenting Black history',
            'Hempsted Houses (New London) — enslaved persons\' quarters, 1678',
        ],
        'cultural_practices': [
            'West Indian carnival traditions — Hartford West Indian Parade',
            'Amistad legacy — the 1839 revolt by Mende captives from Sierra Leone is foundational to Connecticut\'s Black history; annual commemorations',
        ],
    },

    'Delaware': {
        'population': '23.2% Black (230K) — 8th highest percentage nationally',
        'communities': [
            'Wilmington — Eastside, Westside, Hilltop, Southbridge; largest city, majority-Black neighborhoods',
            'Dover Black community — Delaware State University (HBCU)',
            'Georgetown/Sussex County — rural Black communities, poultry industry labor',
        ],
        'cultural_resources': [
            'Delaware State University (Dover) — HBCU founded 1891',
            'John Dickinson Plantation — enslaved persons\' quarters preserved',
            'Old Swedes Church burial ground — includes enslaved persons',
            'Star Hill AME Church — Underground Railroad site',
        ],
        'cultural_practices': [
            'Underground Railroad heritage — Delaware was a border state with active freedom routes to Pennsylvania',
            'Return Day tradition — biracial political tradition in Georgetown',
        ],
    },

    'District of Columbia': {
        'population': '43.4% Black (296K) — historically "Chocolate City"; peaked at 71% in 1970; declining due to gentrification',
        'communities': [
            'Anacostia/Southeast DC — historic Black community since post-Civil War; Frederick Douglass settled here',
            'Shaw/U Street — "Black Broadway" from 1920s–60s; Howard Theatre, Lincoln Theatre, Pearl Bailey, Duke Ellington',
            'Georgetown Black community — pre-Civil War free Black community, largely displaced by university and gentrification',
            'Barry Farm/Hillsdale — freedpeople\'s community established 1867; demolished for redevelopment 2016–present',
            'Deanwood — self-sufficient Black community since 1870s, the "Brookland of the East"',
            'Brightwood/Brightwood Park — historic Black middle-class',
            'Petworth/Park View — Ethiopian/Eritrean diaspora center, Little Ethiopia',
            'Columbia Heights — historically Black, rapidly gentrifying',
            'LeDroit Park — historically Black neighborhood adjacent to Howard University',
            'H Street NE — historic Black commercial corridor, Trinidad neighborhood',
            'Black immigrant communities — Ethiopian (largest diaspora outside Africa), Eritrean, Haitian, Nigerian, Ghanaian, Cameroonian, Sierra Leonean concentrated in Maryland suburbs and DC neighborhoods',
        ],
        'afro_indigenous': [
            'Free Black-Piscataway intermarriage — documented historical connections between free Black communities and Piscataway people along the Potomac',
        ],
        'cultural_resources': [
            'National Museum of African American History and Culture (NMAAHC, Smithsonian) — opened 2016, 40,000+ artifacts',
            'Frederick Douglass National Historic Site (Cedar Hill, Anacostia)',
            'Howard University — preeminent HBCU, founded 1867; Moorland-Spingarn Research Center (largest Black research library)',
            'African American Civil War Memorial and Museum (U Street)',
            'Mary McLeod Bethune Council House NHS — National Council of Negro Women headquarters',
            'Carter G. Woodson Home NHS — founder of Black History Month',
            'Lincoln Memorial — Marian Anderson concert (1939), March on Washington (1963)',
            'Martin Luther King Jr. Memorial — National Mall',
            'Ben\'s Chili Bowl (U Street) — Black cultural landmark since 1958',
            'Howard Theatre — oldest theater in US continuously devoted to Black culture',
            'Duke Ellington School of the Arts — named for DC-born jazz legend',
            'Anacostia Community Museum (Smithsonian) — community-centered Black heritage museum',
            'Emancipation Memorial (Lincoln Park) — erected with funds from formerly enslaved people',
            'Black Lives Matter Plaza — 16th Street NW, painted June 2020',
        ],
        'cultural_practices': [
            'Go-go music — DC\'s indigenous music genre, created by Chuck Brown in the 1970s; combines funk, R&B, and hip-hop with call-and-response and percussion-heavy groove; #DontMuteDC movement',
            'U Street jazz and Black Broadway tradition — 1920s–60s, Pearl Bailey, Duke Ellington, Cab Calloway performed',
            'Ethiopian coffee ceremony (jebena buna) — DC metro area is the center of Ethiopian cultural life in America; ceremony as community-building practice',
            'Homecoming/Howard traditions — Howard University homecoming as pan-African cultural event',
            'DC Emancipation Day (April 16) — commemorates 1862 compensated emancipation in DC, 8 months before Emancipation Proclamation',
            'Second Line parades — DC\'s version influenced by New Orleans tradition; local brass band processions',
        ],
    },

    'Florida': {
        'population': '16.9% Black (3.7M) — 3rd largest Black population in US by number',
        'communities': [
            'Miami: Liberty City, Overtown, Little Haiti, Opa-Locka, Carol City, Richmond Heights; largest Haitian community in US',
            'Jacksonville — LaVilla ("Harlem of the South"), Eastside, New Town; largest Black population in Florida',
            'Tampa — Ybor City (Afro-Cuban community), East Tampa, College Hill, West Tampa',
            'Orlando — Parramore, Washington Shores, Eatonville (oldest Black-incorporated municipality in US, 1887; Zora Neale Hurston\'s hometown)',
            'Tallahassee — FAMU (Florida A&M University, HBCU) community, Frenchtown',
            'Fort Lauderdale/Broward — Sistrunk neighborhood; large Caribbean immigrant community',
            'Little Haiti (Miami) — Haitian Cultural Arts Alliance, Creole-language institutions, botanicas; under intense gentrification pressure',
            'Rosewood (Levy County) — destroyed in 1923 racial massacre; entire Black community burned; reparations paid by Florida 1994',
            'West Palm Beach/Riviera Beach — historic Black community',
            'Afro-Cuban community (Tampa/Ybor City) — cigar workers, mutual aid societies since 1880s',
            'Bahamian community (Key West, Miami) — "Conchs," longest-standing Caribbean diaspora in Florida',
        ],
        'afro_indigenous': [
            'Black Seminoles (Seminole Maroons) — African-descended people who escaped enslavement and allied with Seminole; fought alongside Seminole in all three Seminole Wars; "the largest slave rebellion in US history"; John Horse/Juan Caballo was key leader',
            'Afro-Seminole Creole language — unique English-based creole still spoken by some descendants',
            'Gullah/Geechee communities of northeast Florida — Amelia Island, Fort George Island; extension of Sea Islands culture',
        ],
        'cultural_resources': [
            'Eatonville Historic District — first Black incorporated town in US (1887); Zora Neale Hurston\'s birthplace',
            'Zora Neale Hurston National Museum of Fine Arts (Eatonville)',
            'Fort Mose Historic State Park (St. Augustine) — first legally sanctioned free Black settlement in North America (1738), sanctuary for escaped enslaved persons from Carolina colonies',
            'American Beach (Amelia Island) — Black beach community founded 1935 during Jim Crow; A.L. Lewis, Florida\'s first Black millionaire',
            'FAMU campus (Tallahassee) — Florida A&M University, HBCU heritage',
            'Bethune-Cookman University (Daytona Beach) — Mary McLeod Bethune\'s HBCU',
            'Kingsley Plantation (Fort George Island, NPS) — enslaved persons\' quarters, interracial family of Zephaniah Kingsley and Anna Madgigine Jai (Wolof woman from Senegal)',
            'Rosewood historical site (Levy County) — 1923 massacre site',
            'Black Archives History and Research Foundation of South Florida (Miami)',
            'Lyric Theater (Overtown, Miami) — historic "Little Broadway" venue',
            'Tampa\'s Afro-Cuban heritage sites — La Unión Martí-Maceo, the Afro-Cuban mutual aid society (founded 1904)',
        ],
        'cultural_practices': [
            'Haitian Vodou (Voudou/Voodoo) — spiritual tradition of profound historical significance; practitioners in Little Haiti maintain ceremonies, peristyles, and botanical knowledge; Vodou was the spiritual foundation of the Haitian Revolution (1791–1804), the only successful slave revolt in history',
            'Haitian Rara — street music processions, particularly during Lent/Easter; bamboo trumpets, drums, call-and-response; practiced in Little Haiti',
            'Haitian Compas/Konpa music — popular dance music tradition maintained in diaspora',
            'Junkanoo (Key West/Bahamian) — Afro-Bahamian masquerade tradition with roots in West African masquerade; performed at Christmas/New Year',
            'Gullah/Geechee cultural practices in northeast Florida — sweetgrass basketry, ring shout, Gullah language',
            'Zora! Festival (Eatonville) — annual celebration of Hurston\'s legacy and African-descendant folk culture',
            'FAMU Marching 100 — "The Incomparable" marching band tradition, continuation of HBCU musical excellence',
            'Afro-Cuban cultural practices in Tampa — rumba, santería, mutual aid society traditions (La Unión Martí-Maceo)',
            'Black Seminole traditions — knowledge of Everglades navigation, herbal medicine, Afro-Seminole Creole language',
        ],
    },

    'Georgia': {
        'population': '33.0% Black (3.5M) — 2nd largest Black population by number, 5th by percentage',
        'communities': [
            'Atlanta: Auburn Avenue ("Sweet Auburn"), West End, Cascade Heights, Collier Heights, Bankhead, East Atlanta, South Atlanta, Old Fourth Ward (MLK birthplace); historically "Black Mecca" of the South',
            'Savannah — Yamacraw, Cuyler-Brownsville, Eastside; oldest planned city in US with deep Black history',
            'Augusta — Laney-Walker/Bethlehem, Harrisburg; James Brown\'s hometown',
            'Macon — Pleasant Hill, East Macon; Otis Redding, Little Richard connections',
            'Albany — Albany Movement 1961–62, Dr. King\'s "most stunning defeat"',
            'Sapelo Island — Hog Hammock community, one of last intact Gullah/Geechee communities on Georgia coast; Cornelia Walker Bailey was last community historian',
            'St. Simons Island/Sea Islands — Gullah/Geechee cultural territory along Georgia coast',
            'Darien — historic free Black community, oldest Black church in Georgia',
            'Columbus Black community — Fort Benning connection',
            'African immigrant communities — Clarkston ("the Ellis Island of the South," refugee resettlement), Decatur (Ethiopian/Eritrean), Norcross (West African)',
        ],
        'afro_indigenous': [
            'Freedmen of the Cherokee Nation — descendants of people enslaved by Cherokee in Georgia before removal; many remained in Georgia',
            'Freedmen of the Creek Nation — descendants of people enslaved by Muscogee Creek',
            'Gullah/Geechee-Indigenous connections — documented intermarriage between Sea Islands communities and coastal Indigenous peoples',
        ],
        'cultural_resources': [
            'Martin Luther King Jr. National Historical Park (Atlanta) — birth home, Ebenezer Baptist Church, crypt',
            'Sweet Auburn Historic District (Atlanta) — "richest Negro street in the world" (Forbes 1956); SCLC headquarters',
            'Ebenezer Baptist Church (Atlanta) — MLK Sr. and Jr. pastored; National Historic Landmark',
            'Atlanta University Center — Morehouse College, Spelman College, Clark Atlanta University, Morris Brown College; largest consortium of HBCUs in the world',
            'National Center for Civil and Human Rights (Atlanta)',
            'APEX Museum (Atlanta) — African American Panoramic Experience',
            'First African Baptist Church (Savannah) — one of oldest Black churches in North America (1773); breathing holes in floor where enslaved people hid in escape tunnel',
            'Sapelo Island Hog Hammock (Gullah/Geechee) — NPS study, National Register district',
            'Pin Point Heritage Museum (Savannah) — Gullah/Geechee oyster community, Justice Clarence Thomas\'s hometown',
            'Tubman Museum (Macon) — largest museum in Southeast dedicated to African American history',
            'Augusta Canal/Enterprise Mill — enslaved labor built canal system',
            'Butler Island Plantation (Darien) — Fanny Kemble\'s abolitionist account; enslaved persons\' community archaeology',
            'Albany Civil Rights Institute',
            'Ocmulgee Mounds — enslaved persons built additional earthworks during plantation era; landscape of layered histories',
        ],
        'cultural_practices': [
            'Gullah/Geechee culture — Sea Islands of Georgia coast; language, ring shout, sweetgrass basketry, net-making, indigo dyeing, rice cultivation knowledge from Sierra Leone/Senegambia; threatened by resort development and sea-level rise',
            'Ring shout — West African–derived circular religious dance, preserved most fully in McIntosh County, Georgia; McIntosh County Shouters are the oldest known practitioners',
            'Atlanta hip-hop — trap music originated in Atlanta (Zone 6, Bankhead); continuation of African-descendant musical innovation; global cultural export',
            'Atlanta Black arts scene — Auburn Avenue, Sweet Auburn; historically centered Black literary, visual, and performing arts',
            'Savannah Second African Baptist Church traditions — one of the oldest Black congregations in North America',
            'Geechee fishing traditions — cast-net fishing, crabbing, oyster harvesting using techniques with West African origins',
        ],
    },

    'Hawaii': {
        'population': '2.2% Black (31K) — primarily military-connected',
        'communities': [
            'Honolulu military communities — Joint Base Pearl Harbor-Hickam, Schofield Barracks',
            'Historic Black community on Oahu — small but present since whaling era',
        ],
        'afro_indigenous': [
            'Afro-Polynesian Hawaiians — individuals with both African American and Kānaka Maoli ancestry; military intermarriage since WWII',
            'Black-Pacific Islander communities — growing population navigating multiple cultural identities',
        ],
        'cultural_resources': [
            'Doris Miller Memorial (Pearl Harbor) — Black Navy messman who became first African American awarded Navy Cross at Pearl Harbor',
        ],
        'cultural_practices': [
            'Military-community Black cultural retention — church communities, fraternal organizations maintaining cultural connections across Pacific',
        ],
    },

    'Illinois': {
        'population': '14.6% Black (1.8M) — 5th largest Black population by number',
        'communities': [
            'Chicago South Side — Bronzeville ("Black Metropolis"), Chatham, South Shore, Englewood, Woodlawn, Hyde Park, Pullman, Roseland, Auburn Gresham, Washington Park; center of Great Migration urban Black life',
            'Chicago West Side — Austin, Garfield Park, Lawndale, Humboldt Park; Martin Luther King Jr.\'s campaign for open housing (1966)',
            'Bronzeville/Douglas — "Black Metropolis" 1920s–60s; 47th Street and South Parkway; Gwendolyn Brooks, Richard Wright, Louis Armstrong, Muddy Waters',
            'East St. Louis — historically majority-Black industrial city; 1917 race massacre killed 39+',
            'Springfield Black community — historic Lincoln connection, 1908 Springfield Race Riot led to founding of NAACP',
            'Decatur, Peoria, Rockford — smaller Black communities',
            'Harvey, Maywood, Robbins (South suburbs) — Black suburban communities',
            'Nigerian community (Chicago) — concentrated in South suburbs and Rogers Park; one of largest in US',
            'Ghanaian community (Chicago)',
        ],
        'cultural_resources': [
            'DuSable Museum of African American History (Chicago) — first independent museum of Black history in US, founded 1961 by Dr. Margaret Burroughs',
            'Bronzeville Historic District — Supreme Life Building, Chicago Bee Building, Overton Hygienic Building',
            'Pullman National Historical Park — includes A. Philip Randolph\'s Brotherhood of Sleeping Car Porters history',
            'Chicago Defender building site — most influential Black newspaper, Robert S. Abbott',
            'Ida B. Wells-Barnett House (Bronzeville) — National Historic Landmark',
            'Muddy Waters House (Chicago) — National Register, Chicago Blues heritage',
            'Chess Records building (Willie Dixon\'s Blues Heaven Foundation) — Chicago Blues recorded here',
            'Johnson Publishing Company building — Ebony and Jet magazines, John H. Johnson',
            'South Side Community Art Center — WPA-era, oldest Black art center in US',
            'Harold Washington Library Center — first Black mayor of Chicago',
            'Emmett Till house (Argo/Summit) — where Till lived before his murder in Mississippi (1955)',
        ],
        'cultural_practices': [
            'Chicago Blues — electric amplification of Mississippi Delta Blues; Muddy Waters, Howlin\' Wolf, Buddy Guy, Willie Dixon; Chess Records; direct cultural link to West African griot tradition through Mississippi',
            'Chicago gospel — Thomas Dorsey\'s fusion of blues and hymns at Pilgrim Baptist Church; Mahalia Jackson; continuing tradition',
            'South Side jazz tradition — Louis Armstrong\'s second career in Chicago; Earl Hines, Sun Ra\'s Arkestra',
            'Chicago house music — originated in Black LGBTQ clubs of South Side in 1980s; Frankie Knuckles at the Warehouse; global dance music genre',
            'Bud Billiken Parade (Chicago) — oldest and largest African American parade in US (since 1929)',
            'Chicago step/steppin\' — social dance tradition with roots in Black South Side clubs',
            'Spoken word/poetry slam — Chicago is birthplace of poetry slam (Marc Smith, Green Mill); Black poets central',
        ],
    },

    'Indiana': {
        'population': '10.0% Black (680K)',
        'communities': [
            'Indianapolis — Indiana Avenue (historic Black business/entertainment district), Martindale-Brightwood, Haughville, Mapleton-Fall Creek; Great Migration destination (migrants from Kentucky, Tennessee, Alabama, Mississippi)',
            'Gary — historically Black industrial city, steel industry; Michael Jackson\'s hometown; once majority-Black, declining population',
            'Fort Wayne Black community — Hanna-Creighton',
            'Evansville Black community — Baptisttown/Lincoln Gardens',
        ],
        'cultural_resources': [
            'Indiana Avenue Cultural District (Indianapolis) — "Naptown\'s" jazz and blues corridor; Madame Walker Legacy Center',
            'Madam C.J. Walker Manufacturing Company (Indianapolis) — first female self-made millionaire in US; National Historic Landmark',
            'Crispus Attucks High School (Indianapolis) — first all-Black high school to win state basketball championship (1955)',
            'Freetown Village Living History Museum (Indianapolis)',
            'Levi Coffin House (Fountain City) — Underground Railroad "Grand Central Station"',
        ],
        'cultural_practices': [
            'Indiana Avenue jazz — rival to Chicago and Harlem in the 1930s–50s; Wes Montgomery performed here',
            'Circle City Classic — HBCU football classic, Indianapolis, Black cultural celebration',
        ],
    },

    'Iowa': {
        'population': '4.1% Black (131K)',
        'communities': [
            'Des Moines — Center Street corridor, historic Black neighborhood',
            'Waterloo — historically significant Black community, Rath Packing plant labor',
            'Cedar Rapids, Davenport, Iowa City — smaller Black communities',
            'Buxton (Mahaska County) — once one of the most integrated towns in America (1900–1920), majority-Black mining community, now a ghost town',
        ],
        'cultural_resources': [
            'Buxton, Iowa archaeological/historical site — model multiracial mining community, archaeological digs',
            'Iowa Juneteenth observances — among earliest in the Midwest',
        ],
        'cultural_practices': [
            'Buxton community legacy — represents utopian possibility of multiracial community in Jim Crow era',
        ],
    },

    'Kansas': {
        'population': '6.1% Black (180K)',
        'communities': [
            'Kansas City (Kansas side) — Quindaro/Sumner neighborhood (abolitionist free-state town)',
            'Wichita — northeast Wichita, McAdams neighborhood',
            'Topeka — Monroe neighborhood, site of Brown v. Board',
            'Nicodemus (Graham County) — oldest and only remaining Black settlement west of the Mississippi founded during Reconstruction Exodus (1877); National Historic Site',
            'Exodusters communities — post-Reconstruction migration from the South to Kansas (1879–80), led by Benjamin "Pap" Singleton',
        ],
        'cultural_resources': [
            'Nicodemus National Historic Site — only remaining western Black town from Reconstruction; five historic buildings; annual homecoming celebration',
            'Brown v. Board of Education National Historical Park (Topeka) — Monroe School, 1954 Supreme Court desegregation decision',
            'Quindaro Townsite National Commemorative Site — Underground Railroad terminus, free-state town',
            'Kansas African American Museum (Wichita)',
        ],
        'cultural_practices': [
            'Nicodemus Homecoming/Emancipation Celebration — held annually since 1878; oldest continuous Black celebration in the West',
            'Exoduster heritage — represents Black self-determination movement; Pap Singleton\'s vision of Black land ownership',
        ],
    },

    'Kentucky': {
        'population': '8.5% Black (382K)',
        'communities': [
            'Louisville — West End (Russell, Smoketown, California, Portland, Park DuValle, Chickasaw), historic Black neighborhoods',
            'Lexington — East End, Pralltown/Davis Bottom, Cadentown',
            'Camp Nelson — Civil War site where 10,000+ enslaved men enlisted as US Colored Troops',
            'Berea — historically integrated college town, founded for interracial education 1855',
        ],
        'cultural_resources': [
            'Camp Nelson National Monument — 10,000+ Black soldiers enlisted; refugee camp for their families; 400+ burials',
            'Muhammad Ali Center (Louisville) — cultural center honoring Louisville-born champion',
            'Kentucky Center for African American Heritage (Louisville)',
            'Whitney M. Young Jr. Birthplace (Simpsonville) — National Urban League leader',
            'Berea College — first interracial coeducational institution in the South (1855)',
            'Louisville Western Branch Library — first free public library in the nation fully operated for Black patrons (1905–1908 struggle by Rev. Thomas Blue)',
        ],
        'cultural_practices': [
            'Louisville\'s West End cultural traditions — Derby Day celebrations (historically segregated), Chestnut Street entertainment corridor',
            'Camp Nelson Memorial Day traditions — honoring US Colored Troops',
            'Kentucky bourbon industry Black labor — enslaved people built the bourbon industry; Nathan "Nearest" Green taught Jack Daniel to distill; largely unacknowledged until recently',
        ],
    },

    'Louisiana': {
        'population': '33.1% Black (1.5M) — 3rd highest percentage nationally',
        'communities': [
            'New Orleans — Tremé (oldest Black neighborhood in US), 7th Ward, 9th Ward (Lower Ninth), Central City, Algiers, Hollygrove, New Orleans East, Gentilly, Bywater',
            'Baton Rouge — North Baton Rouge, Scotlandville (Southern University), Old South Baton Rouge',
            'Shreveport — Allendale, Mooretown, Queensborough, MLK',
            'Louisiana Creole communities — French-speaking Black Creoles of south Louisiana; distinct from Cajun; concentrated in Natchitoches, St. Martinville, Opelousas, Lafayette, New Iberia',
            'Cane River Creole community (Natchitoches Parish) — free people of color community dating to colonial era; Isle Brevelle',
            'River Road plantation communities — descendants of enslaved people who remained along the Mississippi; "Cancer Alley" environmental justice zone',
            'Haitian diaspora — New Orleans has historical ties to Saint-Domingue/Haiti; 10,000+ refugees in 1809',
        ],
        'afro_indigenous': [
            'Mardi Gras Indians (Black Masking Indians) — African-descendant communities who honor relationships with Indigenous peoples through elaborate beaded suits; tribes include Wild Magnolias, Guardians of the Flame, Young Seminole Hunters, Golden Eagles, Wild Tchoupitoulas; tradition spans 200+ years',
            'Black-Houma connections — documented intermarriage between African Americans and United Houma Nation, particularly in Terrebonne Parish',
            'Afro-Creole-Indigenous families — some Cane River Creole families have documented Natchitoches/Caddo ancestry alongside African and French',
        ],
        'cultural_resources': [
            'Whitney Plantation (Edgard) — only plantation museum focused entirely on enslaved people\'s experience',
            'Tremé Historic District (New Orleans) — oldest African-descendant neighborhood in US, birthplace of jazz',
            'Congo Square / Louis Armstrong Park — where enslaved Africans gathered on Sundays to drum, dance, sell goods; birthplace of American musical culture',
            'St. Augustine Church (Tremé) — free people of color purchased pews for enslaved people; Tomb of the Unknown Slave',
            'Southern University (Baton Rouge) — largest HBCU in Louisiana, HBCU campus on the bluffs',
            'Dillard University (New Orleans) — HBCU',
            'Xavier University of Louisiana (New Orleans) — only historically Black Catholic university in US',
            'Laura Plantation — Creole plantation, enslaved persons\' stories documented including origin of Br\'er Rabbit tales (from West African Anansi tradition)',
            'Backstreet Cultural Museum (Tremé) — Mardi Gras Indian suits, second line umbrellas, jazz funeral traditions',
            'Le Musée de f.p.c. (New Orleans) — museum of free people of color',
            'Cane River Creole National Historical Park — Oakland and Magnolia Plantations, enslaved and free Creole community',
            'River Road African American Museum (Donaldsonville)',
            'New Orleans Jazz National Historical Park',
            'Amistad Research Center (Tulane) — largest independent archive of African American history',
        ],
        'cultural_practices': [
            'Jazz — born in New Orleans from the convergence of West African rhythmic traditions, blues, ragtime, brass band, and French/Spanish/Caribbean influences; Buddy Bolden, Louis Armstrong, Sidney Bechet, Jelly Roll Morton',
            'Second Line parades — community brass band processions following jazz funerals or organized by Social Aid and Pleasure Clubs; West African funeral procession lineage',
            'Mardi Gras Indian masking — African American communities build elaborate hand-beaded suits weighing 100+ pounds; "Big Chief" structure mirrors West African and Caribbean carnival traditions; tribes "meet" on Mardi Gras Day and Super Sunday',
            'Jazz funeral tradition — brass band plays dirges to cemetery, then "cuts the body loose" with jubilant music; West African transition-celebration of death',
            'Zydeco music — Creole music tradition combining French/Creole songs with African rhythms, blues, and R&B; Clifton Chenier, Buckwheat Zydeco; accordion and washboard (frottoir)',
            'Creole/Cajun French language — Louisiana Creole is a French-based creole with African grammatical structures; endangered, fewer than 10,000 speakers',
            'Voodoo/Vodou (New Orleans) — syncretic tradition blending Haitian Vodou, West African Vodun, Catholicism; Marie Laveau; distinct from Hollywood caricature',
            'Congo Square drumming — the survival of African percussion in the Americas; enslaved people\'s Sunday gatherings preserved rhythmic traditions that became jazz',
            'Gumbo and Creole cuisine — West African okra (ki ngombo), rice cultivation knowledge from Senegambia, filé (sassafras from Choctaw), roux from French; Creole cuisine as diasporic synthesis',
            'Skull and Bone gangs (Mardi Gras) — wake communities at dawn on Mardi Gras morning with skeleton costumes, announcing "you next"; connected to Kongo/BaKongo ancestral veneration',
            'Baby Dolls — women\'s Mardi Gras masking tradition from Black Storyville era (1912)',
            'Social Aid and Pleasure Club traditions — mutual aid societies (West African tontine lineage) that sponsor second line parades; benevolent associations dating to 1783',
        ],
    },

    'Maryland': {
        'population': '31.1% Black (1.9M) — 4th highest percentage nationally',
        'communities': [
            'Baltimore — West Baltimore, East Baltimore, Cherry Hill, Park Heights, Sandtown-Winchester, Druid Heights, Upton, Penn North, Mondawmin, Edmondson Village; historically segregated by redlining',
            'Prince George\'s County — wealthiest majority-Black county in US; Mitchellville, Bowie, Largo, Upper Marlboro, Fort Washington',
            'Silver Spring/Takoma Park — Ethiopian/Eritrean diaspora hub, one of densest concentrations in US',
            'Montgomery County — significant African immigrant communities',
            'Annapolis — historically Black communities displaced by Naval Academy expansion',
            'Eastern Shore Black communities — descendants of enslaved people, Harriet Tubman\'s birthplace region (Dorchester County)',
        ],
        'afro_indigenous': [
            'Black-Piscataway connections — documented intermarriage in southern Maryland since colonial era',
            'Wesort community (Charles County) — historically tri-racial community with African, Piscataway, and European ancestry; endured racial classification struggles',
        ],
        'cultural_resources': [
            'Harriet Tubman Underground Railroad National Historical Park (Church Creek, Dorchester County)',
            'Harriet Tubman Underground Railroad Byway — 125-mile driving route',
            'Reginald F. Lewis Museum (Baltimore) — Maryland African American history',
            'Great Blacks in Wax Museum (Baltimore)',
            'Frederick Douglass-Isaac Myers Maritime Park (Baltimore) — Douglass escaped from Baltimore',
            'Morgan State University (Baltimore) — HBCU',
            'Bowie State University — HBCU, oldest HBCU in Maryland (1865)',
            'University of Maryland Eastern Shore (Princess Anne) — HBCU',
            'Coppin State University (Baltimore) — HBCU',
            'Thurgood Marshall statue (Annapolis) — first Black Supreme Court Justice, Baltimore native',
            'Banneker-Douglass Museum (Annapolis) — state-supported Black history museum',
            'Benjamin Banneker Historical Park (Oella) — astronomer, surveyor who helped plan DC',
        ],
        'cultural_practices': [
            'Baltimore club music — fast-tempo, breakbeat-heavy dance music born in Baltimore\'s Black clubs; distinct from DC go-go and house music',
            'Baltimore step — social dance tradition with roots in stepping and Black Greek traditions',
            'Ethiopian/Eritrean cultural life in Silver Spring — the largest Ethiopian diaspora community concentration in America; restaurants, churches, cultural centers, Ge\'ez Academy',
            'Chesapeake Black waterman tradition — Black oystermen, crabbers, and fishermen; centuries-old maritime tradition; skipjack crewing',
            'Eastern Shore Underground Railroad heritage — Harriet Tubman\'s escape routes; coded songs, quilts, and star navigation',
        ],
    },

    'Massachusetts': {
        'population': '9.0% Black (630K)',
        'communities': [
            'Boston — Roxbury ("heart of Black Boston"), Dorchester (Codman Square, Four Corners, Fields Corner has Cape Verdean/Haitian communities), Mattapan (Haitian community center), Jamaica Plain, Hyde Park',
            'Springfield — Mason Square/Old Hill, historically significant Black community',
            'Brockton — large Cape Verdean and Haitian community',
            'Worcester Black community',
            'Cape Verdean communities — New Bedford, Brockton, Dorchester; one of oldest African diaspora groups in US (whaling industry brought Cape Verdeans to New England in 1800s)',
            'Haitian community — Mattapan, Dorchester, Brockton, Malden',
        ],
        'afro_indigenous': [
            'Black Wampanoag — documented African-Wampanoag intermarriage since 1600s; some Mashpee Wampanoag members have African ancestry; Amos Haskins, Black Wampanoag veteran of American Revolution',
            'Afro-Indigenous Nipmuc connections — mixed-race communities in colonial-era "Praying Towns"',
        ],
        'cultural_resources': [
            'Black Heritage Trail (Boston) — 14-site walking tour, Beacon Hill',
            'Museum of African American History (Boston/Nantucket) — African Meeting House (oldest standing Black church building in US, 1806), Abiel Smith School',
            'African Meeting House (Beacon Hill, Boston) — "Black Faneuil Hall"; Garrison founded New England Anti-Slavery Society here 1832',
            'New Bedford Whaling National Historical Park — includes Black whaling and maritime heritage; Frederick Douglass found freedom here',
            'Frederick Douglass arrived in New Bedford 1838 — worked on wharves; New Bedford was a center of Black maritime industry',
            'Crispus Attucks memorial (Boston Common) — first person killed in American Revolution (1770), Black/Indigenous',
            'William Monroe Trotter House (Dorchester) — radical civil rights editor',
        ],
        'cultural_practices': [
            'Cape Verdean morna and coladeira — musical traditions maintained in New England diaspora; Cesária Évora\'s tradition',
            'Cape Verdean cachupa — national dish maintained as community tradition in New Bedford, Brockton',
            'Haitian cultural celebrations — Haitian Flag Day (May 18), Kanaval traditions in Mattapan',
            'Boston abolitionist tradition — William Lloyd Garrison, Frederick Douglass, William C. Nell; Black activism since colonial era',
        ],
    },

    'Michigan': {
        'population': '14.1% Black (1.4M)',
        'communities': [
            'Detroit — Black Bottom (destroyed by I-375), Paradise Valley, Palmer Park, Conant Gardens, Sherwood Forest, Bagley, Rosedale Park, east side, west side; majority-Black since 1970s; Great Migration destination #2 after Chicago (migrants from Alabama, Mississippi, Georgia, Tennessee drawn by Ford Motor Company $5/day wage and auto industry)',
            'Flint — Northside, Civic Park; water crisis disproportionately impacted Black residents',
            'Saginaw, Grand Rapids, Muskegon, Benton Harbor, Pontiac, Inkster — significant Black communities',
            'Idlewild (Lake County) — "Black Eden," resort community from 1912; Aretha Franklin, W.E.B. Du Bois, Langston Hughes summered here',
        ],
        'cultural_resources': [
            'Charles H. Wright Museum of African American History (Detroit) — largest African American history museum in the world',
            'Motown Museum (Hitsville U.S.A., Detroit) — 2648 West Grand Boulevard, birthplace of Motown Records',
            'Idlewild Historic District — Black resort community',
            'Second Baptist Church (Detroit) — final stop on Underground Railroad to Canada (1836)',
            'Ossian Sweet House (Detroit) — 1925 self-defense case, Clarence Darrow defended',
        ],
        'cultural_practices': [
            'Motown sound — Berry Gordy\'s Motown Records (1959) created a global musical revolution from Detroit\'s Black community; Supremes, Temptations, Stevie Wonder, Marvin Gaye, Jackson 5',
            'Detroit techno — originated in Black Detroit in 1980s; Juan Atkins, Derrick May, Kevin Saunderson; continuation of Black electronic music innovation from disco through house',
            'Detroit\'s Black Bottom cultural traditions — destroyed by freeway construction; community documented through oral history',
            'Aretha Franklin gospel tradition — New Bethel Baptist Church, Rev. C.L. Franklin; gospel as foundation of soul music',
        ],
    },

    'Minnesota': {
        'population': '7.0% Black (400K)',
        'communities': [
            'Minneapolis — North Minneapolis (Near North, Harrison, Jordan, Willard-Hay), South Minneapolis (Phillips, Powderhorn); George Floyd killed at 38th & Chicago, May 25, 2020',
            'St. Paul — Rondo neighborhood (destroyed by I-94 construction), Frogtown/Thomas-Dale, Summit-University',
            'Somali community — largest Somali diaspora in US (100,000+ in Twin Cities); Cedar-Riverside ("Little Mogadishu"), Karmel Mall',
            'Oromo community — significant Ethiopian Oromo population in Twin Cities',
            'Liberian community — Brooklyn Park, Brooklyn Center',
        ],
        'cultural_resources': [
            'George Floyd Square (38th & Chicago, Minneapolis) — community memorial site',
            'Rondo neighborhood historical markers (St. Paul) — Black community destroyed by I-94',
            'Sabathani Community Center (Minneapolis) — Black community institution since 1966',
            'Penumbra Theatre (St. Paul) — August Wilson premiered many plays here',
        ],
        'cultural_practices': [
            'Somali cultural practices — poetry (Somali oral poetry is among world\'s richest traditions), hees (song), Eid celebrations, qaaddo (communal eating), dhaqan celis (cultural restoration of diaspora youth)',
            'Rondo Days — annual celebration honoring destroyed Rondo neighborhood, St. Paul',
            'Prince/Minneapolis Sound — Black musical innovation from Minneapolis; fusion of funk, rock, R&B, new wave',
        ],
    },

    'Mississippi': {
        'population': '38.0% Black (1.1M) — highest percentage of any US state',
        'communities': [
            # Mississippi Delta — the most culturally significant African-descendant region in the US
            'Mississippi Delta — alluvial floodplain between Memphis and Vicksburg; majority-Black since enslavement era; cradle of the Blues; Great Migration departure point for Chicago, Detroit, St. Louis',
            'Clarksdale (Coahoma County) — crossroads of Highways 61 and 49; Muddy Waters, Bessie Smith, Son House, John Lee Hooker, Sam Cooke connections; Ground Zero Blues Club, Riverside Hotel (where Bessie Smith died)',
            'Greenville (Washington County) — Delta\'s largest city; literary and civil rights tradition; 1927 Great Flood devastated Black community; Nelson Street entertainment district',
            'Greenwood (Leflore County) — SNCC voter registration headquarters 1962–64; Emmett Till\'s body recovered from Tallahatchie River near here; Robert Johnson\'s grave (one of three claimed sites)',
            'Indianola (Sunflower County) — B.B. King\'s hometown; B.B. King Museum; also Sunflower County where Fannie Lou Hamer organized',
            'Ruleville (Sunflower County) — Fannie Lou Hamer\'s home; "I\'m sick and tired of being sick and tired"; registered to vote 1962 and was evicted from plantation; SNCC Freedom School',
            'Money (Leflore County) — Bryant\'s Grocery, where 14-year-old Emmett Till was accused (1955); murder galvanized the civil rights movement',
            'Sumner (Tallahatchie County) — Tallahatchie County courthouse where Till\'s murderers were acquitted by all-white jury',
            'Rolling Fork (Sharkey County) — Muddy Waters\'s birthplace (McKinley Morganfield, 1913); destroyed by tornado 2023',
            'Tutwiler (Tallahatchie County) — where W.C. Handy first heard the Blues at the train station (1903); Tutwiler Tracks',
            'Mound Bayou (Bolivar County) — all-Black town founded 1887 by Isaiah T. Montgomery (formerly enslaved by Jefferson Davis\'s family) and Benjamin Green; "Jewel of the Delta"; had own hospital, bank, cotton oil mill; model of Black self-determination',
            'Dockery Plantation (Sunflower County) — "birthplace of the Delta Blues"; Charley Patton, Howlin\' Wolf, Roebuck Staples, Robert Johnson all connected; cotton plantation where Blues evolved from field hollers',
            'Stovall Plantation (Coahoma County) — where Muddy Waters was recorded by Alan Lomax for Library of Congress (1941); cabin preserved at Delta Blues Museum',
            'Parchman Farm / Mississippi State Penitentiary (Sunflower County) — prison farm where Blues were documented by John and Alan Lomax; Bukka White, Son House, Leadbelly served time; Freedom Riders imprisoned here 1961; symbol of convict-lease system and forced labor',
            'Rosedale (Bolivar County) — Robert Johnson "Cross Road Blues" connection; historic Delta community',
            'Leland (Washington County) — Jim Henson\'s hometown, but also significant Black community; Highway 61 corridor',
            'Belzoni (Humphreys County) — Rev. George Lee murdered for voter registration 1955; "Catfish Capital"',
            'Yazoo City (Yazoo County) — historic Black community; integrated schools 1970; connections to broader Delta culture',
            'Drew (Sunflower County) — Parchman Farm proximity; sharecropping community',
            'Merigold (Bolivar County) — Po\' Monkey\'s juke joint (closed 2016), last rural juke joint in Mississippi',
            # Non-Delta Mississippi
            'Jackson — Farish Street Historic District, west Jackson, south Jackson; Medgar Evers\'s home; Jackson State University; capital city and cultural center',
            'Natchez — oldest settlement on Mississippi River; large free Black community before Civil War; Forks of the Road slave market (second largest in the South); Natchez Under-the-Hill',
            'Vicksburg — Black community integral to Civil War history; siege of Vicksburg; Black Union soldiers',
            'Hattiesburg — Palmer\'s Crossing, historically significant civil rights community; Vernon Dahmer murdered by KKK 1966',
            'Meridian — Jimmie Rodgers/country music connection, but also significant Black community; Chaney, Goodman, Schwerner connection (Philadelphia, MS nearby)',
            'Philadelphia/Neshoba County — murders of Chaney, Goodman, Schwerner (1964); Mississippi Burning case',
            'Oxford/Lafayette County — James Meredith integrated Ole Miss 1962',
            'Holly Springs (Marshall County) — Rust College (HBCU); Ida B. Wells\'s birthplace',
            'Tate County / Panola County — Hill Country Blues territory; distinct from Delta Blues',
        ],
        'cultural_resources': [
            'Delta Blues Museum (Clarksdale) — Muddy Waters\'s cabin from Stovall Plantation',
            'B.B. King Museum and Delta Interpretive Center (Indianola)',
            'GRAMMY Museum Mississippi (Cleveland)',
            'Emmett Till and Mamie Till-Mobley National Monument (2023) — multiple sites: Graball Landing, Roberts Temple (Chicago), Tallahatchie County Courthouse (Sumner)',
            'Fannie Lou Hamer Memorial Garden (Ruleville)',
            'Medgar Evers Home Museum (Jackson) — National Monument, NAACP field secretary assassinated 1963',
            'Farish Street Historic District (Jackson) — Black commercial district',
            'Smith Robertson Museum (Jackson) — first public school for Black children in Jackson (1894), Richard Wright attended',
            'Dockery Plantation (Cleveland area) — birthplace of Delta Blues; commissary building preserved',
            'Mound Bayou historic district — all-Black town',
            'Ground Zero Blues Club (Clarksdale) — Morgan Freeman co-owned; in historic downtown',
            'Riverside Hotel (Clarksdale) — formerly G.T. Thomas Afro-American Hospital where Bessie Smith died 1937; converted to hotel where every major Blues musician stayed',
            'Robert Johnson\'s crossroads (Clarksdale area) — legendary site of "deal with the devil"',
            'Forks of the Road slave market site (Natchez) — second largest slave market in the antebellum South',
            'Alcorn State University (Lorman) — oldest public HBCU (1871)',
            'Jackson State University — HBCU; 1970 police killings of Phillip Lafayette Gibbs and James Earl Green',
            'Tougaloo College — HBCU; civil rights movement center; Freedom Riders, sit-ins',
            'Rust College (Holly Springs) — HBCU, founded 1866; Ida B. Wells attended',
            'Mississippi Valley State University (Itta Bena) — HBCU in the Delta',
            'Coahoma Community College (Clarksdale) — Delta education',
            'Mt. Zion United Methodist Church (Longdale, Neshoba County) — burned by KKK 1964, leading to murders of Chaney, Goodman, Schwerner',
        ],
        'cultural_practices': [
            'Delta Blues — the foundational African American musical form; Robert Johnson, Son House, Muddy Waters, Charley Patton, B.B. King, Howlin\' Wolf, John Lee Hooker; emerged from field hollers on cotton plantations (Dockery, Stovall); direct lineage from West African griot tradition; bottleneck slide guitar, AAB lyric form, blue notes',
            'Hill Country Blues — distinct from Delta flatland Blues; hypnotic, droning, trance-like rhythm from Tate/Panola/Marshall County hill country; R.L. Burnside, Junior Kimbrough, Fred McDowell, Jessie Mae Hemphill; connected to West African trance music traditions; North Mississippi Allstars continue tradition',
            'Parchman Farm Blues / Prison Blues — songs documented at Mississippi State Penitentiary by John and Alan Lomax (1930s–40s); work songs, field hollers, and blues from forced labor; Bukka White "Parchman Farm Blues," Son House served time; convict-lease system perpetuated slavery conditions',
            'Field hollers and work songs — pre-Blues vocal tradition; solo, unaccompanied calls across cotton fields; direct link to West African call-and-response; Lomax recordings at Parchman and plantations',
            'Juke joint tradition — informal Black entertainment spaces; shotgun shacks or rural buildings with live Blues, dancing, moonshine; Red\'s Lounge (Clarksdale), Po\' Monkey\'s (Merigold, closed 2016), Blue Front Café (Bentonia); endangered by depopulation',
            'Fife and drum tradition — direct West African musical survival in Tate/Panola County; Othar Turner, Rising Star Fife and Drum Band, Sharde Thomas; goatskin drums and cane fifes; the most intact African musical survival in North America',
            'Sharecropping and tenant farming — the economic system that defined Black Delta life from Reconstruction to mechanization (1865–1960s); quarter system, company store debt peonage, cotton cycle; created the conditions from which Blues emerged and Great Migration fled',
            'Decoration Day / graveyard cleaning — annual tradition of cleaning and decorating family graves; gathering of extended family; distinct from Memorial Day; rooted in West African ancestor veneration; practiced across the rural South but especially strong in Delta',
            'River baptism tradition — full-immersion baptism in rivers, creeks, and bayous; deeply rooted in Black Baptist and African spiritual traditions of water as sacred passage; Sunflower River, Tallahatchie River, Mississippi River',
            'Shotgun house architecture — one-room-wide houses; Yoruba/Haitian architectural lineage; prevalent in Delta towns; endangered',
            'Quilting traditions — Delta quilting distinct from Gee\'s Bend; strip quilts, string quilts, improvisational design; West African textile aesthetics',
            'Catfish farming and foodways — Mississippi catfish industry built on Black agricultural knowledge; fried catfish, hot tamales (brought by Mexican workers who shared Delta labor), sweet potato pie; Delta-specific foodways',
            'Hot tamales tradition — brought to the Delta by Mexican and Central American migrant workers alongside Black laborers; adopted and adapted by Black Delta communities; Doe\'s Eat Place (Greenville), tamale vendors throughout Delta; a unique Afro-Latino culinary convergence',
        ],
    },

    'Missouri': {
        'population': '11.8% Black (720K)',
        'communities': [
            'St. Louis — The Ville, Wellston, Ferguson, Jennings, North St. Louis, Hyde Park, Old North; historically segregated by Delmar Divide; Great Migration destination via Illinois Central and L&N railroads (migrants from Mississippi, Arkansas, Tennessee)',
            'Kansas City — 18th & Vine Historic District, Ivanhoe, Troost Avenue divide, Historic Northeast',
            'Ferguson — site of Michael Brown shooting (2014) and subsequent uprising',
            'Columbia Black community — small but historic',
        ],
        'cultural_resources': [
            'Scott Joplin House State Historic Site (St. Louis) — King of Ragtime',
            '18th & Vine Historic District (Kansas City) — American Jazz Museum, Negro Leagues Baseball Museum',
            'Gateway Arch — built with integrated labor force; Black workers died in construction',
            'Shelley House (St. Louis) — Shelley v. Kraemer 1948, Supreme Court struck down racial covenants',
            'Homer G. Phillips Hospital site (St. Louis) — once premier Black hospital in US',
            'Lincoln University (Jefferson City) — HBCU founded by Black Civil War soldiers (1866)',
        ],
        'cultural_practices': [
            'Kansas City jazz — Count Basie, Charlie Parker; 18th & Vine corridor; distinct from New Orleans and Chicago styles; jam session tradition',
            'St. Louis ragtime — Scott Joplin, precursor to jazz; African-descended compositional innovation',
            'St. Louis blues tradition — W.C. Handy, "St. Louis Blues"; different feel from Delta and Chicago',
            'Kansas City barbecue — Arthur Bryant\'s, Gates BBQ; Black pitmaster tradition; sauce and smoking techniques',
        ],
    },

    'New York': {
        'population': '17.6% Black (3.5M) — largest Black population of any US state by number',
        'communities': [
            'New York City — Harlem (cultural capital of Black America), Bedford-Stuyvesant, Crown Heights, Flatbush, East New York, Brownsville, Jamaica (Queens), St. Albans, South Bronx, Morrisania, Mott Haven; Great Migration destination via Atlantic Coast Line and Pennsylvania railroads (migrants from South Carolina, Georgia, Virginia, North Carolina, Florida); Harlem\'s population went from 10% to 70% Black 1910–1930',
            'Harlem — 125th Street, Sugar Hill, Strivers\' Row, Hamilton Heights, East Harlem (formerly Italian/Puerto Rican, now mixed); Harlem Renaissance center',
            'Bedford-Stuyvesant (Brooklyn) — largest Black community in Brooklyn; Restoration Plaza',
            'Crown Heights (Brooklyn) — Caribbean community center; West Indian Day Parade on Eastern Parkway',
            'Flatbush/East Flatbush (Brooklyn) — Haitian, Jamaican, Trinidadian, Guyanese communities',
            'Seneca Village (Central Park) — destroyed 1857 for Central Park construction; one of first Black property-owning communities in NYC; archaeology ongoing',
            'Weeksville (Brooklyn) — free Black community founded 1838; Hunterfly Road houses preserved',
            'Buffalo — East Side, historic Black community; Tops supermarket mass shooting site (2022)',
            'Rochester, Syracuse, Albany, Yonkers — significant Black communities',
            'Little Senegal (Harlem) — West African immigrant community, 116th Street',
            'Little Haiti (Flatbush, Brooklyn) — Nostrand Avenue and Church Avenue corridor',
            'Little Caribbean (Flatbush, Brooklyn) — NYC\'s first Caribbean cultural district',
        ],
        'afro_indigenous': [
            'Afro-Shinnecock — documented African-Shinnecock intermarriage on Long Island since 1700s; some Shinnecock Nation members have African ancestry',
            'Black Haudenosaunee — historical presence of African-descended people in Haudenosaunee communities; some escaped slavery to Haudenosaunee territory',
        ],
        'cultural_resources': [
            'Schomburg Center for Research in Black Culture (Harlem, NYPL) — world\'s leading research facility devoted to Black history and culture; Arturo Alfonso Schomburg\'s original collection',
            'National Museum of African American History (proposed Harlem extension)',
            'Studio Museum in Harlem — premier museum of Black art',
            'Apollo Theater (Harlem) — "the Palace" of Black entertainment since 1934',
            'African Burial Ground National Monument (Lower Manhattan) — 15,000+ enslaved and free Africans buried 1690s–1790s; discovered 1991; most important urban archaeological project in US history',
            'Weeksville Heritage Center (Brooklyn) — preserved 1860s houses of free Black community',
            'Seneca Village site (Central Park) — archaeological site of destroyed Black community',
            'Abyssinian Baptist Church (Harlem) — Adam Clayton Powell Jr., founded 1808',
            'Langston Hughes House (Harlem) — National Historic Landmark',
            'Louis Armstrong House Museum (Corona, Queens)',
            'Jackie Robinson House (Stamford, CT / Brooklyn connection)',
            'Medgar Evers College (Brooklyn) — CUNY institution named for civil rights leader',
            'Harlem cultural landmarks — Hotel Theresa, Minton\'s Playhouse, Small\'s Paradise, Lenox Lounge, Cotton Club site',
        ],
        'cultural_practices': [
            'Harlem Renaissance — 1920s–30s explosion of Black art, literature, music, and thought; Langston Hughes, Zora Neale Hurston, Claude McKay, Aaron Douglas, Augusta Savage, Duke Ellington; most influential Black cultural movement in American history',
            'Bebop jazz — born at Minton\'s Playhouse and Monroe\'s Uptown House in Harlem; Charlie Parker, Dizzy Gillespie, Thelonious Monk; revolution in American music',
            'Hip-hop — originated in South Bronx in 1970s; DJ Kool Herc (Jamaican-born), Afrika Bambaataa, Grandmaster Flash; most globally influential cultural export of the late 20th century; direct lineage from West African griot tradition through toasting, signifying, and dozens',
            'West Indian Day Parade/Carnival (Labor Day, Eastern Parkway) — largest Caribbean carnival in North America; 1–3 million participants; soca, calypso, steel pan, mas (masquerade); rooted in Trinidad Carnival tradition',
            'Brooklyn dancehall culture — Jamaican dancehall and reggae maintained in Caribbean community',
            'Haitian Rara in Brooklyn — Lenten street processions with bamboo instruments',
            'Harlem Shake (original) — community dance from Harlem, predating the internet meme',
            'Stepping/Black Greek step shows — competitive synchronized dance tradition rooted in African-descendant fraternity/sorority culture',
            'African Burial Ground ceremonies — annual October remembrance ceremony honoring the 15,000+ interred',
        ],
    },

    'North Carolina': {
        'population': '22.2% Black (2.3M)',
        'communities': [
            'Durham — Hayti District ("Black Wall Street of the South"), historically wealthiest Black community in America; North Carolina Central University (HBCU)',
            'Charlotte — West End, Biddleville, Johnson C. Smith University (HBCU)',
            'Raleigh — Shaw University (HBCU, oldest in the South), Southeast Raleigh, St. Augustine\'s University (HBCU)',
            'Greensboro — East Greensboro, NC A&T State University (HBCU), Bennett College (HBCU)',
            'Winston-Salem — East Winston, Winston-Salem State University (HBCU)',
            'Wilmington — Northside; 1898 Wilmington Coup, only successful armed overthrow of a US government; Black aldermen, police chief, and newspaper editor driven out or killed',
            'Princeville — oldest town incorporated by African Americans (1885); devastated by Hurricane Floyd 1999 and Hurricane Matthew 2016',
        ],
        'cultural_resources': [
            'International Civil Rights Center & Museum (Greensboro) — Woolworth lunch counter sit-in site (1960)',
            'Hayti Heritage Center (Durham) — remains of "Black Wall Street of the South"',
            'North Carolina Mutual Life Insurance Company (Durham) — largest Black-owned business in US for decades',
            'Shaw University (Raleigh) — SNCC was founded here in 1960',
            'Bennett College (Greensboro) — HBCU for women',
            'NC A&T State University (Greensboro) — Greensboro Four students, largest HBCU in NC',
            '1898 Wilmington Coup memorial — only successful violent overthrow of elected US government; mob destroyed Black newspaper Daily Record',
            'Princeville (Edgecombe County) — oldest Black-incorporated town in America',
            'Stagville Plantation (Durham) — one of largest plantations in the South; extensive enslaved persons\' community documentation',
        ],
        'cultural_practices': [
            'Piedmont blues — Blind Boy Fuller, Reverend Gary Davis; lighter, ragtime-influenced acoustic blues distinct from Delta',
            'HBCU homecoming traditions — NC A&T, NC Central, Shaw, Johnson C. Smith; marching band competitions, step shows, tailgating',
            'Jabberwock step competitions — Black sorority step show tradition, strong in NC',
            'Carolina shag (dance) — interracial dance tradition from Carolina beaches; beach music',
        ],
    },

    'Ohio': {
        'population': '13.1% Black (1.5M)',
        'communities': [
            'Cleveland — Hough, Glenville, Mount Pleasant, Central; Great Migration destination',
            'Cincinnati — Walnut Hills, Avondale, Over-the-Rhine (historic), West End; Underground Railroad terminus',
            'Columbus — King-Lincoln/Bronzeville, Linden, Hilltop, East Side',
            'Dayton — West Dayton, DeSoto Bass; Paul Laurence Dunbar\'s hometown',
            'Akron, Toledo, Youngstown — significant Black communities',
            'Wilberforce — Wilberforce University (oldest private HBCU, 1856), Central State University (HBCU)',
            'Oberlin — historic interracial abolitionist community; Oberlin-Wellington Rescue (1858)',
        ],
        'cultural_resources': [
            'National Underground Railroad Freedom Center (Cincinnati)',
            'Paul Laurence Dunbar House (Dayton) — first nationally acclaimed Black poet',
            'Charles Young Buffalo Soldiers National Monument (Wilberforce) — first Black colonel in US Army',
            'Wilberforce University (1856) — oldest private HBCU',
            'Karamu House (Cleveland) — oldest Black performing arts institution in US (1915)',
            'African American Museum (Cleveland)',
            'National Afro-American Museum and Cultural Center (Wilberforce)',
        ],
        'cultural_practices': [
            'Cleveland soul/R&B — connection to Motown; Bobby Womack, Bone Thugs-N-Harmony',
            'Cincinnati R&B/funk — Bootsy Collins, Ohio Players, Midnight Star',
            'Underground Railroad heritage — Ohio was the primary crossing point; over 3,000 documented safe houses',
        ],
    },

    'Oklahoma': {
        'population': '7.8% Black (310K)',
        'communities': [
            'Tulsa — Greenwood District ("Black Wall Street"), North Tulsa; 1921 Tulsa Race Massacre destroyed 35 blocks',
            'Oklahoma City — Deep Deuce Historic District, NE Oklahoma City',
            'Langston — all-Black town, Langston University (HBCU)',
            'Boley, Taft, Rentiesville, Clearview, Tullahassee, Red Bird — all-Black towns, more than 50 were established in Indian Territory/Oklahoma',
        ],
        'afro_indigenous': [
            'Freedmen of the Five Tribes — descendants of people enslaved by Cherokee, Chickasaw, Choctaw, Creek/Muscogee, and Seminole nations; brought on Trail of Tears; fought for citizenship rights; some denied citizenship by their nations despite treaty obligations',
            'Cherokee Freedmen — won citizenship rights in Cherokee Nation through litigation (2017 Cherokee Supreme Court ruling)',
            'Chickasaw Freedmen — still denied citizenship by Chickasaw Nation',
            'Choctaw Freedmen — denied citizenship; ongoing legal battles',
            'Creek/Muscogee Freedmen — citizenship recognized',
            'Seminole Freedmen — fought alongside Seminole; Seminole Freedmen Bands',
            'Black Indian identity — many Oklahoma residents identify as both Black and Indian; distinct cultural identity',
        ],
        'cultural_resources': [
            'Greenwood Cultural Center / Greenwood Rising (Tulsa) — 1921 Race Massacre history museum and memorial',
            'John Hope Franklin Reconciliation Park (Tulsa)',
            'Deep Deuce Historic District (OKC) — Charlie Christian (jazz guitarist), Jimmy Rushing',
            'Langston University — HBCU',
            'All-Black Towns historic sites — Boley (National Historic Landmark), Taft, others; largest concentration in US',
        ],
        'cultural_practices': [
            'Black Wall Street heritage — Greenwood District had 600+ Black businesses, hospital, bank, schools, and its own bus system before 1921 destruction',
            'All-Black town traditions — annual celebrations, rodeos, homecomings at Boley, Langston, and other surviving towns',
            'Oklahoma City jazz — Deep Deuce corridor; Charlie Christian invented amplified jazz guitar here',
            'Freedmen cultural practices — blending of African-descendant and tribal cultural elements; Freedmen communities maintain distinct traditions',
        ],
    },

    'Pennsylvania': {
        'population': '12.0% Black (1.5M)',
        'communities': [
            'Philadelphia — North Philadelphia, West Philadelphia, Germantown, Mount Airy, Oak Lane, South Philadelphia (Point Breeze, Grays Ferry), Southwest; first free Black community in a northern city; Great Migration destination (migrants from Georgia, South Carolina, Virginia, North Carolina via Pennsylvania Railroad)',
            'Pittsburgh — Hill District ("Little Harlem"), Homewood, East Liberty, Manchester; August Wilson\'s Hill District; Great Migration destination (migrants from Alabama, Mississippi, Virginia via steel industry labor recruitment)',
            'Harrisburg — Allison Hill, Uptown',
            'Chester, Camden (NJ connection) — Black industrial communities',
        ],
        'cultural_resources': [
            'Mother Bethel AME Church (Philadelphia) — oldest AME congregation (1794), Richard Allen; Underground Railroad site',
            'President\'s House (Independence Mall, Philadelphia) — enslaved persons of George Washington; memorial to Oney Judge and others',
            'Johnson House (Germantown) — Underground Railroad site, National Historic Landmark',
            'August Wilson House (Pittsburgh) — childhood home of Pulitzer Prize-winning playwright',
            'August Wilson African American Cultural Center (Pittsburgh)',
            'African American Museum in Philadelphia — founded 1976, first major Black history museum in US',
            'Lincoln University (Chester County) — first HBCU (1854), Thurgood Marshall and Langston Hughes attended',
            'Cheyney University (Chester County) — oldest HBCU (1837)',
            'Henry Ossawa Tanner House (Philadelphia) — first internationally acclaimed Black painter',
        ],
        'cultural_practices': [
            'Philadelphia soul/Philly Sound — Gamble & Huff, TSOP Records, The O\'Jays, Harold Melvin & the Blue Notes, Patti LaBelle; lush orchestral soul',
            'Philadelphia hip-hop — The Roots, Schoolly D (early gangsta rap), Jill Scott, Meek Mill; neo-soul; Black Thought\'s lyricism',
            'Pittsburgh\'s Hill District cultural tradition — August Wilson\'s ten-play Pittsburgh Cycle documenting Black life in every decade of the 20th century; Crawford Grill jazz',
            'Mummers Parade — historically excluded Black participation; parallel Black performance traditions',
            'Philadelphia Odunde Festival — largest African American street festival in US (since 1975); Yoruba-rooted New Year celebration',
        ],
    },

    'South Carolina': {
        'population': '27.0% Black (1.4M)',
        'communities': [
            'Charleston — East Side, West Ashley, North Charleston, Johns Island, James Island; slave port through which 40% of enslaved Africans entered North America',
            'Gullah/Geechee communities — Sea Islands (St. Helena, Hilton Head, Edisto, Johns Island, Wadmalaw, Kiawah, Daufuskie); continuous cultural connection to West Africa',
            'Columbia — Waverly, Allen University (HBCU), Benedict College (HBCU)',
            'Beaufort/Port Royal — Penn Center (first school for freed slaves, 1862), Reconstruction-era Black community',
            'Orangeburg — South Carolina State University (HBCU), Claflin University (HBCU); Orangeburg Massacre 1968',
            'Denmark — Voorhees University (HBCU)',
        ],
        'afro_indigenous': [
            'Gullah/Geechee-Cusabo connections — intermarriage between enslaved Africans and coastal Indigenous peoples',
            'Brass Ankles, Turks, and other tri-racial communities — mixed African, Indigenous, and European communities in rural SC, historically denied classification',
        ],
        'cultural_resources': [
            'International African American Museum (Charleston) — opened 2023, built on Gadsden\'s Wharf where 100,000+ enslaved Africans were disembarked',
            'Penn Center National Historic Landmark (St. Helena Island) — first school for freed people (1862); Dr. King retreated here to draft speeches',
            'Gullah/Geechee Cultural Heritage Corridor (NPS) — from Jacksonville NC to Jacksonville FL',
            'Emanuel AME Church (Charleston) — "Mother Emanuel," founded 1816; 2015 mass shooting killed 9',
            'Old Slave Mart Museum (Charleston) — only surviving building used as a slave market in SC',
            'McLeod Plantation Historic Site (James Island) — enslaved persons\' cabins preserved; Gullah/Geechee connection',
            'Drayton Hall — oldest surviving plantation house in US; enslaved persons\' archaeology',
            'Boone Hall Plantation — brick slave quarters ("Slave Street") preserved',
            'Robert Smalls House (Beaufort) — enslaved man who stole Confederate ship and piloted it to freedom; later US Congressman',
            'Reconstruction Era National Historical Park (Beaufort) — Reconstruction history',
            'Avery Research Center (Charleston) — archives of African American history in the Lowcountry',
        ],
        'cultural_practices': [
            'Gullah/Geechee language — English-based creole with substantial West African vocabulary and grammar (Mende, Vai, Fula, Wolof, Temne, Krio influences); UNESCO recognized as endangered',
            'Sweetgrass basket weaving — coiled basketry technique from Sierra Leone/Senegambia; practiced by Gullah/Geechee women on Mt. Pleasant, Charleston; 300+ year unbroken tradition; most direct West African craft survival in the Americas',
            'Ring shout — counterclockwise circular worship movement with roots in West/Central African spiritual traditions; documented on St. Helena Island',
            'Indigo and rice cultivation knowledge — enslaved Africans, particularly from Senegambia and Sierra Leone, brought the agricultural expertise that built South Carolina\'s plantation economy',
            'Gullah/Geechee foodways — red rice (Jollof lineage), hoppin\' John, shrimp and grits, she-crab soup; West African culinary techniques',
            'Spirituals — "Goin\' Home," "Michael Row the Boat Ashore" and other spirituals originated in Sea Islands; collected by abolitionists at Penn Center',
            'Gullah storytelling — Br\'er Rabbit tales (from Anansi spider trickster of Akan/Ashanti tradition)',
        ],
    },

    'Tennessee': {
        'population': '17.1% Black (1.2M)',
        'communities': [
            'Memphis — Orange Mound (first community built by and for Black Americans, 1890), South Memphis, Whitehaven, Binghampton, Frayser, North Memphis, Downtown (Beale Street)',
            'Nashville — North Nashville, Jefferson Street corridor (Fisk University, Meharry Medical College, Tennessee State University — three HBCUs), East Nashville',
            'Knoxville — East Knoxville, Mechanicsville',
            'Chattanooga — MLK neighborhood, East Side',
        ],
        'cultural_resources': [
            'National Civil Rights Museum (Memphis) — Lorraine Motel, where MLK was assassinated April 4, 1968',
            'Beale Street Historic District (Memphis) — "Home of the Blues"; W.C. Handy Park',
            'Stax Museum of American Soul Music (Memphis) — Soulsville USA',
            'Sun Studio (Memphis) — recorded early blues and rock; interracial musical exchange',
            'Fisk University (Nashville) — HBCU, Jubilee Hall (oldest permanent structure for higher education of Black students), Aaron Douglas murals',
            'Meharry Medical College (Nashville) — first medical school for Black Americans in the South (1876)',
            'Tennessee State University (Nashville) — HBCU; Wilma Rudolph, Oprah Winfrey attended',
            'Fisk Jubilee Singers — preserved and popularized Negro spirituals globally since 1871; UNESCO Memory of the World',
            'Alex Haley House Museum (Henning) — Roots author',
            'Orange Mound community (Memphis) — first neighborhood in US built by and for Black Americans',
            'Slave Haven Underground Railroad Museum / Burkle Estate (Memphis)',
        ],
        'cultural_practices': [
            'Memphis Blues — W.C. Handy documented and published Delta blues; Beale Street as Black entertainment epicenter; foundation of rock and roll',
            'Memphis soul — Stax Records (Otis Redding, Sam & Dave, Booker T. & the MGs, Isaac Hayes), Hi Records (Al Green); raw, gritty soul distinct from Motown polish',
            'Jubilee Singers tradition — Fisk Jubilee Singers\' 1871 tour saved Fisk University and introduced Negro spirituals to the world; sacred choral tradition continues',
            'Memphis barbecue — Black pitmaster tradition; dry rub, pulled pork shoulder; Cozy Corner, Payne\'s, A&R',
            'Nashville sit-in tradition — John Lewis, Diane Nash led lunch counter sit-ins 1960; Nashville Student Movement',
        ],
    },

    'Texas': {
        'population': '13.2% Black (3.9M) — 2nd largest Black population by number',
        'communities': [
            'Houston — Third Ward (TSU, Project Row Houses), Fifth Ward (Phillis Wheatley High School), Sunnyside, Acres Homes, Kashmere Gardens, South Park, South Union; largest Black population in Texas',
            'Dallas — South Dallas, Fair Park, Oak Cliff, Cedar Crest',
            'San Antonio — East Side, Eastside Promise Zone',
            'Austin — East Austin (Rosewood, Chestnut, 12th Street corridor; rapidly gentrifying)',
            'Fort Worth — Stop Six, Como, Polytechnic Heights/South Side',
            'Galveston — Juneteenth origin city (June 19, 1865); Ashton Villa where General Order No. 3 was read',
            'Beaumont/Port Arthur — historically Black communities, petrochemical industry labor',
            'Nigerian community (Houston) — one of largest in US, concentrated in Alief and SW Houston',
            'Haitian and other Caribbean communities in Houston',
        ],
        'afro_indigenous': [
            'Buffalo Soldiers at Texas frontier forts — Fort Davis, Fort Concho, Fort Clark, Fort McKavett; 9th and 10th Cavalry, 24th and 25th Infantry',
            'Seminole Negro Indian Scouts — descendants of Black Seminoles who went to Mexico; recruited by US Army at Fort Clark (Brackettville) 1870–1914; four won Medal of Honor; community persists in Brackettville',
            'Afro-Creole communities in East Texas — extension of Louisiana Creole culture; Zydeco tradition',
        ],
        'cultural_resources': [
            'Juneteenth birthplace (Galveston) — Ashton Villa, June 19, 1865; national holiday since 2021',
            'Buffalo Soldiers National Museum (Houston)',
            'Fort Davis National Historic Site — Buffalo Soldiers headquarters in West Texas',
            'Freedmen\'s Town (Houston Fourth Ward) — brick streets laid by formerly enslaved people; largely demolished despite preservation efforts',
            'Texas Southern University (Houston) — HBCU',
            'Prairie View A&M University — HBCU, Prairie View',
            'Huston-Tillotson University (Austin) — HBCU',
            'Paul Quinn College (Dallas) — HBCU',
            'Project Row Houses (Houston Third Ward) — community art and social institution in shotgun houses',
            'Seminole Negro Indian Scouts Cemetery (Brackettville) — Medal of Honor recipients',
        ],
        'cultural_practices': [
            'Juneteenth — originated in Galveston June 19, 1865; now a federal holiday; the oldest nationally celebrated African American holiday',
            'Texas Blues — Blind Lemon Jefferson, T-Bone Walker, Lightnin\' Hopkins, Stevie Ray Vaughan (influenced by Black tradition); distinct acoustic and electric traditions',
            'Houston hip-hop — DJ Screw (chopped and screwed), UGK, Scarface/Geto Boys, Megan Thee Stallion, Travis Scott; H-Town rap as continuation of Southern Black oral tradition',
            'Zydeco in East Texas — extension of Louisiana Creole tradition; accordion-driven music',
            'Trail ride tradition — Houston-area Black trail rides (Prairie View, Salt Grass); horseback culture; Black cowboys were 25% of all cowboys in the West',
            'Black cowboy heritage — Bass Reeves (first Black US Deputy Marshal), Bill Pickett (inventor of bulldogging); rodeo tradition',
        ],
    },

    'Virginia': {
        'population': '20.0% Black (1.7M)',
        'communities': [
            'Richmond — Jackson Ward ("Harlem of the South"), Church Hill, Highland Park, East End, Northside; capital of the Confederacy with deep Black history',
            'Norfolk/Hampton Roads — Huntersville, Berkley, Brambleton, Campostella; Norfolk State University (HBCU), Hampton University (HBCU)',
            'Hampton — Fort Monroe (where first Africans arrived 1619), Phoebus, Hampton University campus',
            'Newport News — Southeast Community, Newsome Park',
            'Charlottesville — Vinegar Hill (Black business district demolished 1965 by urban renewal)',
            'Danville, Lynchburg, Petersburg, Suffolk — historically significant Black communities',
            'First Landing 1619 site (Point Comfort/Fort Monroe) — "20 and odd Negroes" arrived August 1619; beginning of slavery in English North America',
        ],
        'afro_indigenous': [
            'Afro-Powhatan connections — documented intermarriage between free Black people and Pamunkey, Mattaponi, and other Virginia tribal communities; complicated by Walter Plecker\'s "Racial Integrity Act" which classified both groups as "colored"',
            'Nottoway and free Black community connections — intermarriage documented in Southampton County',
        ],
        'cultural_resources': [
            'Fort Monroe National Monument (Hampton) — "Freedom\'s Fortress"; first Africans in English North America arrived here 1619; Union fort where enslaved people were declared "contraband of war" 1861',
            'Hampton University (Hampton) — HBCU founded 1868; Hampton University Museum (oldest African American museum in US, founded 1868)',
            'Norfolk State University — HBCU',
            'Virginia Union University (Richmond) — HBCU',
            'Virginia State University (Petersburg) — HBCU',
            'Jackson Ward Historic District (Richmond) — "Harlem of the South"; Maggie Walker (first woman to charter a bank in US)',
            'Maggie L. Walker National Historic Site (Richmond)',
            'Black History Museum and Cultural Center of Virginia (Richmond)',
            'Robert Russa Moton Museum (Farmville) — 1951 student walkout led by Barbara Johns, became part of Brown v. Board',
            'Booker T. Washington National Monument (Hardy) — birthplace of Tuskegee founder',
            'Colonial Williamsburg — ongoing archaeology of enslaved people\'s quarters; living history interpreters',
            'Blandford Church (Petersburg) — enslaved persons\' burial ground',
            'Historic Jamestowne — 1619 arrival site; "Angela" first documented African woman in English North America',
        ],
        'cultural_practices': [
            'Hampton-Tuskegee model — Booker T. Washington\'s industrial education philosophy began at Hampton Institute; shaped Black education nationally',
            'Virginia spirituals tradition — Virginia is origin of many documented spirituals; preserved at Hampton',
            'Black fraternity/sorority founding — Alpha Phi Alpha (Cornell 1906) and others have strong Virginia HBCU connections; step show tradition',
            'Richmond hip-hop — Pharrell Williams, Missy Elliott, Timbaland from Virginia; "Virginia sound"',
        ],
    },

    # ── US TERRITORIES ─────────────────────────────────────────────────────

    'Puerto Rico': {
        'population': '12.4% self-identified Black/Afro-Puerto Rican (2020 census) — historically underreported due to racial dynamics; estimated 75%+ have African ancestry',
        'communities': [
            'Loíza — historically Black municipality; center of Afro-Puerto Rican culture; largest concentration of people of African descent in PR',
            'Carolina/Piñones — Afro-Puerto Rican coastal community; mangrove ecosystem',
            'Santurce — Afro-Puerto Rican cultural center in metro San Juan',
            'Guayama — southern coast, historically significant Afro-Puerto Rican community',
            'Ponce — Playa de Ponce, historically Black neighborhoods',
        ],
        'afro_indigenous': [
            'Afro-Taíno Puerto Ricans — most Puerto Ricans carry both African and Taíno ancestry; genetic studies show significant Indigenous maternal and African paternal lineage; cultural blending across 500 years',
        ],
        'cultural_resources': [
            'Museo de la Raza Africana en Puerto Rico (proposed) — documenting African heritage',
            'Piñones boardwalk and cultural sites — Afro-Puerto Rican fishing community and food traditions',
            'Loíza cultural sites — Iglesia de San Patricio, vejigante mask workshops',
            'Hacienda Buena Vista (Ponce) — restored coffee plantation with enslaved persons\' quarters',
            'Fortín de San Gerónimo — built with enslaved labor',
        ],
        'cultural_practices': [
            'Bomba — Afro-Puerto Rican drum and dance tradition; direct link to West African and Kongo percussion traditions; call-and-response between dancer and lead drummer (primo); practiced in Loíza, Santurce, Ponce; oldest surviving musical tradition in Puerto Rico',
            'Plena — Afro-Puerto Rican musical form using panderetas (hand drums); "the newspaper of the people"; storytelling tradition; originated in Ponce\'s Black community',
            'Vejigante masking (Loíza) — African-derived masquerade tradition for Fiestas de Santiago Apóstol; coconut shell masks (distinct from Ponce papier-mâché); represents African warrior resisting colonialism',
            'Fiestas de Santiago Apóstol (Loíza) — annual festival blending African spiritual traditions with Catholic saints; largest Afro-Puerto Rican cultural celebration',
            'Cocina criolla afropuertorriqueña — mofongo (from West African fufu), pasteles, arroz con gandules; cooking with pilón (mortar) of African origin',
            'Madama/espiritismo — Afro-Puerto Rican spiritual practice blending African, Taíno, and Catholic traditions',
        ],
    },

    'US Virgin Islands': {
        'population': '76.0% Black (76K) — majority-Black territory; largest percentage of any US jurisdiction',
        'communities': [
            'St. Croix — Frederiksted (freedom city; emancipation proclaimed here 1848), Christiansted; Danish colonial history',
            'St. Thomas — Charlotte Amalie; historic free Black community',
            'St. John — Coral Bay; 1733 slave rebellion (one of first in the Americas)',
        ],
        'afro_indigenous': [
            'Afro-Taíno-Kalinago Virgin Islanders — layered Indigenous and African heritage; cultural practices from all three ancestral streams',
        ],
        'cultural_resources': [
            'Christiansted National Historic Site (St. Croix) — Danish colonial buildings, enslaved persons\' history',
            'Fort Frederik (Frederiksted) — where emancipation was proclaimed July 3, 1848, after enslaved people\'s revolt led by "General Buddhoe" (Moses Gottlieb)',
            'Estate Whim Museum (St. Croix) — plantation museum with enslaved persons\' quarters',
            'Annaberg Plantation ruins (St. John, NPS) — sugar mill and enslaved persons\' village',
            'Haagensen House (St. Thomas) — colonial merchant house documenting slavery',
        ],
        'cultural_practices': [
            'Crucian Carnival (St. Croix) — J\'ouvert morning celebration with roots in emancipation; quelbe music; mocko jumbie stilt walkers',
            'Quelbe/scratch music — USVI indigenous music combining African drumming with European fiddle and guitar; "official music" of USVI',
            'Mocko Jumbie — stilt-walking masquerade tradition from West Africa; protective spiritual figure; performed at Carnival',
            'Quadrille dance — formal dance tradition adapted from European colonial dances by enslaved people; distinct USVI version',
            'Fungi/funchi (cornmeal dish) — West African culinary survival; community food tradition',
            'Bamboula drum — large single-headed drum tradition connecting to West African and Kongo drumming; used in quelbe and cultural celebrations',
        ],
    },

    'Guam': {
        'population': '1.5% Black (~2.5K) — almost entirely military-connected',
        'communities': [
            'Military base communities — Naval Base Guam, Andersen AFB',
        ],
        'afro_indigenous': [
            'Afro-CHamoru individuals — children of African American military personnel and CHamoru families; navigating both cultural identities in Pacific island context',
        ],
        'cultural_resources': [],
        'cultural_practices': [],
    },

    'American Samoa': {
        'population': '<1% Black — minimal population',
        'communities': [],
        'afro_indigenous': [
            'Afro-Samoan individuals — growing population globally (represented by athletes, cultural figures); complex identity navigation within fa\'a Sāmoa',
        ],
        'cultural_resources': [],
        'cultural_practices': [],
    },

    'Northern Mariana Islands (CNMI)': {
        'population': '<1% Black — minimal population, military-connected',
        'communities': [],
        'afro_indigenous': [],
        'cultural_resources': [],
        'cultural_practices': [],
    },

    'Republic of the Marshall Islands': {
        'population': 'Minimal Black population; COFA citizens in US face racial discrimination',
        'communities': [
            'Marshallese diaspora in US — Springdale AR, Enid OK, Salem OR communities include some mixed-race Afro-Marshallese individuals',
        ],
        'afro_indigenous': [],
        'cultural_resources': [],
        'cultural_practices': [],
    },

    # ── MISSING STATES (added for completeness) ───────────────────────────

    'Wisconsin': {
        'population': '6.7% Black (390K)',
        'communities': [
            'Milwaukee — Bronzeville (historic, centered on Walnut Street), Sherman Park, North Division, Harambee, Lindsay Heights, Metcalfe Park, Capitol Drive corridor; most segregated metro in US by multiple measures; Great Migration destination (1920s–60s from Mississippi, Arkansas, Tennessee)',
            'Madison — South Side, Allied Drive; smaller but growing Black community',
            'Racine/Kenosha — industrial labor communities; Great Migration legacy',
            'Beloit — significant Black community relative to size',
        ],
        'cultural_resources': [
            'America\'s Black Holocaust Museum (Milwaukee) — founded by James Cameron, only known survivor of a lynching',
            'Bronzeville Cultural and Entertainment District (Milwaukee) — revitalization of historic Black neighborhood',
            'Milwaukee Art Museum — significant African American art collection',
        ],
        'cultural_practices': [
            'Milwaukee Juneteenth Day celebration — one of oldest and largest in the Midwest (since 1971)',
            'Great Migration cultural retention from Mississippi and Arkansas — Delta Blues, gospel, and soul food traditions transplanted to Milwaukee',
        ],
    },

    'New Jersey': {
        'population': '15.1% Black (1.4M)',
        'communities': [
            'Newark — Central Ward, South Ward, West Ward, Clinton Hill, Weequahic; Great Migration destination; Amiri Baraka\'s home; 1967 Newark uprising',
            'Trenton — historic Black community',
            'Camden — Centerville, Parkside; deindustrialized Black community',
            'Atlantic City — Northside, historically segregated resort city; Black entertainers performed but couldn\'t stay in hotels they played',
            'Paterson — historic Black community, Great Falls',
            'East Orange, Irvington, Plainfield, Asbury Park — historically Black communities',
            'Lawnside (Camden County) — one of oldest self-governing Black communities in northern US; pre-Civil War free Black settlement; Underground Railroad stop',
        ],
        'cultural_resources': [
            'Newark Museum of Art — significant African American collection',
            'Harriet Tubman Museum (Cape May) — honoring Tubman\'s time working in Cape May',
            'Lawnside historical sites — free Black community, Peter Mott House (Underground Railroad)',
        ],
        'cultural_practices': [
            'Newark jazz and spoken word — Amiri Baraka\'s Black Arts Movement; jazz tradition at Newark\'s clubs',
            'Jersey club music — electronic dance music from Newark\'s Black community',
            'Atlantic City Black entertainment legacy — Club Harlem, Paradise Club on Kentucky Avenue; Sammy Davis Jr., Sarah Vaughan',
        ],
    },

    'Oregon': {
        'population': '2.2% Black (93K) — small percentage but significant history',
        'communities': [
            'Portland — Albina neighborhood (historically Black community decimated by I-5, Emanuel Hospital expansion, and gentrification; went from 80% Black to 25%); North/NE Portland, MLK Boulevard corridor; Great Migration Second Wave destination (1940s, Kaiser Shipyards)',
            'Vanport — largest wartime housing project in US; majority-Black area destroyed by Columbia River flood 1948; residents displaced to Albina',
            'Salem, Eugene — smaller Black communities',
        ],
        'cultural_resources': [
            'Oregon Black Pioneers — historical organization documenting Black Oregon history',
            'Vanport Mosaic project — documenting the destroyed city',
            'Billy Webb Elks Lodge (Portland) — historic Black social club',
            'Golden West Hotel (Portland) — one of few hotels that would serve Black travelers',
        ],
        'cultural_practices': [
            'Oregon exclusion law legacy — Oregon was only state admitted with an exclusion law barring Black residents (1857); shapes current demographics and racial dynamics',
            'Albina community preservation efforts — against ongoing gentrification',
        ],
    },

    'Washington': {
        'population': '4.4% Black (340K)',
        'communities': [
            'Seattle — Central District ("the CD"), historically Black from 1890s through 2000s; Rainier Beach, Columbia City; gentrification has displaced much of Black community; Great Migration Second Wave destination (1940s, Boeing/shipyards)',
            'Tacoma — Hilltop neighborhood, historically Black community; Fort Lewis connection',
            'Joint Base Lewis-McChord — military-connected Black community',
        ],
        'afro_indigenous': [
            'Black-Indigenous Pacific Northwesterners — small but documented community of African American and Coast Salish, Duwamish, and other PNW Indigenous ancestry',
        ],
        'cultural_resources': [
            'Northwest African American Museum (Seattle) — in former Colman School, historic Black school',
            'Jimi Hendrix statue and Park (Seattle) — born in Seattle\'s Central District',
            'East Madison Street/Jackson Street jazz corridor — historic Black entertainment district',
        ],
        'cultural_practices': [
            'Seattle jazz tradition — Jackson Street clubs 1930s–60s; Ray Charles, Quincy Jones, Ernestine Anderson started here',
            'Central District community defense — organizing against displacement/gentrification',
        ],
    },

    'Nevada': {
        'population': '10.3% Black (320K)',
        'communities': [
            'Las Vegas — Historic Westside (Jackson Street corridor), North Las Vegas; during Jim Crow, Black entertainers (Sammy Davis Jr., Nat King Cole, Lena Horne, Ella Fitzgerald) performed on the Strip but were barred from staying in the hotels; had to stay in Westside boarding houses; Moulin Rouge Hotel (1955) was first integrated casino',
            'Reno — small but historic Black community',
            'Nellis AFB, Creech AFB — military-connected communities',
        ],
        'cultural_resources': [
            'Harrison House (Las Vegas) — boarding house for Black entertainers during segregation',
            'Moulin Rouge Hotel site (Las Vegas) — first integrated casino-hotel (1955); National Register',
            'Historic Westside School (Las Vegas) — segregated-era school, now community center',
        ],
        'cultural_practices': [
            'Las Vegas Westside entertainment tradition — during Jim Crow, Westside was "the Black Strip"; Cotton Club, Town Tavern, El Morocco; parallel entertainment ecosystem',
        ],
    },

    'West Virginia': {
        'population': '3.6% Black (64K)',
        'communities': [
            'Charleston — East End, Kanawha City',
            'Huntington, Martinsburg, Beckley — smaller Black communities',
            'Coal mining communities — Black coal miners in McDowell County, Fayette County, Raleigh County; recruited from Alabama and Virginia; company towns; United Mine Workers integrated earlier than most unions',
            'Institute — West Virginia State University (HBCU), historically Black community',
            'Bluefield — Bluefield State University (HBCU)',
        ],
        'cultural_resources': [
            'West Virginia State University (Institute) — HBCU; Carter G. Woodson taught here',
            'Bluefield State University — HBCU',
            'African Zion Baptist Church (Malden) — Booker T. Washington\'s childhood church; where he learned to read',
            'Booker T. Washington cultural sites (Malden) — worked in salt furnaces and coal mines as a child before going to Hampton Institute',
        ],
        'cultural_practices': [
            'Black coal mining heritage — company towns, union organizing; songs and oral traditions from mining communities; Carter G. Woodson (founder of Black History Month) was a coal miner before attending Berea College',
        ],
    },

    'Rhode Island': {
        'population': '8.5% Black (92K)',
        'communities': [
            'Providence — South Side (South Providence, Broad Street corridor), West End, Olneyville; Cape Verdean, Liberian, Dominican communities',
            'Newport — historically significant; colonial-era enslaved population; one of major slave trade ports',
        ],
        'cultural_resources': [
            'God\'s Little Acre / Newport Common Burying Ground — largest collection of colonial-era African and African American gravestones in the US; carved stone art shows African symbolic traditions',
            'Isaac Rice House (Newport) — site connected to Colonial-era Black community',
            'Rhode Island Black Heritage Society (Providence)',
        ],
        'cultural_practices': [
            'Newport slave trade history — Rhode Island was the leading slave-trading state in the US; DeWolf family of Bristol was the largest slave-trading family in American history; annual acknowledgment and memorial',
            'Cape Verdean diaspora traditions in Providence — morna, batuku, cachupa; maintained since 1800s whaling connections',
        ],
    },

    'New Mexico': {
        'population': '2.6% Black (55K)',
        'communities': [
            'Albuquerque — South Valley, International District; small but historic community',
            'Las Cruces, Roswell — military-connected communities',
            'Blackdom (Chaves County) — all-Black town founded 1901 by Frank Boyer; the only Black settlement in New Mexico Territory; abandoned 1920s but archaeological site remains',
        ],
        'afro_indigenous': [
            'Afro-Indigenous New Mexicans — small but documented community of people with African and Pueblo or Navajo ancestry; some trace to Spanish colonial era (African soldiers and settlers in New Spain)',
            'Estevanico/Esteban (1539) — Moroccan/African explorer who was the first non-Indigenous person to enter the Pueblo world; critical historical figure',
        ],
        'cultural_resources': [
            'Blackdom historic site (near Dexter, NM) — archaeological remains of all-Black town',
            'Fort Bayard — Buffalo Soldiers, 9th Cavalry',
        ],
        'cultural_practices': [
            'Buffalo Soldier heritage in New Mexico — 9th and 10th Cavalry stationed at Fort Bayard, Fort Stanton, Fort Selden',
        ],
    },

    'Nebraska': {
        'population': '5.2% Black (101K)',
        'communities': [
            'Omaha — North Omaha (Near North Side, Florence, Benson corridor); historically Black; Malcolm X born here (1925); Great Migration community',
            'Lincoln — small but growing Black community; African refugee communities (Sudanese, South Sudanese)',
        ],
        'cultural_resources': [
            'Great Plains Black History Museum (Omaha)',
            'Malcolm X House Site (Omaha) — birthplace of Malcolm Little (1925)',
            'Dreamland Historical Ballroom site (Omaha) — historic Black entertainment venue',
        ],
        'cultural_practices': [
            'North Omaha jazz tradition — Dreamland Ballroom, Carvery\'s Lounge; Omaha was stop on the "Chitlin\' Circuit"',
        ],
    },

    'Montana': {
        'population': '0.6% Black (7K)',
        'communities': [
            'Great Falls — military connected (Malmstrom AFB)',
            'Helena, Missoula, Billings — tiny but documented Black communities',
        ],
        'cultural_resources': [
            'York — enslaved man who traveled with Lewis and Clark; only enslaved person on the expedition; contributed significantly but received no land or freedom upon return',
        ],
        'cultural_practices': [],
    },

    'Idaho': {
        'population': '0.9% Black (18K)',
        'communities': [
            'Boise — growing Black and African refugee community',
            'Mountain Home AFB — military-connected community',
        ],
        'cultural_resources': [],
        'cultural_practices': [],
    },

    'South Dakota': {
        'population': '2.3% Black (21K)',
        'communities': [
            'Sioux Falls — growing African refugee community (Sudanese, South Sudanese, Somali, Ethiopian, Congolese); significant relative to city size',
        ],
        'afro_indigenous': [
            'Afro-Lakota individuals — documented community of people with both African American and Lakota ancestry',
        ],
        'cultural_resources': [],
        'cultural_practices': [
            'African refugee cultural maintenance in Sioux Falls — South Sudanese community celebrations, Somali Eid gatherings, Ethiopian coffee ceremonies; one of the fastest-growing African diaspora communities in the Midwest',
        ],
    },

    'North Dakota': {
        'population': '3.4% Black (27K)',
        'communities': [
            'Fargo — growing African refugee community (Somali, South Sudanese, Congolese, Bhutanese)',
            'Grand Forks AFB, Minot AFB — military-connected',
        ],
        'cultural_resources': [],
        'cultural_practices': [],
    },

    'Utah': {
        'population': '1.5% Black (48K)',
        'communities': [
            'Salt Lake City — Rose Park, Glendale, West Side; small but historic Black community; complicated relationship with LDS Church (priesthood ban on Black men until 1978)',
            'Ogden — historic railroad Black community',
        ],
        'cultural_resources': [
            'Utah Black History collection (University of Utah) — documenting small but significant community',
            'Calvary Baptist Church (Salt Lake City) — oldest Black church in Utah',
        ],
        'cultural_practices': [
            'Black LDS (Latter-day Saints) experience — complex history of exclusion and faith; 1978 revelation ending priesthood ban; Black Mormon history',
        ],
    },

    'Vermont': {
        'population': '1.4% Black (9K)',
        'communities': [
            'Burlington — New North End; growing African refugee community (Somali Bantu, Bhutanese, Congolese)',
        ],
        'cultural_resources': [
            'Daisy Turner homestead (Grafton) — African American family homestead from 1870s; Daisy Turner was a renowned storyteller; subject of Jane Beck\'s oral history work',
        ],
        'cultural_practices': [
            'African refugee community building in Burlington — Somali Bantu farming cooperatives; community gardens using traditional agricultural knowledge',
        ],
    },

    'New Hampshire': {
        'population': '1.8% Black (25K)',
        'communities': [
            'Manchester, Nashua — growing African refugee communities',
            'Portsmouth — Black Heritage Trail documenting colonial-era African presence',
        ],
        'cultural_resources': [
            'Portsmouth Black Heritage Trail — documenting 400 years of Black history in Portsmouth',
            'Wentworth-Gardner House — colonial-era enslaved persons\' history',
        ],
        'cultural_practices': [],
    },

    'Wyoming': {
        'population': '1.3% Black (8K)',
        'communities': [
            'F.E. Warren AFB (Cheyenne) — military-connected community',
        ],
        'cultural_resources': [
            'Buffalo Soldiers at Fort Laramie and Fort D.A. Russell — 9th and 10th Cavalry history in Wyoming',
        ],
        'cultural_practices': [],
    },
}

# ---------------------------------------------------------------------------
# GREAT MIGRATION FRAMEWORK
# The Great Migration (1910–1970) was the movement of 6 million African
# Americans from the rural South to cities in the North, Midwest, and West.
# It transformed American culture, politics, music, literature, and cities.
# ---------------------------------------------------------------------------

GREAT_MIGRATION = {
    'first_wave': {
        'period': '1910–1940 (approximately 1.6 million people)',
        'causes': 'Boll weevil devastation of cotton economy, Jim Crow violence, lynching, sharecropping debt peonage, World War I labor demand in northern factories',
        'routes': {
            'Mississippi River corridor': {
                'origins': ['Mississippi Delta', 'Arkansas Delta', 'West Tennessee', 'Louisiana', 'Alabama Black Belt'],
                'destinations': ['Chicago (Illinois Central Railroad)', 'St. Louis', 'Milwaukee', 'Minneapolis'],
                'railroad': 'Illinois Central Railroad — "the Chickenbone Express"; $11.10 from Mississippi to Chicago',
            },
            'Eastern seaboard corridor': {
                'origins': ['South Carolina Lowcountry', 'Georgia', 'North Carolina', 'Virginia', 'Florida'],
                'destinations': ['New York City / Harlem', 'Philadelphia', 'Newark', 'Baltimore', 'Washington DC', 'Boston', 'Hartford', 'Pittsburgh'],
                'railroad': 'Atlantic Coast Line, Seaboard Air Line, Pennsylvania Railroad',
            },
            'Gulf Coast corridor': {
                'origins': ['Louisiana', 'East Texas', 'Alabama'],
                'destinations': ['Detroit', 'Cleveland', 'Indianapolis', 'Cincinnati'],
                'railroad': 'Louisville & Nashville Railroad',
            },
        },
    },
    'second_wave': {
        'period': '1940–1970 (approximately 5 million people)',
        'causes': 'WWII defense industry labor demand, mechanization of cotton agriculture, continued racial violence, Cold War military expansion',
        'routes': {
            'Western corridor': {
                'origins': ['Louisiana', 'Texas', 'Oklahoma', 'Arkansas', 'Mississippi'],
                'destinations': ['Los Angeles', 'Oakland/San Francisco', 'Portland', 'Seattle', 'Phoenix', 'Las Vegas', 'San Diego', 'Denver'],
                'railroad': 'Southern Pacific Railroad; also Route 66 by automobile',
            },
            'Continued northern corridor': {
                'origins': ['Same southern origins plus Appalachian coalfields'],
                'destinations': ['Continued growth of Chicago, Detroit, Cleveland, NYC, Philadelphia, Newark; also smaller cities like Gary, Flint, Saginaw, Pontiac'],
            },
        },
    },
    'cultural_impact': [
        'Chicago Blues (from Delta Blues) — Muddy Waters brought Delta Blues from Stovall Plantation to Maxwell Street; amplified it electrically; created modern Blues and ultimately rock and roll',
        'Harlem Renaissance (from southern folk culture) — Claude McKay, Langston Hughes, Zora Neale Hurston transformed southern oral and folk traditions into literary modernism',
        'Motown (from southern gospel and R&B) — Berry Gordy\'s Motown Records in Detroit; migrant families from Alabama, Mississippi, Georgia created the Motown sound',
        'The Chicago Defender — most important Black newspaper; actively recruited southern Blacks to move North; Robert S. Abbott',
        'The Chitlin\' Circuit — touring route for Black entertainers connecting southern and northern Black venues; Apollo Theater, Howard Theatre, Regal Theater, Royal Peacock',
        'Northern Black church development — migrants brought Baptist and AME church traditions; churches became political and social hubs in new cities',
        'Soul food in northern cities — migrants brought southern foodways; restaurants and grocery stores created "taste of home"',
        'Great Migration literature — Richard Wright (Black Boy, Native Son), Ralph Ellison (Invisible Man), Lorraine Hansberry (A Raisin in the Sun), Isabel Wilkerson (The Warmth of Other Suns)',
    ],
}

# ---------------------------------------------------------------------------
# COMPLETE HBCU LIST (107 institutions)
# Historically Black Colleges and Universities, organized by state
# These are the 107 institutions recognized by the US Department of Education
# ---------------------------------------------------------------------------

HBCU_BY_STATE = {
    'Alabama': [
        'Alabama A&M University (Normal/Huntsville) — public, 1875',
        'Alabama State University (Montgomery) — public, 1867',
        'Bishop State Community College (Mobile) — public 2-year, 1927',
        'Concordia College Alabama (Selma) — private, 1922; LCMS affiliated',
        'Drake State Community and Technical College (Huntsville) — public 2-year, 1961',
        'Gadsden State Community College (Gadsden) — public 2-year',
        'H. Councill Trenholm State Community College (Montgomery) — public 2-year, 1966',
        'J.F. Ingram State Technical College (Deatsville) — public 2-year',
        'Lawson State Community College (Birmingham) — public 2-year, 1949',
        'Miles College (Fairfield/Birmingham) — private, 1898; CME Church',
        'Oakwood University (Huntsville) — private, 1896; Seventh-day Adventist',
        'Selma University (Selma) — private, 1878; Baptist',
        'Shelton State Community College (Tuscaloosa) — public 2-year',
        'Stillman College (Tuscaloosa) — private, 1876; Presbyterian',
        'Talladega College (Talladega) — private, 1867; first to admit Black students in Alabama',
        'Tuskegee University (Tuskegee) — private, 1881; Booker T. Washington founder; National Historic Site',
    ],
    'Arkansas': [
        'Arkansas Baptist College (Little Rock) — private, 1884',
        'Philander Smith University (Little Rock) — private, 1877; United Methodist',
        'Shorter College (North Little Rock) — private 2-year, 1886; AME Church',
        'University of Arkansas at Pine Bluff — public, 1873',
    ],
    'California': [
        'Charles R. Drew University of Medicine and Science (Los Angeles) — private, 1966',
    ],
    'Delaware': [
        'Delaware State University (Dover) — public, 1891',
    ],
    'District of Columbia': [
        'Howard University — private, 1867; preeminent HBCU; Moorland-Spingarn Research Center',
        'University of the District of Columbia — public, 1851; only urban land-grant HBCU',
    ],
    'Florida': [
        'Bethune-Cookman University (Daytona Beach) — private, 1904; Mary McLeod Bethune founder',
        'Edward Waters University (Jacksonville) — private, 1866; oldest HBCU in Florida; AME Church',
        'Florida A&M University (Tallahassee) — public, 1887; Marching 100 band; law and pharmacy schools',
        'Florida Memorial University (Miami Gardens) — private, 1879',
    ],
    'Georgia': [
        'Albany State University — public, 1903',
        'Clark Atlanta University (Atlanta) — private, 1988 (merger of Clark 1869 and Atlanta 1865); AUC member',
        'Fort Valley State University — public, 1895',
        'Interdenominational Theological Center (Atlanta) — private, 1958; AUC member',
        'Morehouse College (Atlanta) — private, 1867; men\'s college; MLK Jr., Samuel L. Jackson, Spike Lee alma mater',
        'Morehouse School of Medicine (Atlanta) — private, 1975',
        'Morris Brown College (Atlanta) — private, 1881; AME Church; AUC member; regaining accreditation',
        'Paine College (Augusta) — private, 1882; CME Church and United Methodist',
        'Savannah State University — public, 1890; oldest public HBCU in Georgia',
        'Spelman College (Atlanta) — private, 1881; women\'s college; AUC member; most prestigious HBCU for women',
    ],
    'Kentucky': [
        'Kentucky State University (Frankfort) — public, 1886',
        'Simmons College of Kentucky (Louisville) — private, 1879; Baptist',
    ],
    'Louisiana': [
        'Dillard University (New Orleans) — private, 1869; United Methodist and United Church of Christ',
        'Grambling State University — public, 1901; Eddie Robinson, legendary football coach',
        'Southern University and A&M College (Baton Rouge) — public, 1880; largest HBCU system',
        'Southern University at New Orleans — public, 1956',
        'Southern University at Shreveport — public 2-year, 1964',
        'Xavier University of Louisiana (New Orleans) — private, 1925; only historically Black Catholic university in US; #1 in placing Black students in medical school',
    ],
    'Maryland': [
        'Bowie State University — public, 1865; oldest HBCU in Maryland',
        'Coppin State University (Baltimore) — public, 1900',
        'Morgan State University (Baltimore) — public, 1867',
        'University of Maryland Eastern Shore (Princess Anne) — public, 1886',
    ],
    'Michigan': [
        'Lewis College of Business (Detroit) — private, 1928',
    ],
    'Mississippi': [
        'Alcorn State University (Lorman) — public, 1871; oldest public HBCU',
        'Coahoma Community College (Clarksdale) — public 2-year, 1949',
        'Hinds Community College–Utica Campus — public 2-year, 1903',
        'Jackson State University — public, 1877; Sonic Boom marching band',
        'Mississippi Valley State University (Itta Bena) — public, 1950; Jerry Rice alma mater',
        'Rust College (Holly Springs) — private, 1866; United Methodist; Ida B. Wells attended',
        'Tougaloo College — private, 1869; civil rights movement center',
    ],
    'Missouri': [
        'Harris-Stowe State University (St. Louis) — public, 1857',
        'Lincoln University (Jefferson City) — public, 1866; founded by Black Union soldiers of 62nd and 65th US Colored Infantry',
    ],
    'North Carolina': [
        'Barber-Scotia College (Concord) — private, 1867; Presbyterian',
        'Bennett College (Greensboro) — private, 1873; women\'s college; United Methodist',
        'Elizabeth City State University — public, 1891',
        'Fayetteville State University — public, 1867',
        'Johnson C. Smith University (Charlotte) — private, 1867; Presbyterian',
        'Livingstone College (Salisbury) — private, 1879; AME Zion Church',
        'North Carolina A&T State University (Greensboro) — public, 1891; largest HBCU in NC; Greensboro Four',
        'North Carolina Central University (Durham) — public, 1910; law school',
        'Saint Augustine\'s University (Raleigh) — private, 1867; Episcopal',
        'Shaw University (Raleigh) — private, 1865; oldest HBCU in the South; SNCC founded here 1960',
        'Winston-Salem State University — public, 1892',
    ],
    'Ohio': [
        'Central State University (Wilberforce) — public, 1887',
        'Wilberforce University (Wilberforce) — private, 1856; oldest private HBCU; AME Church',
    ],
    'Oklahoma': [
        'Langston University — public, 1897; only HBCU in Oklahoma',
    ],
    'Pennsylvania': [
        'Cheyney University of Pennsylvania — public, 1837; oldest HBCU in the nation',
        'Lincoln University — public, 1854; Thurgood Marshall, Langston Hughes attended',
    ],
    'South Carolina': [
        'Allen University (Columbia) — private, 1870; AME Church',
        'Benedict College (Columbia) — private, 1870; Baptist',
        'Claflin University (Orangeburg) — private, 1869; United Methodist',
        'Clinton College (Rock Hill) — private 2-year, 1894; AME Zion Church',
        'Denmark Technical College — public 2-year, 1948',
        'Morris College (Sumter) — private, 1908; Baptist',
        'South Carolina State University (Orangeburg) — public, 1896; Orangeburg Massacre 1968',
        'Voorhees University (Denmark) — private, 1897; Episcopal',
    ],
    'Tennessee': [
        'American Baptist College (Nashville) — private, 1924; John Lewis attended',
        'Fisk University (Nashville) — private, 1866; Fisk Jubilee Singers; W.E.B. Du Bois, Nikki Giovanni attended',
        'Knoxville College — private, 1875; United Presbyterian; undergoing revitalization',
        'Lane College (Jackson) — private, 1882; CME Church',
        'LeMoyne-Owen College (Memphis) — private, 1862; United Church of Christ',
        'Meharry Medical College (Nashville) — private, 1876; first medical school for Black Americans in the South',
        'Tennessee State University (Nashville) — public, 1912; Wilma Rudolph, Oprah Winfrey attended',
    ],
    'Texas': [
        'Huston-Tillotson University (Austin) — private, 1875; United Methodist and United Church of Christ',
        'Jarvis Christian University (Hawkins) — private, 1912; Disciples of Christ',
        'Paul Quinn College (Dallas) — private, 1872; AME Church',
        'Prairie View A&M University — public, 1876; second-oldest public HBCU in Texas',
        'St. Philip\'s College (San Antonio) — public 2-year, 1898; only HBCU that is also a Hispanic-Serving Institution',
        'Southwestern Christian College (Terrell) — private, 1948; Churches of Christ',
        'Texas College (Tyler) — private, 1894; CME Church',
        'Texas Southern University (Houston) — public, 1947; Thurgood Marshall School of Law',
        'Wiley College (Marshall) — private, 1873; United Methodist; Great Debaters',
    ],
    'Virginia': [
        'Hampton University (Hampton) — private, 1868; Hampton University Museum (oldest African American museum)',
        'Norfolk State University — public, 1935',
        'Saint Paul\'s College (Lawrenceville) — private, 1888; closed 2013',
        'Virginia State University (Petersburg) — public, 1882',
        'Virginia Union University (Richmond) — private, 1865; Baptist',
        'Virginia University of Lynchburg — private, 1886; Baptist',
    ],
    'US Virgin Islands': [
        'University of the Virgin Islands (St. Thomas/St. Croix) — public, 1962; only HBCU in a US territory',
    ],
    'West Virginia': [
        'Bluefield State University — public, 1895',
        'West Virginia State University (Institute) — public, 1891; Carter G. Woodson taught here',
    ],
}

# ---------------------------------------------------------------------------
# HISTORIC BLACK PLACES OF WORSHIP
# Churches, mosques, synagogues, and temples significant to
# African-descendant history and culture, organized by state
# ---------------------------------------------------------------------------

HISTORIC_BLACK_PLACES_OF_WORSHIP = {
    'Alabama': [
        '16th Street Baptist Church (Birmingham) — site of 1963 bombing that killed Addie Mae Collins, Cynthia Wesley, Carole Robertson, Carol Denise McNair; National Historic Landmark',
        'Dexter Avenue King Memorial Baptist Church (Montgomery) — MLK pastored 1954–1960; bus boycott organized here',
        'Brown Chapel AME Church (Selma) — staging ground for Selma-to-Montgomery marches 1965',
        'First Baptist Church (Montgomery) — where Freedom Riders were sheltered 1961; MLK addressed crowd',
        'Bethel Baptist Church (Birmingham) — Rev. Fred Shuttlesworth\'s church; bombed three times',
        'Tabernacle Baptist Church (Selma) — Bloody Sunday organizing',
        'First Baptist Church of Africatown (Mobile) — founded by Clotilda survivors',
    ],
    'California': [
        'First AME Church of Los Angeles — oldest Black church in LA (1872); civil rights organizing center',
        'Allen Temple Baptist Church (Oakland) — community organizing hub; Black Panther connections',
        'Third Baptist Church (San Francisco) — Fillmore District; longest-standing Black institution in the city',
        'Masjid Al-Islam (Los Angeles) — W.D. Mohammed community mosque',
    ],
    'Connecticut': [
        'Dixwell Avenue Congregational Church (New Haven) — one of oldest Black congregations in Connecticut',
    ],
    'District of Columbia': [
        'Metropolitan AME Church — "National Cathedral of African Methodism"; Frederick Douglass\'s funeral held here 1895; Rosa Parks lay in state 2005',
        'Shiloh Baptist Church — founded 1863 by freed slaves; Jessie Jackson\'s church base for DC operations',
        'Nineteenth Street Baptist Church — oldest Black Baptist church in DC (1839)',
        'Vermont Avenue Baptist Church — historically significant congregation',
        'Masjid Muhammad (The Nation\'s Mosque) — the first mosque in America established for the propagation of Islam (1945, originally Temple No. 4 under Elijah Muhammad)',
        'Israel Congregation (DC area) — historically Black synagogue; serves Black Jews and Hebrew Israelites',
    ],
    'Florida': [
        'Bethel Baptist Institutional Church (Jacksonville) — civil rights organizing',
        'Mt. Zion Missionary Baptist Church (Tallahassee) — bus boycott organizing 1956',
        'St. Paul AME Church (St. Augustine) — staging ground for civil rights protests',
        'Ah-Tah-Thi-Ki spiritual sites — Seminole, including Black Seminole ceremonial practices',
    ],
    'Georgia': [
        'Ebenezer Baptist Church (Atlanta) — Martin Luther King Sr. and Jr. pastored; "the church of the movement"; National Historic Landmark',
        'Big Bethel AME Church (Atlanta) — oldest African American congregation in Atlanta (1847)',
        'First African Baptist Church (Savannah) — one of oldest Black churches in North America (1773); enslaved congregants; breathing holes in floor (Underground Railroad)',
        'First Bryan Baptist Church (Savannah) — oldest continuous Black Baptist congregation in North America (1788)',
        'Wheat Street Baptist Church (Atlanta) — Sweet Auburn; massive congregation',
        'Butler Street CME Church (Atlanta) — civil rights movement gathering',
        'Al-Farooq Masjid (Atlanta) — largest mosque in the Southeast; serves diverse African-descendant Muslim community',
    ],
    'Illinois': [
        'Pilgrim Baptist Church (Chicago) — Thomas Dorsey invented gospel music here; Mahalia Jackson sang here; original building burned 2006',
        'Quinn Chapel AME Church (Chicago) — oldest Black congregation in Chicago (1844); Underground Railroad stop',
        'Olivet Baptist Church (Chicago) — at one point the largest Protestant congregation in the world; Great Migration receiving church',
        'Trinity United Church of Christ (Chicago) — Rev. Jeremiah Wright; "unashamedly Black and unapologetically Christian"; largest UCC congregation',
        'Mosque Maryam (Chicago) — Nation of Islam international headquarters; Louis Farrakhan',
        'Muhammad Mosque No. 2 / Temple No. 2 (Chicago) — Elijah Muhammad\'s base; Nation of Islam historic site',
    ],
    'Louisiana': [
        'St. Augustine Church (New Orleans/Tremé) — free people of color purchased pews for enslaved people; Tomb of the Unknown Slave; one of oldest Black Catholic parishes in US',
        'First African Baptist Church (New Orleans)',
        'Tremé\'s historic churches and spiritual houses — including voodoo/vodou temples and spiritual churches',
        'Greater St. Stephen Full Gospel Baptist Church (New Orleans) — mega-church; Bishop Paul Morton',
        'Masjid Al-Islam (New Orleans) — significant Black Muslim community presence',
    ],
    'Maryland': [
        'Sharp Street Memorial United Methodist Church (Baltimore) — oldest Black Methodist church in Baltimore (1787)',
        'Bethel AME Church (Baltimore) — Frederick Douglass worshipped here',
        'Orchard Street United Methodist Church (Baltimore) — Underground Railroad stop',
    ],
    'Massachusetts': [
        'African Meeting House (Boston) — oldest standing Black church building in US (1806); "Black Faneuil Hall"; William Lloyd Garrison founded Anti-Slavery Society here',
    ],
    'Michigan': [
        'New Bethel Baptist Church (Detroit) — Rev. C.L. Franklin (Aretha\'s father) pastored; Aretha sang gospel here as a child',
        'Second Baptist Church (Detroit) — final stop on Underground Railroad to Canada (1836)',
        'Hartford Memorial Baptist Church (Detroit) — Rev. Charles Adams; major civil rights congregation',
        'Masjid Wali Muhammad (Detroit) — one of oldest continuously operating mosques in the US; W.D. Mohammed community',
    ],
    'Mississippi': [
        'Mt. Zion United Methodist Church (Longdale, Neshoba County) — burned by KKK June 1964; the event that drew Chaney, Goodman, and Schwerner to investigate',
        'First Baptist Church (Meridian) — Chaney\'s funeral drew thousands',
        'Vernon Dahmer\'s church (Hattiesburg area) — Dahmer killed by KKK firebomb 1966 for offering to pay poll taxes',
    ],
    'Missouri': [
        'Antioch Baptist Church (St. Louis) — civil rights organizing center',
    ],
    'New York': [
        'Abyssinian Baptist Church (Harlem) — founded 1808; Adam Clayton Powell Jr. pastored; one of oldest Black congregations in the US; 4,000+ members',
        'Mother AME Zion Church (Harlem) — "Freedom Church"; Harriet Tubman, Frederick Douglass, Sojourner Truth attended; founded 1796',
        'Canaan Baptist Church of Christ (Harlem) — Wyatt Tee Walker pastored',
        'Bethel Gospel Assembly (Harlem)',
        'Masjid Malcolm Shabazz (Harlem) — formerly Muhammad\'s Mosque No. 7 (Malcolm X\'s mosque); renamed in his honor',
        'Convent Avenue Baptist Church (Harlem)',
        'Concord Baptist Church of Christ (Brooklyn) — one of largest Black congregations in the US',
        'Congregation Beth Elohim (Brooklyn) — historic Jewish congregation; Beth Shalom B\'nai Zaken Ethiopian Hebrew Congregation in Chicago is one of the historically Black synagogues',
    ],
    'North Carolina': [
        'White Rock Baptist Church (Durham) — organizing hub for Hayti community and civil rights',
    ],
    'Ohio': [
        'Antioch Baptist Church (Cleveland) — Great Migration receiving church',
    ],
    'Oklahoma': [
        'Vernon AME Church (Tulsa) — one of few surviving structures from 1921 Tulsa Race Massacre; basement used as refuge during massacre',
        'First Baptist Church (North Tulsa) — Greenwood community church',
    ],
    'Pennsylvania': [
        'Mother Bethel AME Church (Philadelphia) — founded 1794 by Richard Allen; birthplace of the African Methodist Episcopal denomination; oldest AME property in the world; Underground Railroad site',
        'First African Presbyterian Church (Philadelphia) — founded 1807',
        'Church of the Advocate (Philadelphia) — site of Black Power conference and Philadelphia\'s civil rights organizing',
    ],
    'South Carolina': [
        'Emanuel AME Church (Charleston) — "Mother Emanuel"; founded 1816 by Morris Brown; Denmark Vesey planned revolt here 1822; 2015 massacre by white supremacist killed 9; National Historic Landmark',
        'Brick Baptist Church (St. Helena Island) — oldest surviving church built by enslaved persons (1855)',
        'Morris Brown AME Church (Charleston) — connected to Emanuel history',
        'Oyotunji African Village / Ile Ife (Sheldon, Beaufort County) — see AFRICAN_SPIRITUAL_CULTURAL_SITES below',
    ],
    'Tennessee': [
        'Mason Temple (Memphis) — Church of God in Christ international headquarters; MLK delivered "I\'ve Been to the Mountaintop" speech here April 3, 1968 (night before assassination)',
        'First Baptist Church (Nashville) — Freedom Riders refuge 1961',
        'Clark Memorial United Methodist Church (Nashville) — sit-in movement organizing',
        'Al-Farooq Mosque (Nashville) — serving growing African Muslim community',
    ],
    'Texas': [
        'Wheeler Avenue Baptist Church (Houston) — one of largest Black congregations in Texas',
        'Antioch Missionary Baptist Church (Houston) — oldest Black church in Houston (1866)',
        'Mosque No. 45 / Masjid Warithud-Deen Muhammad (Houston) — Black Muslim community center',
    ],
    'Virginia': [
        'First Baptist Church (Williamsburg) — one of oldest Black churches in America; founded 1776 by enslaved persons',
        'Ebenezer Baptist Church (Richmond) — historic Black church in Jackson Ward',
        'First African Baptist Church (Richmond) — Robert Ryland pastored; congregation included enslaved people',
    ],
    'US Virgin Islands': [
        'Frederick Lutheran Church (Charlotte Amalie, St. Thomas) — enslaved and free Black congregants',
        'Lord God of Sabaoth Lutheran Church (Frederiksted, St. Croix) — connected to emancipation history',
    ],
}

# Additional historically Black synagogues, temples, and unique spiritual sites
HISTORIC_BLACK_SYNAGOGUES_AND_TEMPLES = [
    'Beth Shalom B\'nai Zaken Ethiopian Hebrew Congregation (Chicago) — oldest historically Black synagogue in the US; serves African American Hebrew Israelites since 1918',
    'Temple Beth-El (Harlem, NYC) — Black Jewish congregation',
    'Commandment Keepers Ethiopian Hebrew Congregation (Harlem, NYC) — founded 1919 by Rabbi Wentworth Arthur Matthew; Black Hebrew Israelite tradition',
    'Beth Elohim Hebrew Congregation (St. Thomas, USVI) — second oldest synagogue in the Western Hemisphere; historic connection to Caribbean Jewish communities including Sephardic Jews of African descent',
    'International Israelite Board of Rabbis (various locations) — ordaining Black rabbis since 1960s',
    'Temple of the African Hebrew Israelites (Dimona, Israel / Chicago connection) — founded by Ben Ammi Ben-Israel from Chicago',
]

# ---------------------------------------------------------------------------
# AFRICAN-DERIVED SPIRITUAL AND CULTURAL SITES
# Including Oyotunji African Village and similar sites preserving
# African spiritual traditions, cultural practices, and community life
# ---------------------------------------------------------------------------

AFRICAN_SPIRITUAL_CULTURAL_SITES = [
    # Major sites
    'Oyotunji African Village / Ile Ife (Sheldon, Beaufort County, SC) — founded 1970 by Oba Ofuntola Oseijeman Adelabu Adefunmi I (born Walter Eugene King in Detroit); only Yoruba village in North America; practicing Yoruba/Orisha spiritual tradition; maintains Oba (king), Ogun shrine, Oshun shrine, Shango shrine, and Obatala temple; community of 50+; National Register nominee; represents the most complete reconstruction of West African village life and governance in the Americas',
    'Voodoo Spiritual Temple (New Orleans, LA) — founded by Priestess Miriam Chamani; practicing Voodoo/Vodou; open to public; one of few functioning temples',
    'Island of Salvation Botanica (New Orleans, LA) — Sallie Ann Glassman\'s Haitian Vodou peristyle and community center',
    'Congo Square / Louis Armstrong Park (New Orleans, LA) — where enslaved Africans gathered on Sundays to drum, dance, and maintain cultural traditions; birthplace of American musical culture; sacred ground',
    'Hoodoo Heritage sites (various, especially Mississippi, Alabama, South Carolina) — locations associated with rootwork, conjure, and herbal medicine traditions blending African, Indigenous, and European knowledge systems',
    'African American Islam historic sites — including Muhammad\'s Temple No. 2 (Chicago), Mosque Maryam (Chicago), Masjid Malcolm Shabazz (Harlem), Masjid Muhammad (DC)',
    'Gullah/Geechee praise house tradition sites (Sea Islands, SC/GA) — small wooden buildings for prayer meetings and ring shout; some still standing on St. Helena Island, Sapelo Island',
    'Ile Ase (Brooklyn, NY) — Yoruba/Lucumí/Orisha spiritual house',
    'Church of Lukumi Babalu Aye (Hialeah, FL) — won Supreme Court case (1993) establishing animal sacrifice as protected religious practice; Santería/Lukumí',
    'Canopied/bottle tree tradition sites (throughout the South) — blue bottles hung on trees to ward off evil spirits; Kongo/BaKongo cosmological tradition; visible in rural Mississippi, Alabama, South Carolina, Virginia',
    'African American Buddhist communities — Soka Gakkai International (various), East Bay Meditation Center (Oakland, CA), Spirit Rock (Marin, CA) with Black sangha',

    # Cemeteries and burial grounds of spiritual significance
    'African Burial Ground National Monument (NYC) — 15,000+ enslaved and free Africans buried 1690s–1790s; some buried with African spiritual objects; most important urban archaeological site in US history',
    'Geer Cemetery (Durham, NC) — historically Black cemetery with grave decorations reflecting African spiritual traditions',
    'Holt Cemetery (New Orleans, LA) — historically Black "poor" cemetery; Buddy Bolden buried here; unique in-ground graves that families maintain with personal objects (West African tradition)',
    'God\'s Little Acre / Newport Common Burying Ground (Newport, RI) — largest collection of colonial-era African gravestones; carved imagery shows African symbolic traditions',
    'Freedmen\'s Cemetery National Monument (Alexandria, VA) — over 1,800 formerly enslaved people buried during Civil War',

    # Cultural/living history sites
    'Penn Center (St. Helena Island, SC) — first school for formerly enslaved people (1862); Gullah/Geechee cultural preservation center; MLK retreat; National Historic Landmark',
    'Mitchelville Freedom Park (Hilton Head, SC) — site of first self-governed town of formerly enslaved people in US (1862)',
    'Kingsley Plantation (Fort George Island, FL, NPS) — tabby slave quarters; Anna Madgigine Jai (Wolof woman from Senegal) ran the plantation',
    'Fort Mose Historic State Park (St. Augustine, FL) — first legally sanctioned free Black settlement in North America (1738)',
    'Whitney Plantation (Wallace/Edgard, LA) — the only plantation museum focused entirely on the enslaved experience',
    'The National Great Blacks in Wax Museum (Baltimore, MD) — Black history through life-size wax figures',
    'DuSable Museum of African American History (Chicago, IL) — first independent museum of Black history in the US (1961)',
    'Africa Town/Africatown (Mobile, AL) — community founded by survivors of the Clotilda, last known slave ship (1860)',
]

# States and major cities with largest African-descendant populations
# Used for geographic validation: if an entry mentions these places, it should
# address African-descendant impact
AFRICAN_DESCENDANT_POPULATION_CENTERS = {
    # By total population (top 20 metro areas)
    'New York City': ['Harlem', 'Bedford-Stuyvesant', 'Crown Heights', 'South Bronx', 'Jamaica Queens'],
    'Chicago': ['South Side', 'Bronzeville', 'West Side', 'Austin', 'Englewood'],
    'Atlanta': ['Sweet Auburn', 'West End', 'Cascade Heights', 'Bankhead', 'College Park'],
    'Houston': ['Third Ward', 'Fifth Ward', 'Sunnyside', 'Acres Homes'],
    'Washington DC': ['Anacostia', 'Shaw', 'Ward 7', 'Ward 8', 'Petworth'],
    'Philadelphia': ['North Philadelphia', 'West Philadelphia', 'Germantown'],
    'Dallas': ['South Dallas', 'Oak Cliff', 'Cedar Crest'],
    'Detroit': ['East Side', 'West Side', 'Palmer Park', 'Conant Gardens'],
    'Memphis': ['Orange Mound', 'South Memphis', 'Whitehaven', 'Beale Street'],
    'Baltimore': ['West Baltimore', 'East Baltimore', 'Cherry Hill', 'Park Heights'],
    'Miami': ['Liberty City', 'Overtown', 'Little Haiti', 'Opa-Locka'],
    'Los Angeles': ['South LA', 'Watts', 'Compton', 'Inglewood', 'Leimert Park', 'Crenshaw'],
    'New Orleans': ['Tremé', '7th Ward', '9th Ward', 'Central City', 'Algiers'],
    'Jacksonville': ['LaVilla', 'Eastside', 'New Town', 'Arlington'],
    'Charlotte': ['West End', 'Biddleville', 'Hidden Valley'],
    'Cleveland': ['Hough', 'Glenville', 'Mount Pleasant'],
    'St. Louis': ['The Ville', 'North City', 'Ferguson'],
    'Oakland': ['West Oakland', 'East Oakland', 'Fruitvale'],
    'Birmingham': ['4th Avenue District', 'Ensley', 'Smithfield', 'Titusville'],
    'Richmond': ['Jackson Ward', 'Church Hill', 'Highland Park'],
    # By percentage (states over 25%)
    'Mississippi': 'Highest percentage nationally (38.0%)',
    'Louisiana': '33.1%',
    'Georgia': '33.0%',
    'Maryland': '31.1%',
    'South Carolina': '27.0%',
    'Alabama': '26.8%',
    'North Carolina': '22.2%',
    'Delaware': '23.2%',
    'Virginia': '20.0%',
    'Tennessee': '17.1%',
    'Florida': '16.9%',
    'New York State': '17.6%',
    'Arkansas': '15.7%',
    'Illinois': '14.6%',
}

# Keywords that signal an entry involves African-descendant cultural resources
AFRICAN_DESCENDANT_SIGNAL_KEYWORDS = [
    'African American', 'Black', 'African-descendant', 'African descendant',
    'enslaved', 'slavery', 'plantation', 'HBCU', 'historically Black',
    'civil rights', 'Reconstruction', 'Jim Crow', 'segregation', 'desegregation',
    'lynching', 'redlining', 'Great Migration', 'Freedmen', 'freedpeople',
    'Underground Railroad', 'abolitionist', 'emancipation', 'Juneteenth',
    'Gullah', 'Geechee', 'Creole', 'Haitian', 'diaspora',
    'NAACP', 'SCLC', 'SNCC', 'Urban League', 'Black Panther',
    'Negro', 'colored', 'race riot', 'race massacre', 'racial violence',
    'Black church', 'AME', 'Baptist', 'gospel', 'spirituals',
    'blues', 'jazz', 'hip-hop', 'soul', 'R&B', 'Motown',
    'Harlem', 'Bronzeville', 'Tremé', 'Greenwood',
    'DEI', 'diversity', 'equity', 'affirmative action',
    'environmental justice', 'Cancer Alley', 'food desert',
    'mass incarceration', 'police', 'voting rights',
    'reparations', 'racial wealth gap',
    'Africa', 'West African', 'East African', 'Caribbean',
    'Nigerian', 'Ethiopian', 'Somali', 'Haitian', 'Jamaican',
    'Trinidadian', 'Cape Verdean', 'Ghanaian', 'Eritrean',
]

# Critical cultural practices and concepts for African-descendant communities
AFRICAN_DESCENDANT_CULTURAL_CONCEPTS = {
    'music_traditions': [
        'Blues (Delta, Piedmont, Chicago, Texas, West Coast) — direct lineage from West African griot tradition through field hollers and work songs',
        'Jazz (New Orleans, swing, bebop, cool, free, fusion) — born from convergence of African rhythmic traditions, blues, and European harmony',
        'Gospel — sacred music tradition from Black church; Thomas Dorsey, Mahalia Jackson; fusion of blues feeling with Christian hymns',
        'Hip-hop (East Coast, West Coast, South, Midwest) — DJ Kool Herc in South Bronx 1973; griot tradition through toasting, signifying, and dozens',
        'R&B/Soul (Motown, Stax, Philly, funk) — secular expression of gospel; Ray Charles, James Brown, Aretha Franklin',
        'Go-go (DC) — Chuck Brown, percussion-heavy groove with call-and-response',
        'Zydeco (Louisiana) — Creole music: French songs + African rhythms + blues + R&B; accordion and frottoir',
        'Quelbe/scratch (USVI) — African drumming + European fiddle',
        'Bomba and Plena (Puerto Rico) — Afro-Puerto Rican percussion and dance',
        'Spirituals/Negro spirituals — encoded freedom messages, West African call-and-response; Fisk Jubilee Singers preserved',
        'Work songs and field hollers — direct African musical survival through enslavement',
    ],
    'foodways': [
        'Soul food — West African culinary foundations: okra (ki ngombo/gumbo), black-eyed peas (cowpeas from West Africa), yams, rice, collard greens, cornbread; seasoning traditions',
        'Gullah/Geechee foodways — red rice (Jollof lineage), hoppin\' John, shrimp and grits; Senegambian/Sierra Leonean origins',
        'Creole cuisine — gumbo, jambalaya, étouffée; synthesis of West African, French, Spanish, Indigenous techniques',
        'Barbecue — African and Caribbean smoking/grilling techniques (barbacoa from Taíno via African adaptation); pitmaster tradition',
        'Haitian cuisine — griot (fried pork), diri ak djon djon (black mushroom rice), akra (fritters from Yoruba akara)',
        'Ethiopian/Eritrean cuisine — injera, wot, coffee ceremony (jebena buna); maintained in diaspora',
        'Afro-Puerto Rican cuisine — mofongo (from West African fufu), pasteles, gandules',
    ],
    'spiritual_traditions': [
        'Black church tradition — AME, Baptist, COGIC, Pentecostal; call-and-response preaching; the Black church as political, social, and spiritual institution',
        'Haitian Vodou — spiritual system from Dahomey/Benin; lwa (spirits), ceremonies, peristyle; foundation of Haitian Revolution',
        'New Orleans Voodoo/Vodou — syncretic tradition; Marie Laveau; distinct from Hollywood caricature',
        'Santería/Lucumí — Yoruba-derived tradition maintained in Cuban and Puerto Rican diaspora',
        'Hoodoo/rootwork/conjure — folk spiritual practice blending African, Indigenous, and European herbal and spiritual knowledge; distinct from Vodou',
        'Ring shout — counterclockwise circular worship with West/Central African roots; preserved in Georgia Sea Islands',
        'Espiritismo — Puerto Rican and Caribbean syncretic practice with African and Taíno elements',
        'Candomblé connections — Afro-Brazilian tradition with shared Yoruba roots to US practices',
    ],
    'material_culture': [
        'Sweetgrass basketry — Gullah/Geechee coiled basket tradition from Sierra Leone/Senegambia; 300+ year continuity',
        'Quilting traditions — Gee\'s Bend (Alabama), strip quilting, improvisational design with West African textile aesthetics',
        'Shotgun house architecture — one-room-wide house form from Yoruba/Haitian architectural tradition',
        'Ironwork/blacksmithing — West African metalworking traditions visible in New Orleans, Charleston wrought iron',
        'Pottery — Edgefield pottery tradition (South Carolina), Dave the Potter/David Drake; enslaved potter who inscribed poems on vessels',
        'Mardi Gras Indian suits — hand-beaded ceremonial regalia weighing 100+ pounds; 200+ year tradition',
        'Vejigante masks (Puerto Rico) — coconut shell masks from Loíza; African-derived masquerade',
        'Kente cloth adaptations — adopted as pan-African cultural symbol in US diaspora',
    ],
    'oral_and_literary_traditions': [
        'Signifying/the dozens — verbal art form of indirect meaning, wordplay, and ritual insult; West African lineage',
        'Call-and-response — pervasive African-derived communication pattern in preaching, music, and daily life',
        'Anansi/Br\'er Rabbit trickster tales — Akan/Ashanti spider stories transformed in diaspora; Joel Chandler Harris appropriated them',
        'Griots/jali tradition — West African hereditary oral historians/musicians; lineage to blues, hip-hop MCs',
        'Slave narratives — Frederick Douglass, Harriet Jacobs, Solomon Northup; foundational American literature',
        'Harlem Renaissance literature — Langston Hughes, Zora Neale Hurston, Claude McKay, Countee Cullen',
        'Black Arts Movement — Amiri Baraka, Sonia Sanchez, Nikki Giovanni; 1960s–70s',
    ],
    'social_institutions': [
        'HBCU tradition — 107 institutions; most significant educational infrastructure in Black America',
        'Black church as institution — political organizing, mutual aid, education, social services since slavery',
        'Black Greek-letter organizations (Divine Nine) — Alpha Phi Alpha (1906) through Iota Phi Theta (1963); stepping tradition',
        'Mutual aid/benevolent societies — burial societies, Social Aid and Pleasure Clubs (New Orleans); West African tontine lineage',
        'Black fraternal orders — Prince Hall Freemasonry (1775, oldest), Elks, Knights of Pythias',
        'Juneteenth — oldest nationally celebrated African American holiday; federal holiday since 2021',
        'Kwanzaa — pan-African holiday created by Maulana Karenga (1966); seven principles (Nguzo Saba)',
        'Black History Month — Carter G. Woodson established Negro History Week 1926; expanded to month 1976',
        'Homecoming traditions — HBCU homecomings as cultural reunions; also church homecoming in rural South',
        'Watch Night/Freedom\'s Eve — New Year\'s Eve service commemorating Emancipation Proclamation (Jan 1, 1863)',
    ],
}

# Flattened index of geographic keywords → African-descendant communities
GEOGRAPHIC_AFRICAN_DESCENDANT_INDEX = {}
for _jurisdiction, _data in AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION.items():
    _communities = _data.get('communities', [])
    _afro_indigenous = _data.get('afro_indigenous', [])
    if _communities or _afro_indigenous:
        GEOGRAPHIC_AFRICAN_DESCENDANT_INDEX[_jurisdiction] = {
            'communities': _communities,
            'afro_indigenous': _afro_indigenous,
            'resources': _data.get('cultural_resources', []),
            'practices': _data.get('cultural_practices', []),
        }


class TrackerUpdate:
    # Canonical community names — map legacy/variant labels to the standardized form
    COMMUNITY_NAME_MAP = {
        'African American': 'African-descendant Communities',
        'African': 'African-descendant Communities',
        'African Descendant': 'African-descendant Communities',
        'Black': 'African-descendant Communities',
        'Afro-Caribbean': 'African-descendant Communities',
        'Afro-Latino': 'African-descendant Communities',
        'Afro-Latina': 'African-descendant Communities',
        'African descent': 'African-descendant Communities',
        'HBCU Communities': 'African-descendant Communities',
        # Other common normalizations
        'Latine': 'Latiné',
        'Latino': 'Latiné',
        'Latina': 'Latiné',
        'Hispanic': 'Latiné',
        'Latinx': 'Latiné',
        'Latino/Latina': 'Latiné',
        'LGBTQ+': 'LGBTQIA2S+',
        'LGBTQI+': 'LGBTQIA2S+',
        'LGBTQ': 'LGBTQIA2S+',
        'LGBT': 'LGBTQIA2S+',
        'Native American': 'Indigenous/Tribal',
        'Tribal': 'Indigenous/Tribal',
        'Indigenous': 'Indigenous/Tribal',
        'Low-income': 'Low-income Communities',
        'Low income': 'Low-income Communities',
        'Rural': 'Rural Communities',
        'Immigrant': 'Immigrant Communities',
        'Disabled': 'Disabled Community',
        'Environmental Justice': 'Environmental Justice Communities',
        'Environmental justice': 'Environmental Justice Communities',
        'Arts': 'Arts Community',
        'Artists': 'Arts Community',
        'Nonprofit': 'Nonprofit(s)',
        'Nonprofits': 'Nonprofit(s)',
    }

    # Map legacy impact-analysis keys to the canonical key names
    IMPACT_KEY_MAP = {
        'africanAmerican': 'africanDescendant',
        'black': 'africanDescendant',
        'african': 'africanDescendant',
        'Indigenous/Tribal': 'indigenous',
        'indigenousTribal': 'indigenous',
        'All communities': 'allCommunities',
        'All Communities': 'allCommunities',
        'Asian American': 'asianAmerican',
        'Latiné': 'latine',
        'latiné': 'latine',
        'Women': 'women',
        'Immigrant': 'immigrant',
        'Indigenous': 'indigenous',
        'Native Hawaiian': 'nativeHawaiian',
        'Pacific Islander/Oceania': 'pacificIslanderOceania',
        'Nonprofit(s)': 'nonprofit',
        'Arts community': 'artsCommunity',
    }

    # Title color coding by threat level
    THREAT_LEVEL_COLORS = {
        'SEVERE': '#991B1B',
        'HARMFUL': '#CA8A04',
        'PROTECTIVE': '#065F46',
        'WATCH': '#1D4ED8',
    }

    # Required PPPT sub-keys for each impact community block
    PPPT_KEYS = ('people', 'places', 'practices', 'treasures')

    def __init__(self, auto_mode=False, dry_run=False):
        self.auto_mode = auto_mode
        self.dry_run = dry_run
        self.new_entries = []
        self.log = []
        os.chdir(str(TRACKER_DIR))
        
    def log_msg(self, msg: str, level: str = "INFO"):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"[{timestamp}] {level}: {msg}"
        self.log.append(formatted)
        if not self.dry_run or level in ["ERROR", "WARNING"]:
            print(formatted)
    
    def run_git_command(self, cmd: List[str]) -> tuple[int, str, str]:
        """Execute git command and return exit code, stdout, stderr"""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(TRACKER_DIR)
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            self.log_msg(f"Git command timed out: {' '.join(cmd)}", "ERROR")
            return -1, "", "Timeout"
        except Exception as e:
            self.log_msg(f"Git command failed: {str(e)}", "ERROR")
            return -1, "", str(e)
    
    def load_data(self) -> Dict:
        """Load current tracker data"""
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.log_msg(f"Failed to load data.json: {str(e)}", "ERROR")
            return None
    
    def load_state(self) -> Dict:
        """Load current pipeline state"""
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.log_msg(f"Failed to load state.json: {str(e)}", "ERROR")
            return None
    
    def save_data(self, data: Dict) -> bool:
        """Save tracker data"""
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.log_msg(f"Saved data.json ({sum(len(v) for v in data.values() if isinstance(v, list))} total entries)")
            return True
        except Exception as e:
            self.log_msg(f"Failed to save data.json: {str(e)}", "ERROR")
            return False
    
    def save_state(self, state: Dict) -> bool:
        """Save pipeline state"""
        try:
            with open(STATE_FILE, 'w') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            self.log_msg("Updated state.json")
            return True
        except Exception as e:
            self.log_msg(f"Failed to save state.json: {str(e)}", "ERROR")
            return False
    
    def check_git_status(self) -> bool:
        """Check if repository is in clean state"""
        code, stdout, stderr = self.run_git_command(['git', 'status', '--porcelain'])
        if code != 0:
            self.log_msg("Failed to check git status", "ERROR")
            return False
        
        # Filter out untracked files we expect
        ignored_patterns = ['.claude/', 'Archive/', 'README.md', 'research_', 'tckc-tracker.html', 'word_count']
        status_lines = [line for line in stdout.strip().split('\n') if line and not any(p in line for p in ignored_patterns)]
        
        if status_lines:
            self.log_msg(f"Repository has uncommitted changes:\n{chr(10).join(status_lines)}", "WARNING")
            if not self.auto_mode:
                response = input("Continue anyway? (y/n): ").strip().lower()
                return response == 'y'
            return False
        
        return True
    
    def fetch_from_github(self) -> bool:
        """Fetch latest from origin/main"""
        self.log_msg("Fetching latest from GitHub...")
        code, stdout, stderr = self.run_git_command(['git', 'fetch', 'origin', 'main'])
        if code != 0:
            self.log_msg(f"Failed to fetch: {stderr}", "ERROR")
            return False
        self.log_msg("Fetched successfully")
        return True
    
    def check_for_new_entries(self) -> bool:
        """Check if new entries exist to integrate"""
        entries_file = TRACKER_DIR / "NEW_ENTRIES_APRIL_2026.json"
        if not entries_file.exists():
            self.log_msg("No NEW_ENTRIES file found. Skipping entry integration.", "WARNING")
            return False
        
        try:
            with open(entries_file, 'r') as f:
                entries = json.load(f)
            
            total = sum(len(v) if isinstance(v, list) else 0 for v in entries.values())
            self.log_msg(f"Found {total} entries in NEW_ENTRIES file")
            self.new_entries = entries
            return total > 0
        except Exception as e:
            self.log_msg(f"Failed to load new entries: {str(e)}", "ERROR")
            return False
    
    def normalize_community_names(self, communities: list) -> list:
        """Normalize community names to canonical labels, deduplicating."""
        seen = set()
        normalized = []
        for c in communities:
            mapped = self.COMMUNITY_NAME_MAP.get(c, c)
            if mapped not in seen:
                seen.add(mapped)
                normalized.append(mapped)
        return normalized

    def normalize_impact_keys(self, impact: dict) -> dict:
        """Rename legacy impact-analysis keys and ensure PPPT sub-structure."""
        normalized = {}
        for key, value in impact.items():
            canonical = self.IMPACT_KEY_MAP.get(key, key)
            # Merge if canonical key already exists (e.g. two legacy keys map to same)
            if canonical in normalized and isinstance(value, dict):
                normalized[canonical].update(value)
            else:
                normalized[canonical] = value
            # Ensure PPPT keys exist in each community block
            if isinstance(normalized[canonical], dict):
                for pppt in self.PPPT_KEYS:
                    if pppt not in normalized[canonical]:
                        normalized[canonical][pppt] = ""
                        self.log_msg(f"  Added missing '{pppt}' to impact key '{canonical}'", "WARNING")
        return normalized

    def normalize_title_color(self, entry: dict) -> dict:
        """Ensure the T (formatted title) field has the correct color for the threat level."""
        level = entry.get('L', '')
        title_html = entry.get('T', '')
        color = self.THREAT_LEVEL_COLORS.get(level)

        if not color or not title_html:
            return entry

        # If T already has a span with a color, replace the color value
        if '<span style="color:' in title_html or "<span style='color:" in title_html:
            entry['T'] = re.sub(
                r'(<span\s+style=["\']color:\s*)#[0-9a-fA-F]{6}',
                rf'\g<1>{color}',
                title_html
            )
        else:
            # Wrap the entry type prefix with the correct color span
            entry_type = entry.get('t', '')
            if entry_type and title_html.startswith(entry_type):
                rest = title_html[len(entry_type):]
                entry['T'] = f'<span style="color: {color};">{entry_type}</span>{rest}'
            elif entry_type:
                # T doesn't start with type — wrap everything
                entry['T'] = f'<span style="color: {color};">{entry_type}:</span> {title_html}'
        return entry

    def validate_indigenous_specificity(self, entry: dict) -> list:
        """Check whether an entry that involves Indigenous cultural resources
        actually names specific tribal nations, cultural practices, places,
        and concepts rather than using only generic labels.

        Returns a list of warning strings (empty = passes validation).
        """
        warnings = []
        entry_id = entry.get('i', 'unknown')

        # Collect all searchable text from the entry
        text_parts = [
            entry.get('n', ''), entry.get('s', ''),
            entry.get('D', ''), entry.get('S', ''),
        ]
        impact = entry.get('I', {})
        for _, comm_val in impact.items():
            if isinstance(comm_val, dict):
                for pppt_val in comm_val.values():
                    if isinstance(pppt_val, str):
                        text_parts.append(pppt_val)
            elif isinstance(comm_val, str):
                text_parts.append(comm_val)
        full_text = ' '.join(text_parts)
        full_text_lower = full_text.lower()

        # 1. Does this entry involve Indigenous cultural resources?
        signal_count = sum(1 for kw in INDIGENOUS_SIGNAL_KEYWORDS
                          if kw.lower() in full_text_lower)
        if signal_count == 0:
            return []  # Not an Indigenous-relevant entry

        # 2. Does the entry have an Indigenous impact section?
        indigenous_keys = {'indigenous', 'indigenousTribal', 'alaskaNative',
                          'nativeHawaiian', 'pacificIslander', 'pacificIslanderOceania',
                          'tribalNations', 'pacificNorthwestTribes'}
        has_indigenous_impact = bool(indigenous_keys & set(impact.keys()))

        communities = entry.get('c', [])
        has_indigenous_community = any(
            c in ('Indigenous/Tribal', 'Alaska Native', 'Native Hawaiian',
                  'Pacific Islander', 'Native American', 'Indigenous',
                  'All 574 federally recognized tribes', 'Tribal nations')
            for c in communities
        )

        if not has_indigenous_impact and has_indigenous_community:
            warnings.append(
                f"[{entry_id}] Lists Indigenous community in 'c' but has no "
                f"Indigenous impact key in 'I'"
            )

        if not has_indigenous_impact:
            return warnings  # Can't check further without impact text

        # 3. Gather the Indigenous-specific impact text
        indigenous_text = ''
        for ik in indigenous_keys & set(impact.keys()):
            block = impact[ik]
            if isinstance(block, dict):
                indigenous_text += ' '.join(
                    v for v in block.values() if isinstance(v, str)
                )
        indigenous_lower = indigenous_text.lower()

        # 4. Check for at least one named tribal nation (not just generic)
        generic_only_terms = {
            'indigenous', 'tribal', 'native', 'native american',
            'tribal nations', 'tribes', 'indigenous peoples',
            'first nations', 'indian', 'indians',
        }
        # Build a set of specific nation names from the reference database
        specific_names = set()
        for _jur_data in INDIGENOUS_PEOPLES_BY_JURISDICTION.values():
            for _key in ('federally_recognized', 'state_recognized',
                        'displaced_peoples', 'indigenous_peoples',
                        'unrecognized_with_presence'):
                if _key in _jur_data:
                    for _name in _jur_data[_key]:
                        # Extract the primary name before any dash/parenthetical
                        primary = _name.split('—')[0].split('(')[0].strip()
                        # Also get alternate names from parentheticals
                        if '(' in _name:
                            alt = _name.split('(')[1].split(')')[0]
                            for a in alt.split(','):
                                a = a.strip()
                                if len(a) > 2:
                                    specific_names.add(a.lower())
                        if len(primary) > 2:
                            specific_names.add(primary.lower())
        # Remove generic terms
        specific_names -= generic_only_terms

        found_specific = False
        for name in specific_names:
            if name in indigenous_lower:
                found_specific = True
                break

        if not found_specific and len(indigenous_text) > 100:
            warnings.append(
                f"[{entry_id}] Has Indigenous impact text ({len(indigenous_text)} chars) "
                f"but names NO specific tribal nation. Add named nations from the "
                f"reference database for the relevant jurisdiction(s)."
            )

        # 5. Check for PPPT completeness in Indigenous impact sections
        for ik in indigenous_keys & set(impact.keys()):
            block = impact[ik]
            if isinstance(block, dict):
                for pppt in self.PPPT_KEYS:
                    val = block.get(pppt, '')
                    if not val or len(val.strip()) < 20:
                        warnings.append(
                            f"[{entry_id}] Impact key '{ik}' has empty or thin "
                            f"'{pppt}' field ({len(val.strip())} chars). Should name "
                            f"specific peoples, places, practices, or treasures."
                        )

        # 6. Check for geographic match — if entry text mentions a state/place,
        #    do the Indigenous peoples of that jurisdiction appear?
        for jurisdiction, peoples in GEOGRAPHIC_INDIGENOUS_INDEX.items():
            jur_lower = jurisdiction.lower()
            # Check if the jurisdiction is mentioned in the entry
            if jur_lower in full_text_lower or (
                len(jur_lower) > 3 and jur_lower in indigenous_lower
            ):
                # Check if at least one people from that jurisdiction is named
                found_local = False
                for people_entry in peoples:
                    primary = people_entry.split('—')[0].split('(')[0].strip().lower()
                    if primary in indigenous_lower:
                        found_local = True
                        break
                if not found_local and len(indigenous_text) > 200:
                    # Extract first 3 peoples for the suggestion
                    suggestions = []
                    for p in peoples[:3]:
                        suggestions.append(p.split('—')[0].split('(')[0].strip())
                    warnings.append(
                        f"[{entry_id}] Mentions '{jurisdiction}' but names none of its "
                        f"Indigenous peoples. Consider: {', '.join(suggestions)}"
                    )

        return warnings

    def validate_african_descendant_specificity(self, entry: dict) -> list:
        """Check whether an entry that involves African-descendant communities
        names specific communities, cultural resources, and practices rather
        than using only generic labels like 'African American' or 'Black.'

        Returns a list of warning strings (empty = passes validation).
        """
        warnings = []
        entry_id = entry.get('i', 'unknown')

        # Collect all searchable text
        text_parts = [entry.get('n', ''), entry.get('s', ''), entry.get('D', ''), entry.get('S', '')]
        impact = entry.get('I', {})
        for _, block in impact.items():
            if isinstance(block, dict):
                for v in block.values():
                    if isinstance(v, str):
                        text_parts.append(v)
            elif isinstance(block, str):
                text_parts.append(block)
        full_text = ' '.join(text_parts)
        full_text_lower = full_text.lower()

        # 1. Does this entry involve African-descendant communities?
        signal_count = sum(1 for kw in AFRICAN_DESCENDANT_SIGNAL_KEYWORDS
                          if kw.lower() in full_text_lower)
        if signal_count == 0:
            return []

        # 2. Does the entry have an africanDescendant impact key?
        ad_keys = {'africanDescendant', 'africanAmerican', 'african', 'black'}
        has_ad_impact = bool(ad_keys & set(impact.keys()))

        communities = entry.get('c', [])
        has_ad_community = any(
            c in ('African-descendant Communities', 'African American', 'Black',
                  'HBCU Communities', 'Afro-Caribbean', 'Afro-Latino')
            for c in communities
        )

        if not has_ad_impact and has_ad_community and signal_count >= 3:
            warnings.append(
                f"[{entry_id}] Lists African-descendant community in 'c' but has "
                f"no africanDescendant impact key in 'I'"
            )

        if not has_ad_impact:
            return warnings

        # 3. Gather the African-descendant-specific impact text
        ad_text = ''
        for ak in ad_keys & set(impact.keys()):
            block = impact[ak]
            if isinstance(block, dict):
                ad_text += ' '.join(v for v in block.values() if isinstance(v, str))
        ad_lower = ad_text.lower()

        # 4. Check for specific community/place names (not just generic "African American")
        specific_terms = {
            'harlem', 'bronzeville', 'tremé', 'treme', 'gullah', 'geechee',
            'greenwood', 'sweet auburn', 'jackson ward', 'watts', 'south la',
            'fifth ward', 'third ward', 'fillmore', 'leimert park',
            'bed-stuy', 'bedford-stuyvesant', 'anacostia', 'overtown',
            'liberty city', 'little haiti', 'eatonville', 'africatown',
            'rosewood', 'tulsa', 'durham', 'hayti',
            'orange mound', 'beale street', 'farish street',
            'hbcu', 'morehouse', 'spelman', 'howard', 'fisk', 'hampton',
            'tuskegee', 'xavier', 'lincoln university',
            'gee\'s bend', 'nicodemus', 'mound bayou',
            'naacp', 'sclc', 'sncc', 'black panther', 'urban league',
            'haitian', 'somali', 'ethiopian', 'eritrean', 'nigerian',
            'jamaican', 'trinidadian', 'cape verdean', 'ghanaian',
            'vodou', 'voodoo', 'santería', 'hoodoo',
            'blues', 'jazz', 'gospel', 'hip-hop', 'soul',
            'juneteenth', 'kwanzaa', 'ring shout', 'second line',
            'sweetgrass', 'quilting', 'bomba', 'plena',
            'underground railroad', 'trail of tears freedmen',
            'middle passage', 'clotilda',
        }

        found_specific = any(term in ad_lower for term in specific_terms)

        if not found_specific and len(ad_text) > 100:
            warnings.append(
                f"[{entry_id}] Has African-descendant impact text ({len(ad_text)} chars) "
                f"but names NO specific communities, institutions, or cultural practices. "
                f"Add named communities from the reference database."
            )

        # 5. PPPT completeness
        for ak in ad_keys & set(impact.keys()):
            block = impact[ak]
            if isinstance(block, dict):
                for pppt in self.PPPT_KEYS:
                    val = block.get(pppt, '')
                    if not val or len(val.strip()) < 20:
                        warnings.append(
                            f"[{entry_id}] Impact key '{ak}' has empty or thin "
                            f"'{pppt}' field ({len(val.strip())} chars)."
                        )

        # 6. Geographic match — if entry text mentions a state with large Black
        #    population, do the specific communities of that state appear?
        for jurisdiction, jur_info in GEOGRAPHIC_AFRICAN_DESCENDANT_INDEX.items():
            jur_lower = jurisdiction.lower()
            if jur_lower not in full_text_lower:
                continue
            if not jur_info['communities']:
                continue
            # Check if any specific community from that jurisdiction appears
            found_local = False
            for comm in jur_info['communities']:
                # Extract a searchable fragment from the community entry
                fragments = comm.split('—')[0].split('(')[0].strip().lower()
                primary = fragments.split(',')[0].strip()
                if len(primary) > 4 and primary in ad_lower:
                    found_local = True
                    break
            if not found_local and len(ad_text) > 200:
                sample = [c.split('—')[0].split('(')[0].strip()
                         for c in jur_info['communities'][:3]]
                warnings.append(
                    f"[{entry_id}] Mentions '{jurisdiction}' but names none of its "
                    f"African-descendant communities. Consider: {', '.join(sample)}"
                )

        return warnings

    def _detect_jurisdictions(self, text: str) -> list:
        """Detect US jurisdictions mentioned in text for enrichment lookups."""
        text_lower = text.lower()
        # Lightweight keyword map — covers all 50 states, DC, and territories
        _JURISDICTION_HINTS = {
            'Alabama': ['alabama', 'birmingham', 'montgomery', 'selma', 'mobile', 'huntsville', 'tuskegee'],
            'Alaska': ['alaska', 'anchorage', 'fairbanks'],
            'Arizona': ['arizona', 'phoenix', 'tucson'],
            'Arkansas': ['arkansas', 'little rock'],
            'California': ['california', 'los angeles', 'san francisco', 'oakland', 'sacramento'],
            'Colorado': ['colorado', 'denver'],
            'Connecticut': ['connecticut', 'hartford', 'new haven'],
            'Delaware': ['delaware', 'wilmington', 'dover'],
            'District of Columbia': ['washington, d.c.', 'washington dc', 'district of columbia', 'smithsonian', 'anacostia'],
            'Florida': ['florida', 'miami', 'jacksonville', 'tampa', 'orlando', 'tallahassee', 'everglades'],
            'Georgia': ['georgia', 'atlanta', 'savannah', 'augusta'],
            'Hawaii': ['hawaii', 'honolulu'],
            'Idaho': ['idaho', 'boise'],
            'Illinois': ['illinois', 'chicago', 'cahokia'],
            'Indiana': ['indiana', 'indianapolis', 'gary'],
            'Iowa': ['iowa', 'des moines'],
            'Kansas': ['kansas', 'wichita', 'topeka', 'nicodemus'],
            'Kentucky': ['kentucky', 'louisville', 'lexington'],
            'Louisiana': ['louisiana', 'new orleans', 'baton rouge', 'shreveport'],
            'Maine': ['maine', 'portland, me'],
            'Maryland': ['maryland', 'baltimore', 'annapolis'],
            'Massachusetts': ['massachusetts', 'boston', 'cambridge'],
            'Michigan': ['michigan', 'detroit', 'flint'],
            'Minnesota': ['minnesota', 'minneapolis', 'st. paul'],
            'Mississippi': ['mississippi', 'jackson, ms', 'delta', 'clarksdale', 'natchez'],
            'Missouri': ['missouri', 'st. louis', 'kansas city'],
            'Montana': ['montana'],
            'Nebraska': ['nebraska', 'omaha'],
            'Nevada': ['nevada', 'las vegas'],
            'New Hampshire': ['new hampshire'],
            'New Jersey': ['new jersey', 'newark', 'trenton'],
            'New Mexico': ['new mexico', 'albuquerque', 'santa fe'],
            'New York': ['new york', 'harlem', 'brooklyn', 'bronx', 'queens', 'manhattan'],
            'North Carolina': ['north carolina', 'charlotte', 'raleigh', 'durham', 'greensboro'],
            'North Dakota': ['north dakota', 'fargo'],
            'Ohio': ['ohio', 'cleveland', 'columbus', 'cincinnati', 'dayton'],
            'Oklahoma': ['oklahoma', 'tulsa', 'oklahoma city'],
            'Oregon': ['oregon', 'portland, or', 'portland, ore'],
            'Pennsylvania': ['pennsylvania', 'philadelphia', 'pittsburgh'],
            'Rhode Island': ['rhode island', 'providence', 'newport'],
            'South Carolina': ['south carolina', 'charleston', 'columbia, sc'],
            'South Dakota': ['south dakota', 'sioux falls'],
            'Tennessee': ['tennessee', 'memphis', 'nashville', 'knoxville'],
            'Texas': ['texas', 'houston', 'dallas', 'san antonio', 'austin, tx'],
            'Utah': ['utah', 'salt lake'],
            'Vermont': ['vermont', 'burlington'],
            'Virginia': ['virginia', 'richmond', 'norfolk', 'hampton', 'williamsburg'],
            'Washington': ['washington state', 'seattle', 'tacoma'],
            'West Virginia': ['west virginia', 'charleston, wv'],
            'Wisconsin': ['wisconsin', 'milwaukee', 'madison, wi'],
            'Wyoming': ['wyoming', 'cheyenne'],
            'Puerto Rico': ['puerto rico', 'san juan', 'ponce'],
            'US Virgin Islands': ['virgin islands', 'st. croix', 'st. thomas'],
            'Guam': ['guam'],
            'American Samoa': ['american samoa'],
        }
        found = []
        for jur, hints in _JURISDICTION_HINTS.items():
            if any(h in text_lower for h in hints):
                found.append(jur)
        return found

    def auto_enrich_indigenous(self, entry: dict, full_text: str) -> list:
        """Auto-enrich an entry with specific Indigenous peoples for detected
        jurisdictions. Returns list of enrichment actions taken."""
        actions = []
        jurisdictions = self._detect_jurisdictions(full_text)
        full_lower = full_text.lower()

        # Only enrich if entry has Indigenous signal
        signal = sum(1 for kw in INDIGENOUS_SIGNAL_KEYWORDS if kw.lower() in full_lower)
        if signal == 0:
            return actions

        impact = entry.setdefault('I', {})
        indig_key = None
        for k in ('indigenous', 'Indigenous', 'Indigenous/Tribal', 'indigenousTribal'):
            if k in impact:
                indig_key = k
                break
        if not indig_key:
            indig_key = 'indigenous'
            impact[indig_key] = {'people': '', 'places': '', 'practices': '', 'treasures': ''}

        block = impact[indig_key]
        if not isinstance(block, dict):
            block = {'people': str(block), 'places': '', 'practices': '', 'treasures': ''}
            impact[indig_key] = block
        for pppt in self.PPPT_KEYS:
            block.setdefault(pppt, '')

        existing = ' '.join(v for v in block.values() if isinstance(v, str)).lower()

        for jur in jurisdictions:
            jur_data = INDIGENOUS_PEOPLES_BY_JURISDICTION.get(jur)
            if not jur_data:
                continue
            peoples = []
            for key in ('federally_recognized', 'state_recognized', 'displaced_peoples',
                       'indigenous_peoples', 'unrecognized_with_presence'):
                peoples.extend(jur_data.get(key, []))
            names_to_add = [p.split('—')[0].split('(')[0].strip()
                           for p in peoples
                           if p.split('—')[0].split('(')[0].strip().lower() not in existing
                           and len(p.split('—')[0].split('(')[0].strip()) > 2]
            if names_to_add:
                sentence = f' Indigenous peoples of {jur} include {", ".join(names_to_add[:6])}.'
                block['people'] = (block['people'].rstrip() + sentence).strip()
                actions.append(f'Added {len(names_to_add[:6])} Indigenous peoples for {jur}')

            resources = jur_data.get('cultural_resources', [])
            resources_to_add = [r for r in resources
                               if r.split('—')[0].split('(')[0].strip().lower() not in existing]
            if resources_to_add:
                block['places'] = (block['places'].rstrip() +
                    f' Cultural resources in {jur}: {"; ".join(resources_to_add[:4])}.').strip()
                actions.append(f'Added {len(resources_to_add[:4])} Indigenous resources for {jur}')

        return actions

    def auto_enrich_african_descendant(self, entry: dict, full_text: str) -> list:
        """Auto-enrich an entry with specific African-descendant communities,
        migration routes, worship sites, HBCUs, spiritual sites, and Delta
        specificity for detected jurisdictions."""
        actions = []
        full_lower = full_text.lower()

        ad_context = any(t in full_lower for t in
                        ['african', 'black', 'enslaved', 'civil rights', 'hbcu',
                         'segregation', 'dei', 'diversity', 'negro', 'slavery'])
        if not ad_context:
            return actions

        impact = entry.setdefault('I', {})
        ad_key = None
        for k in ('africanDescendant', 'africanAmerican', 'african', 'black'):
            if k in impact:
                ad_key = k
                break
        if not ad_key:
            ad_key = 'africanDescendant'
            impact[ad_key] = {'people': '', 'places': '', 'practices': '', 'treasures': ''}

        block = impact[ad_key]
        if not isinstance(block, dict):
            block = {'people': str(block), 'places': '', 'practices': '', 'treasures': ''}
            impact[ad_key] = block
        for pppt in self.PPPT_KEYS:
            block.setdefault(pppt, '')

        existing = ' '.join(v for v in block.values() if isinstance(v, str)).lower()

        jurisdictions = self._detect_jurisdictions(full_text)

        # A. Named communities per jurisdiction
        for jur in jurisdictions:
            jur_data = AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION.get(jur)
            if not jur_data:
                continue
            communities = jur_data.get('communities', [])
            to_add = [c.split('—')[0].split('(')[0].strip().split(',')[0].strip()
                     for c in communities
                     if c.split('—')[0].split('(')[0].strip().split(',')[0].strip().lower() not in existing
                     and len(c.split('—')[0].strip()) > 3]
            if to_add:
                block['people'] = (block['people'].rstrip() +
                    f' African-descendant communities in {jur}: {"; ".join(to_add[:5])}.').strip()
                actions.append(f'Added {len(to_add[:5])} AD communities for {jur}')

        # B. Great Migration routes
        if 'great migration' in full_lower and 'illinois central railroad' not in existing:
            block['places'] = (block['places'].rstrip() +
                ' The Great Migration moved 6 million African Americans from the South via'
                ' the Illinois Central Railroad (Mississippi/Louisiana to Chicago/St. Louis),'
                ' the Pennsylvania Railroad and Atlantic Coast Line (Southeast to NYC/Philly/'
                'DC/Boston), the Louisville & Nashville Railroad (Alabama/Mississippi to'
                ' Detroit/Cleveland/Cincinnati), and Route 66/Southern Pacific (Louisiana/'
                'Texas/Oklahoma to LA/Oakland/Portland/Seattle).').strip()
            actions.append('Added Great Migration routes')

        # C. Oyotunji and African spiritual/heritage sites
        if ad_context and 'oyotunji' not in existing:
            spiritual = any(t in full_lower for t in
                          ['vodou', 'voodoo', 'yoruba', 'orisha', 'hoodoo',
                           'spiritual', 'sacred', 'ceremony', 'ring shout'])
            if spiritual:
                block['places'] = (block['places'].rstrip() +
                    ' African-derived spiritual sites: Oyotunji African Village (Sheldon, SC'
                    ' — only Yoruba village in North America); Congo Square (New Orleans);'
                    ' African Burial Ground National Monument (NYC); Church of Lukumi Babalu'
                    ' Aye (Hialeah, FL); Gullah/Geechee praise houses (Sea Islands). Heritage'
                    ' sites of origin: Goree Island/Door of No Return (Senegal), Cape Coast'
                    ' Castle and Elmina Castle (Ghana), Osun-Osogbo Sacred Grove (Nigeria).').strip()
                actions.append('Added Oyotunji and African spiritual/heritage sites')

        # D. Mississippi Delta specificity
        if ('mississippi' in full_lower or 'delta' in full_lower) and 'dockery' not in existing:
            block['places'] = (block['places'].rstrip() +
                ' Mississippi Delta landmarks: Dockery Plantation (birthplace of Delta Blues'
                ' — Charley Patton, Howlin\' Wolf); Clarksdale (crossroads, Muddy Waters);'
                ' Ruleville (Fannie Lou Hamer); Money (Emmett Till); Mound Bayou (all-Black'
                ' town, 1887); Parchman Farm (prison blues, Lomax recordings); Hill Country'
                ' Blues territory of Tate/Panola County (R.L. Burnside, Junior Kimbrough).').strip()
            actions.append('Added Delta specificity')

        # E. Historic Black places of worship
        worship_context = any(t in full_lower for t in
                            ['church', 'baptist', ' ame ', 'mosque', 'synagogue', 'worship'])
        if worship_context and 'mother bethel' not in existing:
            block['treasures'] = (block['treasures'].rstrip() +
                ' Historic Black places of worship: 16th Street Baptist Church (Birmingham);'
                ' Ebenezer Baptist Church (Atlanta — MLK); Mother Bethel AME (Philadelphia'
                ' — 1794, birthplace of AME); Emanuel AME (Charleston — "Mother Emanuel");'
                ' Abyssinian Baptist (Harlem); Mason Temple (Memphis — "Mountaintop" speech);'
                ' Masjid Muhammad (DC — first American mosque for Islam); Mosque Maryam'
                ' (Chicago — NOI HQ); Beth Shalom B\'nai Zaken (Chicago — oldest Black'
                ' synagogue).').strip()
            actions.append('Added Black places of worship')

        # F. HBCU specificity
        if ('hbcu' in full_lower or 'historically black' in full_lower) and 'morehouse' not in existing:
            block['places'] = (block['places'].rstrip() +
                ' Key HBCUs: Howard University (DC); Morehouse and Spelman (Atlanta);'
                ' Fisk University (Nashville); Tuskegee University; Hampton University;'
                ' FAMU (Tallahassee); Xavier University of Louisiana (only Black Catholic'
                ' university); Meharry Medical College; Cheyney University (oldest HBCU,'
                ' 1837); Alcorn State (oldest public HBCU); Shaw University (SNCC founded'
                ' here 1960).').strip()
            actions.append('Added HBCU specificity')

        # G. Afro-Indigenous cross-references
        has_indigenous = any(t in full_lower for t in ['indigenous', 'tribal', 'native american'])
        if has_indigenous and 'freedmen' not in existing and 'black seminole' not in existing:
            block['people'] = (block['people'].rstrip() +
                ' Afro-Indigenous communities: Freedmen of the Five Tribes (Cherokee,'
                ' Chickasaw, Choctaw, Creek, Seminole); Black Seminoles/Seminole Maroons'
                ' (allied with Seminole in three wars); Mardi Gras Indians of New Orleans'
                ' (honoring Indigenous-African relationships through beaded suits).').strip()
            actions.append('Added Afro-Indigenous cross-references')

        # H. African diaspora communities
        diaspora_context = any(t in full_lower for t in
                              ['immigration', 'immigrant', 'diaspora', 'refugee', 'deportation'])
        if diaspora_context and 'haitian' not in existing and 'somali' not in existing:
            block['people'] = (block['people'].rstrip() +
                ' African diaspora communities: Haitian (Miami, Brooklyn, Boston — Vodou,'
                ' Rara, Compas); Somali (Minneapolis, Columbus, San Diego — oral poetry);'
                ' Ethiopian/Eritrean (DC metro, LA — coffee ceremony, Ge\'ez script);'
                ' Nigerian (Houston, NYC, Chicago); Jamaican (NYC, South FL — dancehall,'
                ' reggae); Cape Verdean (New Bedford/Brockton MA — morna, coladeira).').strip()
            actions.append('Added African diaspora communities')

        return actions

    def normalize_entry(self, entry: dict) -> dict:
        """Apply all normalizations and auto-enrichments to a single entry
        before integration."""
        # 1. Community names
        if 'c' in entry and isinstance(entry['c'], list):
            entry['c'] = self.normalize_community_names(entry['c'])

        # 2. Impact analysis keys + PPPT
        if 'I' in entry and isinstance(entry['I'], dict):
            entry['I'] = self.normalize_impact_keys(entry['I'])

        # 3. Title color coding
        entry = self.normalize_title_color(entry)

        # Collect full text once for validation and enrichment
        text_parts = [entry.get('n', ''), entry.get('s', ''), entry.get('D', ''), entry.get('S', '')]
        for block in entry.get('I', {}).values():
            if isinstance(block, dict):
                for v in block.values():
                    if isinstance(v, str):
                        text_parts.append(v)
        full_text = ' '.join(text_parts)

        # 4. Indigenous specificity validation (warn)
        indigenous_warnings = self.validate_indigenous_specificity(entry)
        for w in indigenous_warnings:
            self.log_msg(w, "WARNING")

        # 5. African-descendant specificity validation (warn)
        african_warnings = self.validate_african_descendant_specificity(entry)
        for w in african_warnings:
            self.log_msg(w, "WARNING")

        # 6. Auto-enrich Indigenous content
        indig_actions = self.auto_enrich_indigenous(entry, full_text)
        for a in indig_actions:
            self.log_msg(f"  [enrich] {entry.get('i', '?')}: {a}")

        # 7. Auto-enrich African-descendant content (includes migration routes,
        #    Oyotunji/spiritual sites, Delta, worship, HBCUs, Afro-Indigenous,
        #    and diaspora)
        ad_actions = self.auto_enrich_african_descendant(entry, full_text)
        for a in ad_actions:
            self.log_msg(f"  [enrich] {entry.get('i', '?')}: {a}")

        return entry

    def integrate_new_entries(self) -> bool:
        """Normalize and integrate new entries into data.json"""
        if not self.new_entries:
            self.log_msg("No new entries to integrate")
            return True

        data = self.load_data()
        if not data:
            return False

        # Map new entries to categories
        category_map = {
            'executive_actions': 'executive_actions',
            'legislation': 'legislation',
            'litigation': 'litigation',
            'agency_actions': 'agency_actions',
            'international': 'international'
        }

        total_added = 0
        for source_cat, target_cat in category_map.items():
            if source_cat in self.new_entries:
                new = self.new_entries[source_cat]
                if isinstance(new, list):
                    # Normalize each entry before adding
                    normalized = []
                    for entry in new:
                        normalized.append(self.normalize_entry(entry))
                        self.log_msg(f"  Normalized entry: {entry.get('i', 'unknown')}")
                    data[target_cat].extend(normalized)
                    total_added += len(normalized)
                    self.log_msg(f"Added {len(normalized)} entries to {target_cat}")

        if total_added == 0:
            self.log_msg("No entries were integrated", "WARNING")
            return False

        self.log_msg(f"Integrated {total_added} total entries (all normalized)")
        if not self.save_data(data):
            return False

        # Update state.json
        state = self.load_state()
        if state:
            state['last_successful_run'] = datetime.now().strftime("%Y-%m-%d")
            state['last_run_new_entries'] = total_added
            self.save_state(state)

        return True
    
    def commit_changes(self) -> bool:
        """Commit changes to git"""
        self.log_msg("Committing changes...")
        
        # Stage data files
        code, _, stderr = self.run_git_command(['git', 'add', 'data/data.json', 'data/state.json'])
        if code != 0:
            self.log_msg(f"Failed to stage files: {stderr}", "ERROR")
            return False
        
        # Commit
        total = sum(len(v) if isinstance(v, list) else 0 for v in self.new_entries.values())
        commit_msg = f"Comprehensive update: {datetime.now().strftime('%B %d, %Y')} - Added {total} new entries across all categories"
        
        code, stdout, stderr = self.run_git_command(['git', 'commit', '-m', commit_msg])
        if code != 0:
            self.log_msg(f"Commit failed: {stderr}", "ERROR")
            return False
        
        # Extract commit hash
        lines = stdout.strip().split('\n')
        if lines:
            self.log_msg(f"Committed: {lines[0]}")
        
        return True
    
    def push_to_github(self) -> bool:
        """Push changes to GitHub"""
        self.log_msg("Pushing to GitHub...")
        
        code, stdout, stderr = self.run_git_command(['git', 'push', 'origin', 'main'])
        if code != 0:
            self.log_msg(f"Push failed: {stderr}", "WARNING")
            self.log_msg("Attempting rebase and retry...")
            
            # Try rebase approach
            code, _, stderr = self.run_git_command(['git', 'pull', '--rebase', 'origin', 'main'])
            if code != 0:
                self.log_msg(f"Rebase failed: {stderr}", "ERROR")
                return False
            
            # Retry push
            code, stdout, stderr = self.run_git_command(['git', 'push', 'origin', 'main'])
            if code != 0:
                self.log_msg(f"Push retry failed: {stderr}", "ERROR")
                return False
        
        self.log_msg("Successfully pushed to GitHub")
        return True
    
    def verify_publication(self) -> bool:
        """Verify entries are on GitHub"""
        self.log_msg("Verifying publication...")
        
        code, stdout, stderr = self.run_git_command(['git', 'log', 'origin/main', '--oneline', '-1'])
        if code != 0:
            self.log_msg("Failed to verify remote", "ERROR")
            return False
        
        self.log_msg(f"Remote HEAD: {stdout.strip()}")
        return True
    
    def run(self) -> bool:
        """Execute full update workflow"""
        self.log_msg("=== TCKC Threat Tracker Comprehensive Update ===")
        self.log_msg(f"Mode: {'AUTO' if self.auto_mode else 'INTERACTIVE'} | Dry-run: {self.dry_run}")
        
        # Phase 1: Git sync
        if not self.check_git_status():
            return False
        
        if not self.fetch_from_github():
            return False
        
        # Phase 2: Check for new entries
        if not self.check_for_new_entries():
            self.log_msg("No new entries to process. Exiting.")
            return True
        
        # Phase 3: Integrate
        if not self.integrate_new_entries():
            return False
        
        # Phase 4: Commit & Push
        if self.dry_run:
            self.log_msg("DRY RUN: Skipping commit and push")
            return True
        
        if not self.commit_changes():
            return False
        
        if not self.push_to_github():
            return False
        
        # Phase 5: Verify
        if not self.verify_publication():
            self.log_msg("Publication verification failed", "WARNING")
        
        self.log_msg("=== Update Complete ===")
        return True
    
    def save_log(self):
        """Save execution log to file"""
        log_file = TRACKER_DIR / f"update_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(log_file, 'w') as f:
                f.write('\n'.join(self.log))
            self.log_msg(f"Log saved to {log_file.name}")
        except Exception as e:
            print(f"Failed to save log: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='TCKC Threat Tracker - Comprehensive Update Automation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python comprehensive_update.py              # Interactive mode
  python comprehensive_update.py --auto       # Fully automated
  python comprehensive_update.py --dry-run    # Preview without commit
        '''
    )
    
    parser.add_argument('--auto', action='store_true', 
                       help='Fully automated mode (no prompts)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview changes without committing')
    
    args = parser.parse_args()
    
    updater = TrackerUpdate(auto_mode=args.auto, dry_run=args.dry_run)
    success = updater.run()
    updater.save_log()
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
