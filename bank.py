import json
from account import Account


class Bank:

    def __init__(self):
        self.accounts = {}
        self.load_data()

    def create_account(self, name, password):
        account = Account(name, password)
        self.accounts[account.account_number] = account
        self.save_data()
        print("Account created successfully")
        print("Account Number:", account.account_number)

    def login(self, acc_number, password):
        account = self.accounts.get(acc_number)

        if account and account.password == password:
            return account
        return None

    def transfer(self, sender, receiver_acc, amount):
        receiver = self.accounts.get(receiver_acc)

        if not receiver:
            print("Receiver not found")
            return

        if sender.withdraw(amount):
            receiver.deposit(amount)
            self.save_data()
            print("Transfer successful")
        else:
            print("Insufficient balance")

    def save_data(self):
        data = {}

        for acc_no, acc in self.accounts.items():
            data[acc_no] = {
                "name": acc.name,
                "password": acc.password,
                "balance": acc.balance,
                "transactions": acc.transactions
            }

        with open("data.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

                for acc_no, info in data.items():
                    acc = Account(info["name"], info["password"], info["balance"])
                    acc.account_number = acc_no
                    acc.transactions = info["transactions"]
                    self.accounts[acc_no] = acc

        except FileNotFoundError:
            pass