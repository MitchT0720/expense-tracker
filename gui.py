import tkinter as tk
from expense_manager import add_expense
from file_handler import load_expenses, save_expenses

# UI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

name_label = tk.Label(root, text="Expense Name")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

category_label = tk.Label(root, text="Category")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack()

amount_label = tk.Label(root, text ="Amount")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

def refresh_listbox():
    expense_listbox.delete(0, tk.END)

    expenses = load_expenses()

    for expense in expenses:
        expense_listbox.insert(
            tk. END,
            f"{expense['name']} - {expense['category']} - £{expense['amount']}"
        )

expense_listbox = tk.Listbox(root, width=50)
expense_listbox.pack()
refresh_listbox()

# Add
def add_expense_gui():
    global editing_index

    name = name_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    expenses = load_expenses()

    if editing_index is not None:
        #UPDATE mode
        expenses[editing_index] ={
            "name": name,
            "category": category,
            "amount": float(amount)
        }
        editing_index = None
    else:
        # ADD mode
        expenses.append({
            "name": name,
            "category": category,
            "amount": float(amount)
        })

    save_expenses(expenses)
    refresh_listbox()

    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

add_button = tk.Button(
    root,
    text="Add Expense",
    command=add_expense_gui
)

add_button.pack()

# Delete
def delete_expense():
    selected = expense_listbox.curselection()

    if not selected:
        return
    
    index = selected[0]
    selected_text = expense_listbox.get(index)

    expenses = load_expenses()

    for expense in expenses:
        formatted = f"{expense['name']} - {expense['category']} - £{expense['amount']}"

        if formatted == selected_text:
            expenses.remove(expense)
            break

    save_expenses(expenses)
    refresh_listbox()

delete_button = tk.Button(
    root,
    text="Delete Selected",
    command=delete_expense
)

delete_button.pack()

# Edit
def edit_expense():
    selected = expense_listbox.curselection()

    if not selected:
        return
    
    index = selected[0]

    global editing_index
    editing_index = index

    expenses = load_expenses()
    expense = expenses[index]

    name_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    name_entry.insert(0, expense["name"])
    category_entry.insert(0, expense["category"])
    amount_entry.insert(0, expense["amount"])

edit_button = tk.Button(
    root,
    text="Edit Selected",
    command=edit_expense
)

edit_button.pack()

root.mainloop()