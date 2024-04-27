#!/usr/bin/python3

"""Python script that fetche data (with `requests`) from a URL and displays the
value of the `X-Request-Id` variable found in the header of the response"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    print(headers.get('X-Request-Id'))
