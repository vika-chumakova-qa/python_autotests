import requests
import pytest 

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
trainer_id = 4058

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons', params={'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url= f'{URL}/trainers', params={'trainer_id' : trainer_id})
    assert response_get.json()["data"][0]["id"] ==  "4058"
