"""Pipeline configuration — reads API keys from environment variables."""
import os
from datetime import date, timedelta

# API Keys (set via GitHub Secrets or local env)
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
    # Cultural life — foodways, landways, arts, celebrations, programming
    'foodways', 'landways', 'folk arts', 'cultural arts', 'performing arts',
    'parade', 'celebration', 'festival', 'ceremony', 'cultural event',
    'cultural programming', 'cultural center', 'community center',
    # Education & knowledge institutions
    'school', 'university', 'college', 'museum', 'library', 'archive',
    'curriculum', 'Title I', 'Title IX', 'student', 'scholarship',
    'tribal college', 'community college', 'head start',
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
