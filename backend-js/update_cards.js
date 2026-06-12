// update_cards.js — Node.js equivalent of update_cards.py
// Fetches featured GitHub repos, builds HTML project cards,
// and injects them into index.html replacing the .projects-grid content.
//
// Usage:  node update_cards.js
//   (run from the root of the portfolio folder, i.e. "New Portfolio/")

const https = require('https');
const fs = require('fs');
const path = require('path');

// ── Config ────────────────────────────────────────────────────────────────────

const GITHUB_USER = 'anushastefyj';
const INDEX_HTML = path.join(__dirname, '..', 'index.html');

const GOOD_PROJECTS = [
    'AI-Powered-Sign-Language-to-Speech',
    'Ashiopix_Ecommerce-website',
    'podmind-ai-kubernetes-intelligence',
    'Telemedicine-Platform',
    'Whatsapp-rumor-detector',
    'Electronic_voting_System',
    'AgriVision-AI-Smart-Crop-Disease-Detection-System',
    'BabyJose-Jewelry',
    'CLOUD-MONITORING-AND-ALERTS'
];

const COLORS = [
    { badge: 'badge-pink',   btn: 'btn-pink',   gradStart: '#ec4899', gradEnd: '#7B5CFA' },
    { badge: 'badge-blue',   btn: 'btn-blue',   gradStart: '#3b82f6', gradEnd: '#06b6d4' },
    { badge: 'badge-purple', btn: 'btn-purple', gradStart: '#7B5CFA', gradEnd: '#B75CFA' }
];

// ── Helpers ───────────────────────────────────────────────────────────────────

/** Convert "some-name_like-this" → "Some Name Like This" */
function toTitle(str) {
    return str.replace(/[-_]/g, ' ').replace(/\w\S*/g, w => w.charAt(0).toUpperCase() + w.slice(1));
}

/** Truncate string to maxLen with "..." suffix if needed */
function trunc(str, maxLen) {
    return str.length > maxLen ? str.slice(0, maxLen - 3) + '...' : str;
}

/** Pick a tech label for the project */
function getTech(repo, name) {
    if (repo.language) {
        return trunc(repo.language, 20);
    }
    const desc = repo.description || '';
    if (name.includes('AI') || name.includes('Detection'))        return 'Python / ML';
    if (desc.includes('Web') || name.includes('Platform') || name.includes('Ecommerce')) return 'JavaScript / Web';
    if (name.includes('Cloud') || name.includes('Kubernetes'))    return 'DevOps';
    return 'Development';
}

/** Build a single project card HTML string */
function buildCard(repo, index) {
    const c    = COLORS[index % COLORS.length];
    const raw  = toTitle(repo.name);
    const name = trunc(raw, 25);
    const desc = repo.description || '';
    const url  = repo.html_url;
    const tech = getTech(repo, raw);
    const pid  = `p${index + 1}`;

    return `
            <!-- Project ${index + 1} -->
            <div class="glass-card project-card">
                <div class="project-img-wrapper">
                    <svg width="100%" height="100%" viewBox="0 0 400 220" style="background:#13131f;">
                        <defs>
                            <linearGradient id="${pid}-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%"   stop-color="${c.gradStart}" stop-opacity="0.8"/>
                                <stop offset="100%" stop-color="${c.gradEnd}"   stop-opacity="0.2"/>
                            </linearGradient>
                        </defs>
                        <rect width="400" height="220" fill="url(#${pid}-grad)"/>
                        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
                              fill="#ffffff" font-family="sans-serif" font-size="16"
                              font-weight="700" letter-spacing="1">${name}</text>
                    </svg>
                </div>
                <div class="project-info">
                    <div class="badge-row">
                        <span class="category-badge ${c.badge}">${tech}</span>
                    </div>
                    <h3 class="project-title">${name}</h3>
                    <p class="project-desc">${desc}</p>
                    <a href="${url}" target="_blank" class="view-project-btn ${c.btn}">View on GitHub</a>
                </div>
            </div>`;
}

// ── Main ──────────────────────────────────────────────────────────────────────

const apiOptions = {
    hostname: 'api.github.com',
    path: `/users/${GITHUB_USER}/repos?sort=updated&per_page=100`,
    headers: { 'User-Agent': 'Mozilla/5.0' }
};

https.get(apiOptions, (res) => {
    let raw = '';
    res.on('data', chunk => raw += chunk);
    res.on('end', () => {
        const allRepos = JSON.parse(raw);

        // Filter to only featured projects (preserving order of GOOD_PROJECTS list)
        const projects = GOOD_PROJECTS
            .map(name => allRepos.find(r => r.name === name))
            .filter(Boolean);

        // Build card HTML
        let cardsHtml = projects.map((repo, i) => buildCard(repo, i)).join('');
        cardsHtml += '\n        ';

        // Read index.html
        let html = fs.readFileSync(INDEX_HTML, 'utf8');

        // Replace content between <div class="projects-grid"> ... </section>
        const pattern = /(<div class="projects-grid">).*?(<\/section>)/s;
        const updated = html.replace(pattern, `$1${cardsHtml}</div>\n    $2`);

        // Write back
        fs.writeFileSync(INDEX_HTML, updated, 'utf8');

        console.log(`✅  Updated index.html with ${projects.length} featured projects.`);
    });
}).on('error', err => {
    console.error('❌  Request failed:', err.message);
});
