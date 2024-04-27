#!/usr/bin/python3

"""Sends a POST request to the provided URL (using `requests`),
with the provided email as a parameter.
It then displays the body of the response."""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    req = requests.post(url, data=values)
    response = req.text
    print(response)
