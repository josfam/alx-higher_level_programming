#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io and displays the
value of the `X-Request-Id` variable found in the header of the response"""

if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
