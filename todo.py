# ==========================================
# DECODELABS PROJECT 1 - SMART TO DO LIST
# Developed by: Ravi Gupta
# ==========================================

# List to store all tasks
tasks = []


# Function to add a new task
def add_task():
    print("\n----- ADD TASK -----")

    task_name = input("Enter Task Name: ")

    # Dictionary representing one task
    task = {
        "task": task_name,
        "status": "Pending"
    }

    tasks.append(task)

    print("✅ Task Added Successfully!")


# Function to view all tasks
def view_tasks():
    print("\n----- YOUR TASKS -----")

    if len(tasks) == 0:
        print("No Tasks Available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']} --> {task['status']}")


# Function to mark a task as completed
def complete_task():
    print("\n----- COMPLETE TASK -----")

    if len(tasks) == 0:
        print("No Tasks Available.")
        return

    view_tasks()

    try:
        task_number = int(
            input("Enter Task Number to Complete: ")
        )

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Completed"
            print("✅ Task Marked as Completed!")
        else:
            print("❌ Invalid Task Number")

    except ValueError:
        print("❌ Please Enter a Valid Number")


# Function to delete a task
def delete_task():
    print("\n----- DELETE TASK -----")

    if len(tasks) == 0:
        print("No Tasks Available.")
        return

    view_tasks()

    try:
        task_number = int(
            input("Enter Task Number to Delete: ")
        )

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)

            print(
                f"✅ Deleted Task: {removed_task['task']}"
            )

        else:
            print("❌ Invalid Task Number")

    except ValueError:
        print("❌ Please Enter a Valid Number")


# Main Program Loop
while True:

    print("\n")
    print("=" * 45)
    print("         SMART TO DO LIST")
    print("=" * 45)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter Your Choice: ")
    print("you entered:",choice)

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank You For Using Smart To Do List!")
        print("Project Closed Successfully.")
        break

    else:
        print("❌ Invalid Choice. Please Try Again.")