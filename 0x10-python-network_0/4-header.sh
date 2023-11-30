#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL
# and displays the body of the response

url=$1
header="X-School-User-Id: 98"
response_body=$(curl -s -H "$header" "$url")

echo "$response_body"
