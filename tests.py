import unittest
from game import *
from items import *
from map import *
from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestGameCore(unittest.TestCase):

    def setUp(self):
        pass

    def test_consumption(self):
        self.assertEqual(consume_item(item_cheeseburger), True)

    def test_list_generation(self):
        self.assertEqual(list_of_items([]), 'no items')
        self.assertEqual(list_of_items([item_cheeseburger]), 'cheese burger')
        self.assertEqual(list_of_items([item_cheeseburger, item_chicken]), 'cheese burger, chicken shish')

    def test_room_items(self):
        with captured_output() as (out, err):
            print_room_items(rooms['North Road'])
        output = out.getvalue().strip()
        self.assertEqual(output, 'There are no items here!')
        with captured_output() as (out, err):
            print_room_items(rooms['Fridge'])
        output = out.getvalue().strip()
        self.assertEqual(output, 'There is a bottle of beer, shot of vodka, a block of cheese here.')

    def test_inventory_items(self):
        with captured_output() as (out, err):
            print_inventory_items([])
        output = out.getvalue().strip()
        self.assertEqual(output, 'You have no items.')
        with captured_output() as (out, err):
            print_inventory_items([item_beer, item_id, item_cheeseburger])
        output = out.getvalue().strip()
        self.assertEqual(output, 'You have bottle of beer, driving licence, cheese burger.')

    def test_room_printing(self):
        with captured_output() as (out, err):
            print_room(rooms['Fridge'])
        output = out.getvalue().strip()
        self.assertEqual(output, 'FRIDGE\n\nThere was food in here before somebody had eaten it. You need to buy some more if you want to consume something apart from bottle of beer. Tesco everyday value beer.\n\nThere is a bottle of beer, shot of vodka here.')

    def test_room_printing(self):
        self.assertEqual(exit_leads_to(rooms['Fridge']['exits'], "west"), 'Uni Halls')
    def test_room_exit_printing(self):
        with captured_output() as (out, err):
            print_exit("south", "Uni Halls")
        output = out.getvalue().strip()
        self.assertEqual(output, 'GO SOUTH to Uni Halls.')

    def test_menu(self):
        with captured_output() as (out, err):
            print_menu(rooms['Fridge']['exits'], rooms['Fridge']['items'], [item_beer, item_mixed_grill] )
        output = out.getvalue().strip()
        self.assertEqual(output, """You can carry an extra 2.2kg of items.

You can:
GO WEST to Uni Halls.
TAKE BEER to take bottle of beer.
TAKE VODKA to take shot of vodka.
TAKE CHEESE to take a block of cheese.
DROP/INSPECT BEER to drop your bottle of beer.
DROP/INSPECT MIXEDGRILL to drop your mixed grill.
DRINK BEER to drink your bottle of beer.
EAT MIXEDGRILL to eat your mixed grill.
What do you want to do?""")

    
if __name__ == '__main__':
    unittest.main()