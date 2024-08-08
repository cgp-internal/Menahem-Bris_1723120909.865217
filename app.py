from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from forms.expense_form import ExpenseForm
from forms.income_form import IncomeForm
from routes.dashboard import dashboard
from routes.expenses import expenses
from routes.income import income
from routes.auth import login, register, logout

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/dashboard')
def dashboard_route():
    return dashboard()

@app.route('/expenses')
def expenses_route():
    return expenses()

@app.route('/income')
def income_route():
    return income()

@app.route('/login')
def login_route():
    return login()

@app.route('/register')
def register_route():
    return register()

@app.route('/logout')
def logout_route():
    return logout()

if __name__ == '__main__':
    app.run(debug=True)