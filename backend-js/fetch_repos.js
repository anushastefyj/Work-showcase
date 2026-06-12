// fetch_repos.js — Node.js equivalent of fetch_repos.py
// Fetches all public repos for anushastefyj from GitHub API and prints their names.
//
// Usage:  node fetch_repos.js

const https = require('https');

const options = {
    hostname: 'api.github.com',
    path: '/users/anushastefyj/repos?sort=updated&per_page=100',
    headers: { 'User-Agent': 'Mozilla/5.0' }
};

https.get(options, (res) => {
    let raw = '';
    res.on('data', chunk => raw += chunk);
    res.on('end', () => {
        const repos = JSON.parse(raw);
        const names = repos
            .filter(r => r.name !== 'anushastefyj')
            .map(r => r.name);
        console.log(names);
    });
}).on('error', err => {
    console.error('Request failed:', err.message);
});
