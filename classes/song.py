class Song:
    
    def __init__(self, input_name, input_artist):
        self.name = input_name
        self.artist = input_artist
    
    def get_song_name(self):
        return self.name