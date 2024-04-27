#!/usr/bin/python3

"""Sends a request to the provided URL, and then displays the body of the
response. Should an error be encountered, the error code is printed"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            returned_data = response.read()
            print(returned_data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
