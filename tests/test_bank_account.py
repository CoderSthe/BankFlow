import pytest
from decimal import Decimal

from banking.bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount(balance=1000, interest_rate=12)


@pytest.fixture
def account_2():
    return BankAccount(balance=1000.50, interest_rate=8.2)


@pytest.fixture
def zero_interest_account():
    return BankAccount(balance=1000, interest_rate=0)


def test_correct_bank_balance(account):
    assert account.balance == Decimal("1000.00")


def test_deposit_updates_balance(account):
    account.deposit(amount=5000)
    assert account.balance == Decimal("6000.00")


def test_cannot_deposit_negative_amount(account):
    with pytest.raises(
        ValueError, match="Deposit amount must be greater than or equal to 0.00."
    ):
        account.deposit(amount=-300)


def test_withdrawal_updates_balance(account):
    account.withdraw(amount=250.00)
    assert account.balance == Decimal("750.00")


def test_cannot_withdraw_negative_amount(account):
    with pytest.raises(
        ValueError, match="Withdrawal amount must be greater than or equal to 0.00."
    ):
        account.withdraw(amount=-100)


def test_cannot_withdraw_more_than_balance(account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account.withdraw(amount=2000.00)


def test_compound_interest_updates_balance(account):
    account.compound_interest()
    assert account.balance == Decimal("1010.00")


def test_compound_interest_with_float_digits(account_2):
    account_2.compound_interest()
    assert account_2.balance == Decimal("1007.34")


def test_check_value_validity_with_negative_value(account):
    with pytest.raises(
        ValueError, match="Deposit amount must be greater than or equal to 0.00."
    ):
        account.validate_and_convert_input(value=-100.00, name="Deposit amount")


def test_negative_initial_balance_throws_error():
    with pytest.raises(
        ValueError, match="Initial balance must be greater than or equal to 0.00."
    ):
        BankAccount(balance=-500, interest_rate=12)


def test_zero_interest_no_balance_change(zero_interest_account):
    zero_interest_account.compound_interest()
    assert zero_interest_account.balance == Decimal("1000.00")


def test_compound_interest_on_zero_balance(account):
    zero_balance_account = BankAccount(balance=0, interest_rate=5)
    zero_balance_account.compound_interest()
    assert zero_balance_account.balance == Decimal("0.00")


def test_large_precision_interest_calculation(account_2):
    account_2.interest_rate = Decimal("8.2345")
    account_2.compound_interest()
    assert account_2.balance == Decimal("1007.37")
