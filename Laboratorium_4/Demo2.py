import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['crypto_db']
cryptocurrencies_collection = db['cryptocurrencies']

url = "https://api.geckoterminal.com/api/v2/networks"
response = requests.get(url)
data = response.json()

cryptocurrencies = []
for network in data.get('data', []):
    crypto_info = {
        "id": network.get('id'),
        "type": network.get('type'),
        "name": network.get('attributes').get('name')
    }
    cryptocurrencies.append(crypto_info)

cryptocurrencies_collection.insert_many(cryptocurrencies)



