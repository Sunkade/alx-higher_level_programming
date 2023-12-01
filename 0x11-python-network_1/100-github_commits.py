#!/usr/bin/python3
"""
Lists 10 most recent commits of a GitHub repository by a user
"""

import requests
import sys

if __name__ == '__main__':
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    commits = response.json()

    for commit in reversed(commits):
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f'{sha}: {author_name}')
