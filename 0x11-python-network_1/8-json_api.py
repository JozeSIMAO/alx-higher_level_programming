#!/usr/bin/python3
"""
Takes in a letter, sends a POST request
and displays the id and name from the JSON response Uses requests package
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        user_data = response.json()
        if user_data:
            print(f"[{user_data['id']}] {user_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
