#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import requests

    MAX_COMMITS = 10
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repo_name
    )
    headers = {'Accept': 'application/vnd.github+json'}
    response = requests.request('GET', url, headers=headers)
    response_json = response.json()

    # fetch the first 10 commits, and output the sha-author pairs
    for item in response_json[:MAX_COMMITS]:
        sha = item['sha']
        author = item['commit']['author']['name']
        print(f'{sha}: {author}')
