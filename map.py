from items import *
from characters import characters

room_unihalls = {
    "name": "Uni Halls",

    "description": "Uni Hall description goes here",

    "exits": {"south": {"name": "Ty-Gwyn road", "cost": "0"}, "east": {"name": "Fridge", "cost": "0"}, "west": {"name": "Friend Room", "cost": "0"}, "North": {"name": "Your Room", "cost": "0"}},

    "items": [],

    "person": characters['flat_mate']
}

room_yourroom = {
    "name": "Your room",

    "description":
    "Your room looks like a complete mess right now. Maybe this is because of yesterday's party, maybe just because you had to submit 3 labs in the week - but right now the only thing that is clear is that there is no way anything can be found here",

    "exits": {"south": {"name": "Uni Halls", "cost": "0"}},

    "items": []
}

room_fridge = {
    "name": "Fridge",

    "description": "There was food before somebody had eaten it. You need to buy some more if you want to consume something apart from bottle of wine...actually do you really want?..",

    "exits": {"west": {"name": "Uni Halls", "cost": "0"}},

    "items": [item_beer]
}

room_tygwynroad = {
    "name": "Ty-Gwyn road",

    "description": "Quite big road though right now there are only a few people there - maybe because everyone is at Pryzm already?",

    "exits": {"south": {"name": "Pres", "cost": "10"}, "north": {"name": "Uni Halls", "cost": "0"}},

    "items" : []
}

room_friendsroom = {
    "name": "Friends Room",

    "description": "You finally found them, well done! Do you wish to have a drink to celebrate it right now?",

    "exits": {"east": {"name": "Uni Halls", "cost": "0"}},

    "items": [item_money]

}    

room_pres = {
    "name": "Pres",

    "description": "someone needs to write description",

    "exits": {"west": {"name": "Corridor", "cost": "0"}, "south": {"name": "North Road", "cost": "0"}},

    "items": [item_vodka]

}

room_corridor = {
    "name": "Corridor",

    "description": "someone needs to write a description",

    "exits": {"east": {"name": "Pres", "cost": "0"}, "south": {"name": "Pres Host Room", "cost": "0"}},

    "items": []

}


room_preshostroom = {
    "name": "Pres Host Room",

     "description": "someone needs to write a description",

    "exits": {"north": {"name": "Corridor", "cost": "0"}},

    "items": []

}

room_northroad = {
    "name": "North Road",

     "description": "someone needs to add a description",

    "exits": {"east": {"name": "Fattoush Restaurant", "cost": "0"}, "south": {"name": "Park Place", "cost": "0"}, "north": {"name": "Pres", "cost": "0"}},

    "items": []
}

room_fattoush = {
    "name": "Fattoush Restaurant",

     "description": "someone needs to add a description",

    "exits": {"west": {"name": "North Road", "cost": "0"}},

    "items": []
}

room_parkplace = {
    "name": "Park Place",

     "description": "someone needs to add a description",

    "exits": {"North": {"name": "North Road", "cost": "0"}, "west": {"name": "Cathays Park", "cost": "0"}, "south": {"name": "Pryzm", "cost": "0"}},

    "items": []
}

room_cathayspark = {
    "name": "Cathays Park",

    "description": "someone needs to add a description",

    "exits": {"east": {"name": "Park Place", "cost": "0"}},

    "items": []
}

room_pryzm = {
    "name": "Pryzm",

    "description": "someone needs to add a description",

    "exits": {"North": {"name": "Park Place", "cost": "0"}},

    "items": []
} 
    

rooms = {
    "Uni Halls": room_unihalls,
    "Your Room": room_yourroom,
    "Fridge": room_fridge,
    "Ty-Gywn road": room_tygwynroad,
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
