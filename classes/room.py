class Room:
    
    def __init__(self, input_name, input_capacity, input_fee, input_till):
        self.name = input_name
        self.capacity = input_capacity
        self.playlist = []
        self.fee = input_fee
        self.till = input_till
        self.guests = []
        self.queue = []

    def get_room_name(self):
        return self.name

    def get_till(self):
        return self.till

    def song_count(self):
        return len(self.playlist)
    
    def add_song(self, song):
        self.playlist.append(song)

    def get_capacity(self):
        return self.capacity

#This works
    # def check_in(self, guest):
    #     if len(self.guests) < self.capacity:
    #         self.guests.append(guest)
    #         self.till += self.fee
    #     else: 
    #         self.queue.append(guest)
    #     return len(self.guests), len(self.queue), self.till

    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            self.till += self.fee
        else: 
            self.queue.append(guest)
        return len(self.guests), len(self.queue), self.till

    def check_out(self, guest):
        self.guests.remove(guest)
        return len(self.guests)

    # def collect_fee(self, customer, drink):
    #     if self.drinks.count(drink) == 0:
    #         return
    #     self.drinks.remove(drink)
    #     customer.buy_drink(drink)
    #     self.till += drink.price   
