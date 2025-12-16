import csv
from datetime import datetime
from expense_class import Expense, ExpenseTracker
from analyzer import MonthlySummary, BudgetAnalyzer


def confirm_entry(func):
    def wrapper(*args, **kwargs):
        print("\nRecording expense...")
        result = func(*args, **kwargs)   
        print("Expense recorded successfully!\n")
        return result
    return wrapper


@confirm_entry
def new_expense_to_tracker(tracker):
    amt = float(input("Amount: "))

    print("\nEnter category (Food / Travel / Entertainment or anything else):")
    cat = input("Category: ")

    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")

   
    exp = Expense(amt, cat, date, description)
    tracker.new_expense(exp)

    print(exp)



def main():
    tracker = ExpenseTracker()

    while True:
        print("1. Add Expense")
        print("2. Show Monthly Summary")
        print("3. Check Budget")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            new_expense_to_tracker(tracker)
            
            

        elif choice == "2":
            month = input("Enter month number (1-12): ")
            year = input("Enter year (YYYY): ")

            summary = MonthlySummary(tracker.expenses, month, year)
            summary.show_summary()
            summary.show_pie_chart()

            

        elif choice == "3":
            category = input("Enter category to check: ")
            limit = float(input("Enter budget limit: "))

            month = input("Enter month number (1-12): ")
            year = input("Enter year (YYYY): ")

            summary = MonthlySummary(tracker.expenses, month, year)
            analyzer = BudgetAnalyzer(summary.cat_total)
            analyzer.check_budget(category, limit)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
