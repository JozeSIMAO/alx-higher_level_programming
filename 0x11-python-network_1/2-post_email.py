#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        content = response.text
        print(f"Your email is: {content}")
    except requests.RequestException as e:
        print(f"Error: {e}")
