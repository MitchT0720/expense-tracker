import datetime
from models import db, Expense

SEED_DATA = [
    Expense(title="Groceries", amount=45.50, category="Food", date=datetime.date(2026, 4, 3)),
    Expense(title="Bus pass", amount=30.00, category="Transport", date=datetime.date(2026, 4, 7)),
    Expense(title="Netflix", amount=10.99, category="Entertainment", date=datetime.date(2026, 4, 10)),
    Expense(title="Electricity bill", amount=85.00, category="Bills", date=datetime.date(2026, 4, 15)),
    Expense(title="Lunch", amount=12.50, category="Food", date=datetime.date(2026, 4, 18)),
    Expense(title="Train ticket", amount=22.00, category="Transport", date=datetime.date(2026, 4, 22)),
    Expense(title="New shoes", amount=65.00, category="Shopping", date=datetime.date(2026, 4, 28)),
    Expense(title="Coffee", amount=3.50, category="Food", date=datetime.date(2026, 5, 2)),
    Expense(title="Spotify", amount=9.99, category="Entertainment", date=datetime.date(2026, 5, 5)),
    Expense(title="Internet bill", amount=35.00, category="Bills", date=datetime.date(2026, 5, 8)),
    Expense(title="Dinner out", amount=48.00, category="Food", date=datetime.date(2026, 5, 14)),
    Expense(title="Uber", amount=15.50, category="Transport", date=datetime.date(2026, 5, 19)),
    Expense(title="Amazon order", amount=29.99, category="Shopping", date=datetime.date(2026, 5, 23)),
    Expense(title="Cinema", amount=14.00, category="Entertainment", date=datetime.date(2026, 5, 28)),
    Expense(title="Supermarket", amount=67.30, category="Food", date=datetime.date(2026, 6, 1)),
    Expense(title="Gas bill", amount=55.00, category="Bills", date=datetime.date(2026, 6, 3)),
    Expense(title="Gym wear", amount=40.00, category="Shopping", date=datetime.date(2026, 6, 5)),
]

def seed():
    if Expense.query.first() is None:
        for item in SEED_DATA:
            expense = Expense(**item)
            db.session.add(expense)
        db.session.commit()
        print(f"Seeded {len(SEED_DATA)} expenses.")
    else:
        print("Database already has data, skipping seed.")