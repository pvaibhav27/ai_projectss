# TO-DO LIST APP

todos = []

def show_menu():
    print("==========================")
    print("      MY TO-DO LIST       ")
    print("==========================")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")
    print("==========================")

def add_task():
    task = input("Enter your task: ")
    todos.append({"task": task, "done": False}) #false - task not done yet
    print(f"✅ '{task}' added!")

def view_tasks():
    if len(todos) == 0:
        print("\n📋 No tasks yet! Add something.")
    else:
        print("\n📋 YOUR TASKS:")
        for i, item in enumerate(todos, 1):
            status = "✅" if item["done"] else "❌"
            print(f"{i}. {status} {item['task']}")

def remove_task():
    view_tasks()
    if len(todos) > 0:
        try:
            num = int(input("\nEnter task number to remove: "))
            if 1 <= num <= len(todos):
                removed = todos.pop(num - 1)
                print(f"🗑️ '{removed['task']}' removed!")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Please enter a number!")

def mark_done():
    view_tasks()
    if len(todos) > 0:
        try:
            num = int(input("\nEnter task number to mark done: "))
            if 1 <= num <= len(todos):
                todos[num - 1]["done"] = True
                print(f"🎉 Task marked as done!")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Please enter a number!")

# Main program
print("Welcome to Your To-Do List App!")

while True: #Tasks keeps running from this
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("\n👋 Goodbye! Stay productive!")
        break
    else:
        print("❌ Invalid choice! Enter 1 to 5.")
