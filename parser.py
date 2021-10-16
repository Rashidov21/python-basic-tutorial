import requests
import sqlite3
from bs4 import BeautifulSoup
import telebot
from telebot import types
group_id = 00000

bot = telebot.TeleBot("")

url = "https://yandex.uz/"
page = requests.get(url)
# print(page.status_code) # 200
soup = BeautifulSoup(page.content, "html.parser")
# print(soup.text) # full html page text
location = soup.find("span", class_="geolink__reg").text
date = soup.find("span", class_="datetime__date").text
temp = soup.find("div", class_="weather__temp").text

course = soup.findAll("span", class_="inline-stocks__value_inner")
l = []
for i in course:
    l.append(i.text)

keyboard = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text="Ob havo", callback_data="weather")
btn2 = types.InlineKeyboardButton(text="Valyuta kurslari", callback_data="cash")
keyboard.add(btn,btn2)

@bot.message_handler(commands=["start"])
def send_data(message):
    text = "Assalomu alaykum! \nNimani bilmoqchisiz iltimos tanlang..."
    bot.send_message(message.chat.id,text, reply_markup=keyboard )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "cash":
        user = call.message.from_user.username
        text = f"USD: {l[0]}\nEURO: {l[1]}\nRUB: {l[2]}"
        sql = f"""\
            INSERT INTO userdata(username,data)
            VALUES ('{user}','{text}')
        """
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        try:
            cur.execute(sql)
        except sqlite3.DatabaseError as err:
            bot.reply_to(call.message.chat.id, f"Uzr xatolik yuz berdi : {err}")
        else:
            con.commit()
            cur.close()
            con.close()
        bot.send_message(call.message.chat.id, text)
    if call.data == "weather":
        text = f"Bugun - {date} \n Havo - {temp} "
        bot.send_message(call.message.chat.id, text)

# @bot.message_handler(commands=["get"])
# def send_all_data(message):
#     con = sqlite3.connect("database.db")
#     cur = con.cursor()
#     sql = """\
#         SELECT * from userdata
#     """
#     cur.execute(sql)
#     data = cur.fetchall()
#     if len(data) > 0:
#         for i in data:
#             bot.send_message(message.chat.id, f"Username: {i[0]}, Data: {i[1]}")
#     cur.close()
#     con.close()



bot.polling(none_stop=True)
# month = soup.find("span", class_="datetime__month").text
# print(location.text) # geolocation is find | Toshkent
# task 1
# input: a ab cde ee
# output:abcde 3
# task 2
# input: -5 , 12 , % 3 == 0 >>  6: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12
# output: 4.5
# task 3
# Sample Input: txt file
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb