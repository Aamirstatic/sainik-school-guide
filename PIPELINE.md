# Daily Content Pipeline — Sainik School Guide

Every day, 5 scheduled runs each publish **1 news article + 1 blog article**
= **10 pieces/day**. This playbook is the complete instruction set for each run.
Read `CONTENT-SYSTEM.md` (v2.0) first — every rule there applies here, especially:
multi-source verification (§2), human voice (§5), Discover checklist (§6),
and the pre-publish checklist (§9).

## Run schedule (IST) — chosen for the audience (Indian parents/students)

| Run | Time (IST) | Why this slot |
|-----|-----------|---------------|
| morning | ~07:00 | Morning news check before school/work; Discover morning peak |
| latenoon | ~11:00 | Late-morning browse window |
| afternoon | ~14:30 | Lunch-break scroll |
| evening | ~18:30 | Post-school/work wind-down, family discussion time |
| night | ~21:00 | Night peak — admission research hour; Discover evening surge |

## Per-run procedure

### 0. Setup
- Repo: `~/workspace/sainik-school-guide` (branch `master`)
- Hugo: `~/workspace/bin/hugo`
- Image composer: `~/workspace/scripts/cracku_style.py` (cracku style, real photos)
- Backgrounds: `~/workspace/imgbg/{exam,admission,prep,life,compare}/`
- Log: `data/pipeline-log.json` — **read it first**, append every item you publish.
- `git status` must be clean before you start. If it is NOT clean: inspect the
  uncommitted files first. If they are valid pipeline outputs from a previous
  interrupted run (markdown + images + matching log entries in
  `data/pipeline-log.json`), verify them, build, and push them, then continue
  with today's new pieces. Only stop and report if the dirty state looks
  unrelated or broken.

### 1. Pick the two pieces
- **Blog:** FIRST check what's hot right now — Google Trends
  (trends.google.com, India, past 7 days: "AISSEE", "Sainik School",
  "sainik school admission"), plus a web search for AISSEE / Sainik School
  news and discussions from the last 24–48 hours. If a genuinely trending
  topic emerges that is NOT already in the log and NOT the same angle as
  today's news piece, write the blog on that hot topic (guide/explainer
  angle, never a duplicate of the news) and do NOT advance
  `blog_topic_cursor`. Otherwise fall back to the evergreen bank:
  read `data/blog-topics.yaml`; take the topic with the lowest `id`
  greater than `blog_topic_cursor` in the log; set cursor to that id.
  If all 90 are used, restart at id 1 with a visibly fresh angle
  (new examples, new FAQs, updated year references).
  Hot topic ≠ unverified: CONTENT-SYSTEM.md §2 applies fully — one Tier-1
  source or two independent Tier-2 sources per hard fact, EXPECTED label
  when uncertain, never invent.
- **News:** search the web for AISSEE / Sainik School / NTA / school-education
  news from the **last 48 hours**. Pick the single most relevant, genuinely
  new development. Check the log + `content/blog/` slugs: **never republish
  the same news twice.** If nothing genuinely new exists, write an
  "update/explainer" tied to the nearest upcoming milestone
  (e.g. "X days to AISSEE 2027: what to finish this week") — clearly labelled,
  never fabricated as breaking news.

### 2. Write the content (English only, human voice)
- **News article** → `content/news/<slug>.md` (URL `/news/<slug>/`; slug ends with
  `-YYYY-MM-DD`, e.g. `nta-extends-aissee-2027-deadline-2026-10-02`). 450–750 words.
  Frontmatter: title, date (today, ISO with +05:30), lastmod, draft false,
  description, keywords, author (rotate: Aamir Raza / Nisha Sharma /
  Sameer Khan / Rifaul Hasan), featured_image, `categories: ["News"]`.
  Body: "Last verified: <today>" box, CONFIRMED/EXPECTED labels, what
  happened, why it matters, what to do next, 3–4 FAQs, Sources section
  with real URLs you actually opened.
- **Blog article** → `content/blog/<slug>.md`. 900–1400 words. Same frontmatter
  (no News category). Follow §9 pre-publish checklist: original table or
  checklist or timeline, 4–6 FAQs, internal links to 2–3 existing pages,
  Sources section, "Last verified" box.
- **FAQs frontmatter (required for news + blog):** every article MUST include a
  `faqs:` list in frontmatter — it powers the FAQPage schema (AEO/rich results).
  Format:
  ```yaml
  faqs:
    - question: "Is there negative marking in AISSEE 2027?"
      answer: "No — wrong answers and blanks both score zero; nothing is deducted."
  ```
  Mirror the same Q&As in the `## FAQs` body section as `**Question?**` +
  answer paragraph. 3–4 for news, 4–6 for blog. Answers: plain text, no markdown.
- Author images exist: `/images/authors/aamir.jpeg`,
  `/images/authors/nisha-sharma.png`, `/images/authors/sameer-khan.png`,
  `/images/authors/rifaul-hasan.jpeg`. author_title values: use
  "Founder, Sainik School Guide" (Aamir), "Education Writer" (Nisha),
  "Defence Career Counsellor" (Sameer), "Principal, JGPS | Senior Education Expert" (Rifaul).
- **Never invent**: dates, fees, cutoffs, quotas, topper names, quotes,
  percentages. Unknown = EXPECTED with basis, or omitted.

### 3. Generate images (cracku style, REAL photos, English text)
Photo library: real stock photos in `static/images/photos/` (see MANIFEST.md).
NEVER use AI-generated images. Featured images are ALWAYS 1200x675.

For each news/blog piece, generate TWO images:
```
# 1) Featured: 1200x675 cracku-style (real photo bg + big navy headline
#    + blue pill sub + red tag), save webp AND jpg twin (og:image uses .jpg)
python3 ~/workspace/scripts/cracku_style.py --featured \
  --photo static/images/photos/<thematic-photo>.jpg \
  --out static/images/thumbnails/<slug>.webp \
  --headline "<SHORT ENGLISH HOOK>" --sub "<one factual line>" --tag "<NEWS|GUIDE|...>"
python3 -c "from PIL import Image; im=Image.open('static/images/thumbnails/<slug>.webp'); im.save('static/images/thumbnails/<slug>.jpg','JPEG',quality=88)"

# 2) In-body: 1 clean real photo (NO text), 1200x675
python3 ~/workspace/scripts/cracku_style.py --clean \
  --photo static/images/photos/<different-photo>.jpg \
  --out static/images/inbody/<slug>.webp --size 1200x675
```
Insert the in-body image into the markdown just before the first `## ` heading:
`![<descriptive alt text>](/images/inbody/<slug>.webp)`
- News → `content/news/<slug>.md` (URL becomes `/news/<slug>/`), frontmatter
  `categories: ["News"]`, featured_image → `/images/thumbnails/<slug>.webp`.
- Blog → `content/blog/<slug>.md`, featured_image → `/images/thumbnails/<slug>.webp`.
- Headline: short English hook, ≤8 words. Sub: one factual line. Tag: 1-2 words.

### 4. Verify, build, push
1. Append both items to `data/pipeline-log.json` (date, type, slug, title).
2. Build: `cd ~/workspace/sainik-school-guide && ~/workspace/bin/hugo --minify`.
   Fix any error before proceeding.
3. Quick link sanity: the build must report 0 broken internal links
   (the repo has a link checker — if unavailable, at least confirm the
   two new pages render in `public/`).
4. Push with `~/workspace/skills/github/bin/gh_push.py`
   (pushes uncommitted working-tree changes — **do NOT commit first**).
5. After push: `git fetch origin && git reset --hard origin/master`, confirm clean.

### 5. IndexNow submission (instant indexing for Bing/Yandex/DuckDuckGo)
After the push, submit the 2 new URLs to IndexNow so Bing-family
search engines pick them up within minutes instead of days:
```bash
curl -s -X POST https://api.indexnow.org/indexnow \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{"host":"sainikschooleastsiang.in","key":"ddb0134a637bbb4d07f9ae2f65ab147b","keyLocation":"https://sainikschooleastsiang.in/ddb0134a637bbb4d07f9ae2f65ab147b.txt","urlList":["https://sainikschooleastsiang.in/news/<news-slug>/","https://sainikschooleastsiang.in/blog/<blog-slug>/"]}'
```
Replace `<news-slug>` etc. with the actual slugs published this run.
A `200` response means accepted. (The key file
`static/ddb0134a637bbb4d07f9ae2f65ab147b.txt` is already deployed;
the key is public by design — IndexNow requires it to be fetchable.)

### 6. Google Indexing API submission (instant crawl notification for Google)
After the push, notify Google about the 2 new URLs:
```bash
python3 ~/workspace/scripts/google_indexing.py \
  "https://sainikschooleastsiang.in/news/<news-slug>/" \
  "https://sainikschooleastsiang.in/blog/<blog-slug>/"
```
`200` per URL = notification accepted. The service-account key lives at
`~/workspace/user/files/jgps-479610-a8094215c449.json` — NEVER copy it into
the repo, NEVER print it, NEVER put it in chat. (Quota: 200 URLs/day;
we use ~10.)
Honest caveat: this asks Googlebot to crawl quickly; it does NOT guarantee
indexing. Google officially supports this API for job-posting/livestream
pages — for articles it still returns 200 and usually triggers a faster
crawl, but indexing remains Google's decision. Search Console verification
+ submitted sitemap is still the durable path.

### 7. Report
Final message: the 2 titles + slugs published and confirmation of push.
Keep it to 3–4 lines. Do not dump article text into chat.

## Guardrails
- If a step fails (no news found is NOT a failure — use the explainer fallback),
  finish what you can, push that, and report the gap honestly.
- Never publish the same slug or near-duplicate title twice — the log is the
  source of truth.
- Quality beats quota: one skipped piece with an honest report is better
  than a fabricated one.
