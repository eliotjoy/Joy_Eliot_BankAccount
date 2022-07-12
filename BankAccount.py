class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance, name): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(name)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5.00
            return self
    def display_account_info(self):
        print("Balance:", self.balance)
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_info(cls):
        print(cls.all_accounts)



user1 = BankAccount(0.1, 100.00, "user1")
user2 = BankAccount(0.05, 1500.00, "user2")

user1.deposit(50.00).deposit(25.00).deposit(75.00).withdraw(200.00).yield_interest().display_account_info()
user2.deposit(500.00).deposit(1000.00).withdraw(2000.00).withdraw(500.00).withdraw(250.00).withdraw(1000.00).yield_interest().display_account_info()

BankAccount.print_all_info()