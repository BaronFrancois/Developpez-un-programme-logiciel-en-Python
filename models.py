from datetime import datetime
import random
from datetime import datetime
import random

class Player:
    def __init__(self, name, first_name, birth_date, identifier, elo_score):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.identifier = identifier
        self.elo_score = elo_score

# permet de calculer le score ELO qui donne une estimation de la force d'un joueur selon s'il gagne, perd ou fait match nul
    def update_elo_score(self, opponent_score, result):
        # Calcul de l'ajustement basé sur les scores ELO originaux car de base je prenais le score modifié après le calcul du Elo ex:1010 au lieu de 1000
        ajustement = (opponent_score - self.elo_score) * 0.1

        if result == "win":
            self.elo_score += 10
        elif result == "loss":
            self.elo_score -= 10
        elif result == "draw":
            self.elo_score += 5

        self.elo_score += ajustement

# possibilité de modifier ses informations
    def update_information(self, name, first_name, birth_date, identifier):
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.identifier = identifier

class Tournament:
    def __init__(self, name, location, start_date, end_date, number_of_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round_number = 1
        self.rounds = []
        self.initial_elo = 1000  # Score ELO de départ pour tous les joueurs
        self.registered_players = []
        self.description = description
        

    def register_player(self, player):
        # Initialisez le score ELO du joueur pour le tournoi
        player.tournament_elo = self.initial_elo
        self.registered_players.append(player)

# permet de générer des pairs de joueurs pour les matchs de manière aléatoire pour la première manche et ensuite en fonction de leur score ELO
    def pair_players(self):
        # Si nombre impair de joueurs
        if len(self.registered_players) % 2 != 0:
            bye_player = random.choice(self.registered_players)
            self.registered_players.remove(bye_player)
            
            # Mettre à jour le score ELO pour le bye, comme une victoire contre un score ELO de 1000
            bye_player.update_elo_score(1000, "win")

        if self.current_round_number == 1:
            random.shuffle(self.registered_players)
        else:
            self.registered_players.sort(key=lambda player: player.elo_score, reverse=True)

        matches = []
        for i in range(0, len(self.registered_players), 2):
            player1 = self.registered_players[i]
            player2 = self.registered_players[i+1]
            match = Match(player1, player2)
            matches.append(match)

        round = Round(f"Round {self.current_round_number}", datetime.now(), None)
        round.matches = matches
        self.rounds.append(round)

# modifie le score ELO des joueurs en fonction du résultat du match
    def update_results(self, match, result):
        match.set_result(result)
        if result == "win":
            match.player1.update_elo_score(match.player2.elo_score, "win")
            match.player2.update_elo_score(match.player1.elo_score, "loss")
        elif result == "loss":
            match.player1.update_elo_score(match.player2.elo_score, "loss")
            match.player2.update_elo_score(match.player1.elo_score, "win")
        elif result == "draw":
            match.player1.update_elo_score(match.player2.elo_score, "draw")
            match.player2.update_elo_score(match.player1.elo_score, "draw")

# verifie s'il y a encore des manches à jouer
    def progress_round(self):
        if self.current_round_number < self.number_of_rounds:
            self.current_round_number += 1
            self.pair_players()
        else:
            self.end_tournament()

# determine le gagnant selon son ELO, il est égale pour tous pour la premiere manche.
    def end_tournament(self):
        winner = max(self.registered_players, key=lambda player: player.elo_score)
        print(f"The winner of the tournament is {winner.name} {winner.first_name}!")


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = ""
        self.elo_gain_player1 = 0
        self.elo_gain_player2 = 0

    def set_result(self, result):
        self.result = result
        old_elo_player1 = self.player1.elo_score
        old_elo_player2 = self.player2.elo_score

        if result == "win":
            self.player1.update_elo_score(self.player2.elo_score, "win")
            self.player2.update_elo_score(self.player1.elo_score, "loss")
        elif result == "loss":
            self.player1.update_elo_score(self.player2.elo_score, "loss")
            self.player2.update_elo_score(self.player1.elo_score, "win")
        elif result == "draw":
            self.player1.update_elo_score(self.player2.elo_score, "draw")
            self.player2.update_elo_score(self.player1.elo_score, "draw")

        # Calculer le gain ou la perte en ELO
        self.elo_gain_player1 = self.player1.elo_score - old_elo_player1
        self.elo_gain_player2 = self.player2.elo_score - old_elo_player2

class Round:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = []
# a modifier il ne faut pas qu'il y ai de doublons de matchs, un message d'erreur est inutile au final. Peut être plutot relancer la génération de matchs ?
    def add_match(self, match):
        for existing_match in self.matches:
            if (existing_match.player1 == match.player1 and existing_match.player2 == match.player2) or (existing_match.player1 == match.player2 and existing_match.player2 == match.player1):
                raise ValueError("les joueurs se sont déja rencontrés.")
        self.matches.append(match)
