from typing import Any

import requests
from bs4 import BeautifulSoup


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

    def extract_location_in_concurrent_page(self):
        return self.soup.find_all('div', class_="c4mnd7m")
