@echo off

set /p IP_ADDRESS=Enter your IP address: 

echo IP_ADDRESS=%IP_ADDRESS%> .env
echo VITE_IP_ADDRESS=%IP_ADDRESS%> frontend\.env

start cmd /k "cd /d %~dp0 && pip install -r requirements.txt"
start cmd /k "cd /d %~dp0frontend && npm install"

echo "Setup complete."

exit