# Python Networking Scripts

This repository contains Python scripts for network-related tasks, adhering to specific requirements and standards.

## Table of Contents

- [Scripts](#scripts)
- [General Information](#general-information)
- [Requirements](#requirements)
- [Usage](#usage)
- [Testing](#testing)

## Scripts

1. **0-hbtn_status.py**: Fetches https://alx-intranet.hbtn.io/status using urllib.

2. **1-hbtn_header.py**: Takes a URL, sends a request, and displays the value of the X-Request-Id variable in the header.

3. **2-post_email.py**: Sends a POST request with an email parameter to the provided URL and displays the response body.

4. **3-error_code.py**: Takes a URL, sends a request, and displays the body of the response. Handles HTTP errors using urllib.

5. **4-hbtn_status.py**: Fetches https://alx-intranet.hbtn.io/status using the requests package.

6. **5-hbtn_header.py**: Takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header using requests.

7. **6-post_email.py**: Sends a POST request with an email parameter to the provided URL and displays the response body using requests.

8. **7-error_code.py**: Takes a URL, sends a request, and displays the body of the response. Handles HTTP errors using requests.

9. **8-json_api.py**: Takes a letter, sends a POST request, and displays user information from the JSON response.

10. **10-my_github.py**: Uses GitHub API to display the user id with Basic Authentication.

## General Information

These scripts are designed to perform various network-related tasks using Python. Each script is a standalone program that adheres to specific coding standards and requirements.

## Requirements

- **Editors**: vi, vim, emacs
- **OS**: Ubuntu 20.04 LTS
- **Python Version**: 3.8.5
- **Coding Style Checker**: pycodestyle (version 2.8.*)
- **Packages**: urllib, requests
- **Execution**: All files must be executable
- **Documentation**: Each module should have proper documentation (`python3 -c 'print(__import__("my_module").__doc__)`)
- ...

## Usage

To use a script, run it from the command line with the appropriate arguments:

```bash
./script_name.py [arguments]
