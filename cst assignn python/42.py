##42.	Create a class that models a BankAccount with methods to deposit and withdraw funds.
class bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self, amount ):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully. new balnce: ${self.balance:.2f}")
        else :
            print("deposite amount must be positive")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                 print(f"${amount} withdraw successfully . new balance: ${self.balance:.2f}")

            else :
                 print("insufficient funds.")
        else:
            print("withdrawal samount must be positive.")

    def display_balance(self):
        print(f"current balance : ${self.balance:.2f}")


