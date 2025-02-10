tasks = []

def add_task(description):
    task = {"description": description, "status": "Pending"}
    tasks.append(task)
    print(f'Task "{description}" added!')

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = task["status"]
            print(f"{index}. {task['description']} - {status}")

def mark_task_completed(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "Completed"
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed["description"]}" deleted.')
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task Completed\n4. Delete Task\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        add_task(description)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_num = int(input("Enter task number to mark completed: "))
        mark_task_completed(task_num)
    elif choice == "4":
        task_num = int(input("Enter task number to delete: "))
        delete_task(task_num)
    elif choice == "5":
        break
    else:
        print("Invalid option, try again.")
