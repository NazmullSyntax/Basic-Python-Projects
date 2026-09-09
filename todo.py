tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == '2':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        num = int(input("Task number to delete: "))
        tasks.pop(num-1)
    elif choice == '4':
        break