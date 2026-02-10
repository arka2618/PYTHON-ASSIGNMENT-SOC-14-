class Bankaccount:
    def __init__(self, account_no, balance = 0):
        self.account_no = account_no
        self.balance = balance
        print(f"Your current balance is Rs {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs {amount} successfully deposited")
            print(f"Your current balance is Rs {self.balance}")
        else:
            print("Invalid diposit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Rs {amount} has been withdrawn")
        else:
            print(f"Sorry! Withdrawal of Rs {amount} not possible due to Insufficient balance or invalid amount")
    
    def check_balance(self):
        print(f"The current balance of you account is Rs {self.balance}")


account = Bankaccount(210, 9000)
account.deposit(500)
account.withdraw(8000)

account.check_balance()
