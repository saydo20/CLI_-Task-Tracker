from show_task import show_tasks
import os
import json
def delete_task(task_file):
    if  not os.path.exists(task_file):
        return
    else:
        with open(task_file, "r") as file:
            tasks = json.load(file)
        if not tasks:
            print("there is no task to delete!")
            return
        show_tasks(task_file)
        try:
            task_id = int(input("which one you want to delete? : "))
        except ValueError:
            print("your value is invalid!")
            return
        updated_tasks = [task for task in tasks if task["id"] != task_id]
        
        for index, task in enumerate(updated_tasks, start=1):
            task["id"] = index
        if len(updated_tasks) == len(tasks):
            print(f"No task with ID {task_id} found.")
            return
        with open(task_file, "w") as file:
            json.dump(updated_tasks, file, indent=2)
        print(f"Task with ID {task_id} deleted successfully.")
        
        