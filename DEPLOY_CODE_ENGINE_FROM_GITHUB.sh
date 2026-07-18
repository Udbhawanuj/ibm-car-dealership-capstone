#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 https://github.com/USERNAME/REPOSITORY.git [APP_NAME]"
  exit 1
fi
SOURCE_URL="$1"
APP_NAME="${2:-cars-dealership}"

ibmcloud ce application create \
  --name "$APP_NAME" \
  --build-source "$SOURCE_URL" \
  --port 8000 \
  --min-scale 1 \
  --max-scale 1 \
  --wait-timeout 900 || \
ibmcloud ce application update \
  --name "$APP_NAME" \
  --build-source "$SOURCE_URL" \
  --port 8000 \
  --min-scale 1 \
  --max-scale 1 \
  --wait-timeout 900

URL="$(ibmcloud ce application get -n "$APP_NAME" -o url)"
printf '%s\n' "$URL" | tee evidence/deploymentURL
echo "Deployment ready: $URL"
