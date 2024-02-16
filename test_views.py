import unittest
from io import StringIO
from unittest.mock import patch
import views

class TestDisplayPlayerList(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_player_list(self, mock_stdout):
        players = [
            type('Player', (object,), {'identifier': '1', 'name': 'Doe', 'first_name': 'John', 'elo_score': '1200', 'birth_date': '1990-01-01'}),
            type('Player', (object,), {'identifier': '2', 'name': 'Smith', 'first_name': 'Jane', 'elo_score': '1300', 'birth_date': '1991-02-01'})
        ]
        views.display_player_list(players)
        expected_output = """Player List:
1: Doe John, Elo: 1200, Date of Birth: 1990-01-01
2: Smith Jane, Elo: 1300, Date of Birth: 1991-02-01"""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

class TestDisplayTournamentDetails(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_tournament_details(self, mock_stdout):
        tournament = type('Tournament', (object,), {'name': 'Open International', 'location': 'Paris', 'start_date': '2024-01-01', 'end_date': '2024-01-10'})
        views.display_tournament_details(tournament)
        expected_output = "Tournament: Open International, Location: Paris, Date: 2024-01-01"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

class TestDisplayMatchPairings(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_match_pairings(self, mock_stdout):
        match_player1 = type('Player', (object,), {'name': 'Example1', 'first_name': 'Player1'})
        match_player2 = type('Player', (object,), {'name': 'Example2', 'first_name': 'Player2'})
        rounds = [type('Round', (object,), {'name': 'Round 1', 'matches': [(match_player1, match_player2)]})]
        views.display_match_pairings(rounds)
        expected_output = "Round 1: Match Pairings: Player 1 vs Player 2, Player 3 vs Player 4"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

class TestAnnounceWinner(unittest.TestCase):
   @patch('sys.stdout', new_callable=StringIO)
   def test_announce_winner(self, mock_stdout):
        player_example = type('Player', (object,), {'name': 'Doe', 'first_name': 'John', 'elo_score': 1200})
        tournament = type('Tournament', (object,), {'winner': 'John Doe', 'registered_players': [player_example]})
        views.announce_winner(tournament)
        expected_output = "The winner of the tournament is Doe John with an Elo of 1200."
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
