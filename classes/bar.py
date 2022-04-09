class Bar:

    def __init__(self, input_name, input_price):
        self.name = input_name
        self.price = input_price
        self.till = 0

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price