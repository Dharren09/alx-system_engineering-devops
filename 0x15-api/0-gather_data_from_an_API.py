#!/usr/bin/python3

"""Returns information about employee TODO list progress"""

import requests


def get_employee_todo_progress(employee_id):
    # URL for API endpoint
    url = f"https://jsonplaceholder.typicode.com/todos?userid={employee_id}"

    # Get the response from the API
    response = requests.get(url)

    # Check if response was successful
    if response.status_code == 200:

        # Get the JSON data from the response
        data = response.json()

        # Count the number of completed tasks
        completed_tasks = len([task for task in data if task["completed"]])
        total_tasks = len(data)

        # Get the employee name
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_response = requests.get(url)
        employee_data = employee_response.json()
        employee_name = employee_data["name"]

        # Print the results
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in data:
            if task["completed"]:
                print(f"\t {task['title']}")
    else:
        print("An error occurred while retrieving the data")
