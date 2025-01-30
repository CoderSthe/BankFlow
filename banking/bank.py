from decimal import Decimal
from random import randint

from banking.bank_account import AMOUNT_TYPE, BankAccount


class Bank:
    def __init__(self) -> None:

        self.bank_accounts = {}
        self.bank_account_types = {}

    def add_account_type(
        self, account_type: str, interest_rate: AMOUNT_TYPE
    ) -> None:
        if account_type in self.bank_account_types:
            raise ValueError(f"Account Type {account_type} already exists.")
        else:
            self.bank_account_types[account_type] = interest_rate

    def open_bank_account(self, account_type: str) -> str:
        if account_type not in self.bank_account_types:
            raise ValueError(f"Account type {account_type} does not exist.")

        account_number = self.generate_unique_number()
        balance = Decimal("0.00")
        interest_rate = self.bank_account_types[account_type]
        new_account = BankAccount(interest_rate, balance)
        self.bank_accounts[account_number] = new_account

        return account_number

    def deposit(
        self, bank_account_number: str, amount: AMOUNT_TYPE
    ) -> None:
        account = self.get_account(bank_account_number)
        account.deposit(amount)

    def withdraw(
        self, bank_account_number: str, amount: AMOUNT_TYPE
    ) -> None:
        account = self.get_account(bank_account_number)
        account.withdraw(amount)

    def transfer(
        self,
        from_account_number: str,
        to_account_number: str,
        amount: AMOUNT_TYPE,
    ) -> None:
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def compound_interest(self) -> None:
        for account_number in self.bank_accounts:
            account = self.get_account(account_number)
            account.compound_interest()

    def get_balance(self, from_account_number: str) -> AMOUNT_TYPE:
        account = self.get_account(from_account_number)
        return account.balance

    def get_interest_rate(self, from_account_number: str) -> AMOUNT_TYPE:
        account = self.get_account(from_account_number)
        return account.interest_rate

    def generate_unique_number(self) -> str:
        num_of_digits = 10
        generated_number = "".join(
            ["{}".format(randint(0, 9)) for _ in range(0, num_of_digits)]
        )

        while generated_number in self.bank_accounts.keys():
            generated_number = "".join(
                ["{}".format(randint(0, 9)) for _ in range(0, num_of_digits)]
            )

        return generated_number

    def get_account(self, account_number: str):
        if account_number not in self.bank_accounts:
            raise ValueError(f"Account number {account_number} does not exist.")
        return self.bank_accounts[account_number]
