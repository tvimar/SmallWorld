import requests
import json
import urllib.parse
from pathlib import Path

# Test input acceptance
print("Getting all card data")
cards = []

monsters = {}

# The API endpoint
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

response = requests.get(url)
master_card_data = response.json()["data"]

for card in master_card_data:
    card_name = card["name"]
    url_name = urllib.parse.quote_plus(card_name)

    file_name = url_name + ".json"
    file_path = "carddata/" + file_name

    my_file = Path(file_path)
    if not my_file.is_file():
        file = open(file_path, 'w')
        json.dump(card, file)