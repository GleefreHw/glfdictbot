import tok
import telebot
import random


bot = telebot.TeleBot(token=tok.token)


@bot.message_handler(func=True)
def rhi(message):
    bot.send_message(chat_id=message.chat.id, text='Hi! Your k20 is ' + str(random.randint(1, 100)))


bot.polling()

