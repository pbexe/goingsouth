import random
from player import health, player_abilities
def battle(character):
    global health
    while character['health'] > 0 or health > 0:
        print("Choose your attack: ")
        for attack in player_abilities:
            print(attack['name'])