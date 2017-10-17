from items import *

room_unihalls = {
    "name": "Uni Halls",

##    "description": someone needs to write description,

    "exits": {"south": {"name": "Ty-Gwyn road", "cost": "0"}, "east": {"name": "Fridge", "cost": "0"}, "west": {"name": "Friend Room", "cost": "0"}, "North": {"name": "Your Room", "cost": "0"}},

    "items": []
}

room_yourroom = {
    "name": "Your room",

##    "description": someone needs to write description,

    "exits": {"south": {"name": "Uni Halls", "cost": "0"}},

    "items": []
}

room_fridge = {
    "name": "Fridge",

##   "description": someone needs to write description,

    "exits": {"west": {"name": "Uni Halls", "cost": "0"}},

    "items": [beer]
}

room_tygwynroad = {
    "name": "Ty-Gwyn road",

##    "description": someone needs to write description,

    "exits": {"south": {"name": "Pres", "cost": "10"}, "north": {"name": "Uni Halls", "cost": "0"}},

    "items" = []
}

room_friendsroom = {
    "name": "Friends Room",

##   "description": someone needs to add a description,

    "exits": {"east": {"name": "Uni Halls", "cost": "0"}},

    "items": [money]

}    

room_pres = {
    "name": "Pres",

##  "description": someone needs to write description,

    "exits": {"west": {"name": "Corridor", "cost": "0"}, "south": {"name": "North Road", "cost": "0"}},

    "items": [vodka]

}

room_corridor = {
    "name": "Corridor",

##  "description": someone needs to write a description,

    "exits": {"east": {"name": "Pres", "cost": "0"}},

    "items": []

}


room_preshostroom = {
    "name": "Pres Host Room",

##  "description": someone needs to write a description,

    "exits": {"north": {"name": "Corridor", "cost": "0"}},

    "items": []

}

room_corridor = {
    "name" = "Corridor",

##  "description": someone needs to add a description,

    "exits": {"west": {"name": "Pres", "cost": "0"},

    "items": []
              
}

    

rooms = {
    "Uni Halls": room_unihalls,
    "Your Room": room_yourroom,
    "Fridge": room_fridge,
    "Ty-Gywn road": room_tygwynroad,
    "Friends Room": room_friendsroom,
    "Pres": room_pres
    "Corridor": room_corridor
    "Pres Host Room": room_preshostroom
}
