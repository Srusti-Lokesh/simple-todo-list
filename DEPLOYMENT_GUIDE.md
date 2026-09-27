# Deployment Guide — PowerShell, GitHub and Render

## 1. Prerequisites

Install:

- Python 3.10 or newer
- Git
- A GitHub account
- A Render account

Check Python and Git:

```powershell
py -3 --version
git --version
```

## 2. Extract the ZIP

Extract `simple-todo-list-submission.zip` to a normal folder such as:

```text
C:\Users\YOUR_NAME\Desktop\simple-todo-list
```

Open PowerShell in that folder.

```powershell
cd "C:\Users\YOUR_NAME\Desktop\simple-todo-list"
```

## 3. Create the Python virtual environment

```powershell
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the beginning of the PowerShell prompt.

## 4. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Run tests BEFORE GitHub

```powershell
python -m unittest discover -s . -p "test_*.py" -v
```

Expected result:

```text
Ran 3 tests
OK
```

If this fails, stop and fix the local issue before pushing to GitHub.

## 6. Run the required CLI application

```powershell
python todo_cli.py
```

Test every menu option:

1. Add at least two tasks.
2. View the tasks.
3. Update one task.
4. Mark it completed.
5. Remove another task.
6. Enter an invalid menu option such as `9`.
7. Exit with option `5`.

Take a screenshot of the terminal showing the CRUD flow. This is your sample-execution evidence.

## 7. Optional local Render-style web test

Installations are already complete from `requirements.txt`.

```powershell
python web_app.py
```

Open:

```text
http://127.0.0.1:5000
```

Also verify:

```text
http://127.0.0.1:5000/health
http://127.0.0.1:5000/api/tasks
```

Stop it with `Ctrl+C`.

## 7A. Open the complete application using your IP address

The browser version contains the complete five-option menu:

```text
1. Add Task
2. View Tasks
3. Update Task
4. Remove Task
5. Exit
```

Start it:

```powershell
python web_app.py
```

Find your IPv4 address:

```powershell
ipconfig
```

Look for the active adapter's `IPv4 Address`, for example:

```text
192.168.1.10
```

Open this in your browser:

```text
http://192.168.1.10:5000
```

Replace the example IP with your actual IPv4 address.

The application is bound to `0.0.0.0`, so it can accept connections to the PC's local IP. If Windows Firewall asks whether Python may communicate on the network, allow access on the appropriate private network.

The five browser menu options are:

- **1. Add Task** — create a task.
- **2. View Tasks** — display all tasks.
- **3. Update Task** — edit title and completed status.
- **4. Remove Task** — delete a task.
- **5. Exit** — display the completion/exit page.

The browser Exit option does not terminate the server process. To stop the local server, return to PowerShell and press `Ctrl+C`.

## 8. Create the GitHub repository

On GitHub, create a new repository:

- Repository name: `simple-todo-list`
- Visibility: Public, if the internship requires a public repository
- Do NOT add a second README if this package already contains `README.md`
- Do NOT add an unrelated `.gitignore` if you already have the included one

GitHub's own documentation supports creating a repository and then pushing an existing local repository.

## 9. Push from PowerShell

From the project folder:

```powershell
git init
git add .
git status
git commit -m "Initial commit - Simple To-Do List"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/simple-todo-list.git
git push -u origin main
```

Replace:

```text
YOUR_USERNAME
```

with your actual GitHub username.

If Git asks you to authenticate, complete GitHub's browser/credential flow. Do not put a GitHub password or personal access token inside source code.

## 10. Verify GitHub

Refresh the repository page and check that it contains:

```text
todo_cli.py
todo_core.py
web_app.py
test_todo_core.py
requirements.txt
render.yaml
README.md
DEPLOYMENT_GUIDE.md
SUBMISSION_CHECKLIST.md
LINKEDIN_POST.md
SAMPLE_EXECUTION.txt
REPORT.pdf
LICENSE
.gitignore
```

## 11. Deploy to Render using the included Blueprint

The included `render.yaml` is at the repository root.

On Render:

1. Sign in.
2. Choose `New`.
3. Choose `Blueprint`.
4. Connect GitHub if it is not already connected.
5. Select `simple-todo-list`.
6. Select the `main` branch.
7. Review the service configuration.
8. Deploy the Blueprint.
9. Wait for the service to become live.
10. Open the generated public URL.

The Blueprint is configured for a Python web service.

### Expected Render settings

```text
Runtime: Python
Plan: Free
Build command: pip install -r requirements.txt
Start command: gunicorn web_app:app --bind 0.0.0.0:$PORT --workers 1
Health check: /health
```

The single worker is intentional because the demo uses an in-memory list. Multiple workers could have separate memory states.

## 12. Verify the live Render application

Open:

```text
https://YOUR-SERVICE.onrender.com/
```

Then verify:

```text
https://YOUR-SERVICE.onrender.com/health
https://YOUR-SERVICE.onrender.com/api/tasks
```

For `/health`, expect JSON similar to:

```json
{"status":"ok"}
```

For `/api/tasks`, expect:

```json
[]
```

before any tasks are added.

Then add, update, complete and delete a task from the web UI.

## 13. Important Render data limitation

The project intentionally uses a Python list to satisfy the learning objective. Render's default filesystem is ephemeral and a Free web service can spin down. This version does not claim permanent storage.

For a production version, use a managed database such as PostgreSQL or another durable datastore.

## 14. Rollback evidence

The assignment asks for rollback evidence. This cannot honestly be generated before you have a real Render deployment.

After your first successful deployment:

1. Take a screenshot of the successful deploy.
2. Make a small change to a visible text string.
3. Commit and push it.
4. Wait for Render to deploy the second version.
5. Capture the Deploys history.
6. Use the Render rollback control to return to the previous successful deployment if your assignment specifically requires a rollback action.
7. Capture the rollback result.
8. Keep these screenshots with your final submission.

Do not create fake screenshots or claim a rollback occurred if it did not.

## 15. Final GitHub update after deployment

If you add evidence files, commit them:

```powershell
git add .
git commit -m "Add deployment and submission evidence"
git push
```

Avoid committing secrets, `.env` files, virtual environments, or credentials.

## 16. Final submission checklist

- [ ] CLI runs with `python todo_cli.py`
- [ ] Add works
- [ ] View works
- [ ] Update works
- [ ] Remove works
- [ ] Invalid menu choice is handled
- [ ] Unit tests pass
- [ ] GitHub repository is public if required
- [ ] README is present
- [ ] Render service is live
- [ ] Live URL works
- [ ] Render health check works
- [ ] Sample execution screenshot captured
- [ ] Successful Render deployment screenshot captured
- [ ] Rollback evidence captured after an actual rollback
- [ ] Report PDF included
- [ ] LinkedIn post prepared
- [ ] Repository link copied correctly
- [ ] Render URL copied correctly
- [ ] No secrets or `.venv` folder committed
