import requests

api_key = 'b7f69f08-e0e7-48dd-a415-037ea1c18507'
word = 'kambing'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)