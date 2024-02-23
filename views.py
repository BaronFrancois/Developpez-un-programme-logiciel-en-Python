import controllers

def main_menu():
    print("Welcome to the Chess Tournament Manager CLI")
    print("1. Register Player")
    print("2. View Players")
    print("3. Create Tournament")
    print("4. Start Next Round")
    print("5. Enter Match Results")
    print("6. View Tournament Standings")
    print("7. Exit")
    choice = input("Please choose an option (1-7): ")
    return choice

def register_player():
    print("Register a new Player")
    name = input("Enter player's name: ")
    first_name = input("Enter player's first name: ")
    # birth_date = input("Enter player's birth date (YYYY-MM-DD): ")
    # gender = input("Enter player's gender (M/F): ")
    # ranking = input("Enter player's ranking: ")
    # controllers.register_player(name, first_name, birth_date, gender, ranking)
    controllers.register_player(name, first_name)
    print(f"Player {first_name} {name} registered successfully.")

def view_players():
    print("List of Registered Players:")
    players = controllers.get_all_players()
    for player in players:
        print(f"{player['first_name']} {player['name']}")

def create_tournament():
    print("Create a new Chess Tournament")
    name = input("Enter tournament name: ")
    location = input("Enter tournament location: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    number_of_rounds = input("Enter number of rounds: ")
    controllers.create_tournament(name, location, start_date, end_date, number_of_rounds)
    print(f"Tournament {name} created successfully.")

def start_next_round():
    print("Starting next round...")
    

def enter_match_results():
    print("Enter Match Results")
    match_id = input("Enter match ID: ")
    result = input("Enter result: ")

def view_tournament_standings():
    print("Tournament Standings")
    tournament_name = input("Enter tournament name: ")

def exit_application():
    print("Exiting the application. Goodbye!")
    exit()

def main_menu_loop():
    while True:
        user_choice = main_menu()
        if user_choice == '1':
            register_player()
        elif user_choice == '2':
            view_players()
        elif user_choice == '3':
            create_tournament()
        elif user_choice == '4':
            start_next_round()
        elif user_choice == '5':
            enter_match_results()
        elif user_choice == '6':
            view_tournament_standings()
        elif user_choice == '7':
            exit_application()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu_loop()
