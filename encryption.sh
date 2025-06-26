#!/bin/bash
echo "=============================="

# Set git config with fallback values if not set
if [ -z "$GITHUB_USER" ]; then
  git config --global user.name "github-actions[bot]"
else
  git config --global user.name "$GITHUB_USER"
fi
if [ -z "$GITHUB_EMAIL" ]; then
  git config --global user.email "github-actions[bot]@users.noreply.github.com"
else
  git config --global user.email "$GITHUB_EMAIL"
fi
git config --global --add safe.directory /github/workspace

python3 /usr/bin/feed.py

git add . -A && git commit -m "Update feed" || echo "No changes to commit"

git push origin main || echo "Push failed, check your credentials or network connection"
echo "=============================="