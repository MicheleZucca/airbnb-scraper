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

    def get_camere(self):
        return self.camere

    def get_bagni(self):
        return self.bagni

    def get_ospiti(self):
        return self.ospiti

    def set_link(self, link):
        self.link = link

    def set_title(self, title):
        self.title = title

    def set_price(self, price):
        self.price = price

    def set_type(self, type):
        self.type = type

    def set_camere(self, camere):
        self.camere = camere

    def set_bagni(self, bagni):
        self.bagni = bagni

    def set_ospiti(self, ospiti):
        self.ospiti = ospiti

    def print_location(self, with_link):
        if with_link:
            print(self.get_link())
            print(self.get_title())
            print(self.get_price())
            print(self.get_camere())
            print(self.get_bagni())
            print(self.get_ospiti())
            print(self.get_type())
        else:
            print(self.get_title())
            print(self.get_price())
            print(self.get_camere())
            print(self.get_bagni())
            print(self.get_ospiti())
            print(self.get_type())
