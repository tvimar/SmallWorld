import requests
import json
import urllib.parse
from pathlib import Path

def get_card_info(card_url_name: str):
    # The API endpoint
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + card_url_name
    response = requests.get(url)
    return response