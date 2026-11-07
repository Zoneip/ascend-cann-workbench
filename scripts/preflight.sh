#!/usr/bin/env bash
# Read-only: includes untracked non-ignored publication candidates.
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "$0")/.." && pwd)"
exec python3 -B "$ROOT/scripts/preflight.py"
