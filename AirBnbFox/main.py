from Scrap.Scrap import Scrap

if __name__ == '__main__':
    link_scrapper = 'https://www.airbnb.it/s/Bonaria--Cagliari--CA--Italia/homes?tab_id=home_tab&refinement_paths%5B%5D' \
          '=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-10-01&monthly_length=3' \
          '&price_filter_input_type=0&price_filter_num_nights=3&channel=EXPLORE&query=Bonaria%2C%20Cagliari%2C%20CA' \
          '&place_id=ChIJdXcPiIkz5xIRq62INO1tfzI&date_picker_type=calendar&checkin=2024-01-04&checkout=2024-01-07' \
          '&source=structured_search_input_header&search_type=user_map_move&ne_lat=39.21455208919867&ne_lng=9' \
          '.144950005624395&sw_lat=39.19367659568514&sw_lng=9.122534314517367&zoom=14.516550974121694&zoom_level=14' \
          '.516550974121694&search_by_map=true'

    self_scrapper = Scrap(None, None, link_scrapper)

    #print(self_scrapper)
    all_data_scrapped = []
    self_scrapper.set_url(link_scrapper)
    self_scrapper.set_soup(self_scrapper.get_soup())
    all_data_scrapped.append(self_scrapper.extract_location_in_concurrent_page())
