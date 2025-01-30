from typing import Union
from decimal import Decimal, ROUND_HALF_UP

PRECISION = Decimal("0.01")
AMOUNT_TYPE = Union[Decimal, int, float]


class BankAccount:
    def __init__(
        self,
        interest_rate: AMOUNT_TYPE,
        balance: AMOUNT_TYPE = 0.00,
    ) -> None:
        self.balance = self.validate_and_convert_input(balance, name="Initial balance")
        self.interest_rate = self.validate_and_convert_input(
            interest_rate, name="Interest rate"
        )

    def deposit(self, amount: AMOUNT_TYPE) -> None:
        amount = self.validate_and_convert_input(amount, name="Deposit amount")
        self.balance += Decimal(amount)
        self.balance = self.round_off_precision(self.balance)

    def withdraw(self, amount: AMOUNT_TYPE) -> None:
        amount = self.validate_and_convert_input(amount, name="Withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= Decimal(amount)
        self.balance = self.round_off_precision(self.balance)

    def compound_interest(self) -> None:
        self.balance = Decimal(self.balance)
        self.interest_rate = Decimal(self.interest_rate)
        yearly_interest = (self.interest_rate / Decimal(100)) * self.balance
        monthly_interest = yearly_interest / 12
        self.balance += monthly_interest
        self.balance = self.round_off_precision(self.balance)

    def validate_and_convert_input(
        self, value: AMOUNT_TYPE, name: str
    ) -> Decimal:
        if Decimal(value) < 0:
            raise ValueError(f"{name} must be greater than or equal to 0.00.")
        return Decimal(value)

    def round_off_precision(self, value: AMOUNT_TYPE) -> Decimal:
        return Decimal(value).quantize(PRECISION, rounding=ROUND_HALF_UP)
