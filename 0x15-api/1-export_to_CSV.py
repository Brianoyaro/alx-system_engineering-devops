#!/usr/bin/python3
"""request data from api servers"""
import requests
import sys


if __name__ == "__main__":
    value = int(sys.argv[1])
    name_url = 'https://jsonplaceholder.typicode.com/users?id={}'.format(value)
    data_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(value)
    username = requests.get(name_url)
    data = requests.get(data_url)
    username = username.json()
    data = data.json()
    """name = username[0].get('name')
    total = len(data)
    count = 0
    actual_done = []
    for item in data:
        if item.get('completed'):
            count += 1
            actual_done.append(item.get('title'))
    print("Employee {} is done with tasks {}/{}".format(name, count, total))
    for item in actual_done:
        print("\t{}".format(item))"""

    filename = "{}.csv".format(value)
    u_name = username[0].get('username')
    line = ""
    for item in data:
        line += '"{}","{}","{}","{}"\n'.\
                format(value, u_name, item.get('completed'), item.get('title'))
    with open(filename, "w")as f:
        f.write(line)
