class BankAccount:
    bank_name = "Armen's Union Bank"
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("insufficient funds: Chharging fee")
            self.balance -= 5
        return self

    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

checking = BankAccount(.02,2000)
savings = BankAccount(.04,1000)

savings.deposit(20).deposit(10).deposit(15).yield_interest().display_account_info()
checking.deposit(20).deposit(15).withdraw(5).withdraw(2).withdraw(1).yield_interest().display_account_info()

class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)

armen = User("Armen", "bob@gmail", checking)

armen.display_user_balance()