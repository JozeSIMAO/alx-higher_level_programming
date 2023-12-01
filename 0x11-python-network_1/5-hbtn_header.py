#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value of
the variable X-Request-Id Uses requests package
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    header_value = response.headers.get('X-Request-Id')
    print(header_value)
