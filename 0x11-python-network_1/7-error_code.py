#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the body of the response
Handles HTTP status codes >= 400 using requests package
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
