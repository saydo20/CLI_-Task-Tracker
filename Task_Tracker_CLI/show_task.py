import json

def show_tasks(task_file):
    try:
        with open(task_file, "r") as file:
            tasks = json.load(file)
            if not tasks:
                print("There are no tasks.")
                return 0
            else:
                grouped_tasks = {}
                for task in tasks:
                    status = task['status']
                    if status not in grouped_tasks:
                        grouped_tasks[status] = []
                    grouped_tasks[status].append(task) 
                    
            for status, tasks_list in grouped_tasks.items():
                print(f"\nTasks {status}:")
                for task in tasks_list:
                    print(f"{task['id']}. {task['description']}")

    except FileNotFoundError:
        print("\nThere is no tasks file.")
        return 0
