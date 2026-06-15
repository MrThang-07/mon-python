from main import calculate_payment
import pytest

# Trường hợp tốt nhất
def test_happy():
    assert calculate_payment(100.0 , 0.1) == 90.0

def test_rate_full():
    assert calculate_payment(100.0 , 1.0) == 0.0

def test_rate_zero():
    assert calculate_payment(100.0 , 0.0) == 100.0

#  trường hợp lỗi , xấu
def test_negative():
    with pytest.raises(ValueError):
        calculate_payment(-100.0 , 0.1)