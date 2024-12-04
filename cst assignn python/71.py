##71.	Create a budgeting application that tracks expenses using classes.in very short 
class Budget:
    def __init__(self):
        self.expenses =[]

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def show_expenses(self):
        total = 0
        print("Expenses:")
        for exp in self.expenses:
            print(f"{exp['description']}: ${exp['amount']}")
            total += exp["amount"]
        print(f"Total: ${total}")

# Usage
budget = Budget()
budget.add_expense("Groceries", 750)
budget.add_expense("Utilities", 645)
budget.show_expenses()