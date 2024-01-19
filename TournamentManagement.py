from datetime import datetime
import json
import random

class Player:
    """Represents a player in the tournament."""
    def __init__(self, name, ranking, date_of_birth):
        self.name = name
        self.ranking = ranking
        self.score = 0
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    def update_score(self, points):
        """Updates the player's score."""
        print(f"Mise à jour du score pour {self.name}, ajout de {points} points.")
        self.score += points

class Match:
    """Represents a match between two players."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def set_result(self, winner):
        """Sets the result of the match."""
        self.result = winner

    def update_match_results(self, match_results):
        """Updates the results of the matches in the round."""
        for match, winner in match_results.items():
            match.set_result(winner)
            winner.update_score(1)  # Assuming a simple scoring system

class Tournament:
    """Represents a chess tournament."""
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date
        self.rounds = []
        self.players = []
        self.match_history = set()

    def add_round(self, round):
        """Adds a round to the tournament."""
        self.rounds.append(round)

    def register_player(self, player):
        """Registers a player for the tournament."""
        self.players.append(player)

    def create_round(self):
        """Creates a new round in the tournament."""
        round_number = len(self.rounds) + 1
        new_round = Round(round_number, self)
        self.add_round(new_round)
        return new_round

    def schedule_matches(self, round):
        """Schedules matches for a round with random pairings."""
        shuffled_players = random.sample(self.players, len(self.players))
        for i in range(0, len(shuffled_players), 2):
            player1, player2 = shuffled_players[i], shuffled_players[i+1]
            if (player1, player2) not in self.match_history and (player2, player1) not in self.match_history:
                match = Match(player1, player2)
                round.add_match(match)
                self.match_history.add((player1, player2))

    def record_match_results(self):
        """Records the results of matches in the current round."""
        if self.rounds:
            current_round = self.rounds[-1]
            input_match_results(current_round)
        else:
            print("Aucun round en cours.")
    
    def load_players_from_json(self, file_path):
        """Loads players from a JSON file."""
        with open(file_path, 'r') as file:
            players_data = json.load(file)
        for player_data in players_data:
            player = Player(player_data['name'], player_data['ranking'])
            print(f"Enregistrement du joueur {player.name}.")
            self.register_player(player)

    def save_to_json(self, file_path):
        """Saves the tournament data to a JSON file."""
        tournament_data = {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'players': [{'name': player.name, 'ranking': player.ranking} for player in self.players]
        }
        with open(file_path, 'w') as file:
            json.dump(tournament_data, file, indent=4)


class Round:
    """Represents a round in a chess tournament."""
    def __init__(self, round_number, tournament):
        self.round_number = round_number 
        self.tournament = tournament
        self.matches = []

    def add_match(self, match):
        """Adds a match to the round."""
        self.matches.append(match)

def input_match_results(round):
    print("\nSaisie des résultats du Round", round.round_number)
    for match in round.matches:
        print(f"Match: {match.player1.name} vs {match.player2.name}")
        winner_name = input("Entrez le nom du gagnant (laissez vide en cas de match nul) : ")
        if winner_name:
            winner = next((player for player in round.tournament.players if player.name == winner_name), None)
            if winner:
                match.set_result(winner)
                winner.update_score(1)  # Ajout d'un point pour la victoire
                print(f"Résultat enregistré : {winner_name} gagne.")
            else:
                print("Joueur non trouvé. Vérifiez le nom et réessayez.")
        else:
            print("Match nul enregistré.")    


# A modifier (pour tester)
          
def main():
    # Création d'un tournoi
    tournament = Tournament("Championnat d'Echecs", "Paris", "2024-07-15")

    # Ajout de quelques joueurs
    tournament.register_player(Player("Alice", 1, "1990-01-01"))
    tournament.register_player(Player("Bob", 2, "1985-06-15"))
    tournament.register_player(Player("Charlie", 3, "1992-03-22"))
    tournament.register_player(Player("Diana", 4, "1995-11-08"))

    # Démarrer un round
    round1 = tournament.create_round()
    tournament.schedule_matches(round1)

    # Affichage des matchs planifiés
    print("Matchs du Round 1 :")
    for match in round1.matches:
        print(f"{match.player1.name} vs {match.player2.name}")


    # Affichage des informations du tournoi et des joueurs
    print(f"Tournoi : {tournament.name}, Lieu : {tournament.location}, Date : {tournament.date}")
    for player in tournament.players:
        print(f"Joueur : {player.name}, Classement : {player.ranking}, Score : {player.score}")

if __name__ == "__main__":
    main()
