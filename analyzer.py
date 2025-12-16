import pandas as pd
import matplotlib.pyplot as plt

class MonthlySummary:
    def __init__(self, expenses, month, year):
    
        
        self.expenses = [e for e in expenses if e.date.month == int(month) and e.date.year == int(year)]

        self.month = month
        self.year = year
        self.total = sum(e.amount for e in self.expenses)
        self.cat_total = self.group_by_category()

    def group_by_category(self):
        data = {}


        for e in self.expenses:
            data[e.category] = data.get(e.category, 0) + e.amount
        return data

 

    def show_summary(self):
        print(f"\nSUMMARY FOR {self.month}/{self.year}")
        print(f"Total Spending: {self.total}")

        print("\nBreakdown by Category:")
        for cat, amt in self.cat_total.items():
            percent = (amt / self.total) * 100 if self.total > 0 else 0
            print(f"{cat}: {amt} ({percent:.1f}%)")

        # Highest spending day
        if self.expenses:
            daily = {}    # key:day & value: total spending for day
            for e in self.expenses:
                day = e.date.day
                daily[day] = daily.get(day, 0) + e.amount

            high_day = max(daily, key=lambda x: daily[x])

            print(f"\nHighest Spending Day: {high_day} ({daily[high_day]})")
            print(f"Average Daily Spending: {self.total / 30:.2f}")
        else:
            print("No expenses recorded.")
            
    
    def show_pie_chart(self):
        if not self.cat_total:
            print("\nNo data to plot.")
            return

        labels = list(self.cat_total.keys())
        amounts = list(self.cat_total.values())

        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"Spending Breakdown - {self.month}/{self.year}")
        plt.tight_layout()  # Adjust everything without overlap
        plt.show()


class BudgetAnalyzer:
    def __init__(self, cat_totals):
        self.cat_totals = cat_totals

    def check_budget(self, category, limit):
        spent = self.cat_totals.get(category, 0)
        if spent > limit:
            print(f"\nBudget Alert: Exceeded {category} budget by {spent - limit}.")
            print("Recommendation: Reduce spending in this category.\n")
