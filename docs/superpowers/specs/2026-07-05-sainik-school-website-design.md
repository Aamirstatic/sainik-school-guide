# Sainik School Guide India - Website Design Spec

## [S1] Project Overview

**Website:** sainikschooleastsiang.in
**Type:** Unofficial informational guide for Sainik Schools in India
**Goal:** School info + AISSEE prep + daily articles (cracku.in style)
**Target Audience:** Parents + Students
**Language:** Hindi + English
**SEO Focus:** All India Sainik Schools
**Monetization:** Coaching institute promotion
**Design:** Cracku.in style professional design

## [S2] Technology Stack

| Component | Choice | Cost |
|-----------|--------|------|
| Site Generator | Hugo (fastest static site generator) | Free |
| Hosting | Cloudflare Pages (free CDN + SSL) | Free |
| Theme | Custom cracku.in style layouts | Free |
| Analytics | Google Analytics + Search Console | Free |
| Domain | sainikschooleastsiang.in (already owned) | Already purchased |

## [S3] Website Structure

### Homepage
- Hero section with stats (33+ schools, 95% success, 5000+ students)
- Features grid (6 cards: School Directory, AISSEE Prep, Daily Articles, Expert Tips, Cut-off Analysis, Study Resources)
- AISSEE course cards (Class 6 & Class 9)
- Important dates table
- Testimonials section
- Featured schools
- Latest articles
- Newsletter signup
- 4-column footer

### Article Pages
- Left content + right sidebar layout
- Breadcrumb navigation
- Author box with avatar
- Latest updates banner
- Collapsible Table of Contents
- Content with styled tables
- FAQ accordion with schema markup
- Feedback emojis (1-5 rating)
- Related articles
- Sidebar: AISSEE CTA, Top Schools, Newsletter
- Sticky bottom CTA bar

### School Directory
- Individual pages for each Sainik School
- Card grid layout for listing
- State-wise filtering

### Blog Listing
- Card grid layout
- Tags and metadata
- Date sorting

## [S4] SEO Implementation

### Structured Data (JSON-LD)
- EducationalOrganization schema
- FAQPage schema for FAQs
- Article schema with datePublished/dateModified
- BreadcrumbList schema

### Meta Tags
- Open Graph tags for social sharing
- Twitter Card tags
- `max-image-preview:large` for Google Discover
- Canonical URLs
- `date:published` and `date:modified` meta properties

### Content Strategy
- Daily articles (7 days/week)
- Bilingual content (Hindi + English)
- Internal linking between schools and articles
- Large hero images (1200px+) in WebP format

## [S5] Target Keywords

| Type | Keywords |
|------|----------|
| Primary | Sainik School India, AISSEE 2027, Sainik School Admission |
| Secondary | Sainik School fees, Sainik School syllabus, AISSEE preparation |
| Long-tail | Sainik School East Siang admission, How to crack AISSEE |

## [S6] Content Calendar

| Day | Topic | Example |
|-----|-------|---------|
| Monday | AISSEE Tips | Math preparation strategy |
| Tuesday | School Spotlight | Individual school guide |
| Wednesday | Study Resources | Best books for AISSEE |
| Thursday | Success Stories | Student interview |
| Friday | Notifications | Important dates |
| Saturday | Previous Papers | Paper analysis |
| Sunday | Current Affairs | Defense news |

## [S7] Monetization Strategy

- Coaching institute promotion in sidebar CTAs
- Featured school listings
- Newsletter sponsorships
- Affiliate links for study materials

## [S8] Pages Required

1. Homepage
2. Sainik Schools Directory (listing)
3. Individual School Pages (33+ schools)
4. AISSEE Guide
5. Blog Listing
6. Individual Blog Posts
7. State-wise Pages
8. Search Page
9. 404 Page
10. Contact Page

## [S9] Features

- PWA support (manifest.json, service worker)
- Dark mode toggle
- Search functionality
- Newsletter signup
- Responsive design (mobile-first)
- Fast loading (Hugo + Cloudflare CDN)
- SEO optimized
- Google Discover ready
