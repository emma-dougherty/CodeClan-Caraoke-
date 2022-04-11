import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from classes.bar import Bar

class TestRoom(unittest.TestCase):

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
        self.guest2 = Guest("Richard Taylor", 28, 10, "Club Tropicana", "Nice one!")
        self.guest3 = Guest("Jane Morrell", 56, 60, "Let's Stay Together", "Love this one!")
        self.guest4 = Guest("Nancy Muir", 42, 45, "That's Life", "Bonus!")
        self.guest5 = Guest("Johnny Stash", 42, 45, "Fortunate Son", "Hell yeah!")

        self.bar = Bar("Asahi", 4.50)
        
    def test_room_has_name(self):
        self.assertEqual("Shibuya", self.room2.name)
    
    def test_room_has_till(self):
        self.assertEqual(0, self.room3.till)
        
    def test_room_can_add_songs(self):
        self.room2.add_song(self.song1)
        self.assertEqual(1, self.room2.song_count())

    def test_get_capacity(self):
        self.assertEqual(4, self.room1.capacity)
    
    def test_room_can_check_in(self):
        self.room2.check_in( self.guest1,self.room1)
        self.assertEqual(1, len(self.room2.guests))
        self.assertEqual(0, len(self.room1.queue))

    def test_room_cannot_check_in_if_at_capacity(self):
        self.room1.check_in(self.guest1,self.room1)
        self.room1.check_in(self.guest2, self.room1)
        self.room1.check_in(self.guest3, self.room1)
        self.room1.check_in(self.guest4, self.room1)
        self.room1.check_in(self.guest5, self.room1)
        self.assertEqual(4, len(self.room1.guests))
        self.assertEqual(1, len(self.room1.queue))

    def test_room_can_check_out(self):
        self.room2.check_in(self.guest1,self.room1)
        self.room2.check_out(self.guest1)
        self.assertEqual(0, len(self.room2.guests))
    
    def test_room_can_collect_entry_fee_if_enough_capacity(self):
        self.room1.check_in(self.guest1,self.room1)
        self.assertEqual(1, len(self.room1.guests))
        self.assertEqual(0, len(self.room1.queue))
        self.assertEqual(10, self.room1.till)
        
    def test_room_can_collect_entry_fee_if_at_capacity(self):
        self.room1.check_in(self.guest1,self.room1)
        self.room1.check_in(self.guest2, self.room1)
        self.room1.check_in(self.guest3, self.room1)
        self.room1.check_in(self.guest4, self.room1)
        self.room1.check_in(self.guest5, self.room1)
        self.assertEqual(4, len(self.room1.guests))
        self.assertEqual(1, len(self.room1.queue))
        self.assertEqual(40, self.room1.till)
    
    def test_room_can_add_bar_drinks(self):
        self.room1.add_drink(self.bar)
        self.assertEqual(1, self.room1.drink_count())

