#!/usr/bin/python3
"""request data from api servers"""
import json
import requests
import sys


if __name__ == "__main__":
    value = sys.argv[1]
    username_url = 'https://jsonplaceholder.typicode.com/users?id={}'.format(value)
    data_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(value)
    username = requests.get(username_url)
    data = requests.get(data_url)
    username = username.json()
    data = data.json()
    """name = username[0].get('name')
    total_tasks = len(data)
    count = 0
    actual_done = []
    for item in data:
        if item.get('completed'):
            count += 1
            actual_done.append(item.get('title'))
    print("Employee {} is done with tasks {}/{}".format(name, count, total_tasks))
    for item in actual_done:
        print("\t{}".format(item))"""

    filename = "{}.json".format(value)
    dict_ = {}
    data_ = []
    for i, item in enumerate(data):
        dict_ = {}
        dict_["task"] = item.get("title")
        dict_["completed"] = item.get("completed")
        dict_["username"] = username[0].get("username")
        data_.append(dict_)
    line = {value: data}
    with open(filename, "w") as f:
        json.dump(line, f)
