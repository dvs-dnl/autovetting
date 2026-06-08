#!/usr/bin/env bash
# One-time: wire scripts/ as the git hooks path for this clone.
# Idempotent — safe to run multiple times.

set -e
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

current="$(git config --local core.hooksPath || echo '')"
if [ "$current" = "scripts/" ] || [ "$current" = "scripts" ]; then
  echo "✓ core.hooksPath already set to scripts/ — nothing to do."
  exit 0
fi

git config --local core.hooksPath scripts/
echo "✓ Wired core.hooksPath → scripts/"
echo "  Pre-push hook will now run scripts/gate-check.py before any push."
echo "  Bypass for one-off pushes with: git push --no-verify"
