import telebot
import yfinance as yf
import json
from bs4 import BeautifulSoup, Tag
import requests
import random
import typing as t
import os
from telebot import types

# coin = "BTC-USD"
# currency = yf.Ticker(f"{coin}")
# with open ('coin.json', 'w') as file:
#     json.dump(currency.info, file) # dict to json

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY, parse_mode=None)

# Self-explanatory.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    item_1 = types.KeyboardButton('Top-10 crypto🪙')
    # item_2 = types.KeyboardButton('Top-10 corporations🏦')
    # item_3 = types.KeyboardButton('Latest News')
    # item_4 = types.KeyboardButton('About')
    

    markup.add(item_1)
    bot.send_message(
        message.chat.id, 
        'Hello! \n' + 
        'This is a currency market cap bot based on yahoo db!\n' +
        'Enter a ticker like TRX-USD or AAPL to see their current price and info.' .format(message.from_user), 
        reply_markup=markup)

# Sends base answers.
# @bot.message_handler(func=lambda message: True)
# def crypto(message):
#     currency = yf.Ticker(f"{message.text}")
#     image = (f'{message.text}')
#     price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
    
    # try:
    #     info = currency.info['description']
    # except KeyError:
    #     info = currency.info['longBusinessSummary']

#     bot.send_photo(message.chat.id, get_google_img(image), caption=price)
#     bot.send_message(message.chat.id, info)
#     for link in get_marketnews():    
#         bot.send_message(message.chat.id, link)
        
@bot.message_handler(func=lambda message: True)
def bot_message(message):
    # if message.chat.type == 'private':
    #     if message.text == 'About':
    #         bot.send_message(message.chat.id,'This is a currency market cap bot based on yahoo db!')

    if message.text == 'Top-10 crypto🪙':
        
        item_1 = types.KeyboardButton('btc-usd')
        item_2 = types.KeyboardButton('eth-usd')
        item_3 = types.KeyboardButton('usdt-usd')
        item_4 = types.KeyboardButton('bnb-usd')
        item_5 = types.KeyboardButton('xrp-usd')
        item_6 = types.KeyboardButton('hex-usd')
        item_7 = types.KeyboardButton('ada-usd')
        item_8 = types.KeyboardButton('sol-usd')
        item_9 = types.KeyboardButton('doge-usd')
        item_10 = types.KeyboardButton('trx-usd')
        back = types.KeyboardButton('Back')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        markup.add(
            item_1, item_2, item_3, 
            item_4, item_5, item_6, 
            item_7, item_8, item_9, 
            item_10, back,)
        
        bot.send_message(message.chat.id, 'Wait a sec..', reply_markup=markup)
  
        # Make it work!
        try:
            currency = yf.Ticker(f"{message.text}")
            image = f'{message.text}'  
            print(image)
            price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
            bot.send_photo(message.chat.id, get_google_img(image), caption=price)

            # info = currency.info['description']  
        except KeyError:
            bot.send_message(message.chat.id, 'Choose your crypto')
        
            # bot.send_message(message.chat.id, info)

                    
    # elif message.text == 'Top-10 corporations🏦':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     item_1 = types.KeyboardButton('AAPL')
    #     item_2 = types.KeyboardButton('MSFT')
    #     item_3 = types.KeyboardButton('TSLA')
    #     item_4 = types.KeyboardButton('FB')
    #     item_5 = types.KeyboardButton('TSM')
    #     item_6 = types.KeyboardButton('TCEHY')
    #     item_7 = types.KeyboardButton('JNJ')
    #     item_8 = types.KeyboardButton('V')
    #     item_9 = types.KeyboardButton('NVDA')
    #     item_10 = types.KeyboardButton('JPM')
    #     back = types.KeyboardButton('Back')
    

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
