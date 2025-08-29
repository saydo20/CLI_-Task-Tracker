Task Tracker CLI

A simple Command Line Interface (CLI) application to track and manage your tasks and to-do list. This project helps you practice working with the filesystem, handling user input, and building CLI applications.

Features

Add, update, and delete tasks

Mark tasks as in progress or done

List all tasks

List tasks filtered by status: done, todo, or in-progress

Persistent storage using a JSON file

Task Properties

Each task has the following properties:

id: Unique identifier for the task

description: Short description of the task

status: Task status (todo, in-progress, done)

createdAt: Date and time when the task was created

updatedAt: Date and time when the task was last updated

Installation & Setup

Ensure your development environment is ready:

Install your preferred programming language (Python, JavaScript, etc.)

Use a code editor like VSCode or PyCharm

Usage

Run the CLI application from the command line with the following commands:

Add a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

Update or delete a task
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

Mark a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

List tasks
# List all tasks
task-cli list

# List tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

Implementation Guidelines

Use positional arguments to accept user inputs.

Store tasks in a JSON file in the project directory.

Create the JSON file if it does not exist.

Use the native file system module of your language; no external libraries required.

Handle errors and edge cases gracefully.

Project Roadmap

Set up CLI structure – Handle user inputs

Implement features – Add, list, update, delete, mark tasks

Testing & debugging – Verify tasks are correctly stored in JSON

Finalize project – Clean code, add comments, and polish README

License

This project is open source and free to use.