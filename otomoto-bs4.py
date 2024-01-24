from otomoto_funcs.otomoto_functions import scrape_from_page
from otomoto_cls.otomoto_classes import SearchConfig

search = SearchConfig()
offers = scrape_from_page(search.url)

for i, offer in enumerate(offers):
    print(offer.title)
    print(offer.link)
    print(offer.mileage)
    print(offer.price)
    print(offer.production_year)
    print(offer.city)
    print(f'#######{i}')

