#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "============================================================"
echo "DriveSphere Cars Dealership - Setup and Run"
echo "============================================================"

if [ ! -x .venv/bin/python ]; then
  echo "[1/5] Creating virtual environment..."
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "[2/5] Installing dependencies..."
python -m pip install --upgrade pip
pip install -r server/requirements.txt

echo "[3/5] Applying migrations..."
cd server
python manage.py migrate --noinput

echo "[4/5] Loading demo data..."
python manage.py seed_demo

echo "[5/5] Starting Django server..."
echo "App:   http://127.0.0.1:8000/"
echo "Admin: http://127.0.0.1:8000/admin/"
echo "Reviewer: reviewer / Reviewer@123"
echo "Admin:    root / Root@123"
python manage.py runserver 0.0.0.0:8000
