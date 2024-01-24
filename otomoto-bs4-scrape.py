from otomoto_funcs.otomoto_functions import scrape_from_page, export_to_csv
from otomoto_cls.otomoto_classes import SearchConfig
# import pandas as pd
try:
    search = SearchConfig()
    offers = scrape_from_page(search.url)
    if len(offers) == 0:
        print('Empty list')
        quit()
    export_to_csv(f'{search.make}-{search.model}', offers)
except ConnectionError:
    print('Connection failure')
# df = pd.DataFrame()
