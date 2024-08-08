from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('expenses', lazy=True))

    def __init__(self, title, amount, user_id):
        self.title = title
        self.amount = amount
        self.user_id = user_id

    def __repr__(self):
        return f'Expense({self.id}, {self.title}, {self.amount}, {self.date}, {self.user_id})'

Expense