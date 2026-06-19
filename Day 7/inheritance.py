## inehritance - a reuse

class Animal:
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return "...."
class Dog(Animal):
    def speak(self):
        return "woof!"
class Cat(Animal):
    def speak(self):
        return "meow!"
    
rex = Dog("Rex")
print(rex.speak())
luna = Cat("Luna")
print(luna.speak())
mystery = Animal("Mystery")
print(mystery.speak())


#Main Class - BankAccount
#Sub - Saving Account - Current Account, Loan Account
#Saving Account - Cannot withdraw more than 30k, Interest
#rate - 6%
#Current Account- can withdraw any amount
#CA- interest rate 2%, Cannot deposit more than 300k
#loan account - cannot withdraw


class BankAccount:
    interest_rate= 4
    def __init__(self, name, account_no, balance=0,):
        self.name=name
        self.account_no=account_no
        self.balance=balance

    def withdraw(self, withdraw_amount):
        self.balance-= withdraw_amount
        return (f"updated balance: (self.balance)")
        
    def deposit(self, deposit_amount):
        balance+= deposit_amount
        return (f"updated balance: (self.balance)")
        
class SavingsAccount:
    interest_rate=6
    def withdraw(self, withdraw_amount):
        if withdraw_amount <=30000:
            balance-= withdraw_amount
            return(self.balance)
        else:
            return("can only withdraw 30k")
        
class CurrentAccount:
    interest_rate=2
    def withdraw(self,withdraw_amount):
        if withdraw_amount <=300000:
            balance-= withdraw_amount
            return(self.balance)
        else:
            return(self.balance)
    
class LoanAccount:
    def withdraw(self,withdraw_amount):
        return(self.balance)


##str function - human readable output generate karta hai
##super() keyword