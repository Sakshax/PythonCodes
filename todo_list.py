tasks = []

def show_menu():
    print("\n📋 To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📌 Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Removed: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Enter a number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice.")
