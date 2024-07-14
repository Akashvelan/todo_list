def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task(todo_list):
    task = input("\nEnter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to your to-do list.")

def delete_task(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty!")
        return

    view_todo_list(todo_list)
    try:
        task_num = int(input("\nEnter the task number you want to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' has been deleted from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            delete_task(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

if _name_ == "_main_":
    main()
