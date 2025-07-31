#!/bin/bash
set -e

echo "Waiting for Elasticsearch ..."

until curl -s "http://elasticsearch:9200" > /dev/null; do
  echo "Elasticsearch is unavailable - sleeping"
  sleep 2
done

echo "Elasticsearch is up! Running mapping script..."
sleep 5

python mapping.py

echo "Starting FastAPI app..."

exec uvicorn main:app --host 0.0.0.0 --port 8000
