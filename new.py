class BankAccount:

    accounts_num = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.accounts_num += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
        elif amount < 0 or amount == 0:
            print("ERROR")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Your balance not enough")
        elif amount < 0 or amount == 0:
            print("ERROR")
        else:
            self.balance -= amount
            self.show_balance()


    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


custom_1 = BankAccount("Ahmed", 80)
custom_2 = BankAccount("Ali", 40)

custom_1.deposit(40)
