from show_task import show_tasks
from add_task import add_task
import sys

def show_menu():
    print("\n--- Task Manager ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")
       
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