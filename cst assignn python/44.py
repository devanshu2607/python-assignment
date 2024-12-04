##44.	Write a program that demonstrates encapsulation through private class members.
class account :
    def __init__(self,account_number,initial_balance):
        self.__account_number =account_number #private attribute
        self.balance=initial_balance  #private attribute

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f'depositrd:{amount}. new balance: {self.__balance}') 
        else:
            print("invalideamount.deposit faild.")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance -= amount
            print(f"withdrew: {amount}.new balance: {self.__balance}")
        else:
            print("invalide amount or insufficicet balance . withdrawal faild. ")

    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
account= account("123456789",1000)

print(f"account number:{account.get_account_number()}")
print(f"initial balance: {account.get_balance()}")
account.deposit(400)
account.withdraw(200)
print(f"final balnce :{account.get_balance()}") 