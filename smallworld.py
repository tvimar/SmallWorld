import requests
import json
import urllib.parse
from pathlib import Path

# Test input acceptance
print("Taking input")
cards = []

inp = input()       # Get the input
while inp != "":        # Loop until it is a blank line
    cards.append(inp)
    inp = input()   # Get the input again

monsters = {}

for card in cards:
    if card[0] != '1' and card[0] != '2' and card[0] != '3':
        continue
    solo_name = card.partition(' ')[2]
    url_name = urllib.parse.quote_plus(solo_name)

    # The API endpoint
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + url_name

    file_name = url_name + ".json"
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

    card_data = data

    card_name = card_data['name']
    #print("Card name is {0}".format(card_name))
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