#!/usr/bin/python3

"""Fetches `https://alx-intranet.hbtn.io/status` using requests"""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url).text
    print(f'Body response:')
    print(f'\t- type: {type(response)}')
    print(f'\t- content: {response}')
