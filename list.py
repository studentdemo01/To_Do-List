#  !!!!!!! TO - DO LIST !!!!!!!
list = []
def show_task():
    if len(list) == 0:
        print("There is no task to doo : \n\n")
    else:
        for i , task in enumerate(list):
            print(f'{i+1}.{task["Name"]} | {task["Status"]} | {task["priority"]}\n')

def Add_task():
    Name = input("Enter the task : ")
    priority = input("Enter the priority of task(low/medium/high) : ")
    task =  {
        "Name" : Name,
        "priority" : priority,
        "Status" : "Pending"
    }
    list.append(task)
    print(f' !!!! Task Added !!!!\n\n')

def Delete_task():
    show_task()
    num = int(input("Enter the number of task you want to delete : "))
    
    if 0 < num < len(list):
        
        list.pop(num-1)
        print(f'Task {num} Deleted\n\n')
        
    else:
        print("Invalid Number ")

def Update_status():
    show_task()
    num = int(input("Enter the number of task you want to update the status : "))
    if 0 < num < len(list):
        if list[num - 1]["Status"] == "Pending":
            list[num - 1]["Status"] = "Completed"
            print("Task is Marked as Compeleted\n\n")
        else:
            list[num - 1]["Status"] = "Pending"
            print("Task is Marked as Pending\n\n")
    else:
        print("INVLID TASK NUMBER\n\n")
    



while(True):
    print("For Addind Task  ---->(1)")
    print("For Deleting Task  ---->(2)")
    print("For Update_Status Task  ---->(3)")
    print("For Show_Task  ---->(4)")
    print("For Exit  ---->(5)\n\n")

    choice = int(input("Enter the Opration You want to Do : "))
    if(choice == 1):
        Add_task()

    elif(choice == 2):
        Delete_task()
    
    elif(choice == 3):
        Update_status()

    elif(choice == 4):
        show_task()

    elif(choice == 5):
        print("Good Bye \n\n")
        break

    else:
        print("INVALID CHOICE")

    