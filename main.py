import telebot
from telebot import types

token = "" # сюда писать токен бота
bot = telebot.TeleBot(token) # объект для самого бота

@bot.message_handler(commands=['start'])
# декоратор реакции на функцию обязателен
def start(message):
    # Функция которую обертывает декоратор
	bot.send_message(message.from_user.id, "{0}, рад приветствовать Вас".format(message.from_user.first_name)) # это пишется в одну строчку

@bot.message_handler(content_types=['text'])
def getMessages(message):
	if message.text == "Aboba":
		bot.send_message(message.from_user.id, "Aoma")
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Угу")
	if message.text == "Пока":
		bot.send_message(message.from_user.id, "Пока :(")

bot.polling()