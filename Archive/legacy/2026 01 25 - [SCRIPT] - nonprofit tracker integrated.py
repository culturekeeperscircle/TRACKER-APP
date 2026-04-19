#!/usr/bin/env python3
"""
TCKC Nonprofit Organization Threat Tracker - Integrated Edition
================================================================
Fully integrated with the TCKC Federal Litigation Threat Tracker.
Tracks executive, legislative, and agency actions targeting nonprofit organizations,
with linkages to the main cultural resources tracker and community impacts.

Integration Features:
- Links to main tracker entry IDs
- Cultural community impact tracking using 4Ps framework
- Evidence level classification
- Relationship mapping between actions and targets
- Cross-reference to international obligations
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path

# Database path - same directory as main tracker
DB_PATH = Path(__file__).parent / 'nonprofit_tracker.db'

def init_db():
    """Initialize the integrated nonprofit tracker database with enhanced schema."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute('PRAGMA foreign_keys = ON')

    # =========================================================================
    # 1. ACTIONS TABLE - Executive/Legislative/Agency Actions
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_id TEXT UNIQUE NOT NULL,          -- Links to main tracker (e.g., "eo-14151")
            title TEXT NOT NULL,
            short_title TEXT,
            date TEXT,
            doc_type TEXT,                           -- EO, Memo, Bill, Letter, Proclamation, Agency Action
            administration TEXT,                     -- Trump I, Biden, Trump II
            agencies TEXT,                           -- JSON array of agencies
            status TEXT,
            threat_level TEXT,                       -- SEVERE, HARMFUL, WATCH, PROTECTIVE
            description TEXT,
            source_url TEXT,
            federal_register_citation TEXT,
            main_tracker_ref TEXT,                   -- Reference to main tracker entry ID
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # =========================================================================
    # 2. TARGETS TABLE - Specifically Targeted Organizations
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS targets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_name TEXT NOT NULL,
            entity_type TEXT,                        -- University, Foundation, Nonprofit, Media, Museum, Library
            tax_status TEXT,                         -- 501(c)(3), 501(c)(4), State Entity, etc.
            headquarters TEXT,
            threat_nature TEXT,
            threat_level TEXT,                       -- SEVERE, HARMFUL, WATCH
            official_source TEXT,                    -- Who made the threat
            evidence_level TEXT,                     -- Official Document, Reported Internal Directive, Public Statement, Political Rhetoric
            evidence_description TEXT,
            date_first_targeted TEXT,
            current_status TEXT,                     -- Active Threat, Implemented, Litigation Pending, Resolved
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # =========================================================================
    # 3. ACTION_TARGETS - Many-to-Many Relationship
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS action_targets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_id INTEGER NOT NULL,
            target_id INTEGER NOT NULL,
            relationship_type TEXT,                  -- Direct Target, Collateral Impact, Class Member
            impact_description TEXT,
            FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE CASCADE,
            FOREIGN KEY (target_id) REFERENCES targets(id) ON DELETE CASCADE,
            UNIQUE(action_id, target_id)
        )
    ''')

    # =========================================================================
    # 4. CULTURAL COMMUNITIES TABLE
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cultural_communities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            community_code TEXT UNIQUE NOT NULL,     -- e.g., "africanDescendant", "indigenous"
            community_name TEXT NOT NULL,
            description TEXT
        )
    ''')

    # =========================================================================
    # 5. ACTION_COMMUNITY_IMPACTS - 4Ps Cultural Impact Framework
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS action_community_impacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_id INTEGER NOT NULL,
            community_id INTEGER NOT NULL,
            people_severity TEXT,                    -- SEVERE, HARMFUL, WATCH, PROTECTIVE
            people_description TEXT,
            places_severity TEXT,
            places_description TEXT,
            practices_severity TEXT,
            practices_description TEXT,
            treasures_severity TEXT,
            treasures_description TEXT,
            overall_severity TEXT,
            FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE CASCADE,
            FOREIGN KEY (community_id) REFERENCES cultural_communities(id) ON DELETE CASCADE,
            UNIQUE(action_id, community_id)
        )
    ''')

    # =========================================================================
    # 6. TARGET_COMMUNITY_IMPACTS
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS target_community_impacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target_id INTEGER NOT NULL,
            community_id INTEGER NOT NULL,
            impact_description TEXT,
            services_affected TEXT,                  -- JSON array of services
            FOREIGN KEY (target_id) REFERENCES targets(id) ON DELETE CASCADE,
            FOREIGN KEY (community_id) REFERENCES cultural_communities(id) ON DELETE CASCADE,
            UNIQUE(target_id, community_id)
        )
    ''')

    # =========================================================================
    # 7. MAIN_TRACKER_LINKS - Cross-references to main tracker
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main_tracker_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nonprofit_action_id INTEGER,
            nonprofit_target_id INTEGER,
            main_tracker_entry_id TEXT NOT NULL,     -- ID from main tracker (e.g., "eo-14151")
            link_type TEXT,                          -- Source Action, Related Action, Derivative
            notes TEXT,
            FOREIGN KEY (nonprofit_action_id) REFERENCES actions(id) ON DELETE CASCADE,
            FOREIGN KEY (nonprofit_target_id) REFERENCES targets(id) ON DELETE CASCADE
        )
    ''')

    # =========================================================================
    # 8. EVIDENCE_DOCUMENTS - Supporting documentation
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evidence_documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action_id INTEGER,
            target_id INTEGER,
            document_type TEXT,                      -- Federal Register, Press Release, Letter, Court Filing, News Report
            document_title TEXT,
            document_date TEXT,
            document_url TEXT,
            document_content TEXT,
            FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE CASCADE,
            FOREIGN KEY (target_id) REFERENCES targets(id) ON DELETE CASCADE
        )
    ''')

    # =========================================================================
    # 9. LITIGATION TABLE - Legal challenges
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS litigation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_name TEXT NOT NULL,
            case_number TEXT,
            court TEXT,
            filing_date TEXT,
            current_status TEXT,                     -- Filed, Preliminary Injunction, Trial, Appeal, Resolved
            outcome TEXT,
            plaintiffs TEXT,                         -- JSON array
            defendants TEXT,                         -- JSON array
            related_action_id INTEGER,
            related_target_id INTEGER,
            main_tracker_ref TEXT,
            FOREIGN KEY (related_action_id) REFERENCES actions(id) ON DELETE SET NULL,
            FOREIGN KEY (related_target_id) REFERENCES targets(id) ON DELETE SET NULL
        )
    ''')

    # =========================================================================
    # 10. TIMELINE_EVENTS - Chronological tracking
    # =========================================================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS timeline_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_date TEXT NOT NULL,
            event_type TEXT,                         -- Action Signed, Target Named, Litigation Filed, Injunction, Implementation
            title TEXT NOT NULL,
            description TEXT,
            action_id INTEGER,
            target_id INTEGER,
            litigation_id INTEGER,
            FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE SET NULL,
            FOREIGN KEY (target_id) REFERENCES targets(id) ON DELETE SET NULL,
            FOREIGN KEY (litigation_id) REFERENCES litigation(id) ON DELETE SET NULL
        )
    ''')

    conn.commit()
    return conn


def populate_cultural_communities(conn):
    """Populate cultural communities from main tracker taxonomy."""
    cursor = conn.cursor()

    communities = [
        ('africanDescendant', 'African Descendant Communities', 'African American, Caribbean, and African diaspora communities'),
        ('indigenous', 'Indigenous/Tribal Communities', '574 federally recognized tribes, state-recognized tribes, Indigenous peoples'),
        ('latine', 'Latiné Communities', 'Mexican American, Central American, South American, Caribbean Hispanic communities'),
        ('asianAmerican', 'Asian American Communities', 'Chinese, Japanese, Korean, Filipino, Vietnamese, South Asian, Southeast Asian communities'),
        ('pacificIslander', 'Pacific Islander/Oceania', 'Native Hawaiian, Samoan, Chamorro, Tongan, Marshallese communities'),
        ('caribbean', 'Caribbean Communities', 'Puerto Rican, Cuban, Dominican, Jamaican, Haitian, other Caribbean communities'),
        ('middleEastern', 'Middle Eastern/North African', 'Arab American, Persian, Turkish, North African communities'),
        ('muslim', 'Muslim Communities', 'Muslim Americans of all ethnic backgrounds'),
        ('lgbtq', 'LGBTQ+ Communities', 'Lesbian, Gay, Bisexual, Transgender, Queer, Two-Spirit communities'),
        ('immigrant', 'Immigrant Communities', 'First-generation immigrants, refugees, asylum seekers, mixed-status families'),
        ('disabled', 'Disabled Communities', 'People with disabilities, Deaf community'),
        ('alaskaNative', 'Alaska Native Communities', 'Yupik, Inupiat, Athabascan, Tlingit, Haida, and other Alaska Native peoples'),
        ('arts', 'Arts/Cultural Worker Communities', 'Artists, performers, museum professionals, cultural workers'),
        ('academic', 'Academic/Research Communities', 'Scholars, researchers, students, university communities'),
        ('environmental', 'Environmental Justice Communities', 'Communities bearing disproportionate environmental burdens')
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO cultural_communities (community_code, community_name, description)
        VALUES (?, ?, ?)
    ''', communities)

    conn.commit()


def populate_actions(conn):
    """
    Populate actions from both the user's original data and expanded entries
    from the main TCKC tracker.
    """
    cursor = conn.cursor()

    actions_data = [
        # =====================================================================
        # ORIGINAL USER DATA
        # =====================================================================
        {
            'action_id': 'eo-14151',
            'title': 'Ending Radical and Wasteful Government DEI Programs and Preferencing',
            'short_title': 'End Federal DEI',
            'date': '2025-01-20',
            'doc_type': 'Executive Order',
            'administration': 'Trump II',
            'agencies': json.dumps(['OMB', 'OPM', 'NEA', 'NEH', 'SMITHSONIAN', 'ALL']),
            'status': 'Active - Partial Injunction',
            'threat_level': 'SEVERE',
            'description': '''Executive Order 14151 directs all agencies to terminate DEI/DEIA offices, positions, programs, grants, and contracts within 60 days. Revokes Biden equity orders (EO 13985, 14031, 14045, 14049, 14091, 14096).

NONPROFIT IMPACT: Over 1,000 nonprofits rewrote mission statements to comply. DEI-focused grants terminated. Organizations with diversity missions face federal funding exclusion. Grantee certification requirements chill nonprofit advocacy.

IMPLEMENTATION: NEA requires certification against "gender ideology" and DEI in grants. Smithsonian closed diversity office. Kennedy Center eliminated Social Impact team. NMAAHC, NMAI, Latino Museum programming affected.''',
            'main_tracker_ref': 'eo-14151'
        },
        {
            'action_id': 'eo-14235',
            'title': 'Restoring Public Service Loan Forgiveness',
            'short_title': 'PSLF Changes',
            'date': '2025-03-07',
            'doc_type': 'Executive Order',
            'administration': 'Trump II',
            'agencies': json.dumps(['ED', 'OMB']),
            'status': 'Active',
            'threat_level': 'HARMFUL',
            'description': '''Executive Order modifying Public Service Loan Forgiveness program eligibility.

NONPROFIT IMPACT: Changes to PSLF eligibility criteria could affect nonprofit employees' ability to qualify for loan forgiveness. Nonprofits may face difficulty recruiting workers if loan forgiveness benefits are reduced or eliminated for certain organization types.''',
            'main_tracker_ref': None
        },
        {
            'action_id': 'nspm-7',
            'title': 'Countering Domestic Terrorism and Radical Ideology',
            'short_title': 'Counter-Terrorism Memo',
            'date': '2025-09-25',
            'doc_type': 'Memorandum',
            'administration': 'Trump II',
            'agencies': json.dumps(['DHS', 'DOJ', 'FBI']),
            'status': 'Active',
            'threat_level': 'SEVERE',
            'description': '''National Security Presidential Memorandum establishing framework for designating domestic organizations as supporting terrorism.

NONPROFIT IMPACT: Broad language could be used to target civil rights organizations, immigrant advocacy groups, environmental organizations, and others engaged in lawful advocacy. Creates chilling effect on First Amendment protected activities.''',
            'main_tracker_ref': None
        },
        {
            'action_id': 'hr-9495',
            'title': 'Stop Terror-Financing and Tax Penalties on American Hostages Act',
            'short_title': 'Tax-Exempt Revocation Bill',
            'date': '2024-11-21',
            'doc_type': 'Bill',
            'administration': 'Congress (118th)',
            'agencies': json.dumps(['Treasury', 'IRS']),
            'status': 'Stalled/Pending Standalone',
            'threat_level': 'SEVERE',
            'description': '''H.R. 9495 would allow the Treasury Secretary to revoke 501(c)(3) tax-exempt status of organizations designated as "terrorist supporting organizations" with minimal due process.

NONPROFIT IMPACT: Creates mechanism for politically-motivated revocation of tax-exempt status. Organizations would lose status first and have to challenge designation after the fact. Broad and vague criteria could target legitimate advocacy organizations.

CURRENT STATUS: Passed House attached to other legislation but stalled. Expected reintroduction in 119th Congress.''',
            'main_tracker_ref': None
        },

        # =====================================================================
        # EXPANDED FROM MAIN TRACKER - DEI/EQUITY RELATED
        # =====================================================================
        {
            'action_id': 'eo-14168',
            'title': 'Defending Women from Gender Ideology Extremism and Restoring Biological Truth to the Federal Government',
            'short_title': 'Gender Ideology Ban',
            'date': '2025-01-20',
            'doc_type': 'Executive Order',
            'administration': 'Trump II',
            'agencies': json.dumps(['NEA', 'NEH', 'STATE', 'HHS', 'ED', 'ALL']),
            'status': 'Partially Enjoined (NEA provision struck Sept 19, 2025)',
            'threat_level': 'SEVERE',
            'description': '''Directs agencies to "end federal funding of gender ideology" and recognize only "biological sex."

NONPROFIT IMPACT: NEA requires grant certification against promoting "gender ideology" - affects LGBTQ+ arts organizations, theaters, and cultural groups. Rhode Island Latino Arts led successful lawsuit. Ballroom culture (Black/Latino origin) and Two-Spirit traditions excluded from recognition.

LITIGATION: NEA provision struck down Sept 19, 2025 as First Amendment violation.''',
            'main_tracker_ref': 'eo-14168'
        },

        # =====================================================================
        # CULTURAL AGENCY ACTIONS
        # =====================================================================
        {
            'action_id': 'imls-grants-terminated-2025',
            'title': 'IMLS Staff on Administrative Leave, 1,200 Grants Terminated',
            'short_title': 'IMLS Grant Terminations',
            'date': '2025-02-15',
            'doc_type': 'Agency Action',
            'administration': 'Trump II',
            'agencies': json.dumps(['IMLS']),
            'status': 'Implemented',
            'threat_level': 'SEVERE',
            'description': '''Institute of Museum and Library Services terminated 1,200+ grants affecting museums and libraries nationwide.

NONPROFIT IMPACT: Terminated Native American Library Services grants - only federal program supporting tribal libraries. 28+ tribal libraries affected. Native American/Native Hawaiian Museum Services grants ended. NAGPRA compliance support eliminated. African American museum and library grants terminated. Latino cultural institution grants ended. Asian American cultural organization grants terminated.''',
            'main_tracker_ref': 'aa-imls-firings-grants'
        },
        {
            'action_id': 'nea-friday-massacre',
            'title': 'NEA "Friday Night Massacre" - 50%+ of Grants Terminated',
            'short_title': 'NEA Mass Terminations',
            'date': '2025-03-01',
            'doc_type': 'Agency Action',
            'administration': 'Trump II',
            'agencies': json.dumps(['NEA']),
            'status': 'Implemented',
            'threat_level': 'SEVERE',
            'description': '''NEA terminated over 50% of active grants in mass termination event.

NONPROFIT IMPACT: Arts organizations nationwide lost federal funding. Disproportionate impact on organizations serving communities of color, LGBTQ+ communities, and rural areas. Terminated grants include those for Black theater companies, Latino folk arts, Indigenous arts programs, Asian American cultural organizations, and disability arts.''',
            'main_tracker_ref': 'aa-nea-friday-massacre'
        },
        {
            'action_id': 'neh-grants-terminated-2025',
            'title': 'NEH Chair Removed; 1,400+ Grants Terminated',
            'short_title': 'NEH Mass Terminations',
            'date': '2025-02-20',
            'doc_type': 'Agency Action',
            'administration': 'Trump II',
            'agencies': json.dumps(['NEH']),
            'status': 'Implemented - Partial Court Order',
            'threat_level': 'SEVERE',
            'description': '''NEH Chair Dr. Shelly Lowe (Navajo) removed. 1,400+ humanities grants terminated.

NONPROFIT IMPACT: State humanities councils lost all federal funding. Historical societies, archives, libraries, museums, and universities lost humanities grants. Projects on African American history, Latino heritage, Indigenous languages, Asian American experiences, and civil rights history terminated.''',
            'main_tracker_ref': 'aa-neh-chair-removed'
        },
        {
            'action_id': 'kennedy-center-dei-elimination',
            'title': 'Kennedy Center Eliminates Social Impact Team and DEI Programs',
            'short_title': 'Kennedy Center DEI Cuts',
            'date': '2025-02-01',
            'doc_type': 'Agency Action',
            'administration': 'Trump II',
            'agencies': json.dumps(['KENNEDY']),
            'status': 'Implemented',
            'threat_level': 'SEVERE',
            'description': '''Kennedy Center eliminated Social Impact team and DEI-related programming.

NONPROFIT IMPACT: Ended The Cartography Project documenting lynchings and race-based violence. Terminated 19-year Christmas Eve jazz tradition. Eliminated arts access programs for low-income communities. Disability arts initiatives terminated. Pride programming eliminated.''',
            'main_tracker_ref': 'aa-kennedy-dei'
        },

        # =====================================================================
        # PUBLIC MEDIA DEFUNDING
        # =====================================================================
        {
            'action_id': 'cpb-rescission-2025',
            'title': 'Rescissions Act of 2025 - Defunding the Corporation for Public Broadcasting',
            'short_title': 'CPB Defunding',
            'date': '2025-05-15',
            'doc_type': 'Legislation',
            'administration': 'Trump II',
            'agencies': json.dumps(['CPB']),
            'status': 'Enacted',
            'threat_level': 'SEVERE',
            'description': '''P.L. 119-28 rescinds appropriated funds for Corporation for Public Broadcasting.

NONPROFIT IMPACT: Affects 1,500 local public radio and TV stations (mostly nonprofits). Rural stations serving Indigenous, Latino, and isolated communities face closure. Over 200 rural communities served only by public broadcasting lose all broadcast service. Stations serving as community cultural centers face defunding.''',
            'main_tracker_ref': 'pl-119-28-cpb'
        },
        {
            'action_id': 'hr-1216-defund-cpb',
            'title': 'Defund Government-Sponsored Propaganda Act',
            'short_title': 'Defund PBS/NPR Act',
            'date': '2025-01-15',
            'doc_type': 'Bill',
            'administration': 'Congress (119th)',
            'agencies': json.dumps(['CPB']),
            'status': 'Pending',
            'threat_level': 'SEVERE',
            'description': '''H.R. 1216 would dissolve the Corporation for Public Broadcasting entirely.

NONPROFIT IMPACT: Would permanently eliminate federal funding for public media. 1,500 nonprofit stations affected. Rural and underserved communities lose broadcast infrastructure. Native broadcasting (AIROS, Koahnic) lose essential support.''',
            'main_tracker_ref': 'hr-1216-defund-pbs-npr'
        },

        # =====================================================================
        # UNIVERSITY/EDUCATION TARGETING
        # =====================================================================
        {
            'action_id': 'proc-harvard-ban',
            'title': 'Restricting Entry of Foreign Nationals to Harvard University',
            'short_title': 'Harvard International Ban',
            'date': '2025-04-15',
            'doc_type': 'Proclamation',
            'administration': 'Trump II',
            'agencies': json.dumps(['STATE', 'DHS']),
            'status': 'Enjoined',
            'threat_level': 'SEVERE',
            'description': '''Proclamation banning issuance of visas to international students, faculty, and researchers at Harvard University.

NONPROFIT IMPACT: First-ever executive action targeting a specific university. Affects 7,000+ international students. Chills academic freedom at all universities. Retaliation for Harvard's refusal to comply with political demands.

LITIGATION: Preliminary injunction granted; Harvard v. DHS ongoing.''',
            'main_tracker_ref': 'proc-harvard-ban'
        },
        {
            'action_id': 'eo-14156-divisive-concepts',
            'title': 'Ending Illegal Discrimination and Restoring Merit-Based Opportunity',
            'short_title': 'Divisive Concepts Ban',
            'date': '2025-01-20',
            'doc_type': 'Executive Order',
            'administration': 'Trump II',
            'agencies': json.dumps(['ED', 'DOJ', 'ALL']),
            'status': 'Active - Multiple Injunctions',
            'threat_level': 'SEVERE',
            'description': '''Extends DEI restrictions to federal contractors and grant recipients. Targets "divisive concepts" in education.

NONPROFIT IMPACT: Universities, schools, and educational nonprofits receiving federal funds must comply. Teaching about systemic racism, implicit bias, and structural inequality potentially prohibited. Affects grants for African American studies, ethnic studies, women's studies, and LGBTQ+ research.''',
            'main_tracker_ref': 'eo-14156-doi'
        },

        # =====================================================================
        # SMITHSONIAN ACTIONS
        # =====================================================================
        {
            'action_id': 'smithsonian-fy2026-cuts',
            'title': 'FY2026 Budget: Latino and Anacostia Museums Defunded',
            'short_title': 'Smithsonian Budget Cuts',
            'date': '2025-02-01',
            'doc_type': 'Budget Request',
            'administration': 'Trump II',
            'agencies': json.dumps(['SMITHSONIAN']),
            'status': 'Proposed',
            'threat_level': 'SEVERE',
            'description': '''FY2026 budget request eliminates funding for National Museum of the American Latino and Anacostia Community Museum.

NONPROFIT IMPACT: Latino Museum construction halted despite congressional authorization. Anacostia - nation's first federally-funded Black community museum - faces closure. NMAAHC and NMAI face programming cuts. Diversity office closed.''',
            'main_tracker_ref': 'smithsonian-fy2026'
        },

        # =====================================================================
        # ENVIRONMENTAL JUSTICE
        # =====================================================================
        {
            'action_id': 'ej-grant-terminations',
            'title': 'EPA Environmental Justice Grant Terminations',
            'short_title': 'EJ Grant Cuts',
            'date': '2025-02-15',
            'doc_type': 'Agency Action',
            'administration': 'Trump II',
            'agencies': json.dumps(['EPA']),
            'status': 'Implemented',
            'threat_level': 'SEVERE',
            'description': '''EPA terminated environmental justice grants and closed Office of Environmental Justice.

NONPROFIT IMPACT: Community-based organizations in frontline communities lost funding. Health advocates, air quality monitors, and environmental justice organizations defunded. Affects organizations serving Indigenous, Black, Latino, Asian American, and low-income communities bearing disproportionate pollution burdens.''',
            'main_tracker_ref': 'lit-ej-grant-terminations'
        },

        # =====================================================================
        # IMMIGRATION-RELATED (AFFECTING IMMIGRANT-SERVING NONPROFITS)
        # =====================================================================
        {
            'action_id': 'eo-14159-border',
            'title': 'Securing Our Borders Executive Order',
            'short_title': 'Border Security EO',
            'date': '2025-01-20',
            'doc_type': 'Executive Order',
            'administration': 'Trump II',
            'agencies': json.dumps(['DHS', 'DOJ', 'DOD']),
            'status': 'Active - Partial Injunctions',
            'threat_level': 'SEVERE',
            'description': '''Declares national emergency at southern border. Deploys military for immigration enforcement.

NONPROFIT IMPACT: Immigrant services organizations face operational challenges. Legal aid nonprofits overwhelmed. Humanitarian organizations at border restricted. Nonprofit shelters and service providers affected.''',
            'main_tracker_ref': 'eo-14159'
        },
        {
            'action_id': 'eo-14287-sanctuary',
            'title': 'Sanctuary Cities Executive Order',
            'short_title': 'Sanctuary Cities Order',
            'date': '2025-01-25',
            'doc_type': 'Executive Order',
            'administration': 'Trump II',
            'agencies': json.dumps(['DOJ', 'DHS']),
            'status': 'Active - Litigation Pending',
            'threat_level': 'SEVERE',
            'description': '''Withholds federal funding from sanctuary jurisdictions. Targets cities and states limiting cooperation with ICE.

NONPROFIT IMPACT: Nonprofits in affected jurisdictions could lose federal funding. Social service organizations face funding cuts. Immigrant services organizations face hostile environment.''',
            'main_tracker_ref': 'eo-14287'
        },
    ]

    for action in actions_data:
        cursor.execute('''
            INSERT OR REPLACE INTO actions
            (action_id, title, short_title, date, doc_type, administration, agencies, status,
             threat_level, description, main_tracker_ref, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (
            action['action_id'],
            action['title'],
            action.get('short_title'),
            action.get('date'),
            action.get('doc_type'),
            action.get('administration'),
            action.get('agencies'),
            action.get('status'),
            action.get('threat_level'),
            action.get('description'),
            action.get('main_tracker_ref')
        ))

    conn.commit()


def populate_targets(conn):
    """
    Populate targeted organizations from user's original data and expanded list.
    """
    cursor = conn.cursor()

    targets_data = [
        # =====================================================================
        # ORIGINAL USER DATA - SPECIFICALLY NAMED ORGANIZATIONS
        # =====================================================================
        {
            'entity_name': 'Wikimedia Foundation',
            'entity_type': 'Foundation',
            'tax_status': '501(c)(3)',
            'headquarters': 'San Francisco, CA',
            'threat_nature': '501(c)(3) Eligibility Questioned',
            'threat_level': 'SEVERE',
            'official_source': 'Ed Martin (FEC Commissioner Nominee)',
            'evidence_level': 'Official Correspondence',
            'evidence_description': 'Ed Martin sent official correspondence questioning Wikimedia Foundation tax-exempt status',
            'date_first_targeted': '2025-03-15',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'Open Society Foundations',
            'entity_type': 'Foundation',
            'tax_status': '501(c)(3)',
            'headquarters': 'New York, NY',
            'threat_nature': 'RICO investigation threatened; "criminal organization" rhetoric',
            'threat_level': 'SEVERE',
            'official_source': 'JD Vance, Stephen Miller, Donald Trump',
            'evidence_level': 'Reported Internal Directive',
            'evidence_description': 'Multiple reports of internal directives to investigate George Soros and Open Society Foundations',
            'date_first_targeted': '2024-11-01',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'Harvard University',
            'entity_type': 'University',
            'tax_status': '501(c)(3)',
            'headquarters': 'Cambridge, MA',
            'threat_nature': 'Tax-exempt revocation calls; international student ban; federal funding threats',
            'threat_level': 'SEVERE',
            'official_source': 'Donald Trump, Administration Officials',
            'evidence_level': 'Official Document',
            'evidence_description': 'Presidential proclamation banning international students; presidential statements calling for tax-exempt revocation',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Litigation Pending'
        },
        {
            'entity_name': 'Ford Foundation',
            'entity_type': 'Foundation',
            'tax_status': '501(c)(3)',
            'headquarters': 'New York, NY',
            'threat_nature': 'Tax-exempt status review; political targeting',
            'threat_level': 'HARMFUL',
            'official_source': 'JD Vance',
            'evidence_level': 'Public Statement',
            'evidence_description': 'Vice President Vance made public statements questioning Ford Foundation tax-exempt status',
            'date_first_targeted': '2025-02-01',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'Southern Poverty Law Center',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)',
            'headquarters': 'Montgomery, AL',
            'threat_nature': 'Accused of radicalizing shooters; terrorist designation rhetoric',
            'threat_level': 'SEVERE',
            'official_source': 'Administration Officials, Conservative Media',
            'evidence_level': 'Public Statement',
            'evidence_description': 'Administration officials repeated claims that SPLC "hate group" designations radicalized shooters',
            'date_first_targeted': '2025-01-25',
            'current_status': 'Active Threat'
        },

        # =====================================================================
        # EXPANDED LIST - CULTURAL ORGANIZATIONS
        # =====================================================================
        {
            'entity_name': 'Rhode Island Latino Arts',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)',
            'headquarters': 'Providence, RI',
            'threat_nature': 'NEA grant denial under gender ideology certification',
            'threat_level': 'HARMFUL',
            'official_source': 'NEA',
            'evidence_level': 'Official Document',
            'evidence_description': 'Lead plaintiff in successful lawsuit against NEA gender ideology certification requirement',
            'date_first_targeted': '2025-02-01',
            'current_status': 'Resolved - Lawsuit Won'
        },
        {
            'entity_name': 'National Museum of African American History and Culture',
            'entity_type': 'Museum',
            'tax_status': 'Federal Entity',
            'headquarters': 'Washington, DC',
            'threat_nature': 'DEI program elimination; budget cuts; programming restrictions',
            'threat_level': 'SEVERE',
            'official_source': 'Trump Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'EO 14151 affects Smithsonian museums; diversity office closed',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Implemented'
        },
        {
            'entity_name': 'National Museum of the American Indian',
            'entity_type': 'Museum',
            'tax_status': 'Federal Entity',
            'headquarters': 'Washington, DC',
            'threat_nature': 'DEI program elimination; consultation requirements weakened',
            'threat_level': 'SEVERE',
            'official_source': 'Trump Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'EO 14151 affects tribal consultation framed as "equity"',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Implemented'
        },
        {
            'entity_name': 'National Museum of the American Latino (Planned)',
            'entity_type': 'Museum',
            'tax_status': 'Federal Entity',
            'headquarters': 'Washington, DC',
            'threat_nature': 'Construction halted; funding eliminated in FY2026 budget',
            'threat_level': 'SEVERE',
            'official_source': 'OMB/Trump Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'FY2026 budget request eliminates funding despite congressional authorization',
            'date_first_targeted': '2025-02-01',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'Anacostia Community Museum',
            'entity_type': 'Museum',
            'tax_status': 'Federal Entity',
            'headquarters': 'Washington, DC',
            'threat_nature': 'Closure threatened in FY2026 budget',
            'threat_level': 'SEVERE',
            'official_source': 'OMB/Trump Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'FY2026 budget request eliminates funding for nation\'s first federally-funded Black community museum',
            'date_first_targeted': '2025-02-01',
            'current_status': 'Active Threat'
        },

        # =====================================================================
        # PUBLIC MEDIA
        # =====================================================================
        {
            'entity_name': 'National Public Radio (NPR)',
            'entity_type': 'Media',
            'tax_status': '501(c)(3)',
            'headquarters': 'Washington, DC',
            'threat_nature': 'Federal funding elimination; "propaganda" accusations',
            'threat_level': 'SEVERE',
            'official_source': 'Trump Administration, Congress',
            'evidence_level': 'Official Document',
            'evidence_description': 'P.L. 119-28 rescinds CPB funding; H.R. 1216 targets NPR dissolution',
            'date_first_targeted': '2025-01-15',
            'current_status': 'Litigation Pending'
        },
        {
            'entity_name': 'Public Broadcasting Service (PBS)',
            'entity_type': 'Media',
            'tax_status': '501(c)(3)',
            'headquarters': 'Arlington, VA',
            'threat_nature': 'Federal funding elimination',
            'threat_level': 'SEVERE',
            'official_source': 'Trump Administration, Congress',
            'evidence_level': 'Official Document',
            'evidence_description': 'P.L. 119-28 rescinds CPB funding; H.R. 1216 targets PBS dissolution',
            'date_first_targeted': '2025-01-15',
            'current_status': 'Litigation Pending'
        },
        {
            'entity_name': 'Corporation for Public Broadcasting',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)',
            'headquarters': 'Washington, DC',
            'threat_nature': 'Complete dissolution targeted',
            'threat_level': 'SEVERE',
            'official_source': 'Congress, Trump Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'P.L. 119-28 enacted; H.R. 1216 seeks complete dissolution',
            'date_first_targeted': '2025-01-15',
            'current_status': 'Implemented - Funding Rescinded'
        },

        # =====================================================================
        # LIBRARIES AND HUMANITIES
        # =====================================================================
        {
            'entity_name': 'State Humanities Councils (Federation of 56)',
            'entity_type': 'Nonprofit Network',
            'tax_status': '501(c)(3)',
            'headquarters': 'Nationwide',
            'threat_nature': 'All federal funding terminated via NEH cuts',
            'threat_level': 'SEVERE',
            'official_source': 'NEH',
            'evidence_level': 'Official Document',
            'evidence_description': 'NEH terminated all grants to 56 state and territorial humanities councils',
            'date_first_targeted': '2025-02-20',
            'current_status': 'Implemented - Litigation Pending'
        },
        {
            'entity_name': 'Tribal Libraries (28+ institutions)',
            'entity_type': 'Library Network',
            'tax_status': 'Tribal/501(c)(3)',
            'headquarters': 'Nationwide',
            'threat_nature': 'Only federal support program (Native American Library Services) terminated',
            'threat_level': 'SEVERE',
            'official_source': 'IMLS',
            'evidence_level': 'Official Document',
            'evidence_description': 'IMLS terminated Native American Library Services Basic Grants - only federal program supporting tribal libraries',
            'date_first_targeted': '2025-02-15',
            'current_status': 'Implemented'
        },
        {
            'entity_name': 'Chinese Historical Society of America',
            'entity_type': 'Museum',
            'tax_status': '501(c)(3)',
            'headquarters': 'San Francisco, CA',
            'threat_nature': 'IMLS grants terminated; digitization projects halted',
            'threat_level': 'HARMFUL',
            'official_source': 'IMLS',
            'evidence_level': 'Official Document',
            'evidence_description': 'Grant terminations affected archives preservation and digitization',
            'date_first_targeted': '2025-02-15',
            'current_status': 'Implemented'
        },
        {
            'entity_name': 'Japanese American National Museum',
            'entity_type': 'Museum',
            'tax_status': '501(c)(3)',
            'headquarters': 'Los Angeles, CA',
            'threat_nature': 'IMLS digitization grants frozen',
            'threat_level': 'HARMFUL',
            'official_source': 'IMLS',
            'evidence_level': 'Official Document',
            'evidence_description': 'Grant terminations halted digitization of Japanese American incarceration records',
            'date_first_targeted': '2025-02-15',
            'current_status': 'Implemented'
        },

        # =====================================================================
        # CIVIL RIGHTS / ADVOCACY
        # =====================================================================
        {
            'entity_name': 'American Civil Liberties Union',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)/501(c)(4)',
            'headquarters': 'New York, NY',
            'threat_nature': 'Political targeting; "radical" organization rhetoric',
            'threat_level': 'HARMFUL',
            'official_source': 'Administration Officials',
            'evidence_level': 'Public Statement',
            'evidence_description': 'Administration officials have characterized ACLU as radical; ACLU litigation challenging multiple administration actions',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'NAACP',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)/501(c)(4)',
            'headquarters': 'Baltimore, MD',
            'threat_nature': 'DEI restrictions affect programming; political targeting',
            'threat_level': 'HARMFUL',
            'official_source': 'Administration',
            'evidence_level': 'Public Statement',
            'evidence_description': 'EO 14151 and related orders restrict equity-focused programming and federal partnerships',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'MALDEF (Mexican American Legal Defense and Educational Fund)',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)',
            'headquarters': 'Los Angeles, CA',
            'threat_nature': 'Immigration enforcement impacts clients; political targeting',
            'threat_level': 'HARMFUL',
            'official_source': 'Administration',
            'evidence_level': 'Public Statement',
            'evidence_description': 'Immigration orders and DEI restrictions affect MALDEF programming and litigation',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'National Congress of American Indians',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)',
            'headquarters': 'Washington, DC',
            'threat_nature': 'Tribal consultation requirements weakened as "equity"',
            'threat_level': 'HARMFUL',
            'official_source': 'Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'EO 14151 characterizes tribal consultation requirements as DEI and targets for elimination',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Active Threat'
        },

        # =====================================================================
        # ENVIRONMENTAL
        # =====================================================================
        {
            'entity_name': 'Environmental Defense Fund',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)',
            'headquarters': 'New York, NY',
            'threat_nature': 'Federal partnerships terminated; "radical environmentalist" rhetoric',
            'threat_level': 'HARMFUL',
            'official_source': 'Administration',
            'evidence_level': 'Official Document',
            'evidence_description': 'Environmental justice office closures and grant terminations affect partnerships',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Active Threat'
        },
        {
            'entity_name': 'Sierra Club',
            'entity_type': 'Nonprofit',
            'tax_status': '501(c)(3)/501(c)(4)',
            'headquarters': 'Oakland, CA',
            'threat_nature': 'Environmental justice programs defunded; political targeting',
            'threat_level': 'HARMFUL',
            'official_source': 'Administration',
            'evidence_level': 'Public Statement',
            'evidence_description': 'Administration characterizes environmental groups as radical; EJ grants terminated',
            'date_first_targeted': '2025-01-20',
            'current_status': 'Active Threat'
        },
    ]

    for target in targets_data:
        cursor.execute('''
            INSERT OR REPLACE INTO targets
            (entity_name, entity_type, tax_status, headquarters, threat_nature, threat_level,
             official_source, evidence_level, evidence_description, date_first_targeted,
             current_status, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (
            target['entity_name'],
            target.get('entity_type'),
            target.get('tax_status'),
            target.get('headquarters'),
            target.get('threat_nature'),
            target.get('threat_level'),
            target.get('official_source'),
            target.get('evidence_level'),
            target.get('evidence_description'),
            target.get('date_first_targeted'),
            target.get('current_status')
        ))

    conn.commit()


def populate_action_targets(conn):
    """Link actions to their targets."""
    cursor = conn.cursor()

    # Get action and target IDs
    cursor.execute('SELECT id, action_id FROM actions')
    actions = {row[1]: row[0] for row in cursor.fetchall()}

    cursor.execute('SELECT id, entity_name FROM targets')
    targets = {row[1]: row[0] for row in cursor.fetchall()}

    links = [
        # DEI Order affects many
        ('eo-14151', 'Harvard University', 'Direct Target', 'DEI compliance requirements'),
        ('eo-14151', 'National Museum of African American History and Culture', 'Direct Target', 'Smithsonian diversity office closed'),
        ('eo-14151', 'National Museum of the American Indian', 'Direct Target', 'Tribal consultation as DEI targeted'),
        ('eo-14151', 'National Museum of the American Latino (Planned)', 'Collateral Impact', 'DEI framing threatens Latino museum'),
        ('eo-14151', 'Ford Foundation', 'Collateral Impact', 'Grantee certification requirements'),
        ('eo-14151', 'Open Society Foundations', 'Collateral Impact', 'Grantee certification requirements'),
        ('eo-14151', 'NAACP', 'Collateral Impact', 'Federal equity partnerships terminated'),

        # Gender ideology order
        ('eo-14168', 'Rhode Island Latino Arts', 'Direct Target', 'Lead plaintiff in successful challenge'),

        # Harvard ban
        ('proc-harvard-ban', 'Harvard University', 'Direct Target', 'University specifically targeted by proclamation'),

        # IMLS terminations
        ('imls-grants-terminated-2025', 'Tribal Libraries (28+ institutions)', 'Direct Target', 'Native American Library Services grants terminated'),
        ('imls-grants-terminated-2025', 'Chinese Historical Society of America', 'Direct Target', 'Digitization grants frozen'),
        ('imls-grants-terminated-2025', 'Japanese American National Museum', 'Direct Target', 'Digitization grants frozen'),

        # NEH terminations
        ('neh-grants-terminated-2025', 'State Humanities Councils (Federation of 56)', 'Direct Target', 'All federal funding terminated'),

        # CPB defunding
        ('cpb-rescission-2025', 'National Public Radio (NPR)', 'Direct Target', 'Federal funding rescinded'),
        ('cpb-rescission-2025', 'Public Broadcasting Service (PBS)', 'Direct Target', 'Federal funding rescinded'),
        ('cpb-rescission-2025', 'Corporation for Public Broadcasting', 'Direct Target', 'Appropriations rescinded'),

        # HR 1216
        ('hr-1216-defund-cpb', 'National Public Radio (NPR)', 'Direct Target', 'Complete dissolution sought'),
        ('hr-1216-defund-cpb', 'Public Broadcasting Service (PBS)', 'Direct Target', 'Complete dissolution sought'),
        ('hr-1216-defund-cpb', 'Corporation for Public Broadcasting', 'Direct Target', 'Complete dissolution sought'),

        # Smithsonian budget
        ('smithsonian-fy2026-cuts', 'National Museum of the American Latino (Planned)', 'Direct Target', 'Construction funding eliminated'),
        ('smithsonian-fy2026-cuts', 'Anacostia Community Museum', 'Direct Target', 'Closure threatened'),
        ('smithsonian-fy2026-cuts', 'National Museum of African American History and Culture', 'Collateral Impact', 'Budget cuts'),

        # HR 9495
        ('hr-9495', 'Wikimedia Foundation', 'Collateral Impact', 'Could be targeted under broad language'),
        ('hr-9495', 'Open Society Foundations', 'Collateral Impact', 'Political targeting could use this mechanism'),
        ('hr-9495', 'Southern Poverty Law Center', 'Collateral Impact', 'Could be targeted under terrorism rhetoric'),
        ('hr-9495', 'American Civil Liberties Union', 'Collateral Impact', 'Could be targeted under broad language'),

        # Kennedy Center
        ('kennedy-center-dei-elimination', 'National Museum of African American History and Culture', 'Collateral Impact', 'Shared Smithsonian DEI infrastructure'),

        # Environmental Justice
        ('ej-grant-terminations', 'Environmental Defense Fund', 'Collateral Impact', 'Federal EJ partnerships terminated'),
        ('ej-grant-terminations', 'Sierra Club', 'Collateral Impact', 'EJ programs affected'),
    ]

    for action_id, target_name, rel_type, description in links:
        if action_id in actions and target_name in targets:
            cursor.execute('''
                INSERT OR IGNORE INTO action_targets
                (action_id, target_id, relationship_type, impact_description)
                VALUES (?, ?, ?, ?)
            ''', (actions[action_id], targets[target_name], rel_type, description))

    conn.commit()


def populate_community_impacts(conn):
    """Populate cultural community impacts using 4Ps framework."""
    cursor = conn.cursor()

    # Get IDs
    cursor.execute('SELECT id, action_id FROM actions')
    actions = {row[1]: row[0] for row in cursor.fetchall()}

    cursor.execute('SELECT id, community_code FROM cultural_communities')
    communities = {row[1]: row[0] for row in cursor.fetchall()}

    impacts = [
        # EO 14151 - DEI Order
        {
            'action_id': 'eo-14151',
            'community_code': 'africanDescendant',
            'people_severity': 'SEVERE',
            'people_description': 'Smithsonian diversity officers, NMAAHC community engagement staff, Kennedy Center Social Impact team terminated. Black museum professionals\' equity expertise delegitimized.',
            'places_severity': 'SEVERE',
            'places_description': 'NMAAHC community partnerships disrupted. Kennedy Center connections to Black communities severed. NEA presence in historically Black neighborhoods eliminated.',
            'practices_severity': 'SEVERE',
            'practices_description': 'Community engagement methodologies centering Black voices eliminated. Black curatorial practices emphasizing equity dismantled.',
            'treasures_severity': 'HARMFUL',
            'treasures_description': 'NMAAHC collection growth potentially affected. African American oral history projects lose support. Black documentary heritage initiatives defunded.'
        },
        {
            'action_id': 'eo-14151',
            'community_code': 'indigenous',
            'people_severity': 'SEVERE',
            'people_description': 'Tribal liaison positions across cultural agencies eliminated. NMAI community engagement staff reduced. NEA tribal arts coordinators terminated.',
            'places_severity': 'SEVERE',
            'places_description': 'NMAI connections to tribal communities disrupted. NEA presence in Indian Country eliminated. NEH partnerships with tribal colleges ended.',
            'practices_severity': 'SEVERE',
            'practices_description': 'Government-to-government consultation requirements potentially weakened as "equity." Indigenous curatorial methodologies delegitimized. Tribal language programming defunded.',
            'treasures_severity': 'HARMFUL',
            'treasures_description': 'NMAI collection partnerships with tribes affected. Indigenous oral history projects lose support. Tribal language documentation initiatives defunded.'
        },
        {
            'action_id': 'eo-14151',
            'community_code': 'latine',
            'people_severity': 'SEVERE',
            'people_description': 'National Museum of the American Latino planning staff face uncertain future. Latino cultural organization directors rewrote mission statements.',
            'places_severity': 'SEVERE',
            'places_description': 'Pending National Museum of the American Latino faces ideological review. Latino cultural centers lose Smithsonian partnerships.',
            'practices_severity': 'HARMFUL',
            'practices_description': 'Bilingual museum interpretation potentially framed as "DEI." Latino community engagement methodologies disrupted.',
            'treasures_severity': 'HARMFUL',
            'treasures_description': 'Latino museum collection building paused. Chicano art documentation projects affected. Immigration oral histories lose federal support.'
        },
        {
            'action_id': 'eo-14151',
            'community_code': 'lgbtq',
            'people_severity': 'SEVERE',
            'people_description': 'LGBTQ+ museum professionals face hostile workplace climate. Queer arts organization staff rewrote mission statements (1,000+ nonprofits affected).',
            'places_severity': 'SEVERE',
            'places_description': 'Stonewall National Monument interpretation potentially affected. LGBTQ+ cultural centers lose federal engagement. Pride programming cancelled.',
            'practices_severity': 'SEVERE',
            'practices_description': 'LGBTQ+ history documentation delegitimized as "ideology." Pride celebrations at cultural institutions eliminated.',
            'treasures_severity': 'HARMFUL',
            'treasures_description': 'LGBTQ+ archives face uncertain federal support. AIDS memorial collections affected. Queer documentary heritage projects defunded.'
        },

        # IMLS Grant Terminations
        {
            'action_id': 'imls-grants-terminated-2025',
            'community_code': 'indigenous',
            'people_severity': 'SEVERE',
            'people_description': 'Tribal librarians and museum professionals lose federal support. 28+ tribal libraries serving Navajo Nation, Cherokee Nation, Alaska Native villages affected.',
            'places_severity': 'SEVERE',
            'places_description': 'Tribal libraries - often the only cultural and educational hub in remote communities - lose federal support.',
            'practices_severity': 'SEVERE',
            'practices_description': 'Native American Library Services grants - only federal program supporting tribal libraries - terminated. NAGPRA compliance support eliminated.',
            'treasures_severity': 'SEVERE',
            'treasures_description': 'Native American/Native Hawaiian Museum Services grants ended. Tribal archives and collections lose preservation support.'
        },
        {
            'action_id': 'imls-grants-terminated-2025',
            'community_code': 'asianAmerican',
            'people_severity': 'HARMFUL',
            'people_description': 'Asian American museum professionals face grant terminations. Chinese Historical Society, Japanese American National Museum staff affected.',
            'places_severity': 'HARMFUL',
            'places_description': 'Asian American cultural institutions lose federal partnership. Museums serving Asian immigrant communities defunded.',
            'practices_severity': 'HARMFUL',
            'practices_description': 'Multilingual library services for Asian immigrant communities defunded. Cultural programming grants terminated.',
            'treasures_severity': 'HARMFUL',
            'treasures_description': 'Digitization of Japanese American incarceration records halted. Chinese American archives preservation stopped.'
        },

        # CPB Defunding
        {
            'action_id': 'cpb-rescission-2025',
            'community_code': 'indigenous',
            'people_severity': 'SEVERE',
            'people_description': 'Native broadcasters at AIROS (American Indian Radio on Satellite) and Koahnic Broadcast Corporation face job losses. Rural Alaska Native communities lose only broadcast service.',
            'places_severity': 'SEVERE',
            'places_description': 'Reservation communities with no commercial broadcasting lose all broadcast infrastructure. Alaska Native villages lose only news source.',
            'practices_severity': 'SEVERE',
            'practices_description': 'Native language programming on public radio terminated. Indigenous storytelling traditions lose broadcast platform.',
            'treasures_severity': 'HARMFUL',
            'treasures_description': 'Archives of Native broadcasting, including language preservation recordings, lose institutional support.'
        },
        {
            'action_id': 'cpb-rescission-2025',
            'community_code': 'africanDescendant',
            'people_severity': 'HARMFUL',
            'people_description': 'Black public media professionals face job losses. NPR reporters covering Black communities, Black-led stations affected.',
            'places_severity': 'HARMFUL',
            'places_description': 'Urban public stations serving Black communities face budget cuts or closure.',
            'practices_severity': 'HARMFUL',
            'practices_description': 'Black public affairs programming, jazz programming, and cultural content reduced.',
            'treasures_severity': 'WATCH',
            'treasures_description': 'Archives of Black public broadcasting face uncertain future.'
        },
    ]

    for impact in impacts:
        action_db_id = actions.get(impact['action_id'])
        community_db_id = communities.get(impact['community_code'])

        if action_db_id and community_db_id:
            cursor.execute('''
                INSERT OR REPLACE INTO action_community_impacts
                (action_id, community_id, people_severity, people_description,
                 places_severity, places_description, practices_severity, practices_description,
                 treasures_severity, treasures_description, overall_severity)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                action_db_id, community_db_id,
                impact.get('people_severity'), impact.get('people_description'),
                impact.get('places_severity'), impact.get('places_description'),
                impact.get('practices_severity'), impact.get('practices_description'),
                impact.get('treasures_severity'), impact.get('treasures_description'),
                impact.get('people_severity')  # Use people severity as overall for now
            ))

    conn.commit()


def populate_timeline_events(conn):
    """Populate timeline with key events."""
    cursor = conn.cursor()

    # Get action IDs
    cursor.execute('SELECT id, action_id, date, title FROM actions')
    actions = {row[1]: {'id': row[0], 'date': row[2], 'title': row[3]} for row in cursor.fetchall()}

    events = [
        ('2025-01-20', 'Action Signed', 'EO 14151 Signed - End Federal DEI', 'President Trump signs Executive Order 14151 ending DEI programs government-wide'),
        ('2025-01-20', 'Action Signed', 'EO 14168 Signed - Gender Ideology Ban', 'President Trump signs Executive Order 14168 on biological sex'),
        ('2025-02-01', 'Implementation', 'Smithsonian Diversity Office Closed', 'Smithsonian Institution closes Office of Diversity and Inclusion'),
        ('2025-02-01', 'Implementation', 'Kennedy Center Social Impact Team Eliminated', 'Kennedy Center eliminates Social Impact team and DEI programming'),
        ('2025-02-15', 'Implementation', 'IMLS Terminates 1,200 Grants', 'Institute of Museum and Library Services terminates 1,200+ grants'),
        ('2025-02-20', 'Implementation', 'NEH Chair Removed, Grants Terminated', 'Dr. Shelly Lowe (Navajo) removed as NEH Chair; 1,400+ grants terminated'),
        ('2025-03-01', 'Implementation', 'NEA Friday Night Massacre', 'NEA terminates 50%+ of grants in mass termination event'),
        ('2025-04-15', 'Action Signed', 'Harvard International Student Ban', 'Proclamation banning visas for Harvard international students'),
        ('2025-05-15', 'Legislation', 'CPB Funding Rescinded', 'P.L. 119-28 rescinds Corporation for Public Broadcasting appropriations'),
        ('2025-09-19', 'Litigation', 'NEA Gender Certification Struck Down', 'Federal court strikes down NEA gender ideology certification requirement'),
        ('2025-09-25', 'Action Signed', 'NSPM-7 Counter-Terrorism Memo', 'National Security Presidential Memorandum on domestic terrorism'),
    ]

    for date, event_type, title, description in events:
        cursor.execute('''
            INSERT INTO timeline_events (event_date, event_type, title, description)
            VALUES (?, ?, ?, ?)
        ''', (date, event_type, title, description))

    conn.commit()


def populate_litigation(conn):
    """Populate litigation tracking."""
    cursor = conn.cursor()

    litigation_data = [
        {
            'case_name': 'Rhode Island Latino Arts v. NEA',
            'case_number': '1:25-cv-00XXX',
            'court': 'D.R.I.',
            'filing_date': '2025-03-01',
            'current_status': 'Resolved - Plaintiff Victory',
            'outcome': 'NEA gender ideology certification requirement struck down Sept 19, 2025',
            'plaintiffs': json.dumps(['Rhode Island Latino Arts']),
            'defendants': json.dumps(['National Endowment for the Arts']),
            'main_tracker_ref': 'lit-rila-v-nea'
        },
        {
            'case_name': 'Harvard et al. v. DHS',
            'case_number': '1:25-cv-00XXX',
            'court': 'D. Mass.',
            'filing_date': '2025-04-20',
            'current_status': 'Preliminary Injunction Granted',
            'outcome': 'International student ban enjoined pending trial',
            'plaintiffs': json.dumps(['Harvard University', 'MIT']),
            'defendants': json.dumps(['Department of Homeland Security', 'Department of State']),
            'main_tracker_ref': 'harvard-v-dhs-student-visa-2025'
        },
        {
            'case_name': 'NPR v. Trump',
            'case_number': '1:25-cv-00XXX',
            'court': 'D.D.C.',
            'filing_date': '2025-05-20',
            'current_status': 'Pending',
            'outcome': None,
            'plaintiffs': json.dumps(['National Public Radio', 'PBS', 'NPR Member Stations']),
            'defendants': json.dumps(['Donald J. Trump', 'Corporation for Public Broadcasting']),
            'main_tracker_ref': 'lit-npr-v-trump'
        },
        {
            'case_name': 'ALA v. Sonderling (IMLS Grant Challenge)',
            'case_number': '1:25-cv-00XXX',
            'court': 'D.D.C.',
            'filing_date': '2025-03-01',
            'current_status': 'Pending',
            'outcome': None,
            'plaintiffs': json.dumps(['American Library Association', 'National Tribal Libraries Association']),
            'defendants': json.dumps(['IMLS Acting Director']),
            'main_tracker_ref': 'lit-ala-v-imls'
        },
        {
            'case_name': 'State Humanities Councils v. NEH',
            'case_number': '1:25-cv-00XXX',
            'court': 'D.D.C.',
            'filing_date': '2025-03-15',
            'current_status': 'Partial Ruling - Grants Unlawfully Terminated',
            'outcome': 'Court ruled grant terminations violated APA',
            'plaintiffs': json.dumps(['Federation of State Humanities Councils']),
            'defendants': json.dumps(['National Endowment for the Humanities']),
            'main_tracker_ref': 'lit-shc-v-neh'
        },
    ]

    for case in litigation_data:
        cursor.execute('''
            INSERT INTO litigation
            (case_name, case_number, court, filing_date, current_status, outcome,
             plaintiffs, defendants, main_tracker_ref)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            case['case_name'],
            case.get('case_number'),
            case.get('court'),
            case.get('filing_date'),
            case.get('current_status'),
            case.get('outcome'),
            case.get('plaintiffs'),
            case.get('defendants'),
            case.get('main_tracker_ref')
        ))

    conn.commit()


def generate_report(conn):
    """Generate a summary report of nonprofit threats."""
    cursor = conn.cursor()

    print("\n" + "="*80)
    print("TCKC NONPROFIT THREAT TRACKER - INTEGRATED REPORT")
    print("="*80)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Summary statistics
    cursor.execute('SELECT COUNT(*) FROM actions WHERE threat_level = "SEVERE"')
    severe_actions = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM targets WHERE threat_level = "SEVERE"')
    severe_targets = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM targets')
    total_targets = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM actions')
    total_actions = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM litigation WHERE current_status NOT LIKE "%Resolved%"')
    active_litigation = cursor.fetchone()[0]

    print(f"\n📊 SUMMARY STATISTICS")
    print(f"   Total Actions Tracked: {total_actions}")
    print(f"   SEVERE Threat Actions: {severe_actions}")
    print(f"   Total Organizations Targeted: {total_targets}")
    print(f"   SEVERE Threat Targets: {severe_targets}")
    print(f"   Active Litigation: {active_litigation}")

    # Actions by threat level
    print(f"\n📋 ACTIONS BY THREAT LEVEL")
    cursor.execute('''
        SELECT threat_level, COUNT(*) as count
        FROM actions
        GROUP BY threat_level
        ORDER BY
            CASE threat_level
                WHEN 'SEVERE' THEN 1
                WHEN 'HARMFUL' THEN 2
                WHEN 'WATCH' THEN 3
                ELSE 4
            END
    ''')
    for row in cursor.fetchall():
        print(f"   {row[0]}: {row[1]}")

    # Most affected communities
    print(f"\n🏛️ MOST AFFECTED COMMUNITIES (by action count)")
    cursor.execute('''
        SELECT cc.community_name, COUNT(*) as impact_count
        FROM action_community_impacts aci
        JOIN cultural_communities cc ON aci.community_id = cc.id
        GROUP BY cc.community_name
        ORDER BY impact_count DESC
        LIMIT 10
    ''')
    for row in cursor.fetchall():
        print(f"   {row[0]}: {row[1]} actions")

    # Severe targets
    print(f"\n🎯 ORGANIZATIONS UNDER SEVERE THREAT")
    cursor.execute('''
        SELECT entity_name, threat_nature, official_source
        FROM targets
        WHERE threat_level = "SEVERE"
        ORDER BY date_first_targeted
    ''')
    for row in cursor.fetchall():
        print(f"   • {row[0]}")
        print(f"     Threat: {row[1][:60]}...")
        print(f"     Source: {row[2]}")

    # Active litigation
    print(f"\n⚖️ ACTIVE LITIGATION")
    cursor.execute('''
        SELECT case_name, court, current_status
        FROM litigation
        WHERE current_status NOT LIKE "%Resolved%"
        ORDER BY filing_date DESC
    ''')
    for row in cursor.fetchall():
        print(f"   • {row[0]} ({row[1]})")
        print(f"     Status: {row[2]}")

    # Recent timeline
    print(f"\n📅 RECENT TIMELINE EVENTS")
    cursor.execute('''
        SELECT event_date, event_type, title
        FROM timeline_events
        ORDER BY event_date DESC
        LIMIT 10
    ''')
    for row in cursor.fetchall():
        print(f"   {row[0]} | {row[1]}: {row[2]}")

    print("\n" + "="*80)


def export_to_json(conn, output_path=None):
    """Export database to JSON for integration with main tracker."""
    if output_path is None:
        output_path = Path(__file__).parent / 'nonprofit_tracker_export.json'

    cursor = conn.cursor()

    # Export actions with community impacts
    cursor.execute('''
        SELECT a.*,
               GROUP_CONCAT(DISTINCT t.entity_name) as affected_targets
        FROM actions a
        LEFT JOIN action_targets at ON a.id = at.action_id
        LEFT JOIN targets t ON at.target_id = t.id
        GROUP BY a.id
    ''')

    columns = [desc[0] for desc in cursor.description]
    actions = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Export targets
    cursor.execute('SELECT * FROM targets')
    columns = [desc[0] for desc in cursor.description]
    targets = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Export litigation
    cursor.execute('SELECT * FROM litigation')
    columns = [desc[0] for desc in cursor.description]
    litigation = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Export timeline
    cursor.execute('SELECT * FROM timeline_events ORDER BY event_date')
    columns = [desc[0] for desc in cursor.description]
    timeline = [dict(zip(columns, row)) for row in cursor.fetchall()]

    export_data = {
        'metadata': {
            'title': 'TCKC Nonprofit Threat Tracker - Integrated Export',
            'exported_at': datetime.now().isoformat(),
            'source': 'nonprofit_tracker_integrated.py',
            'main_tracker_integration': True
        },
        'summary': {
            'total_actions': len(actions),
            'total_targets': len(targets),
            'active_litigation': sum(1 for l in litigation if 'Resolved' not in (l.get('current_status') or '')),
            'severe_threats': sum(1 for a in actions if a.get('threat_level') == 'SEVERE')
        },
        'actions': actions,
        'targets': targets,
        'litigation': litigation,
        'timeline': timeline
    }

    with open(output_path, 'w') as f:
        json.dump(export_data, f, indent=2, default=str)

    print(f"\n✅ Exported to {output_path}")
    return export_data


def main():
    """Main entry point."""
    print("Initializing TCKC Nonprofit Threat Tracker (Integrated Edition)...")

    conn = init_db()

    print("Populating cultural communities...")
    populate_cultural_communities(conn)

    print("Populating actions from main tracker and expanded sources...")
    populate_actions(conn)

    print("Populating targeted organizations...")
    populate_targets(conn)

    print("Linking actions to targets...")
    populate_action_targets(conn)

    print("Populating community impacts (4Ps framework)...")
    populate_community_impacts(conn)

    print("Populating timeline events...")
    populate_timeline_events(conn)

    print("Populating litigation tracking...")
    populate_litigation(conn)

    # Generate report
    generate_report(conn)

    # Export to JSON
    export_to_json(conn)

    conn.close()

    print(f"\n✅ Database created at: {DB_PATH}")
    print("Run this script again to update with latest data.")


if __name__ == '__main__':
    main()
