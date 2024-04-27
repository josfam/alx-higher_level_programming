#!/usr/bin/python3

"""Sends a POST request to the provided URL, with the provided email as a
parameter. It then displays the body of the response."""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    # turn into proper format, and to bytes
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        returned_data = response.read()
        print(returned_data.decode('utf-8'))
