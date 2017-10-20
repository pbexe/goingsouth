from items import *
from characters import characters

room_unihalls = {
    "name": "Uni Halls",

    "description": "University Halls: slap bang in the middle of nowhere. The only thing going for it the free bus service. Oh, and the close proximity of Roath Park.",

    "exits": {"south": {"name": "Ty-Gwyn road", "cost": "0"}, "east": {"name": "Fridge", "cost": "0"}, "west": {"name": "Friends Room", "cost": "0"}, "north": {"name": "Your Room", "cost": "0"}},

    "items": [],

    "person": characters['flat_mate'],

    "ascii_art": ""
}

room_yourroom = {
    "name": "Your room",

    "description":
    "Your room looks like a complete mess right now. Maybe this is due to yesterday's party, maybe just because you had to submit 3 labs in the week - but right now the only thing that is clear is that there is no way anything can be found here",

    "exits": {"south": {"name": "Uni Halls", "cost": "0"}},

    "items": [],

    "character": [],

    "ascii_art": "room.txt"
}

room_fridge = {
    "name": "Fridge",

    "description": "There was food in here before somebody had eaten it. You need to buy some more if you want to consume something apart from bottle of beer. Tesco everyday value beer.",

    "exits": {"west": {"name": "Uni Halls", "cost": "0"}},

    "items": [item_beer],

    "character": [],

    "ascii_art": "fridge.txt"
}

room_tygwynroad = {
    "name": "Ty-Gwyn road",

    "description": "Quite a big road, although right now there are only a few people there - maybe because everyone is at Pryzm already?",

    "exits": {"south": {"name": "Pres", "cost": "10"}, "north": {"name": "Uni Halls", "cost": "0"}},

    "items" : [],

    "character": [],

    "ascii_art": ""
    
}

room_friendsroom = {
    "name": "Friends Room",

    "description": "You finally found them, well done! Do you wish to have a drink to celebrate it right now?",

    "exits": {"east": {"name": "Uni Halls", "cost": "0"}},

    "items": [item_money],

    "character": [],

    "ascii_art": "room.txt"

}    

room_pres = {
    "name": "Pres",

    "description": "God, Talybont North is a complete dive. You can barely fit 6 people in the kitchen.",

    "exits": {"west": {"name": "Corridor", "cost": "0"}, "south": {"name": "North Road", "cost": "0"}},

    "items": [item_vodka],

    "character": [],

    "ascii_art": ""

}

room_corridor = {
    "name": "Corridor",

    "description": "It's a corridor. No description needed.",

    "exits": {"east": {"name": "Pres", "cost": "0"}, "south": {"name": "Pres Host Room", "cost": "0"}},

    "items": [],

    "character": ['pres_host'],

    "ascii_art": ""

}


room_preshostroom = {
    "name": "Pres Host Room",

     "description": "The rather acrid smell of booze is plentiful. In typical student fashion, the floor is not visible.",

    "exits": {"north": {"name": "Corridor", "cost": "0"}},

    "items": [],

    "character": [],

    "ascii_art": ""

}

room_northroad = {
    "name": "North Road",

     "description": "North road is deceptively long. Crossing the road drunk is an accident waiting to happen. On this road you will find the Fattoush Restaurant.",

    "exits": {"east": {"name": "Fattoush Restaurant", "cost": "0"}, "south": {"name": "Park Place", "cost": "0"}, "north": {"name": "Pres", "cost": "0"}},

    "items": [],

    "character": [],

    "ascii_art": ""
}

room_fattoush = {
    "name": "Fattoush Restaurant",

    "description": "What's not to love about cheap food after, or during, a night out?",

    "exits": {"west": {"name": "North Road", "cost": "0"}},

    "items": [item_sauce, item_cheeseburger, item_mixed_grill, item_chicken],

    "character": [],

    "ascii_art": ""

}

room_parkplace = {
    "name": "Park Place",

    "description": "It's Bin day, the stench is awful here.",

    "exits": {"north": {"name": "North Road", "cost": "0"}, "west": {"name": "Cathays Park", "cost": "0"}, "south": {"name": "Pryzm", "cost": "0"}},

    "items": [],

    "character": [],

    "ascii_art": ""

}

room_cathayspark = {
    "name": "Cathays Park",

    "description": "someone needs to add a description",

    "exits": {"east": {"name": "Park Place", "cost": "0"}},

    "items": [],

    "person": characters['homeless_man'],

    "ascii_art": ""

}

room_pryzm = {
    "name": "Pryzm",

    "description": "Please visit https://www.pryzm.co.uk/cardiff for more details.",

    "exits": {"north": {"name": "Park Place", "cost": "0"}},

    "items": [],

    "person": characters['bouncer'],

    "ascii_art": ""

} 
    

rooms = {
    "Uni Halls": room_unihalls,
    "Your Room": room_yourroom,
    "Fridge": room_fridge,
    "Ty-Gwyn road": room_tygwynroad,
    "Friends Room": room_friendsroom,
    "Pres": room_pres,
    "Corridor": room_corridor,
    "Pres Host Room": room_preshostroom,
    "North Road": room_northroad,
    "Fattoush Restaurant": room_fattoush,
    "Park Place": room_parkplace,
    "Cathays Park": room_cathayspark,
    "Pryzm": room_pryzm,
}
