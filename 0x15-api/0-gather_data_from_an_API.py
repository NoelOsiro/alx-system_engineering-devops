#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed_tasks = [task for task in todos if task.get("completed")]
    completed_titles = [task.get("title") for task in completed_tasks]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))

    for title in completed_titles:
        print("\t {}".format(title))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    get_employee_todo_progress(employee_id)
