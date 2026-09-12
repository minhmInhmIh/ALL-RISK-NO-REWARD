#!/bin/bash

read -p "Enter your IP address: " IP_ADDRESS

echo "IP_ADDRESS=$IP_ADDRESS" > .env
echo "VITE_IP_ADDRESS=$IP_ADDRESS" > frontend/.env

python3 -m pip install -r requirements.txt

cd frontend
npm install

echo "Setup complete."