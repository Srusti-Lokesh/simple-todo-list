# Simple To-Do List — Python CLI + Render Demo

A beginner-friendly command-line to-do application built in Python. The core project demonstrates **Create, Read, Update, Delete (CRUD)** operations using Python lists, loops, functions, conditionals, and menu-driven input.

The repository also contains a Flask browser interface so the full CRUD menu can be opened through a local IP address and demonstrated through a public Render Web Service. The **CLI remains the primary assignment deliverable**.

## Features

- Add a task
- View all tasks
- Update a task title
- Mark a task as completed/pending
- Remove a task
- Input validation and invalid-menu handling
- Unit tests for core CRUD operations
- Flask web demo with HTML UI and JSON API
- Render Blueprint configuration
- GitHub-ready documentation

## Project structure

```text
simple-todo-list/
├── todo_cli.py             # Main command-line application
├── todo_core.py            # Reusable CRUD logic using a Python list
├── web_app.py              # Flask adapter for Render deployment
├── test_todo_core.py       # Unit tests
├── requirements.txt        # Python dependencies
├── render.yaml             # Render Blueprint configuration
├── Procfile                # Alternative process declaration
├── README.md
├── DEPLOYMENT_GUIDE.md
├── SUBMISSION_CHECKLIST.md
├── LINKEDIN_POST.md
├── SAMPLE_EXECUTION.txt
├── REPORT.pdf
├── LICENSE
└── .gitignore
```

## Technologies

- Python 3.10+
- Flask 3.1.3
- Gunicorn 26.2.0
- Git and GitHub
- Render
- HTML/CSS for the optional web demo
- Python `unittest`

## Run locally on Windows PowerShell

> PowerShell commands are shown exactly as commands you can paste. Replace only values explicitly marked `YOUR_...`.

```powershell
py -3 --version
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s . -p "test_*.py" -v
python todo_cli.py
```

If your PowerShell execution policy does not block activation, the `Set-ExecutionPolicy` line can be skipped.

### Run the browser/IP-address version locally

```powershell
python web_app.py
```

Find your local IPv4 address:

```powershell
ipconfig
```

Then open the browser menu using:

```text
http://YOUR_IPV4_ADDRESS:5000
```

Example:

```text
http://192.168.1.10:5000
```

The browser page now provides:

1. Add Task
2. View Tasks
3. Update Task
4. Remove Task
5. Exit

The Exit option displays a completion page. It does not shut down the Flask server; stop the server with `Ctrl+C` when you are finished.

## CRUD menu

The CLI menu is:

```text
1. Add task
2. View tasks
3. Update task
4. Remove task
5. Exit
```

## GitHub

Create a new empty GitHub repository, then from the project folder:

```powershell
git init
git add .
git commit -m "Initial commit - Simple To-Do List"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/simple-todo-list.git
git push -u origin main
```

Verify that GitHub shows the source files, `render.yaml`, `README.md`, tests, and documentation.

## Render deployment

Render Web Services need an HTTP server listening on `0.0.0.0` and the port provided by the `PORT` environment variable. This repository therefore includes `web_app.py` specifically for deployment demonstration.

### Recommended: Blueprint deployment

1. Push the project to GitHub.
2. Sign in to Render.
3. Choose **New → Blueprint**.
4. Select the GitHub repository.
5. Select the branch containing `render.yaml` (normally `main`).
6. Review the service shown by the Blueprint.
7. Deploy the Blueprint.
8. Open the generated `onrender.com` URL.
9. Verify `/` loads, `/health` returns `{"status":"ok"}`, and `/api/tasks` returns JSON.
10. Take screenshots of the live page and successful deployment logs for your submission evidence.

The Blueprint uses:

```text
Build: pip install -r requirements.txt
Start: gunicorn web_app:app --bind 0.0.0.0:$PORT --workers 1
Health check: /health
```

### Important data note

The demo stores tasks in an in-memory Python list because the assignment is designed to teach lists and CRUD. On Render, in-memory data is not durable: a restart, spin-down, or redeploy can clear it. Do not claim database persistence for this version.

## Rollback evidence

Do not fabricate rollback evidence. After you have a successful Render deployment:

1. Make a small visible change and deploy it.
2. Confirm the new deployment is live.
3. Use Render's Deploys/rollback controls to return to the previous successful deployment if your assignment requires an actual rollback demonstration.
4. Capture a screenshot showing the deployment history and rollback result.
5. Put that screenshot in your submission folder or attach it according to your internship portal instructions.

Render documents instant rollbacks for web services; the exact available rollback history depends on the service plan.

## Interview questions

### Why are lists useful?

Lists store multiple values in an ordered collection and can be changed during program execution. They are a simple way to represent the current set of tasks.

### What does CRUD mean?

CRUD stands for:

- **Create** — add a task
- **Read** — view tasks
- **Update** — edit task information
- **Delete** — remove a task

### Why separate operations into functions?

Separate functions make the program easier to read, test, debug, and reuse. Each function has a focused responsibility.

## Assignment alignment

The project directly covers:

- Working command-line to-do application
- CRUD menu
- Python list storage
- Loops and conditionals
- Separate functions for operations
- Invalid menu handling
- Sample execution
- GitHub-ready repository
- Render deployment configuration
- Submission checklist and report

## License

MIT License. See `LICENSE`.
