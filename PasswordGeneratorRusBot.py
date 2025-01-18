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
    bot.send_message(message.chat.id ,f"Greetings, {message.from_user.first_name}.I'm a 16-digit password generator!This is a list of all my commands.\n/start - restart the bot\n/help - a list of all my commands.\n/generate - generate a password.\n\You can also write an id, this will display your current id.\n\If you don't mind, here is my link to Github:\nhttps://github.com/vesel4akProjects")

#function for help message

@bot.message_handler(commands=["help"])

def help(message):
    bot.send_message(message.chat.id "Вот список всех моих команд 🔥/start - перезапустить бота\n/help - список всех моих команд \n/generate - сгенерировать пароль\n\Вы также можете ввести id, это выведет ваш текущий id\nЕсли вам не сложно, то вот моя ссылка на Github:https://github.com/vesel4akProjects")

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
        bot.send_message(message.chat.id,f " {message.from_user. first_name} , here is your generated password 👌\n {password}")
        password =""
        return

#function for other commands

@bot.message_handler()
def info(message):
   if message.text.lower() =="id":
        bot.reply_to(message,f"ID:{message.from_user.id}")

#infunity polling

bot.infinity_polling()

