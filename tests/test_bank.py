import pytest
from decimal import Decimal
from banking.bank import Bank


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def setup_bank_account(bank):
    bank.add_account_type("Savings", Decimal(5))
    account_number = bank.open_bank_account("Savings")
    return bank, account_number


@pytest.fixture
def setup_deposited_bank_account(bank):
    bank.add_account_type("Savings", Decimal(5))
    account_number = bank.open_bank_account("Savings")
    bank.deposit(account_number, Decimal(1000))
    return bank, account_number


def test_existing_account_type_raises_error(setup_bank_account):
    bank, account_number = setup_bank_account
    with pytest.raises(ValueError, match="Account Type Savings already exists."):
        bank.add_account_type("Savings", Decimal(8))


def test_open_bank_account(setup_bank_account):
    bank, account_number = setup_bank_account
    assert account_number in bank.bank_accounts


def test_deposit(setup_deposited_bank_account):
    bank, account_number = setup_deposited_bank_account
    initial_balance = bank.get_balance(account_number)
    bank.deposit(account_number, Decimal(100))
    assert bank.get_balance(account_number) == initial_balance + Decimal(100)


def test_withdraw(setup_deposited_bank_account):
    bank, account_number = setup_deposited_bank_account
    initial_balance = bank.get_balance(account_number)
    bank.withdraw(account_number, Decimal(100))
    assert bank.get_balance(account_number) == initial_balance - Decimal(100)


def test_withdraw_insufficient_funds(setup_bank_account):
    bank, account_number = setup_bank_account
    with pytest.raises(ValueError, match="Insufficient funds."):
        bank.withdraw(account_number, Decimal(100))


def test_transfer(setup_deposited_bank_account):
    bank, account_number_from = setup_deposited_bank_account
    account_number_to = bank.open_bank_account("Savings")
    bank.transfer(account_number_from, account_number_to, Decimal(100))

    assert bank.get_balance(account_number_from) == Decimal(900)
    assert bank.get_balance(account_number_to) == Decimal(100)


def test_compound_interest(setup_deposited_bank_account):
    bank, account_number = setup_deposited_bank_account
    bank.compound_interest()

    interest = (Decimal(5) / Decimal(100)) * Decimal(1000) / Decimal(12)
    expected_balance = Decimal(1000) + interest

    assert round(bank.get_balance(account_number), 2) == round(expected_balance, 2)


def test_interest_rate(setup_bank_account):
    bank, account_number = setup_bank_account
    assert bank.get_interest_rate(account_number) == Decimal(5)


def test_generate_unique_number(setup_bank_account):
    bank, _ = setup_bank_account
    new_account_number = bank.generate_unique_number()
    assert new_account_number not in bank.bank_accounts


def test_nonexistent_account_type(bank):
    with pytest.raises(ValueError, match="Account type Fixed Deposit does not exist."):
        bank.open_bank_account("Fixed Deposit")


def test_nonexistent_account_transfer(setup_deposited_bank_account):
    bank, account_number_from = setup_deposited_bank_account
    invalid_account_number = "1234567890"
    with pytest.raises(ValueError, match=f"Account number {invalid_account_number} does not exist."):
        bank.transfer(account_number_from, invalid_account_number, Decimal(100))


def test_compound_interest_on_zero_balance(bank):
    bank.add_account_type("Current", Decimal(2.5))
    zero_balance_account = bank.open_bank_account("Current")
    bank.compound_interest()
    assert bank.get_balance(zero_balance_account) == Decimal("0.00")