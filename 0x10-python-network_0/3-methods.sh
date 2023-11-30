#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.

url=$1

# Use curl to send an OPTIONS request and retrieve the Allow header
allow_header=$(curl -s -I -X OPTIONS "$url" | grep -i "Allow:")

# Extract and display the HTTP methods allowed by the server
if [ -n "$allow_header" ]; then
  methods=$(echo "$allow_header" | sed -E 's/Allow: (.*)/\1/' | tr -d '\r')
  echo "$methods"
else
  echo "Error: Allow header not found in the response."
fi