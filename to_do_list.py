tasks = []
def to_do():

    while True:
        print("1-Add task")
        print("2-View tasks")
        print("3-Delete tasks")
        print("4-Exit")

        choice = input("Enter choice:")

        if choice == "1":
            while True:
                task = input("Enter task (or 'done' to stop):")
                if task == "done":
                    break
                tasks.append(task)

        elif choice == "2":
            print(f"You have {len(tasks)} tasks")
            if len(tasks) == "0":
                print("No tasks yet")
            else:                     
                for number, task in enumerate(tasks,1):
                    print(f"{number}.{task}")
                    
                    

        elif choice == "3":
            number = int(input("Which task do you want to delete:"))
            index = number - 1
            task = tasks[index]
            ask2 = input("Are you sure? yes/no:")
            if ask2 == "yes":
                tasks.remove(task)
                print("Sucessfully deleted")
            else:
                print("Cancelled")


        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid option")

to_do()
