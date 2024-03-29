#!/usr/bin/python3
""" Script that uses JSONPlaceholder API and exports TODO list
information of employees to JSON format.
usage <./3-dictionary_of_list_of_dictionaries.py>"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    todo_all_employees = {}

    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + "todos?userId={}".format(user_id)).json()

        todo_all_employees[user_id] = []
        for todo in todos:
            todo_all_employees[user_id].append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            })

    filename = "todo_all_employees.json"
    with open(filename, mode="w") as jsonfile:
        json.dump(todo_all_employees, jsonfile)
