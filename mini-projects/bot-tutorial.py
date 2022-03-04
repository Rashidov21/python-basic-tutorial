import telebot
from telebot import types
from firebase_python import db_get,db_set
from async_bot.config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def set_user_data_to_firebase(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton('Send my Contact \U0001F636', request_contact=True)
    markup.add(btn)
    # user_id = message.chat.id
    # text = message.text
    #
    # db_set("user",{"id":user_id,"text":text})
    bot.send_message(message.chat.id, "Send me  your Contact please.", reply_markup=markup, parse_mode='html')
    # print("bot create user id ")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call)
    print(call.data)
    bot.send_message(call.message.chat.id, f"dsdsdfs")
    
bot.infinity_polling()