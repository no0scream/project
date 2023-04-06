import json
import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

key = "https://api.binance.com/api/v3/ticker/price?symbol="
TOKEN = '6109604212:AAFfWbtUUL3eKccmUqSOl3L0MEhtSLLGyas'
bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Привет бот!'))
keyboard.add(KeyboardButton('Да, хе-хе'))
keyboard.add(KeyboardButton('Спасибо бро)'))

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Ку-ку маленький криптомиллионер', reply_markup=keyboard)

@bot.message_handler(regexp=r'Привет бот!\.*')
def hello(message):
    bot.send_message(message.chat.id, 'Хочешь узнать какой курс на биток?)')

@bot.message_handler(ragexp=r'Да, хе-хе\.*')
def get_curs():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=')
    data = requests.get(key)
    data = data.json()
    bot.send_message(message.chat.id, data)

@bot.message_handler(func=lambda s: 'Спасибо бро)' in s.text)
def bye(message):
    bot.send_message(message.chat.id, 'Обращайся. Дальше больше!)')


bot.infinity_polling()