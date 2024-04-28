#!/usr/bin/python3

"""Takes GitHub credentials and uses the GitHub API to display the user's id"""

if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    access_token = sys.argv[2]

    url = 'https://api.github.com/users/{}'.format(username)
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {access_token}',
    }

    req = requests.request('GET', url, headers=headers)
    json_response = req.json()
    if json_response.get('message', None) == 'Bad credentials':
        print('None')
    else:
        print(json_response.get('id'))
