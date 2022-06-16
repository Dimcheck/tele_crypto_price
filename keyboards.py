import typing as t
from helpers import get_google_img
import yfinance as yf
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


MAIN_KEYBOARD: t.Final = {
    'Top-10 crypto🪙': 'open_crypto_list',
    'Top-10 corporations🏦': 'open_corpo_list',
    'Latest News': 'open_news_list',
}

OPEN_CORPO_LIST: t.Final = {
    'Berkshire Hathaway Inc.': 'BRK-B',
    'Microsoft Corporation': 'MSFT',
    'Tesla Inc.': 'TSLA',
    'Meta Platforms': 'FB',
    'Taiwan Semiconductor Manufacturing Company Limited': 'TSM',
    'Tencent Holdings Limited': 'TCEHY',
    'Johnson & Johnson': 'JNJ',
    'Amazon.com': 'AMZN',
    'NVIDIA Corporation': 'NVDA',
    'JP Morgan Chase & Co.': 'JPM',
    'Back': 'main_menu',
}

OPEN_CRYPTO_LIST: t.Final = {
    'Bitcoin': 'btc-usd',
    'Ethereum': 'eth-usd',
    'Tether': 'usdt-usd',
    'BNB': 'bnb-usd',
    'XRP': 'xrp-usd',
    'HEX': 'hex-usd',
    'Cardano': 'ada-usd',
    'Wrapped Solana': 'sol-usd',
    'Dogecoin': 'doge-usd',
    'TRON': 'trx-usd',
    'Back': 'main_menu',
}

class KeyboardInvalid(Exception):
    """Raise when button has invalid type"""


class Keyboard:
    keyboard: InlineKeyboardMarkup
    
    def __init__(self, keyboard):
        self.keyboard = keyboard

    def _generate_keyboard(self, buttons: t.List[InlineKeyboardButton]) -> InlineKeyboardMarkup:
        buttons_inl = []
        for name, callback_data in buttons.items():
            buttons_inl.append(InlineKeyboardButton(name, callback_data=callback_data))
        return self.keyboard.add(*buttons_inl)

    def generate_keyboard(self, buttons) -> InlineKeyboardMarkup:
        if isinstance(buttons, dict):
            return self._generate_keyboard(buttons)
        raise KeyboardInvalid('Not a Dict type')


class BaseReaction:
    callback_datas: t.Iterable[str]
    info: str

    def __init__(self, data):
        self.data = data

    def get_currency(self):
        if self.data == 'main_menu':
            pass
        else:
            return yf.Ticker(self.data)

    def get_img(self):
        return get_google_img(self.data)

    def get_info(self, currency):
        return currency.info[self.info]
    
    def get_price(self, currency):
        price = currency.info.get('shortName', '') + " : " + str(currency.info.get('regularMarketPrice', ''))
        price += '💸\n' + 'Highest price today📈 : ' + str(currency.info.get('dayHigh', '')) + '$\n' + 'Lowest price today 📉 : ' 
        price += str(currency.info.get('dayLow', '')) + '$\n'
        return price

    def send_reaction(self, bot, chat_id):
        try:
            currency = self.get_currency()
            bot.send_photo(chat_id, self.get_img(), caption=self.get_price(currency))
            bot.send_message(chat_id, self.get_info(currency))
        except AttributeError:
            print('Back to main menu...')


class CorpoReaction(BaseReaction):
    info: str = 'longBusinessSummary'
    callback_datas: t.Iterable[str] = OPEN_CORPO_LIST.values()


class CryptoReaction(BaseReaction):
    info: str = 'description'
    callback_datas: t.Iterable[str] = OPEN_CRYPTO_LIST.values()
    