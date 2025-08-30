import json
from datetime import datetime
import os
from show_task import show_tasks
def update_task(task_file):
    if not os.path.exists(task_file):
        return
    else:
        with open(task_file, "r") as file:
            tasks = json.load(file)
        if not tasks:
            print("there is no task to update!")
            return
        show_tasks(task_file)
        try:
            task_id = int(input("which one you want to update? : "))
        except ValueError:
            print("your value is invalid!")
            return
        now = datetime.utcnow().isoformat()
        to_be_updated = int(input("if you want to update the description press : 1 \n if you want to update status press : 2  "))
        if to_be_updated == 1:
            new_decription = input("what is the new description : ")
            for task in tasks:
                if task["id"] == task_id:
                    task["description"] = new_decription
                    task["updated_date"] = now
                    break
        elif to_be_updated == 2:
            new_status = input("for mark as done press 'd' and 'l' for in progress  ")
            for task in tasks:
                if task["id"] == task_id:
                    if new_status == 'd':
                        task["status"] = "done"
                        task["updated_date"] = now
                        break
                    elif new_status == 'l':
                        task["status"] = "to_do"
                        task["updated_date"] = now
                        break
                    else:
                        print("invalid input!")
                        return
        with open(task_file , "w") as file:
            json.dump(tasks, file, indent=2)
        print(f"Task with ID {task_id} updated successfully!")