#!/usr/bin/env python3
"""Generate featured images for all Sainik School Guide blog articles."""
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

OUTPUT_DIR = "/home/work/.openclaw/workspace/sainik-school-guide/static/images/thumbnails"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1200, 630

# Article data: (filename, title, emoji, gradient_colors)
articles = [
    ("sainik-school-admission-mistakes", "5 Mistakes Parents Make\nDuring Sainik School\nAdmission 2027", "⚠️", ((220, 38, 38), (185, 28, 28))),
    ("aissee-previous-year-papers-pdf", "AISSEE Previous Year\nQuestion Papers\nDownload PDF & Analysis", "📄", ((37, 99, 235), (29, 78, 216))),
    ("aissee-application-form-2027-guide", "How to Fill AISSEE\nApplication Form 2027\nStep-by-Step Guide", "📝", ((5, 150, 105), (4, 120, 87))),
    ("nda-after-sainik-school-career-path", "NDA After Sainik School\nComplete Career Path\nto Armed Forces", "🎖️", ((30, 58, 138), (15, 23, 42))),
    ("sainik-school-counselling-2027", "Sainik School\nCounselling 2027\nE-Counselling Guide", "🏛️", ((124, 58, 237), (109, 40, 217))),
    ("sainik-school-scholarship-fee-concession-2027", "Sainik School\nScholarship 2027\nFee Concession Guide", "💰", ((217, 119, 6), (180, 83, 9))),
    ("sainik-school-vs-military-school", "Sainik School vs\nMilitary School 2027\nWhich Is Better?", "⚔️", ((75, 85, 99), (55, 65, 81))),
    ("sainik-school-vs-rimc-vs-rashtriya-military-school", "Sainik School vs RIMC\nvs Rashtriya Military\nSchool 2027", "🏫", ((16, 185, 129), (5, 150, 105))),
    ("sainik-school-daily-routine-timetable", "Sainik School\nDaily Routine 2027\nComplete Timetable", "⏰", ((6, 182, 212), (8, 145, 178))),
    ("sainik-school-fee-comparison-all-schools", "Sainik School Fees 2027\nComplete Fee\nComparison", "📊", ((139, 92, 246), (124, 58, 237))),
    ("sainik-school-for-girls-2027", "Sainik School for\nGirls 2027\nAdmission Guide", "👩‍🎓", ((236, 72, 153), (219, 39, 119))),
    ("sainik-school-medical-test-2027", "Sainik School\nMedical Test 2027\nRequirements", "🏥", ((245, 158, 11), (217, 119, 6))),
    ("sainik-school-nda-success-stories", "Sainik School\nNDA Success Rate 2027\nOfficers & Alumni", "⭐", ((234, 179, 8), (202, 138, 4))),
    ("sainik-school-admission-2027-guide", "Sainik School\nAdmission 2027\nComplete Guide", "🎯", ((22, 163, 74), (21, 128, 61))),
    ("aissee-2027-preparation-tips", "AISSEE 2027\nPreparation Tips\nComplete Strategy", "📚", ((220, 38, 38), (185, 28, 28))),
    ("aissee-2027-syllabus-class-6-class-9", "AISSEE 2027 Syllabus\nClass 6 & Class 9\nChapter-wise Weightage", "📖", ((37, 99, 235), (29, 78, 216))),
    ("best-books-aissee-2027", "Best Books for\nAISSEE 2027\nExpert Recommendations", "📕", ((161, 98, 7), (120, 53, 15))),
    ("sainik-school-hostel-life", "Sainik School\nHostel Life 2027\nComplete Guide", "🛏️", ((55, 48, 163), (49, 46, 129))),
]

def get_font(size):
    """Try to load a good font, fall back to default."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

def draw_gradient(draw, width, height, color1, color2):
    """Draw a vertical gradient."""
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_pattern(draw, width, height):
    """Draw subtle geometric pattern overlay."""
    for x in range(0, width, 60):
        for y in range(0, height, 60):
            draw.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255, 30))
    # Diagonal lines
    for i in range(-height, width + height, 80):
        draw.line([(i, 0), (i + height, height)], fill=(255, 255, 255, 15), width=1)

def generate_image(filename, title, emoji, colors):
    """Generate a single featured image."""
    img = Image.new('RGB', (WIDTH, HEIGHT), colors[0])
    draw = ImageDraw.Draw(img)

    # Gradient background
    draw_gradient(draw, WIDTH, HEIGHT, colors[0], colors[1])

    # Pattern overlay
    draw_pattern(draw, WIDTH, HEIGHT)

    # White overlay box (semi-transparent effect)
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rounded_rectangle([60, 80, WIDTH-60, HEIGHT-80], radius=20, fill=(255, 255, 255, 25))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)

    # Top badge
    font_badge = get_font(18)
    badge_text = "SAINIK SCHOOL GUIDE INDIA"
    badge_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    badge_w = badge_bbox[2] - badge_bbox[0] + 40
    badge_x = (WIDTH - badge_w) // 2
    draw.rounded_rectangle([badge_x, 30, badge_x + badge_w, 68], radius=15, fill=(255, 255, 255, 80))
    draw.text((badge_x + 20, 36), badge_text, fill=(255, 255, 255), font=font_badge)

    # Title text
    font_title = get_font(52)
    lines = title.split('\n')
    y_start = 160
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_title)
        text_w = bbox[2] - bbox[0]
        x = (WIDTH - text_w) // 2
        # Shadow
        draw.text((x + 2, y_start + 2), line, fill=(0, 0, 0, 80), font=font_title)
        # Text
        draw.text((x, y_start), line, fill=(255, 255, 255), font=font_title)
        y_start += 70

    # Bottom bar
    draw.rounded_rectangle([100, HEIGHT - 120, WIDTH - 100, HEIGHT - 70], radius=12, fill=(255, 255, 255, 40))
    font_sub = get_font(22)
    sub_text = "sainikschooleastsiang.in  •  AISSEE 2027  •  Updated August 2026"
    sub_bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text(((WIDTH - sub_w) // 2, HEIGHT - 108), sub_text, fill=(255, 255, 255, 200), font=font_sub)

    # Decorative elements
    # Top left circle
    draw.ellipse([-50, -50, 150, 150], fill=(255, 255, 255, 15))
    # Bottom right circle
    draw.ellipse([WIDTH - 150, HEIGHT - 150, WIDTH + 50, HEIGHT + 50], fill=(255, 255, 255, 15))

    # Save as JPG
    output_path = os.path.join(OUTPUT_DIR, f"{filename}.jpg")
    img_rgb = img.convert('RGB')
    img_rgb.save(output_path, 'JPEG', quality=90)
    print(f"✅ Generated: {output_path}")
    return output_path

# Generate all images
print(f"🎨 Generating {len(articles)} featured images...\n")
for filename, title, emoji, colors in articles:
    generate_image(filename, title, emoji, colors)

print(f"\n🎉 Done! {len(articles)} images saved to: {OUTPUT_DIR}")
