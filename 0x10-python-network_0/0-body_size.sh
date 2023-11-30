#!/bin/bash
# script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response

url=$1
response_body=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '/r')

echo $response_body