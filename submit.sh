#!/bin/zsh

./scripts/publish-next.py && ./scripts/clean-up-tags.py && ./scripts/tweet-most-recent.py | pbcopy && git add _posts/ && git commit -m "New post $(date +%Y-%m-%d)" && git push && ./scripts/create-tomorrows-file.py
