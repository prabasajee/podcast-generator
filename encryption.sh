#!/bin/bash
echo "=============================="

git config --global user.name "${GITHUB_USER}"
git config --global user.email "${GITHUB_EMAIL}"
git config --global --add safe.directory /github/workspace

python3 /usr/bin/feed.py

git add . -A && git commit -m "Update feed" || echo "No changes to commit"

git push origin main || echo "Push failed, check your credentials or network connection"
echo "=============================="