#!/bin/bash
set -e

ES_HOST="elasticsearch"
ES_PORT=9200
ES_URL="http://$ES_HOST:$ES_PORT"

echo "Waiting for Elasticsearch at $ES_URL ..."

until curl -s "$ES_URL" > /dev/null; do
  echo "Elasticsearch is unavailable - sleeping"
  sleep 2
done

echo "Elasticsearch is up! Running mapping script..."

python mapping.py

echo "Starting FastAPI app..."

exec uvicorn main:app --host 0.0.0.0 --port 8000
