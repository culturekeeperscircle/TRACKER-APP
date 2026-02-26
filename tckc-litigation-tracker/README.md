# TCKC Federal Litigation Threat Tracker

A comprehensive tracking system for federal litigation affecting cultural resources and communities across federal agencies.

## Overview

This tracker monitors litigation involving:

### Agency Categories

**Stewards of Place-Based Resources:**
- Department of Interior (DOI) — including NPS, BLM, BIA, BOEM
- Environmental Protection Agency (EPA)
- National Oceanic and Atmospheric Administration (NOAA)

**Repositories of Cultural Knowledge:**
- Smithsonian Institution
- National Archives and Records Administration (NARA)
- U.S. Library of Congress (LoC)
- Institute of Museum and Library Services (IMLS)

**Promoters of Cultural Expression:**
- National Endowment for the Arts (NEA)
- National Endowment for the Humanities (NEH)
- Kennedy Center for the Performing Arts
- Corporation for Public Broadcasting (CPB)/PBS/NPR

**Other Agencies with Cultural Impact:**
- Department of Education (ED)
- Health and Human Services (HHS)
- U.S. Department of Agriculture (USDA)
- Department of Homeland Security (DHS)
- State Department
- Department of Justice (DOJ)

### Communities Tracked

- African Descendant communities
- Indigenous communities
- Latiné communities
- Asian American communities
- Pacific Islander/Oceania communities

### 4Ps Cultural Impact Framework

Each case is analyzed using the 4Ps Framework:
- **People** — Who is affected and how
- **Places** — Geographic and territorial impacts
- **Practices** — Cultural practices, traditions, and activities affected
- **Treasures** — Cultural resources, artifacts, and heritage at stake

### Classification System

| Classification | Description |
|----------------|-------------|
| **CRITICAL** | Highest severity - mass layoffs, land transfers, environmental rollbacks, major grant terminations |
| **PROTECTIVE** | Favorable outcomes - successful injunctions, restored grants/protections |
| **MODERATE** | Significant concern - content censorship, procedural violations |
| **WATCH** | Newly filed cases with unclear trajectory |

## Installation

### Prerequisites

- Node.js (v14 or higher)
- npm

### Setup

1. Clone or download this repository to your local machine

2. Navigate to the project directory:
   ```bash
   cd tckc-litigation-tracker
   ```

3. No npm install required - this uses only Node.js built-in modules

4. Start the server:
   ```bash
   node server.js
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

## Project Structure

```
tckc-litigation-tracker/
├── server.js                    # Node.js HTTP server
├── README.md                    # This file
├── data/
│   └── litigation-database.json # Main database file
└── public/
    ├── index.html               # Main HTML page
    ├── styles.css               # CSS styles
    └── app.js                   # Frontend JavaScript
```

## API Endpoints

### GET /api/litigation
Returns all litigation entries with optional filters.

**Query Parameters:**
- `classification` - Filter by classification (CRITICAL, PROTECTIVE, MODERATE, WATCH)
- `agency` - Filter by agency code
- `community` - Filter by affected community
- `status` - Filter by case status
- `id` - Get single entry by ID

**Example:**
```
GET /api/litigation?classification=CRITICAL&agency=EPA
```

### GET /api/litigation/search
Search entries by keyword.

**Query Parameters:**
- `q` - Search query (required)

**Example:**
```
GET /api/litigation/search?q=environmental justice
```

### GET /api/litigation/stats
Returns statistics about the database.

**Response includes:**
- Total entry count
- Counts by classification
- Counts by agency
- Counts by community
- Counts by status category

### GET /api/agencies
Returns agency category definitions.

## Database Structure

Each litigation entry includes:

```json
{
  "id": "AGENCY-YEAR-NUMBER",
  "caseName": "Full case name",
  "docketNumber": "Court docket number",
  "court": "Court name",
  "filingDate": "YYYY-MM-DD",
  "currentStatus": "Status description",
  "statusDate": "YYYY-MM-DD",
  "parties": {
    "plaintiffs": [],
    "defendants": [],
    "intervenors": []
  },
  "claimsAndLegalBasis": {
    "summary": "Description of claims",
    "statutesAtIssue": [],
    "reliefSought": []
  },
  "operativeQuotes": [],
  "agenciesInvolved": [],
  "culturalImpactAnalysis": {
    "affectedCommunities": [],
    "impactByFramework": {
      "people": "",
      "places": "",
      "practices": "",
      "treasures": ""
    },
    "narrativeAssessment": ""
  },
  "proceduralPosture": {},
  "outcome": {},
  "relatedActions": {},
  "classification": "CRITICAL|PROTECTIVE|MODERATE|WATCH",
  "classificationRationale": ""
}
```

## Adding New Entries

1. Open `data/litigation-database.json`
2. Add new entry to the `litigationEntries` array
3. Follow the existing structure
4. Restart the server to load changes

## Usage Tips

### Dashboard
- View statistics at a glance
- See critical cases requiring attention
- Chart visualizations of cases by agency and community

### All Litigation
- Search across all case fields
- Filter by classification, agency, or community
- Click any case card for full details

### By Agency
- Browse cases by agency category
- Click agency buttons to see related cases
- Understand which agencies are most affected

### By Community
- See how many cases affect each community
- Click community cards to see relevant cases
- Understand cross-community impacts

### Case Detail Modal
- Full case documentation
- 4Ps cultural impact analysis
- Related executive orders and companion cases
- Procedural history and outcomes

## Visual Studio Code Integration

For the best development experience in VS Code:

1. Install the "Live Server" extension
2. Right-click `public/index.html` and select "Open with Live Server"
3. The page will auto-reload when you make changes

Alternatively, use the Node.js server for the full API functionality.

## Contributing

To add new litigation entries:

1. Research the case thoroughly
2. Document using the full entry structure
3. Apply the 4Ps cultural impact analysis
4. Assign appropriate classification
5. Add to the database JSON file

## License

For The Culture Keepers Circle (TCKC) internal use.

## Contact

For questions or updates, contact the TCKC team.
