import requests
import json
import urllib.parse
from pathlib import Path

def get_single_card(card_url_name: str):
    # The API endpoint
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + card_url_name
    response = requests.get(url)
    return response