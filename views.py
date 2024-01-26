# for now just prints, but have to add methods for showing results
def display_player(player):
    print("Affichage du Joueur:")
    print(player)

def display_players(players):
    print("Liste des Joueurs:")
    for player in players:
        print(player)

def display_tournament(tournament):
    print("Détails du Tournoi:")
    print(tournament)
    for player in tournament.players:
        print(player)