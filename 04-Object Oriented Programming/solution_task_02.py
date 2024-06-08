from abc import ABC, abstractmethod
from datetime import date

# Abstract base class representing a generic account
class Account(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance  # Encapsulation of balance attribute
        self.transactions = []

    # Deposit money into the account
    def deposit(self, amount):
        self._balance += amount
        self.add_transaction("Deposit", amount)
    
    # Abstract method for withdrawing money, must be implemented by subclasses
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Getter for balance
    def get_balance(self):
        return self._balance

    # Add a transaction to the account's transaction history
    def add_transaction(self, transaction_type, amount):
        self.transactions.append(Transaction(transaction_type, amount, date.today(), self._balance))

    # Abstract method for calculating interest, must be implemented by subclasses
    @abstractmethod
    def calculate_interest(self):
        pass

    # String representation of the account
    def __str__(self):
        return f"Account: {self.account_number}, Holder: {self.account_holder}, Balance: {self._balance}"

# Class representing a savings account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # Withdraw money from the savings account if there are sufficient funds
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self.add_transaction("Withdrawal", amount)
        else:
            print("Insufficient funds.")

    # Calculate interest for the savings account
    def calculate_interest(self):
        return self._balance * self.interest_rate

# Class representing a checking account
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Withdraw money from the checking account, considering the overdraft limit
    def withdraw(self, amount):
        if self._balance + self.overdraft_limit >= amount:
            self._balance -= amount
            self.add_transaction("Withdrawal", amount)
        else:
            print("Overdraft limit exceeded.")

    # Calculate interest for the checking account (always zero)
    def calculate_interest(self):
        return 0

# Class representing a fixed deposit account
class FixedDepositAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05, maturity_date=None):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date

    # Withdraw money from the fixed deposit account (not allowed until maturity date)
    def withdraw(self, amount):
        print("Withdrawal not allowed until maturity date.")

    # Calculate interest for the fixed deposit account
    def calculate_interest(self):
        return self._balance * self.interest_rate

# Class representing a transaction
class Transaction:
    def __init__(self, transaction_type, amount, date, balance_after_transaction):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
        self.balance_after_transaction = balance_after_transaction

    # String representation of the transaction
    def __str__(self):
        return f"{self.date}: {self.transaction_type} of {self.amount}. Balance: {self.balance_after_transaction}"

# Class representing the bank, managing multiple accounts
class Bank:
    def __init__(self):
        self.accounts = {}

    # Create a new account and add it to the bank's list of accounts
    def create_account(self, account_type, account_number, account_holder, balance=0, **kwargs):
        if account_type == "Savings":
            account = SavingsAccount(account_number, account_holder, balance, kwargs.get('interest_rate', 0.01))
        elif account_type == "Checking":
            account = CheckingAccount(account_number, account_holder, balance, kwargs.get('overdraft_limit', 500))
        elif account_type == "FixedDeposit":
            account = FixedDepositAccount(account_number, account_holder, balance, kwargs.get('interest_rate', 0.05), kwargs.get('maturity_date', None))
        else:
            print("Invalid account type.")
            return
        
        self.accounts[account_number] = account

    # Retrieve an account by its account number
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    # List all accounts in the bank
    def list_accounts(self):
        for account in self.accounts.values():
            print(account)

# Example usage
bank = Bank()

# Creating accounts
bank.create_account("Savings", "001", "Alice", 1000, interest_rate=0.02)
bank.create_account("Checking", "002", "Bob", 500)
bank.create_account("FixedDeposit", "003", "Charlie", 2000, interest_rate=0.03, maturity_date=date(2025, 12, 31))

# Depositing and withdrawing money
account = bank.get_account("001")
account.deposit(500)
account.withdraw(200)
print(account)

# Calculating interest
print(f"Interest: {account.calculate_interest()}")

# Listing all accounts
bank.list_accounts()




"""
Explanation:
    
    Encapsulation:
        Encapsulation is used in the Account class where the balance is stored as a private attribute (_balance). This prevents direct modification and ensures that changes to the balance can only be made through the methods deposit(), withdraw(), and get_balance().
    
    Inheritance:
        The SavingsAccount, CheckingAccount, and FixedDepositAccount classes inherit from the Account class. This allows these classes to share common functionality while implementing their specific behavior for withdraw() and calculate_interest() methods.
    
    Polymorphism:
        Polymorphism is demonstrated in the withdraw() and calculate_interest() methods. Each subclass (SavingsAccount, CheckingAccount, and FixedDepositAccount) has its own implementation of these methods, allowing them to be used interchangeably through the Account reference.

    Abstraction:
        The Account class is an abstract base class (ABC) with abstract methods withdraw() and calculate_interest(). This enforces that any subclass must implement these methods, providing a clear and consistent interface for different types of accounts.
    
    Setters and Getters:
        Getter for Balance: get_balance() method in the Account class provides controlled access to the private _balance attribute.
        Setters for Transactions: Although there are no explicit setters for transactions, the add_transaction() method encapsulates the logic for updating the transactions list, ensuring that transactions are recorded properly.
                
        
    Class Methods:
        Account Class Methods:

            deposit(): Adds money to the account and records the transaction.
            withdraw(): Abstract method to be implemented by subclasses, defining how money is withdrawn.
            get_balance(): Returns the current balance.
            add_transaction(): Adds a transaction to the transaction history.
            calculate_interest(): Abstract method to be implemented by subclasses, defining how interest is calculated.
        
        Bank Class Methods:

            create_account(): Creates a new account based on the type and adds it to the bank's accounts.
            get_account(): Retrieves an account by its account number.
            list_accounts(): Lists all accounts in the bank.
        """