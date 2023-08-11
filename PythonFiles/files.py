# To-Do List Application

def display_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Your to-do list:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("Your to-do list is empty.")
    except FileNotFoundError:
        print("No to-do list found. Create one by adding tasks.")


def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the to-do list.")


def main():
    print("Welcome to the To-Do List App!")

    while True:
        print("\nChoose an option:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
