from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.environ.get("DATA_FILE", "expenses.json")


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


@app.route("/")
def home():
    return jsonify({"message": "Smart Expense Tracker API Running"})


# ---------------- POST ----------------

@app.route("/expenses", methods=["POST"])
def add_expense():

    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    required = ["title", "amount", "category", "date"]

    for field in required:
        if field not in data:
            return jsonify({"message": f"{field} is required"}), 400

    expenses = load_expenses()

    new_id = max([e["id"] for e in expenses], default=0) + 1

    new_expense = {
        "id": new_id,
        "title": data["title"],
        "amount": float(data["amount"]),
        "category": data["category"],
        "date": data["date"]
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    return jsonify(new_expense), 201


# ---------------- GET ALL ----------------

@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify(load_expenses()), 200


# ---------------- GET ONE ----------------

@app.route("/expenses/<int:id>", methods=["GET"])
def get_expense(id):

    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == id:
            return jsonify(expense), 200

    return jsonify({"message": "Expense not found"}), 404


# ---------------- UPDATE ----------------

@app.route("/expenses/<int:id>", methods=["PUT"])
def update_expense(id):

    data = request.get_json()

    expenses = load_expenses()

    for expense in expenses:

        if expense["id"] == id:

            expense["title"] = data.get("title", expense["title"])

            if "amount" in data:
                expense["amount"] = float(data["amount"])

            expense["category"] = data.get("category", expense["category"])
            expense["date"] = data.get("date", expense["date"])

            save_expenses(expenses)

            return jsonify(expense), 200

    return jsonify({"message": "Expense not found"}), 404


# ---------------- DELETE ----------------

@app.route("/expenses/<int:id>", methods=["DELETE"])
def delete_expense(id):

    expenses = load_expenses()

    for expense in expenses:

        if expense["id"] == id:

            expenses.remove(expense)

            save_expenses(expenses)

            return jsonify({
                "message": "Expense deleted successfully"
            }), 200

    return jsonify({
        "message": "Expense not found"
    }), 404

@app.route("/expenses", methods=["DELETE"])
def delete_all():

    save_expenses([])

    return jsonify({
        "message": "All expenses deleted successfully"
    }), 200

# ---------------- CATEGORY ----------------

@app.route("/expenses/category/<category>", methods=["GET"])
def category_expenses(category):

    expenses = load_expenses()

    filtered = [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return jsonify(filtered), 200


# ---------------- TOTAL ----------------

@app.route("/expenses/total", methods=["GET"])
def total_expenses():

    expenses = load_expenses()

    total = sum(float(expense["amount"])for expense in expenses)

    return jsonify({
        "total_expenses": len(expenses),
        "total_amount": total
    }), 200


# ---------------- TOTAL BY CATEGORY ----------------

@app.route("/expenses/total/<category>", methods=["GET"])
def total_by_category(category):

    expenses = load_expenses()

    total = sum(
       float(expense["amount"])
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    return jsonify({
        "category": category,
        "total_amount": total
    }), 200

@app.route("/expenses/summary", methods=["GET"])
def expense_summary():

    expenses = load_expenses()

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        summary[category] = summary.get(category, 0) + amount

    return jsonify(summary), 200

if __name__ == "__main__":
    app.run(debug=True)