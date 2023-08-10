# -*- coding: utf-8 -*-
# import sqlite3

# conn = sqlite3.connect("./test.db", check_same_thread=False)

# print(dir(conn))
# cur = conn.cursor() # db ni boshqarish uchun kursor

# sql = """CREATE TABLE students( \
#     id INTEGER,
#     name TEXT,
#     age INTEGER,
#     country TEXT
#     );"""
# sql = """INSERT INTO students
#         VALUES(5,'Jason Statham',45,'UK');
# """
# cur.execute() # sql buyruqlarini yozish va amalga oshirish uchun metod 


# sql = """SELECT name , age FROM students;"""
# sql = """SELECT * FROM students WHERE age > 50;"""
# try:
#     data = cur.execute(sql)
#     print(data.fetchall()) # sorovdagi barcha yozuvlarni olish
# except sqlite3.DatabaseError as er:
#     print(er)
# else:
#     conn.commit() # o'zgarishlarni tasdiqlash
#     conn.close() # db boglanishni yopish
#     print("Success !")

