class Player:
    def __init__(self, name, ranking, age, country):
        self.name = name
        self.ranking = ranking
        self.age = age
        self.country = country

    def __str__(self):
        return f"{self.name}, Classement: {self.ranking}, Âge: {self.age}, Pays: {self.country}"

class Tournament:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"Tournament: {self.name} à {self.location}, Joueurs: {len(self.players)}"