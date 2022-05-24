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
def get_marketnews():
    # response = requests.get('https://finance.yahoo.com/topic/stock-market-news/')
    response = requests.get('https://finance.yahoo.com/topic/crypto/')
    soup = BeautifulSoup(response.content, 'html.parser')
    base_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'})
    # news_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'}).find_all('p')
    # title_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'}).find_all('a')
    # part_url = 'https://finance.yahoo.com/topic/stock-market-news'
    part_url = 'https://finance.yahoo.com/topic/crypto'

    if base_page := base_page.find_all(href=True):
        for link in base_page:
            full_url = part_url + link['href']
            yield full_url

# coin = "BTC-USD"
# currency = yf.Ticker(f"{coin}")
# with open ('coin.json', 'w') as file:
#     json.dump(currency.info, file) # dict to json
