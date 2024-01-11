
class Tournament:
    """Represents a chess tournament."""
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date
        self.rounds = []
        self.players = []

    def add_round(self, round):
        """Adds a round to the tournament."""
        self.rounds.append(round)

    def register_player(self, player):
        """Registers a player for the tournament."""
        self.players.append(player)


class Round:
    """Represents a round in a chess tournament."""
    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = []

    def add_match(self, match):
        """Adds a match to the round."""
        self.matches.append(match)


class Match:
    """Represents a match between two players."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def set_result(self, winner):
        """Sets the result of the match."""
        self.result = winner


class Player:
    """Represents a player in the tournament."""
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.score = 0

    def update_score(self, points):
        """Updates the player's score."""
        self.score += points
