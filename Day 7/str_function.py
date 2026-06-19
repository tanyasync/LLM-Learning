class BankAccount:
    interest_rate= 4
    def __init__(self, name, account_no, balance=0,):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        
    def __str__(self):
        return f"(self.owner): Rs(self.balance)"

tom = BankAccount("Tom", 3000)
print(tom)