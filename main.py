import telebot
import yfinance as yf
import json
from bs4 import BeautifulSoup, Tag
import requests
import random
import typing as t

# coin = "BTC-USD"
# currency = yf.Ticker(f"{coin}")
# with open ('coin.json', 'w') as file:
#     json.dump(currency.info, file) # dict to json

bot = telebot.TeleBot('yourAPIkey', parse_mode=None)

# Self-explanatory.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello, this is a currency market cap bot based on yahoo db!\nEnter a ticker like TRX-USD or AAPL to see their current price and info.')

# Sends base answers.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    currency = yf.Ticker(f"{message.text}")
    image = (f'{message.text}')
    price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'

    try:
        info = currency.info['description']
    except KeyError:
        info = currency.info['longBusinessSummary']
    finally:
        bot.send_photo(message.chat.id, get_google_img(image), caption=price)
        bot.send_message(message.chat.id, info)

# Gets a link to the first five google images.
def get_google_img(query:'str')-> 'str':
    url = "https://www.google.com/search?q=" + str(query) + "&source=lnms&tbm=isch"
    headers = {'content-type': 'image/png'}
    response = requests.get(url, headers=headers).text    
    
    soup = BeautifulSoup(response, 'html.parser')
    items = soup.find_all('img', {'class': 'yWs4tf'})
    index = random.randint(0,5)
    dirty_image = items[index]
    return dirty_image['src']

# # Gets latest news from yahoo marketnews.
def get_marketnews():
    response = requests.get('https://finance.yahoo.com/topic/stock-market-news/')
    soup = BeautifulSoup(response.content, 'html.parser')
    news_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'}).find_all('p')
    title_page = soup.find('ul', {'class': 'My(0) P(0) Wow(bw) Ov(h)'}).find_all('a')
    
    if title_page:
        for title in title_page:
            print(title.text)

    if news_page:    
        for news in news_page:
            print(news.text.split('.'))
            print(type(news.text))

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

# bot.infinity_polling()


# if __name__ == '__main__':
#     get_marketnews()
    # test_map()
    # parse()
    # test()
    # query = input('search tearm\n')
    # get_google_img(query)
