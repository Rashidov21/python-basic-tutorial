import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
TOKEN = ""
me = 0
# con = sqlite3.connect("users.db")
# cur = con.cursor()
#
# sql = """\
#     CREATE TABLE users(
#     firstname TEXT,
#     lastname TEXT)
# """
# try:
#     cur.execute(sql)
# except sqlite3.DatabaseError as er:
#     print(er)
# else:
#     con.commit()
#     cur.close()
#     con.close()



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(type(message.chat))
    id = message.chat.id
    fname = message.chat.first_name
    lname = message.chat.last_name
    print(fname)
    print(lname)
    # try:
    #     con = sqlite3.connect("users.db")
    #     cur = con.cursor()
    #     sql = f"""\
    #         INSERT INTO users(firstname, lastname)
    #         VALUES ('{fname}', '{lname}')
    #     """
    # except sqlite3.DatabaseError as er:
    #     print(er)
    # else:
    #     cur.execute(sql)
    #     con.commit()
    #     cur.close()
    #     con.close()


    # print(type(message))
    # print(dir(message))
    await message.reply(f"Hi! - {fname + ' ' + lname}\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['get'])
async def send_users(message: types.Message):
    u = []
    try:
        con = sqlite3.connect("users.db")
        cur = con.cursor()
            sql = """\
                    SELECT * FROM users;
                """
        for row in cur.execute(sql):
            u.append(row)
    except sqlite3.DatabaseError as er:
        print(er)
    else:
        print(u)


    await message.reply(f"All users")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)