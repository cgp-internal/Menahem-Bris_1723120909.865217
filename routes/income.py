from flask import Blueprint, render_template, request, redirect, url_for
from models.income import Income
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

income_blueprint = Blueprint('income', __name__)

@income_blueprint.route('/income', methods=['GET', 'POST'])
def income():
    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        date = request.form['date']
        new_income = Income(user_id=1, amount=amount, description=description, date=date)
        db.session.add(new_income)
        db.session.commit()
        return redirect(url_for('income.income'))
    return render_template('income.html')

def get_income_route():
    return income

income = get_income_route()