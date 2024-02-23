from tinydb import TinyDB, Query
from models import Match, Round

# Initialise la base de données TinyDB
db = TinyDB('dataJson/db.json')

# Tables pour différentes entités
players_table = db.table('players')
tournaments_table = db.table('tournaments')
rounds_table = db.table('rounds')
matches_table = db.table('matches')

# def register_player(name, first_name, birth_date, gender, ranking):
#     players_table.insert({'name': name, 'first_name': first_name, 'birth_date': birth_date, 'gender': gender, 'ranking': ranking})

def register_player(name,first_name):
    players_table.insert({'name': name, 'first_name': first_name})    

def get_all_players():
    return players_table.all()

def create_tournament(name, location, start_date, end_date, number_of_rounds):
    tournaments_table.insert({
        'name': name, 
        'location': location, 
        'start_date': start_date, 
        'end_date': end_date, 
        'number_of_rounds': number_of_rounds
    })


def add_round(tournament_name, round_name):
    rounds_table.insert({'tournament_name': tournament_name, 'round_name': round_name})

def add_match(tournament_name, round_name, player1, player2, result=None):
    matches_table.insert({'tournament_name': tournament_name, 'round_name': round_name, 'player1': player1, 'player2': player2, 'result': result})

def update_match_result(match_id, result):
    MatchQuery = Query()
    matches_table.update({'result': result}, MatchQuery.id == match_id)


def get_tournament_matches(tournament_name):
    Match = Query()
    return matches_table.search(Match.tournament_name == tournament_name)
