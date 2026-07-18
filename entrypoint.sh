#!/usr/bin/env sh
set -eu

cd /app
python manage.py migrate --noinput
python manage.py seed_demo
python manage.py collectstatic --noinput

PORT_VALUE="${PORT:-8000}"
exec gunicorn dealership_project.wsgi:application \
  --bind "0.0.0.0:${PORT_VALUE}" \
  --workers 1 \
  --threads 4 \
  --timeout 120 \
  --access-logfile - \
  --error-logfile -
