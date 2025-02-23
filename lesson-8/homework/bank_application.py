from abc import ABC, abstractmethod
import csv
import json
class Account:
    def __init__(self, account_num, name, balance=0):
        self.account_num = account_num
        self.name = name
        self.balance = balance
    
    def to_dict(self):
        return {
            "Account number": self.account_num,
            "Name" : self.name,
            "Balance" : self.balance
        }
    
    @staticmethod
    def from_dict(data):
        return Account(data["Account number"], data["Name"], data["Balance"])
    
class FileStoring(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class CSVFileStoring(FileStoring):
    def __init__(self, filename = "bank_accounts.csv"):
        self.filename = filename

    def save(self, accounts):
        with open(self.filename, "w", newline="") as file:
            content = csv.DictWriter(file, fieldnames=["Account number", "Name", "Balance"])
            content.writeheader()
            for acc in accounts:
                content.writerow(acc.to_dict())

    def load(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Account.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks
    
class JSONFileStoring(FileStoring):
    def __init__(self, filename = "bank_accounts.json"):
        self.filename = filename
    
    def save(self, accounts):
        with open(self.filename, 'w') as file:
            json.dump([acc.to_dict() for acc in accounts], file, indent=2)
    
    def load(self):
        accounts = []
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                accounts = [Account.from_dict(acc) for acc in data]
        except FileNotFoundError:
            pass
        return accounts

class Bank:
    def __init__(self, file_storing: FileStoring):
        self.file_storing = file_storing
        self.accounts = file_storing.load()

    def create_account(self, account):
        self.accounts.append(account)
        print("Account has created succesfully!")

    def search_acc(self, acc_num, silent = False):
        for account in self.accounts:
            if account.account_num == acc_num:
                if not silent:
                    print("Account is found")
                return account
        else:
            if not silent:
                print("There is no account with this number.")
        return 

    def view_acc(self, acc_num):
        account = self.search_acc(acc_num, silent=True)
        if account:
            print(account.to_dict())
        else:
            print("There is no account with this number")

    
    def deposit(self, acc_num, amount):
        account = self.search_acc(acc_num, silent=True)
        if account:
            account.balance += amount
            print(f"{amount} has been deposited. New balance: {account.balance}")
        else:
            print("There is no account with this number")

    def withdrawal(self, acc_num, amount):
        account = self.search_acc(acc_num, silent=True)
        if account:
            if amount<=account.balance:
                account.balance= account.balance - amount
                print(f"{amount} has been withdrawn. New balance: {account.balance}")
            else:
                print(f"There is no {amount} in your account!")
        else:
            print("There is no account with this number")   

    def save_accs(self):
        self.file_storing.save(self.accounts)
        print("Account has saved successfully!")

if __name__ == "__main__":
    storage = JSONFileStoring()
    BankApp = Bank(storage)
    while True:
        print("Bank application")
        print("1. Create a new bank account")
        print("2. View the bank account")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Save the account")
        print("6. Exit")

        choice = int(input("Choose option (1-6): "))
        
        try: 
            if choice == 1:
                acc_number = input("Write the account number: ")
                acc_name = input("Write a name for your bank account: ")
                while True:
                    try:
                        acc_balance = int(input("Write your balance: "))
                        break
                    except ValueError:
                        print("Invalid input for balance. Please enter a number for balance!")
                new_acc = Account(acc_number, acc_name, acc_balance)
                BankApp.create_account(new_acc)
            elif choice == 2:
                acc_number = input("Write the account number: ")
                BankApp.view_acc(acc_number)
            elif choice ==3:
                acc_number = input("Write the account number: ")
                while True:
                    try:
                        amount = int(input("Enter the amount of deposit: "))
                        break
                    except ValueError:
                        print("Invalid input for deposit. Please enter a number for deposit!")
                BankApp.deposit(acc_number, amount)
            elif choice == 4:
                acc_number = input("Write the account number: ")
                while True:
                    try:
                        amount = int(input("Enter the amount of withdrawal: "))
                        break
                    except ValueError:
                        print("Invalid input for withdrawal. Please enter a number for it!")
                BankApp.withdrawal(acc_number, amount)
            elif choice ==5:
                BankApp.save_accs()
            elif choice ==6:
                print("Application is closed")
                break            
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid Value, please enter number!")


        




