#!/bin/bash
# Backlink Outreach Automation Script
# Usage: bash backlink-outreach.sh [quora|reddit|directories|track]

REPO_DIR="/home/work/.openclaw/workspace/sainik-school-guide"
TRACKING_FILE="$REPO_DIR/.automation/backlink-tracking.csv"

# Initialize tracking file if not exists
if [ ! -f "$TRACKING_FILE" ]; then
    echo "Website,URL,DA,Method,Contact,Status,Date Sent,Follow Up,Link URL,Notes" > "$TRACKING_FILE"
fi

case "$1" in
    "quora")
        echo "🔍 Finding Quora questions about Sainik Schools..."
        echo ""
        echo "Search these on Quora:"
        echo "1. site:quora.com sainik school admission 2027"
        echo "2. site:quora.com AISSEE preparation tips"
        echo "3. site:quora.com sainik school fees"
        echo "4. site:quora.com sainik school age limit"
        echo "5. site:quora.com best sainik school India"
        echo "6. site:quora.com sainik school vs military school"
        echo "7. site:quora.com NDA after sainik school"
        echo "8. site:quora.com sainik school hostel life"
        echo ""
        echo "📝 Answer Template:"
        echo "---"
        echo "Great question! Here's what I know:"
        echo ""
        echo "[Your answer - 3-4 paragraphs]"
        echo ""
        echo "I wrote a detailed guide about this: [LINK]"
        echo "Hope this helps!"
        echo "---"
        ;;
    
    "reddit")
        echo "🔍 Reddit posting schedule..."
        echo ""
        echo "Target subreddits:"
        echo "1. r/IndianEducation (50K+ members)"
        echo "2. r/IndianParents (30K+ members)"
        echo "3. r/India (500K+ members)"
        echo "4. r/IndianAcademia (20K+ members)"
        echo "5. r/CBSE (15K+ members)"
        echo "6. r/IndianDefence (10K+ members)"
        echo ""
        echo "📝 Post Ideas:"
        echo "1. Free age calculator tool"
        echo "2. Complete AISSEE preparation guide"
        echo "3. Sainik School comparison (vs RIMC vs RMS)"
        echo "4. Scholarship guide for SC/ST students"
        echo "5. Previous year papers analysis"
        echo ""
        echo "⚠️ Rules:"
        echo "- Don't spam - 1 post per subreddit per week"
        echo "- Add value first, link second"
        echo "- Engage with comments"
        ;;
    
    "directories")
        echo "📋 Directory submission checklist..."
        echo ""
        echo "High Priority (Do First):"
        echo "□ Google My Business - business.google.com"
        echo "□ Bing Places - bingplaces.com"
        echo "□ Justdial - justdial.com"
        echo "□ Sulekha - sulekha.com"
        echo ""
        echo "Education Directories:"
        echo "□ Shiksha - shiksha.com"
        echo "□ CollegeDekho - collegedekho.com"
        echo "□ Careers360 - careers360.com"
        echo "□ Ezyschooling - ezyschooling.com"
        echo "□ SchoolMyKids - schoolmykids.com"
        echo ""
        echo "General Directories:"
        echo "□ IndiaMART - indiamart.com"
        echo "□ Yellow Pages - yellowpages.in"
        echo "□ AskLaila - asklaila.com"
        echo "□ TradeIndia - tradeindia.com"
        ;;
    
    "track")
        echo "📊 Backlink Tracking Summary"
        echo ""
        echo "Total entries: $(tail -n +2 "$TRACKING_FILE" | wc -l)"
        echo ""
        echo "By Status:"
        echo "- Not Started: $(grep -c 'Not Started' "$TRACKING_FILE" 2>/dev/null || echo 0)"
        echo "- Sent: $(grep -c 'Sent' "$TRACKING_FILE" 2>/dev/null || echo 0)"
        echo "- Accepted: $(grep -c 'Accepted' "$TRACKING_FILE" 2>/dev/null || echo 0)"
        echo "- Rejected: $(grep -c 'Rejected' "$TRACKING_FILE" 2>/dev/null || echo 0)"
        echo ""
        echo "Recent entries:"
        tail -5 "$TRACKING_FILE"
        ;;
    
    "email")
        echo "📧 Outreach Email Templates"
        echo ""
        echo "1. Guest Post Pitch:"
        echo "   Subject: Guest Post: [TOPIC TITLE]"
        echo "   → See backlink-outreach.md for full template"
        echo ""
        echo "2. Resource Page:"
        echo "   Subject: Adding Sainik School Guide to your resources"
        echo "   → See backlink-outreach.md for full template"
        echo ""
        echo "3. Broken Link:"
        echo "   Subject: Broken link on [WEBSITE NAME]"
        echo "   → See backlink-outreach.md for full template"
        ;;
    
    *)
        echo "🔗 Backlink Outreach Automation"
        echo ""
        echo "Usage: bash backlink-outreach.sh [command]"
        echo ""
        echo "Commands:"
        echo "  quora      - Quora answer templates & targets"
        echo "  reddit     - Reddit posting schedule"
        echo "  directories - Directory submission checklist"
        echo "  track      - View tracking summary"
        echo "  email      - Outreach email templates"
        echo ""
        echo "Full guide: .automation/backlink-outreach.md"
        ;;
esac
