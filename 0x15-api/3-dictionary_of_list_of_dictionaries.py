#!/usr/bin/python3
"""records all tasks for all employees"""
import requests
import json


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(users_url).json()
    response = requests.get(todos_url).json()
    final_dict = {}
    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")
        value = []
        for i in response:
            if user_id == i["userId"]:
                json_entry = {'username': user['username'], 'completed': i['completed'], 'task': i['title']}
                value.append(json_entry)
        final_dict[user_id] = value
    with open(filename, "w") as f:
        json.dump(final_dict, f)
