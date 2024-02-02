import unittest
from models import Player, Tournament
from datetime import datetime
import random

# ○ créer quelques joueurs ;
# ○ créer un tour, ajouter les joueurs ;
# ○ voir comment les joueurs sont associés (points) ;
# ○ gagner/perdre des matchs de manière aléatoire ;
# ○ vérifier que les données des modèles sont correctement mises à
# jour.

class TestTournamentSimulation(unittest.TestCase):
    def setUp(self):
        # Création de quelques joueurs
        self.player1 = Player("Doe", "John", datetime(1990, 1, 1), "1", 1200)
        self.player2 = Player("Roe", "Jane", datetime(1985, 2, 2), "2", 1300)
        self.player3 = Player("Moe", "Joe", datetime(1980, 3, 3), "3", 1100)
        self.players = [self.player1, self.player2, self.player3]

        # Création d'un tournoi et ajout des joueurs
        self.tournament = Tournament("Spring Open", "New York", datetime(2022, 4, 1), datetime(2022, 4, 7))
        for player in self.players:
            self.tournament.register_player(player)

    def simulate_match(self, player1, player2):
        # Simuler un résultat de match aléatoire
        result = random.choice(["win", "loss", "draw"])
        print(f"Match entre {player1.name} et {player2.name}: {result.upper()}")
        if result == "win":
            player1.update_elo_score(player2.elo_score, "win")
            player2.update_elo_score(player1.elo_score, "loss")
        elif result == "loss":
            player1.update_elo_score(player2.elo_score, "loss")
            player2.update_elo_score(player1.elo_score, "win")
        else:  # draw
            player1.update_elo_score(player2.elo_score, "draw")
            player2.update_elo_score(player1.elo_score, "draw")
        print(f"Après le match, le score ELO de {player1.name} est {player1.elo_score}")
        print(f"Après le match, le score ELO de {player2.name} est {player2.elo_score}\n")

    def test_tournament_simulation(self):
        # Simuler des matchs entre tous les joueurs
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                self.simulate_match(self.players[i], self.players[j])

        # Vérifier que les scores ELO ont été mis à jour
        print("Scores ELO finaux après le tournoi :")
        for player in self.players:
            print(f"{player.name}: {player.elo_score}")
            self.assertNotEqual(player.elo_score, 1200)  # En supposant que tous les joueurs n'ont pas commencé avec 1200

if __name__ == '__main__':
    unittest.main()
