#!/usr/bin/env python3
"""Generate JNVST-style featured images for Sainik School Guide blog articles."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

THUMB_DIR = "/home/work/.openclaw/workspace/sainik-school-guide/static/images/thumbnails"
WIDTH, HEIGHT = 1200, 630

# Article data: (filename, headline, subline, cta, bg_image, panel_color, accent_color)
articles = [
    ("sainik-school-admission-mistakes", "5 Admission Mistakes", "Every Parent Must Avoid in 2027", "Expert Guide", "bg_school.jpg", (220, 38, 38), (255, 220, 0)),
    ("aissee-previous-year-papers-pdf", "AISSEE Previous Papers", "Download PDF 2021-2026", "Free Download", "bg_books.jpg", (37, 99, 235), (0, 255, 150)),
    ("aissee-application-form-2027-guide", "AISSEE Application Form", "Step-by-Step Guide 2027", "Apply Now", "bg_exam.jpg", (5, 150, 105), (255, 220, 0)),
    ("nda-after-sainik-school-career-path", "NDA After Sainik School", "Complete Career Path", "Officers Track", "bg_military.jpg", (30, 58, 138), (255, 200, 0)),
    ("sainik-school-counselling-2027", "Sainik School Counselling", "E-Counselling Guide 2027", "Seat Allotment", "bg_students.jpg", (124, 58, 237), (0, 255, 200)),
    ("sainik-school-scholarship-fee-concession-2027", "Sainik School Scholarship", "Save Up to 75% on Fees", "Fee Guide", "bg_graduation.jpg", (217, 119, 6), (255, 255, 0)),
    ("sainik-school-vs-military-school", "Sainik vs Military School", "Which Is Better for 2027?", "Compare Now", "bg_classroom.jpg", (75, 85, 99), (255, 150, 0)),
    ("sainik-school-vs-rimc-vs-rashtriya-military-school", "Sainik vs RIMC vs RMS", "Complete 3-Way Comparison", "Decide Now", "bg_teaching.jpg", (16, 185, 129), (255, 220, 0)),
    ("sainik-school-daily-routine-timetable", "Sainik School Routine", "5:30 AM to 10 PM Schedule", "Daily Timetable", "bg_running.jpg", (6, 182, 212), (255, 255, 0)),
    ("sainik-school-fee-comparison-all-schools", "Sainik School Fees 2027", "Compare All 33+ Schools", "Fee Details", "bg_desk.jpg", (139, 92, 246), (0, 255, 180)),
    ("sainik-school-for-girls-2027", "Sainik School for Girls", "Admission Guide 2027", "Girls Entry", "bg_indian_student.jpg", (236, 72, 153), (255, 220, 0)),
    ("sainik-school-medical-test-2027", "Medical Test Guide", "Height, Weight & Vision", "Requirements", "bg_medical.jpg", (245, 158, 11), (255, 255, 0)),
    ("sainik-school-nda-success-stories", "NDA Success Stories", "Officers & Alumni Achievements", "Inspiring", "bg_uniform.jpg", (234, 179, 8), (255, 255, 255)),
    ("sainik-school-admission-2027-guide", "Admission Guide 2027", "Complete Sainik School Guide", "Start Here", "bg_writing.jpg", (22, 163, 74), (255, 220, 0)),
    ("aissee-2027-preparation-tips", "AISSEE 2027 Tips", "Preparation Strategy Guide", "Topper Tips", "bg_study.jpg", (220, 38, 38), (0, 255, 150)),
    ("aissee-2027-syllabus-class-6-class-9", "AISSEE 2027 Syllabus", "Class 6 & Class 9 Weightage", "Chapter-wise", "bg_reading.jpg", (37, 99, 235), (255, 220, 0)),
    ("best-books-aissee-2027", "Best Books AISSEE 2027", "Expert Recommendations", "Book List", "bg_books.jpg", (161, 98, 7), (255, 255, 0)),
    ("sainik-school-hostel-life", "Hostel Life Guide", "Daily Routine & Activities", "Inside Story", "bg_teamwork.jpg", (55, 48, 163), (0, 255, 200)),
]

def get_font(size, bold=True):
    """Try to load a good font."""
    if bold:
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
    else:
        paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def generate_image(filename, headline, subline, cta, bg_name, panel_color, accent_color):
    """Generate JNVST-style featured image."""
    bg_path = os.path.join(THUMB_DIR, bg_name)

    # Load and prepare background
    if os.path.exists(bg_path):
        bg = Image.open(bg_path).convert('RGB')
        bg = bg.resize((WIDTH, HEIGHT), Image.LANCZOS)
        # Warm filter
        enhancer = ImageEnhance.Color(bg)
        bg = enhancer.enhance(1.1)
        enhancer = ImageEnhance.Brightness(bg)
        bg = enhancer.enhance(0.85)
    else:
        bg = Image.new('RGB', (WIDTH, HEIGHT), (40, 40, 40))

    img = bg.copy()
    draw = ImageDraw.Draw(img)

    # Panel dimensions (left side)
    panel_w = 520
    panel_x = 50
    panel_y = 60
    panel_h = HEIGHT - 120

    # Draw main panel with rounded corners
    draw.rounded_rectangle(
        [panel_x, panel_y, panel_x + panel_w, panel_y + panel_h],
        radius=16, fill=panel_color
    )

    # Add subtle gradient overlay on panel
    for i in range(panel_h):
        alpha = int(255 * (1 - i / panel_h * 0.15))
        y = panel_y + i
        draw.line([(panel_x, y), (panel_x + panel_w, y)],
                  fill=tuple(max(0, c - 10) for c in panel_color))

    # Add accent stripe on left edge of panel
    draw.rectangle([panel_x, panel_y, panel_x + 8, panel_y + panel_h], fill=accent_color)

    # Text positioning
    text_x = panel_x + 40
    text_y = panel_y + 60

    # Brand tag (small)
    font_brand = get_font(16, bold=False)
    brand_text = "SAINIK SCHOOL GUIDE"
    draw.text((text_x, text_y), brand_text, fill=(255, 255, 255, 180), font=font_brand)
    text_y += 35

    # Thin separator line
    draw.line([(text_x, text_y), (text_x + 100, text_y)], fill=accent_color, width=2)
    text_y += 25

    # Headline (large, bold)
    font_headline = get_font(42, bold=True)
    # Word wrap
    words = headline.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font_headline)
        if bbox[2] - bbox[0] > panel_w - 80:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)

    for line in lines:
        draw.text((text_x, text_y), line, fill=(255, 255, 255), font=font_headline)
        text_y += 55
    text_y += 10

    # Subline
    font_sub = get_font(24, bold=False)
    draw.text((text_x, text_y), subline, fill=(255, 255, 255, 220), font=font_sub)
    text_y += 50

    # CTA button
    font_cta = get_font(20, bold=True)
    cta_bbox = draw.textbbox((0, 0), cta, font=font_cta)
    cta_w = cta_bbox[2] - cta_bbox[0] + 40
    cta_h = 44
    cta_x = text_x
    cta_y = text_y + 10

    # CTA background
    draw.rounded_rectangle(
        [cta_x, cta_y, cta_x + cta_w, cta_y + cta_h],
        radius=8, fill=accent_color
    )
    # CTA text (dark color for contrast)
    draw.text((cta_x + 20, cta_y + 10), cta, fill=(0, 0, 0), font=font_cta)

    # Bottom right badge
    font_badge = get_font(14, bold=False)
    badge_text = "sainikschooleastsiang.in"
    badge_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    badge_w = badge_bbox[2] - badge_bbox[0] + 20
    draw.rounded_rectangle(
        [WIDTH - badge_w - 20, HEIGHT - 40, WIDTH - 20, HEIGHT - 12],
        radius=6, fill=(0, 0, 0, 120)
    )
    draw.text((WIDTH - badge_w - 10, HEIGHT - 36), badge_text, fill=(255, 255, 255), font=font_badge)

    # Save
    output = os.path.join(THUMB_DIR, f"{filename}.jpg")
    img.save(output, 'JPEG', quality=92)
    print(f"✅ {filename}.jpg")

# Generate all
print(f"🎨 Generating {len(articles)} JNVST-style images...\n")
for args in articles:
    generate_image(*args)
print(f"\n🎉 Done! {len(articles)} images generated.")
