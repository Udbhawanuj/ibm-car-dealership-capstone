#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
[ -x .venv/bin/python ] || python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r server/requirements.txt
python scripts/generate_evidence.py --start-server --base-url http://127.0.0.1:8000
echo "DONE. Open the evidence folder."
