import telebot
from telebot import types

from functions import price, compute, convert 

help = ['List of avaliable commands: \n\n'
        '/calc: check sale profit \n'
        '/gas: get gas price \n'
        '/eth: convert ETH to USD and RUB \n'
        '/usd: convert USD to ETH and RUB \n'
        '/rub: convert RUB to ETH and USD \n']

TOKEN = '5475678962:AAFzRcJB8QLqo5DGEQETv-AcyddJ2Cw4300'

bot = telebot.TeleBot(TOKEN)

#start message
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'WELCOME /help')

#help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, help)

#calculate profit
@bot.message_handler(commands=['calc'])
def calculation(message):
    msg = message.text.split(' ')
    try:
        bot.send_message(message.chat.id, compute.profit(msg[1:]))
    except IndexError:
        bot.send_message(message.chat.id, 'Input requires 4 numbers')
          
#convertation
@bot.message_handler(commands=['eth'])
def start_message(message):
    bot.send_message(message.chat.id, convert.eth(message.text.split(' ')))
 

@bot.message_handler(commands=['usd'])
def start_message(message):
    bot.send_message(message.chat.id, convert.usd(message.text.split(' ')))


@bot.message_handler(commands=['rub'])
def start_message(message):
    bot.send_message(message.chat.id, convert.rub(message.text.split(' ')))
    
#gas price        
@bot.message_handler(commands=['gas'])
def start_message(message):
    bot.send_message(message.chat.id, price.gas())


bot.polling(none_stop=True, interval=0)