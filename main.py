import json
import os
import random
import typing as t

import requests
from requests import Response
import telebot
import yfinance as yf
from bs4 import BeautifulSoup, Tag

# coin = "BTC-USD"
# currency = yf.Ticker(f"{coin}")
# with open ('coin.json', 'w') as file:
#     json.dump(currency.info, file) # dict to json

bot = telebot.TeleBot(os.environ['TOKEN_API'], parse_mode=None)

# Self-explanatory.


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 'Hello, this is a currency market cap bot based on yahoo db!\nEnter a ticker like TRX-USD or AAPL to see their current price and info.')

# Sends base answers.


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    currency = yf.Ticker(f"{message.text}")
    image = (f'{message.text}')
    price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(
        currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'

    try:
        info = currency.info['description']
    except KeyError:
        info = currency.info['longBusinessSummary']
        
    
    bot.send_photo(message.chat.id, get_google_img(image), caption=price)
    bot.send_message(message.chat.id, info)
    news = News()
    for txt in news():
        bot.send_message(message.chat.id, txt)


# Gets a link to the first five google images.
def get_google_img(query: 'str') -> 'str':
    url = "https://www.google.com/search?q=" + \
        str(query) + "&source=lnms&tbm=isch"
    headers = {'content-type': 'image/png'}
    response = requests.get(url, headers=headers).text

    soup = BeautifulSoup(response, 'html.parser')
    items = soup.find_all('img', {'class': 'yWs4tf'})
    index = random.randint(0, 5)
    dirty_image = items[index]
    return dirty_image['src']

# # Gets latest news from yahoo marketnews.


# def get_marketnews():
#     # response = requests.get('https://finance.yahoo.com/topic/stock-market-news/')
#     part_url = 'https://finance.yahoo.com/topic/crypto'
#     response = requests.get(part_url)

#     soup = BeautifulSoup(response.content, 'html.parser')
#     base_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'})
#     # news_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'}).find_all('p')
#     # title_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'}).find_all('a')
#     # part_url = 'https://finance.yahoo.com/topic/stock-market-news'

#     if base_page := base_page.find_all(href=True):
#         for link in base_page:
#             full_url = part_url + link['href']
#             yield full_url


class LinksNotFoundError(Exception):
    """Raise when link does not found on the page"""


class News:
    _soup: BeautifulSoup
    tag = 'ul'
    navigable_str = {'class': 'My(0) P(0) Wow(bw) Ov(h)'}
    url_yahoo = 'https://finance.yahoo.com/topic/crypto/'
    full_link_template = 'https://finance.yahoo.com/topic/crypto/{path_to_article}'

    def __init__(self) -> None:
        self._soup = BeautifulSoup(self._get_response(), 'html.parser')

    def __call__(cls) -> t.Generator[str, None, None]:
        if page_content := cls._soup.find(cls.tag, cls.navigable_str).find_all(href=True):
            return cls.iterate_links(page_content)
        raise LinksNotFoundError()

    def _get_response(self) -> bytes:
        return requests.get(self.url_yahoo).content

    def iterate_links(self, page_content) -> t.Generator[str, None, None]:
        for link in page_content:
            yield self.full_link_template.format(path_to_article=link['href'])


    # if news_page:
    #     for news in news_page:
    #         print(news.text.split('.'))
    #         print(type(news.text))

# !!!NextUpdateWIP!!!
# def get_marketnews():
#     response = requests.get('https://finance.yahoo.com/topic/stock-market-news/')
#     soup = BeautifulSoup(response.content, 'html.parser')
#     new = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'})
#     # for a in iterate_content('a', new):
#     #     print(a.text)
#
#     list(map(print_text, iterate_content('a', new)))
#     list(map(print_text, iterate_content('p', new)))
#     # # news_page = new.find_all('p')

    # if title_page := new.find_all('a'):
    #     for title in title_page:
    #         print(title.text)

# !!!NextUpdateWIP!!!
# def iterate_content(tag: str, borsch: Tag) -> t.Generator[str, None, None]:
#     yield from borsch.find_all(tag)
#     # for object in borsch.find_all(tag):
#     #     yield object

# !!!NextUpdateWIP!!!
# def print_text(arg):
#     print(arg.text)

# /news/stock-market-news-live-updates-may-18-2022-221712104.html --- create link for the parsed half of the link

# def test_map():
#    ma = list(map(lambda x: x+x, [1,2,3]))
#    ma


bot.infinity_polling()


# if __name__ == '__main__':
#     get_marketnews()
# test_map()
# parse()
# test()
# query = input('search tearm\n')
# get_google_img(query)
