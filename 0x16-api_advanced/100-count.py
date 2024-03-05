#!/usr/bin/python3
"""recursivelly query reddit api"""
import requests


def count_words(subreddit, word_list):
    """finds the hot titles"""
    url = "https://www.reddit.com/r/{}/hot.json"\
        .format(subreddit)
    headers = {"user-agent": "user-agent"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    val = resp.json().get('data', {})
    if val is None:
        return print()
    array_word_lists = word_list.split(" ")
    for item in array_word_list:
        count = val.count(item)
        print(item + ": " + count)
