# add classes
class Player:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking

    def __str__(self):
        return f"{self.name}, Classement: {self.ranking}"