#!/usr/bin/env python3
"""Add strategic internal links to all blog articles."""
import os
import re

BLOG_DIR = "/home/work/.openclaw/workspace/sainik-school-guide/content/blog"

# Keyword → URL mapping (order matters - longer phrases first to avoid partial matches)
KEYWORD_MAP = [
    # Long phrases first
    ("sainik school admission mistakes", "/blog/sainik-school-admission-mistakes/", "Sainik School Admission Mistakes"),
    ("sainik school admission guide", "/blog/sainik-school-admission-2027-guide/", "Sainik School Admission Guide"),
    ("sainik school admission 2027", "/blog/sainik-school-admission-2027-guide/", "Sainik School Admission 2027"),
    ("sainik school admission", "/blog/sainik-school-admission-2027-guide/", "Sainik School Admission"),
    ("aissee previous year papers", "/blog/aissee-previous-year-papers-pdf/", "AISSEE Previous Year Papers"),
    ("aissee previous year question papers", "/blog/aissee-previous-year-papers-pdf/", "AISSEE Previous Year Papers"),
    ("aissee application form", "/blog/aissee-application-form-2027-guide/", "AISSEE Application Form"),
    ("sainik school fee comparison", "/blog/sainik-school-fee-comparison-all-schools/", "Sainik School Fee Comparison"),
    ("sainik school fees", "/blog/sainik-school-fee-comparison-all-schools/", "Sainik School Fees"),
    ("sainik school scholarship", "/blog/sainik-school-scholarship-fee-concession-2027/", "Sainik School Scholarship"),
    ("sainik school counselling", "/blog/sainik-school-counselling-2027/", "Sainik School Counselling"),
    ("sainik school medical test", "/blog/sainik-school-medical-test-2027/", "Sainik School Medical Test"),
    ("sainik school daily routine", "/blog/sainik-school-daily-routine-timetable/", "Sainik School Daily Routine"),
    ("sainik school hostel life", "/blog/sainik-school-hostel-life/", "Sainik School Hostel Life"),
    ("sainik school for girls", "/blog/sainik-school-for-girls-2027/", "Sainik School for Girls"),
    ("nda after sainik school", "/blog/nda-after-sainik-school-career-path/", "NDA After Sainik School"),
    ("nda success stories", "/blog/sainik-school-nda-success-stories/", "NDA Success Stories"),
    ("sainik school vs rimc", "/blog/sainik-school-vs-rimc-vs-rashtriya-military-school/", "Sainik School vs RIMC"),
    ("sainik school vs military school", "/blog/sainik-school-vs-military-school/", "Sainik School vs Military School"),
    ("aissee 2027 syllabus", "/blog/aissee-2027-syllabus-class-6-class-9/", "AISSEE 2027 Syllabus"),
    ("aissee syllabus", "/blog/aissee-2027-syllabus-class-6-class-9/", "AISSEE Syllabus"),
    ("aissee preparation", "/blog/aissee-2027-preparation-tips/", "AISSEE Preparation"),
    ("aissee 2027 preparation", "/blog/aissee-2027-preparation-tips/", "AISSEE 2027 Preparation"),
    ("best books for aissee", "/blog/best-books-aissee-2027/", "Best Books for AISSEE"),
    ("best books aissee", "/blog/best-books-aissee-2027/", "Best Books AISSEE"),
]

def get_slug(filename):
    """Get the slug from filename."""
    return filename.replace(".md", "")

def add_internal_links(content, current_slug):
    """Add internal links to content for keyword mentions."""
    links_added = 0
    linked_keywords = set()  # Track what we've already linked in this article

    for keyword, url, anchor_text in KEYWORD_MAP:
        # Skip if this article IS the target (don't self-link)
        target_slug = url.split("/blog/")[1].rstrip("/")
        if target_slug == current_slug:
            continue

        # Skip if we already linked a similar keyword
        if keyword in linked_keywords:
            continue

        # Find first occurrence of keyword (case-insensitive)
        # Only match if not already inside a link [text](url) or <a> tag
        pattern = re.compile(
            r'(?<!\[)(?<!\()(?<!")\b(' + re.escape(keyword) + r')\b(?!\])(?!\))(?!["\w]*[)])',
            re.IGNORECASE
        )

        match = pattern.search(content)
        if match:
            # Check it's not inside a markdown link or HTML tag
            start = match.start()
            # Check if preceded by [ or <a
            before = content[max(0, start-10):start]
            if '[' in before or '<a' in before:
                continue

            # Replace first occurrence with link
            replacement = f'[{match.group(1)}]({url})'
            content = content[:match.start()] + replacement + content[match.end():]
            links_added += 1
            linked_keywords.add(keyword)

            # Limit to 5 internal links per article (avoid over-linking)
            if links_added >= 5:
                break

    return content, links_added

def process_articles():
    """Process all blog articles."""
    total_links = 0

    for filename in sorted(os.listdir(BLOG_DIR)):
        if not filename.endswith(".md") or filename.startswith("_"):
            continue

        filepath = os.path.join(BLOG_DIR, filename)
        current_slug = get_slug(filename)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split front matter and body
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        front_matter = parts[0] + "---" + parts[1] + "---"
        body = parts[2]

        # Skip the "Related Articles" and "FAQ" sections at the bottom
        # Only add links in the main content
        body_parts = body.split("## Related Articles")
        main_content = body_parts[0]
        rest = "## Related Articles" + body_parts[1] if len(body_parts) > 1 else ""

        # Also skip FAQ section
        main_parts = main_content.split("## Frequently Asked Questions")
        linkable_content = main_parts[0]
        faq_and_rest = "## Frequently Asked Questions" + main_parts[1] if len(main_parts) > 1 else ""

        # Add links
        updated_content, links = add_internal_links(linkable_content, current_slug)

        if links > 0:
            # Reassemble
            new_body = updated_content + faq_and_rest + rest
            new_file = front_matter + new_body

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_file)

            total_links += links
            print(f"✅ {filename}: +{links} internal links")
        else:
            print(f"⬜ {filename}: no changes")

    print(f"\n🎯 Total internal links added: {total_links}")

if __name__ == "__main__":
    process_articles()
