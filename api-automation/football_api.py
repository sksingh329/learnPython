import requests


def get_football_competitions():
    competitions_uri = "http://api.football-data.org/v2/competitions/"
    response = requests.get(competitions_uri)
    json_response = response.json()
    return json_response['count']


get_football_competitions()
