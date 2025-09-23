# toDoApp.py

# Store tasks in a list
tasks = []


# === Core Functions ===
def add_task(task: str):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added successfully!")


def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task(task_number: int):
    """Remove a task by its number (1-based index)."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task removed: '{removed}'")
    else:
        print("Invalid task number! Please try again.")


# === Helper Functions ===
def print_menu():
    """Display the main menu."""
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")


# === Main Program Loop ===
def main():
    """Main loop for the To-Do App."""
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty!")

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                try:
                    n = int(input("Enter task number to remove: "))
                    confirm = input(f"Are you sure you want to delete task {n}? (y/n): ")
                    if confirm.lower() == "y":
                        remove_task(n)
                    else:
                        print("Deletion cancelled.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-4.")


# Run the program
if __name__ == "__main__":
    main()