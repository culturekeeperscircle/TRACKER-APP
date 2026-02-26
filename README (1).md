# TCKC Threat Tracker™ v2.0.0

A comprehensive system for monitoring federal government actions affecting Indigenous, Latiné, African Descendant, Asian American, Pacific Islander/Oceania, Caribbean, and immigrant communities' cultural resources.

## 📁 Project Structure

```
tckc-final/
├── index.jsx              # Application entry point & exports
├── README.md              # This documentation
│
├── data/                  # Data layer (separated for easy updates)
│   ├── agencies.js        # Agency registry (17 agencies, 120+ sub-agencies)
│   ├── constants.js       # Constants, categories, frameworks
│   ├── schema.js          # Validation schemas & templates
│   ├── executive-orders.js # Executive Orders & Legislation (70+ entries)
│   ├── historical-impacts.js # Historical Impact Database (200+ entries)
│   └── index.js           # Data module exports
│
├── components/            # React components
│   └── ThreatTracker.jsx  # Main application component (~800 lines)
│
├── utils/                 # Utility functions
│   ├── filters.js         # Filtering, sorting, presets
│   ├── export.js          # CSV, JSON, Markdown export
│   ├── search.js          # AI-powered search & relevance
│   └── migration.js       # Data migration & encoding fixes
│
└── assets/                # Static assets
    └── logo.js            # Logo placeholder
```

## 🚀 Getting Started

### Basic Usage

```jsx
import ThreatTracker from './tckc-final';

function App() {
  return <ThreatTracker />;
}
```

### Using Individual Modules

```jsx
import { 
  HISTORICAL_DATABASE, 
  EXECUTIVE_ORDERS_LEGISLATION,
  filterAndSort,
  downloadCSV,
  searchWithRelevance
} from './tckc-final';

// Filter for critical threats in 2025
const criticalThreats = filterAndSort(HISTORICAL_DATABASE, {
  threatFilter: 'CRITICAL',
  yearFilter: '2025'
});

// Export to CSV
downloadCSV(criticalThreats, 'critical-threats-2025.csv');

// AI-powered search
const results = searchWithRelevance(HISTORICAL_DATABASE, 'indigenous land rights');
```

## 📊 Data Schemas

### Executive Order Entry

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | ✓ | Unique identifier (e.g., 'eo-14151') |
| documentType | string | ✓ | Type (Executive Order, Public Law, etc.) |
| number | string | | Official number (e.g., 'EO 14151') |
| title | string | ✓ | Full official title |
| shortTitle | string | | Brief title for display |
| dateSigned | string | ✓ | ISO date (YYYY-MM-DD) |
| datePublished | string | | Publication date |
| president | string | | Signing president |
| administration | string | ✓ | Trump I, Biden-Harris, Trump II |
| agencies | string[] | ✓ | Affected agency codes |
| status | string | | Current status |
| threatLevel | string | ✓ | CRITICAL, MODERATE, or PROTECTIVE |
| summary | string | | Executive summary |
| culturalImpact | string | | Cultural impact analysis |
| federalRegisterUrl | string | | Federal Register link |
| whiteHouseUrl | string | | White House link |
| congressUrl | string | | Congress.gov link |

### Historical Impact Entry

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | ✓ | Unique identifier |
| date | string | ✓ | ISO date |
| type | string | ✓ | Entry type |
| title | string | ✓ | Entry title |
| agencies | string[] | ✓ | Affected agencies |
| status | string | | Current status |
| threatLevel | string | ✓ | CRITICAL, MODERATE, or PROTECTIVE |
| description | string | | Full description |
| communities | string[] | | Affected communities |
| relatedEO | string | | Related executive order |
| impactAnalysis | object | | 4Ps impact analysis |
| sourceUrl | string | | Source URL |

### 4Ps Impact Analysis Structure

```javascript
impactAnalysis: {
  people: {
    affected: true,
    severity: 'severe', // severe, moderate, minor
    estimatedNumber: 50000,
    details: 'Description of impact on people',
    geographicScope: 'National'
  },
  places: { /* same structure */ },
  practices: { /* same structure */ },
  treasures: { /* same structure */ }
}
```

## 🏛️ Agency Registry

### Environmental & Land Management
- **DOI** - Department of the Interior (NPS, BLM, BIA, BOR, FWS, USGS, etc.)
- **EPA** - Environmental Protection Agency (OAR, OW, OLEM, OEJ, etc.)
- **NOAA** - National Oceanic and Atmospheric Administration

### Cultural & Archival
- **NARA** - National Archives and Records Administration
- **LOC** - Library of Congress
- **SMITHSONIAN** - Smithsonian Institution (23 museums/centers)
- **IMLS** - Institute of Museum and Library Services

### Arts & Humanities
- **NEA** - National Endowment for the Arts
- **NEH** - National Endowment for the Humanities
- **KENNEDY** - Kennedy Center for the Performing Arts
- **CPB** - Corporation for Public Broadcasting

### Social Services (* Cultural Focus)
- **ED** - Department of Education
- **HHS** - Health and Human Services
- **USDA** - Department of Agriculture

### Immigration (** Immigration Focus)
- **DHS** - Department of Homeland Security
- **STATE** - Department of State
- **DOJ** - Department of Justice

## ⚖️ Classification Rules

### CRITICAL
- Mass layoffs (>1,000 employees)
- Complete defunding of programs
- Permanent land transfers away from community control
- Irreversible environmental damage
- Agency abolishment

### MODERATE
- Reversible policy changes
- Partial funding reductions (<50%)
- Temporary program suspensions
- Leadership changes

### PROTECTIVE
- Litigation defending communities
- New funding allocations
- Expanded rights and protections
- Community resource restoration

## 🔧 Utilities Reference

### Filters (`utils/filters.js`)

```javascript
import { 
  filterAndSort, 
  DEFAULT_FILTER_STATE,
  FILTER_PRESETS,
  applyPreset 
} from './utils/filters.js';

// Apply filters
const filtered = filterAndSort(documents, {
  threatFilter: 'CRITICAL',
  yearFilter: '2025',
  agencyFilter: 'DOI',
  communityFilter: 'indigenous'
});

// Use a preset
const preset = applyPreset('indigenous-impacts');
```

### Export (`utils/export.js`)

```javascript
import { 
  downloadCSV, 
  downloadJSON, 
  generateMarkdownReport 
} from './utils/export.js';

// Export to CSV with impact analysis
downloadCSV(documents, 'export.csv', { includeImpactAnalysis: true });

// Export to JSON
downloadJSON(documents, 'export.json', { pretty: true });

// Generate Markdown report grouped by threat level
const report = generateMarkdownReport(documents, { 
  groupBy: 'threatLevel',
  includeExecutiveSummary: true 
});
```

### Search (`utils/search.js`)

```javascript
import { 
  searchWithRelevance, 
  buildAIQueryContext,
  parseStructuredQuery 
} from './utils/search.js';

// Relevance-scored search
const results = searchWithRelevance(documents, 'indigenous land rights', {
  minScore: 10,
  maxResults: 20
});

// Structured query syntax
const parsed = parseStructuredQuery('agency:DOI threat:CRITICAL year:2025');
```

### Migration (`utils/migration.js`)

```javascript
import { 
  fixEncoding, 
  runMigration,
  validateBatch 
} from './utils/migration.js';

// Fix encoding issues
const cleanText = fixEncoding('LatinÃ©'); // Returns 'Latiné'

// Validate entries
const validation = validateBatch(entries, 'eo');
console.log(`Valid: ${validation.valid}, Invalid: ${validation.invalid}`);
```

## 📈 Adding New Entries

### 1. Add Executive Order

Edit `data/executive-orders.js`:

```javascript
{
  id: 'eo-xxxxx',
  documentType: 'Executive Order',
  number: 'EO XXXXX',
  title: 'Full Title Here',
  shortTitle: 'Brief Title',
  dateSigned: '2026-01-22',
  administration: 'Trump II',
  agencies: ['DOI', 'EPA'],
  threatLevel: 'CRITICAL',
  status: 'Active',
  summary: 'Summary of the order...',
  culturalImpact: 'Impact on communities...',
  federalRegisterUrl: 'https://...'
}
```

### 2. Add Historical Impact

Edit `data/historical-impacts.js`:

```javascript
{
  id: 'impact-2026-xxx',
  date: '2026-01-22',
  type: 'Agency Action',
  title: 'Impact Title',
  agencies: ['DOI'],
  threatLevel: 'CRITICAL',
  status: 'Ongoing',
  description: 'Full description...',
  communities: ['indigenous', 'latine'],
  impactAnalysis: {
    people: {
      affected: true,
      severity: 'severe',
      estimatedNumber: 50000,
      details: 'Impact details...'
    }
  }
}
```

## 📋 Benefits of Modular Structure

| Aspect | Original (8,376 lines) | Restructured |
|--------|------------------------|--------------|
| Main Component | 8,376 lines | ~800 lines |
| Data Updates | Edit component file | Edit data files only |
| Validation | None | Schema validation |
| Export Options | Limited | CSV, JSON, Markdown |
| Search | Basic text match | AI-powered relevance |
| Filter Presets | None | 10 built-in presets |
| Testing | Difficult | Easy per-module |
| Maintenance | Complex | Modular & simple |

## 🔄 Version History

- **v2.0.0** (2026-01-22) - Complete modular restructure
- **v1.x** - Monolithic single-file application

## 📝 License

© The Culture Keepers Circle. All rights reserved.

---

*Protecting Cultural Continuity Through Comprehensive Documentation*
