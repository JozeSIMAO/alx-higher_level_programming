#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument
# and displays the body of the response
# Check if a URL is provided as the first argument

url=$1
response_body=$(curl -s -X DELETE "$url")

echo "$response_body"
