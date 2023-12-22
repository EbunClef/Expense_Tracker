# Expense Tracker Project

## Overview
The Expense Tracker project is a simple Python application that models and manages financial expenses. It includes two classes: `Expense` and `ExpenseDatabase`, which allow users to represent individual expenses and manage a collection of expenses.

## Classes

### Expense Class
Represents an individual financial expense.

#### Attributes:
- **id**: A unique identifier generated as a UUID string.
- **title**: A string representing the title of the expense.
- **amount**: A float representing the amount of the expense.
- **created_at**: A timestamp indicating when the expense was created.
- **updated_at**: A timestamp indicating the last time the expense was updated.

#### Methods:
- `__init__`: Initializes the attributes.
- `update`: Allows updating the title and/or amount, updating the `updated_at` timestamp.
- `to_dict`: Returns a dictionary representation of the expense.

### ExpenseDB Class
Manages a collection of Expense objects.

#### Attributes:
- **expenses**: A list storing Expense instances.

#### Methods:
- `__init__`: Initializes the list.
- `add_expense`: Adds an expense.
- `remove_expense`: Removes an expense.
- `get_expense_by_id`: Retrieves an expense by ID.
- `get_expense_by_title`: Retrieves expenses by title.
- `to_dict`: Returns a list of dictionaries representing expenses.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Clone the Repository

