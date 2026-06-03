from file_handler import save_expenses
import datetime

today = datetime.date.today()

def add_expense(expenses):
    category = input("Enter category: ")
    date = today

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid input: numbers only")
        return

    if amount <= 0:
        print("Amount must be greater than 0")
        return

    expense = {
        "category": category,
        "amount": amount,
        "date": str(date)
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense addded!")

def view_expenses(expenses):
    if not expenses:
        print("No data")

    totals = {}
        
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    for category in totals:
        print(f"{category}: £{totals[category]}")

def total_expense(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spent: £{total}")