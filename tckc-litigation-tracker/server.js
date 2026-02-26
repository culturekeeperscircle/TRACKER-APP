/**
 * TCKC Federal Litigation Threat Tracker - Local HTTP Server
 * 
 * A comprehensive tracking system for federal litigation affecting cultural resources
 * and communities of concern across federal agencies.
 * 
 * Usage:
 *   node server.js
 * 
 * Then open http://localhost:3000 in your browser
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;
const HOST = 'localhost';

// MIME type mapping
const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

// API endpoints
const API_ROUTES = {
  '/api/litigation': handleLitigationAPI,
  '/api/litigation/search': handleSearchAPI,
  '/api/litigation/stats': handleStatsAPI,
  '/api/agencies': handleAgenciesAPI
};

// Create HTTP server
const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const pathname = url.pathname;

  // Enable CORS for development
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  // Check if this is an API route
  for (const [route, handler] of Object.entries(API_ROUTES)) {
    if (pathname.startsWith(route)) {
      handler(req, res, url);
      return;
    }
  }

  // Serve static files
  serveStaticFile(req, res, pathname);
});

// Serve static files
function serveStaticFile(req, res, pathname) {
  // Default to index.html
  if (pathname === '/') {
    pathname = '/index.html';
  }

  const filePath = path.join(__dirname, 'public', pathname);
  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';

  fs.readFile(filePath, (err, data) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 - File Not Found</h1>');
      } else {
        res.writeHead(500, { 'Content-Type': 'text/html' });
        res.end('<h1>500 - Internal Server Error</h1>');
      }
      return;
    }

    res.writeHead(200, { 'Content-Type': contentType });
    res.end(data);
  });
}

// Load litigation database
function loadDatabase() {
  const dbPath = path.join(__dirname, 'data', 'litigation-database.json');
  try {
    const data = fs.readFileSync(dbPath, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    console.error('Error loading database:', err);
    return null;
  }
}

// API: Get all litigation entries or filter by parameters
function handleLitigationAPI(req, res, url) {
  const db = loadDatabase();
  if (!db) {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Database not available' }));
    return;
  }

  const params = url.searchParams;
  let entries = db.litigationEntries;

  // Filter by classification
  const classification = params.get('classification');
  if (classification) {
    entries = entries.filter(e => e.classification === classification.toUpperCase());
  }

  // Filter by agency
  const agency = params.get('agency');
  if (agency) {
    entries = entries.filter(e => 
      e.agenciesInvolved.some(a => 
        a.agency.toUpperCase() === agency.toUpperCase() ||
        (a.subAgency && a.subAgency.toUpperCase().includes(agency.toUpperCase()))
      )
    );
  }

  // Filter by community
  const community = params.get('community');
  if (community) {
    entries = entries.filter(e =>
      e.culturalImpactAnalysis.affectedCommunities.some(c =>
        c.toLowerCase().includes(community.toLowerCase())
      )
    );
  }

  // Filter by status
  const status = params.get('status');
  if (status) {
    entries = entries.filter(e =>
      e.currentStatus.toLowerCase().includes(status.toLowerCase())
    );
  }

  // Get single entry by ID
  const id = params.get('id');
  if (id) {
    entries = entries.filter(e => e.id === id);
  }

  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    count: entries.length,
    entries: entries,
    metadata: db.metadata
  }));
}

// API: Search litigation entries
function handleSearchAPI(req, res, url) {
  const db = loadDatabase();
  if (!db) {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Database not available' }));
    return;
  }

  const query = url.searchParams.get('q');
  if (!query) {
    res.writeHead(400, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Search query required' }));
    return;
  }

  const searchTerms = query.toLowerCase().split(' ');
  
  const results = db.litigationEntries.filter(entry => {
    const searchableText = [
      entry.caseName,
      entry.claimsAndLegalBasis.summary,
      entry.culturalImpactAnalysis.narrativeAssessment,
      ...entry.agenciesInvolved.map(a => a.agency),
      ...entry.culturalImpactAnalysis.affectedCommunities
    ].join(' ').toLowerCase();

    return searchTerms.every(term => searchableText.includes(term));
  });

  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    query: query,
    count: results.length,
    results: results
  }));
}

// API: Get statistics
function handleStatsAPI(req, res, url) {
  const db = loadDatabase();
  if (!db) {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Database not available' }));
    return;
  }

  const entries = db.litigationEntries;

  // Count by classification
  const byClassification = entries.reduce((acc, e) => {
    acc[e.classification] = (acc[e.classification] || 0) + 1;
    return acc;
  }, {});

  // Count by agency
  const byAgency = entries.reduce((acc, e) => {
    e.agenciesInvolved.forEach(a => {
      acc[a.agency] = (acc[a.agency] || 0) + 1;
    });
    return acc;
  }, {});

  // Count by community
  const byCommunity = entries.reduce((acc, e) => {
    e.culturalImpactAnalysis.affectedCommunities.forEach(c => {
      acc[c] = (acc[c] || 0) + 1;
    });
    return acc;
  }, {});

  // Count by status category
  const byStatus = entries.reduce((acc, e) => {
    let category = 'Other';
    const status = e.currentStatus.toLowerCase();
    
    if (status.includes('injunction granted') || status.includes('judgment for plaintiffs')) {
      category = 'Protective Outcomes';
    } else if (status.includes('active') || status.includes('pending')) {
      category = 'Active Litigation';
    } else if (status.includes('dismissed') || status.includes('withdrew')) {
      category = 'Dismissed/Withdrawn';
    } else if (status.includes('review') || status.includes('watch')) {
      category = 'Under Review';
    }
    
    acc[category] = (acc[category] || 0) + 1;
    return acc;
  }, {});

  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    totalEntries: entries.length,
    byClassification,
    byAgency,
    byCommunity,
    byStatus,
    lastUpdated: db.metadata.lastUpdated
  }));
}

// API: Get agency categories
function handleAgenciesAPI(req, res, url) {
  const db = loadDatabase();
  if (!db) {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Database not available' }));
    return;
  }

  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(db.agencyCategories));
}

// Start server
server.listen(PORT, HOST, () => {
  console.log(`
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   TCKC Federal Litigation Threat Tracker                         ║
║   ──────────────────────────────────────                         ║
║                                                                  ║
║   Server running at: http://${HOST}:${PORT}                        ║
║                                                                  ║
║   API Endpoints:                                                 ║
║   • GET /api/litigation          - All entries (with filters)    ║
║   • GET /api/litigation/search   - Search entries                ║
║   • GET /api/litigation/stats    - Statistics                    ║
║   • GET /api/agencies            - Agency categories             ║
║                                                                  ║
║   Press Ctrl+C to stop the server                                ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
  `);
});
