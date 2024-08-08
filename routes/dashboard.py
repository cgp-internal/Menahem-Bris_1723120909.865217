from flask import Blueprint, render_template
from models.expense import Expense
from models.income import Income

dashboard_blueprint = Blueprint('dashboard', __name__)

def get_all_expenses():
    return Expense.query.all()

def get_all_incomes():
    return Income.query.all()

def dashboard():
    expenses = get_all_expenses()
    incomes = get_all_incomes()
    return render_template('dashboard.html', expenses=expenses, incomes=incomes)

dashboard_blueprint.add_url_rule('/dashboard', view_func=dashboard)

def get_dashboard():
    return dashboard_blueprint