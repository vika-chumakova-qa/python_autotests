import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "email",
    "password": "password"
}
body_confirm = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бабл",
    "photo": "https://dolnikov.ru/pokemons/albums/032.png"
}


#запрос для регистрации тренера
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''
#запрос для подтверждения аккаунта тренера
'''response_confirm = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirm)
print(response_confirm.text)'''
#запрос для создания покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER,  json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']

#запрос для поимки покемона в покебол
body_add = {
    "pokemon_id": response_create.json()['id']
}
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,  json = body_add)
print(response_add.text)
#запрос для смены имени покемона
body_change = {
    "pokemon_id": response_create.json()['id'],
    "name": "Nosik",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER,  json = body_change)
print(response_change.text)

