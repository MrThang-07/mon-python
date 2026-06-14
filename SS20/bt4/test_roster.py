import unittest
from bt4 import calculate_actual_pay

class TestPayrollLogic(unittest.TestCase):
    
    def test_active_salary(self):
        """Test Case 1: Tuyển thủ Active nhận đúng 100% lương"""
        mock_player = {
            "player_id": "P01",
            "name": "Faker",
            "salary": 5000.0,
            "status": "Active"
        }
        # Thực nhận mong đợi là 5000.0
        result = calculate_actual_pay(mock_player)
        self.assertEqual(result, 5000.0)

    def test_benched_salary(self):
        """Test Case 2: Tuyển thủ Benched nhận đúng 50% lương"""
        mock_player = {
            "player_id": "P03",
            "name": "Ruler",
            "salary": 6000.0,
            "status": "Benched"
        }
        # 50% của 6000 là 3000.0
        result = calculate_actual_pay(mock_player)
        self.assertEqual(result, 3000.0)

if __name__ == '__main__':
    unittest.main()