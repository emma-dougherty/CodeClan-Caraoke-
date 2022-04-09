import unittest
from classes.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Asahi", 4.50)
    
    def test_bar_item_has_name(self):
        self.assertEqual("Asahi", self.bar.name)

    def test_bar_item_has_price(self):
        self.assertEqual(4.50, self.bar.price)