# logic between models and views, like add_round ? add_results ?

from models import Player, Tournament
from views import display_player, display_players, display_tournament

class PlayerController:
    def __init__(self):
        self.players = []

    def add_player(self, name, ranking, age, country):
        player = Player(name, ranking, age, country)
        self.players.append(player)
        display_player(player)
        return player

    def show_all_players(self):
        display_players(self.players)

class TournamentController:
    def __init__(self):
        self.tournaments = []

    def create_tournament(self, name, location):
        tournament = Tournament(name, location)
        self.tournaments.append(tournament)
        return tournament
    
    def add_player_to_tournament(self, tournament, player):
        tournament.add_player(player)

    def add_player(self, name, ranking, age, country):
        player = Player(name, ranking, age, country)
        self.players.append(player)
        display_player(player)
        return player

    def show_tournament_details(self, tournament):
        display_tournament(tournament)