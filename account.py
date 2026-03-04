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
        if amount > self.balance:
            return False

        self.balance -= amount
        self.transactions.append({
            "type": "withdraw",
            "amount": amount,
            "time": str(datetime.now())
        })
        return True