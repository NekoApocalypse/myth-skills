#!/bin/bash
# snapshot.sh - Take a daily snapshot of PROJECTS.md
#
# Usage: ./snapshot.sh
# Output: Copies PROJECTS.md to vault/myth-projects-stash/daily-snapshots/{YYYY-MM-DD}_PROJECTS.md

set -e

WORKSPACE_ROOT="/home/node/.openclaw/workspace"
SOURCE="${WORKSPACE_ROOT}/PROJECTS.md"
DEST_DIR="${WORKSPACE_ROOT}/vault/myth-projects-stash/daily-snapshots"
DATE=$(TZ='Asia/Shanghai' date +%Y-%m-%d)
DEST="${DEST_DIR}/${DATE}_PROJECTS.md"

if [ ! -f "$SOURCE" ]; then
    echo "Error: Source file not found: $SOURCE" >&2
    exit 1
fi

mkdir -p "$DEST_DIR"
cp "$SOURCE" "$DEST"
echo "Snapshot saved: $DEST"
