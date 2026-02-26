# International Obligations Data Extractor

**For: The Culture Keepers Threat Tracker™**

A comprehensive Python framework for extracting data from international organizations that may create obligations or constraints affecting U.S. cultural, environmental, and heritage institutions.

---

## 📊 Data Sources

| Source | API | What It Provides | US Relevance |
|--------|-----|------------------|--------------|
| **WTO** | ✅ Yes* | Trade disputes, tariffs, cultural goods trade | Trade obligations |
| **IMF** | ✅ Yes | Economic indicators, funding metrics | Economic context |
| **World Bank** | ✅ Yes | Development indicators, environment data | Policy benchmarks |
| **UN** | ⚠️ Partial | Security Council resolutions | Treaty obligations |
| **ICJ** | ❌ No | International court cases | Legal precedents |
| **NATO** | ❌ No | Official texts, communiqués | Alliance commitments |

*WTO trade data requires free API key from apiportal.wto.org

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4
```

### 2. Run Extraction

```bash
# Extract from all free sources (no API key needed)
python quick_start.py

# Extract and export for Threat Tracker
python quick_start.py --export

# Full extraction (if you have WTO API key)
export WTO_API_KEY="your-key-here"
python quick_start.py --full --export
```

### 3. Query the Data

```python
from query_utils import ObligationsDatabase, get_threat_summary

# Get threat summary for dashboard
summary = get_threat_summary()
print(f"Active WTO disputes: {summary['wto_active_disputes']}")
print(f"Active ICJ cases: {summary['icj_active_cases']}")

# Query specific data
db = ObligationsDatabase()

# Get US-involved WTO disputes
disputes = db.get_us_wto_disputes()

# Search for cultural heritage issues
cultural = db.search_cultural_issues('indigenous')

# Get environmental obligations
env = db.get_environmental_obligations()
```

---

## 📁 Files Overview

```
intl_obligations_extractor/
├── master_extractor.py     # Main extraction engine (all sources)
├── quick_start.py          # Simple one-command extraction
├── query_utils.py          # Query functions for Threat Tracker
├── data/
│   └── intl_obligations.db # SQLite database (created on first run)
└── exports/
    └── threat_tracker_data.json  # Exported data for integration
```

---

## 🔑 API Keys

### WTO (Optional but Recommended)

1. Go to https://apiportal.wto.org/
2. Create a free account
3. Subscribe to "Timeseries API"
4. Copy your subscription key
5. Set environment variable:

```bash
export WTO_API_KEY="your-subscription-key"
```

**Without the key:** You'll still get WTO dispute data via web scraping, but not detailed trade statistics.

### Other Sources

- **IMF, World Bank, UN**: No API key required
- **ICJ, NATO**: Uses web scraping and academic datasets

---

## 📊 Database Schema

### Tables

| Table | Description |
|-------|-------------|
| `wto_trade_data` | Trade statistics (cultural goods, etc.) |
| `wto_disputes` | WTO dispute settlement cases |
| `imf_economic_data` | IMF economic indicators |
| `world_bank_indicators` | World Bank development data |
| `unsc_resolutions` | UN Security Council resolutions |
| `icj_cases` | International Court of Justice cases |
| `nato_documents` | NATO official texts and communiqués |
| `extraction_log` | Tracking of extraction runs |

### Key Fields for Threat Tracking

- `us_involvement` - How the US is involved (applicant, respondent, etc.)
- `cultural_relevance` - Tags for cultural/heritage relevance
- `status` - Current status of disputes/cases

---

## 🔗 Threat Tracker Integration

### Export Data for React App

```python
from query_utils import ObligationsDatabase

db = ObligationsDatabase()
json_path = db.export_threat_tracker_data()
print(f"Exported to: {json_path}")
```

### Example: Add to Threat Tracker Dashboard

```javascript
// In your React Threat Tracker component
import intlData from './exports/threat_tracker_data.json';

const InternationalObligations = () => {
  const { us_obligations, cultural_heritage, economic_indicators } = intlData;
  
  return (
    <div className="intl-obligations-panel">
      <h3>International Obligations</h3>
      
      {/* WTO Disputes */}
      <section>
        <h4>WTO Disputes ({us_obligations.wto_disputes.length})</h4>
        {us_obligations.wto_disputes.map(dispute => (
          <div key={dispute.dispute_number} className="dispute-card">
            <span className="badge">{dispute.status}</span>
            <p>{dispute.title}</p>
          </div>
        ))}
      </section>
      
      {/* ICJ Cases */}
      <section>
        <h4>ICJ Cases ({us_obligations.icj_cases.length})</h4>
        {/* ... */}
      </section>
    </div>
  );
};
```

### Example: Real-Time Query API

```python
# Flask/FastAPI endpoint example
from flask import Flask, jsonify
from query_utils import ObligationsDatabase, get_threat_summary

app = Flask(__name__)

@app.route('/api/obligations/summary')
def obligations_summary():
    return jsonify(get_threat_summary())

@app.route('/api/obligations/search/<keyword>')
def search_obligations(keyword):
    from query_utils import search_all
    return jsonify(search_all(keyword))
```

---

## 📋 Cultural Relevance Keywords

The extractor automatically tags data with cultural relevance based on these keywords:

- **Heritage**: cultural, heritage, museum, art, artifact, archaeological, monument, preservation
- **Indigenous**: indigenous, tribal, native, NAGPRA, repatriation
- **Environment**: environment, climate, conservation, wildlife, national park, sanctuary
- **Media/Education**: broadcast, media, education, library, intellectual property, copyright, UNESCO

---

## 🔄 Scheduled Updates

For automated updates, add to crontab:

```bash
# Daily update at 2 AM
0 2 * * * cd /path/to/extractor && python quick_start.py --export >> /var/log/intl_extractor.log 2>&1
```

Or use the Python scheduler:

```python
import schedule
import time
from master_extractor import MasterExtractor

def daily_update():
    extractor = MasterExtractor()
    extractor.extract_all()
    extractor.export_for_threat_tracker()

schedule.every().day.at("02:00").do(daily_update)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## 🛠️ Advanced Usage

### Custom Configuration

```python
from master_extractor import MasterExtractor, ExtractorConfig

config = ExtractorConfig()
config.start_year = 2015
config.end_year = 2025
config.cultural_keywords.extend(['smithsonian', 'archive', 'historic'])

extractor = MasterExtractor(config)
results = extractor.extract_all(['imf', 'world_bank'])
```

### Direct Database Queries

```python
from query_utils import ObligationsDatabase

db = ObligationsDatabase()

# Custom SQL query
results = db._query("""
    SELECT 
        case_name, 
        applicant, 
        respondent, 
        date_filed,
        us_involvement
    FROM icj_cases 
    WHERE us_involvement IS NOT NULL
    AND date_filed >= '2020-01-01'
    ORDER BY date_filed DESC
""")

for case in results:
    print(f"{case['case_name']} - US as {case['us_involvement']}")
```

### Extract Specific Sources Only

```python
from master_extractor import MasterExtractor

extractor = MasterExtractor()

# Only IMF and World Bank
results = extractor.extract_all(['imf', 'world_bank'])

# Only legal sources
results = extractor.extract_all(['wto', 'icj'])
```

---

## 📈 Sample Output

### Threat Summary JSON

```json
{
  "wto_active_disputes": 12,
  "wto_total_disputes": 45,
  "icj_active_cases": 3,
  "icj_total_cases": 18,
  "cultural_heritage_alerts": 7,
  "last_updated": "2026-01-24T12:00:00"
}
```

### US WTO Dispute Example

```json
{
  "dispute_number": "DS543",
  "title": "United States — Tariff Measures on Certain Goods from China",
  "complainant": "China",
  "respondent": "United States",
  "status": "Panel established",
  "cultural_relevance": "intellectual property",
  "url": "https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds543_e.htm"
}
```

---

## ⚠️ Limitations

1. **WTO Trade Data**: Requires API key for detailed statistics
2. **ICJ/NATO**: No official APIs; relies on academic datasets and web scraping
3. **UNSC Resolutions**: Full text not always available; uses Zenodo corpus
4. **Rate Limiting**: Built-in delays to respect server limits

---

## 📜 License

MIT License - Free for research and non-commercial use.

---

## 🙏 Data Sources Credits

- WTO: https://apiportal.wto.org/
- IMF: http://dataservices.imf.org/
- World Bank: https://api.worldbank.org/
- UN Data: http://data.un.org/
- CR-UNSC Corpus: https://zenodo.org/records/11212056
- CD-ICJ Corpus: https://zenodo.org/records/3826444

---

## 📞 Support

For issues or feature requests, please contact the development team or submit an issue to the repository.
