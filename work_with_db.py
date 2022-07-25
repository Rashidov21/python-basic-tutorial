import sqlite3

# conn = sqlite3.connect('users.db')  # check_same_thread=False
# # conn = sqlite3.connect(:memory:) # operativ xotiradan DB sifatida foydalanish
# customers = [
#     ('00005', 'Stephanie', 'Stewart', '12'),
#     ('00006', 'Sincere', 'Sherman', '30'),
#     ('00007', 'Sidney', 'Horn', '40'),
#     ('00008', 'Litzy', 'Yates', '56'),
# ]
# cur = conn.cursor()
# cur - DB ni boshqarish uchun kursor
# table ochish
# yangi narsa yozish
# o'chirish
# db ni tozalash kabi ishlar cursor orqali qilinadi
# sql = """CREATE TABLE users(
#    userid INT PRIMARY KEY,
#    name TEXT,
#    surname TEXT,
#    age TEXT);
# """
# cur.execute(sql)  # cursorga sql buyruqlarini berish
# conn.commit()  # commit bu o'zgarishlarni tasdiqlash
# sql = """INSERT INTO users(userid, name, surname, age)
#    VALUES('00001', 'Alex', 'Smith', '23');"""
# cur.execute(sql)
# conn.commit()

# yangi table qo'shish
# sql = """CREATE TABLE songs(
#     singer TEXT,
#     song TEXT,
#     rating INT);"""

# try:
#     cur.execute(sql)
# except sqlite3.DatabaseError as er:
#     print("Wrong !", er)
# else:
#     conn.commit()

# try:
#     for user in customers:
#         sql = f"""INSERT INTO users(userid,name,surname,age)
#         VALUES('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}');"""
#         cur.execute(sql)
# except sqlite3.DatabaseError as er:
#     print("Wrong ! \n", er)
# else:
#     conn.commit()
#     conn.close()  # DB bilan boglanishni yopadi
# sql = "SELECT * FROM users;"  # users table dan hamma yozuvlarni belgilash

# cur.execute(sql)
# one_results = cur.fetchone()  # 1-sini olish
# many_results = cur.fetchmany(2)  # 2 tasini olish
# all_results = cur.fetchall()  # hammasini olish
# print(one_results)
# (1, 'Alex', 'Smith', '23')
# print(many_results)
# [(5, 'Stephanie', 'Stewart', '12'), (6, 'Sincere', 'Sherman', '30')]
# print(all_results)
# [(7, 'Sidney', 'Horn', '40'), (8, 'Litzy', 'Yates', '56')]

# sql = cur.execute("SELECT * FROM users WHERE userid = 7")
# data = sql.fetchone()
# print(data)  # (7, 'Sidney', 'Horn', '40')
# conn.close()
# cur.execute("DELETE FROM users WHERE name='Alex';")  # DB dan narsa o'chirish
# conn.commit()
# conn.close()
# task 1
# Ushbu ma'lumotlardan foydalanib personal.db ni hosil qilung
# 02 Will worker
# 03 John worker
# 04 Paul staff
# 05 Same geddir
# # personal :
# #     id INT
# #     name TEXT
# #     position TEXT
