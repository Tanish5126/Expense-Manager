import csv
from datetime import datetime

class Expense:
    valid_categories = ["Food", "Travel", "Entertainment", "Others"]

    def __init__(self, amount: float, category: str, date: str, description: str = ""):
        if amount <= 0:
            raise ValueError("Amount must be positive")

    ## Assisgning attributes in class
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.strptime(date, "%Y-%m-%d")
    
    # dunder method
    def __str__(self):
        return (f"{self.date.strftime('%Y-%m-%d')} | {self.category}: ₹{self.amount:.2f} - {self.description}")


class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.old_expenses()

    def old_expenses(self):
        ## Error Handling
        try:

            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header, returns None if empty

                for row in reader:
                    if row:  # Only process non-empty rows
                        amt, cat, date, desc = row
                        exp = Expense(float(amt), cat, date, desc)     #created expense object, and passed value in expense class
                        self.expenses.append(exp)

        except FileNotFoundError:
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["amount", "category", "date", "description"])

    def new_expense(self, exp):
        self.expenses.append(exp)
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([exp.amount,exp.category,exp.date.strftime("%Y-%m-%d"),exp.description ])
