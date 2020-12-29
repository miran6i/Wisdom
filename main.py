# import telebot
# bot = telebot.TeleBot("1415537508:AAE4mxhOXjtgZH_Se4st7f-pTTdL4rfW4KU", parse_mode=None)
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Press a button to get stoic wisdom.")
#
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
#

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
