
# Simple OOP Bank Account Program (User Data Only)
import random

class BankAccount:
    def __init__(self, name, balance):
        self.account_number = ''.join([str(random.randint(0,9)) for _ in range(16)])
        self.account_holder = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Balance:", self.balance)

    def speak(self):
        print(f"Hello, I am a bank account belonging to {self.account_holder}.")

class SavingAccount(BankAccount):
    interest_rate = 4
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest added:", interest)

    def speak(self):
        print(f"Saving Account created.")

class CurrentAccount(BankAccount):
    overdraft_limit = 50000
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Overdraft limit exceeded.")

    def speak(self):
        print(f"Hello, I am a Current Account for {self.account_holder} with overdraft limit ₹{self.overdraft_limit}.")

# Main program (user data only)
acc_type = input("Enter account type (saving/current): ").lower()
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))


if acc_type == "saving":
    acc = SavingAccount(name, balance)
    print("Account Number:", acc.account_number)
    print("Interest Rate:", acc.interest_rate, "%")
    acc.speak()
elif acc_type == "current":
    acc = CurrentAccount(name, balance)
    print("Account Number:", acc.account_number)
    print("Overdraft Limit:", acc.overdraft_limit)
    acc.speak()
else:
    print("Invalid account type.")
    exit()

while True:
    print("\n 1.Deposit \n 2.Withdraw \n 3.Display Balance")
    if acc_type == "saving":
        print(" 4.Apply Interest \n 5.Exit")
    else:
        print(" 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Amount to deposit: "))
        acc.deposit(amt)
    elif choice == "2":
        amt = float(input("Amount to withdraw: "))
        acc.withdraw(amt)
    elif choice == "3":
        acc.display_balance()
    elif choice == "4" and acc_type == "saving":
        acc.apply_interest()
    elif (choice == "4" and acc_type == "current") or (choice == "5" and acc_type == "saving"):
        print("Thank you!")
        break
    else:
        print("Invalid choice.")