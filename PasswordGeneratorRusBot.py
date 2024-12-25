# import directories

from random import choice
import telebot
import pyperclip
from telebot import types

#token

bot =telebot.TeleBot("")

#password varible

password = ""

#function for start message

@bot.message_handler(commands=["start"])

def main(message):
    bot.send_message(message.chat.id,f"Приветствую , {message.from_user.first_name}.Я генератор паролей из 16 цифр!\nВот список всех моих команд 🔥\n/start - перезапуск бота\n/help - список всех моих команд\n/generate - сгенерировать пароль\n\nТакже вы можете написать id ,это выведет ваш текущий id\n\nЕсли вам не трудно,то вот моя ссылка на Github:\nhttps://github.com/vesel4akProjects")

#function for help message

@bot.message_handler(commands=["help"])

def help(message):
    bot.send_message(message.chat.id,"Вот список всех моих команд 🔥 \n/start - перезапуск бота\n/help - список всех моих команд \n/generate - сгенерировать пароль\n \nТакже вы можете написать id ,это выведет ваш текущий id\n\nЕсли вам не трудно,то вот моя ссылка на Github:\nhttps://github.com/vesel4akProjects")

#function for generating

@bot.message_handler(commands=["generate"])

def generate_password(message):
    variants =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"]
    while True:
        for i in range(16):
            global password

            #append variants

            numbers = choice(variants)
            password += numbers
        bot.send_message(message.chat.id,f"{message.from_user.first_name} , вот твой сгенерируемый пароль 👌 \n {password}")
        password =""
        return

#function for other commands

@bot.message_handler()
def info(message):
   if message.text.lower() =="id":
        bot.reply_to(message,f"ID:{message.from_user.id}")

#infunity polling

bot.infinity_polling()

