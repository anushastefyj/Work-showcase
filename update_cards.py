import urllib.request, json, re

req = urllib.request.Request("https://api.github.com/users/anushastefyj/repos?sort=updated&per_page=100", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

# List of explicitly "good" projects to feature
good_projects = [
    'AI-Powered-Sign-Language-to-Speech',
    'Ashiopix_Ecommerce-website',
    'podmind-ai-kubernetes-intelligence',
    'Telemedicine-Platform',
    'Whatsapp-rumor-detector',
    'Electronic_voting_System',
    'AgriVision-AI-Smart-Crop-Disease-Detection-System',
    'BabyJose-Jewelry',
    'CLOUD-MONITORING-AND-ALERTS'
]

projects = [r for r in data if r['name'] in good_projects]

colors = [
    {"badge": "badge-pink", "btn": "btn-pink", "grad_start": "#ec4899", "grad_end": "#7B5CFA"},
    {"badge": "badge-blue", "btn": "btn-blue", "grad_start": "#3b82f6", "grad_end": "#06b6d4"},
    {"badge": "badge-purple", "btn": "btn-purple", "grad_start": "#7B5CFA", "grad_end": "#B75CFA"}
]

cards_html = ""
for i, p in enumerate(projects):
    c = colors[i % 3]
    name = p['name'].replace('-', ' ').replace('_', ' ').title()
    if len(name) > 25:
        name = name[:22] + "..."
        
    desc = p['description'] or ""
    url = p['html_url']
    
    # Use the primary language or a fallback tech stack
    tech = p.get('language')
    if not tech:
        if "AI" in name or "Detection" in name:
            tech = "Python / ML"
        elif "Web" in desc or "Platform" in name or "Ecommerce" in name:
            tech = "JavaScript / Web"
        elif "Cloud" in name or "Kubernetes" in name:
            tech = "DevOps"
        else:
            tech = "Development"
            
    # Keep tech short
    if len(tech) > 20:
        tech = tech[:17] + "..."
    
    card = f"""
            <!-- Project {i+1} -->
            <div class="glass-card project-card">
                <div class="project-img-wrapper">
                    <svg width="100%" height="100%" viewBox="0 0 400 220" style="background:#13131f;">
                        <defs>
                            <linearGradient id="p{i+1}-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="{c['grad_start']}" stop-opacity="0.8"/>
                                <stop offset="100%" stop-color="{c['grad_end']}" stop-opacity="0.2"/>
                            </linearGradient>
                        </defs>
                        <rect width="400" height="220" fill="url(#p{i+1}-grad)"/>
                        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="700" letter-spacing="1">{name}</text>
                    </svg>
                </div>
                <div class="project-info">
                    <div class="badge-row">
                        <span class="category-badge {c['badge']}">{tech}</span>
                    </div>
                    <h3 class="project-title">{name}</h3>
                    <p class="project-desc">{desc}</p>
                    <a href="{url}" target="_blank" class="view-project-btn {c['btn']}">View on GitHub</a>
                </div>
            </div>"""
    cards_html += card

cards_html += "\n        "

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
new_html = re.sub(r'(<div class="projects-grid">).*?(</section>)', r'\1' + cards_html + '</div>\n    \2', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Updated index.html with {len(projects)} featured projects showcasing their tech stacks!")
