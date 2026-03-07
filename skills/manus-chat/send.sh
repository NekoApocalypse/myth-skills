#!/usr/bin/env bash

# Helper script to send requests to Manus IPC Daemon
PROMPT="$1"

if [ -z "$PROMPT" ]; then
    echo "Error: Prompt required."
    exit 1
fi

curl -s -X POST http://127.0.0.1:17171/send \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"${PROMPT}\"}"
