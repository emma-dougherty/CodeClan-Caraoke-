class Room:
    
    def __init__(self, input_name, input_capacity, input_fee):
        self.name = input_name
        self.capacity = input_capacity
        self.playlist = []
        self.fee = input_fee
        self.till = 0
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

    def check_in(self, guest):
        if len(self.guests) >= self.capacity:
            self.queue.append(guest)
        else:
            self.guests.append(guest)
            self.till += self.fee
            len(self.guests)
            len(self.queue)
    
    def check_out(self, guest):
        self.guests.remove(guest)
        return len(self.guests)


# Attempt to also deduct from guest wallet
    # def check_in(self, guest, room):
    #     if len(self.guests) >= self.capacity:
    #         self.queue.append(guest)
    #     else:
    #         self.guests.append(guest)
    #         guest.pay_fee(room)  #### pay_fee not recognised ####
    #         self.till += self.fee
    #         len(self.guests)
    #         len(self.queue)

