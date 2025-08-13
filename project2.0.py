id = 1
my_tasks = {}
def AddTask(n):
    global id
    for _ in range(n):
        task = input("Enter the task: ")
        my_tasks[id] = {"task": task, "status": False}
        id += 1
    print(" Tasks added successfully!\n")
def UpdateTask(task_id):
    if task_id in my_tasks:
        new_task = input("Enter the new task name: ")
        my_tasks[task_id]["task"] = new_task
        print(" Task updated successfully!\n")
    else:
        print(" Task ID not found!\n")
def MarkDone(task_id):
    if task_id in my_tasks:
        my_tasks[task_id]["status"] = True
        print(" Task marked as done!\n")
    else:
        print(" Task ID not found!\n")
def ShowTasks():
    if not my_tasks:
        print("No tasks available.\n")
        return
    print("\n Your ToDo List:")
    for todo_id in my_tasks:
        status = " done" if my_tasks[todo_id]["status"] else " not done"
        print(f"{todo_id}. {my_tasks[todo_id]['task']} - {status}")
    print()
def RemoveTask(task_id):
    if task_id in my_tasks:
        del my_tasks[task_id]
        print(" Task removed successfully!\n")
    else:
        print("Task ID not found!\n")
while True:
    print("==== ToDo Tasks ====")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Show Tasks")
    print("4. Remove Task")
    print("5. Mark Task as Done")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task_count = int(input("Enter task count: "))
        AddTask(task_count)
    elif choice == 2:
        ShowTasks()
        tid = int(input("Enter task ID to update: "))
        UpdateTask(tid)
    elif choice == 3:
        ShowTasks()
    elif choice == 4:
        ShowTasks()
        tid = int(input("Enter task ID to remove: "))
        RemoveTask(tid)
    elif choice == 5:
        ShowTasks()
        tid = int(input("Enter task ID to mark as done: "))
        MarkDone(tid)
    elif choice == 6:
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice! Please try again.\n")