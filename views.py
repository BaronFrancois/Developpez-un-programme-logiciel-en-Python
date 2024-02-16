# for now just prints, but have to add methods for showing results
def display_player_list(players):
    print("Player List:")
    for player in players:
        print(f"{player.identifier}: {player.name} {player.first_name}, Elo: {player.elo_score}, Date of Birth: {player.birth_date}")

def display_tournament_details(tournament):
    print(f"Tournament: {tournament.name}")
    print(f"Location: {tournament.location}, Date: {tournament.start_date} to {tournament.end_date}")
    print("Players:")
    display_player_list(tournament.registered_players)

def display_match_pairings(rounds):
    for round in rounds:
        print(f"{round.name}:")
        for match in round.matches:
            print(f"{match.player1.name} {match.player1.first_name} vs {match.player2.name} {match.player2.first_name}")

def input_match_results():
    match_id = input("Enter match ID: ")
    result = input("Enter result (win: Player 1 wins, loss: Player 2 wins, draw: Draw): ")
    # Logic to find the match by ID and update match result here
    print("Result updated. Please integrate this logic with your actual match handling logic.")

def announce_winner(tournament):
    # Adjusted to use your attribute names
    winner = max(tournament.registered_players, key=lambda player: player.elo_score)
    print(f"The winner of the tournament is {winner.name} {winner.first_name} with an Elo of {winner.elo_score}.")

