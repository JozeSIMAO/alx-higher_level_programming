#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
# and displays the body of the response

url=$1

# Set the variables for the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with the specified variables and store the response body in a variable
response_body=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "$response_body"