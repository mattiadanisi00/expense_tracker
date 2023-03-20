from flask import render_template, url_for, request
from app_factory import create_app
import database_logic as db

app = create_app()


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/transaction')
def transaction():
    amount = float(request.form.get('amount'))
    is_income = int(request.form.get('is_income'))
    db.add_expense(amount, is_income)
    return db.get_balance()


@app.post('/balance')
def get_balance():
    return db.get_balance()


@app.post('/incomes')
def get_incomes():
    return db.get_incomes()


@app.post('/expenses')
def get_expenses():
    return db.get_expenses()


if __name__ == '__main__':
    app.run(debug=True)
    #  host='13.50.13.62'
