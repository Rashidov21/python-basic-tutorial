import telebot
from firebase_python import db_get,db_set
from async_bot.config import TOKEN

bot = telebot.TeleBot(TOKEN)
bot.send_message(668618297, "qale")