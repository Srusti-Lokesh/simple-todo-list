"""Browser/IP-address version of the Simple To-Do List."""

from flask import Flask, jsonify, request, render_template_string, redirect, url_for
from todo_core import add_task, get_tasks, get_task, remove_task, update_task

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Simple To-Do List</title>
<style>
body { font-family: Arial, sans-serif; max-width: 900px; margin: 35px auto; padding: 0 20px; background:#f5f7fb; color:#172033; }
.container { background:white; padding:28px; border-radius:14px; box-shadow:0 3px 18px rgba(0,0,0,.08); }
h1 { margin-top:0; }
.menu { display:flex; flex-wrap:wrap; gap:10px; margin:20px 0; }
.menu a, button { border:0; border-radius:7px; padding:10px 16px; cursor:pointer; text-decoration:none; background:#173f8f; color:white; }
.menu .exit { background:#777; }
.card { border:1px solid #ddd; border-radius:10px; padding:18px; margin-top:18px; }
input[type=text] { padding:10px; width:65%; max-width:520px; border:1px solid #bbb; border-radius:6px; }
.task { display:flex; align-items:center; gap:12px; padding:12px 0; border-bottom:1px solid #eee; }
.done { text-decoration:line-through; color:#777; }
.actions { margin-left:auto; display:flex; gap:6px; }
.small { color:#666; }
.success { padding:10px; background:#eef8ee; border-radius:7px; }
</style>
</head>
<body>
<div class="container">
<h1>Simple To-Do List</h1>
<p class="small">IP-address browser version — CRUD menu</p>

<div class="menu">
<a href="/">1. Add Task</a>
<a href="/view">2. View Tasks</a>
<a href="/update">3. Update Task</a>
<a href="/remove">4. Remove Task</a>
<a class="exit" href="/exit">5. Exit</a>
</div>

{% if page == "add" %}
<div class="card">
<h2>Add Task</h2>
<form method="post" action="/tasks">
<input type="text" name="title" placeholder="Enter task title" maxlength="200" required>
<button type="submit">Add Task</button>
</form>
</div>
{% elif page == "view" %}
<div class="card">
<h2>View Tasks</h2>
{% if tasks %}
{% for task in tasks %}
<div class="task">
<span class="{{ 'done' if task.completed else '' }}">
<strong>#{{ task.id }}</strong> — {{ task.title }}
</span>
<span class="small">[{{ "Done" if task.completed else "Pending" }}]</span>
</div>
{% endfor %}
{% else %}
<p>No tasks found.</p>
{% endif %}
</div>
{% elif page == "update" %}
<div class="card">
<h2>Update Task</h2>
{% if tasks %}
{% for task in tasks %}
<form method="post" action="/tasks/{{ task.id }}/update" style="margin:12px 0;">
<strong>#{{ task.id }}</strong>
<input type="text" name="title" value="{{ task.title }}" maxlength="200" required>
<label>
<input type="checkbox" name="completed" {% if task.completed %}checked{% endif %}>
Completed
</label>
<button type="submit">Update</button>
</form>
{% endfor %}
{% else %}
<p>No tasks to update.</p>
{% endif %}
</div>
{% elif page == "remove" %}
<div class="card">
<h2>Remove Task</h2>
{% if tasks %}
{% for task in tasks %}
<div class="task">
<span><strong>#{{ task.id }}</strong> — {{ task.title }}</span>
<form method="post" action="/tasks/{{ task.id }}/delete" class="actions">
<button type="submit">Remove</button>
</form>
</div>
{% endfor %}
{% else %}
<p>No tasks to remove.</p>
{% endif %}
</div>
{% elif page == "exit" %}
<div class="card">
<h2>Goodbye!</h2>
<p class="success">You selected <strong>5. Exit</strong>. The application session is finished.</p>
<p>The server remains available so you can return to the application using the IP address.</p>
</div>
{% endif %}

<div class="card">
<p><a href="/api/tasks">JSON API</a> &nbsp; | &nbsp; <a href="/health">Health Check</a></p>
</div>
</div>
</body>
</html>
"""

def render_page(page):
    return render_template_string(PAGE, page=page, tasks=get_tasks())

@app.get("/")
def home():
    return render_page("add")

@app.get("/view")
def view_tasks():
    return render_page("view")

@app.get("/update")
def update_page():
    return render_page("update")

@app.get("/remove")
def remove_page():
    return render_page("remove")

@app.get("/exit")
def exit_page():
    return render_page("exit")

@app.post("/tasks")
def create_task():
    try:
        add_task(request.form.get("title", ""))
    except ValueError:
        pass
    return redirect(url_for("view_tasks"))

@app.post("/tasks/<int:task_id>/update")
def update_task_page(task_id):
    if get_task(task_id) is not None:
        try:
            update_task(
                task_id,
                title=request.form.get("title"),
                completed=request.form.get("completed") == "on"
            )
        except ValueError:
            pass
    return redirect(url_for("view_tasks"))

@app.post("/tasks/<int:task_id>/delete")
def delete_task_page(task_id):
    remove_task(task_id)
    return redirect(url_for("view_tasks"))

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/tasks")
def api_tasks():
    return jsonify(get_tasks())

@app.post("/api/tasks")
def api_create():
    data = request.get_json(silent=True) or {}
    try:
        task = add_task(str(data.get("title", "")))
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify(task), 201

@app.patch("/api/tasks/<int:task_id>")
def api_update(task_id):
    if get_task(task_id) is None:
        return jsonify({"error": "Task not found."}), 404
    data = request.get_json(silent=True) or {}
    try:
        task = update_task(task_id, title=data.get("title"), completed=data.get("completed"))
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify(task)

@app.delete("/api/tasks/<int:task_id>")
def api_delete(task_id):
    removed = remove_task(task_id)
    if removed is None:
        return jsonify({"error": "Task not found."}), 404
    return jsonify(removed)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
