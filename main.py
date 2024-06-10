import telebot
import webbrowser
from telebot import types
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

tokenbot = config["BOT"]["token"]

bot = telebot.TeleBot(tokenbot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Пререйти на сайт')
    btn2 = types.KeyboardButton('Сообщество')

    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, 'эПривет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Пререйти на сайт':
        bot.send_message(message.chat.id, 'nbgf gthtitk')
    elif message.text == 'Сообщество':
        bot.send_message(message.chat.id, 'text')


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://ya.ru')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Пререйти на сайт', url="https://ya.ru")
    btn2 = types.InlineKeyboardButton('Сообщество', callback_data='edit')

    markup.row(btn1, btn2)

    btn3 = types.InlineKeyboardButton('Найди своего чувака', callback_data='find')

    markup.row(btn3)

    bot.send_message(message.chat.id, "message", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'find':
        bot.send_message(callback.message.chat.id, "hz")


bot.polling(none_stop=True, interval=0)