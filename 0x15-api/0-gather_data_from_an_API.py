#!/usr/bin/python3
"""request data from api servers"""
import requests
import sys


value = int(sys.argv[1])
username_url = 'https://jsonplaceholder.typicode.com/users?id={}'.format(value)
data_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(value)
username = requests.get(username_url)
data = requests.get(data_url)
username = username.json()
data = data.json()
name = username[0].get('name')
total_tasks = len(data)
count = 0
actual_done = []
for item in data:
    if item.get('completed'):
        count += 1
        actual_done.append(item.get('title'))
print("Employee {} is done with tasks {}/{}".format(name, count, total_tasks))
for item in actual_done:
    print("\t{}".format(item))
