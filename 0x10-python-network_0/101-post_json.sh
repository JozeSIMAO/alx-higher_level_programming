#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file
if [ -f "$2" ]; then
    curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" | grep "Valid JSON" && echo "" || echo "Not a valid JSON"
