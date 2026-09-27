"""Core CRUD operations for the Simple To-Do List project."""

tasks = []
_next_id = 1


def reset_tasks():
    """Reset the in-memory task list. Useful for tests and demos."""
    global _next_id
    tasks.clear()
    _next_id = 1


def add_task(title):
    """Create and return a new task."""
    global _next_id
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    task = {"id": _next_id, "title": title, "completed": False}
    tasks.append(task)
    _next_id += 1
    return task.copy()


def get_tasks():
    """Return a copy of all tasks."""
    return [task.copy() for task in tasks]


def get_task(task_id):
    """Return one task or None if it does not exist."""
    return next((task for task in tasks if task["id"] == task_id), None)


def update_task(task_id, title=None, completed=None):
    """Update a task and return the updated task, or None if missing."""
    task = get_task(task_id)
    if task is None:
        return None

    if title is not None:
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        task["title"] = title

    if completed is not None:
        task["completed"] = bool(completed)

    return task.copy()


def remove_task(task_id):
    """Remove and return a task, or None if missing."""
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index).copy()
    return None
