id=1
my_tasks={}
def AddTask(n):
    global my_tasks
    global id
    for t in range(n):
        task=input("Enter the task : ")
        my_tasks[id]={"tasks":task,"status":False}
        id+=1
def ShowTasks():
    for todo in my_tasks:
        print(f"{todo} {my_tasks[todo]["tasks"]} - {"Done" if my_tasks[todo]["status"]else "Incomplete"}")
def Update(task_id):
    task=my_tasks.get(task_id,"Tasks not found")
    task['status']=not task['status']
    ShowTasks()
def DeleteTask(task_id):
    try:
        my_tasks.pop(task_id)
    except KeyError:
        print("Tasks not found")
    except Exception:
        print("Error")
while True:
    print("ToDo Project")
    print("1.Add Task\n2.Update Task\n3.Show Tasks\n4.Delete Tasks")
    choice=int(input("Enter your choice : "))
    if choice==1:
        task_count=int(input("How many tasks do you wish to add : "))
        AddTask(task_count)
    elif choice==2:
        task_id=int(input("Enter the task id to be updated : "))
        Update(task_id)
    elif choice==3:
        ShowTasks()
    elif choice==4:
        task_id = int(input("Enter the task id to be deleted : "))
        DeleteTask(task_id)