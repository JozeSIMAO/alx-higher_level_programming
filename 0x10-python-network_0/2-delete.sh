#!/usr/bin/env bash
# script that sends a DELETE request to the URL passed as the first argument
# and displays the body of the response
# Check if a URL is provided as the first argument

url=$1

# Use curl to send a DELETE request and store the response body in a variable
response_body=$(curl -s -X DELETE "$url")

# Display the body of the response
echo "$response_body"
