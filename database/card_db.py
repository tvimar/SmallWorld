import requests
import json
import urllib.parse
from pathlib import Path

def get_single_card(card_url_name: str):
    # The API endpoint
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + card_url_name

    file_name = card_url_name + ".json"
    file_path = "carddata/" + file_name

    my_file = Path(file_path)
    if my_file.is_file():
        #print("File exists")
        with open(file_path, 'r') as file:
            data = json.load(file)
        #print(data)
    else:
        response = requests.get(url)
        file = open(file_path, 'w')
        #file.write(response.json()["data"][0])
        json.dump(response.json()["data"][0], file)
        file.close
        #print(response.json().keys())
        data = response.json()["data"][0]
        #print(response.text)
    return data