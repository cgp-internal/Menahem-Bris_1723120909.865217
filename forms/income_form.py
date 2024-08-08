from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateTimeField
from wtforms.validators import DataRequired
from .models.income import Income

IncomeForm = FlaskForm

class IncomeForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    date = DateTimeField('Date', validators=[DataRequired()])

    def populate_obj(self, income):
        super().populate_obj(income)
        income.amount = income.amount if income.amount else 0.0