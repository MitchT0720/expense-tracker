import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return
