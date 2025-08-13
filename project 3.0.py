my_tasks = {}
task_id_counter = 1
def AddTask(n):
    global task_id_counter
    for _ in range(n):
        task = input("Enter the task: ")
        my_tasks[task_id_counter] = {"task": task, "status": False}
        task_id_counter += 1
    print("Tasks added successfully!\n")
def UpdateTask(task_id):
    if task_id in my_tasks:
        new_task = input("Enter the new task name: ")
        my_tasks[task_id]["task"] = new_task
        # Option to mark as done
        mark = input("Mark this task as done? (y/n): ").strip().lower()
        if mark == "y":
            my_tasks[task_id]["status"] = True
            print("Task updated and marked as done!\n")
        else:
            print("Task updated without marking as done.\n")
    else:
        print("Task ID not found!\n")
def ShowTasks():
    if not my_tasks:
        print("No tasks available.\n")
        return
    print("\nYour ToDo List:")
    for tid in sorted(my_tasks):
        status = "Done" if my_tasks[tid]["status"] else "Not done"
        print(f"{tid}. {my_tasks[tid]['task']} - {status}")
    print()
def RemoveTask(task_id):
    if task_id in my_tasks:
        del my_tasks[task_id]
        print("Task removed successfully!\n")
    else:
        print("Task ID not found!\n")
while True:
    print("==== ToDo Tasks ====")
    print("1. Add Task")
    print("2. Update Task (with option to mark done)")
    print("3. Show Tasks")
    print("4. Remove Task")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue
    if choice == 1:
        try:
            task_count = int(input("Enter task count: "))
            AddTask(task_count)
        except ValueError:
            print("Invalid number!\n")
    elif choice == 2:
        ShowTasks()
        try:
            tid = int(input("Enter task ID to update: "))
            UpdateTask(tid)
        except ValueError:
            print("Invalid number!\n")
    elif choice == 3:
        ShowTasks()
    elif choice == 4:
        ShowTasks()
        try:
            tid = int(input("Enter task ID to remove: "))
            RemoveTask(tid)
        except ValueError:
            print("Invalid number!\n")
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")