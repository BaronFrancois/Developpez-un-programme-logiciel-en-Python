from datetime import date
from typing import List, Optional

class MatchError(Exception):
    pass

class PairingError(Exception):
    pass

class Player:
    def __init__(self, name: str, first_name: str, birth_date: date, gender: str, ranking: int):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.points = 0  # Points accumulated in the tournament

class ChessTournament:
    def __init__(self, name: str, location: str, start_date: date, end_date: date, number_of_rounds: int = 4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.rounds: List['Round'] = []
        self.players: List[Player] = []

    def add_player(self, player: Player):
        if player in self.players:
            raise ValueError("The player is already registered for the tournament.")
        self.players.append(player)

    def generate_pairs(self):
        if len(self.players) % 2 != 0:
            raise PairingError("Odd number of players, cannot generate pairs.")
        # Logic to generate pairs following specific rules

class Round:
    def __init__(self, name: str):
        self.name = name
        self.matches: List['Match'] = []

    def add_match(self, match: 'Match'):
        if any(existing_match for existing_match in self.matches if match.player1 in (existing_match.player1, existing_match.player2) or match.player2 in (existing_match.player1, existing_match.player2)):
            raise MatchError("Players have already been paired.")
        self.matches.append(match)

class Match:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.result: Optional[str] = None  # Can be updated after the match
