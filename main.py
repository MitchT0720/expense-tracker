from file_handler import load_expenses
from expense_manager import(
    add_expense,
    view_expenses,
    total_expense
)

expenses = load_expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total_expense(expenses)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")