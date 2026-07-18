#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "Run ./RUN_PROJECT_LINUX_MAC.sh first."
  exit 1
fi
source .venv/bin/activate
python scripts/generate_evidence.py --base-url http://127.0.0.1:8000
