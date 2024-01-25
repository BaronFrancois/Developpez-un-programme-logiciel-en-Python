# logic between models and views, like add_round ? add_results ?
from models import Player
from views import display_player

class PlayerController:
    def __init__(self):
        self.players = []

    def add_player(self, name, ranking):
        player = Player(name, ranking)
        self.players.append(player)
        display_player(player)