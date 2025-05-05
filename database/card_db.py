import requests
import json
import urllib.parse
from pathlib import Path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from api import ygoproapi

def get_single_card(card_url_name: str):
    file_name = card_url_name + ".json"
    file_path = "carddata/" + file_name

    my_file = Path(file_path)
    if my_file.is_file():
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        response = ygoproapi.get_card_info(card_url_name)
        file = open(file_path, 'w')
        json.dump(response.json()["data"][0], file)
        file.close
        data = response.json()["data"][0]
    return data