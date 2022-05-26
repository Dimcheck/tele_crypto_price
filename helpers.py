from bs4 import BeautifulSoup
import requests
import random


# Gets a link to the first five google images.
def get_google_img(query: 'str') -> 'str':
    url = "https://www.google.com/search?q=" + str(query) + "&source=lnms&tbm=isch"
    headers = {'content-type': 'image/png'}
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')

    items = soup.find_all('img', {'class': 'yWs4tf'})
    index = random.randint(0, 5)
    dirty_image = items[index]
    return dirty_image['src']


# Gets latest news from yahoo marketnews.
class News:
    tag = 'ul'
    nav_str = {'class': 'My(0) P(0) Wow(bw) Ov(h)'}
    base_url = 'https://finance.yahoo.com/topic/crypto/'
    full_link_url = 'https://finance.yahoo.com/topic/crypto/{path_to_article}'

    def __call__(self):
        soup = self._get_client()
        base_page = soup.find(self.tag, self.nav_str)
        return self.iterate_links(base_page)

    def _get_client(self) -> None:
        response = requests.get(self.base_url)
        return BeautifulSoup(response.content, 'html.parser')

    def iterate_links(self, base_page):
        if base_page := base_page.find_all(href=True):
            for link in base_page:
                yield self.full_link_url.format(path_to_article=link['href'])


# coin = "BTC-USD"
# currency = yf.Ticker(f"{coin}")
# with open ('coin.json', 'w') as file:
#     json.dump(currency.info, file) # dict to json
