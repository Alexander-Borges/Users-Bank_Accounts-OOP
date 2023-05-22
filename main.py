class User: 
    def __init__(self,name,email):
        self.name = name 
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    #other methods
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self.account.balance
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self.account.balance
    
    def display_account_info(self):
        return self.account.display_account_info()
    
class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=5

    def display_account_info(self):
        return f"Balance: ${self.balance}, Interest Rate: {self.int_rate *100}%"

user = User("Alex Borges", "Alex@gmail.com")
user.make_deposit(20000)
user.make_withdrawal(7000)
print(user.display_account_info())