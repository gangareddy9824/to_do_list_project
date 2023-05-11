tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)

def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found!")

def print_tasks():
    print("To-Do List:")
    for task in tasks:
        print(task)

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Print tasks")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        print_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
