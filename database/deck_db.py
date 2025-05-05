import json
from pathlib import Path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def import_decklist_from_file():
    deck = []
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    file = open(filename)
    for line in file:
        card = line.strip()
        deck.append(card)
    return deck

def save_decklist(deck: list):
    print("Please type filename:")
    deck_file_name = input()
    file_path = "decklists/" + deck_file_name

    Path('decklists/').mkdir(parents=True, exist_ok=True) 
    my_file = Path(file_path)
    if my_file.is_file():
        print("Deck already exists, not saving")
    else:
        file = open(file_path, 'w')
        for card in deck:
            file.write(card + "\n")
        file.close