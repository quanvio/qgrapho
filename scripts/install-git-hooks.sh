#!/usr/bin/env bash
# Install git hooks that remove Cursor co-author trailers from commits.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK_SRC="$ROOT/scripts/hooks/prepare-commit-msg"
HOOK_DST="$ROOT/.git/hooks/prepare-commit-msg"

if [[ ! -d "$ROOT/.git" ]]; then
  echo "Error: run from a git clone (no .git directory)."
  exit 1
fi

cp "$HOOK_SRC" "$HOOK_DST"
chmod +x "$HOOK_DST"
echo "Installed: .git/hooks/prepare-commit-msg"
