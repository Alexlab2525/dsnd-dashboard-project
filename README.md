# Employee Performance Dashboard

A FastHTML dashboard for monitoring employee performance and predicting recruitment risk using a machine learning model.

---

## Project Overview

This project has two components:

- **employee_events Python package** - provides SQL query classes for the SQLite database
- **FastHTML Dashboard** - visualises performance and shows ML-based recruitment risk

---

## Project Structure

    dsnd-dashboard-project/
    ├── assets/
    │   ├── model.pkl              (Trained ML model)
    │   └── report.css             (Dashboard styling)
    ├── python-package/
    │   ├── employee_events/
    │   │   ├── __init__.py
    │   │   ├── employee.py        (Employee SQL queries)
    │   │   ├── employee_events.db (SQLite database)
    │   │   ├── query_base.py      (Shared SQL queries)
    │   │   ├── sql_execution.py   (DB connection mixin)
    │   │   └── team.py            (Team SQL queries)
    │   └── setup.py
    ├── report/
    │   ├── base_components/
    │   ├── combined_components/
    │   ├── dashboard.py           (FastHTML app and routes)
    │   └── utils.py
    ├── tests/
    │   └── test_employee_events.py
    └── requirements.txt

---

## Prerequisites

- Python 3.10 or higher
- pip
- Git

---

## Environment Setup

### Option A: GitHub Codespaces (recommended)

1. Click the green **Code** button on the repository page
2. Select **Codespaces** tab
3. Click **Create codespace on main**
4. A browser-based VS Code opens with a terminal

### Option B: Local Setup

Open a terminal and run:

    git clone https://github.com/Alexlab2525/dsnd-dashboard-project.git
    cd dsnd-dashboard-project

---

## Install Dependencies

Run these two commands in the terminal:

    pip install -r requirements.txt

Then install the Python package:

    pip install -e python-package/

---

## Run the Tests

    pytest tests/ -v

Expected output:

    tests/test_employee_events.py::test_db_exists PASSED
    tests/test_employee_events.py::test_employee_table_exists PASSED
    tests/test_employee_events.py::test_team_table_exists PASSED
    tests/test_employee_events.py::test_employee_events_table_exists PASSED
    4 passed in 0.02s

---

## Start the Dashboard

    cd report
    python dashboard.py

Open your browser at the URL shown in the terminal (e.g. http://localhost:5001 for local setup, or the Codespaces forwarded URL when using GitHub Codespaces).

Codespaces users: click **Open in Browser** when the popup appears.

---

## Dashboard Features

**Employee View** - select an employee to see:
- Predicted recruitment risk score (Low / Medium / High)
- Line chart of positive and negative events over time
- Data table with per-date event counts

**Team View** - select a team to see:
- Average recruitment risk across all team members
- Aggregated line chart of team performance events
- Data table with per-date event counts

---

## CI/CD Pipeline

GitHub Actions automatically runs all tests on every push to main.

Workflow file: .github/workflows/tests.yml

Steps:
1. Checkout repository
2. Setup Python 3.10 and 3.11
3. Install dependencies
4. Install employee_events package
5. Run pytest
