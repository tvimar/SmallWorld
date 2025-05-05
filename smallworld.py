import requests
import json
import urllib.parse
from pathlib import Path

from database import card_db 
from database import deck_db

def main():
    print("Would you like to use a save deck or use a new one? (Y/N)")
    command = input()

    while command != 'Y' and command != 'N':
        print("Please enter a valid command")
        command = input()

    deck = []

    if command == 'Y':
        deck = deck_db.import_decklist_from_file()
    elif command == 'N':
        print("Taking input")
        cards = []

        inp = input()       # Get the input
        while inp != "":        # Loop until it is a blank line
            cards.append(inp)
            inp = input()   # Get the input again

        # process input as deck
        for card in cards:
            if card[0] != '1' and card[0] != '2' and card[0] != '3':
                continue
            solo_name = card.partition(' ')[2]
            deck.append(solo_name)

        print("Would you like to save this decklist? Type 'Y' if yes, anything else if no")
        command = input()

        if command == 'Y':
            deck_db.save_decklist(deck)
        else:
            print("Not saving decklist")
            

    monsters = {}

    for card in deck:
        url_name = urllib.parse.quote_plus(card)

    # card_db function
        data = card_db.get_single_card(url_name)

        card_data = data

        card_name = card_data['name']
        card_type = card_data['frameType']
        if card_type != "spell" and card_type != "trap" and card_type != "xyz" and card_type != "link" and card_type != "synchro" and card_type != "fusion" and card_type != "fusion_pendulum" and card_type != "xyz_pendulum":
            monsters[card_name] = card_data

# next init the bridge dictionary
    bridges = {}

    for monster_name in monsters:
        monster_bridge = set()
        for bridge in monsters:
        # compare stats
            matching_stats = 0

            if(monsters[monster_name]['race'] == monsters[bridge]['race']):
                matching_stats += 1
            if(monsters[monster_name]['atk'] == monsters[bridge]['atk']):
                matching_stats += 1
            if(monsters[monster_name]['def'] == monsters[bridge]['def']):
                matching_stats += 1
            if(monsters[monster_name]['level'] == monsters[bridge]['level']):
                matching_stats += 1
            if(monsters[monster_name]['attribute'] == monsters[bridge]['attribute']):
                matching_stats += 1

            if matching_stats == 1:
                monster_bridge.add(bridge)
        bridges[monster_name] = monster_bridge

    # input loop
    while True:
    # get start name
        print("Type EXACT starting monster name")
        starter = input()       # Get the input

        if starter not in bridges.keys():
            print("Starter not found")
            exit

    # get end name
        print("Type EXACT ending monster name")
        ender = input()       # Get the input

        if ender not in bridges.keys():
            print("Ender not found")
            exit

        final_bridges = []

        for potential_bridge in bridges[starter]:
            if ender in bridges[potential_bridge]:
                final_bridges.append(potential_bridge)

        print("Number of bridges are {0}".format(len(final_bridges)))
        for bridge in final_bridges:
            print(bridge)

        print("Would you do another bridge search? (Y/N)")
        command = input()
        while command != 'Y' and command != 'N':
            print("Please enter a valid command")
            command = input()
        if command == 'N':
            break
    

main()