import pytest
from pos_logic import calculate_total, add_to_order, InvalidQuantityError

def test_calculate_total():
    mock_order = [
        {"drink_code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
        {"drink_code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
    ]
    assert calculate_total(mock_order) == 125000

def test_invalid_quantity():
    mock_order = []
    with pytest.raises(InvalidQuantityError):
        add_to_order(mock_order, "T1", -1)