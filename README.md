# Employee Performance Dashboard

A FastHTML dashboard for monitoring employee performance and
predicting recruitment risk using a machine learning model.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Environment Setup](#environment-setup)
4. [Install Dependencies](#install-dependencies)
5. [Run the Tests](#run-the-tests)
6. [Start the Dashboard](#start-the-dashboard)
7. [Dashboard Features](#dashboard-features)
8. [Python Package API](#python-package-api)
9. [CI/CD Pipeline](#cicd-pipeline)

---

## Project Overview

This project consists of two main components:

- **`employee_events` Python package** – provides SQL query classes
  for accessing the `employee_events.db` SQLite database
- **FastHTML Dashboard** – a web dashboard that visualises employee
  performance and displays ML-based recruitment risk scores

---

## Project Structure
dsnd-dashboard-project/
├── assets/
│   ├── model.pkl                  # Trained ML recruitment-risk model
│   └── report.css                 # Dashboard CSS styling
├── python-package/
│   ├── employee_events/
│   │   ├── init.py            # Package public API
│   │   ├── employee.py            # Employee-specific SQL queries
│   │   ├── employee_events.db     # SQLite database
│   │   ├── query_base.py          # Shared SQL queries (base class)
│   │   ├── sql_execution.py       # QueryMixin: DB connection handling
│   │   └── team.py                # Team-specific SQL queries
│   ├── requirements.txt
│   └── setup.py
├── report/
│   ├── base_components/           # Reusable HTML base components
│   │   ├── base_component.py
│   │   ├── data_table.py
│   │   ├── dropdown.py
│   │   ├── matplotlib_viz.py
│   │   └── radio.py
│   ├── combined_components/       # Page layout components
│   │   ├── combined_component.py
│   │   └── form_group.py
│   ├── dashboard.py               # FastHTML app and route definitions
│   └── utils.py                   # load_model() and path variables
├── tests/
│   └── test_employee_events.py    # pytest test suite
├── requirements.txt               # Project dependencies
└── README.md

---

## Environment Setup

### Prerequisites

- Python 3.10 or higher
- pip (comes with Python)
- Git

### Option A: GitHub Codespaces (recommended, no local install needed)

1. Go to the repository on GitHub
2. Click the green **`<> Code`** button
3. Select **Codespaces** → **Create codespace on main**
4. A browser-based VS Code opens with a terminal — continue with
   [Install Dependencies](#install-dependencies) below

### Option B: Clone locally

```bash
git clone https://github.com/Alexlab2525/dsnd-dashboard-project.git
cd dsnd-dashboard-project
