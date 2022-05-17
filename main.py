import telebot
import yfinance as yf
import json
from bs4 import BeautifulSoup
import requests
import random


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

bot.infinity_polling()


# if __name__ == '__main__':
    # parse()
    # test()
    # query = input('search tearm\n')
    # get_google_img(query)
