#!/usr/bin/env bash
# build.sh — pack starter-brain.zip + demo-data.zip for the Finding Camp workshop USB.
# Usage: ./build.sh            (from this folder)
# Refuses to pack if any smoke-test residue or secrets are inside starter-brain.
set -euo pipefail
cd "$(dirname "$0")"

# 1. Guard: no smoke-test outputs, no PATI-specific strings inside the starter vault.
residue=$(find starter-brain -type f \( -name 'hello.md' -o -path '*96-daily/*.md' -o -path '*40-hr/candidates/*.md' -o -path '*10-work/*.md' \) 2>/dev/null || true)
if [ -n "$residue" ]; then echo "REFUSE: smoke-test residue in starter-brain:"; echo "$residue"; exit 1; fi
if grep -rIl -E 'LLM-Wiki|9router|40\.1-hiring|patigroup|ANTHROPIC_API_KEY' starter-brain >/dev/null; then
  echo "REFUSE: PATI-specific strings found:"; grep -rIl -E 'LLM-Wiki|9router|40\.1-hiring|patigroup|ANTHROPIC_API_KEY' starter-brain; exit 1
fi

# 2. Pack (exclude macOS junk).
rm -f starter-brain.zip demo-data.zip
zip -qr starter-brain.zip starter-brain -x '*.DS_Store' '*/.obsidian/*'
zip -qr demo-data.zip demo-data -x '*.DS_Store'

# 3. Report what was packed (numbers, not "PASS").
echo "starter-brain: $(find starter-brain -type f -not -path '*/.claude/skills/*' | wc -l | tr -d ' ') vault files + $(find starter-brain/.claude/skills -type f | wc -l | tr -d ' ') skill files in $(ls -d starter-brain/.claude/skills/*/ | wc -l | tr -d ' ') skills"
echo "demo-data:     $(find demo-data -type f | wc -l | tr -d ' ') files"
ls -la starter-brain.zip demo-data.zip | awk '{print $5" bytes  "$9}'
