# to run the script
from controllers import PlayerController

def main():
    controller = PlayerController()
    controller.add_player("Magnus Carlsen", 1)
    # Ajoutez d'autres joueurs et testez d'autres fonctionnalités ici

if __name__ == "__main__":
    main()