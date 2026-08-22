#!/bin/bash
# =============================================================
# Google Discover Freshness Update Script
# Run daily or every 2 days to keep articles fresh
# Rotates 2-3 articles per run with updated lastmod + update box
# =============================================================

CONTENT_DIR="$(dirname "$0")/../content/blog"
TODAY=$(date +%Y-%m-%d)
TODAY_ISO="${TODAY}T$(date +%H:%M):00+05:30"
LOG_FILE="$(dirname "$0")/freshness-log.txt"

# Articles to rotate (pick 2-3 per run, cycle through all)
ALL_ARTICLES=(
  "sainik-school-admission-2027-guide.md"
  "aissee-2027-preparation-tips.md"
  "aissee-2027-syllabus-class-6-class-9.md"
  "sainik-school-fee-comparison-all-schools.md"
  "sainik-school-for-girls-2027.md"
  "sainik-school-counselling-2027.md"
  "best-books-aissee-2027.md"
  "sainik-school-admission-mistakes.md"
  "sainik-school-daily-routine-timetable.md"
  "sainik-school-medical-test-2027.md"
  "aissee-application-form-2027-guide.md"
  "aissee-previous-year-papers-pdf.md"
  "sainik-school-cutoff-2026-state-wise.md"
  "new-sainik-schools-ppp-model-2027.md"
  "sainik-school-class-9-admission-2027.md"
  "sainik-school-seats-2027-all-schools-matrix.md"
  "sainik-school-state-wise-complete-directory-2027.md"
  "sainik-school-to-nda-roadmap.md"
  "nda-after-sainik-school-career-path.md"
  "life-after-sainik-school-career-options.md"
  "sainik-school-interview-questions-2027.md"
  "sainik-school-mock-test-2027.md"
  "sainik-school-physical-test-guide.md"
  "sainik-school-scholarship-fee-concession-2027.md"
  "sainik-school-sc-st-defence-quota-2027.md"
)

TOTAL=${#ALL_ARTICLES[@]}

# Use day-of-year to rotate which articles get updated
DAY_OF_YEAR=$(date +%j)
BATCH_SIZE=3
START_IDX=$(( (DAY_OF_YEAR * BATCH_SIZE) % TOTAL ))

echo "=== Freshness Update: $TODAY ===" >> "$LOG_FILE"

UPDATED=0
for i in $(seq 0 $((BATCH_SIZE - 1))); do
  IDX=$(( (START_IDX + i) % TOTAL ))
  ARTICLE="${ALL_ARTICLES[$IDX]}"
  FILE="$CONTENT_DIR/$ARTICLE"

  if [ ! -f "$FILE" ]; then
    echo "SKIP: $ARTICLE (not found)" >> "$LOG_FILE"
    continue
  fi

  # Check if already updated today
  if grep -q "lastmod: $TODAY" "$FILE"; then
    echo "SKIP: $ARTICLE (already updated today)" >> "$LOG_FILE"
    continue
  fi

  # Get current lastmod for the update block
  OLD_LASTMOD=$(grep "^lastmod:" "$FILE" | head -1 | sed 's/^lastmod: //')

  # Update lastmod in frontmatter
  sed -i "s/^lastmod: .*/lastmod: $TODAY_ISO/" "$FILE"

  # Update the "Last Updated" box date (if exists in upd-box)
  # The template auto-reads from frontmatter, so no body change needed

  echo "UPDATED: $ARTICLE (was: $OLD_LASTMOD → now: $TODAY_ISO)" >> "$LOG_FILE"
  UPDATED=$((UPDATED + 1))
done

echo "Total updated: $UPDATED" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"

echo "✅ Updated $UPDATED articles for $TODAY"
