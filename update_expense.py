from expense import Expense
from expense_db import ExpenseDatabase
import json

if __name__ == "__main__":
    db = ExpenseDatabase()

    # Retrieve the initial state from the file
    with open("initial_state.json", "r") as file:
        initial_state = json.load(file)

    # Add the initial state to the database
    for expense_data in initial_state:
        expense = Expense(title=expense_data['title'], amount=expense_data['amount'])
        db.add_expense(expense)

    # Print the initial state of the database
    print("Initial state:", db.to_dict())

    # Update an existing expense
    updated_title = "Beverages"
    updated_amount = 60000.0
    expense1 = db.get_expenses_by_title("Groceries")
    if expense1:
        expense1.update(title=updated_title, amount=updated_amount)

    # Print the updated state of the database
    updated_state = db.to_dict()
    print("After updating:", updated_state)

    # Save the updated state to a file with indentation
    with open("updated_state.json", "w") as file:
        json.dump(updated_state, file, indent=2)
