from otomoto_cls.otomoto_classes import Article, Soup


def find_article_tags(bsoup) -> list:
    try:

        articles = bsoup.find_all('article')

        return articles

    except:
        print('Internet connection failure')
        return []


def scrape_from_page(BeautifulSoup: Soup) -> list[Article]:
    articles = find_article_tags(BeautifulSoup.make_soup)

    offers = []
    i = 0
    for article in articles:
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


def export_to_csv(fname: str, article_objs: list[Article]):
    count = len(article_objs)
    with open(f'{fname}_{count}_ofert.csv', mode='w', encoding='utf8') as f:
        f.write('title,price,picture,mileage,fuel,gearbox,production_year,city,link\n')
        for article_obj in article_objs:
            f.write(
                f"{article_obj.title},{article_obj.price},{article_obj.picture},{article_obj.mileage},{article_obj.fuel},{article_obj.gearbox},{article_obj.production_year},{article_obj.city},{article_obj.link}\n")
