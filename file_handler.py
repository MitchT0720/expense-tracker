import json

# --------------- For main.py ---------------
# def load_expenses():
#     try:
#         with open("expenses.json", "r") as file:
#             return json.load(file)

#     except (FileNotFoundError, json.JSONDecodeError):
#         return

# def save_expenses(expenses):
#     with open("expenses.json", "w") as file:
#         json.dump(expenses, file)



# --------------- For gui.py ---------------
FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)