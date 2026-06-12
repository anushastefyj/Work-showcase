// rewrite_dark.js — Node.js equivalent of rewrite_dark.py
// Writes the full dark-theme index.html and style.css from scratch.
//
// Usage:  node rewrite_dark.js
//   (run from the root of the portfolio folder, i.e. "New Portfolio/")

const fs   = require('fs');
const path = require('path');

const ROOT       = path.join(__dirname, '..');
const INDEX_PATH = path.join(ROOT, 'index.html');
const CSS_PATH   = path.join(ROOT, 'style.css');

// ── HTML ──────────────────────────────────────────────────────────────────────

const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Personal Portfolio of Anusha Stefy J - UI/UX Designer &amp; Web Developer.">
    <title>Anusha Stefy J | Portfolio</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
</head>
<body>
    <!-- Floating Side Navigation -->
    <div class="floating-nav">
        <a href="#home" class="f-nav-item active" aria-label="Home"><i class="ph ph-house"></i></a>
        <a href="#about" class="f-nav-item" aria-label="About"><i class="ph ph-user"></i></a>
        <a href="#portfolio" class="f-nav-item" aria-label="Portfolio"><i class="ph ph-briefcase"></i></a>
        <a href="#contact" class="f-nav-item" aria-label="Contact"><i class="ph ph-phone"></i></a>
    </div>

    <!-- Main Container -->
    <div class="main-container">
        
        <!-- Hero Section Panel (Touches top, left, right. Rounded bottom-right) -->
        <div class="panel-hero">
            <header class="header">
                <a href="#home" class="logo">ASJ</a>
                <nav class="top-nav">
                    <a href="#home" class="nav-link">Home</a>
                    <a href="#about" class="nav-link">About Me</a>
                    <a href="#portfolio" class="nav-link">Portfolio</a>
                    <a href="#contact" class="nav-link contact-pill">Contact Me</a>
                </nav>
            </header>

            <section id="home" class="hero-section">
                <div class="hero-left">
                    <p class="hero-greeting">Hi, My Name Is</p>
                    <h1 class="hero-name">Anusha Stefy J</h1>
                    <div class="hero-title-pill">Front-end Developer / UI Designer</div>
                    <p class="hero-desc">
                        Skills: Full Stack Development, Cloud &amp; DevOps, Machine Learning, Big Data, web designing, Lifetime SSL Solutions, Figma &amp; Adobe XD.
                    </p>
                    <a href="#about" class="hero-link">Learn More About Me</a>
                </div>
                <div class="hero-right">
                    <div class="profile-glow-ring">
                        <img src="assets/profile.png?v=3" alt="Anusha Stefy J" class="profile-img">
                    </div>
                    <div class="location-tag">
                        <i class="ph ph-map-pin"></i> Chennai, India
                    </div>
                </div>
            </section>
        </div>

        <!-- About &amp; Skills Panel (Margin left. Touches right. Rounded left corners) -->
        <section id="about" class="panel-about">
            <h2 class="panel-title white-title">About Me</h2>
            <p class="panel-subtitle">I'm <span class="gold-text">Anusha Stefy J</span>, Full Stack Developer / UI Designer</p>
            <p class="panel-desc">
                I am a skilled Full Stack Developer with a passion for web development and design. Specializing in highly interactive applications, I create visually stunning web experiences and offer scalable cloud solutions. Proficient in React, Python, AWS, and modern design tools like Figma, I ensure seamless functionality and exceptional user experiences.
            </p>

            <h3 class="panel-title white-title" style="margin-top: 4rem; font-size: 2rem;">Skills</h3>
            <div class="skills-grid">
                <div class="skill-pill"><i class="ph ph-globe"></i> React / Angular</div>
                <div class="skill-pill"><i class="ph ph-file-code"></i> JavaScript / HTML</div>
                <div class="skill-pill"><i class="ph ph-desktop"></i> UI/UX Designing</div>
                <div class="skill-pill"><i class="ph ph-server"></i> Backend (Python)</div>
                <div class="skill-pill"><i class="ph ph-cloud"></i> Cloud (AWS) DevOps</div>
                <div class="skill-pill"><i class="ph ph-database"></i> Big Data Engineering</div>
                <div class="skill-pill"><i class="ph ph-brain"></i> Machine Learning</div>
                <div class="skill-pill"><i class="ph ph-app-window"></i> Figma &amp; Adobe</div>
                <div class="skill-pill disabled"><i class="ph ph-lock"></i> Learning...</div>
                <div class="skill-pill disabled"><i class="ph ph-lock"></i> Learning...</div>
                <div class="skill-pill disabled"><i class="ph ph-lock"></i> Learning...</div>
            </div>
        </section>

        <!-- Portfolio Panel (Margin right. Touches left. Rounded right corners) -->
        <section id="portfolio" class="panel-portfolio">
            <h2 class="panel-title gold-title">Portfolio</h2>
            
            <div class="portfolio-layout">
                <!-- Vertical Filters -->
                <div class="portfolio-sidebar">
                    <a href="#" class="port-filter">All</a>
                    <a href="#" class="port-filter active">Web Design</a>
                    <a href="#" class="port-filter">Development</a>
                    <a href="#" class="port-filter">Graphic Design</a>
                    <a href="#" class="port-filter">Wordpress</a>
                    <a href="#" class="port-filter">Copywriting</a>
                </div>

                <!-- Projects Grid -->
                <div class="portfolio-grid">
                    <a href="https://github.com/anushastefyj/podmind-ai-kubernetes-intelligence" target="_blank" class="project-square"></a>
                    <a href="https://github.com/anushastefyj/Telemedicine-Platform" target="_blank" class="project-square"></a>
                    <a href="https://github.com/anushastefyj/CLOUD-MONITORING-AND-ALERTS" target="_blank" class="project-square"></a>
                    <a href="https://github.com/anushastefyj/Whatsapp-rumor-detector" target="_blank" class="project-square"></a>
                    <a href="https://github.com/anushastefyj/AI-Powered-Sign-Language-to-Speech" target="_blank" class="project-square"></a>
                    <a href="https://github.com/anushastefyj/AgriVision-AI-Smart-Crop-Disease-Detection-System" target="_blank" class="project-square"></a>
                </div>
            </div>
        </section>

        <!-- Contact Me Panel (Margin left. Touches right. Rounded left corners) -->
        <section id="contact" class="panel-contact">
            <h2 class="panel-title gold-title">Contact Me</h2>
            
            <div class="contact-box">
                <!-- Left Side: Info -->
                <div class="contact-info-side">
                    <h3 class="contact-sub">Contact Info</h3>
                    <div class="info-item">
                        <i class="ph ph-envelope-simple"></i>
                        <span>anushastefy002@gmail.com</span>
                    </div>
                    <div class="info-item">
                        <i class="ph ph-user"></i>
                        <span>Anusha Stefy J</span>
                    </div>

                    <h3 class="contact-sub" style="margin-top: 2.5rem;">Social Handles</h3>
                    <a href="https://github.com/anushastefyj" target="_blank" class="info-item hover-gold">
                        <i class="ph ph-github-logo"></i>
                        <span>anushastefyj</span>
                    </a>
                    <a href="https://www.linkedin.com/in/anusha-stefy-j-2a43a9378/" target="_blank" class="info-item hover-gold">
                        <i class="ph ph-linkedin-logo"></i>
                        <span>anusha-stefy-j</span>
                    </a>
                    <a href="https://instagram.com/ms_micky_mini/" target="_blank" class="info-item hover-gold">
                        <i class="ph ph-instagram-logo"></i>
                        <span>ms_micky_mini</span>
                    </a>
                </div>

                <!-- Right Side: Form -->
                <div class="contact-form-side">
                    <form class="gold-form">
                        <input type="text" placeholder="Name" required class="gold-input">
                        <input type="email" placeholder="Email" required class="gold-input">
                        <textarea placeholder="Message" rows="5" required class="gold-input" style="resize: vertical;"></textarea>
                        <button type="submit" class="gold-submit-btn">Send</button>
                    </form>
                </div>
            </div>
        </section>

        <!-- Footer (Full width) -->
        <footer class="footer">
            <div class="footer-logo">ASJ</div>
            <div class="footer-nav">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#portfolio">Portfolio</a>
                <a href="#contact">Contact</a>
                <span>&copy; 2026 Anusha Stefy J</span>
            </div>
            <div class="footer-socials">
                <a href="https://www.linkedin.com/in/anusha-stefy-j-2a43a9378/" target="_blank"><i class="ph ph-linkedin-logo"></i></a>
                <a href="https://instagram.com/ms_micky_mini/" target="_blank"><i class="ph ph-instagram-logo"></i></a>
                <a href="https://github.com/anushastefyj" target="_blank"><i class="ph ph-github-logo"></i></a>
                <a href="mailto:anushastefy002@gmail.com" target="_blank"><i class="ph ph-envelope-simple"></i></a>
            </div>
        </footer>

    </div>

    <!-- Certificate Modal -->
    <div id="certModal" class="modal">
        <span class="close-modal" onclick="closeCertModal()">&times;</span>
        <img class="modal-content" id="certImage">
    </div>

    <script src="script.js"></script>
</body>
</html>
`;

// ── CSS ───────────────────────────────────────────────────────────────────────

const cssContent = `@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

:root {
    --bg-page: #40424a;
    --bg-main: #181920;
    --bg-panel-light: #25252d;
    --gold: #d4af37;
    --gold-light: #f2cf9e;
    --gold-muted: rgba(242, 207, 158, 0.2);
    --text-white: #ffffff;
    --text-gray: #a0a0a5;
    --border-dark: #3a3a45;
    --font-main: 'Poppins', sans-serif;
    --panel-radius: 80px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-page);
    color: var(--text-white);
    font-family: var(--font-main);
    line-height: 1.6;
    overflow-x: hidden;
}

a {
    text-decoration: none;
    color: inherit;
}

/* Floating Navigation */
.floating-nav {
    position: fixed;
    right: 30px;
    top: 50%;
    transform: translateY(-50%);
    background: var(--bg-panel-light);
    border: 1px solid var(--gold-muted);
    border-radius: 40px;
    padding: 1rem 0.6rem;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    z-index: 1000;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.f-nav-item {
    color: var(--text-gray);
    font-size: 1.4rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.f-nav-item:hover, .f-nav-item.active {
    color: var(--gold-light);
    transform: scale(1.1);
}

.main-container {
    max-width: 1400px;
    margin: 0 auto;
    background-color: var(--bg-page);
}

.panel-hero {
    background: var(--bg-main);
    border-bottom-right-radius: var(--panel-radius);
    padding: 0 6rem 5rem 6rem;
    margin-bottom: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

.panel-about {
    background: var(--bg-main);
    border-top-left-radius: var(--panel-radius);
    border-bottom-left-radius: var(--panel-radius);
    margin-left: 5rem;
    padding: 5rem 6rem;
    margin-bottom: 2rem;
    box-shadow: -20px 20px 40px rgba(0,0,0,0.2);
}

.panel-portfolio {
    background: var(--bg-main);
    border-top-right-radius: var(--panel-radius);
    border-bottom-right-radius: var(--panel-radius);
    margin-right: 5rem;
    padding: 5rem 6rem;
    margin-bottom: 2rem;
    box-shadow: 20px 20px 40px rgba(0,0,0,0.2);
}

.panel-contact {
    background: var(--bg-main);
    border-top-left-radius: var(--panel-radius);
    border-bottom-left-radius: var(--panel-radius);
    margin-left: 5rem;
    padding: 5rem 6rem;
    box-shadow: -20px 20px 40px rgba(0,0,0,0.2);
}

.footer {
    background: var(--bg-main);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem 6rem;
    border-top: 1px solid var(--gold-muted);
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 3rem 0;
}

.logo {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--gold-light);
    letter-spacing: 2px;
}

.top-nav {
    display: flex;
    align-items: center;
    gap: 3rem;
}

.nav-link {
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--text-white);
    transition: 0.3s;
}

.nav-link:hover { color: var(--gold-light); }

.contact-pill {
    background: var(--gold-light);
    color: var(--bg-main) !important;
    padding: 0.5rem 1.5rem;
    border-radius: 30px;
    font-weight: 600;
}

.contact-pill:hover { background: #fff; }

.hero-section {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 50vh;
}

.hero-left { flex: 1.2; padding-right: 2rem; }

.hero-greeting {
    font-size: 1.1rem;
    font-weight: 500;
    color: var(--text-white);
    margin-bottom: 0.5rem;
}

.hero-name {
    font-size: 3.5rem;
    font-weight: 700;
    color: var(--gold-light);
    line-height: 1.1;
    margin-bottom: 1rem;
}

.hero-title-pill {
    display: inline-block;
    border: 1px solid var(--gold-light);
    color: var(--gold-light);
    padding: 0.4rem 1.2rem;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
    background: rgba(242, 207, 158, 0.05);
}

.hero-desc {
    font-size: 0.85rem;
    color: var(--text-white);
    margin-bottom: 1.5rem;
    max-width: 500px;
    line-height: 1.8;
}

.hero-link {
    font-size: 0.85rem;
    color: var(--text-white);
    text-decoration: underline;
    text-decoration-color: var(--text-white);
    text-underline-offset: 4px;
    font-weight: 500;
    transition: 0.3s;
}

.hero-link:hover {
    color: var(--gold-light);
    text-decoration-color: var(--gold-light);
}

.hero-right {
    flex: 0.8;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.profile-glow-ring {
    width: 250px;
    height: 250px;
    border-radius: 50%;
    padding: 6px;
    background: linear-gradient(135deg, var(--gold-light) 0%, transparent 50%, var(--gold) 100%);
    box-shadow: 0 0 30px rgba(212, 175, 55, 0.15);
}

.profile-img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    background: var(--bg-main);
}

.location-tag {
    font-size: 0.85rem;
    color: var(--text-white);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 500;
}

.panel-title {
    font-size: 2.5rem;
    font-weight: 600;
    text-align: center;
    margin-bottom: 1.5rem;
}

.white-title { color: var(--text-white); }
.gold-title  { color: var(--gold-light); }

.panel-subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: var(--text-gray);
    margin-bottom: 1.5rem;
}

.gold-text { color: var(--gold-light); font-weight: 600; }

.panel-desc {
    text-align: center;
    font-size: 0.85rem;
    color: var(--text-white);
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.8;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-top: 2rem;
}

.skill-pill {
    background: rgba(255,255,255,0.03);
    border: 1px solid var(--gold-muted);
    color: var(--gold-light);
    padding: 0.8rem 1rem;
    border-radius: 8px;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    transition: 0.3s;
    text-align: center;
}

.skill-pill:hover {
    background: rgba(242, 207, 158, 0.05);
    border-color: var(--gold-light);
    transform: translateY(-2px);
}

.skill-pill.disabled {
    color: var(--text-gray);
    border-color: transparent;
    background: rgba(255,255,255,0.02);
    cursor: not-allowed;
}

.skill-pill.disabled:hover { transform: none; }

.portfolio-layout {
    display: flex;
    gap: 4rem;
    margin-top: 3rem;
}

.portfolio-sidebar {
    width: 200px;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    border-right: 1px solid var(--gold-muted);
    padding-right: 1rem;
}

.port-filter {
    font-size: 0.9rem;
    color: var(--text-white);
    font-weight: 500;
    transition: 0.3s;
}

.port-filter:hover { color: var(--gold-light); }

.port-filter.active {
    color: var(--gold-light);
    text-decoration: underline;
    text-decoration-color: var(--gold-light);
    text-underline-offset: 4px;
}

.portfolio-grid {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
}

.project-square {
    aspect-ratio: 1;
    border: 1px solid var(--gold-muted);
    border-radius: 8px;
    background: rgba(255,255,255,0.02);
    transition: 0.3s;
}

.project-square:hover {
    border-color: var(--gold-light);
    background: rgba(242, 207, 158, 0.05);
    transform: scale(1.02);
}

.contact-box {
    display: flex;
    border: 1px solid var(--gold-muted);
    border-radius: 12px;
    margin-top: 3rem;
    overflow: hidden;
    background: rgba(255,255,255,0.02);
}

.contact-info-side {
    flex: 1;
    padding: 3rem;
    border-right: 1px solid var(--gold-muted);
}

.contact-sub {
    font-size: 1.1rem;
    color: var(--text-white);
    margin-bottom: 1.5rem;
    font-weight: 600;
}

.info-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    color: var(--text-white);
    font-size: 0.85rem;
    transition: 0.3s;
}

.info-item i { font-size: 1.2rem; color: var(--gold-light); }
.hover-gold:hover { color: var(--gold-light); }

.contact-form-side { flex: 1.5; padding: 3rem; }

.gold-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.gold-input {
    width: 100%;
    background: transparent;
    border: 1px solid var(--gold-muted);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    color: var(--text-white);
    font-family: var(--font-main);
    font-size: 0.85rem;
    transition: 0.3s;
}

.gold-input:focus { outline: none; border-color: var(--gold-light); }

.gold-submit-btn {
    align-self: center;
    background: var(--gold-light);
    color: var(--bg-main);
    border: none;
    padding: 0.8rem 3rem;
    border-radius: 30px;
    font-weight: 600;
    font-size: 0.9rem;
    cursor: pointer;
    margin-top: 1rem;
    transition: 0.3s;
}

.gold-submit-btn:hover { background: #fff; }

.footer-logo { font-weight: 800; color: var(--gold-light); letter-spacing: 2px; }

.footer-nav {
    display: flex;
    gap: 1.5rem;
    font-size: 0.8rem;
    color: var(--text-gray);
}

.footer-nav a:hover { color: var(--text-white); }

.footer-socials { display: flex; gap: 1rem; font-size: 1.2rem; color: var(--text-gray); }
.footer-socials a:hover { color: var(--text-white); }

.modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0; top: 0; width: 100%; height: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.85);
    backdrop-filter: blur(8px);
}

.modal-content {
    margin: auto; display: block; width: 80%; max-width: 800px;
    margin-top: 5%; border-radius: 10px; box-shadow: 0 0 30px rgba(0,0,0,0.8);
    border: 2px solid var(--gold-light);
    animation: zoom 0.3s ease;
}

@keyframes zoom { from { transform: scale(0.8) } to { transform: scale(1) } }

.close-modal {
    position: absolute; top: 20px; right: 35px; color: var(--gold-light);
    font-size: 40px; font-weight: bold; cursor: pointer; transition: 0.3s;
}

.close-modal:hover { color: #fff; }

@media(max-width: 1024px) {
    .main-container { padding: 0 2rem; }
    .floating-nav { display: none; }
    .panel-hero { padding: 0 3rem 4rem 3rem; border-bottom-right-radius: 60px; }
    .panel-about { margin-left: 2rem; padding: 4rem 3rem; border-top-left-radius: 60px; border-bottom-left-radius: 60px; }
    .panel-portfolio { margin-right: 2rem; padding: 4rem 3rem; border-top-right-radius: 60px; border-bottom-right-radius: 60px; }
    .panel-contact { margin-left: 2rem; padding: 4rem 3rem; border-top-left-radius: 60px; border-bottom-left-radius: 60px; }
    .hero-section { flex-direction: column; text-align: center; gap: 3rem; }
    .hero-left { padding-right: 0; display: flex; flex-direction: column; align-items: center; }
    .portfolio-layout { flex-direction: column; }
    .portfolio-sidebar { width: 100%; border-right: none; border-bottom: 1px solid var(--gold-muted); padding-bottom: 1rem; flex-direction: row; flex-wrap: wrap; justify-content: center; }
    .portfolio-grid { grid-template-columns: repeat(2, 1fr); }
    .contact-box { flex-direction: column; }
    .contact-info-side { border-right: none; border-bottom: 1px solid var(--gold-muted); }
    .skills-grid { grid-template-columns: repeat(2, 1fr); }
}

@media(max-width: 768px) {
    .portfolio-grid { grid-template-columns: 1fr; }
    .skills-grid { grid-template-columns: 1fr; }
    .footer { flex-direction: column; gap: 1rem; text-align: center; }
    .top-nav { display: none; }
    .panel-hero { border-bottom-right-radius: 40px; padding: 0 1.5rem 3rem 1.5rem; }
    .panel-about { margin-left: 1rem; padding: 3rem 1.5rem; border-top-left-radius: 40px; border-bottom-left-radius: 40px; }
    .panel-portfolio { margin-right: 1rem; padding: 3rem 1.5rem; border-top-right-radius: 40px; border-bottom-right-radius: 40px; }
    .panel-contact { margin-left: 1rem; padding: 3rem 1.5rem; border-top-left-radius: 40px; border-bottom-left-radius: 40px; }
}
`;

// ── Write files ───────────────────────────────────────────────────────────────

fs.writeFileSync(INDEX_PATH, htmlContent, 'utf8');
fs.writeFileSync(CSS_PATH,   cssContent,  'utf8');

console.log('✅  Dark theme written to index.html and style.css');
