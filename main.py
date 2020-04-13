import tok
import telebot
import random


bot = telebot.TeleBot(token=tok.token)


@bot.message_handler(commands=['start', 'help'])
def rhi(message):
    bot.send_message(chat_id=message.chat.id, text='Hi! Your k is ' + str(random.randint(1, 100)))


bot.polling()

