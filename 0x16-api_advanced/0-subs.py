#!/usr/bin/python3
""" queries the Reddit API for the number of subscribers for a subreddit.
    If an invalid subreddit is given, the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """handles the actual querying"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "user-agent"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        return resp.json().get("data", {}).get("subscribers", 0)
    return 0
