#!/usr/bin/python3
"""recursivelly query reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """finds the hot titles"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}"\
        .format(subreddit, after)
    headers = {"user-agent": "user-agent"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    val = resp.json().get('data', {}).get('children')
    if val is None:
        if len(val) == 0:
            return None
        return hot_list
    for v in val:
        hot_list.append(v.get('data', {}).get('title'))
    after = resp.json().get('data', {}).get('after')
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
