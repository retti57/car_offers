import requests
from bs4 import BeautifulSoup as bs4


class Article:
    def __init__(self):
        self.title = ''
        self.picture = ''
        self.link = ''
        self.price = ''
        self.mileage = ''
        self.gearbox = ''
        self.fuel = ''
        self.production_year = ''
        self.city = ''
        self.identifier = 0

    def __str__(self):
        return self.title, self.price


class SetURL:
    def __init__(self, page=1):
        self.price_low, self.price_high = 15000, 40000
        self.year_from, self.year_to = 2007, 2018
        self.make, self.model = 'ford', 'mondeo'
        self.page = str(page)

    @property
    def url(self):
        return f"https://www.otomoto.pl/osobowe/{self.make}/{self.model}/seg-sedan/od-{self.year_from}?search%5Bfilter_enum_fuel_type%5D=petrol&search%5Bfilter_float_price%3Afrom%5D={self.price_low}&search%5Bfilter_float_price%3Ato%5D={self.price_high}&search%5Bfilter_float_year%3Ato%5D={self.year_to}&page={self.page}&search%5Badvanced_search_expanded%5D=true"


class Soup:
    def __init__(self, search_url):
        self.search_url = search_url

    @property
    def make_soup(self):
        response = requests.get(self.search_url).text
        bs = bs4(response, 'html.parser')
        return bs

    def get_pages(self):
        main = self.make_soup.find('main')
        ul_tags = main.find_all('li', attrs={'data-testid': "pagination-list-item", 'class': 'pagination-item'})
        return len(ul_tags) + 1
