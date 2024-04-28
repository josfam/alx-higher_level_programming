#!/usr/bin/python3

"""Sends a request to the provided URL (with `requests`), and then displays
the body of the response.
Should an error be encountered, the error code is printed"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)
    status_code = response.status_code
    if status_code >= 400:
        print(f'Error code: {status_code}')
    else:
        print(response.text)
