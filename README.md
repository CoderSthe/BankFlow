# BankFlow


# BankAccount Class

## Overview

The `BankAccount` class simulates a simple bank account system with functionalities for deposits, withdrawals, and compound interest calculations.


## Installation

1. Open Terminal and clone the repository:

```bash
git clone git@github.com:CoderSthe/BankFlow.git
```

2. Navigate to the project directory:

```bash
cd BankFlow
```

3. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # for Linux/macOS
# or
.\venv\Scripts\activate   # for Windows
```

4. Install the required packages:

```bash
pip install .
```

Alternatively, you can install the project as a module by running:

```bash
pip install -e .
```

This will install the `bank_account` module in "editable" mode, allowing you to work
on the code while having the module installed.

5. Once installed, you can import the `BankAccount` class in your Python scripts:

```python
from banking.bank_account import BankAccount
```

# Running Tests

To run the test cases using pytest, use the following command:

```bash
pytest tests/
```

# Deactivate the Virtual Environment

Once you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

## Features

- **Initialization**: Create a new bank account with an initial balance and interest rate.
- **Deposit**: Add funds to the account.
- **Withdraw**: Remove funds from the account, provided there are sufficient funds.
- **Compound Interest**: Apply monthly compound interest to the account balance.

## Usage

### Class Initialization

To create a new bank account, provide the interest rate and optionally an initial balance:

```python
from decimal import Decimal
from banking.bank_account import BankAccount

# Creating a new bank account with an interest rate of 12% and initial balance of 0.00
account = BankAccount(interest_rate=12)

# Creating a new bank account with an interest rate of 8% and an initial balance of 100.00
account_with_balance = BankAccount(interest_rate=8, balance=100)
```

### Deposits

To deposit funds into the account, use the `deposit` method:

```python
# Deposit 500.00 into the account
account.deposit(500)

# Check the updated balance
print(account.balance)  # Should print 500.00
```

### Withdrawals

To withdraw funds from the account, use the `withdraw` method:

```python
# Withdraw 200.00 from the account
account.withdraw(200)

# Check the updated balance
print(account.balance)  # Should print 300.00
```

### Compound Interest

To apply monthly compound interest to the account balance, use the `compound_interest` method:

```python
# Apply compound interest
account.compound_interest()

# Check the updated balance
print(account.balance)  # Balance reflects the compound interest
```

# Bank Class

## Overview

The `Bank` class simulates a simple banking system, allowing users to manage bank accounts, perform transactions, and calculate interest. It inherits from the `BankAccount` class, which handles basic account attributes like interest rate and balance.

## Features

- **Account Management**: Create different types of bank accounts with specified interest rates.
- **Transactions**: Perform deposits, withdrawals, and transfers between accounts.
- **Interest Calculation**: Apply compound interest on account balances.
- **Unique Account Numbers**: Generate unique account numbers for new accounts.

## Usage

### Importing the class

First, ensure that the `Bank` class is accessible in your code:

```python
from banking.bank import Bank
```

### Creating a Bank instance

Instantiate the `Bank` class with an optional interest rate and initial balance:

```python
bank = Bank(interest_rate=5, balance=0)
```

### Adding account types

You can add different account types with specific interest rates:

```python
bank.add_account_type("Savings", Decimal(5))
bank.add_account_type("Checking", Decimal(2))
```

### Opening a bank account

To open a new bank account, specify the account type:

```python
account_number = bank.open_bank_account("Savings")
```

### Depositing money

To deposit money into an account:

```python
bank.deposit(account_number, Decimal(100))
```

### Withdrawing money

To withdraw money from an account:

```python
bank.withdraw(account_number, Decimal(50))
```

### Transferring money

To transfer money from one account to another:

```python
account_number_to = bank.open_bank_account("Checking")
bank.transfer(account_number, account_number_to, Decimal(30))
```

### Calculating compound interest

To apply compound interest to an account balance:

```python
bank.compound_interest(account_number)
```

### Checking balances and interest rates

You can check the balance and interest rate of an account:

```python
balance = bank.get_balance(account_number)
interest_rate = bank.get_interest_rate(account_number)
```

## Conclusion

The `Bank` class provides a foundational banking system with basic functionalities for account management and transactions. It can be expanded with additional features such as account statements and transaction history.


# Author

This project was created by Sithembiso Mdhluli

# Licence

This project is licenced under the [MIT Licence](https://opensource.org/license/MIT)