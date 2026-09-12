@echo off

start cmd /k "cd /d %~dp0app && python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000"

start cmd /k "cd /d %~dp0frontend && npm run dev -- --host 0.0.0.0"

exit