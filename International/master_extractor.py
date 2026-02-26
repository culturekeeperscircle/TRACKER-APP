#!/usr/bin/env python3
"""
================================================================================
INTERNATIONAL OBLIGATIONS DATA EXTRACTOR
================================================================================
Master Script for Extracting Data from International Organizations

Designed for: The Culture Keepers Threat Tracker™
Purpose: Pull treaty obligations, disputes, and policy data that affect U.S. 
         cultural, environmental, and heritage institutions

Data Sources:
- WTO: Trade disputes affecting cultural goods/services
- IMF: Economic data affecting funding
- World Bank: Development indicators and project data  
- UN: Security Council resolutions and treaty data
- ICJ: International court cases involving the U.S.
- NATO: Official texts and communiqués

Author: Generated for TCKC Threat Tracker Integration
================================================================================
"""

import os
import json
import sqlite3
import logging
import time
import csv
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from pathlib import Path
from io import StringIO
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    handlers=[
        logging.FileHandler('extraction.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('IntlExtractor')

# =============================================================================
# TRY IMPORTS - Handle missing dependencies gracefully
# =============================================================================
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    logger.warning("requests library not available - install with: pip install requests")

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    logger.warning("beautifulsoup4 not available - install with: pip install beautifulsoup4")

# =============================================================================
# CONFIGURATION
# =============================================================================
@dataclass
class ExtractorConfig:
    """Configuration for the data extractor."""
    
    # API Keys (set via environment variables)
    wto_api_key: str = field(default_factory=lambda: os.getenv('WTO_API_KEY', ''))
    
    # Database
    database_path: str = './data/intl_obligations.db'
    
    # Rate limiting (seconds between requests)
    wto_rate_limit: float = 1.0
    imf_rate_limit: float = 0.5
    world_bank_rate_limit: float = 1.0
    un_rate_limit: float = 0.5
    icj_rate_limit: float = 0.3
    nato_rate_limit: float = 0.3
    
    # Time range for data collection
    start_year: int = 2020
    end_year: int = 2025
    
    # Countries of interest (ISO codes)
    countries_iso3: List[str] = field(default_factory=lambda: ['USA'])
    countries_iso2: List[str] = field(default_factory=lambda: ['US'])
    
    # Keywords relevant to cultural/heritage tracking
    cultural_keywords: List[str] = field(default_factory=lambda: [
        'cultural', 'heritage', 'museum', 'art', 'artifact',
        'indigenous', 'tribal', 'native', 'archaeological',
        'monument', 'preservation', 'repatriation', 'NAGPRA',
        'UNESCO', 'intellectual property', 'copyright',
        'broadcast', 'media', 'education', 'library',
        'environment', 'climate', 'conservation', 'wildlife',
        'national park', 'public land', 'sanctuary'
    ])

# =============================================================================
# API ENDPOINTS
# =============================================================================
class APIEndpoints:
    """Central registry of API endpoints."""
    
    # WTO
    WTO_BASE = "https://api.wto.org/timeseries/v1"
    WTO_DATA = f"{WTO_BASE}/data"
    WTO_INDICATORS = f"{WTO_BASE}/indicators"
    WTO_REPORTERS = f"{WTO_BASE}/reporters"
    
    # IMF
    IMF_BASE = "https://dataservices.imf.org/REST/SDMX_JSON.svc"
    IMF_DATAFLOW = f"{IMF_BASE}/Dataflow"
    IMF_DATA = f"{IMF_BASE}/CompactData"
    
    # World Bank
    WB_BASE = "https://api.worldbank.org/v2"
    WB_INDICATORS = f"{WB_BASE}/indicator"
    WB_COUNTRIES = f"{WB_BASE}/country"
    
    # UN
    UN_DATA = "http://data.un.org/ws/rest"
    UN_DIGITAL_LIBRARY = "https://digitallibrary.un.org"
    
    # Zenodo (for academic datasets)
    ZENODO_API = "https://zenodo.org/api/records"
    ZENODO_UNSC_CORPUS = "11212056"  # CR-UNSC corpus
    ZENODO_ICJ_CORPUS = "3826444"    # CD-ICJ corpus
    
    # ICJ
    ICJ_BASE = "https://www.icj-cij.org"
    
    # NATO
    NATO_BASE = "https://www.nato.int"

# =============================================================================
# DATABASE MANAGER
# =============================================================================
class DatabaseManager:
    """Manages SQLite database for storing extracted data."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()
    
    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _init_schema(self):
        """Initialize database schema."""
        conn = self._get_conn()
        cursor = conn.cursor()
        
        # WTO Trade Data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS wto_trade_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                indicator_code TEXT,
                indicator_name TEXT,
                reporter_code TEXT,
                reporter_name TEXT,
                partner_code TEXT,
                product_code TEXT,
                year INTEGER,
                value REAL,
                unit TEXT,
                relevance_tags TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(indicator_code, reporter_code, partner_code, product_code, year)
            )
        """)
        
        # WTO Disputes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS wto_disputes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dispute_number TEXT UNIQUE,
                title TEXT,
                complainant TEXT,
                respondent TEXT,
                third_parties TEXT,
                status TEXT,
                date_initiated DATE,
                subject_matter TEXT,
                cultural_relevance TEXT,
                url TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # IMF Data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS imf_economic_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dataset TEXT,
                indicator_code TEXT,
                indicator_name TEXT,
                country_code TEXT,
                country_name TEXT,
                year INTEGER,
                period TEXT,
                value REAL,
                unit TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(dataset, indicator_code, country_code, year, period)
            )
        """)
        
        # World Bank Indicators
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS world_bank_indicators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                indicator_code TEXT,
                indicator_name TEXT,
                country_code TEXT,
                country_name TEXT,
                year INTEGER,
                value REAL,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(indicator_code, country_code, year)
            )
        """)
        
        # UN Security Council Resolutions
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unsc_resolutions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                resolution_number TEXT UNIQUE,
                title TEXT,
                date_adopted DATE,
                vote_for INTEGER,
                vote_against INTEGER,
                vote_abstain INTEGER,
                topics TEXT,
                summary TEXT,
                us_relevance TEXT,
                cultural_relevance TEXT,
                document_url TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # ICJ Cases
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS icj_cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_number TEXT UNIQUE,
                case_name TEXT,
                case_type TEXT,
                applicant TEXT,
                respondent TEXT,
                date_filed DATE,
                date_decided DATE,
                status TEXT,
                subject_matter TEXT,
                us_involvement TEXT,
                cultural_relevance TEXT,
                outcome TEXT,
                url TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # NATO Documents
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nato_documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id TEXT UNIQUE,
                document_type TEXT,
                title TEXT,
                date_published DATE,
                summary TEXT,
                us_relevance TEXT,
                url TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Treaties and Agreements (cross-reference)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS treaties_obligations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                treaty_name TEXT,
                organization TEXT,
                date_signed DATE,
                date_effective DATE,
                us_status TEXT,
                subject_areas TEXT,
                cultural_heritage_relevance TEXT,
                environmental_relevance TEXT,
                summary TEXT,
                source_url TEXT,
                extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Extraction Log
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS extraction_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                extraction_type TEXT,
                started_at TIMESTAMP,
                completed_at TIMESTAMP,
                records_extracted INTEGER DEFAULT 0,
                status TEXT,
                error_message TEXT
            )
        """)
        
        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_wto_year ON wto_trade_data(year)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_imf_country ON imf_economic_data(country_code)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_unsc_date ON unsc_resolutions(date_adopted)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_icj_us ON icj_cases(us_involvement)")
        
        conn.commit()
        conn.close()
        logger.info(f"Database initialized at {self.db_path}")
    
    def insert_many(self, table: str, records: List[Dict]) -> int:
        """Insert multiple records, ignoring duplicates."""
        if not records:
            return 0
        
        conn = self._get_conn()
        cursor = conn.cursor()
        
        columns = list(records[0].keys())
        placeholders = ','.join(['?' for _ in columns])
        column_str = ','.join(columns)
        
        inserted = 0
        for record in records:
            try:
                cursor.execute(
                    f"INSERT OR REPLACE INTO {table} ({column_str}) VALUES ({placeholders})",
                    [record.get(col) for col in columns]
                )
                inserted += 1
            except Exception as e:
                logger.warning(f"Insert failed: {e}")
        
        conn.commit()
        conn.close()
        return inserted
    
    def query(self, sql: str, params: tuple = None) -> List[Dict]:
        """Execute a query and return results."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        columns = [d[0] for d in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return results
    
    def log_extraction(self, source: str, extraction_type: str) -> int:
        """Log start of extraction, return log ID."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO extraction_log (source, extraction_type, started_at, status) VALUES (?, ?, ?, ?)",
            (source, extraction_type, datetime.now().isoformat(), 'running')
        )
        log_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return log_id
    
    def complete_extraction(self, log_id: int, records: int, status: str = 'success', error: str = None):
        """Log completion of extraction."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE extraction_log 
               SET completed_at = ?, records_extracted = ?, status = ?, error_message = ?
               WHERE id = ?""",
            (datetime.now().isoformat(), records, status, error, log_id)
        )
        conn.commit()
        conn.close()

# =============================================================================
# HTTP CLIENT WITH RATE LIMITING
# =============================================================================
class RateLimitedClient:
    """HTTP client with built-in rate limiting."""
    
    def __init__(self, rate_limit: float = 1.0):
        self.rate_limit = rate_limit
        self.last_request = 0
        self.session = requests.Session() if REQUESTS_AVAILABLE else None
        
        if self.session:
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,application/json,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
            })
    
    def _wait(self):
        """Wait if necessary to respect rate limits."""
        if self.rate_limit > 0:
            elapsed = time.time() - self.last_request
            if elapsed < self.rate_limit:
                time.sleep(self.rate_limit - elapsed)
        self.last_request = time.time()
    
    def get(self, url: str, params: Dict = None, headers: Dict = None, 
            timeout: int = 30, retries: int = 3) -> Optional[requests.Response]:
        """Make a GET request with rate limiting and retries."""
        if not self.session:
            logger.error("requests library not available")
            return None
        
        self._wait()
        
        for attempt in range(retries):
            try:
                response = self.session.get(
                    url, params=params, headers=headers, timeout=timeout
                )
                
                if response.status_code == 429:  # Rate limited
                    wait = int(response.headers.get('Retry-After', 60))
                    logger.warning(f"Rate limited, waiting {wait}s")
                    time.sleep(wait)
                    continue
                
                response.raise_for_status()
                return response
                
            except Exception as e:
                logger.warning(f"Request failed (attempt {attempt + 1}): {e}")
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
        
        return None
    
    def get_json(self, url: str, params: Dict = None, headers: Dict = None) -> Optional[Dict]:
        """Make a GET request and return JSON."""
        response = self.get(url, params=params, headers=headers)
        if response:
            try:
                return response.json()
            except:
                pass
        return None

# =============================================================================
# BASE EXTRACTOR CLASS
# =============================================================================
class BaseExtractor(ABC):
    """Base class for all data extractors."""
    
    def __init__(self, config: ExtractorConfig, db: DatabaseManager):
        self.config = config
        self.db = db
        self.client = RateLimitedClient(self.rate_limit)
    
    @property
    @abstractmethod
    def source_name(self) -> str:
        """Name of the data source."""
        pass
    
    @property
    @abstractmethod
    def rate_limit(self) -> float:
        """Rate limit in seconds."""
        pass
    
    @abstractmethod
    def extract(self) -> Dict[str, Any]:
        """Main extraction method."""
        pass
    
    def is_culturally_relevant(self, text: str) -> Tuple[bool, List[str]]:
        """Check if text contains culturally relevant keywords."""
        if not text:
            return False, []
        
        text_lower = text.lower()
        matches = [kw for kw in self.config.cultural_keywords if kw.lower() in text_lower]
        return len(matches) > 0, matches

# =============================================================================
# WTO EXTRACTOR
# =============================================================================
class WTOExtractor(BaseExtractor):
    """Extractor for WTO data."""
    
    @property
    def source_name(self) -> str:
        return 'WTO'
    
    @property
    def rate_limit(self) -> float:
        return self.config.wto_rate_limit
    
    def extract(self) -> Dict[str, Any]:
        """Extract WTO data."""
        log_id = self.db.log_extraction(self.source_name, 'full')
        total_records = 0
        
        try:
            # Extract trade data (requires API key)
            if self.config.wto_api_key:
                records = self._extract_trade_data()
                total_records += records
            else:
                logger.warning("WTO API key not set - skipping trade data")
            
            # Extract disputes (web scraping, no key needed)
            records = self._extract_disputes()
            total_records += records
            
            self.db.complete_extraction(log_id, total_records)
            
        except Exception as e:
            logger.error(f"WTO extraction failed: {e}")
            self.db.complete_extraction(log_id, total_records, 'error', str(e))
        
        return {'source': 'WTO', 'records': total_records}
    
    def _extract_trade_data(self) -> int:
        """Extract trade statistics from WTO API."""
        logger.info("Extracting WTO trade data...")
        
        # Cultural goods indicators (HS codes for art, antiques, etc.)
        indicators = [
            'HS_M_0097',  # Art/antiques imports
            'HS_X_0097',  # Art/antiques exports
            'HS_M_0049',  # Books/publications imports
            'HS_X_0049',  # Books/publications exports
        ]
        
        records = []
        headers = {'Ocp-Apim-Subscription-Key': self.config.wto_api_key}
        
        for indicator in indicators:
            for country in self.config.countries_iso3:
                url = APIEndpoints.WTO_DATA
                params = {
                    'i': indicator,
                    'r': country,
                    'ps': f'{self.config.start_year}-{self.config.end_year}',
                    'fmt': 'json',
                    'mode': 'full'
                }
                
                data = self.client.get_json(url, params=params, headers=headers)
                
                if data and 'Dataset' in data:
                    for item in data['Dataset']:
                        is_relevant, tags = self.is_culturally_relevant(
                            item.get('ProductSector', '')
                        )
                        
                        records.append({
                            'indicator_code': indicator,
                            'indicator_name': item.get('IndicatorName'),
                            'reporter_code': item.get('ReportingEconomyCode'),
                            'reporter_name': item.get('ReportingEconomy'),
                            'partner_code': item.get('PartnerEconomyCode'),
                            'product_code': item.get('ProductSectorCode'),
                            'year': item.get('Year'),
                            'value': item.get('Value'),
                            'unit': item.get('Unit'),
                            'relevance_tags': ','.join(tags) if tags else None
                        })
        
        inserted = self.db.insert_many('wto_trade_data', records)
        logger.info(f"Inserted {inserted} WTO trade records")
        return inserted
    
    def _extract_disputes(self) -> int:
        """Extract WTO dispute data via web scraping."""
        if not BS4_AVAILABLE:
            logger.warning("BeautifulSoup not available - skipping WTO disputes")
            return 0
        
        logger.info("Extracting WTO disputes...")
        
        # WTO dispute settlement database URL
        base_url = "https://www.wto.org/english/tratop_e/dispu_e"
        
        # US-specific disputes
        us_disputes = []
        
        # Search for disputes involving the US
        search_url = f"{base_url}/dispu_by_country_e.htm"
        response = self.client.get(search_url)
        
        if not response:
            return 0
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find US section and extract dispute links
        # (WTO website structure varies - this is a simplified approach)
        dispute_links = soup.find_all('a', href=lambda x: x and 'ds' in x.lower() if x else False)
        
        records = []
        for link in dispute_links[:50]:  # Limit to recent disputes
            href = link.get('href', '')
            title = link.text.strip()
            
            # Check if US is involved
            if 'united states' in title.lower() or 'US' in title:
                is_relevant, tags = self.is_culturally_relevant(title)
                
                records.append({
                    'dispute_number': href.split('/')[-1].replace('.htm', '').upper(),
                    'title': title[:500],
                    'complainant': 'United States' if 'complainant' in title.lower() else None,
                    'respondent': 'United States' if 'respondent' in title.lower() else None,
                    'cultural_relevance': ','.join(tags) if tags else None,
                    'url': f"https://www.wto.org{href}" if href.startswith('/') else href
                })
        
        inserted = self.db.insert_many('wto_disputes', records)
        logger.info(f"Inserted {inserted} WTO disputes")
        return inserted

# =============================================================================
# IMF EXTRACTOR
# =============================================================================
class IMFExtractor(BaseExtractor):
    """Extractor for IMF data."""
    
    @property
    def source_name(self) -> str:
        return 'IMF'
    
    @property
    def rate_limit(self) -> float:
        return self.config.imf_rate_limit
    
    def extract(self) -> Dict[str, Any]:
        """Extract IMF data."""
        log_id = self.db.log_extraction(self.source_name, 'full')
        total_records = 0
        
        try:
            # Key economic indicators relevant to cultural funding
            indicators = {
                'IFS': [
                    ('NGDP_XDC', 'Nominal GDP'),
                    ('GGR_G01_XDC', 'Government Revenue'),
                    ('GGX_G01_XDC', 'Government Expenditure'),
                ],
                'WEO': [
                    ('NGDP_RPCH', 'Real GDP Growth'),
                    ('GGX_NGDP', 'Government Expenditure % GDP'),
                ]
            }
            
            for dataset, ind_list in indicators.items():
                for country in self.config.countries_iso2:
                    for indicator_code, indicator_name in ind_list:
                        records = self._fetch_series(dataset, country, indicator_code, indicator_name)
                        total_records += records
            
            self.db.complete_extraction(log_id, total_records)
            
        except Exception as e:
            logger.error(f"IMF extraction failed: {e}")
            self.db.complete_extraction(log_id, total_records, 'error', str(e))
        
        return {'source': 'IMF', 'records': total_records}
    
    def _fetch_series(self, dataset: str, country: str, 
                     indicator: str, indicator_name: str) -> int:
        """Fetch a time series from IMF API."""
        url = f"{APIEndpoints.IMF_DATA}/{dataset}/A.{country}.{indicator}"
        
        params = {
            'startPeriod': str(self.config.start_year),
            'endPeriod': str(self.config.end_year)
        }
        
        data = self.client.get_json(url, params=params)
        
        if not data:
            return 0
        
        records = []
        
        try:
            compact_data = data.get('CompactData', {})
            dataset_data = compact_data.get('DataSet', {})
            series = dataset_data.get('Series', {})
            
            if isinstance(series, dict):
                series = [series]
            
            for s in series:
                obs = s.get('Obs', [])
                if isinstance(obs, dict):
                    obs = [obs]
                
                for o in obs:
                    time_period = o.get('@TIME_PERIOD', '')
                    value = o.get('@OBS_VALUE')
                    
                    if value:
                        year = int(time_period[:4]) if len(time_period) >= 4 else None
                        
                        records.append({
                            'dataset': dataset,
                            'indicator_code': indicator,
                            'indicator_name': indicator_name,
                            'country_code': country,
                            'country_name': 'United States' if country == 'US' else country,
                            'year': year,
                            'period': time_period,
                            'value': float(value),
                            'unit': s.get('@UNIT_MULT', '')
                        })
        except Exception as e:
            logger.warning(f"Failed to parse IMF data: {e}")
        
        inserted = self.db.insert_many('imf_economic_data', records)
        return inserted

# =============================================================================
# WORLD BANK EXTRACTOR
# =============================================================================
class WorldBankExtractor(BaseExtractor):
    """Extractor for World Bank data."""
    
    @property
    def source_name(self) -> str:
        return 'World Bank'
    
    @property
    def rate_limit(self) -> float:
        return self.config.world_bank_rate_limit
    
    def extract(self) -> Dict[str, Any]:
        """Extract World Bank data."""
        log_id = self.db.log_extraction(self.source_name, 'full')
        total_records = 0
        
        try:
            # Indicators relevant to cultural/heritage funding and environment
            indicators = [
                'NY.GDP.MKTP.CD',       # GDP
                'GC.XPN.TOTL.GD.ZS',    # Government expenditure % GDP
                'SE.XPD.TOTL.GD.ZS',    # Education expenditure % GDP
                'GB.XPD.RSDV.GD.ZS',    # R&D expenditure % GDP
                'EN.ATM.CO2E.PC',       # CO2 emissions per capita
                'ER.PTD.TOTL.ZS',       # Protected terrestrial area %
                'ER.MRN.PTMR.ZS',       # Protected marine area %
                'SH.XPD.CHEX.GD.ZS',    # Health expenditure % GDP
            ]
            
            for indicator in indicators:
                for country in self.config.countries_iso3:
                    records = self._fetch_indicator(indicator, country)
                    total_records += records
            
            self.db.complete_extraction(log_id, total_records)
            
        except Exception as e:
            logger.error(f"World Bank extraction failed: {e}")
            self.db.complete_extraction(log_id, total_records, 'error', str(e))
        
        return {'source': 'World Bank', 'records': total_records}
    
    def _fetch_indicator(self, indicator: str, country: str) -> int:
        """Fetch indicator data from World Bank API."""
        url = f"{APIEndpoints.WB_BASE}/country/{country}/indicator/{indicator}"
        
        params = {
            'format': 'json',
            'date': f'{self.config.start_year}:{self.config.end_year}',
            'per_page': 100
        }
        
        data = self.client.get_json(url, params=params)
        
        if not data or not isinstance(data, list) or len(data) < 2:
            return 0
        
        records = []
        
        for item in data[1] or []:
            if item.get('value') is not None:
                records.append({
                    'indicator_code': indicator,
                    'indicator_name': item.get('indicator', {}).get('value'),
                    'country_code': item.get('countryiso3code'),
                    'country_name': item.get('country', {}).get('value'),
                    'year': int(item.get('date')) if item.get('date') else None,
                    'value': float(item.get('value'))
                })
        
        inserted = self.db.insert_many('world_bank_indicators', records)
        return inserted

# =============================================================================
# UN EXTRACTOR
# =============================================================================
class UNExtractor(BaseExtractor):
    """Extractor for UN data (UNSC Resolutions)."""
    
    @property
    def source_name(self) -> str:
        return 'UN'
    
    @property
    def rate_limit(self) -> float:
        return self.config.un_rate_limit
    
    def extract(self) -> Dict[str, Any]:
        """Extract UN data."""
        log_id = self.db.log_extraction(self.source_name, 'full')
        total_records = 0
        
        try:
            # Try Zenodo corpus first (structured data)
            records = self._extract_from_zenodo()
            total_records += records
            
            self.db.complete_extraction(log_id, total_records)
            
        except Exception as e:
            logger.error(f"UN extraction failed: {e}")
            self.db.complete_extraction(log_id, total_records, 'error', str(e))
        
        return {'source': 'UN', 'records': total_records}
    
    def _extract_from_zenodo(self) -> int:
        """Extract UNSC resolutions from Zenodo corpus."""
        logger.info("Extracting UNSC resolutions from Zenodo...")
        
        # Get Zenodo record metadata
        url = f"{APIEndpoints.ZENODO_API}/{APIEndpoints.ZENODO_UNSC_CORPUS}"
        data = self.client.get_json(url)
        
        if not data:
            logger.warning("Could not access Zenodo UNSC corpus")
            return 0
        
        # Find CSV file in the record
        files = data.get('files', [])
        csv_file = None
        
        for f in files:
            if f.get('key', '').endswith('.csv'):
                csv_file = f
                break
        
        if not csv_file:
            return 0
        
        # Download CSV
        download_url = csv_file.get('links', {}).get('self')
        if not download_url:
            return 0
        
        response = self.client.get(download_url, timeout=120)
        if not response:
            return 0
        
        # Parse CSV
        records = []
        content = response.content.decode('utf-8', errors='ignore')
        reader = csv.DictReader(StringIO(content))
        
        for row in reader:
            title = row.get('title', '')
            
            # Check US relevance
            us_relevance = None
            if 'united states' in title.lower() or 'america' in title.lower():
                us_relevance = 'mentioned'
            
            # Check cultural relevance
            is_relevant, tags = self.is_culturally_relevant(title + ' ' + row.get('subject', ''))
            
            records.append({
                'resolution_number': row.get('resolution_number') or row.get('symbol'),
                'title': title,
                'date_adopted': row.get('date') or row.get('adoption_date'),
                'vote_for': self._safe_int(row.get('vote_for') or row.get('yes')),
                'vote_against': self._safe_int(row.get('vote_against') or row.get('no')),
                'vote_abstain': self._safe_int(row.get('vote_abstain') or row.get('abstain')),
                'topics': row.get('topics') or row.get('subject'),
                'us_relevance': us_relevance,
                'cultural_relevance': ','.join(tags) if tags else None,
                'document_url': row.get('url')
            })
        
        inserted = self.db.insert_many('unsc_resolutions', records)
        logger.info(f"Inserted {inserted} UNSC resolutions")
        return inserted
    
    def _safe_int(self, val) -> Optional[int]:
        if val is None or val == '':
            return None
        try:
            return int(float(val))
        except:
            return None

# =============================================================================
# ICJ EXTRACTOR
# =============================================================================
class ICJExtractor(BaseExtractor):
    """Extractor for ICJ (International Court of Justice) data."""
    
    @property
    def source_name(self) -> str:
        return 'ICJ'
    
    @property
    def rate_limit(self) -> float:
        return self.config.icj_rate_limit
    
    def extract(self) -> Dict[str, Any]:
        """Extract ICJ data."""
        log_id = self.db.log_extraction(self.source_name, 'full')
        total_records = 0
        
        try:
            # Try Zenodo corpus first
            records = self._extract_from_zenodo()
            total_records += records
            
            self.db.complete_extraction(log_id, total_records)
            
        except Exception as e:
            logger.error(f"ICJ extraction failed: {e}")
            self.db.complete_extraction(log_id, total_records, 'error', str(e))
        
        return {'source': 'ICJ', 'records': total_records}
    
    def _extract_from_zenodo(self) -> int:
        """Extract ICJ cases from Zenodo corpus."""
        logger.info("Extracting ICJ cases from Zenodo...")
        
        url = f"{APIEndpoints.ZENODO_API}/{APIEndpoints.ZENODO_ICJ_CORPUS}"
        data = self.client.get_json(url)
        
        if not data:
            logger.warning("Could not access Zenodo ICJ corpus")
            return 0
        
        files = data.get('files', [])
        csv_file = None
        
        for f in files:
            if f.get('key', '').endswith('.csv'):
                csv_file = f
                break
        
        if not csv_file:
            return 0
        
        download_url = csv_file.get('links', {}).get('self')
        if not download_url:
            return 0
        
        response = self.client.get(download_url, timeout=120)
        if not response:
            return 0
        
        records = []
        content = response.content.decode('utf-8', errors='ignore')
        reader = csv.DictReader(StringIO(content))
        
        for row in reader:
            case_name = row.get('case_name', '') or row.get('title', '')
            applicant = row.get('applicant', '')
            respondent = row.get('respondent', '')
            
            # Check US involvement
            us_involvement = None
            if 'united states' in (applicant + respondent + case_name).lower():
                if 'united states' in applicant.lower():
                    us_involvement = 'applicant'
                elif 'united states' in respondent.lower():
                    us_involvement = 'respondent'
                else:
                    us_involvement = 'mentioned'
            
            # Check cultural relevance
            subject = row.get('subject_matter', '') or row.get('subject', '')
            is_relevant, tags = self.is_culturally_relevant(case_name + ' ' + subject)
            
            records.append({
                'case_number': row.get('case_number') or row.get('id'),
                'case_name': case_name,
                'case_type': row.get('case_type') or row.get('type'),
                'applicant': applicant,
                'respondent': respondent,
                'date_filed': row.get('date_filed') or row.get('date_instituted'),
                'date_decided': row.get('date_decided'),
                'status': row.get('status'),
                'subject_matter': subject,
                'us_involvement': us_involvement,
                'cultural_relevance': ','.join(tags) if tags else None,
                'outcome': row.get('outcome'),
                'url': row.get('url')
            })
        
        inserted = self.db.insert_many('icj_cases', records)
        logger.info(f"Inserted {inserted} ICJ cases")
        return inserted

# =============================================================================
# NATO EXTRACTOR
# =============================================================================
class NATOExtractor(BaseExtractor):
    """Extractor for NATO public documents."""
    
    @property
    def source_name(self) -> str:
        return 'NATO'
    
    @property
    def rate_limit(self) -> float:
        return self.config.nato_rate_limit
    
    def extract(self) -> Dict[str, Any]:
        """Extract NATO data via web scraping."""
        if not BS4_AVAILABLE:
            logger.warning("BeautifulSoup not available - skipping NATO")
            return {'source': 'NATO', 'records': 0}
        
        log_id = self.db.log_extraction(self.source_name, 'full')
        total_records = 0
        
        try:
            records = self._extract_communiques()
            total_records += records
            
            self.db.complete_extraction(log_id, total_records)
            
        except Exception as e:
            logger.error(f"NATO extraction failed: {e}")
            self.db.complete_extraction(log_id, total_records, 'error', str(e))
        
        return {'source': 'NATO', 'records': total_records}
    
    def _extract_communiques(self) -> int:
        """Extract NATO summit communiqués."""
        logger.info("Extracting NATO communiqués...")
        
        # NATO summit declarations page
        url = f"{APIEndpoints.NATO_BASE}/cps/en/natohq/topics_69344.htm"
        
        response = self.client.get(url)
        if not response:
            return 0
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        records = []
        links = soup.find_all('a', href=lambda x: x and 'official_texts' in x if x else False)
        
        for link in links[:30]:
            title = link.text.strip()
            href = link.get('href', '')
            
            # Check US relevance (always high for NATO)
            us_relevance = 'member_state'
            
            records.append({
                'document_id': href.split('/')[-1].replace('.htm', ''),
                'document_type': 'communique',
                'title': title[:500],
                'us_relevance': us_relevance,
                'url': f"{APIEndpoints.NATO_BASE}{href}" if href.startswith('/') else href
            })
        
        inserted = self.db.insert_many('nato_documents', records)
        logger.info(f"Inserted {inserted} NATO documents")
        return inserted

# =============================================================================
# MASTER EXTRACTOR
# =============================================================================
class MasterExtractor:
    """
    Master controller for extracting data from all international organizations.
    """
    
    def __init__(self, config: ExtractorConfig = None):
        self.config = config or ExtractorConfig()
        self.db = DatabaseManager(self.config.database_path)
        
        # Initialize extractors
        self.extractors = {
            'wto': WTOExtractor(self.config, self.db),
            'imf': IMFExtractor(self.config, self.db),
            'world_bank': WorldBankExtractor(self.config, self.db),
            'un': UNExtractor(self.config, self.db),
            'icj': ICJExtractor(self.config, self.db),
            'nato': NATOExtractor(self.config, self.db),
        }
        
        logger.info("Master Extractor initialized")
    
    def extract_all(self, sources: List[str] = None) -> Dict[str, Any]:
        """
        Extract data from all or specified sources.
        
        Args:
            sources: List of source names. If None, extracts from all.
        
        Returns:
            Dictionary with extraction results.
        """
        sources = sources or list(self.extractors.keys())
        results = {}
        
        logger.info(f"Starting extraction from: {', '.join(sources)}")
        
        for source in sources:
            if source not in self.extractors:
                logger.warning(f"Unknown source: {source}")
                continue
            
            logger.info(f"{'='*50}")
            logger.info(f"EXTRACTING FROM {source.upper()}")
            logger.info(f"{'='*50}")
            
            try:
                result = self.extractors[source].extract()
                results[source] = result
                logger.info(f"Completed {source}: {result.get('records', 0)} records")
            except Exception as e:
                logger.error(f"Failed {source}: {e}")
                results[source] = {'source': source, 'records': 0, 'error': str(e)}
        
        return results
    
    def get_us_relevant_data(self) -> Dict[str, List[Dict]]:
        """Get all data specifically relevant to the United States."""
        return {
            'wto_disputes': self.db.query(
                "SELECT * FROM wto_disputes WHERE complainant = 'United States' OR respondent = 'United States'"
            ),
            'icj_cases': self.db.query(
                "SELECT * FROM icj_cases WHERE us_involvement IS NOT NULL"
            ),
            'unsc_resolutions': self.db.query(
                "SELECT * FROM unsc_resolutions WHERE us_relevance IS NOT NULL"
            ),
            'economic_data': self.db.query(
                "SELECT * FROM imf_economic_data WHERE country_code = 'US' ORDER BY year DESC"
            ),
        }
    
    def get_culturally_relevant_data(self) -> Dict[str, List[Dict]]:
        """Get all data relevant to cultural/heritage concerns."""
        return {
            'wto_disputes': self.db.query(
                "SELECT * FROM wto_disputes WHERE cultural_relevance IS NOT NULL"
            ),
            'icj_cases': self.db.query(
                "SELECT * FROM icj_cases WHERE cultural_relevance IS NOT NULL"
            ),
            'unsc_resolutions': self.db.query(
                "SELECT * FROM unsc_resolutions WHERE cultural_relevance IS NOT NULL"
            ),
        }
    
    def export_for_threat_tracker(self, output_path: str = './exports/threat_tracker_data.json'):
        """Export data formatted for the Threat Tracker application."""
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'extracted_at': datetime.now().isoformat(),
            'us_relevant': self.get_us_relevant_data(),
            'culturally_relevant': self.get_culturally_relevant_data(),
            'economic_indicators': self.db.query(
                "SELECT * FROM world_bank_indicators WHERE country_code = 'USA' ORDER BY year DESC"
            ),
            'statistics': self._get_statistics()
        }
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        logger.info(f"Exported threat tracker data to {output_path}")
        return output_path
    
    def _get_statistics(self) -> Dict:
        """Get database statistics."""
        tables = [
            'wto_trade_data', 'wto_disputes', 'imf_economic_data',
            'world_bank_indicators', 'unsc_resolutions', 'icj_cases', 'nato_documents'
        ]
        
        stats = {}
        for table in tables:
            result = self.db.query(f"SELECT COUNT(*) as count FROM {table}")
            stats[table] = result[0]['count'] if result else 0
        
        return stats

# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================
def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='International Obligations Data Extractor for Threat Tracker'
    )
    parser.add_argument(
        '--sources',
        nargs='+',
        choices=['wto', 'imf', 'world_bank', 'un', 'icj', 'nato', 'all'],
        default=['all'],
        help='Data sources to extract from'
    )
    parser.add_argument(
        '--export',
        action='store_true',
        help='Export data for Threat Tracker after extraction'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='./exports/threat_tracker_data.json',
        help='Output path for export'
    )
    parser.add_argument(
        '--db',
        type=str,
        default='./data/intl_obligations.db',
        help='Database path'
    )
    
    args = parser.parse_args()
    
    # Configure
    config = ExtractorConfig()
    config.database_path = args.db
    
    # Initialize
    extractor = MasterExtractor(config)
    
    # Determine sources
    sources = None if 'all' in args.sources else args.sources
    
    # Extract
    print("\n" + "="*70)
    print("INTERNATIONAL OBLIGATIONS DATA EXTRACTOR")
    print("For: The Culture Keepers Threat Tracker™")
    print("="*70 + "\n")
    
    results = extractor.extract_all(sources)
    
    # Print results
    print("\n" + "="*70)
    print("EXTRACTION RESULTS")
    print("="*70)
    
    total = 0
    for source, result in results.items():
        status = "✓" if 'error' not in result else "✗"
        records = result.get('records', 0)
        total += records
        print(f"  {status} {source.upper():15} {records:>6} records")
    
    print("-"*70)
    print(f"    {'TOTAL':15} {total:>6} records")
    print("="*70)
    
    # Export if requested
    if args.export:
        output = extractor.export_for_threat_tracker(args.output)
        print(f"\n✓ Exported data to: {output}")
    
    # Show statistics
    stats = extractor._get_statistics()
    print("\nDatabase Statistics:")
    for table, count in stats.items():
        print(f"  {table}: {count} records")


if __name__ == '__main__':
    main()
