import database
from datetime import datetime


def add_expense(amount, is_income):
    db = database.get_db()
    cursor = db.cursor()
    date = datetime.utcnow()

    if is_income == 1:
        value = amount
    else:
        value = -amount
    cursor.execute('INSERT INTO transactions (amount, date) VALUES (?, ?)', (value, date))
    db.commit()


def get_balance():
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute('SELECT SUM(amount) FROM transactions')
    # or 0 : returns 0 if the result of the query is 0
    balance = cursor.fetchone()[0] or 0
    db.close()
    return str(balance)


def get_expenses():
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute('SELECT SUM(amount) FROM transactions WHERE amount < 0')
    expenses = cursor.fetchone()[0] or 0
    db.close()
    return str(expenses)


def get_incomes():
    db = database.get_db()
    cursor = db.cursor()
    cursor.execute('SELECT SUM(amount) FROM transactions WHERE amount > 0')
    incomes = cursor.fetchone()[0] or 0
    db.close()
    return str(incomes)

# similar functions for incomes table
