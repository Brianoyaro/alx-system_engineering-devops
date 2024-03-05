#!/usr/bin/python3
"""prints the titles of 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """finds the top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10&t=all"\
        .format(subreddit)
    headers = {"user-agent": "user-agent"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        val = resp.json()['data']['children']
        for v in val:
            print(v['data']['title'])
    else:
        print("None")
