import json
import os
from datetime import datetime

def add_task(task_file):
    descption = input("what is your task : ")
    if not descption:
        print("you must input a task")
        return
    #creat the file if not exist
    if not os.path.exists(task_file):
        with open(task_file, "w") as file:
            file.write("[]")
    #handel if the json file is corrupted, and load it to tasks
    try:
        with open(task_file , "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted, resetting.")
        tasks = []
    #find the max id and add 1 to it for next id
    next_id = max([task["id"] for task in tasks] , default=0) + 1
    now = datetime.utcnow().isoformat()
    #creat the task dictionarie
    new_task = {
        "id": next_id,
        "description": descption,
        "status": "to_do",
        "created_date": now,
        "updated_date": now
    }
    #append the new task to the task list and convert it to json format
    tasks.append(new_task)
    try:
        with open(task_file, "w") as f:
            json.dump(tasks, f, indent=2)
        print(f"Task added successfully (ID: {next_id})")
    except Exception as e:
        print("Error: could not write tasks.json")
        print(e)
 