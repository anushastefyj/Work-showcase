import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Personal Portfolio of Anusha Stefy J - UI/UX Designer & Web Developer.">
    <title>Anusha Stefy J | Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Top Bar -->
    <div class="top-bar">
        <div class="top-bar-content">
            <span class="top-info">anushastefy002@gmail.com</span>
        </div>
    </div>

    <!-- Header / Sticky Navigation -->
    <header id="header" class="split-header">
        <div class="nav-container split-nav">
            <a href="#home" class="logo dark-logo" id="logo">
                <svg width="40" height="40" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px; vertical-align: middle;">
                    <path d="M20 20 L80 20 L40 80 L20 80 Z" />
                    <text x="50" y="65" font-family="sans-serif" font-weight="bold" font-size="40" fill="currentColor" stroke="none" text-anchor="middle">AS</text>
                </svg>
            </a>
            <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-links split-links" id="nav-links">
                <li><a href="#about" class="nav-item">About me</a></li>
                <li><a href="#skills" class="nav-item">Skills</a></li>
                <li><a href="#portfolio" class="nav-item">Portfolio</a></li>
                <li><a href="#contact" class="nav-item contact-btn-nav">CONTACT ME</a></li>
            </ul>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero split-hero">
        <div class="hero-bg-split"></div>
        <div class="hero-content-split">
            <div class="hero-left">
                <p class="hero-greeting">Hi, I am</p>
                <h1 class="hero-name-split">Anusha Stefy J</h1>
                <p class="hero-subtitle-split">Front-end Developer / UI Designer</p>
                
                <div class="hero-socials">
                    <a href="mailto:anushastefy002@gmail.com" class="social-square" aria-label="Email"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></a>
                    <a href="https://github.com/anushastefyj" class="social-square" aria-label="GitHub"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></a>
                    <a href="https://www.linkedin.com/in/anusha-stefy-j-2a43a9378/" class="social-square" aria-label="LinkedIn"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                </div>
            </div>
            <div class="hero-right">
                <img src="assets/profile.png?v=2" alt="Anusha Stefy J" class="hero-profile-split">
            </div>
        </div>
    </section>

    <!-- IT Banner Section -->
    <div class="it-banner">
        <div class="it-banner-content">
            <p>IT ENGINEER &middot; DEVELOPER &middot; DESIGNER</p>
            <p class="it-desc">Combining design thinking with technical expertise to build scalable and beautiful applications.</p>
        </div>
        <div class="it-watermark">IT</div>
    </div>

    <!-- About Me Section -->
    <section id="about" class="light-section">
        <div class="section-container">
            <h2 class="bordered-title">ABOUT ME</h2>
            <p class="about-text">
                I am a passionate Front-end Developer and UI Designer dedicated to building highly responsive, interactive interfaces and scalable backend architectures. I specialize in turning complex problems into elegant, intuitive designs.
            </p>
            <a href="#portfolio" class="explore-btn">EXPLORE</a>

            <div class="about-details">
                <div class="detail-item">
                    <h4>DESIGN</h4>
                    <p>I can design beautiful, user-centric interfaces.</p>
                </div>
                <div class="detail-item">
                    <h4>DEVELOPMENT</h4>
                    <p>I can build scalable full-stack applications.</p>
                </div>
                <div class="detail-item">
                    <h4>MAINTENANCE</h4>
                    <p>I can deploy, scale, and monitor cloud systems.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="light-section gray-bg">
        <div class="section-container">
            <h2 class="bordered-title">SKILLS</h2>
            
            <div class="skills-category">
                <h3 class="category-title">USING NOW:</h3>
                <div class="skills-icon-grid">
                    <div class="skill-icon-item"><span class="icon">🌐</span><span class="label">React</span></div>
                    <div class="skill-icon-item"><span class="icon">💻</span><span class="label">JavaScript</span></div>
                    <div class="skill-icon-item"><span class="icon">🎨</span><span class="label">CSS / HTML</span></div>
                    <div class="skill-icon-item"><span class="icon">🐍</span><span class="label">Python</span></div>
                </div>
            </div>

            <div class="skills-category">
                <h3 class="category-title">LEARNING:</h3>
                <div class="skills-icon-grid">
                    <div class="skill-icon-item"><span class="icon">🤖</span><span class="label">Machine Learning</span></div>
                    <div class="skill-icon-item"><span class="icon">☁️</span><span class="label">Cloud DevOps</span></div>
                    <div class="skill-icon-item"><span class="icon">📊</span><span class="label">Big Data</span></div>
                </div>
            </div>

            <div class="skills-category">
                <h3 class="category-title">OTHER SKILLS:</h3>
                <div class="skills-icon-grid">
                    <div class="skill-icon-item"><span class="icon">🗄️</span><span class="label">Databases</span></div>
                    <div class="skill-icon-item"><span class="icon">⚙️</span><span class="label">Backend</span></div>
                    <div class="skill-icon-item"><span class="icon">📱</span><span class="label">Mobile UI</span></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio-section">
        <div class="portfolio-header">
            <h2 class="bordered-title dark-title">PORTFOLIO</h2>
        </div>
        
        <div class="portfolio-filters">
            <a href="#" class="filter-item active">ALL</a>
            <a href="#" class="filter-item">CODED</a>
            <a href="#" class="filter-item">DESIGNED</a>
        </div>

        <div class="portfolio-grid">
            <!-- Project 1 -->
            <div class="portfolio-item">
                <div class="portfolio-img-placeholder" style="background: linear-gradient(135deg, #ec4899, #7B5CFA);">
                    <div class="portfolio-hover">
                        <h3>Podmind Ai Kubernetes</h3>
                        <a href="https://github.com/anushastefyj/podmind-ai-kubernetes-intelligence" target="_blank">View GitHub</a>
                    </div>
                </div>
            </div>
            <!-- Project 2 -->
            <div class="portfolio-item">
                <div class="portfolio-img-placeholder" style="background: linear-gradient(135deg, #3b82f6, #06b6d4);">
                    <div class="portfolio-hover">
                        <h3>Telemedicine Platform</h3>
                        <a href="https://github.com/anushastefyj/Telemedicine-Platform" target="_blank">View GitHub</a>
                    </div>
                </div>
            </div>
            <!-- Project 3 -->
            <div class="portfolio-item">
                <div class="portfolio-img-placeholder" style="background: linear-gradient(135deg, #7B5CFA, #B75CFA);">
                    <div class="portfolio-hover">
                        <h3>Cloud Monitoring</h3>
                        <a href="https://github.com/anushastefyj/CLOUD-MONITORING-AND-ALERTS" target="_blank">View GitHub</a>
                    </div>
                </div>
            </div>
            <!-- Project 4 -->
            <div class="portfolio-item">
                <div class="portfolio-img-placeholder" style="background: linear-gradient(135deg, #10b981, #3b82f6);">
                    <div class="portfolio-hover">
                        <h3>Whatsapp Rumor Detector</h3>
                        <a href="https://github.com/anushastefyj/Whatsapp-rumor-detector" target="_blank">View GitHub</a>
                    </div>
                </div>
            </div>
            <!-- Project 5 -->
            <div class="portfolio-item">
                <div class="portfolio-img-placeholder" style="background: linear-gradient(135deg, #f59e0b, #ef4444);">
                    <div class="portfolio-hover">
                        <h3>Sign Language Converter</h3>
                        <a href="https://github.com/anushastefyj/AI-Powered-Sign-Language-to-Speech" target="_blank">View GitHub</a>
                    </div>
                </div>
            </div>
            <!-- Project 6 -->
            <div class="portfolio-item">
                <div class="portfolio-img-placeholder" style="background: linear-gradient(135deg, #8b5cf6, #ec4899);">
                    <div class="portfolio-hover">
                        <h3>AgriVision AI</h3>
                        <a href="https://github.com/anushastefyj/AgriVision-AI-Smart-Crop-Disease-Detection-System" target="_blank">View GitHub</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Certificates Section -->
    <section id="certificates" class="light-section gray-bg">
        <div class="section-container">
            <h2 class="bordered-title">ACHIEVEMENTS</h2>
            <div class="certs-list">
                <div class="cert-item">
                    <span class="cert-icon">🏆</span>
                    <div class="cert-details">
                        <h4>Data Engineering Virtual Internship</h4>
                        <p>AWS Academy / EduSkills</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert1.png')">View</button>
                </div>
                <div class="cert-item">
                    <span class="cert-icon">☁️</span>
                    <div class="cert-details">
                        <h4>AWS Cloud Essentials</h4>
                        <p>AWS Training & Certification</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert2.png')">View</button>
                </div>
                <div class="cert-item">
                    <span class="cert-icon">📄</span>
                    <div class="cert-details">
                        <h4>Paper Presentation: AI/ML Predictive Analysis</h4>
                        <p>CRATE-2025, VEMU Institute</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert3.png')">View</button>
                </div>
                <div class="cert-item">
                    <span class="cert-icon">📊</span>
                    <div class="cert-details">
                        <h4>Introduction to Data Science</h4>
                        <p>Cisco Networking Academy</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert4.png')">View</button>
                </div>
                <div class="cert-item">
                    <span class="cert-icon">💼</span>
                    <div class="cert-details">
                        <h4>Cloud Computing Internship</h4>
                        <p>Codtech IT Solutions</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert5.png')">View</button>
                </div>
                <div class="cert-item">
                    <span class="cert-icon">🤖</span>
                    <div class="cert-details">
                        <h4>GEN-AI Virtual Internship</h4>
                        <p>AWS Academy / EduSkills</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert6.png')">View</button>
                </div>
                <div class="cert-item">
                    <span class="cert-icon">🥇</span>
                    <div class="cert-details">
                        <h4>HackHouse Web Dev Hackathon</h4>
                        <p>Consolation Prize - Vaultsphere AI</p>
                    </div>
                    <button class="cert-view-btn" onclick="openCertModal('assets/cert7.png')">View</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="light-section">
        <div class="section-container">
            <h2 class="bordered-title">CONTACT</h2>
            <p class="about-text">Have a project in mind? Fill out the form below and let's create something amazing.</p>
            
            <form class="minimal-form">
                <div class="form-row">
                    <input type="text" placeholder="ENTER YOUR NAME*" required>
                </div>
                <div class="form-row">
                    <input type="email" placeholder="ENTER YOUR EMAIL*" required>
                </div>
                <div class="form-row">
                    <input type="text" placeholder="PHONE NUMBER">
                </div>
                <div class="form-row">
                    <textarea placeholder="YOUR MESSAGE*" rows="4" required></textarea>
                </div>
                <button type="submit" class="submit-line-btn">SUBMIT</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer class="dark-footer">
        <div class="footer-socials">
            <a href="https://www.linkedin.com/in/anusha-stefy-j-2a43a9378/" aria-label="LinkedIn" target="_blank" rel="noopener noreferrer"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="https://github.com/anushastefyj" aria-label="GitHub" target="_blank" rel="noopener noreferrer"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></a>
            <a href="https://instagram.com/ms_micky_mini/" aria-label="Instagram" target="_blank" rel="noopener noreferrer"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        </div>
        <p>@ 2026 Anusha Stefy J. All Rights Reserved.</p>
    </footer>

    <!-- Certificate Modal -->
    <div id="certModal" class="modal">
        <span class="close-modal" onclick="closeCertModal()">&times;</span>
        <img class="modal-content" id="certImage">
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

css_content = """@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

:root {
    --bg-light: #e5e5e5;
    --bg-gray: #d4d4d4;
    --bg-dark: #111111;
    --bg-darker: #080808;
    --text-dark: #111111;
    --text-light: #ffffff;
    --text-muted: #666666;
    --font-main: 'Montserrat', sans-serif;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-light);
    color: var(--text-dark);
    font-family: var(--font-main);
    line-height: 1.6;
    overflow-x: hidden;
}

/* Top Bar */
.top-bar {
    background-color: #000;
    color: #fff;
    padding: 0.5rem 2rem;
    font-size: 0.75rem;
    position: relative;
    z-index: 101;
}

.top-bar-content {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: flex-end;
    gap: 2rem;
}

/* Split Header */
.split-header {
    position: absolute;
    top: 30px; /* Below top bar */
    width: 100%;
    z-index: 100;
    background: transparent;
}

.split-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 2rem;
    max-width: 1400px;
    margin: 0 auto;
}

.dark-logo {
    color: var(--text-dark);
    display: flex;
    align-items: center;
    font-weight: 800;
    text-decoration: none;
}

.split-links {
    display: flex;
    gap: 2rem;
    align-items: center;
    list-style: none;
}

.split-links .nav-item {
    color: var(--text-light);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.3s ease;
}

.split-links .nav-item:hover {
    color: #ccc;
}

.contact-btn-nav {
    background: #ffffff;
    color: #000000 !important;
    padding: 0.6rem 1.5rem;
    border-radius: 30px;
}

/* Hero Section */
.split-hero {
    position: relative;
    width: 100%;
    height: 100vh;
    display: flex;
}

.hero-bg-split {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    background: linear-gradient(105deg, var(--bg-light) 45%, var(--bg-dark) 45.1%);
}

.hero-content-split {
    position: relative;
    z-index: 10;
    display: flex;
    width: 100%;
    height: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding-top: 80px;
}

.hero-left {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 4rem;
}

.hero-greeting {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.hero-name-split {
    font-size: 4.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1rem;
    letter-spacing: -2px;
}

.hero-subtitle-split {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-muted);
    margin-bottom: 3rem;
}

.hero-socials {
    display: flex;
    gap: 1.5rem;
}

.social-square {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    background-color: #d1d1d1;
    color: #111;
    border-radius: 4px;
    text-decoration: none;
    transition: 0.3s;
}

.social-square:hover {
    background-color: #111;
    color: #fff;
}

.hero-right {
    flex: 1;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    position: relative;
}

.hero-profile-split {
    width: 80%;
    max-width: 600px;
    object-fit: cover;
}

/* IT Banner */
.it-banner {
    background-color: #1a1a1a;
    color: #ffffff;
    padding: 3rem 2rem;
    position: relative;
    overflow: hidden;
    text-align: center;
}

.it-banner-content {
    position: relative;
    z-index: 2;
}

.it-banner-content p:first-child {
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}

.it-desc {
    color: #999;
    font-size: 0.9rem;
}

.it-watermark {
    position: absolute;
    right: -5%;
    bottom: -40%;
    font-size: 15rem;
    font-weight: 900;
    color: rgba(255,255,255,0.03);
    z-index: 1;
    line-height: 1;
}

/* Base Layout for Light Sections */
.light-section {
    padding: 6rem 2rem;
    background-color: var(--bg-light);
    text-align: center;
}

.gray-bg {
    background-color: var(--bg-gray);
}

.section-container {
    max-width: 800px;
    margin: 0 auto;
}

/* Bordered Title */
.bordered-title {
    display: inline-block;
    padding: 0.5rem 2rem;
    border: 3px solid var(--text-dark);
    font-size: 1.25rem;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 3rem;
}

.dark-title {
    border-color: var(--text-light);
    color: var(--text-light);
}

/* About Section */
.about-text {
    font-size: 1rem;
    color: var(--text-muted);
    margin-bottom: 2rem;
}

.explore-btn {
    display: inline-block;
    padding: 0.5rem 1.5rem;
    border-bottom: 2px solid var(--text-dark);
    color: var(--text-dark);
    text-decoration: none;
    font-weight: 700;
    margin-bottom: 4rem;
    letter-spacing: 1px;
    transition: 0.3s;
}

.explore-btn:hover {
    color: var(--text-muted);
    border-color: var(--text-muted);
}

.about-details {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    text-align: left;
}

.detail-item h4 {
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.detail-item p {
    font-size: 0.85rem;
    color: var(--text-muted);
}

/* Skills Section */
.skills-category {
    margin-bottom: 4rem;
}

.category-title {
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 2rem;
}

.skills-icon-grid {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
}

.skill-icon-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.skill-icon-item .icon {
    font-size: 2.5rem;
}

.skill-icon-item .label {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
}

/* Portfolio Section */
.portfolio-section {
    background-color: var(--bg-dark);
}

.portfolio-header {
    background-image: url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80');
    background-size: cover;
    background-position: center;
    padding: 6rem 2rem;
    text-align: center;
    position: relative;
}

.portfolio-header::before {
    content: '';
    position: absolute;
    top:0; left:0; width:100%; height:100%;
    background: rgba(0,0,0,0.5);
}

.portfolio-header .bordered-title {
    position: relative;
    z-index: 2;
}

.portfolio-filters {
    background-color: var(--bg-darker);
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 1.5rem;
}

.filter-item {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 1px;
}

.filter-item.active, .filter-item:hover {
    color: var(--text-light);
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

.portfolio-item {
    position: relative;
    width: 100%;
    aspect-ratio: 16/9;
    overflow: hidden;
}

.portfolio-img-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.portfolio-hover {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.portfolio-item:hover .portfolio-hover {
    opacity: 1;
}

.portfolio-hover h3 {
    color: #fff;
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.portfolio-hover a {
    color: #fff;
    border: 1px solid #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    font-size: 0.8rem;
    transition: 0.3s;
}

.portfolio-hover a:hover {
    background: #fff;
    color: #000;
}

/* Certificates */
.certs-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    text-align: left;
}

.cert-item {
    display: flex;
    align-items: center;
    background: rgba(255,255,255,0.5);
    padding: 1rem 1.5rem;
    border-radius: 8px;
}

.cert-icon {
    font-size: 1.5rem;
    margin-right: 1.5rem;
}

.cert-details h4 {
    font-size: 1rem;
    margin-bottom: 0.2rem;
}

.cert-details p {
    font-size: 0.85rem;
    color: var(--text-muted);
}

.cert-view-btn {
    margin-left: auto;
    background: transparent;
    border: 1px solid var(--text-dark);
    padding: 0.4rem 1rem;
    cursor: pointer;
    font-weight: 600;
    transition: 0.3s;
}

.cert-view-btn:hover {
    background: var(--text-dark);
    color: var(--text-light);
}

/* Contact */
.minimal-form {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.form-row input, .form-row textarea {
    width: 100%;
    background: transparent;
    border: none;
    border-bottom: 2px solid var(--text-dark);
    padding: 0.5rem 0;
    font-family: var(--font-main);
    font-size: 0.9rem;
    color: var(--text-dark);
    outline: none;
}

.form-row textarea {
    resize: vertical;
}

.submit-line-btn {
    background: transparent;
    border: none;
    border-bottom: 2px solid var(--text-dark);
    padding: 0.5rem 2rem;
    font-weight: 700;
    align-self: center;
    cursor: pointer;
    letter-spacing: 2px;
    margin-top: 1rem;
}

/* Footer */
.dark-footer {
    background: var(--bg-darker);
    color: var(--text-muted);
    text-align: center;
    padding: 4rem 2rem;
}

.footer-socials {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.footer-socials a {
    color: var(--text-light);
    transition: 0.3s;
}

.footer-socials a:hover {
    color: var(--text-muted);
}

/* Modal */
.modal {
    display: none; 
    position: fixed; 
    z-index: 1000; 
    left: 0; top: 0; width: 100%; height: 100%; 
    overflow: auto; 
    background-color: rgba(0,0,0,0.8);
    backdrop-filter: blur(5px);
}

.modal-content {
    margin: auto; display: block; width: 80%; max-width: 800px;
    margin-top: 5%; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.5);
    animation: zoom 0.3s ease;
}

@keyframes zoom { from {transform:scale(0.8)} to {transform:scale(1)} }

.close-modal {
    position: absolute; top: 20px; right: 35px; color: #f1f1f1;
    font-size: 40px; font-weight: bold; cursor: pointer; transition: 0.3s;
}

/* Responsive */
@media(max-width: 768px) {
    .hero-bg-split { background: linear-gradient(180deg, var(--bg-light) 50%, var(--bg-dark) 50.1%); }
    .hero-content-split { flex-direction: column; padding-top: 100px; }
    .hero-left { padding: 2rem; text-align: center; align-items: center; }
    .hero-right { align-items: flex-end; }
    .split-nav { flex-direction: column; }
    .split-links { display: none; }
    .about-details { grid-template-columns: 1fr; }
    .portfolio-grid { grid-template-columns: 1fr; }
    .menu-toggle { display: flex; }
    .cert-item { flex-direction: column; text-align: center; gap: 1rem; }
    .cert-icon { margin-right: 0; }
    .cert-view-btn { margin-left: 0; }
}
"""

with open(r"c:\Users\anush\Desktop\anuprojects\New Portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open(r"c:\Users\anush\Desktop\anuprojects\New Portfolio\style.css", "w", encoding="utf-8") as f:
    f.write(css_content)
