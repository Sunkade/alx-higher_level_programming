#!/usr/bin/python3
"""
Uses GitHub API to display your user ID
"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        user_data = response.json()
        user_id = user_data.get('id')
        print("Your GitHub ID: {}".format(user_id))
    except ValueError:
        print("Not a valid JSON response. Check your credentials.")
