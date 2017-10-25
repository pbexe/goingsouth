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
 
if __name__ == '__main__':
    unittest.main()