#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
APP_NAME="${1:-cars-dealership}"

if ! command -v ibmcloud >/dev/null 2>&1; then
  echo "ibmcloud CLI was not found. Run this inside the Skills Network Code Engine CLI."
  exit 1
fi

ibmcloud ce application create \
  --name "$APP_NAME" \
  --build-source . \
  --port 8000 \
  --min-scale 1 \
  --max-scale 1 \
  --wait-timeout 900 || \
ibmcloud ce application update \
  --name "$APP_NAME" \
  --build-source . \
  --port 8000 \
  --min-scale 1 \
  --max-scale 1 \
  --wait-timeout 900

URL="$(ibmcloud ce application get -n "$APP_NAME" -o url)"
printf '%s\n' "$URL" | tee evidence/deploymentURL
echo "Deployment ready: $URL"
