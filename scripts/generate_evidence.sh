#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"
python scripts/generate_evidence.py --base-url "${1:-http://127.0.0.1:8000}"
