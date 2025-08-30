import json
import os
def add_task():
    
    task_file = "tasks.json"
    
    descption = input("what is your task : ")
    
    if not descption:
        print("you must input a task")
        return
    
    if not os.path.exists(task_file):
        with open(task_file, "w") as file:
            file.write("[]")
    
    try:
        with open(task_file , "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted, resetting.")
        tasks = []
        
    next_id = max([task["id"] for task in tasks] , default=0) + 1
    
    new_task = {
        "id": next_id,
        "description": descption,
        "status": "to_do"
    }
    
    tasks.append(new_task)
    try:
        with open(task_file, "w") as f:
            json.dump(tasks, f, indent=2)
        print(f"Task added successfully (ID: {next_id})")
    except Exception as e:
        print("Error: could not write tasks.json")
        print(e)
 