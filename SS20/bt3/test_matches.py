import unittest
from bt3 import determine_winner

class TestDetermineWinner(unittest.TestCase):
    
    def test_team_a_wins(self):
        """Test Case 1: Đội A có điểm số lớn hơn Đội B và đã hoàn thành"""
        match = {
            "match_id": "M01",
            "team_a": "T1",
            "team_b": "GenG",
            "score_a": 2,
            "score_b": 0,
            "status": "Completed"
        }
        result = determine_winner(match)
        self.assertEqual(result, "T1")

    def test_draw(self):
        """Test Case 2: Hai đội có điểm số bằng nhau và đã hoàn thành"""
        match = {
            "match_id": "M02",
            "team_a": "JDG",
            "team_b": "BLG",
            "score_a": 1,
            "score_b": 1,
            "status": "Completed"
        }
        result = determine_winner(match)
        self.assertEqual(result, "Draw")

    def test_pending(self):
        """Test Case 3: Trận đấu chưa diễn ra (Pending)"""
        match = {
            "match_id": "M03",
            "team_a": "G2",
            "team_b": "FNC",
            "score_a": 0,
            "score_b": 0,
            "status": "Pending"
        }
        result = determine_winner(match)
        self.assertEqual(result, "Not Started")

if __name__ == '__main__':
    unittest.main()