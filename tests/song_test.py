import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song5 = Song("That's Life", "Frank Sinatra")
        
    def test_song_has_name(self):
        self.assertEqual("That's Life", self.song5.name)
