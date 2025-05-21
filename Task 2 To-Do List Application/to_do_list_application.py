def task():
    tasks=[]
    print("-----to do application-----")
    total_tasks=int(input("Enter task task how many tasks you want to add= "))
    for i in range(1,total_tasks+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today tasks are\n{tasks}") 
    
    while True:
        operation=int(input("Enter 1-Add\n2-Delete\n3-View task"))
        if operation==1:
            add=input("Enter you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added.....")
        
        elif operation==2:
            del_val=input("Which task you want to delete = ")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"Tasks {del_val} has been deleted....")

        elif operation==3:
            print(f"Tasks_view={tasks}")
        else:
            print("Invalid choice")
task()