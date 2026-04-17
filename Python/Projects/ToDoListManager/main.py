tasks = []

def add():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view():
    if tasks:
        for i in range(len(tasks)):
            print(f"{i+1} . {tasks[i]}")
    else:
        print("No tasks found !")

def delete():
    if tasks:
        view()
        num = int(input("Enter which task num you want to delete :"))
        if num > len(tasks):
            print("No index found")
        else:
            tasks.pop(num-1)
            print("Tasks Deleted !")
    else:
        print("No tasks found !")

def main():
    while True:
        print("\n-- To-Do List Manager --")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            delete()
        elif choice == "4":
            print("Exited!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()