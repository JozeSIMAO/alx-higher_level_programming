#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.

url=$1
allow_header=$(curl -s -I -X OPTIONS "$url" | grep -i "Allow:")

if [ -n "$allow_header" ]; then
  methods=$(echo "$allow_header" | sed -E 's/Allow: (.*)/\1/' | tr -d '\r')
  echo "$methods"
else
  echo "Error: Allow header not found in the response."
fi
