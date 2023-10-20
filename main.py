import json
from Scrap.Scrap import Scrap
from pandas import *
from CustomizeLink.GenerateCalendar import customize_link as customizator

if __name__ == '__main__':

    with open("input.json", "r") as json_file:
        json_data = json.load(json_file)

    links = customizator(link=json_data['link'], year_=json_data['year'], check_in_day=json_data['check-in-day'],
                         check_out_day=json_data['check-out-day'])


    data = pandas.DataFrame(columns=['Link', 'Title', 'Price', 'Type', 'Badrooms', 'Bathrooms', 'Guests'])

    for k, link in enumerate(links):

        links = []
        titles = []
        prices = []
        types = []
        badrooms = []
        bathrooms = []
        guests = []
        self_scrapper = Scrap(None, None, link)

        all_data_scrapped = []
        self_scrapper.set_url(link)
        self_scrapper.set_soup(self_scrapper.get_soup())
        all_data_scrapped.append(self_scrapper.extract_location_in_concurrent_page("c4mnd7m"))
        all_data_scrapped.append(self_scrapper.extract_location_in_concurrent_page("c1l1h97y"))
        locations = self_scrapper.extract_data_location(all_data_scrapped=all_data_scrapped)

        print('Location scraped: ', len(locations))
        locations_ = self_scrapper.get_type_from_keywords(locations)

        for i in range(0, len(locations_) - 1):
            # locations_[i].print_location(with_link=True)
            links.append(locations_[i].get_link())
            titles.append(locations_[i].get_title())
            prices.append(locations_[i].get_price())
            types.append(locations_[i].get_type())
            badrooms.append(locations_[i].get_rooms())
            bathrooms.append(locations_[i].get_bathrooms())
            guests.append(locations_[i].get_guests())

        data = pandas.DataFrame(columns=['Link', 'Title', 'Price', 'Type', 'Badrooms', 'Bathrooms', 'Guests'])

        data['Link'] = links
        data['Title'] = titles
        data['Price'] = prices
        data['Type'] = types
        data['Badrooms'] = badrooms
        data['Bathrooms'] = bathrooms
        data['Guests'] = guests

        data.to_csv(f'./Report/extract{k}.csv')
