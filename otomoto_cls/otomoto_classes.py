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


class SearchConfig:
    price_low, price_high = 15000, 40000
    year_from, year_to = 2007, 2016
    make, model = 'ford', 'mondeo'
    page = 1
    url = f"https://www.otomoto.pl/osobowe/{make}/{model}/seg-sedan/od-{year_from}?search%5Bfilter_enum_fuel_type%5D=petrol&search%5Bfilter_float_price%3Afrom%5D={price_low}&search%5Bfilter_float_price%3Ato%5D={price_high}&search%5Bfilter_float_year%3Ato%5D={year_to}&page={page}&search%5Badvanced_search_expanded%5D=true"
