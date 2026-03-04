from bank import Bank

bank = Bank()


def account_menu(account):
    while True:
        print("\n1 Deposit")
        print("2 Withdraw")
        print("3 Transfer")
        print("4 Balance")
        print("5 Transactions")
        print("6 Logout")

        choice = input("Choose: ")

        if choice == "1":
            amount = float(input("Amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Amount: "))
            if not account.withdraw(amount):
                print("Insufficient balance")

        elif choice == "3":
            receiver = input("Receiver account number: ")
            amount = float(input("Amount: "))
            bank.transfer(account, receiver, amount)

        elif choice == "4":
            print("Balance:", account.balance)

        elif choice == "5":
            for t in account.transactions:
                print(t)

        elif choice == "6":
            break


while True:
    print("\n--- Banking System ---")
    print("1 Create Account")
    print("2 Login")
    print("3 Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        password = input("Password: ")
        bank.create_account(name, password)

    elif choice == "2":
        acc = input("Account number: ")
        pwd = input("Password: ")

        user = bank.login(acc, pwd)

        if user:
            account_menu(user)
        else:
            print("Invalid login")

    elif choice == "3":
        break