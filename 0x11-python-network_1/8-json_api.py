#!/usr/bin/python3

"""Takes in a letter and POSTs a request to `http://0.0.0.0:5000/search_user`
with the letter as a parameter
"""

if __name__ == '__main__':
    import sys
    import requests

    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    response = requests.post(url, data=data)
    try:
        json_response = response.json()
    except requests.exceptions.JSONDecodeError:
        print('No result')
        sys.exit()

    if not len(json_response):
        print('No result')
    else:
        user_id = json_response.get('id')
        name = json_response.get('name')
        print(f'[{user_id}] {name}')
