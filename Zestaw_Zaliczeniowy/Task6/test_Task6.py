import pytest
from Task6 import BankAccount

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

    with pytest.raises(ValueError):
        BankAccount(-100)

def test_deposit():
    account = BankAccount(0)
    account.deposit(100)
    assert account.get_balance() == 100

    with pytest.raises(ValueError):
        account.deposit(-50)

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

    with pytest.raises(ValueError):
        account.withdraw(-50)

    with pytest.raises(ValueError):
        account.withdraw(200)

def test_get_balance():
    account = BankAccount(200)
    assert account.get_balance() == 200

if __name__ == "__main__":
    pytest.main()
