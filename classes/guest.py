class Guest:

    def __init__(self, input_name, input_age, input_wallet, input_favourite_song, input_cheer):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song
        self.cheer = input_cheer

    def pay_fee(self, room):
        if self.wallet >= room.fee:
            self.wallet -= room.fee

    def get_favourite_song(self):
        self.favourite_song
    
    def cheer_for_favourite(self, room_playlist):
        for song in room_playlist:
            if song == self.favourite_song:
                return self.cheer
    
    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price
    
    def sufficient_funds(self, item):
        return self.wallet >= item.price