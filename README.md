# TaskVault 📋

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI-green?style=flat-square)
![Pytest](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square&logo=pytest&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

A lightweight and efficient CLI-based task manager built with Python and SQLite. `TaskVault` helps you track daily tasks, assign priorities, and manage completion status directly from your terminal with persistent local storage.

## Features

- 💾 **Persistent Storage**: All tasks are stored locally in a lightweight SQLite database.
- 🏷️ **Priority Tracking**: Assign priority levels (High, Medium, Low) to keep focused on important items.
- ⚡ **Simple CLI Workflow**: Intuitive terminal commands for adding, listing, completing, and removing tasks.
- 🎨 **Rich Visuals**: Clear and beautifully formatted tables powered by `rich`.

## Tech Stack

- **Python 3.10+**
- **SQLite3** — Embedded relational database for zero-config data persistence.
- **[Rich](https://rich.readthedocs.io/)** — Terminal formatting and tables.
- **[Typer](https://typer.tiangolo.com/)** — CLI framework.
- **[pytest](https://docs.pytest.org/)** — Unit test framework.

## Installation

1. Clone the repository:
   
   git clone [https://github.com/daria999333/taskvault.git](https://github.com/daria999333/taskvault.git)
   cd taskvault
   

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Add a new task:**
  ```bash
  python main.py add "Finish software architecture report" --priority High
  ```

- **List all tasks:**
  ```bash
  python main.py list
  ```

- **Mark task as complete:**
  ```bash
  python main.py done 1
  ```

- **Delete a task:**
  ```bash
  python main.py remove 1
  ```
