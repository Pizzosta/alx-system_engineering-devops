#!/usr/bin/python3
""" Script that uses JSONPlaceholder API and exports TODO list
information of a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos?userId={}".format(user_id)).json()

    filename = "{}.csv".format(user_id)
    with open(filename, mode="w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [user_id, username, todo.get("completed"), todo.get("title")]
            )
