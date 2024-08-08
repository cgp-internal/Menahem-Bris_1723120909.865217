from flask import Blueprint, render_template, request, redirect, url_for
from models.expense import Expense
from flask_login import login_required, current_user
from database import db

expenses = Blueprint('expenses', __name__)

@expenses.route('/expenses', methods=['GET', 'POST'])
@login_required
def expenses_route():
    if request.method == 'GET':
        user_expenses = Expense.query.filter_by(user_id=current_user.id).all()
        return render_template('expenses.html', expenses=user_expenses)
    elif request.method == 'POST':
        title = request.form['title']
        amount = request.form['amount']
        new_expense = Expense(title=title, amount=amount, user_id=current_user.id)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('expenses.expenses_route'))