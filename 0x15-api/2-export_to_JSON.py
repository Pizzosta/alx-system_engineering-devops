#!/usr/bin/python3
""" Script that uses JSONPlaceholder API and exports TODO list
information of a given employee ID to JSON format.
usage ./2-export_to_JSON.py <ID>"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos?userId={}".format(user_id)).json()

    todo_list = {user_id: []}

    for todo in todos:
        todo_list[user_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    filename = "{}.json".format(user_id)
    with open(filename, mode="w") as jsonfile:
        json.dump(todo_list, jsonfile)
