#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

osascript -e "tell application \"Terminal\" to do script \"cd '$SCRIPT_DIR/app' && python3 -m uvicorn app:app --reload --host 0.0.0.0 --port 8000\""

osascript -e "tell application \"Terminal\" to do script \"cd '$SCRIPT_DIR/frontend' && npm run dev -- --host 0.0.0.0\""

echo "Game Started."