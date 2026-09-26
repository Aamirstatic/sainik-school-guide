# Daily Content Pipeline — Sainik School Guide

Every day, 5 scheduled runs each publish **1 news article + 1 blog article + 1 web story**
= **15 pieces/day**. This playbook is the complete instruction set for each run.
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
- Image composer: `~/workspace/scripts/caneup_style.py` (`--single` mode)
- Backgrounds: `~/workspace/imgbg/{exam,admission,prep,life,compare}/`
- Log: `data/pipeline-log.json` — **read it first**, append every item you publish.
- `git status` must be clean before you start. If it is NOT clean: inspect the
  uncommitted files first. If they are valid pipeline outputs from a previous
  interrupted run (markdown + images + matching log entries in
  `data/pipeline-log.json`), verify them, build, and push them, then continue
  with today's new pieces. Only stop and report if the dirty state looks
  unrelated or broken.

### 1. Pick the three pieces
- **Blog:** read `data/blog-topics.yaml`; take the topic with the lowest `id`
  greater than `blog_topic_cursor` in the log. Set cursor to that id.
  If all 90 are used, restart at id 1 with a visibly fresh angle
  (new examples, new FAQs, updated year references).
- **News:** search the web for AISSEE / Sainik School / NTA / school-education
  news from the **last 48 hours**. Pick the single most relevant, genuinely
  new development. Check the log + `content/blog/` slugs: **never republish
  the same news twice.** If nothing genuinely new exists, write an
  "update/explainer" tied to the nearest upcoming milestone
  (e.g. "X days to AISSEE 2027: what to finish this week") — clearly labelled,
  never fabricated as breaking news.
- **Web story:** make it about the day's news item OR the day's blog topic,
  whichever is more visual. 6–8 slides.

### 2. Write the content (English only, human voice)
- **News article** → `content/blog/<slug>.md` (slug ends with `-YYYY-MM-DD`,
  e.g. `nta-extends-aissee-2027-deadline-2026-10-02`). 450–750 words.
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
- **Web story** → `content/webstories/<slug>.md`. Frontmatter: title, date,
  description, author_name, featured_image (the poster), story_type "image",
  category, tags, and `slides:` — 6–8 slides, each with image, title (≤8 words),
  subtitle (1–2 lines), credit. Body: one short paragraph.
- Author images exist: `/images/authors/aamir-raza.png`,
  `/images/authors/nisha-sharma.png`, `/images/authors/sameer-khan.png`,
  `/images/authors/rifaul-hasan.jpeg`. author_title values: use
  "Founder, Sainik School Guide" (Aamir), "Education Writer" (Nisha),
  "Defence Career Counsellor" (Sameer), "Principal, JGPS | Senior Education Expert" (Rifaul).
- **Never invent**: dates, fees, cutoffs, quotas, topper names, quotes,
  percentages. Unknown = EXPECTED with basis, or omitted.

### 3. Generate images (English text, caneup style)
For each piece, run the composer:
```
python3 ~/workspace/scripts/caneup_style.py --single \
  --out <path> --headline "<SHORT ENGLISH HOOK>" --sub "<one-line context>" \
  --pill "<NEWS|GUIDE|UPDATE|EXAM...>" --size 1200x630 --cat <exam|admission|prep|life|compare>
```
- Blog + news thumbnails → `static/images/thumbnails/<slug>.webp` (1200x630).
- Web story poster → `static/images/webstories/<slug>.webp` (800x1200).
- Headline: ALL-CAPS short hook, ≤6 words. Sub: one factual line. Pill: 1 word.
- Slide images: reuse the new poster + existing files from
  `static/images/webstories/` (pick thematically close ones).
- Background category mapping: exam dates/results → exam; forms/fees/
  counselling → admission; study tips/books → prep; campus/discipline/
  parenting → life; comparisons → compare.

### 4. Verify, build, push
1. Append all three items to `data/pipeline-log.json` (date, type, slug, title).
2. Build: `cd ~/workspace/sainik-school-guide && ~/workspace/bin/hugo --minify`.
   Fix any error before proceeding.
3. Quick link sanity: the build must report 0 broken internal links
   (the repo has a link checker — if unavailable, at least confirm the
   three new pages render in `public/`).
4. Push with `~/workspace/skills/github/bin/gh_push.py`
   (pushes uncommitted working-tree changes — **do NOT commit first**).
5. After push: `git fetch origin && git reset --hard origin/master`, confirm clean.

### 5. Report
Final message: the 3 titles + slugs published and confirmation of push.
Keep it to 3–4 lines. Do not dump article text into chat.

## Guardrails
- If a step fails (no news found is NOT a failure — use the explainer fallback),
  finish what you can, push that, and report the gap honestly.
- Never publish the same slug or near-duplicate title twice — the log is the
  source of truth.
- Quality beats quota: one skipped piece with an honest report is better
  than a fabricated one.
