from locale import currency
import telebot
import yfinance as yf
import json


coin = "AAPL"
currency = yf.Ticker(f"{coin}")
# print(currency.info)

with open ('company.json', 'w') as file:
    json.dump(currency.info, file) # dict to json

bot = telebot.TeleBot('yourAPIkey', parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, this is a currency market cap bot based on yahoo db!\nEnter a ticker like TRX-USD or AAPL to see their current price.')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    currency = yf.Ticker(f"{message.text}")
    bot.send_message(message.chat.id, currency.info['shortName'] + " => " + str(currency.info['regularMarketPrice']) + '$')
    # bot.send_message(message.chat.id,str(currency.info['regularMarketPrice']))
    # bot.send_message(message.chat.id, message.text)
    # coin = "TRX-USD"

bot.infinity_polling()