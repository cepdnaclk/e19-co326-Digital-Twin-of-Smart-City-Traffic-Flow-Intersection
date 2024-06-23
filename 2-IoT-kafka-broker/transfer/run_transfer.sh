#!/bin/bash

# Loop indefinitely
echo "Starting script loop..."
while true; do
  python3 transfer-0.py > /dev/null 2>&1 &
  python3 transfer-1.py > /dev/null 2>&1 &
  python3 transfer-2.py > /dev/null 2>&1 &
  sleep 20
done
