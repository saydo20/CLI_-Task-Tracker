import sys
import json
import os
from datetime import datetime

def show_menu():
    print("\n--- Task Manager ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")


def show_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            if not tasks:
                print("There are no tasks.")
            else:
                print("\nYour tasks are:")
                for task in tasks:
                    print(f"{task['id']}. {task['description']} [{task['status']}]")
    except FileNotFoundError:
        print("There is no tasks file.")

def add_task():
    TASKS_FILE = "tasks.json"

    # Ask the user for task description
    description = input("Enter task description: ").strip()

    if not description:
        print("Error: description is required.")
        return

    # Ensure tasks.json exists
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            f.write("[]")

    # Load existing tasks
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted, resetting.")
        tasks = []

    # Generate next ID
    next_id = max([task["id"] for task in tasks], default=0) + 1

    # Current timestamp
    now = datetime.utcnow().isoformat() + "Z"

    # Create new task
    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    # Append and save tasks
    tasks.append(new_task)
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
        print(f"Task added successfully (ID: {next_id})")
    except Exception as e:
        print("Error: could not write tasks.json")
        print(e)

while True:
    show_menu()
    choice = int(input("What is your choice: "))
    if choice == 1:
        show_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")