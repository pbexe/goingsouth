from abilities import ABILITIES
from items import *
characters = {
  "flat_mate": {
    "name": "Flat Mate",
    "atack speed":20,
    "health": 100,
    "abilities": [
      ABILITIES['drunken_insult'],
      ABILITIES['tac_chunder']
    ],
    'items': [
      item_beer,
      item_id
    ]
  },
  "pres_host": {
    "name": "Pres Host",
    "atack speed": 25,
    "health": 130,
    "abilities": [
      ABILITIES['dance'],
      ABILITIES['bottle']
    ],
    'items': [
      item_vodka,
      item_money
    ]
  },
  "homeless_man": {
    "name": "Homeless Man",
    "atack speed": 15,
    "health": 80,
    "abilities": [
      ABILITIES['steal'],
      ABILITIES['blackmail']
    ],
    'items': [
      item_shoes,
      item_sauce
    ]

  },
  "bouncer": {
    "name": "Bouncer",
    "atack speed": 20,
    "health": 180,
    "abilities": [
      ABILITIES['bottle'],
      ABILITIES['hadouken']
    ],
    'items': []
  }
}
