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
# Monday (weekday 0) looks back 4 days to cover Fri+Sat+Sun+Mon
# All other days look back 2 days for overlap safety
_default_lookback = 4 if date.today().weekday() == 0 else 2
LOOKBACK_DAYS = int(os.environ.get('LOOKBACK_DAYS', str(_default_lookback)))
DRY_RUN = os.environ.get('DRY_RUN', 'false').lower() == 'true'
SOURCE_FILTER = os.environ.get('SOURCE_FILTER', 'all')

# Claude models
CLAUDE_SCREENING_MODEL = 'claude-haiku-4-5-20251001'
CLAUDE_GENERATION_MODEL = 'claude-sonnet-4-6'
CLAUDE_VALIDATION_MODEL = 'claude-haiku-4-5-20251001'

# Relevance keywords for pre-filtering
RELEVANCE_KEYWORDS = [
    'cultural resource', 'historic preservation', 'heritage', 'monument', 'museum',
    'archaeological', 'sacred site', 'burial ground', 'NAGPRA', 'NHPA', 'Section 106',
    'National Register', 'historic district', 'tribal', 'indigenous', 'Native American',
    'Alaska Native', 'treaty', 'sovereignty', 'reservation', 'BIA',
    'civil rights', 'DEI', 'environmental justice', 'Title VI', 'discrimination', 'equity',
    'immigration', 'refugee', 'asylum', 'deportation', 'TPS', 'visa', 'ICE', 'DACA',
    'climate change', 'EPA', 'NEPA', 'environmental review', 'conservation',
    'endangered species', 'public lands', 'national park',
    'education', 'NEA', 'NEH', 'Smithsonian', 'library', 'arts funding',
    'public broadcasting', 'CPB', 'PBS', 'NPR', 'IMLS',
    'African American', 'Latino', 'Latiné', 'Asian American', 'Pacific Islander',
    'Native Hawaiian', 'LGBTQ', 'disability', 'women', 'Muslim',
]

# Federal Register agencies of interest
FED_REG_AGENCIES = [
    'interior-department', 'environmental-protection-agency', 'agriculture-department',
    'justice-department', 'homeland-security-department', 'state-department',
    'education-department', 'health-and-human-services-department',
    'housing-and-urban-development-department', 'defense-department',
    'council-on-environmental-quality', 'advisory-council-on-historic-preservation',
    'national-endowment-for-the-arts', 'national-endowment-for-the-humanities',
    'institute-of-museum-and-library-services', 'smithsonian-institution',
    'corporation-for-public-broadcasting', 'executive-office-of-the-president',
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
