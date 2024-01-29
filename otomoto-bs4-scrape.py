
from otomoto_funcs.otomoto_functions import scrape_from_page, export_to_csv
from otomoto_cls.otomoto_classes import SetURL, Soup

if __name__ == '__main__':
    search_for_pages = SetURL()

    # getting pages from site
    soup_for_pages = Soup(search_for_pages.url)
    pages = soup_for_pages.get_pages()

    for page in range(1, pages):
        try:

            search = SetURL(page)
            search.make = 'toyota'
            search.model = 'corolla'
            search.year_to = 2016
            search.year_from = 2010
            search.price_low = 20000
            search.price_high = 30000

            soup = Soup(search.url)
            offers = scrape_from_page(soup)
            if len(offers) == 0:
                print('Empty list due to no results or error')
                quit()
            export_to_csv(f'{page}_{search.make}-{search.model}', offers)
        except ConnectionError:
            print('Connection failure')
