# haslo: 693014519
# haslo2: 693519014
import requests
from bs4 import BeautifulSoup as bs4

price_low, price_high = 15000, 40000
year_from, year_to = 2007, 2016
make, model = 'ford', 'mondeo'

url = f"https://www.otomoto.pl/osobowe/{make}/{model}/seg-sedan/od-{year_from}?search%5Bfilter_enum_fuel_type%5D=petrol&search%5Bfilter_float_price%3Afrom%5D={price_low}&search%5Bfilter_float_price%3Ato%5D={price_high}&search%5Bfilter_float_year%3Ato%5D={year_to}&search%5Badvanced_search_expanded%5D=true"

response = requests.get(url).text
soup = bs4(response, 'html.parser')

articles = soup.find_all('article')

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
        return self.__init__()

offers = []

i = 0

for article in articles:
    i+=1
    picture = article.find("img")
    if picture is None:
        pass
    else:
        art = Article()
        art.ident = i
        art.picture = picture['src']


        h1_title = article.find('h1')
        if h1_title is None:
            pass
        else:

            art.link = h1_title.a['href']
            art.title = h1_title.text

            h3_price = article.find('h3')
            art.price = h3_price.text

            dl_tag = article.find_all('dl')
            for num, tag in enumerate(dl_tag):
                if num == 0:
                    dd = tag.find_all('dd')

                    art.mileage, art.fuel, art.gearbox, art.production_year= [dd_tag.text for dd_tag in dd]

                else:
                    dd = tag.find_all('dd')
                    art.city,_ = [dd_tag.text for dd_tag in dd]

                # print('#######')
            offers.append(art)

for offer in offers:
    print(offer.title)
    print(offer.link)
    print(offer.mileage)
    print(offer.price)
    print(offer.production_year)
    print(offer.city)
    print('#######')