import unittest
from models import Player
from datetime import datetime

# test pour le Elo
class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Création de deux joueurs pour les tests
        self.player1 = Player("Doe", "John", datetime(1990, 1, 1), "123456", 1000)
        self.player2 = Player("Smith", "Jane", datetime(1985, 5, 15), "654321", 900)

    def test_update_elo_score_win(self):
        original_score = self.player1.elo_score
        ajustement = (self.player2.elo_score - original_score) * 0.1
        expected_score = original_score + ajustement
        if "win":
            expected_score += 10
        self.player1.update_elo_score(self.player2.elo_score, "win")
        self.assertEqual(self.player1.elo_score, expected_score)


    def test_update_elo_score_loss(self):
        original_score = self.player1.elo_score
        ajustement = (self.player2.elo_score - original_score) * 0.1
        expected_score = original_score + ajustement
        if "loss":
            expected_score -= 10
        self.player1.update_elo_score(self.player2.elo_score, "loss")
        self.assertEqual(self.player1.elo_score, expected_score)


    def test_update_elo_score_draw(self):
        original_score = self.player1.elo_score
        ajustement = (self.player2.elo_score - original_score) * 0.1
        expected_score = original_score + ajustement
        if "draw":
            expected_score += 5
        self.player1.update_elo_score(self.player2.elo_score, "draw")
        self.assertEqual(self.player1.elo_score, expected_score)


if __name__ == '__main__':
    unittest.main()
