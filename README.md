<<<<<<< HEAD
# Personal Portfolio Website

## Overview
This is a responsive personal portfolio website designed to showcase skills, projects, certifications, and contact information in a clean and modern UI.

## Tech Stack
- HTML
- CSS
- JavaScript
- Phosphor Icons
- Optional Python utilities for automation or backend features

## Project Structure
- index.html Main page
- style.css Styling for the website
- script.js Interactivity and animations
- assets Folder for images and icons

## Sections
- Hero section Introduction
- About section Personal details
- Portfolio section Project cards
- Certifications section Achievements
- Contact section Contact form and social links

## Setup
- Clone the repository
- Open index.html in browser
- Or use Live Server for best experience

## Usage
- Use navigation bar to explore sections
- View projects in portfolio section
- Submit messages through contact form
=======
# 🚀 Anusha Stefy J — Personal Portfolio

> **MLOps / AI Platform Engineer** | Architecting scalable AI infrastructure, robust MLOps pipelines, and high-performance model deployment platforms.

[![Live Portfolio](https://img.shields.io/badge/Portfolio-Live-gold?style=for-the-badge&logo=google-chrome)](https://anushastefyj.github.io)
[![GitHub](https://img.shields.io/badge/GitHub-anushastefyj-black?style=for-the-badge&logo=github)](https://github.com/anushastefyj)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Anusha%20Stefy%20J-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/anusha-stefy-j-2a43a9378/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Sections](#-sections)
- [Getting Started](#-getting-started)
- [Utility Scripts](#-utility-scripts)
- [Customization](#-customization)
- [Contact](#-contact)

---

## 🌟 Overview

A modern, dark-themed personal portfolio website built with pure HTML, CSS, and Vanilla JavaScript. Designed to showcase skills, projects, and certifications as an **MLOps / AI Platform Engineer**, with a premium glassmorphism aesthetic, smooth animations, and a fully responsive layout.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Premium Dark Theme** | Deep dark background with gold accent colors and glassmorphism panels |
| 🧭 **Floating Side Navigation** | Icon-based vertical nav with scroll-spy active state tracking |
| 🖼️ **Profile Glow Ring** | Animated profile photo with glow ring effect |
| 📁 **Filterable Portfolio Grid** | Projects filterable by category (MLOps, CV, NLP, FastAPI) |
| 🏆 **Certifications Gallery** | Clickable certificate cards with full-screen lightbox modal |
| ✍️ **Typewriter Animation** | Animated role title cycling through multiple roles |
| 📜 **Scroll Reveal Animations** | Sections fade in as they enter the viewport |
| 📬 **Contact Form** | Styled gold form with simulated send confirmation |
| 📱 **Responsive Design** | Works across desktop, tablet, and mobile screens |
| ⚡ **Zero Dependencies** | No frameworks, just HTML, CSS, and vanilla JS |

---

## 📁 Project Structure

```
New Portfolio/
│
├── index.html          # Main HTML — all sections and structure
├── style.css           # All styling — dark theme, layouts, animations
├── script.js           # Interactivity — typewriter, scroll spy, modal, reveal
│
├── assets/
│   ├── logo.png        # ASJ brand logo
│   ├── profile.png     # Profile photo
│   ├── cert1.png       # Certification images (cert1 – cert11)
│   └── ...
│
├── fetch_repos.py      # Python utility to fetch GitHub repos via API
├── repos.json          # Cached GitHub repository data
├── update_cards.py     # Utility to update portfolio project cards
├── rewrite.py          # HTML rewrite utility (light theme variant)
└── rewrite_dark.py     # HTML rewrite utility (dark theme variant)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Structure** | HTML5 (semantic elements) |
| **Styling** | Vanilla CSS3 (custom properties, grid, flexbox, animations) |
| **Interactivity** | Vanilla JavaScript (ES6+, IntersectionObserver API) |
| **Icons** | [Phosphor Icons](https://phosphoricons.com/) (via CDN) |
| **Fonts** | Google Fonts (Inter / system defaults) |
| **Utilities** | Python 3 (repo fetching & HTML generation scripts) |

---

## 📄 Sections

### 🏠 Hero
- Name, role title pill (`MLOps / AI Platform Engineer`)
- Profile photo with animated glow ring
- Location tag (Ramakuppam, Andhra Pradesh)
- CTA button linking to the About section

### 👤 About Me
- Personal bio and professional summary
- **Skills cards** organized by category:
  - 🪄 Generative AI (LLMs, LangChain, RAG, HuggingFace, OpenAI, Vector DBs)
  - 🚀 MLOps & Deployment (Docker, FastAPI, MLflow, DVC, GitHub Actions, CI/CD)
  - ☁️ Cloud Platforms (AWS SageMaker, Google Vertex AI, Kubernetes)
  - 🧠 ML & Deep Learning (Python, PyTorch, scikit-learn, TensorFlow)
  - 🗄️ Data & Pipelines (SQL, Apache Airflow, Spark, REST APIs)
  - 💻 Development (Full Stack FastAPI + React, Git, Linux/Bash)

### 💼 Portfolio
Filterable project grid linking to GitHub repositories:

| Project | Description | Tags |
|---|---|---|
| **Podmind AI K8s** | AI-driven Kubernetes cluster intelligence & monitoring | MLOps, Cloud |
| **AgriVision AI** | Crop disease detection with Deep Learning & FastAPI | Computer Vision, FastAPI |
| **Sign Language to Speech** | Real-time CNN + Flask AI converter | Computer Vision, NLP |
| **Cloud Monitoring** | High-availability cloud monitoring & alerting | MLOps, Cloud |
| **Multi-Cloud Architecture** | Scalable multi-cloud design patterns | MLOps, Cloud |
| **AI Resume Screening** | NLP-based automated resume parsing & ranking | NLP, ML |

### 🏆 Certifications & Achievements
- Grid gallery of 11 certification images
- Click any card to view it in a full-screen lightbox modal

### 📬 Contact Me
- Direct contact information (email, name)
- Social links (GitHub, LinkedIn, Instagram)
- Styled contact form with animated submit state

---

## 🚀 Getting Started

Since this is a pure static website, no build step or server is required.

### Option 1: Open directly in browser
```bash
# Simply open the file in your browser
start index.html        # Windows
open index.html         # macOS
xdg-open index.html     # Linux
```

### Option 2: Serve locally (recommended for full functionality)
```bash
# Using Python's built-in server
python -m http.server 8000

# Then open in browser
http://localhost:8000
```

### Option 3: VS Code Live Server
Install the **Live Server** extension in VS Code and click **"Go Live"** in the bottom status bar.

---

## 🐍 Utility Scripts

These Python helper scripts are used for development/maintenance:

### `fetch_repos.py`
Fetches all public GitHub repositories for `anushastefyj` via the GitHub API and prints their names.

```bash
python fetch_repos.py
```

### `update_cards.py`
Updates the portfolio project cards in `index.html` from `repos.json` data.

```bash
python update_cards.py
```

### `rewrite.py` / `rewrite_dark.py`
Full HTML generation scripts that rewrite `index.html` — one for light theme and one for the current dark theme. Useful when doing large structural regenerations.

```bash
python rewrite_dark.py   # Regenerate dark theme HTML
python rewrite.py        # Regenerate light theme HTML
```

---

## 🎨 Customization

### Changing Colors
CSS custom properties (variables) are defined at the top of `style.css`. Update these to retheme the entire site:

```css
:root {
    --gold: #c9a84c;          /* Primary gold accent */
    --dark-bg: #0a0a0f;       /* Main background */
    --panel-dark: #111118;    /* Panel background */
    --text-light: #e8e8e8;    /* Primary text color */
}
```

### Updating Projects
Edit the portfolio grid section in `index.html` or run `update_cards.py` with updated `repos.json`.

### Adding Certifications
1. Add the certificate image to `assets/` (e.g., `cert12.png`)
2. Add a new `cert-card` div in the `#certifications` section of `index.html`

### Updating Personal Info
Edit the relevant sections in `index.html`:
- **Hero**: Name, title, description
- **About**: Bio text, skill pills
- **Contact**: Email, social links

---

## 📬 Contact

**Anusha Stefy J**

| Platform | Link |
|---|---|
| 📧 Email | [anushastefy002@gmail.com](mailto:anushastefy002@gmail.com) |
| 💼 LinkedIn | [anusha-stefy-j](https://www.linkedin.com/in/anusha-stefy-j-2a43a9378/) |
| 🐙 GitHub | [anushastefyj](https://github.com/anushastefyj) |
| 📸 Instagram | [ms_micky_mini](https://instagram.com/ms_micky_mini/) |

---

<p align="center">
  <sub>© 2026 Anusha Stefy J — Built with ❤️ using HTML, CSS & Vanilla JS</sub>
</p>
>>>>>>> 313b9f6 (Updated portfolio files)
