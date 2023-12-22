class ExpenseDatabase:
    def __init__(self):
        # Initialize the expenses list
        self.expenses = []
        
    def add_expense(self, expense):
        # Add an expense to the database
        self.expenses.append(expense)
    
    def remove_expense(self, expense_id):
        # Remove an expense from the database by ID
        self.expenses = [e for e in self.expenses if e.id != expense_id]
    
    def get_expense_by_id(self, expense_id):
        # Retrieve an expense by ID
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if the expense is not found

    def get_expenses_by_title(self, title):
        # Retrieve expenses by title (returning a list)
        for expense in self.expenses:
            if expense.title == title:
                return expense
        return None


    def to_dict(self):
        # Return a list of dictionaries representing each expense in the database
        return [expense.to_dict() for expense in self.expenses]

