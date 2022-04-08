class Guest:
    def __init__(self, input_name, input_age, input_wallet, input_favourite_song):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def pay_fee(self, room):
        if self.wallet >= room.fee:
            self.wallet -= room.fee
        return self.wallet
    
    # def cheer(self, room_playlist):
    #     if self.favourite_song == room_playlist:
    #         return "Woohoo! I love this song!"