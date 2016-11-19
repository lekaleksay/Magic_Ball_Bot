# -*- coding: utf-8 -*-
import config
import telebot
from random import randint
from config import database_name
from SQLighter import SQLighter

bot = telebot.TeleBot(config.token)
db = SQLighter(database_name)

list_items = []
for a in range (1,21):
    core = db.select_single(a)
    list_items.append(core)
print(list_items)
@bot.message_handler(func=lambda message: True, content_types=['text'])
def otveti(message):

    if message.text[0] == '/':
        bot.send_message(message.chat.id, 'Приветствую в боте Магичесий Шар. Загляни в будущее, задай вопрос.')

    else:
        a = randint(0, 19)
        bot.send_message(message.chat.id, list_items[a])

if __name__ == '__main__':
     bot.polling(none_stop=True)