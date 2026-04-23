"""Pipeline configuration — reads API keys from environment variables."""
import os
from datetime import date, timedelta
from pathlib import Path

# Load API keys from a project-local .env file if present (never committed; see .gitignore).
# Shell exports and GitHub Actions secrets still win because load_dotenv does not override.
try:
    from dotenv import load_dotenv
    _ENV_PATH = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(_ENV_PATH, override=False)
except ImportError:
    pass  # dotenv optional; falls through to raw os.environ

# API Keys (set via GitHub Secrets, shell env, or local .env)
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
CONGRESS_API_KEY = os.environ.get('CONGRESS_API_KEY', '')
COURTLISTENER_TOKEN = os.environ.get('COURTLISTENER_TOKEN', '')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY', '')

# Paths
DATA_JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')
STATE_JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'state.json')
INDEX_HTML_PATH = os.path.join(os.path.dirname(__file__), '..', 'index.html')
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), 'prompts')

# Pipeline settings
# Default lookback is only used when no last_successful_run exists in state.json.
# The pipeline will dynamically calculate since_date from state.json instead.
LOOKBACK_DAYS = int(os.environ.get('LOOKBACK_DAYS', '0'))  # 0 = use state.json
DRY_RUN = os.environ.get('DRY_RUN', 'false').lower() == 'true'
SOURCE_FILTER = os.environ.get('SOURCE_FILTER', 'all')

# Claude models
CLAUDE_SCREENING_MODEL = 'claude-haiku-4-5-20251001'
CLAUDE_GENERATION_MODEL = 'claude-sonnet-4-6'
CLAUDE_VALIDATION_MODEL = 'claude-haiku-4-5-20251001'

# Relevance keywords for pre-filtering — ethnic communities + cultural heritage/practice
RELEVANCE_KEYWORDS = [
    # Cultural heritage & preservation
    'cultural resource', 'cultural heritage', 'cultural practice', 'cultural property',
    'cultural tradition', 'cultural identity', 'intangible heritage',
    'historic preservation', 'heritage', 'monument', 'museum', 'memorial',
    'archaeological', 'sacred site', 'burial ground', 'cemetery', 'historic site',
    'NAGPRA', 'NHPA', 'Section 106', 'National Register', 'historic district',
    'Antiquities Act', 'historic landmark', 'World Heritage',
    # Indigenous / Tribal
    'tribal', 'indigenous', 'Native American', 'Alaska Native', 'Native Hawaiian',
    'treaty', 'sovereignty', 'reservation', 'BIA', 'Indian Affairs',
    'tribal consultation', 'tribal land', 'First Nations', 'aboriginal',
    # African-descendant
    'African American', 'Black community', 'Black history', 'civil rights',
    'racial justice', 'racial equity', 'reparations', 'Juneteenth',
    'historically Black', 'HBCU', 'African diaspora', 'Afro-',
    # Latiné / Hispanic
    'Latino', 'Latina', 'Latiné', 'Latinx', 'Hispanic', 'Chicano', 'Chicana',
    'farmworker', 'bracero', 'Spanish-speaking', 'Latin American',
    # Asian American / Pacific Islander
    'Asian American', 'Pacific Islander', 'AAPI', 'AANHPI',
    'Chinese American', 'Japanese American', 'Korean American',
    'Filipino', 'Vietnamese', 'South Asian', 'Southeast Asian', 'Polynesian',
    # Other ethnic / identity communities
    'LGBTQ', 'disability', 'women', 'Muslim', 'Jewish', 'Sikh', 'Hindu',
    'Arab American', 'Middle Eastern', 'immigrant community', 'refugee community',
    'Garifuna', 'Tamil', 'Tamil American',
    # Heritage months & recognition resolutions
    'heritage month', 'history month', 'recognition month', 'awareness month',
    'National Day of', 'commemorat', 'designat',
    'Black History', 'African American History', 'Filipino American History',
    'Native Hawaiian', 'Asian Pacific American Heritage', 'AANHPI Heritage',
    'Hispanic Heritage', 'Arab American Heritage', 'Indigenous Peoples Day',
    'Juneteenth National Independence Day',
    # Specific bill topics to track
    'official language', 'English language', 'English-only', 'national language',
    'language access', 'multilingual', 'bilingual', 'interpreter', 'translation',
    'reproductive rights', 'reproductive health', 'contraception', 'abortion',
    'maternal health', 'birth equity',
    'worker rights', 'labor rights',  'wage theft', 'workplace safety',
    'fair scheduling', 'domestic workers', 'gig workers',
    'Kennedy Center', 'National Museum', 'Smithsonian museum',
    'African American Museum', 'Latino Museum', 'Women\'s History Museum',
    'Asian Pacific American', 'American Indian Museum',
    # Civil rights & equity
    'DEI', 'environmental justice', 'Title VI', 'discrimination', 'equity',
    'hate crime', 'civil liberties', 'equal protection', 'voting rights',
    # Immigration
    'immigration', 'refugee', 'asylum', 'deportation', 'TPS', 'visa', 'ICE', 'DACA',
    'naturalization', 'USCIS', 'border', 'migrant',
    # Environment & land
    'climate change', 'EPA', 'NEPA', 'environmental review', 'conservation',
    'endangered species', 'public lands', 'national park', 'wilderness',
    'clean water', 'clean air', 'environmental protection',
    # Arts, education, cultural institutions
    'education', 'NEA', 'NEH', 'Smithsonian', 'library', 'arts funding',
    'public broadcasting', 'CPB', 'PBS', 'NPR', 'IMLS',
    'arts community', 'cultural institution', 'humanities', 'folk art',
    'language preservation', 'oral history', 'traditional knowledge',
    'arts education', 'creative workforce', 'cultural funding', 'arts grant',
    'National Endowment', 'Corporation for Public Broadcasting',
    # Cultural life — foodways, landways, arts, celebrations, programming
    'foodways', 'landways', 'folk arts', 'cultural arts', 'performing arts',
    'parade', 'celebration', 'festival', 'ceremony', 'cultural event',
    'cultural programming', 'cultural center', 'community center',
    # Education & knowledge institutions
    'school', 'university', 'college', 'museum', 'library', 'archive',
    'curriculum', 'Title I', 'Title IX', 'student', 'scholarship',
    'tribal college', 'community college', 'head start',
]

# Tracked bill numbers — these specific bills should always pass keyword filter
# when they appear in Congress.gov results (matched by source_id)
TRACKED_BILLS = [
    # Black History & African American Heritage
    'HR1359-119', 'HR844-119', 'HR7549-118', 'SRES99-119', 'HR1817-119',
    'HRES766-118', 'HRES1080-118', 'HRES1088-118', 'S3953-118',
    # Filipino American
    'SRES423-118', 'HRES774-118',
    # Native Hawaiian
    'HRES787-118', 'SRES419-118', 'SRES83-119', 'HRES136-119', 'SRES625-118',
    # Indigenous Peoples
    'HRES809-118', 'SRES450-118', 'HRES911-118', 'SRES501-118',
    # AANHPI
    'SRES214-119', 'HRES400-119', 'S1844-119', 'HR3551-119',
    # Latiné Heritage
    'HRES261-119', 'SRES144-119', 'SRES428-118',
    # Arab American / Garifuna / Tamil
    'HRES351-119', 'HRES288-119', 'HRES41-119',
    # Smithsonian Museums
    'S1303-119',
    # Immigration
    'HR6149-118', 'HR2851-119', 'HRES909-118', 'S3702-118',
    'HR6397-118', 'HR3101-119', 'HR1680-119', 'HR4393-119', 'S391-119',
    # Reproductive Rights
    'S422-119', 'HR999-119', 'HCONRES65-118',
    # Workers' Rights
    'HR3971-119', 'S3396-118',
    # Voting Rights
    'S2589-119', 'HR4917-119',
    # Language Rights
    'HR1572-119', 'HR1772-119', 'HR1862-119', 'S542-119',
    'HR1660-119', 'HR3728-119', 'HRES804-118', 'HRES149-119', 'HR3238-119',
    # Equality
    'HR4373-119',
    # International
    'HR2416-119', 'S2224-119',
    # Arts/Education/Cultural Funding
    'HR82-119', 'HR2485-119', 'HR5399-118', 'HR3852-119',
    'HR5009-119', 'HR4754-119', 'S2431-119', 'HR6165-118',
    # Kennedy Center
    'HR6925-118', 'HRES973-118',
]

# Administration mapping
def get_administration(date_str):
    """Determine administration based on date."""
    d = date.fromisoformat(date_str) if isinstance(date_str, str) else date_str
    if d >= date(2025, 1, 20):
        return 'Trump II'
    elif d >= date(2021, 1, 20):
        return 'Biden'
    elif d >= date(2017, 1, 20):
        return 'Trump I'
    else:
        return 'Obama'
