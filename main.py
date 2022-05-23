from email import message
import telebot
import yfinance as yf
import json
from bs4 import BeautifulSoup, Tag
import requests
import random
import typing as t
import os
from telebot import types


API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY, parse_mode=None)

# Self-explanatory.
@bot.message_handler(commands=['help'])
def send_explanation(message):
    bot.send_message(message.chat.id, 'Enter a ticker like TRX-USD or AAPL to see their current price and info.')

# Self-explanatory.
@bot.message_handler(commands=['start'])
def send_welcome(message):
    main_keyboard = types.InlineKeyboardMarkup(row_width=2)
    menu_1 = types.InlineKeyboardButton('Top-10 crypto🪙', callback_data='open_crypto_list')
    menu_2 = types.InlineKeyboardButton('Top-10 corporations🏦', callback_data='open_corpo_list')
    menu_3 = types.InlineKeyboardButton('Latest News', callback_data='open_news_list')
    menu_4 = types.InlineKeyboardButton('About', callback_data='open_about')
    
    main_keyboard.add(menu_1, menu_2)
    bot.send_message(
        message.chat.id, 
        'Hello! \n' + 
        'This is a currency market cap bot based on yahoo db!\n' +
        'Type /help for more info.',
        reply_markup=main_keyboard)

# Sends base answers.
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == "main_menu":
        main_keyboard = types.InlineKeyboardMarkup(row_width=2)
        menu_1 = types.InlineKeyboardButton('Top-10 crypto🪙', callback_data='open_crypto_list')
        menu_2 = types.InlineKeyboardButton('Top-10 corporations🏦', callback_data='open_corpo_list')
        main_keyboard.add(menu_1, menu_2)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Main menu",reply_markup=main_keyboard)
    
    if call.data == 'open_corpo_list':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        item_1 = types.InlineKeyboardButton('Apple Inc.', callback_data='AAPL')
        item_2 = types.InlineKeyboardButton('Microsoft Corporation', callback_data='MSFT')
        item_3 = types.InlineKeyboardButton('Tesla Inc.', callback_data='TSLA')
        item_4 = types.InlineKeyboardButton('Meta Platforms', callback_data='FB')
        item_5 = types.InlineKeyboardButton('Taiwan Semiconductor Manufacturing Company Limited', callback_data='TSM')
        item_6 = types.InlineKeyboardButton('Tencent Holdings Limited', callback_data='TCEHY')
        item_7 = types.InlineKeyboardButton('Johnson & Johnson', callback_data='JNJ')
        item_8 = types.InlineKeyboardButton('Visa Inc', callback_data='V')
        item_9 = types.InlineKeyboardButton('NVIDIA Corporation', callback_data='NVDA')
        item_10 = types.InlineKeyboardButton('JP Morgan Chase & Co.', callback_data='JPM')
        back = types.InlineKeyboardButton(text='Back', callback_data='main_menu')

        keyboard.add(
            item_1, item_2, item_3, 
            item_4, item_5, item_6, 
            item_7, item_8, item_9, 
            item_10, back)
        
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text='Top-10 corporations🏦',reply_markup=keyboard)

    elif call.data == 'AAPL':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'MSFT':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'TSLA':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)
    
    elif call.data == 'FB':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)
    
    elif call.data == 'TSM':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'TCEHY':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'JNJ':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'V':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'NVDA':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'JPM':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['longBusinessSummary']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)


    if call.data == 'open_crypto_list':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        item_1 = types.InlineKeyboardButton('Bitcoin', callback_data='btc-usd')
        item_2 = types.InlineKeyboardButton('Ethereum', callback_data='eth-usd')
        item_3 = types.InlineKeyboardButton('Tether', callback_data='usdt-usd')
        item_4 = types.InlineKeyboardButton('BNB', callback_data='bnb-usd')
        item_5 = types.InlineKeyboardButton('XRP', callback_data='xrp-usd')
        item_6 = types.InlineKeyboardButton('HEX', callback_data='hex-usd')
        item_7 = types.InlineKeyboardButton('Cardano', callback_data='ada-usd')
        item_8 = types.InlineKeyboardButton('Wrapped Solana', callback_data='sol-usd')
        item_9 = types.InlineKeyboardButton('Dogecoin', callback_data='doge-usd')
        item_10 = types.InlineKeyboardButton('TRON', callback_data='trx-usd')
        back = types.InlineKeyboardButton(text='Back', callback_data='main_menu')

        keyboard.add(
            item_1, item_2, item_3, 
            item_4, item_5, item_6, 
            item_7, item_8, item_9, 
            item_10, back)
        
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text='Top-10 crypto🪙',reply_markup=keyboard)
       
    elif call.data == 'btc-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)
    
    elif call.data == 'eth-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)
        
    elif call.data == 'usdt-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'xrp-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'hex-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'ada-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'sol-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

    elif call.data == 'doge-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)
        
    elif call.data == 'trx-usd':
        currency = yf.Ticker(f"{call.data}")
        image = f'{call.data}'
        info = currency.info['description']
        print(info)
        price = currency.info['shortName'] + " : " + str(currency.info['regularMarketPrice']) + '💸\n' + '24H📈 : ' + str(currency.info['dayHigh']) + '$\n' + '24H📉 : ' + str(currency.info['dayLow']) + '$\n'
        bot.send_photo(call.message.chat.id, get_google_img(image), caption=price)
        bot.send_message(call.message.chat.id, info)

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

bot.infinity_polling()

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
 

# def test_map():
#    ma = list(map(lambda x: x+x, [1,2,3]))
#    ma




# if __name__ == '__main__':
#     get_marketnews()
    # test_map()
    # parse()
    # test()
    # query = input('search tearm\n')
    # get_google_img(query)


# coin = "BTC-USD"
# currency = yf.Ticker(f"{coin}")
# with open ('coin.json', 'w') as file:
#     json.dump(currency.info, file) # dict to json
