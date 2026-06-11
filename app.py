from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from models import db, Expense
import datetime
from collections import defaultdict
import openpyxl
import io
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your-secret-key" # for Flask session and flash messages

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html", **get_template_data())

def get_template_data():
    expenses = Expense.query.all()
    categories = {}
    for e in expenses:
        categories[e.category] = categories.get(e.category, 0) + e.amount

    monthly = defaultdict(float)
    for e in expenses:
        month = e.date.strftime("%Y-%m")
        monthly[month] += e.amount
    monthly = dict(sorted(monthly.items()))

    return {
        "expenses": expenses,
        "total": sum(e.amount for e in expenses),
        "count": len(expenses),
        "categories": categories,
        "monthly": monthly,
        "today": datetime.date.today()
    }

def validate_expense(title, amount, category, date):
    if not title:
        return "Title required"
    if not amount:
        return "Amount required"
    try:
        float(amount)
    except ValueError:
        return " Amount must be a number"
    if float(amount) <= 0:
        return "Amount must be greater than 0"
    if "." in amount:
        decimal_part = amount.split(".")[1]
        if len(decimal_part) > 2:
            return "Amount can only have up to 2 decimal places"
    if not date:
        return "Date required"
    if not category:
        return "Please select a category"
    return None

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"].strip()
    amount = request.form["amount"]
    category = request.form["category"]
    date = request.form["date"]

    error = validate_expense(title, amount, category, date)
    if error:
        return render_template("index.html", **get_template_data(), error=error, form={"title": title, "amount": amount, "category": category, "date": date})

    db.session.add(Expense(title=title, amount=float(amount), category=category, date=datetime.date.today()))
    db.session.commit()
    flash("Expense added successfully", "success")
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash("Expense deleted", "danger")
    return redirect(url_for("index"))

@app.route("/edit/<int:id>")
def edit_page(id):
    expense = Expense.query.get_or_404(id)
    return render_template("edit.html", expense=expense)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    expense = Expense.query.get_or_404(id)
    title = request.form["title"].strip()
    amount = request.form["amount"]
    category = request.form["category"]
    date = request.form["date"]

    error = validate_expense(title, amount, category, date)
    if error:
        return render_template("edit.html", expense=expense, error=error)

    expense.title = title
    expense.amount = float(amount)
    expense.category = category
    expense.date = datetime.date.fromisoformat(date)
    db.session.commit()
    flash("Expense updated successfully", "success")
    return redirect(url_for("index"))

@app.route("/export")
def export():
    expenses = Expense.query.all()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Expenses"

    ws.append(["Title", "Category", "Amount", "Date"])

    for e in expenses:
        ws.append([e.title, e.category, e.amount, str(e.date)])

    file = io.BytesIO()
    wb.save(file)
    file.seek(0)

    return send_file(
        file,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="expenses.xlsx"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)