"""
================================================================================
DATA QUERY UTILITIES
================================================================================
Utility functions for querying and analyzing extracted international data.
Designed for integration with The Culture Keepers Threat Tracker™.
================================================================================
"""

import sqlite3
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path


class ObligationsDatabase:
    """
    Query interface for the international obligations database.
    
    Usage:
        from query_utils import ObligationsDatabase
        db = ObligationsDatabase()
        
        # Get US-involved disputes
        disputes = db.get_us_disputes()
        
        # Search for cultural heritage issues
        results = db.search_cultural_issues('indigenous')
    """
    
    def __init__(self, db_path: str = './data/intl_obligations.db'):
        self.db_path = db_path
        
        if not Path(db_path).exists():
            raise FileNotFoundError(
                f"Database not found at {db_path}. "
                "Run quick_start.py first to extract data."
            )
    
    def _query(self, sql: str, params: tuple = None) -> List[Dict]:
        """Execute a query and return results as dictionaries."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        columns = [d[0] for d in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return results
    
    # =========================================================================
    # US-SPECIFIC QUERIES
    # =========================================================================
    
    def get_us_wto_disputes(self, role: str = None) -> List[Dict]:
        """
        Get WTO disputes involving the United States.
        
        Args:
            role: Filter by 'complainant', 'respondent', or None for both
        """
        sql = """
            SELECT * FROM wto_disputes 
            WHERE complainant LIKE '%United States%' 
               OR respondent LIKE '%United States%'
        """
        if role == 'complainant':
            sql = "SELECT * FROM wto_disputes WHERE complainant LIKE '%United States%'"
        elif role == 'respondent':
            sql = "SELECT * FROM wto_disputes WHERE respondent LIKE '%United States%'"
        
        return self._query(sql + " ORDER BY date_initiated DESC")
    
    def get_us_icj_cases(self) -> List[Dict]:
        """Get ICJ cases involving the United States."""
        return self._query("""
            SELECT * FROM icj_cases 
            WHERE us_involvement IS NOT NULL
            ORDER BY date_filed DESC
        """)
    
    def get_us_economic_indicators(self, indicator: str = None) -> List[Dict]:
        """
        Get US economic indicators from IMF.
        
        Args:
            indicator: Specific indicator code, or None for all
        """
        sql = "SELECT * FROM imf_economic_data WHERE country_code = 'US'"
        params = ()
        
        if indicator:
            sql += " AND indicator_code = ?"
            params = (indicator,)
        
        return self._query(sql + " ORDER BY year DESC", params)
    
    def get_us_world_bank_data(self, indicator: str = None) -> List[Dict]:
        """Get World Bank indicators for the US."""
        sql = "SELECT * FROM world_bank_indicators WHERE country_code = 'USA'"
        params = ()
        
        if indicator:
            sql += " AND indicator_code = ?"
            params = (indicator,)
        
        return self._query(sql + " ORDER BY year DESC", params)
    
    # =========================================================================
    # CULTURAL/HERITAGE QUERIES
    # =========================================================================
    
    def search_cultural_issues(self, keyword: str = None) -> Dict[str, List[Dict]]:
        """
        Search all sources for cultural/heritage relevant issues.
        
        Args:
            keyword: Additional keyword to search for
        
        Returns:
            Dictionary with results from each source
        """
        results = {}
        
        # WTO disputes
        sql = "SELECT * FROM wto_disputes WHERE cultural_relevance IS NOT NULL"
        if keyword:
            sql += f" AND (title LIKE '%{keyword}%' OR subject_matter LIKE '%{keyword}%')"
        results['wto_disputes'] = self._query(sql)
        
        # ICJ cases
        sql = "SELECT * FROM icj_cases WHERE cultural_relevance IS NOT NULL"
        if keyword:
            sql += f" AND (case_name LIKE '%{keyword}%' OR subject_matter LIKE '%{keyword}%')"
        results['icj_cases'] = self._query(sql)
        
        # UNSC resolutions
        sql = "SELECT * FROM unsc_resolutions WHERE cultural_relevance IS NOT NULL"
        if keyword:
            sql += f" AND (title LIKE '%{keyword}%' OR topics LIKE '%{keyword}%')"
        results['unsc_resolutions'] = self._query(sql)
        
        return results
    
    def get_environmental_obligations(self) -> Dict[str, List[Dict]]:
        """Get data related to environmental obligations."""
        return {
            'unsc_resolutions': self._query("""
                SELECT * FROM unsc_resolutions 
                WHERE cultural_relevance LIKE '%environment%'
                   OR cultural_relevance LIKE '%climate%'
                   OR cultural_relevance LIKE '%conservation%'
            """),
            'world_bank': self._query("""
                SELECT * FROM world_bank_indicators 
                WHERE indicator_code IN (
                    'EN.ATM.CO2E.PC',
                    'ER.PTD.TOTL.ZS',
                    'ER.MRN.PTMR.ZS'
                )
                AND country_code = 'USA'
                ORDER BY year DESC
            """)
        }
    
    def get_indigenous_issues(self) -> Dict[str, List[Dict]]:
        """Get data related to indigenous peoples and tribal issues."""
        keyword_search = """
            cultural_relevance LIKE '%indigenous%'
            OR cultural_relevance LIKE '%tribal%'
            OR cultural_relevance LIKE '%native%'
        """
        
        return {
            'icj_cases': self._query(f"""
                SELECT * FROM icj_cases WHERE {keyword_search}
            """),
            'unsc_resolutions': self._query(f"""
                SELECT * FROM unsc_resolutions WHERE {keyword_search}
            """)
        }
    
    # =========================================================================
    # TIMELINE QUERIES
    # =========================================================================
    
    def get_recent_developments(self, days: int = 365) -> Dict[str, List[Dict]]:
        """
        Get recent developments from all sources.
        
        Args:
            days: Number of days to look back
        """
        # Note: Date filtering depends on data availability
        return {
            'icj_cases': self._query("""
                SELECT * FROM icj_cases 
                WHERE date_filed >= date('now', '-1 year')
                   OR date_decided >= date('now', '-1 year')
                ORDER BY COALESCE(date_decided, date_filed) DESC
                LIMIT 20
            """),
            'unsc_resolutions': self._query("""
                SELECT * FROM unsc_resolutions
                WHERE date_adopted >= date('now', '-1 year')
                ORDER BY date_adopted DESC
                LIMIT 50
            """),
            'nato_documents': self._query("""
                SELECT * FROM nato_documents
                WHERE date_published >= date('now', '-1 year')
                ORDER BY date_published DESC
                LIMIT 20
            """)
        }
    
    # =========================================================================
    # SUMMARY/STATISTICS
    # =========================================================================
    
    def get_database_summary(self) -> Dict[str, Any]:
        """Get a summary of all data in the database."""
        tables = {
            'wto_trade_data': 'WTO Trade Data',
            'wto_disputes': 'WTO Disputes',
            'imf_economic_data': 'IMF Economic Data',
            'world_bank_indicators': 'World Bank Indicators',
            'unsc_resolutions': 'UNSC Resolutions',
            'icj_cases': 'ICJ Cases',
            'nato_documents': 'NATO Documents'
        }
        
        summary = {
            'total_records': 0,
            'tables': {},
            'us_specific': {},
            'culturally_relevant': {}
        }
        
        for table, name in tables.items():
            count = self._query(f"SELECT COUNT(*) as c FROM {table}")[0]['c']
            summary['tables'][table] = {'name': name, 'count': count}
            summary['total_records'] += count
        
        # US-specific counts
        summary['us_specific'] = {
            'wto_disputes': len(self.get_us_wto_disputes()),
            'icj_cases': len(self.get_us_icj_cases()),
        }
        
        # Culturally relevant counts
        cultural = self.search_cultural_issues()
        summary['culturally_relevant'] = {
            k: len(v) for k, v in cultural.items()
        }
        
        return summary
    
    # =========================================================================
    # EXPORT FUNCTIONS
    # =========================================================================
    
    def export_threat_tracker_data(self, output_path: str = None) -> str:
        """
        Export all relevant data in format suitable for Threat Tracker.
        
        Returns:
            Path to the exported JSON file
        """
        if output_path is None:
            output_path = f'./exports/threat_tracker_{datetime.now().strftime("%Y%m%d")}.json'
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'exported_at': datetime.now().isoformat(),
            'summary': self.get_database_summary(),
            'us_obligations': {
                'wto_disputes': self.get_us_wto_disputes(),
                'icj_cases': self.get_us_icj_cases(),
            },
            'cultural_heritage': self.search_cultural_issues(),
            'environmental': self.get_environmental_obligations(),
            'indigenous': self.get_indigenous_issues(),
            'economic_indicators': {
                'imf': self.get_us_economic_indicators(),
                'world_bank': self.get_us_world_bank_data()
            }
        }
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        return output_path


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def get_threat_summary() -> Dict:
    """
    Quick function to get a threat summary for the dashboard.
    
    Returns:
        Dictionary with key threat indicators
    """
    try:
        db = ObligationsDatabase()
    except FileNotFoundError:
        return {'error': 'Database not found. Run extraction first.'}
    
    us_disputes = db.get_us_wto_disputes()
    us_cases = db.get_us_icj_cases()
    cultural = db.search_cultural_issues()
    
    # Count active threats
    active_disputes = len([d for d in us_disputes if d.get('status') != 'concluded'])
    active_cases = len([c for c in us_cases if c.get('status') not in ['concluded', 'decided']])
    
    return {
        'wto_active_disputes': active_disputes,
        'wto_total_disputes': len(us_disputes),
        'icj_active_cases': active_cases,
        'icj_total_cases': len(us_cases),
        'cultural_heritage_alerts': sum(len(v) for v in cultural.values()),
        'last_updated': datetime.now().isoformat()
    }


def search_all(keyword: str) -> Dict[str, List[Dict]]:
    """
    Search all data sources for a keyword.
    
    Args:
        keyword: Term to search for
    
    Returns:
        Dictionary with results from each source
    """
    try:
        db = ObligationsDatabase()
    except FileNotFoundError:
        return {'error': 'Database not found. Run extraction first.'}
    
    results = {}
    
    # Search each table
    tables_and_columns = {
        'wto_disputes': ['title', 'subject_matter', 'complainant', 'respondent'],
        'icj_cases': ['case_name', 'subject_matter', 'applicant', 'respondent'],
        'unsc_resolutions': ['title', 'topics', 'summary'],
        'nato_documents': ['title', 'summary']
    }
    
    for table, columns in tables_and_columns.items():
        conditions = ' OR '.join([f"{col} LIKE '%{keyword}%'" for col in columns])
        sql = f"SELECT * FROM {table} WHERE {conditions}"
        results[table] = db._query(sql)
    
    return results


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("International Obligations Database - Query Examples")
    print("=" * 70)
    
    try:
        db = ObligationsDatabase()
        
        # Get summary
        print("\n📊 DATABASE SUMMARY:")
        summary = db.get_database_summary()
        print(f"   Total records: {summary['total_records']}")
        for table, info in summary['tables'].items():
            print(f"   - {info['name']}: {info['count']}")
        
        # US-specific data
        print("\n🇺🇸 US-SPECIFIC DATA:")
        print(f"   WTO disputes: {summary['us_specific']['wto_disputes']}")
        print(f"   ICJ cases: {summary['us_specific']['icj_cases']}")
        
        # Cultural relevance
        print("\n🏛️ CULTURALLY RELEVANT:")
        for source, count in summary['culturally_relevant'].items():
            print(f"   - {source}: {count}")
        
        # Quick threat summary
        print("\n⚠️ THREAT SUMMARY:")
        threats = get_threat_summary()
        for key, value in threats.items():
            if key != 'last_updated':
                print(f"   {key}: {value}")
        
        # Example search
        print("\n🔍 EXAMPLE SEARCH ('cultural'):")
        results = search_all('cultural')
        for source, items in results.items():
            if items:
                print(f"   {source}: {len(items)} results")
        
    except FileNotFoundError as e:
        print(f"\n❌ {e}")
        print("   Run: python quick_start.py")
