expenses = []
editing_index = None

def add_expense(title, amount, category):
    if not title:
        return "Title required"
    
    try:
        amount = float(amount)
    except ValueError:
        return "Amount must be a number"
    
    if amount <= 0:
        return "Amount must be greater than 0"
    
    if not category:
        return "Please select a category"

    expenses.append({
        "title": title,
        "amount": float(amount),
        "category": category
    })

    return None

def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)

def update_expense(index, title, amount, category):
    if 0 <= index < len(expenses):
        expenses[index] = {
            "title": title,
            "amount": float(amount),
            "category": category
        }

def total_expenses():
    return sum(e["amount"] for e in expenses)

def total_count():
    return len(expenses)

def category_totals():
    totals = {}

    for e in expenses:
        category = e["category"]

        if category not in totals:
            totals[category] = 0

        totals[category] += e["amount"]

    return totals