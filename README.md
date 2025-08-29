📝 Task Tracker CLI

A Command Line Interface (CLI) application to manage your tasks and to-do list.
Keep track of what you need to do, what you’re currently working on, and what’s done—all from the terminal!

⚡ Features

Add new tasks

Update existing tasks

Delete tasks

Mark tasks as in-progress or done

List tasks by status: todo, in-progress, done

Store tasks persistently using a JSON file

📋 Task Properties

Each task includes:

Property	Description
id	Unique identifier for the task
description	Short description of the task
status	Task status (todo, in-progress, done)
createdAt	Date and time when the task was created
updatedAt	Date and time when the task was last updated
🚀 Installation & Setup


Ensure your environment is ready:

Install a programming language (Python, JavaScript, etc.)

Open the project in your code editor (VSCode, PyCharm, etc.)

💻 Usage
Add a task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

Update a task
task-cli update 1 "Buy groceries and cook dinner"

Delete a task
task-cli delete 1

Mark a task
task-cli mark-in-progress 1
task-cli mark-done 1

List tasks
# List all tasks
task-cli list

# List tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

🛠 Implementation Guidelines

Use positional arguments for user inputs

Store tasks in a JSON file in the project directory

Automatically create the JSON file if it does not exist

Use the native file system of your programming language

Handle errors and edge cases gracefully

No external libraries required

📈 Project Roadmap

Build basic CLI structure

Implement Add, List, Update, Delete features

Implement status marking (in-progress, done)

Test and debug thoroughly

Finalize project with clean code and documentation

🎉 License

This project is open-source and free to use.