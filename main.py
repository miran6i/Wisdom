from resources import *
import telebot
from telebot import types


TOKEN = 'inser your token here'

bot = telebot.TeleBot(TOKEN)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Get a Stoic Wisdom')
keyboard.add(btn1)


@bot.message_handler(commands=['start'])
def start_mes(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hello, I can help you master self-discipline.", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_mes(message):
    chat_id = message.chat.id
    if message.text == "Get a Stoic Wisdom":
        bot.send_message(chat_id, daily_stoic())


bot.polling()
