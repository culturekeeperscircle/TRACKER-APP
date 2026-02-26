"""Entry schema definitions for reference."""

ENTRY_SCHEMA = {
    'i': 'Unique ID (string) — use "id" for legislation category',
    't': 'Document type (string) — e.g., "Executive Order", "Public Law"',
    'n': 'Number/designation (string) — e.g., "EO 13933", "P.L. 117-169"',
    'T': 'Full title with HTML color span (string)',
    's': 'Short summary slug (string, 2-5 words)',
    'd': 'Date (string, YYYY-MM-DD)',
    'a': 'Administration (string) — "Trump I", "Trump II", "Biden", "Obama"',
    'A': 'Agencies (array of abbreviation strings)',
    'S': 'Status description (string)',
    'L': 'Threat level (string) — "SEVERE", "HARMFUL", or "PROTECTIVE"',
    'D': 'Detailed description (string, 500-1500 words)',
    'I': 'Impact analysis (object) — community keys → 4P fields',
    'c': 'Communities affected (array of strings)',
}

OPTIONAL_FIELDS = {
    '_source': 'Data source tag',
    'agencyMandates': 'Agency-specific requirements (object)',
    'keyQuotes': 'Direct quotes (array of strings)',
    'impactByCommunity': 'Severity per community (object)',
}

IMPACT_4P_FIELDS = ['people', 'places', 'practices', 'treasures']

COMMUNITIES = [
    'Indigenous/Tribal', 'African-descendant', 'Latiné', 'Asian American',
    'Pacific Islander', 'Alaska Native', 'Native Hawaiian', 'Immigrant',
    'LGBTQ+', 'Women', 'Disabled', 'Muslim', 'Rural', 'Urban',
    'Arts community', 'Environmental justice', 'Low-income', 'All communities',
]

AGENCY_CODES = {
    'DOI': 'Department of the Interior',
    'DOJ': 'Department of Justice',
    'DHS': 'Department of Homeland Security',
    'EPA': 'Environmental Protection Agency',
    'ED': 'Department of Education',
    'HHS': 'Department of Health and Human Services',
    'USDA': 'Department of Agriculture',
    'DOD': 'Department of Defense',
    'STATE': 'Department of State',
    'HUD': 'Department of Housing and Urban Development',
    'NEA': 'National Endowment for the Arts',
    'NEH': 'National Endowment for the Humanities',
    'IMLS': 'Institute of Museum and Library Services',
    'Smithsonian': 'Smithsonian Institution',
    'NPS': 'National Park Service',
    'BIA': 'Bureau of Indian Affairs',
    'ACHP': 'Advisory Council on Historic Preservation',
    'CEQ': 'Council on Environmental Quality',
    'CPB': 'Corporation for Public Broadcasting',
    'GSA': 'General Services Administration',
    'OMB': 'Office of Management and Budget',
    'ICE': 'Immigration and Customs Enforcement',
    'CBP': 'Customs and Border Protection',
    'USCIS': 'U.S. Citizenship and Immigration Services',
}
