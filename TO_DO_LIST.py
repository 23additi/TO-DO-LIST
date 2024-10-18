import json
import os

# File to store tasks
FILE_NAME = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{idx}. {task['title']} - {task['description']} [{task['category']}] - {status}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    task = {
        'title': title,
        'description': description,
        'completed': False,
        'category': category
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Edit a task
def edit_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['title'] = input("Enter new title: ")
            tasks[task_num]['description'] = input("Enter new description: ")
            tasks[task_num]['category'] = input("Enter new category: ")
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
