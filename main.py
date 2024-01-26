from controllers import PlayerController, TournamentController

def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    # Création des joueurs
    player1 = player_controller.add_player("Magnus Carlsen", 1, 30, "Norvège")
    player2 = player_controller.add_player("Fabiano Caruana", 2, 28, "USA")

    # Création d'un tournoi
    tournament = tournament_controller.create_tournament("Championnat du Monde", "Paris")
    tournament_controller.add_player_to_tournament(tournament, player1)
    tournament_controller.add_player_to_tournament(tournament, player2)

    # Affichage des détails du tournoi
    tournament_controller.show_tournament_details(tournament)

if __name__ == "__main__":
    main()