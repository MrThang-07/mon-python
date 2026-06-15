import pytest
from main import calculate_energy_financials

def test_duoi_moc_chiet_khau():
    """Test Case 1: Dưới 50,000 kWh -> Chiết khấu 0%"""
    du_lieu = [{'old_index': 0, 'new_index': 10000}]
    tong_dien, chiet_khau, tong_tien = calculate_energy_financials(du_lieu)
    
    # Dùng assert giống y hệt thầy bạn dạy
    assert tong_dien == 10000
    assert chiet_khau == 0
    assert tong_tien == 30000000

def test_dat_moc_chiet_khau():
    """Test Case 2: Từ 50,000 kWh trở lên -> Chiết khấu 3%"""
    du_lieu = [{'old_index': 0, 'new_index': 60000}]
    tong_dien, chiet_khau, tong_tien = calculate_energy_financials(du_lieu)
    
    assert tong_dien == 60000
    assert chiet_khau == 3
    assert tong_tien == 174600000

def test_danh_sach_trong():
    """Test Case 3: Không có thiết bị nào -> Mọi thứ bằng 0"""
    du_lieu = []
    tong_dien, chiet_khau, tong_tien = calculate_energy_financials(du_lieu)
    
    assert tong_dien == 0
    assert chiet_khau == 0
    assert tong_tien == 0