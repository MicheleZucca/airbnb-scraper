from Scrap.Scrap import Scrap
from pandas import *

if __name__ == '__main__':
    link_scrapper = 'https://www.airbnb.it/s/Cagliari/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes' \
                    '&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-11-01&monthly_length=3' \
                    '&price_filter_input_type=0&price_filter_num_nights=2&channel=EXPLORE&date_picker_type=calendar' \
                    '&checkin=2023-11-03&checkout=2023-11-05&adults=2&source=structured_search_input_header' \
                    '&search_type=user_map_move&query=Cagliari%2C%20CA&place_id=ChIJoxyOthU05xIRsW6BzwYVHiA&ne_lat=39' \
                    '.235897600681476&ne_lng=9.144510505139465&sw_lat=39.191742916327996&sw_lng=9.098668250082113' \
                    '&zoom=14.21748072989819&zoom_level=14.21748072989819&search_by_map=true'

    data = pandas.DataFrame(columns=['Link', 'Title', 'Price', 'Type', 'Badrooms', 'Bathrooms', 'Guests'])
    links = []
    titles = []
    prices = []
    types = []
    badrooms = []
    bathrooms = []
    guests = []
    self_scrapper = Scrap(None, None, link_scrapper)

    all_data_scrapped = []
    self_scrapper.set_url(link_scrapper)
    self_scrapper.set_soup(self_scrapper.get_soup())
    all_data_scrapped.append(self_scrapper.extract_location_in_concurrent_page("c4mnd7m"))
    all_data_scrapped.append(self_scrapper.extract_location_in_concurrent_page("c1l1h97y"))
    locations = self_scrapper.extract_data_location(all_data_scrapped=all_data_scrapped)

    print('Location scraped: ', len(locations))
    locations_ = self_scrapper.get_type_from_keywords(locations)


    for i in range(0, len(locations_)-1):
        #locations_[i].print_location(with_link=True)
        links.append(locations_[i].get_link())
        titles.append(locations_[i].get_title())
        prices.append(locations_[i].get_price())
        types.append(locations_[i].get_type())
        badrooms.append(locations_[i].get_camere())
        bathrooms.append(locations_[i].get_bagni())
        guests.append(locations_[i].get_ospiti())


    data = pandas.DataFrame(columns=['Link', 'Title', 'Price', 'Type', 'Badrooms', 'Bathrooms', 'Guests'])

    data['Link'] = links
    data['Title'] = titles
    data['Price'] = prices
    data['Type'] = types
    data['Badrooms'] = badrooms
    data['Bathrooms'] = bathrooms
    data['Guests'] = guests

    data.to_csv('./Report/extract.csv')

