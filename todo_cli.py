"""Command-line interface for the Simple To-Do List."""

from todo_core import add_task, get_tasks, get_task, remove_task, update_task


def print_tasks():
    tasks = get_tasks()
    print("\n--- To-Do List ---")
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} [{status}]')


def prompt_task_id():
    raw = input("Enter task ID: ").strip()
    try:
        return int(raw)
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return None


def add_task_cli():
    title = input("Enter task title: ").strip()
    try:
        task = add_task(title)
        print(f'Task added: #{task["id"]} - {task["title"]}')
    except ValueError as exc:
        print(f"Error: {exc}")


def update_task_cli():
    print_tasks()
    task_id = prompt_task_id()
    if task_id is None:
        return

    task = get_task(task_id)
    if task is None:
        print("Task not found.")
        return

    new_title = input(f'New title [{task["title"]}]: ').strip()
    status_input = input(
        "Mark as completed? (y = done, n = pending, Enter = keep current): "
    ).strip().lower()

    title = new_title if new_title else None
    completed = None
    if status_input in {"y", "yes"}:
        completed = True
    elif status_input in {"n", "no"}:
        completed = False
    elif status_input:
        print("Invalid status choice. Keeping current status.")

    try:
        updated = update_task(task_id, title=title, completed=completed)
        print(f'Updated task #{updated["id"]}.')
    except ValueError as exc:
        print(f"Error: {exc}")


def remove_task_cli():
    print_tasks()
    task_id = prompt_task_id()
    if task_id is None:
        return

    removed = remove_task(task_id)
    if removed is None:
        print("Task not found.")
    else:
        print(f'Removed task #{removed["id"]}: {removed["title"]}')


def print_menu():
    print(
        """
===========================
      SIMPLE TO-DO LIST
===========================
1. Add task
2. View tasks
3. Update task
4. Remove task
5. Exit
"""
    )


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task_cli()
        elif choice == "2":
            print_tasks()
        elif choice == "3":
            update_task_cli()
        elif choice == "4":
            remove_task_cli()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
