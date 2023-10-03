tasks = []
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(tasks)

def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def complete_task():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice : ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
