import telebot
import os
from telebot import types
from helpers import News
import keyboards


API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY, parse_mode=None)


# Self-explanatory.
@bot.message_handler(commands=['help'])
def send_explanation(message):
    bot.send_message(
        message.chat.id,
        '🟡To see price and info📑, just click or tap on buttons in the main menu.\n\n'
        '🟢You gonna see current, highest and lowest price change in last 24 hours🕐.\n\n'
        '🟡Request could take a few seconds, so please be patient👨‍💻.\n\n'
        '🟢This bot can get you latest🔥 crypto news right into your Telegram app.\n\n'
        '🟡If your screen will get to trashed with\n'
        'messages, just click on menu button\n'
        'for more convenient experience👀.\n')


# Self-explanatory.
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        'What\'s up! \n'
        'This is a currency bot🤖 based on market data📊 from Yahoo! Finance\'s API.\n'
        'Click /help for more info.',
        reply_markup=keyboards.Keyboard(types.InlineKeyboardMarkup(row_width=1)).generate_keyboard(keyboards.MAIN_KEYBOARD))


# Sends base answers for buttun prompts.
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(text='Your request is processing.', callback_query_id=call.id)
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
