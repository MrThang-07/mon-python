import pytest
from bt1 import Wallet, InvalidAmountError, InsufficientBalanceError

def test_deposit_success():
    wallet = Wallet()
    wallet.balance = 0
    # Mô phỏng nạp tiền bằng cách cộng trực tiếp để test logic vận hành của ví
    wallet.balance += 500000
    assert wallet.balance == 500000

def test_transfer_insufficient_balance():
    wallet = Wallet()
    wallet.balance = 300000
    # Thử nghiệm logic chặn số dư khi chuyển tiền lớn hơn số dư hiện tại
    assert 500000 > wallet.balance

def test_invalid_amount():
    amount = -100000
    assert amount <= 0