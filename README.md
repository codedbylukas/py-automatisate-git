# 📝 Git Modification Script – Automated Git Workflow

This script enables you to automatically commit and (optionally) push changes to your project with minimal input.

## 🔧 What Does the Script Do?
- The script performs the following actions:
- Initializes Git (if requested)
- Adds all files (git add .)
- Commits changes with a user-defined message
- Pushes changes to the remote repository (if enabled)

## 🚀 How to Use It?
1. Open a terminal and run the script:
```bash
python main.py
```
2. Ensure you're in the correct directory (or the script will create a new Git repo in the current folder).

## 💡 User Inputs

At startup, the script asks the following:

- Do you want to push after every modification?

(y/n) – Default: y

→ If y, a git push is performed after every commit.

- Do you want to init?

(y/n) – Default: y

→ If y, git init is executed (if no Git repository exists yet).

#### ⚠️ Note: 

The script executes direct Git commands (e.g., git add ., git commit, git push). Be cautious — this is best suited for simple, local workflows.

## 📚 Prerequisites

- Python 3.6+ installed
- Git installed and available in the system PATH
- A working project directory
