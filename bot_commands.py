import telebot
from telebot import types

from functions import price, compute, convert 


help = ['List of avaliable commands: \n\n'
        'Check sale profit: /calc \n'
        'Get gas price : /gas\n'
        'ETH ro USD excange rate: /ethusd \n'
        'ETH ro RUB excange rate: /ethrub \n'
        'RUB ro USD excange rate: /usdrub' ]
 
bot = telebot.TeleBot('5475678962:AAFzRcJB8QLqo5DGEQETv-AcyddJ2Cw4300')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'WELCOME /help')

@bot.message_handler(commands=['calc'])
def calculation(message):
    msg = message.text.split(' ')
    try:
        bot.send_message(message.chat.id, compute.profit(msg[1:]))
    except IndexError:
        bot.send_message(message.chat.id, 'Input has to be 4 numbers')
          

@bot.message_handler(commands=['eth'])
def start_message(message):
    bot.send_message(message.chat.id, convert.eth(message.text.split(' ')))
        
#usd
@bot.message_handler(commands=['usd'])
def start_message(message):
    bot.send_message(message.chat.id, convert.usd(message.text.split(' ')))
    
#rub
@bot.message_handler(commands=['rub'])
def start_message(message):
    bot.send_message(message.chat.id, convert.rub(message.text.split(' ')))
        
#help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, help)  
            
#gas price        
@bot.message_handler(commands=['gas'])
def start_message(message):
    bot.send_message(message.chat.id, price.gas())
        
        
bot.polling(none_stop=True, interval=0)