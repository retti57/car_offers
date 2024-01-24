import requests
from bs4 import BeautifulSoup as bs4
from otomoto_cls.otomoto_classes import Article


def find_article_tags(url) -> list:
    response = requests.get(url).text
    soup = bs4(response, 'html.parser')

    articles = soup.find_all('article')
    return articles


def scrape_from_page(url) -> list[Article]:
    offers = []
    i = 0
    for article in find_article_tags(url):
        i += 1
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

                        art.mileage, art.fuel, art.gearbox, art.production_year = [dd_tag.text for dd_tag in dd]

                    else:
                        dd = tag.find_all('dd')
                        art.city, _ = [dd_tag.text for dd_tag in dd]

                offers.append(art)
    return offers
