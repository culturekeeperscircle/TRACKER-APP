/**
 * TCKC Federal Litigation Threat Tracker - Frontend Application
 */

// API Base URL
const API_BASE = '/api';

// State
let allEntries = [];
let filteredEntries = [];
let stats = null;

// DOM Elements
const views = document.querySelectorAll('.view');
const navBtns = document.querySelectorAll('.nav-btn');
const modal = document.getElementById('case-modal');
const caseDetail = document.getElementById('case-detail');

// Initialize application
document.addEventListener('DOMContentLoaded', async () => {
    await loadData();
    setupEventListeners();
    renderDashboard();
});

// Load data from API
async function loadData() {
    try {
        // Load all entries
        const entriesResponse = await fetch(`${API_BASE}/litigation`);
        const entriesData = await entriesResponse.json();
        allEntries = entriesData.entries;
        filteredEntries = [...allEntries];

        // Update metadata
        document.getElementById('last-updated').textContent = `Last Updated: ${entriesData.metadata.lastUpdated}`;
        document.getElementById('total-entries').textContent = `Total Entries: ${allEntries.length}`;

        // Load stats
        const statsResponse = await fetch(`${API_BASE}/litigation/stats`);
        stats = await statsResponse.json();

        // Populate agency filter
        const agencyFilter = document.getElementById('filter-agency');
        Object.keys(stats.byAgency).sort().forEach(agency => {
            const option = document.createElement('option');
            option.value = agency;
            option.textContent = `${agency} (${stats.byAgency[agency]})`;
            agencyFilter.appendChild(option);
        });

    } catch (error) {
        console.error('Error loading data:', error);
    }
}

// Setup event listeners
function setupEventListeners() {
    // Navigation
    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const viewId = btn.dataset.view;
            switchView(viewId);
            navBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });

    // Search
    document.getElementById('search-btn').addEventListener('click', performSearch);
    document.getElementById('search-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performSearch();
    });

    // Filters
    document.getElementById('filter-classification').addEventListener('change', applyFilters);
    document.getElementById('filter-agency').addEventListener('change', applyFilters);
    document.getElementById('filter-community').addEventListener('change', applyFilters);

    // Agency buttons
    document.querySelectorAll('.agency-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.agency-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            showAgencyCases(btn.dataset.agency);
        });
    });

    // Community cards
    document.querySelectorAll('.community-card').forEach(card => {
        card.addEventListener('click', () => {
            showCommunityCases(card.dataset.community);
        });
    });

    // Modal close
    document.querySelector('.close-modal').addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
}

// Switch views
function switchView(viewId) {
    views.forEach(view => view.classList.remove('active'));
    document.getElementById(`${viewId}-view`).classList.add('active');

    if (viewId === 'litigation') {
        renderLitigationList();
    } else if (viewId === 'communities') {
        updateCommunityStats();
    }
}

// Render dashboard
function renderDashboard() {
    if (!stats) return;

    // Update stat cards
    document.getElementById('stat-critical').textContent = stats.byClassification.CRITICAL || 0;
    document.getElementById('stat-protective').textContent = stats.byClassification.PROTECTIVE || 0;
    document.getElementById('stat-moderate').textContent = stats.byClassification.MODERATE || 0;
    document.getElementById('stat-watch').textContent = stats.byClassification.WATCH || 0;

    // Render agency chart
    renderBarChart('agency-chart', stats.byAgency, 'Cases by Agency');

    // Render community chart
    renderBarChart('community-chart', stats.byCommunity, 'Cases by Community');

    // Render critical cases
    const criticalCases = allEntries.filter(e => e.classification === 'CRITICAL').slice(0, 6);
    const criticalContainer = document.getElementById('critical-cases');
    criticalContainer.innerHTML = criticalCases.map(c => createCaseCard(c)).join('');
    
    // Add click handlers to case cards
    criticalContainer.querySelectorAll('.case-card').forEach(card => {
        card.addEventListener('click', () => showCaseDetail(card.dataset.id));
    });
}

// Render bar chart
function renderBarChart(containerId, data, title) {
    const container = document.getElementById(containerId);
    const maxValue = Math.max(...Object.values(data));

    const html = Object.entries(data)
        .sort((a, b) => b[1] - a[1])
        .map(([label, value]) => {
            const width = (value / maxValue) * 100;
            return `
                <div class="chart-bar">
                    <span class="chart-label">${label}</span>
                    <div class="chart-bar-fill" style="width: ${width}%">${value}</div>
                </div>
            `;
        })
        .join('');

    container.innerHTML = html;
}

// Create case card HTML
function createCaseCard(entry) {
    const agencies = entry.agenciesInvolved.map(a => 
        `<span class="agency-tag">${a.agency}</span>`
    ).join('');

    const communities = entry.culturalImpactAnalysis.affectedCommunities.map(c =>
        `<span class="community-tag">${c}</span>`
    ).join('');

    return `
        <div class="case-card ${entry.classification.toLowerCase()}" data-id="${entry.id}">
            <div class="case-header">
                <span class="case-id">${entry.id}</span>
                <span class="case-classification ${entry.classification.toLowerCase()}">${entry.classification}</span>
            </div>
            <h3 class="case-title">${entry.caseName}</h3>
            <div class="case-meta">
                <span>${entry.court}</span> • <span>${entry.currentStatus}</span>
            </div>
            <div class="case-agencies">${agencies}</div>
            <div class="case-communities">${communities}</div>
        </div>
    `;
}

// Render litigation list
function renderLitigationList() {
    const container = document.getElementById('litigation-list');
    container.innerHTML = filteredEntries.map(e => createCaseCard(e)).join('');

    container.querySelectorAll('.case-card').forEach(card => {
        card.addEventListener('click', () => showCaseDetail(card.dataset.id));
    });
}

// Perform search
async function performSearch() {
    const query = document.getElementById('search-input').value.trim();
    
    if (!query) {
        filteredEntries = [...allEntries];
    } else {
        try {
            const response = await fetch(`${API_BASE}/litigation/search?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            filteredEntries = data.results;
        } catch (error) {
            console.error('Search error:', error);
        }
    }

    renderLitigationList();
}

// Apply filters
function applyFilters() {
    const classification = document.getElementById('filter-classification').value;
    const agency = document.getElementById('filter-agency').value;
    const community = document.getElementById('filter-community').value;

    filteredEntries = allEntries.filter(entry => {
        let match = true;

        if (classification && entry.classification !== classification) {
            match = false;
        }

        if (agency && !entry.agenciesInvolved.some(a => a.agency === agency)) {
            match = false;
        }

        if (community && !entry.culturalImpactAnalysis.affectedCommunities.some(c => 
            c.toLowerCase().includes(community.toLowerCase())
        )) {
            match = false;
        }

        return match;
    });

    renderLitigationList();
}

// Show agency cases
function showAgencyCases(agency) {
    const cases = allEntries.filter(e => 
        e.agenciesInvolved.some(a => a.agency === agency)
    );

    const container = document.getElementById('agency-cases');
    container.innerHTML = `
        <h3>Cases Involving ${agency} (${cases.length})</h3>
        <div class="cases-grid">
            ${cases.map(c => createCaseCard(c)).join('')}
        </div>
    `;

    container.querySelectorAll('.case-card').forEach(card => {
        card.addEventListener('click', () => showCaseDetail(card.dataset.id));
    });
}

// Show community cases
function showCommunityCases(community) {
    const cases = allEntries.filter(e =>
        e.culturalImpactAnalysis.affectedCommunities.some(c =>
            c.toLowerCase().includes(community.toLowerCase())
        )
    );

    const container = document.getElementById('community-cases');
    container.innerHTML = `
        <h3>Cases Affecting ${community} Communities (${cases.length})</h3>
        <div class="cases-grid">
            ${cases.map(c => createCaseCard(c)).join('')}
        </div>
    `;

    container.querySelectorAll('.case-card').forEach(card => {
        card.addEventListener('click', () => showCaseDetail(card.dataset.id));
    });
}

// Update community stats
function updateCommunityStats() {
    document.querySelectorAll('.community-card').forEach(card => {
        const community = card.dataset.community;
        const count = allEntries.filter(e =>
            e.culturalImpactAnalysis.affectedCommunities.some(c =>
                c.toLowerCase().includes(community.toLowerCase())
            )
        ).length;
        card.querySelector('.case-count').textContent = `${count} cases`;
    });
}

// Show case detail modal
function showCaseDetail(caseId) {
    const entry = allEntries.find(e => e.id === caseId);
    if (!entry) return;

    const impact = entry.culturalImpactAnalysis.impactByFramework;
    const quotes = entry.operativeQuotes.map(q => `
        <div class="quote-block">
            <div class="quote-text">"${q.quote}"</div>
            <div class="quote-source">— ${q.source}</div>
            <div class="quote-significance">${q.significance}</div>
        </div>
    `).join('');

    caseDetail.innerHTML = `
        <div class="detail-header">
            <div class="case-id">${entry.id}</div>
            <h2>${entry.caseName}</h2>
            <div class="detail-meta">
                <span class="case-classification ${entry.classification.toLowerCase()}">${entry.classification}</span>
                <span>Court: ${entry.court}</span>
                <span>Docket: ${entry.docketNumber}</span>
                <span>Status: ${entry.currentStatus}</span>
            </div>
        </div>

        <div class="detail-section">
            <h3>Claims & Legal Basis</h3>
            <p>${entry.claimsAndLegalBasis.summary}</p>
            <p><strong>Statutes at Issue:</strong> ${entry.claimsAndLegalBasis.statutesAtIssue.join(', ')}</p>
            <p><strong>Relief Sought:</strong> ${entry.claimsAndLegalBasis.reliefSought.join(', ')}</p>
        </div>

        <div class="detail-section">
            <h3>Parties</h3>
            <p><strong>Plaintiffs:</strong> ${entry.parties.plaintiffs.join(', ')}</p>
            <p><strong>Defendants:</strong> ${entry.parties.defendants.join(', ')}</p>
            ${entry.parties.intervenors.length ? `<p><strong>Intervenors:</strong> ${entry.parties.intervenors.join(', ')}</p>` : ''}
        </div>

        <div class="detail-section">
            <h3>Operative Quotes</h3>
            ${quotes || '<p>No notable quotes recorded.</p>'}
        </div>

        <div class="detail-section">
            <h3>Agencies Involved</h3>
            ${entry.agenciesInvolved.map(a => `
                <p><strong>${a.agency}${a.subAgency ? ` (${a.subAgency})` : ''}</strong> — ${a.role}</p>
                <p>${a.specificMandate}</p>
            `).join('')}
        </div>

        <div class="detail-section">
            <h3>Cultural Impact Analysis (4Ps Framework)</h3>
            <p><strong>Affected Communities:</strong> ${entry.culturalImpactAnalysis.affectedCommunities.join(', ')}</p>
            <div class="impact-grid">
                <div class="impact-item">
                    <h4>👥 People</h4>
                    <p>${impact.people}</p>
                </div>
                <div class="impact-item">
                    <h4>📍 Places</h4>
                    <p>${impact.places}</p>
                </div>
                <div class="impact-item">
                    <h4>🎭 Practices</h4>
                    <p>${impact.practices}</p>
                </div>
                <div class="impact-item">
                    <h4>💎 Treasures</h4>
                    <p>${impact.treasures}</p>
                </div>
            </div>
            <p style="margin-top: 1rem;"><strong>Narrative Assessment:</strong> ${entry.culturalImpactAnalysis.narrativeAssessment}</p>
        </div>

        <div class="detail-section">
            <h3>Procedural Status</h3>
            <p><strong>Stage:</strong> ${entry.proceduralPosture.stage}</p>
            <p><strong>TRO Issued:</strong> ${entry.proceduralPosture.trosIssued ? 'Yes' : 'No'}</p>
            <p><strong>Preliminary Injunction:</strong> ${entry.proceduralPosture.preliminaryInjunction ? 'Yes' : 'No'}</p>
            ${entry.proceduralPosture.upcomingDeadlines.length ? `<p><strong>Upcoming Deadlines:</strong> ${entry.proceduralPosture.upcomingDeadlines.join(', ')}</p>` : ''}
        </div>

        <div class="detail-section">
            <h3>Outcome/Impact</h3>
            <p><strong>Current Disposition:</strong> ${entry.outcome.currentDisposition}</p>
            <p><strong>Impact on Agency Operations:</strong> ${entry.outcome.impactOnAgencyOperations}</p>
            <p><strong>Precedential Value:</strong> ${entry.outcome.precedentialValue}</p>
        </div>

        <div class="detail-section">
            <h3>Related Actions</h3>
            ${entry.relatedActions.executiveOrders.length ? `<p><strong>Executive Orders:</strong> ${entry.relatedActions.executiveOrders.join(', ')}</p>` : ''}
            ${entry.relatedActions.companionCases.length ? `<p><strong>Companion Cases:</strong> ${entry.relatedActions.companionCases.join(', ')}</p>` : ''}
            <p><strong>Consolidated Litigation:</strong> ${entry.relatedActions.consolidatedLitigation ? 'Yes' : 'No'}</p>
        </div>

        <div class="detail-section">
            <h3>Classification Rationale</h3>
            <p>${entry.classificationRationale}</p>
        </div>
    `;

    modal.classList.add('active');
}

// Close modal
function closeModal() {
    modal.classList.remove('active');
}
