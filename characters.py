from abilities import ABILITIES
from items import *
characters = {
    "flat_mate": {
        "name": "Flat Mate",
        "health": 100,
        "abilities": [
            ABILITIES['drunken_insult'],
            ABILITIES['tac_chunder']
        ],
        'items': [
            item_beer,
            item_id
        ]
    }


    ,"pres_host" : {
        "name": "Pres Host",
        "health": 130,
        "abilities": [
            ABILITIES['dance'],
            ABILITIES['bottle']
        ],
        'items': [
            item_vodka,
            item_money
        ]
    }
    ,"homeless_man": {
        "name": "Homeless Man",
        "health": 80,
        "abilities": [
            ABILITIES['steal'],
            ABILITIES['blackmail']
        ],
        'items': [
            item_shoes,
            item_sauce
        ]

    }

}


