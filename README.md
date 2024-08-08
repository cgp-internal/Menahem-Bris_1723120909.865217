Expense Management Application
=============================

Overview
--------

This is an expense management application built with Flask. It allows users to track their expenses and income.

How to Run
----------

### Installation

1. Install dependencies: `pip install -r requirements.txt`

### Running the Application

1. Run the application: `python app.py`
2. Open a web browser and navigate to `http://localhost:5000`

Features
--------

* User authentication and authorization
* Expense tracking with categorization and tagging
* Income tracking with categorization and tagging
* Dashboard to view overall financial status

Documentation
-------------

### Models

The application uses the following models:

* `User` (from `models/user.py`)
* `Expense` (from `models/expense.py`)
* `Income` (from `models/income.py`)

### Forms

The application uses the following forms:

* `ExpenseForm` (from `forms/expense_form.py`)
* `IncomeForm` (from `forms/income_form.py`)

### Routes

The application uses the following routes:

* `dashboard` (from `routes/dashboard.py`)
* `expenses` (from `routes/expenses.py`)
* `income` (from `routes/income.py`)
* `login`, `register`, and `logout` (from `routes/auth.py`)

### Templates

The application uses the following templates:

* `base` (from `templates/base.html`)
* `dashboard_template` (from `templates/dashboard.html`)
* `expenses_template` (from `templates/expenses.html`)
* `income_template` (from `templates/income.html`)

Note: This README file provides a basic overview of the application. For more information, please refer to the individual files and modules.