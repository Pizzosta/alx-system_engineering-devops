#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information
for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(sys.argv[1])).json()

    completed = [todo.get("title") for todo in todos
                 if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task))
