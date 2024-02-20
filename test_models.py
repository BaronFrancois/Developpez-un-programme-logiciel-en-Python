import unittest
from datetime import date
from models import Player, ChessTournament, TournamentRound, ChessMatch

class TestPlayer(unittest.TestCase):
    def test_creation_player(self):
        player = Player(name="Doe", first_name="John", birth_date=date(1990, 1, 1), gender="M", ranking=1200)
        self.assertEqual(player.name, "Doe")
        self.assertEqual(player.first_name, "John")
        self.assertEqual(player.birth_date, date(1990, 1, 1))
        self.assertEqual(player.gender, "M")
        self.assertEqual(player.ranking, 1200)

class TestChessTournament(unittest.TestCase):
    def test_creation_tournament(self):
        tournament = ChessTournament(name="Paris Open", location="Paris", start_date=date(2023, 6, 1), end_date=date(2023, 6, 7), number_of_rounds=4)
        self.assertEqual(tournament.name, "Paris Open")
        self.assertEqual(tournament.location, "Paris")
        self.assertEqual(tournament.start_date, date(2023, 6, 1))
        self.assertEqual(tournament.end_date, date(2023, 6, 7))
        self.assertEqual(tournament.number_of_rounds, 4)

class TestTournamentRound(unittest.TestCase):
    def test_add_match_to_round(self):
        round = TournamentRound(name="Round 1")
        player1 = Player(name="Doe", first_name="John", birth_date=date(1990, 1, 1), gender="M", ranking=1200)
        player2 = Player(name="Smith", first_name="Jane", birth_date=date(1991, 2, 2), gender="F", ranking=1300)
        match = ChessMatch(player1=player1, player2=player2)
        round.add_match(match)
        self.assertIn(match, round.matches)
        self.assertEqual(len(round.matches), 1)

class TestChessMatch(unittest.TestCase):
    def test_creation_match(self):
        player1 = Player(name="Doe", first_name="John", birth_date=date(1990, 1, 1), gender="M", ranking=1200)
        player2 = Player(name="Smith", first_name="Jane", birth_date=date(1991, 2, 2), gender="F", ranking=1300)
        match = ChessMatch(player1=player1, player2=player2)
        self.assertEqual(match.player1, player1)
        self.assertEqual(match.player2, player2)

if __name__ == "__main__":
    unittest.main()
