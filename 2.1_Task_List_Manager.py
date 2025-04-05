def display_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("\nTask list is empty.")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task[0]} (Priority: {task[1]})")


def add_task(tasks):
    """Add a new task to the list."""
    task_name = input("Enter the task name: ")
    priority = input("Enter the task priority (High/Medium/Low): ")
    tasks.append((task_name, priority.capitalize()))
    print("Task added successfully.")


def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task[0]}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def update_task(tasks):
    """Update a task in the list."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            task_name = input("Enter the new task name: ")
            priority = input("Enter the new priority (High/Medium/Low): ")
            tasks[task_number - 1] = (task_name, priority.capitalize())
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def sort_tasks(tasks):
    """Sort tasks by priority."""
    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
    tasks.sort(key=lambda x: priority_order.get(x[1], 4))
    print("Tasks sorted by priority successfully.")



tasks = []

while True:
    print("\nTask List Manager")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Sort Tasks by Priority")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        update_task(tasks)
    elif choice == '5':
        sort_tasks(tasks)
    elif choice == '6':
        print("Exiting Task List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

