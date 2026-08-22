# Sainik School Guide India - Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a cracku.in style website for Sainik Schools in India with SEO optimization for top Google ranking

**Architecture:** Hugo static site with custom cracku.in style layouts, hosted on Cloudflare Pages, with daily article publishing workflow

**Tech Stack:** Hugo, HTML/CSS/JavaScript, Cloudflare Pages, JSON-LD structured data

## Global Constraints

- Domain: sainikschooleastsiang.in (already owned)
- Language: Hindi + English bilingual content
- Design: Cracku.in style professional design
- SEO: All India Sainik Schools focus
- Hosting: Cloudflare Pages (free)

---

### Task 1: Fix Homepage Layout

**Files:**
- Modify: `D:\sainik-school-india\layouts\index.html`
- Modify: `D:\sainik-school-india\content\_index.md`

**Interfaces:**
- Produces: Working homepage with cracku.in style design

- [ ] **Step 1: Remove old landing.html reference**

Edit `D:\sainik-school-india\content\_index.md` to remove `layout: "landing"` from frontmatter

- [ ] **Step 2: Verify homepage renders correctly**

Run: Hugo server and check http://localhost:1313/
Expected: Homepage shows Sainik School East Siang content with hero, features, courses, etc.

- [ ] **Step 3: Test all sections visible**

Check: Hero section, Features grid, AISSEE courses, Important dates, Testimonials, Featured schools, Latest articles, Newsletter, Footer

- [ ] **Step 4: Commit**

```bash
git add content/_index.md
git commit -m "fix: homepage layout reference"
```

---

### Task 2: Fix Article Page TOC

**Files:**
- Modify: `D:\sainik-school-india\layouts\_default\single.html`

**Interfaces:**
- Produces: Working TOC that generates from h2/h3 headings

- [ ] **Step 1: Verify TOC JavaScript works**

Open any article page (e.g., /blog/aissee-2027-preparation-tips/)
Check: TOC shows all h2 headings, clicking scrolls to section

- [ ] **Step 2: Test FAQ accordion**

Check: FAQ questions expand/collapse on click

- [ ] **Step 3: Test feedback emojis**

Check: Clicking emoji highlights it

- [ ] **Step 4: Commit**

```bash
git add layouts/_default/single.html
git commit -m "fix: article page TOC and FAQ accordion"
```

---

### Task 3: Add More School Pages

**Files:**
- Create: `D:\sainik-school-india\content\schools\sainik-school-kapurthala.md`
- Create: `D:\sainik-school-india\content\schools\sainik-school-rewa.md`
- Create: `D:\sainik-school-india\content\schools\sainik-school-chittorgarh.md`

**Interfaces:**
- Produces: Individual school pages with complete information

- [ ] **Step 1: Create Sainik School Kapurthala page**

Write content with: Location, Established year, Admission process, Fee structure, Facilities, Contact details

- [ ] **Step 2: Create Sainik School Rewa page**

Same structure as Kapurthala

- [ ] **Step 3: Create Sainik School Chittorgarh page**

Same structure as Kapurthala

- [ ] **Step 4: Test all school pages**

Check: Each page renders correctly with sidebar

- [ ] **Step 5: Commit**

```bash
git add content/schools/
git commit -m "feat: add 3 more school pages"
```

---

### Task 4: Add More Blog Articles

**Files:**
- Create: `D:\sainik-school-india\content\blog\top-10-sainik-schools-india.md`
- Create: `D:\sainik-school-india\content\blog\crack-sainik-school-entrance-exam.md`

**Interfaces:**
- Produces: Blog articles with SEO optimization

- [ ] **Step 1: Create "Top 10 Sainik Schools" article**

Write 1500+ word article with tables, images, and FAQ section

- [ ] **Step 2: Create "How to Crack AISSEE" article**

Write 2000+ word article with tips, strategies, and success stories

- [ ] **Step 3: Test article pages**

Check: TOC works, tables render, FAQ accordion works

- [ ] **Step 4: Commit**

```bash
git add content/blog/
git commit -m "feat: add 2 new blog articles"
```

---

### Task 5: Add State-wise Pages

**Files:**
- Create: `D:\sainik-school-india\content\states\rajasthan.md`
- Create: `D:\sainik-school-india\content\states\tamil-nadu.md`
- Create: `D:\sainik-school-india\content\states\punjab.md`

**Interfaces:**
- Produces: State-wise school listing pages

- [ ] **Step 1: Create Rajasthan page**

List all Sainik Schools in Rajasthan with details

- [ ] **Step 2: Create Tamil Nadu page**

List all Sainik Schools in Tamil Nadu

- [ ] **Step 3: Create Punjab page**

List all Sainik Schools in Punjab

- [ ] **Step 4: Test state pages**

Check: Schools list renders correctly

- [ ] **Step 5: Commit**

```bash
git add content/states/
git commit -m "feat: add state-wise school pages"
```

---

### Task 6: SEO Optimization

**Files:**
- Modify: `D:\sainik-school-india\layouts\_default\baseof.html`
- Modify: `D:\sainik-school-india\hugo.toml`

**Interfaces:**
- Produces: SEO optimized pages with structured data

- [ ] **Step 1: Add JSON-LD structured data**

Add EducationalOrganization, FAQPage, Article schemas

- [ ] **Step 2: Add Open Graph tags**

Add og:title, og:description, og:image tags

- [ ] **Step 3: Add Twitter Card tags**

Add twitter:card, twitter:title, twitter:description

- [ ] **Step 4: Test SEO**

Use Google Rich Results Test tool

- [ ] **Step 5: Commit**

```bash
git add layouts/ hugo.toml
git commit -m "feat: add SEO structured data and meta tags"
```

---

### Task 7: PWA Support

**Files:**
- Modify: `D:\sainik-school-india\static\manifest.json`
- Create: `D:\sainik-school-india\static\sw.js`

**Interfaces:**
- Produces: Installable PWA with offline support

- [ ] **Step 1: Update manifest.json**

Add proper icons, theme color, background color

- [ ] **Step 2: Create service worker**

Cache static assets for offline support

- [ ] **Step 3: Test PWA**

Check: Install prompt appears on mobile

- [ ] **Step 4: Commit**

```bash
git add static/
git commit -m "feat: add PWA support"
```

---

### Task 8: Deploy to Cloudflare Pages

**Files:**
- Create: `D:\sainik-school-india\.github\workflows\deploy.yml`

**Interfaces:**
- Produces: Automated deployment to Cloudflare Pages

- [ ] **Step 1: Create GitHub repository**

Push code to GitHub

- [ ] **Step 2: Connect Cloudflare Pages**

Link GitHub repo to Cloudflare Pages

- [ ] **Step 3: Configure build settings**

Build command: `hugo --minify`
Output directory: `public`

- [ ] **Step 4: Connect domain**

Update DNS in Hostinger to point to Cloudflare

- [ ] **Step 5: Test deployment**

Check: Website loads at sainikschooleastsiang.in

- [ ] **Step 6: Commit**

```bash
git add .github/
git commit -m "feat: add Cloudflare Pages deployment"
```

---

### Task 9: Google Search Console Setup

**Files:**
- None (external setup)

**Interfaces:**
- Produces: Website indexed in Google

- [ ] **Step 1: Add property in Search Console**

Add sainikschooleastsiang.in

- [ ] **Step 2: Verify ownership**

Add DNS TXT record

- [ ] **Step 3: Submit sitemap**

Submit https://sainikschooleastsiang.in/sitemap.xml

- [ ] **Step 4: Request indexing**

Request indexing for homepage and key pages

---

### Task 10: Content Publishing Workflow

**Files:**
- Create: `D:\sainik-school-india\docs\content-workflow.md`

**Interfaces:**
- Produces: Documented workflow for daily article publishing

- [ ] **Step 1: Document article template**

Create template with SEO checklist

- [ ] **Step 2: Document publishing process**

Step-by-step guide for publishing articles

- [ ] **Step 3: Create content calendar template**

Weekly schedule for article topics

- [ ] **Step 4: Commit**

```bash
git add docs/
git commit -m "docs: add content publishing workflow"
```
