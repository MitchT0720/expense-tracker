import datetime
from models import db, Expense

SEED_DATA = [
    ("Monthly rail pass", 89.00, "Transport", datetime.date(2026, 4, 1)),
    ("Electricity bill", 72.40, "Bills", datetime.date(2026, 4, 3)),
    ("Tesco grocery run", 38.20, "Food", datetime.date(2026, 4, 7)),
    ("Amazon purchase", 24.99, "Shopping", datetime.date(2026, 4, 12)),
    ("Cinema tickets", 18.00, "Entertainment", datetime.date(2026, 4, 15)),
    ("Coffee and pastry", 6.50, "Food", datetime.date(2026, 4, 20)),
    ("Bus fare", 3.20, "Transport", datetime.date(2026, 4, 25)),
    ("Monthly rail pass", 89.00, "Transport", datetime.date(2026, 5, 1)),
    ("Internet bill", 35.00, "Bills", datetime.date(2026, 5, 2)),
    ("Tesco grocery run", 45.60, "Food", datetime.date(2026, 5, 8)),
    ("ASOS order", 52.00, "Shopping", datetime.date(2026, 5, 11)),
    ("Uber to airport", 24.00, "Transport", datetime.date(2026, 5, 14)),
    ("Netflix subscription", 10.99, "Entertainment", datetime.date(2026, 5, 18)),
    ("Lunch at Pret", 9.25, "Food", datetime.date(2026, 5, 22)),
    ("Gas bill", 58.00, "Bills", datetime.date(2026, 5, 28)),
    ("Tesco grocery run", 42.50, "Food", datetime.date(2026, 6, 1)),
    ("Monthly rail pass", 89.00, "Transport", datetime.date(2026, 6, 1)),
    ("Electricity bill", 67.30, "Bills", datetime.date(2026, 6, 3)),
    ("ASOS order", 35.00, "Shopping", datetime.date(2026, 6, 4)),
    ("Lunch at Pret", 8.75, "Food", datetime.date(2026, 6, 5)),
    ("Amazon purchase", 19.99, "Shopping", datetime.date(2026, 6, 7)),
    ("Cinema tickets", 22.00, "Entertainment", datetime.date(2026, 6, 9)),
    ("Coffee and pastry", 6.50, "Food", datetime.date(2026, 6, 10)),
    ("Bus fare", 3.20, "Transport", datetime.date(2026, 6, 11)),
]

def seed():
    count = db.session.execute(db.select(Expense)).scalars().all()
    if len(count) == 0:
        for title, amount, category, date in SEED_DATA:
            db.session.add(Expense(title=title, amount=amount, category=category, date=date))
        db.session.commit()
        print(f"Seeded {len(SEED_DATA)} expenses.")
    else:
        print("Database already has data, skipping seed.")