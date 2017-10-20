#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from abilities import ABILITIES
import os
import sys
import time
import math
import random

gameover = False
gamecompleted = False

def print_ascii(file_name):
    """
    This function print out contents from a txt file each char at time.
    The parameter file_name is type string.
    When calling the func, the format of the argument should be "filename.txt"
    """

    with open("./ascii/" + file_name) as f:

        while True:
            line = f.readline()
            if not line:
                break
            else:
                for char in line:
                    sys.stdout.write(char)
                    time.sleep(0.0001)
                    sys.stdout.flush()


def add_ability(substance=False):
    """
    Adds a random ability to the player
    TODO:
    - Implement substances
    """
    for item in ABILITIES:
        if item not in player_abilities:
            player_abilities.append(ABILITIES[item])
            break


def consume_item(item):
    """
    Applies the effect of an item.
    Note: This does not actually delete the item.

    If the item is consumable, True is returned, else, False is returned.
    """
    global money
    if item['id'] == money:
        money += 10
        return True
    elif item['is_alcohol']:
        add_ability()
        print("You drank the " + item['name'])
        return True
    elif item['is_substance']:
        add_ability(True)
        print("You ate the " + item['name'])
        return True
    else:
        return False



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """
    if len(items) > 0:
        return ", ".join([item['name'] for item in items])
    else:
        return "no items"


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names.
    """
    items = []
    for item in room['items']:
        items.append(item)
    if len(room['items']) > 0:
        print("There is " + list_of_items(items) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.".
    """
    print("You have " + list_of_items(items) + ".\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). 
    """
    # Display room name
    print(room["name"].upper()+"\n")

    # Display room description
    print(room["description"]+"\n")
    if len(room['items']) > 0:
        print_room_items(room)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads.
    """
    return rooms[exits[direction]['name']]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can carry an extra "+ str(3-round(calculate_inventory_mass(), 1))+"kg of items.\n")
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        if item["cost"] != "":
            print("BUY " + item['id'].upper() + " to by the " + item['name'] + "for £" + str(item['cost']) +" .")
        else:
            print("TAKE " + item['id'].upper() + " to take " + item['name'] + ".")
    for item in inv_items:
        print("DROP/INSPECT " + item['id'].upper() + " to drop your " + item['name'] + ".")
    for item in inv_items:
        if item["is_substance"]:
            print("EAT " + item['id'].upper() + " to eat your " + item['name'] + ".")
        elif item["is_alcohol"]:
            print("DRINK " + item['id'].upper() + " to drink your " + item['name'] + ".")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if direction in current_room['exits']:
        current_room = rooms[current_room['exits'][direction]['name']]
        if 'person' in current_room:
            current_room['person'] = battle(current_room['person'])
    else:
        print("You cannot go there.")


def calculate_inventory_mass():
    total = 0
    for item in inventory:
        total += item['mass']
    return total



def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    found = False
    global inventory
    global current_room
    global money
    for index, item in enumerate(current_room['items']):
        if item['id'] == item_id:
            found = True
            if item['cost'] == "":            
                if item == item_money:
                    money += 10
                    del current_room['items'][index]
                elif calculate_inventory_mass() + item['mass'] <= 3:
                    inventory.append(item)
                    del current_room['items'][index]
                else:
                    print("You cannot carry any more")
            else:
                print("You can't take that, that would be stealing!")
    if found == False:
        print("You cannot take that")

def execute_buy(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    found = False
    global inventory
    global current_room
    global money
    for index, item in enumerate(current_room['items']):
        if item['id'] == item_id:
            found = True
            if calculate_inventory_mass() + item['mass'] <= 3 and money - item["cost"] >= 0:
                inventory.append(item)
                del current_room['items'][index]
                money -= item["cost"]
            else:
                print("You can't afford that" if money- item["cost"] < 0 else "You can't carry that")
    if found == False:
        print("You cannot take that")


def execute_consume(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    found = False
    global inventory
    global current_room
    for index, item in enumerate(inventory):
        if item['id'] == item_id:
            consumed = consume_item(item)
            if consumed:
                found = True
                del inventory[index]
    if found == False:
        print("You cannot consume that")




def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    found = False
    global inventory
    global current_room
    for index, item in enumerate(inventory):
        if item['id'] == item_id:
            found = True
            current_room['items'].append(item)
            del inventory[index]
    if found == False:
        print("You do not have this item")

def execute_inspect(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    found = False
    global inventory
    global current_room
    for index, item in enumerate(inventory):
        if item['id'] == item_id:
            found = True
            print(Item['description'])
            del inventory[index]
    if found == False:
        print("You do not have this item")



def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    consuming_words = ['eat', 'drink', 'consume', "down", "chug", "consume",
                       "scran","swallow","gulp","bite","ingest","masticate",
                       "chew","devour"]

    if 0 == len(command):
        return

    if command[0] in consuming_words:
        if len(command) > 1:
            execute_consume(command[1])
        else:
            print("Consume what?")
    elif command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "buy":
        if len(command) > 1:
            execute_buy(command[1])
        else:
            print("Buy what?")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_buy(command[1])
        else:
            print("Inspect what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction".
    """

    # Next room to go to
    return rooms[exits[direction]]


def battle(character):
    global health
    if character['health'] <= 0:
        return character
    clear_screen()
    print_ascii('battle.txt')
    print("A wild " + character['name'] + " has appeared")
    if len(player_abilities) == 0:
        print("You are not yet drunk enough to fight " + character['name'] + ". You must find alcohol in order to fight them.")
        print("Press ENTER to continue")
        input()
        clear_screen()
        return character
    # Main battle loop
    while character['health'] > 0:
        print("========================")
        print(character['name'].upper() + ":")
        print("Health: " + str(character['health']) + "hp")
        print("Abilities: " + ", ".join([item['name'] for item in character['abilities']]))
        print("========================")
        print("YOU:")
        print("Health: " + str(health))
        print("Abilities: " + ", ".join([item['name'] for item in player_abilities]))
        print("========================")
        print("\nYour turn to attack:")
        # Print the attacks
        for index, attack in enumerate(player_abilities):
            print(str(index + 1) + ". " + attack['name'])
        # Get the attack input
        while True:
            attack = int(input("> ")) - 1
            if player_abilities[attack]:
                character['health'] -= player_abilities[attack]['damage']
                print("You did "+ str(player_abilities[attack]['damage']) + " damage")
                break
            else:
                print("Invalid attack")
        # If they are still alive
        if character['health'] > 0:
            enemy_attack = random.choice(character['abilities'])
            health -= enemy_attack['damage']
            print("They did "+ str(player_abilities[attack]['damage']) + " damage")
            # If you dead
            if health <= 0:
                return character
    clear_screen()
    # You pick up their items
    inventory.extend(character['items'])
    print("You picked up " + list_of_items(character['items']))
    input("Press ENTER to continue")
    clear_screen()
    return character
    

def game_over():
    if gameover == True:
        print_ascii("gameover.txt")

def game_complete():
    if gamecompleted == True:
        print_ascii("gamecompleted.txt")

def cheat_checker(code):
    global inventory
    global money
    if code == "dollar":
        money += 1000
        print("You have been given £1000 for this entering this code.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# This is the entry point of our program
def main():
    clear_screen()
    print("You are about to embark on your journey. Press enter to begin")
    cheat_code = input()
    cheat_checker(cheat_code)
    clear_screen()
    # Main game loop
    while gameover == False or gamecompleted == False:
        # Display game status (room description, inventory etc.)
        print_ascii(current_room["ascii_art"])
        print_room(current_room)
        print("You are currently have " +("no money" if money == 0 else ("£" + str(money)))+".\n")
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)
        # Clear the screen
        clear_screen()
        # Execute the player's command
        execute_command(command)

        game_complete()
        game_over()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

