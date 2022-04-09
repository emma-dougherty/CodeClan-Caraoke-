import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from classes.bar import Bar

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Yokahama", 4, 10)
        self.room2 = Room("Shibuya", 6, 12)
        self.room3 = Room("Shinjuku", 10, 14)
        self.room4 = Room("Kyoto", 15, 16)

        self.song1 = Song("Know How", "Young MC")
        self.song2 = Song("Club Tropicana", "Wham!")
        self.song3 = Song("Fortunate Son", "Creedence Clearwater Revival")
        self.song4 = Song("Let's Stay Together", "Al Green")
        self.song5 = Song("That's Life", "Frank Sinatra")

        self.guest1 = Guest("Chikako Shiomi", 30, 30, "Know How", "Woohoo!")
        self.guest2 = Guest("Richard Taylor", 28, 4, "Club Tropicana", "Nice one!")
        self.guest3 = Guest("Jane Morrell", 56, 60, "Let's Stay Together", "Love this one!")
        self.guest4 = Guest("Nancy Muir", 42, 45, "That's Life", "Bonus!")
        self.guest4 = Guest("Johnny Stash", 42, 45, "Fortunate Son", "Hell yeah!")

        self.bar = Bar("Asahi", 4.50)

    def test_guest_has_name(self):
        self.assertEqual("Chikako Shiomi", self.guest1.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(30.00, self.guest1.wallet)

    def test_guest_can_pay(self):
        room_fee = Room("Yokahama", 4, 10)
        self.guest1.pay_fee(room_fee)
        self.assertEqual(20, self.guest1.wallet)

    def test_guest_cannot_pay(self):
        room_fee = Room("Kyoto", 15, 16)
        self.guest2.pay_fee(room_fee)
        self.assertEqual(4, self.guest2.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Know How", self.guest1.favourite_song)

    def test_guest1_cheers(self):
        self.room1.add_song(self.song1)
        room_playlist = self.room1.playlist
        self.guest1.cheer_for_favourite(room_playlist)
        self.assertEqual("Woohoo!", self.guest1.cheer)

    def test_guest2_cheers(self):
        self.room2.add_song(self.song2)
        room_playlist = self.room1.playlist
        self.guest2.cheer_for_favourite(room_playlist)
        self.assertEqual("Nice one!", self.guest2.cheer)

    def test_guest_can_buy_drink__decreases_money(self): 
        self.guest1.buy_drink(self.bar)
        self.assertEqual(25.50, self.guest1.wallet)

    def test_sufficient_food_funds__true_if_enough(self):
        self.assertEqual(True, self.guest1.sufficient_funds(self.bar))
    
    def test_sufficient_food_funds__false_if_not_enough(self):
        self.assertEqual(False, self.guest2.sufficient_funds(self.bar))

    