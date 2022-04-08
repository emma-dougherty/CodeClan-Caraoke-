import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Yokahama", 4, 10, 100)
        self.room2 = Room("Shibuya", 6, 12, 120)
        self.room3 = Room("Shinjuku", 10, 14, 85)
        self.room4 = Room("Kyoto", 15, 16, 70)

        self.song1 = Song("Know How", "Young MC")
        self.song2 = Song("Club Tropicana", "Wham!")
        self.song3 = Song("Fortunate Son", "Creedence Clearwater Revival")
        self.song4 = Song("Let's Stay Together", "Al Green")
        self.song5 = Song("That's Life", "Frank Sinatra")


        self.guest1 = Guest("Chikako Shiomi", 30, 30, "Know How")
        self.guest2 = Guest("Richard Taylor", 28, 10, "Club Tropicana")
        self.guest3 = Guest("Jane Morrell", 56, 60, "Let's Stay Together")
        self.guest4 = Guest("Nancy Muir", 42, 45, "That's Life")
        self.guest4 = Guest("Johnny Stash", 42, 45, "Fortunate Son")

    
    def test_guest_has_name(self):
        self.assertEqual("Chikako Shiomi", self.guest1.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(30.00, self.guest1.wallet)

    def test_guest_can_pay(self):
        room_fee = Room("Yokahama", 4, 10, 100)
        self.guest1.pay_fee(room_fee)
        self.assertEqual(20, self.guest1.wallet)

    def test_guest_cannot_pay(self):
        room_fee = Room("Kyoto", 15, 16, 70)
        self.guest2.pay_fee(room_fee)
        self.assertEqual(10, self.guest2.wallet)

    # def test_guest_cheers(self):
    #     self.guest1.cheer(self.room2)
    #     self.assertEqual("Know How", self.guest1.favourite_song)