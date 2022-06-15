import telebot
import yfinance as yf
import os
from telebot import types
from helpers import get_google_img, News
import keyboards


API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY, parse_mode=None)


# Self-explanatory.
@bot.message_handler(commands=['help'])
def send_explanation(message):
    bot.send_message(message.chat.id, 'Enter a ticker like TRX-USD or AAPL to see their current price and info.')


# Self-explanatory.
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        'Hello! \n'
        'This is a currency market cap bot based on yahoo db!\n'
        'Type /help for more info.',
        reply_markup=keyboards.Keyboard(types.InlineKeyboardMarkup(row_width=1)).generate_keyboard(keyboards.MAIN_KEYBOARD))


# Sends base answers for buttun prompts.
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query( text='Your request is processing.', callback_query_id=call.id)
    if call.data == "main_menu":
        keyboard = keyboards.Keyboard(types.InlineKeyboardMarkup(row_width=1))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Main Menu",
            reply_markup=keyboard.generate_keyboard(keyboards.MAIN_KEYBOARD))


    news = News()
    if call.data == "open_news_list":
        for link in news():
            bot.send_message(call.message.chat.id, link)


    if call.data == 'open_corpo_list':
        keyboard = keyboards.Keyboard(types.InlineKeyboardMarkup(row_width=3))            
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Top-10 corporations🏦',
            reply_markup=keyboard.generate_keyboard(keyboards.OPEN_CORPO_LIST))


    if call.data == 'open_crypto_list':
        keyboard = keyboards.Keyboard(types.InlineKeyboardMarkup(row_width=3))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Top-10 crypto🪙',
            reply_markup=keyboard.generate_keyboard(keyboards.OPEN_CRYPTO_LIST))
       
       
    if call.data in keyboards.CryptoReaction.callback_datas:
        keyboards.CryptoReaction(call.data).send_reaction(bot, call.message.chat.id)    
    if call.data in keyboards.CorpoReaction.callback_datas:
        keyboards.CorpoReaction(call.data).send_reaction(bot, call.message.chat.id)


if __name__ == '__main__':
    bot.infinity_polling()
