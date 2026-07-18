#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
[ -x .venv/bin/python ] || python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r server/requirements.txt
cd server
python manage.py check
python manage.py test --verbosity 2
