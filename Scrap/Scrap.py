import copy
import re
import requests
from bs4 import BeautifulSoup

from .Location import Location
from .Location import types as types_of_room


class Scrap:

    def __init__(self, page_request, soup, url):
        self.page_request = page_request
        self.soup = soup
        self.url = url

    def set_soup(self, soup):
        self.soup = soup
        return self.soup

    def set_url(self, url):
        self.url = url
        return self.url

    def get_soup(self):
        return BeautifulSoup(requests.get(self.url).content, 'html.parser')

    def extract_location_in_concurrent_page(self, class_name_option):
        return self.soup.find_all('div', class_=class_name_option)

    def extract(self):
        self.set_soup(self.get_soup())
        return self.soup

    @staticmethod
    def extract_data_location(all_data_scrapped):
        locations = []
        for sub in all_data_scrapped:
            for l in sub:
                try:
                    price = l.find('span', class_="a8jt5op dir dir-ltr").text.replace('\xa0', '')
                    price = re.findall(r'[0-9]*[$€£]', price, re.UNICODE)
                    # print(price)
                    if len(price) > 0:
                        price = price.pop(0)
                    elif len(price) == 0:
                        price = None
                except Exception as e:
                    print('Eccezzione lanciata nella cattura del prezzo (obj_with_data): ', e)
                    print('\nEsecuzione interrotta!')
                    exit()
                if price is not None:
                    try:
                        title = l.find('div', class_="fb4nyux s1cjsi4j dir dir-ltr").text
                    except Exception as e:
                        print('Eccezzione lanciata nella cattura del titolo (obj_with_data): ', e)
                        print('\nEsecuzione interrotta!')
                        exit()
                    try:
                        link = 'https://www.airbnb.it' + l.find('a', rel="noopener noreferrer nofollow").get('href')
                    except Exception as e:
                        print('Eccezzione lanciata nella cattura del link (obj_with_data): ', e)
                        print('\nEsecuzione interrotta!')
                        exit()

                    location_instance = Location()
                    location_instance.set_link(link=link)
                    location_instance.set_title(title=title)
                    location_instance.set_price(price=price)
                    locations.append(location_instance)
        return locations

    @staticmethod
    def search_data_from_keywords(data_from_link):

        people = re.findall((r'[0-9]' + r' ospiti'), data_from_link)
        rooms = re.findall(r'[0-9]' + r' camer' + r'[a-z]' + ' da letto', data_from_link)
        bathrooms = re.findall(r'[0-9]' + ',' + r'[0-9]' + r' bagn' + r'[a-z]', data_from_link)
        types = re.findall(r'[A-Za-z]{1,4}' + 'locale', data_from_link)

        if len(bathrooms) == 0:
            bathrooms = re.findall(r'[0-9]' + r' bagn' + r'[a-z]', data_from_link)

        result = copy.deepcopy({'people': None, 'rooms': None, 'bathrooms': None, 'type': None})
        result['people'] = re.search(r'(\d+)', people.pop()).group(1) if len(people) != 0 else 0
        result['rooms'] = re.search(r'(\d+)', rooms.pop()).group(1) if len(rooms) != 0 else 0
        result['bathrooms'] = re.search(r'(\d+)', bathrooms.pop()).group(1) if len(bathrooms) != 0 else 0
        result['type'] = types.pop() if len(types) != 0 else None

        if result['type'] is None and (result['rooms'] != 0 and result['bathrooms'] != 0):
            rooms_ = int(result['rooms']) + int(result['bathrooms'])
            if rooms_ == 2:
                result['type'] = types_of_room[1]
            elif rooms_ == 3:
                result['type'] = types_of_room[2]
            elif rooms_ == 4:
                result['type'] = types_of_room[3]
            else:
                result['type'] = types_of_room[4]
        else:
            if result['type'] == 'monolocale':
                result['type'] = types_of_room[0]

        return result

    def get_type_from_keywords(self, locations):

        self_locations = []

        for location in locations:
            self_location = Location()

            self_data_from_link = Scrap(None, None, location.get_link())
            location_sheet = self.search_data_from_keywords(str(self_data_from_link.extract()))
            self_location.set_link(location.get_link())
            self_location.set_title(location.get_title())
            self_location.set_price(location.get_price())
            self_location.set_rooms(location_sheet.get('rooms'))
            self_location.set_bathrooms(location_sheet.get('bathrooms'))
            self_location.set_guests(location_sheet.get('people'))
            self_location.set_type(location_sheet.get('type'))
            self_locations.append(self_location)

            del self_location

        return self_locations
