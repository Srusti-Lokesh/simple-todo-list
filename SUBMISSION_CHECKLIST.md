# Submission Checklist

## Required deliverables from the assignment

- Working command-line to-do application
- Menu with CRUD operations
- Sample execution
- Public GitHub repository
- Deployment configuration
- Rollback evidence
- README.md describing approach and outcome
- Repository link submitted through the internship portal
- Completed project shared on LinkedIn

## Evidence to capture yourself

Because GitHub and Render accounts belong to you, these items must come from your actual accounts:

1. **Terminal screenshot**
   - Add task
   - View task
   - Update task
   - Remove task
   - Invalid choice handling

2. **GitHub screenshot**
   - Repository name
   - File list
   - Public visibility if required

3. **Render screenshot**
   - Successful deployment
   - Live service URL
   - Deploy status

4. **Rollback screenshot**
   - Deploy history
   - Actual rollback action/result

Do not fabricate evidence.

## What to paste into the internship portal

### GitHub repository

```text
https://github.com/YOUR_USERNAME/simple-todo-list
```

### Render URL

```text
https://YOUR-SERVICE.onrender.com
```

Replace both placeholders with the real links from your accounts.

## README outcome summary

The project implements a menu-driven Python to-do list using a list-based data structure and separate CRUD functions. It includes validation, unit tests, and a Flask web adapter configured for Render deployment.

## Final check

Run:

```powershell
python -m unittest discover -s . -p "test_*.py" -v
python todo_cli.py
```

Then confirm the GitHub and Render URLs manually before submitting.
