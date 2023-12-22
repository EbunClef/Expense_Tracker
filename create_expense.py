from expense import Expense
from expense_db import ExpenseDatabase
import json

if __name__ == "__main__":
       
    titles = ["Groceries", "Household", "School Fees"]
    amounts = [15000.00, 250000.00, 750000.00]
    
    db = ExpenseDatabase()

    for title, amount in zip(titles, amounts):
        expense = Expense(title=title, amount=amount)
        db.add_expense(expense)

    initial_state = db.to_dict()

    # Save the initial state to a file
    with open("initial_state.json", "w") as file:
        json.dump(initial_state, file, indent=2)

    print("Initial state:", initial_state)
