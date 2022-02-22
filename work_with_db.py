#-*- coding: utf-8 -*-
import sqlite3
#


# songs.db
# con = sqlite3.connect("songs.db")
# cur = con.cursor()

# sql = """\
#     CREATE TABLE music(
#         song_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         song_name TEXT,
#         author TEXT
#     );
#     """
# sql = """\
#     INSERT INTO music(song_name,author)
#     VALUES("Faded","Alan Walker");
# """
# try:
#     cur.execute(sql)
# except sqlite3.DatabaseError as er:
#     # raise sqlite3.DatabaseError()
#     print(er)
# else:
#     print("Song is added.")
#     con.commit() # malumotlarni tasdiqlab saqlash
# cur.close()
# con.close()
#import sqlite3
# print(sqlite3.version) # 2.6
# agar db fayl bolsa unga boglanish bolmasa uni xosil qilish
# conn = sqlite3.connect("myDb.db")
# # db ustidan boshqaruv uchun cursor() metodiga murojaat qilinadi
# cur = conn.cursor()
# # sql = """\
# #     CREATE TABLE user(
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     email TEXT,
# #     password TEXT);
# # """
# sql = """\
#     INSERT INTO user(email)
#     VALUES('yoki@yoki.ru');
# """
# try:
#     cur.execute(sql)
# except sqlite3.Error as err:
#     print("Xatolik", err)
# else:
#     print("user TABLE siga yoki@yoki.ru emaili qoshildi")
#
# # db ustidan amallar bitganidan keyin u bilan aloqani uzamiz
# cur.close()
# conn.close()


# SQL  >> Structed Query Language
# Jadval korinishida info larni saqlash
# Create a new table >> CREATE TABLE <table name>(
#     Create a new column >> <column name> INTEGER,TEXT,REAL,BLOB,NULL
# )
# INTEGER >> int values
# TEXT >>  str values
# REAL >> float values
# BLOB >> binary values
# NULL >> null values

# malumot joylash
# INSERT INTO <table name>(
#     VALUES (value1, value2 ...)
# )
# Tanlash
# SELECT * FROM <table name>

# Tanlab ochirish
# DELETE FROM users WHERE name="Michael"

# Jadvalni ochirish
# DROP TABLE <table name>






















# import sqlite3
# con = sqlite3.connect("users.db")
# cur = con.cursor()
# sql = """\
#     CREATE TABLE users (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         email TEXT,
#         password TEXT
#         );
#     """
# try:
#     cur.execute(sql)
# except sqlite3.DatabaseError as err:
#     print("Error", err)
# else:
#     print("Congrats! user.db created and created users TABLE.")
# try:
#     sql = """\
#         INSERT INTO users (email, password)
#         VALUES ("yoki@meme.ru","qwerty")
#     """
#     cur.execute(sql)
# except sqlite3.DatabaseError as err:
#     print(err)
# else:
#     print("Created a new user data into users.db TABLE users")
# cur.close()
# con.close()
# input()


# from faker import Faker
#
# fake = Faker()
# con = sqlite3.connect("users.db")
# cur = con.cursor()
#
# for i in range(10):
#     name = fake.name().split(" ")[0]
#     surname = fake.name().split(" ")[1]
#
#     sql = f"""\
#         INSERT INTO users(name,surname)
#         VALUES('{name}','{surname}')
#     """
#     try:
#         cur.execute(sql)
#     except sqlite3.DatabaseError as e:
#         print(e)
#     else:
#         print("CREATE TABLE users")
#         con.commit()
# cur.close()
# con.close()