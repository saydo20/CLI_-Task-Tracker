import json
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
