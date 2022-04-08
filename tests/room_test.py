import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

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
        self.guest2 = Guest("Richard Taylor", 28, 20, "Club Tropicana")
        self.guest3 = Guest("Jane Morrell", 56, 60, "Let's Stay Together")
        self.guest4 = Guest("Nancy Muir", 42, 45, "That's Life")
        self.guest4 = Guest("Johnny Stash", 42, 45, "Fortunate Son")
        
    def test_room_has_name(self):
        self.assertEqual("Shibuya", self.room2.name)
    
    def test_room_has_till(self):
        self.assertEqual(85.00, self.room3.till)
        
    def test_room_can_add_songs(self):
        self.room2.add_song(self.song1)
        self.assertEqual(1, self.room2.song_count())

    def test_get_capacity(self):
        self.assertEqual(4, self.room1.capacity)
    
    def test_room_can_check_in(self):
        self.room2.check_in("Chikako Shiomi")
        self.assertEqual(1, len(self.room2.guests))
        self.assertEqual(0, len(self.room1.queue))

    def test_room_cannot_check_in_if_at_capacity(self):
        self.room1.check_in("Chikako Shiomi")
        self.room1.check_in("Richard Taylor")
        self.room1.check_in("Jane Morrell")
        self.room1.check_in("Nancy Muir")
        self.room1.check_in("Johnny Stash")
        self.assertEqual(4, len(self.room1.guests))
        self.assertEqual(1, len(self.room1.queue))

    def test_room_can_check_out(self):
        self.room2.check_in("Chikako Shiomi")
        self.room2.check_out("Chikako Shiomi")
        self.assertEqual(0, len(self.room2.guests))
    
    # def test_room_can_collect_entry_fee(self):
    #     self.room1.check_in("Chikako Shiomi")
    #     self.assertEqual(20, self.guest1.pay_fee())
    #     self.assertEqual(110, self.room1.collect_fee())
        
    # def test_pub_cannot_serve_drink(self):
    #     self.pub.add_drink(self.drink_1)
    #     self.pub.add_drink(self.drink_2)
    #     self.pub.serve(self.customer, self.drink_1)
    #     self.assertEqual(8.00, self.customer.wallet)
    #     self.assertEqual(102.00, self.pub.till)
    #     self.assertEqual(1, self.pub.drink_count())