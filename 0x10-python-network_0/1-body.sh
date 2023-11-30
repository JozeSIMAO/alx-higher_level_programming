#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
# and displays the body of the response

url=$1
response_body=$(curl -s -w "%{http_code}" "$url")
status_code="${response_body: -3}"

if [ "$status_code" -eq 200 ]; then
  echo "${response_body%"$status_code"}"
else
  echo "Error: Unexpected status code - $status_code"
fi