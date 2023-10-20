types = ['Monolocale', 'Bilocale', 'Trilocale', 'Quadrilocale', 'Altro']


class Location:

    def __init__(self):
        pass

    def get_link(self):
        return self.link

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type

    def get_rooms(self):
        return self.rooms

    def get_bathrooms(self):
        return self.bathrooms

    def get_guests(self):
        return self.guests

    def set_link(self, link):
        self.link = link

    def set_title(self, title):
        self.title = title

    def set_price(self, price):
        self.price = price

    def set_type(self, type):
        self.type = type

    def set_rooms(self, rooms):
        self.rooms = rooms

    def set_bathrooms(self, bathrooms):
        self.bathrooms = bathrooms

    def set_guests(self, guests):
        self.guests = guests

    def print_location(self, with_link):
        if with_link:
            print(self.get_link())
            print(self.get_title())
            print(self.get_price())
            print(self.get_rooms())
            print(self.get_bathrooms())
            print(self.get_guests())
            print(self.get_type())
        else:
            print(self.get_title())
            print(self.get_price())
            print(self.get_rooms())
            print(self.get_bathrooms())
            print(self.get_guests())
            print(self.get_type())
