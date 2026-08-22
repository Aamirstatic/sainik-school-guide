#!/bin/bash
# Sainik School Guide - Content Pipeline
# Usage: bash content-pipeline.sh [blog|school] "topic slug"
# This script handles: git pull → build check → commit → push

set -e

REPO_DIR="/home/work/.openclaw/workspace/sainik-school-guide"
HUGO_BIN="$HOME/bin/hugo"
BRANCH="master"

cd "$REPO_DIR"

echo "📥 Pulling latest changes..."
git pull origin "$BRANCH" --rebase 2>&1 || true

echo "🔨 Building site..."
$HUGO_BIN --minify 2>&1
BUILD_STATUS=$?

if [ $BUILD_STATUS -ne 0 ]; then
    echo "❌ Hugo build failed! Fix errors before pushing."
    exit 1
fi

echo "✅ Build successful"

# Check if there are changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "📭 No changes to commit"
    exit 0
fi

# Stage all changes
git add -A

# Generate commit message
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
CHANGED_FILES=$(git diff --cached --name-only | head -5)
COMMIT_MSG="📝 Content update: $TIMESTAMP

Files changed:
$CHANGED_FILES"

echo "💾 Committing..."
git commit -m "$COMMIT_MSG"

echo "🚀 Pushing to GitHub..."
git push origin "$BRANCH"

echo "✅ Done! Cloudflare Pages will auto-deploy in ~2 minutes."
echo "🌐 Site: https://sainikschooleastsiang.in/"
