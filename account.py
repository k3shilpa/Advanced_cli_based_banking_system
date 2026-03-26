import uuid
from datetime import datetime


class Account:
    def __init__(self, name, password, balance=0):
        self.account_number = str(uuid.uuid4())[:8]
        self.name = name
        self.password = password
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            "type": "deposit",
            "amount": amount,
            "time": str(datetime.now())
        })

    def withdraw(self, amount):
        MIN_BALANCE = 100

        if amount > self.balance:
            print("Insufficient balance")
            return False

        if self.balance - amount < MIN_BALANCE:
            print("Cannot withdraw. Minimum balance of 100 must be maintained.")
            return False

        self.balance -= amount

        self.transactions.append({
            "type": "withdraw",
            "amount": amount,
            "time": str(datetime.now()),
            "balance": self.balance
        })

        return True