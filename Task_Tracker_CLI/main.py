from show_task import show_tasks
from add_task import add_task
from delete_task import delete_task
from update_task import update_task
import sys

def show_menu():
    print("\n--- Task Manager ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. delete task")
    print("4. update task")
    print("5. Exit")
       
while True:
    task_file = "tasks.json"
    show_menu()
    try:
        choice = int(input("What is your choice: "))
        if choice == 1:
            show_tasks(task_file)
        elif choice == 2:
            add_task(task_file)
        elif choice == 3:
            delete_task(task_file)
        elif choice == 4:
            update_task(task_file)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.") 
    except ValueError:
        print("invalid")
    