from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

from models.expense import Expense

class ExpenseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add Expense')


# Ensure ExpenseForm can be imported individually
ExpenseForm